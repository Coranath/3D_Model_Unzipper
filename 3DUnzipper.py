import os
from zipfile import ZipFile

#TODO Add the ability to run in the background and scan the downloads folder occasionally (or even better to listen for updates to the downloads folder) then run if changes
# have been made!

downloads = 'C:Users/ASRock_PC/Downloads'

ls = os.listdir(downloads)

ls = [i for i in ls if '.zip' in i]

deleteList = []

for zip in ls:
    is3D = False
    with ZipFile(downloads+'/'+zip, 'r') as curr:
        for i in curr.namelist():
            if '.stl' in i.lower() or '.obj' in i.lower():
                is3D = True
        newName = zip.strip('1234567890')[1:-4] #I know that aint pretty but I gotta do it to remove the underscore after the numbers, then to exclude the '.zip' from the end
        if is3D == True:
            print(f'{zip} contained 3D models, extracting to Desktop/3D Printing now!')
            curr.extractall(path=f'C:Users/ASRock_PC/Desktop/3D Printing/{newName}')
            print(f'Finished extracting, (Time elapsed?) moving to next archive')
            deleteList.append(zip)

for file in deleteList:
    os.remove(f'{downloads}/{file}')


