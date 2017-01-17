import os, subprocess


path = "/home/simen/Dropbox/phd/cse/cse_book_doconce/"


def transform(filename):
    if filename[-3:] == "tex":
        print "Transforming: ", filename[len(path):]
        output = open(filename[:-3]+"do.txt", 'w')
        subprocess.call(["doconce", "latex2doconce", filename],stdout=output)
        output.close()
        

def delete(filename):
    print "Deleting: ", filename[len(path):]
    if filename[-3:] == "tex":
        os.remove(filename)
    if filename[-3:] == "aux":
        os.remove(filename)
    if filename[-6:] == "backup":
        os.remove(filename)
       
        
folders = os.listdir(path)
for folder in folders:
    transform(path+folder)
    if os.path.isdir(path+folder):
        files = os.listdir(path+folder)
        for f in files:
            #transform(path+folder+"/"+f)
            delete(path+folder+"/"+f)
