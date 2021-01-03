# find_secrets_with_aws.py

# this is the script used to find the services in EKS with aws secrets: 
#
from dataclasses import dataclass
import re
from typing import List
import yaml
from subprocess import run
import glob
​
​
@dataclass
class ServiceSecrets:
    name: str
    path: str
    keys: List[str]
​
    @property
    def has_aws_credentials(self):
        return "AWS_ACCESS_KEY_ID" in self.keys
​
    @staticmethod
    def name_from_path(path):
        match = re.search(r".*/(.*).yml", path)
        return match.group(1)
​
    @staticmethod
    def build_service_secret(**kargs):
        return ServiceSecrets(
            name=ServiceSecrets.name_from_path(kargs["path"]), **kargs
        )
​
​
def get_secrets_keys(result):
    secrets_dict = yaml.safe_load(result.stdout)
    return secrets_dict.keys()
​
​
def load_secrets(files):
    secrets_res = []
    for file_path in files:
        result = run(
            f"ansible-vault decrypt --output - {file_path}".split(), capture_output=True
        )
        ks = get_secrets_keys(result)
        secrets_res.append(ServiceSecrets.build_service_secret(path=file_path, keys=ks))
    return secrets_res
​
​
files = glob.glob("roles/vault-populate/files/slo-dev/secret/*.yml")
secrets_res = load_secrets(files)
secrets_with_aws_credentials = filter(lambda x: x.has_aws_credentials, secrets_res)
for secret in secrets_with_aws_credentials:
    print(secret.name)
    # print(secret)
