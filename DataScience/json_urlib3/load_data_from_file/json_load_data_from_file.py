"""
This is python3 example for json object manipulation
"""
# JSON
# import JavaScript object notation manipulation library 
import json


# open file
with open("my_data.json") as my_file:
    my_data = json.load(my_file)

print( "my json data ")
print(my_data)

