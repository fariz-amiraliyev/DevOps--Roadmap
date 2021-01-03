import os

print(f"MY_VAR: {os.getenv('MY_VAR', 'default_value')}")

os.putenv("PUT_VAR", "testing putenv")
os.environ["SET_VAR"] = "Direct Assignment"

print(f"PUT_VAR via getenv: {os.getenv('PUT_VAR')}")

try:
    print(f"PUT_VAR via environ: {os.environ['PUT_VAR']}")
except KeyError:
    print("PUT_VAR not in os.environ")

print(f"SET_VAR via getenv: {os.getenv('SET_VAR')}")

try:
    print(f"SET_VAR via environ: {os.environ['SET_VAR']}")
except KeyError:
    print("SET_VAR not in os.environ")
