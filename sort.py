import os
import shutil
def sortfiles():
    files= os.listdir("C:/Users/igors/OneDrive/Desktop/102-pro/notsorted")
    for i in range(0,len(files)):
        whatfile= "C:/Users/igors/OneDrive/Desktop/102-pro/notsorted/" + files[i]
        name, extension = os.path.splitext(whatfile)
        if(extension==".pfd"):
            shutil.move(whatfile,"C:/Users/igors/OneDrive/Desktop/102-pro/sorted")
sortfiles()