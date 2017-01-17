import subprocess, argparse, shutil

path = "/home/simen/Dropbox/Phd/"

class Literature:
    def __init__(self, name, filename, note):
        self.name = name
        self.filename = filename
        self.note = note

    def __str__(self):     
        return "{:<50} {}".format(self.name, self.note)
        
    def Note(self, note):
        self.note = note

    def Name(self, name):
        self.name = name

    def Filename(self, filename):
        self.filename = filename

    def saveString(self):
        return self.name + " : " + self.filename + " : " + self.note + "\n"
        

class Collection():
    def __init__(self, collectionName):
        self.collectionName = collectionName
        self.collection = []

        f = open(path + self.collectionName + "/" + self.collectionName + ".txt",)
        for line in f:
            splitline = line.split(":")
            self.collection.append(Literature(splitline[0].strip(), splitline[1].strip(),splitline[2].strip()))
        f.close()
        
    def save(self):
        f = open(path + self.collectionName + "/" + self.collectionName + ".txt", "w")
        
        for c in self.collection:
            f.write(c.saveString())

        f.close()
        
    def addNote(self, id, note):
        try:
            id = int(id)
            self.collection[id-1].Note(note)
            
        except ValueError:
            for c in self.collection:
                if c.name == id:
                    c.Note(note)
                    break
            
        except IndexError:
            print "Id is out of range"

                          
    def addElement(self, name, filename, note=""):
        self.collection.append(Literature(name, filename, note))

    def Print(self):
        i = 1;
        #print "Id %5s  %50s" % ("Name", "Note")
        print  "{:<3} {:<50} {}".format("Id","Name", "Note")
        for c in self.collection:
            print i, " ",c
            i+=1


    def view(self, id):
        filename = None 
        try:
            id = int(id)
            filename = self.collection[id-1].filename
            
        except ValueError:
            for c in self.collection:
                if c.name == id:
                    filename = c.filename
                    break
            
        except IndexError:
            print "Id is out of range"

        if filename == None:
            print "No file found"
            return 0
        subprocess.call(["xdg-open", path + self.collectionName + "/" + filename])
            



parser = argparse.ArgumentParser(description="Keep track of literature.")
subparsers = parser.add_subparsers(dest='parser_name')


parser_add = subparsers.add_parser('add', help='Add an article/book')
addgroup = parser_add.add_mutually_exclusive_group(required = True)
addgroup.add_argument("-a", "--article", help="Add an article", action="store_true")
addgroup.add_argument("-b", "--book", help="Add a book", action="store_true")
parser_add.add_argument("name", help="Name of the article/book")
parser_add.add_argument("filename", help="Filename of the article/book")
parser_add.add_argument("-n", "--note", help="Note added to the article/book")


parser_list = subparsers.add_parser('list', help='List all articles/books')
parser_list.set_defaults()
listgroup = parser_list.add_mutually_exclusive_group()
listgroup.add_argument("-a", "--article", help="List all articles", action="store_true")
listgroup.add_argument("-b", "--book", help="List all books", action="store_true")


parser_view = subparsers.add_parser('view', help='View an article/book')
viewgroup = parser_view.add_mutually_exclusive_group(required=True)
viewgroup.add_argument("-a", "--article", help="View article number/name", action="store_true")
viewgroup.add_argument("-b", "--book", help="view book number/name", action="store_true")
parser_view.add_argument("id", help="Id/name of the article/book")


parser_note = subparsers.add_parser('note', help='Add a note to an article/book')
notegroup = parser_note.add_mutually_exclusive_group(required = True)
notegroup.add_argument("-a", "--article", help="Add an article", action="store_true")
notegroup.add_argument("-b", "--book", help="Add a book", action="store_true")
parser_note.add_argument("id", help="Name/id of the article/book")
parser_note.add_argument("note", help="Note added to the article/book")


parser_backup = subparsers.add_parser('backup', help='Backup list of articles/books')
parser_backup = subparsers.add_parser('print', help='Print an article/book')


args = parser.parse_args()



books = Collection("books")
articles = Collection("articles")



if args.parser_name == "list":
    if args.article:
        i = 1
        print  "\n[Articles]\n"
        articles.Print()
        print " "
         
    elif args.book:
        i = 1
        print "\n[Books]\n"
        books.Print()
        print " "    

    else:
        i = 1
        print  "\n[Articles]\n"
        articles.Print()
        print "\n[Books]\n"
        books.Print()
        print " "     

    
if args.parser_name == "add":
    if args.article:
        if args.note:
            articles.addElement(args.name, args.filename, args.note)
        else:
            articles.addElement(args.name, args.filename)
    else:
        if args.note:
            books.addElement(args.name, args.filename, args.note)
        else:
            books.addElement(args.name, args.filename)


if args.parser_name == "view":
    if args.article:
        articles.view(args.id)
    else:
        books.view(args.id)

        
if args.parser_name == "note":
    if args.article:
        articles.addNote(args.id, args.note)
    else:
        books.addNote(args.id, args.note)


if args.parser_name == "backup":
    shutil.copy("books/books.txt", "books/books_old.txt")
    shutil.copy("articles/articles.txt", "articles/articles_old.txt")

if args.parser_name == "print":
    print "Not implemented"

articles.save()
books.save()
