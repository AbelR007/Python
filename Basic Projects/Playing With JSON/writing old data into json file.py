import json # Import JSON, its necessary

file = open("newfile.json","a") # Opening the json file in append mode.

# You need to load the JSON file before to dump JSON data
x = json.load(file)

# NOTE : You can't use file.append() to append data. You need to index data into dictionaries.
# A example of appending data into a dict is shown below
x['newdata'] = {
    "author" : "Its You !",
    "title" : "More advantages of JSON",
    "desc" : "You can use JSON to append new data into old JSON files!"
}

y = json.dump(x, file, indent=2) # Dumping data into json file, Indent is used to make it more readable
file.close() # Closing files is important for data security

# CREATED with ❤️ by AbelR007
