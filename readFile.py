from sys import argv
script, filename = argv
txt = open(filename)
print "Here's your file %r" %filename
print txt.read()
print "Type the file name again:"
file_again = raw_input(">")
txt_again = open(file_again)
#line1 =raw_input("line1:")
print txt_again.read()
