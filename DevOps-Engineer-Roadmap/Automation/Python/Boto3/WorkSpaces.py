import logging
import boto3
from ldap3 import Server, Connection, Tls, NTLM, ALL

logger = logging.getLogger()
logger.setLevel(logging.INFO)

secrets = boto3.client('secretsmanager')
workspaces = boto3.client('workspaces')

def loadMoreResults(NextToken, Directory_Id):
    workspace_users = {}
    while NextToken:
        response = workspaces.describe_workspaces(DirectoryId=Directory_Id, NextToken=NextToken)
        for workspace in response['Workspaces']:
            if not workspace['State'] == 'TERMINATING':
                workspace_users[workspace['UserName']] = workspace['WorkspaceId']
        NextToken = response.get('NextToken')
    return workspace_users

def lambda_handler(event, context):
    #Setup variables
    LDAP_SERVER = event['LDAP_SERVER']
    LDAP_USER = event['LDAP_USER']
    GROUP_FILTER = event['GROUP_FILTER']
    USER_FILTER = event['USER_FILTER']
    SECRET_NAME = event['SECRET_NAME']
    WORKSPACE_GROUP_FRIENDLY_NAME = event['WORKSPACE_GROUP_FRIENDLY_NAME']
    WORKSPACE_GROUP_DN = event['WORKSPACE_GROUP_DN']
    Directory_Id = event['Directory_Id']
    Bundle_Id = event['Bundle_Id']
    #Get LDAP bind password from Secrect Store
    LDAP_PASSWORD = (secrets.get_secret_value(SecretId=SECRET_NAME)).get('SecretString')

    #Create LDAP Bind
    server = Server(LDAP_SERVER, port=636, use_ssl=True, tls=Tls(), get_info=ALL)
    conn = Connection(server, user=LDAP_USER, password=LDAP_PASSWORD, authentication=NTLM, auto_bind=True)

    #Get defined group members and store
    conn.search(WORKSPACE_GROUP_DN, GROUP_FILTER, attributes=['member'])
    group_members = conn.entries[0].member

    #Look up each member of defined group and add a dictionary to the list for each user with an email address
    workspace_group_users = {}
    for user_DN in group_members:
        conn.search(user_DN, USER_FILTER, attributes=['mail', 'sAMAccountName'])
        if conn.entries[0].mail[:7]:
            workspace_group_users[conn.entries[0].sAMAccountName[:17][0]] = conn.entries[0].mail[:7][0]

    #Get current list of WorkSpaces in the defined directory
    all_workspaces = workspaces.describe_workspaces(DirectoryId=Directory_Id)

    #Build dictionary of sAMAccountNames and WorkspaceIds
    current_workspace_users = {}
    for workspace in all_workspaces['Workspaces']:
        if not workspace['State'] == 'TERMINATING':
            current_workspace_users[workspace['UserName']] = workspace['WorkspaceId']
    if all_workspaces.get('NextToken'):
        loadmore_Workspaces_List = loadMoreResults(all_workspaces['NextToken'], Directory_Id)
        current_workspace_users.update(loadmore_Workspaces_List)

    #Check that every user in defined group as a WorkSpace, else add them to the provision list
    provision_sAMAccountName = []
    for groupuser in workspace_group_users.keys():
        if not groupuser in current_workspace_users.keys():
            provision_sAMAccountName.append(groupuser)

    #check that every WorkSpace user is in the defined group, else add them to the termination list
    termination_sAMAccountName = []
    for workspaceuser in current_workspace_users.keys():
        if not workspaceuser in workspace_group_users.keys():
            termination_sAMAccountName.append(workspaceuser)

    #create provisioning task list
    provision = []
    provision_count = 1
    for provision_user in provision_sAMAccountName:
        appendData = {
                'DirectoryId': Directory_Id,
                'UserName': provision_user,
                'BundleId': Bundle_Id,
                'UserVolumeEncryptionEnabled': False,
                'RootVolumeEncryptionEnabled': False,
                'WorkspaceProperties': event['WorkSpace_Properties'],
                'Tags': [
                    {
                        'Key': 'Automation',
                        'Value': 'Managed'
                    },
                    {
                        'Key': 'DirectoryGroup',
                        'Value': WORKSPACE_GROUP_FRIENDLY_NAME
                    }
                ]
            }
        provision.append(dict(appendData))
        if provision_count > 24:
            break
        else:
            provision_count = provision_count + 1

    #create termination task list
    terminate = []
    terminate_count = 1
    for terminate_user in termination_sAMAccountName:
        tags = (workspaces.describe_tags(ResourceId=current_workspace_users[terminate_user]))['TagList']
        if {'Key': 'Automation', 'Value': 'Managed'} in tags:
            if {'Key': 'DirectoryGroup', 'Value': WORKSPACE_GROUP_FRIENDLY_NAME} in tags:
                appendData = {'WorkspaceId': current_workspace_users[terminate_user]}
                terminate.append(dict(appendData))
                if terminate_count > 24:
                    break
                else:
                    terminate_count = terminate_count + 1
    #terminate WorkSpaces for non-group members
    if terminate:
        termination = workspaces.terminate_workspaces(TerminateWorkspaceRequests=terminate)
        print('Created termination task for: ' + str(terminate))
        if termination['FailedRequests']:
            print('Failed to terminate: ' + termination['FailedRequests'])
    else:
        print('No WorkSpaces to terminate at this time.')

    #Create WorkSpaces for members without existing WorkSpaces
    if provision:
        creation = workspaces.create_workspaces(Workspaces=provision)
        print('Successfully created provisioning requests for: ' + str(creation['PendingRequests']))
        if creation['FailedRequests']:
            print('Failed to create provisioning requests for: ' + str(creation['FailedRequests']))
    else:
        print('No WorkSpaces to create at this time.')


        
