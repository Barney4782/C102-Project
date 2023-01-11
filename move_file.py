import os
import shutil

from_dir="/Users/Arnel/Downloads/Document_Files"
to_dir="/Users/Arnel/Downloads"

listOfFiles= os.listdir(from_dir)
#print(listOfFiles)

for fileImage in listOfFiles:
    name, extension = os.path.splitext(fileImage)

    if extension in [".jpg", 'jfif', ".gif", ".png", ".jpeg"]:

        path1 = from_dir + "/" + fileImage
        path2 = to_dir + "/" + "ImageFiles2"
        path3 = to_dir + "/" + "ImageFiles2" + "/" + fileImage

        if os.path.exists(path2):
            print("Moving " + fileImage)
            shutil.move(path1, path3)
        else:
            print("Making Directory")
            os.makedirs(path2)
            print("Moving " + fileImage)
            shutil.move(path1, path3)