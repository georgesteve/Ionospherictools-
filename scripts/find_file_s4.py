import os

def find_file(name,path=os.getcwd()):
    for root, dirs, files in os.walk(path):
        #print(root)
        if name in files:
            #return os.path.join(root, name)
            return name

#if find_file('areq0010.21d.gz')== None
