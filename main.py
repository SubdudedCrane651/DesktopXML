import xml.etree.ElementTree as gfg 
from bs4 import BeautifulSoup
import os
  
# Folder Path
#path = "/home/richard/Documents/sambashare/DesktopBackground/"
path = "/home/richard/Documents/TP-LINK512/DesktopBackground/"

os.system('clear')

global dirname
dirname=""
dirname= input("Enter Directory: ")
global theme
theme = input("Enter Theme name :")

images={}
count=0

path=path+dirname+"/"

# Change the directory
os.chdir(path)

for file in os.listdir():
    images[count]=file
    count=count+1
print(images)

def GenerateXML(fileName,images) :
    count=0  
    root = gfg.Element("background")

    for image in images:  
        m1 = gfg.Element("static")
        root.append (m1)
        
        b1 = gfg.SubElement(m1, "duration")
        b1.text = "60.0"
        b2 = gfg.SubElement(m1, "file")
        b2.text = path+images[count]
        
        m2 = gfg.Element("transition")
        root.append (m2)
        
        c1 = gfg.SubElement(m2, "duration")
        c1.text = ".5"
        c2 = gfg.SubElement(m2, "from")
        c2.text = path+images[count]
        c3 = gfg.SubElement(m2, "to")
        test=len(images)
        if count < len(images)-1:
           c3.text= path+images[count+1]
        else:
           c3.text= path+images[count] 
        count=count+1    
         
    tree = gfg.ElementTree(root)

    with open (path+fileName, "wb") as files:
        tree.write(files)

# Driver Code
if __name__ == "__main__": 
    GenerateXML("Desktop.xml",images)

with open(path+'Desktop.xml', 'r') as f:
    data = f.read()

# Passing the data of the xml
# file to the xml parser of
# beautifulsoup
bs_data = BeautifulSoup(data, 'xml')
 
# A loop for replacing the value
# of attribute `test` to WHAT !!
# The tag is found by the clause
# `bs_data.find_all('child', {'name':'Frank'})`
#for tag in bs_data.find_all('child', {'name':'Frank'}):
#    tag['test'] = "WHAT !!"
 
 
# Output the contents of the
# modified xml file
file=bs_data.prettify()
print(file)
#data = "<?xml version=""1.0"" encoding=""utf-8""?>"+data
#/home/richard/.local/share/backgrounds/Desktop.xml
with open (path+"Desktop.xml", "w") as files:
        files.write(data)

file2='<?xml version="1.0" encoding="UTF-8"?>'+"\n"
file2+='<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">'+"\n"
file2+="<wallpapers>"+"\n"
file2+='  <wallpaper deleted="false">'+"\n"
file2+="    <name>Richard's slideshow</name>"+"\n"
file2+="    <filename>"+path+"Desktop.xml</filename>"+"\n"
#zoom,fill,span,center,scale,title
file2+="    <options>zoom</options>"+"\n"
file2+="    <pcolor>#2c001e</pcolor>"+"\n"
file2+="    <scolor>#2c001e</scolor>"+"\n"
file2+="    <shade_type>solid</shade_type>"+"\n"
file2+="  </wallpaper>"+"\n"
file2+="</wallpapers>"

with open ("/home/richard/.local/share/gnome-background-properties/"+theme+".xml", "w") as files:
        files.write(file2)