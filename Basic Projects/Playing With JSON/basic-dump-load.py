import json # Import JSON, its necessary

file = open("newfile.json","r") # Opening the json file in read mode.

# You can dump the below dictionary easily.
x = {
    "newrarity": {
        "author":"AbelR#0070",
        "title": "Rarities",
        "desc": "Rarity is a count that indicates a slug species level of rareness"
    }
}

y = json.dump(x, file, indent=2) # Dumping data into json file, Indent is used to make it more readable
file.close() # Closing files is important for data security
# DONE

xy = json.load(file)
print(xy)
xy['Newtag'] = {
    "author" : "Always ME",
    "title":"Nocasd",
    "desc":"Cmoadas"
}
print(xy)
file.close()
nfile = open("hi.json","w")
nfile.close()



"""
print(y)
l = []
for i in y:
    print(i)
    l.append(i)

n = "rarity"
if n in l:
    li = y[n]
    print("Author :",li['author'])

print(l)
"""
