from pydoc import plain
from re import A, X
from threading import local
import math
from turtle import pos, position
import sys

file = sys.argv[1]

chr_size = {
    "chr1" : "249250621", "chr2" : "243199373", "chr3" : "198022430", "chr4" : "191154276", "chr5" : "180915260",
    "chr6" : "171115067", "chr7" : "159138663", "chr8" : "146364022", "chr9" : "141213431", "chr10" : "135534747",
    "chr11" : "135006516", "chr12" : "133851895", "chr13" : "115169878", "chr14" : "107349540", "chr15" : "102531392",
    "chr16" : "90354753", "chr17" : "81195210", "chr18" : "78077248", "chr19" : "59128983", "chr20" : "63025520",
    "chr21" : "48129895", "chr22" : "51304566", "chrX" : "155270560","chrY" : "59373566"
}
"""
chr_size = {
    "chr1" : "195471971", "chr2" : "182113224", "chr3" : "160039680", "chr4" : "156508116", "chr5" : "151834684",
    "chr6" : "149736546", "chr7" : "145441459", "chr8" : "129401213", "chr9" : "124595110", "chr10" : "130694993",
    "chr11" : "122082543", "chr12" : "120129022", "chr13" : "120421639", "chr14" : "124902244", "chr15" : "104043685",
    "chr16" : "98207768", "chr17" : "94987271", "chr18" : "90702639", "chr19" : "61431566",  "chrX" : "171031299","chrY" : "91744698"
}
"""
bin_size = 5000
ratio = 0

while ratio <= 1:

    chr_num = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","X","Y"]
    #chr_num = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","X","Y"]
    d = {}
    for i in chr_num:
        locals()["chr" + i + "_num" + "_size"] = math.ceil(int(chr_size["chr"+i])/bin_size)
        list1 = [0 for key in range(1,math.ceil(int(chr_size["chr"+i])/bin_size) +2 )]
        d["chr" + i ] = list1


    with open(file) as line1:
        for line2 in line1.readlines():
            line2 = line2.split("\t")
            
            position1_chr = line2[1]
            position1_num = line2[2]

            position2_chr = line2[3]
            position2_num = line2[4]

            chrs = ["chr" + k for k in chr_num]
            if (position1_chr not in chrs) or (position2_chr not in chrs):
                continue
            
            position1_num_bin = math.ceil(int(position1_num)/bin_size)
            position2_num_bin = math.ceil(int(position2_num)/bin_size)
            
            d[position1_chr][position1_num_bin] = d[position1_chr][position1_num_bin] +1
            d[position2_chr][position2_num_bin] = d[position2_chr][position2_num_bin] +1

    all_chr_bin = 0
    all_chr_bin_1000 = 0

    for j in chr_num:
        a = math.ceil(int(chr_size["chr"+j])/bin_size)
        b = len([v for v in d["chr" + j] if v >= 100])
        all_chr_bin = all_chr_bin + a
        all_chr_bin_1000 = all_chr_bin_1000 + b

    ratio = all_chr_bin_1000/all_chr_bin
    #print(all_chr_bin_1000,all_chr_bin)
    #print(ratio)
    
    if ratio >= 0.5:
        print(bin_size)
        break
    bin_size = bin_size + 1000