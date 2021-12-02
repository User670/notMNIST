import os
import PIL
from PIL import Image
import json

num_imgs={}
list_folders=["A","B","C","D","E","F","G","H","I","J"]

for folder in list_folders:
    t=b""
    list_files=os.listdir("./"+folder)
    num_files=len(list_files)
    print("Folder "+folder+" has "+str(num_files)+" images.")
    processed_count=0
    f=open(folder+".bin","wb")
    for file in list_files:
        try:
            img=Image.open("./"+folder+"/"+file)
        except PIL.UnidentifiedImageError as error:
            print("bad file: "+folder+"/"+file)
            num_files-=1
            continue
        f.write(bytes(list(img.getdata())))
        processed_count+=1
        if processed_count%1000==0:
            print(folder+": "+str(processed_count)+"/"+str(num_files))
    
    num_imgs[folder]=num_files
    f.close()

j=json.dumps(num_imgs)
f=open("number of data in each file.json","w")
f.write(j)
f.close()