"""User input prompt example"""
# input_ = input("Provide number: ")
# print(f"Your number: {input_}")


"""System argument values provided with command line interface CLI"""
import sys

args = sys.argv

"""Enviromental variables input args"""
import os

# env_args = [item for item in os.environ]
env_var = os.getenv("dupa", None)
env_var2 = os.getenv("dupa1", "brak zmiennej")
os.environ["dupa1"] = "1234"
env_var3 = os.getenv("dupa1", "brak zmiennej")
