###A python program for plotting information stored in .dat files.

import sys

def fileplot(name):
    """
    A python program for plotting information stored in a .dat file. The file needs to be on the form:
    -----------------------------------------------
    #Number of rows with numbers
    #Info1     #Info2     #Info3    ...  #InfoN
    #Number1   #Number2   #Number3  ...   #NumberN
    #Number1   #Number2   #Number3  ...   #NumberN
    .
    .
    .
    .
    -----------------------------------------------
    
    It plots #Info1 vs #Info2, #Info1 vs #Info3 and so on
    """
    
    import pylab as p
    import glob, os
    


    #Try except statement to check if the given file excists
    try:
        infile = open(name, "r")
    except:
        print "Error: '" + name + "', no file with that name"
        return 1
    
    #Read the information from the top of each coloumn
    number_of_rows = int(infile.readline())
    info = infile.readline()
    info = info.split()
    number_of_coloumns = len(info)

    #Make the array for storing
    numbers = p.zeros((number_of_coloumns, number_of_rows))

    #Read all the data from the file and store it coloum by coloumn
    row = 0
    for line in infile:
        rows = line.split()
    
        col = 0
        while col < len(info):
            numbers[col][row] = float(rows[col].replace("D","e"))
            col += 1
        row += 1

    #Close the file
    file.close
    
    #Do stuff with the data
          
    #Removing old plots
    outfile = name[:-4] + ".png"
    for filename in glob.glob(outfile):
        os.remove(filename)
       
    #Plot the information in the same plot
    p.clf()
    
    i = 1
    while i < number_of_coloumns:
        p.plot(numbers[0], numbers[i])
        p.hold("on")

        i += 1

    p.xlabel(info[0])
    p.ylabel(info[1])
    p.legend(info[1:])
    p.title(name[:-4])
    p.savefig(outfile)







def fileplotline(name):
    """
    A python program for plotting information stored in a .dat file. The file needs to be on the form:
    -----------------------------------------------
    Number of sets
    #Number of rows with numbers
    #Info1     #Info2     
    #Number1   #Number2   
    #Number1   #Number2   
    .
    .
    .
    .
    #Number1   #Number2
    #Number3   #Number4   
    #Number3   #Number4   
    .
    .
    .
    .
    #Number3   #Number4
    .
    .
    .
    .
    .
    .
    -----------------------------------------------
    
    It plots #Info1 vs #Info2, #Info1 vs #Info3 and so on
    """
    
    import pylab as p
    import glob, os
    


    #Try except statement to check if the given file excists
    try:
        infile = open(name, "r")
    except:
        print "Error: '" + name + "', no file with that name"
        return 1
    
    #Read the information from the top of each coloumn
    number_of_sets  = int(infile.readline())
    number_of_rows = int(infile.readline())
    info = infile.readline()
    info = info.split()
    number_of_coloumns = len(info)

    #Make the array for storing
    numbers = p.zeros((number_of_coloumns, number_of_rows*number_of_sets))

    #Read all the data from the file and store it coloum by coloumn
    row = 0
    for line in infile:
        rows = line.split()
    
        col = 0
        while col < len(info):
            numbers[col][row] = float(rows[col].replace("D","e"))
            col += 1
        row += 1

    #Close the file
    file.close
    
    #Do stuff with the data
          
    #Removing old plots
    outfile = name[:-4] + ".png"
    for filename in glob.glob(outfile):
        os.remove(filename)
       
    #Plot the information in the same plot
    p.clf()
    
    i = 1
    j = 0
    while j < number_of_sets:
        while i < number_of_coloumns:
            print j
            p.plot(numbers[0][number_of_sets*j:number_of_sets*(j+1)], numbers[i][number_of_sets*j:number_of_sets*(j+1)])
            p.hold("on")

            j += 1
            i += 1

    p.xlabel(info[0])
    p.ylabel(info[1])
    p.legend(info[1:])
    p.title(name[:-4])
    p.savefig(outfile)





    
    

if __name__ == "__main__":
    #Try except statement to check if you enter a file
    try:
        name = str(sys.argv[1]) 
    except:
        print "Error: You need to give a data file with the numbers you want to plot."
        sys.exit(1)
 
    for name in sys.argv[1:]:
        fileplot(name)
