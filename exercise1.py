#Use a list of names

names = ["Jennifer","Rose","Alexandra","Margot",
         "Max","Cody","Taylor","Drake","Joe"]

max_length = -1
max_name = None
for name in names:
    # find the name with the maximum length
    if len(name) > max_length:
        max_length = len(name)
        max_name = name
print(max_name)