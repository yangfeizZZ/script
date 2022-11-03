import os
path = "./"


with open("./tmpt.txt") as f:
    line1 = f.read()

with open("index.txt") as foo:
    for i in foo.readlines():
        i = i.strip()
        print(i)
        #os.chdir("./" + i)
        user_config = line1.format(input_dir= ""i)
        with open(i+".txt","w") as fo :
            fo.write(user_config)
            fo.close()
        #os.system()
        #os.chdir("../")