https://www.w3resource.com/python-exercises/python-json-index.php

1. Write a Python program to convert JSON data to Python object.
import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"])


2.Write a Python program to convert Python object to JSON data.

import json
# a Python object (dict):
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6
}
print(type(python_obj))
# convert into JSON:
j_data = json.dumps(python_obj)

3. Write a Python program to convert Python objects into JSON strings. Print all the values.
import json
python_dict =  {"name": "David", "age": 6, "class":"I"}
python_list =  ["Red", "Green", "Black"]
python_str =  "Python Json"
python_int =  (1234)
python_float =  (21.34)
python_T =  (True)
python_F =  (False)
python_N =  (None)

json_dict = json.dumps(python_dict)
json_list = json.dumps(python_list)
json_str = json.dumps(python_str)
json_num1 = json.dumps(python_int)
json_num2 = json.dumps(python_float)
json_t = json.dumps(python_T)
json_f = json.dumps(python_F)
json_n = json.dumps(python_N)
