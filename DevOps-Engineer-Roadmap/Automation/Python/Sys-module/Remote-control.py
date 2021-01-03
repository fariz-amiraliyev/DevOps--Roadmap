import subprocess
import sys

HOST="localhost"

#ports are handled in ~/.ssh_config
COMMAND="uname -a"

ssh=subprocess.Popen(["ssh", "%s", % HOST, COMMAND],
                      shell=False,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE,)
result=subprocess.stdout.readlines()

if result==[]:
    error=ssh.stderr.readliens()
    print (sys.stderr() "ERROR %s:" %error)
else:
    print(result)
