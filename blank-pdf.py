import argparse
from system import system

def blank(pdf):
    """Add blank pages for every other page in a pdf file"""

    pages = int(system("pdftk {pdffile} dump_data | grep NumberOfPages".format(pdffile=pdf)).split(":")[1].strip())

    cmdstring = ""
    for page in range(1, pages + 1):
        cmdstring += " A{page}-{page} B1-1".format(page=page)


    cmd = "pdftk A={pdffile} B=blank.pdf cat {cmdstring} output {pdffile}-blank.pdf".format(pdffile=pdf, cmdstring=cmdstring)

    system(cmd)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Add blank pages for every other page in a pdf file')
    parser.add_argument('pdffile', help='Name of pdffile')

    args = parser.parse_args()

    blank(args.pdffile)
