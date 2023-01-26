import os
import shutil

from_dir = "c:/Users/Admin/Downloads"
to_dir = "c:/User/Admin/Desktop/Document_Files"
list_of_files = os.listdir(from_dir)
#print (list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    
    if extension == '':
        continue

    if extension in ['.gif', '.png', '.jpeg', '.jpg']:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Images"
        path3 = to_dir + "/" + "Images" + "/" + file_name

       # print(path1)
       # print(path2)

        if os.path.exists(path2):
            print("Moving " + file_name + "...")
            shutil.move(path1,path3)
        else:
            print("Folder Doesn't exists, So creating new folder...")
            os.makedirs(path2)
            print("Folder created, moving " + file_name + "...")
            shutil.move(path1,path3)