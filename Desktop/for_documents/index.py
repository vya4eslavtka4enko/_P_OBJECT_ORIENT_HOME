import os
import re
from os import walk

arr_dir  = os.listdir()
arr_dir = [d for d in os.listdir() if not d.startswith('.')]
# print(arr_dir)

# cwd = os.getcwd()
# print(cwd)


def through_the_directory():
    for file in  os.listdir(os.getcwd()):
        # print(file)
        if os.path.isdir(file):
            os.chdir(os.path.abspath(file))
            for file_txt in os.listdir():
                # print(file_txt)
                f = open(file_txt,"r")
                content = f.read()
                pattern = r'\d{3}-\d{3}-\d{4}'
                if re.search(pattern,content):
                    
                    return re.search(pattern,content)
                else:
                    print(os.getcwd())
                    os.chdir('./')
                
                #     # os.chdir("../")
                #     print(os.getcwd())
                # with open(file_txt,'r') as file:
                #     content = file.read()
                #     pattern = re.search(r"\d\d\d-\d\d\d-\d\d\d\d",content)
                #     print(pattern)
                #     os.chdir("../")
                #     print(os.getcwd())
                    
                          
through_the_directory()
