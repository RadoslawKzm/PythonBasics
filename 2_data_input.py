"""User input prompt example"""
# input_ = input("Provide number: ")
# print(f"Your number: {input_}")

"""System argument values provided with command line interface CLI"""
import sys

args = sys.argv
print(f"{args}")

"""Enviromental variables input args"""
import os

# env_args = [item for item in os.environ]
env_var = os.getenv("dupa")
env_var2 = os.getenv("dupa1")
# os.environ["dupa1"] = "1234"
env_var3 = os.getenv("dupa2")

vars = (env_var, env_var2, env_var3)
vars_dict = {"env_var": env_var, "env_var2": env_var2, "env_var3": env_var3}

# if not env_var:
#     raise KeyError("Missing env var")
#
# if not env_var2:
#     raise KeyError("Missing env var")
#
# if not env_var3:
#     raise KeyError("Missing env var")

# if not all(vars):
#     raise KeyError("Missing env var")

for var_name, var in vars_dict.items():
    if not var:
        raise KeyError(f"Missing {var_name}")
