import os
# specify the directory path
path = "/"   # change this to your directory

# get list of files and directories
contents = os.listdir(path)

# print each item
print("Contents of directory:")
for item in contents:
    print(item)