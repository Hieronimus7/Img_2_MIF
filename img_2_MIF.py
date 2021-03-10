import os
from PIL import Image

im = Image.open("../Image.png")


pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]
W,H = im.size
rgbVals = [""]*len(pix_val)

for x in range(0,len(pix_val)):
    temp = bin(0)
    for t in range(0,3):
        if t == 2:
            temp = bin((int(temp[2:],2)<<2) + (int(pix_val[x][t])>>6))
        else:
            temp = bin((int(temp[2:],2)<<3) + (int(pix_val[x][t])>>5))
    rgbVals[x] = rgbVals[x] + hex(int(temp[2:],2))[2:]

f = open("Image.mif","w+")
f.write("DEPTH = " + str(len(pix_val)) + ";\n")
f.write("WIDTH = " + str(8) + ";\n\n")
f.write("ADDRESS_RADIX = HEX;\n")
f.write("DATA_RADIX = HEX;\n")

f.write("CONTENT\nBEGIN\n")
for x in range(0,len(pix_val)):
    f.write(str(hex(x)[2:]).upper() +"    :   " + str(rgbVals[x]).upper() + ";\n")
f.write("END;")
f.close()
