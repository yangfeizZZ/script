with open("test.txt") as f,open("out.txt","w") as fo:
    for line in f.readlines():
        columns = line.split("\t")
        name = columns[0]
        new_name = name.split(".")[0]
        new_columns = [new_name,columns[1]]
        new_line = "\t".join(new_columns)
        fo.write(new_line)
