import os

for folderName, subFolderNames, fileNames in os.walk('/Users/rray/GitHub'):
    print('The current folder is : ' + folderName)

    for subFolderName in subFolderNames:
        print('The subfolder of ' + folderName + ' : ' + subFolderName)

    for fileName in fileNames:
        print('The filename inside ' + folderName + ' : ' + fileName)

    print('')
