import os
import re

def search(file,pattern= r'\d{3}-\d{3}-\d{4}'):
    # f = open(file,'r')
    # text = f.read()
    
    # if re.search(pattern,text):
    #     return re.search(pattern,text)
    # else:
    #     return ''
    pass
    


result = []
print(os.getcwd())
for folder , sub_folders , files in os.walk(os.getcwd()+"/extracted_content"):
    print(folder)
    for f in files:
        full_path = folder+'/'+ f
        print(full_path)
        result.append(search(full_path)) 
        
        
        
for r in result:
    if r != '':
        print(r.group())

print(result)