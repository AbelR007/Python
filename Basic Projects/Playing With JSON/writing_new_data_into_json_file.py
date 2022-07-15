import json # Import JSON, its necessary

file = open("newfile.json","r") # Opening the json file in read mode.

# You can dump the below dictionary easily.
x = {
    "data": {
        "author":"AbelR#0070",
        "title": "JSON",
        "desc": "JSONs works as a database and can help you store data into files. They are easy to handle."
    }
}

y = json.dump(x, file, indent=2) # Dumping data into json file, Indent is used to make it more readable
file.close() # Closing files is important for data security

# CREATED with ❤️ by AbelR007
