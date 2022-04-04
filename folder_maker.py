import os
 
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"\n{directory} creation successful\n")
    except OSError:
        print ('Error: Creating directory. ' +  directory)

cwd = os.getcwd()

createFolder(cwd+'/test')

st_idx = 1 # starting index

while True:
    tit = input("\nEnter title for folder: ")
    if not tit: break
    nam = "0"+str(st_idx)+" "+tit if st_idx<10 else str(st_idx)+" "+tit
    createFolder(nam)
    st_idx += 1
    
