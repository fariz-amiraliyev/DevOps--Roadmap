1. open and print yaml file


import yaml
with open("items.yaml") as f:
    txt=yaml.full_load(f)
for x, y in txt.items():
    print(x,y)

2. write to Yaml file:
import yaml

dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

with open(r'E:\data\store_file.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)

3.
