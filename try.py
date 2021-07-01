from PIL import Image
import os
import glob
import subprocess

num_rows = 0
for row in open("sample-quotes-short.csv"):
    num_rows += 1
print(num_rows)

# Reading the file
with open("sample-quotes-short.csv") as iostream:
    content = iostream.read()
print ("fff")
cwd = os.getcwd()
print (cwd)
files = glob.glob(cwd + '\\input\\*')
print (files)
for file in files:
    print (file)
    im = Image.open(file)
    width, height = im.size
    size = round(width/10*7) 
    print (width, height)
    counter = 0
    for line in content.split("\n"):
        if counter == num_rows:
            break
        text, author, tags = line.split("\t")
        print (text)
        
        imgout = file[:-4]+'_synt' + str(text[:10])+ str(author[:10]) + '.jpg'
        print (imgout)
         
        toeval =f'''magick -background transparent -fill white -gravity center -size {size} -pointsize 30 caption:"{text}" "{file}" +swap -gravity center -composite "{imgout}" '''
        
        print (toeval)
        print (len(line.split("\t")))
        if len(line.split("\t")) == 3:
            subprocess.call(toeval, shell=True)
            counter += 1
            print (num_rows)
            print (counter)