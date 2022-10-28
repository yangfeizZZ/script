with open("test.txt") as f,open("out.txt","w") as fo:
    for line in f.readlines():
        columns = line.split("\t")
        name = columns[0]
        new_name = name.split(".")[0]
        new_columns = [new_name,columns[1]]
        new_line = "\t".join(new_columns)
        fo.write(new_line)


'''
import pandas as pd

in_file = "./test.txt"
out_file = "out.txt"

df = pd.read_csv(in_file, sep="\t", header=None)
df.iloc[:, 1] = df.iloc[:, 1].str.replace("\..*", "")
df.to_csv(out_file, sep="\t")
'''