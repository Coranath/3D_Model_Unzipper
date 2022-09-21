import os

ls = os.listdir('C:Users/ASRock_PC/Downloads')

ls = [i for i in ls if '.zip' in i]

print(ls)