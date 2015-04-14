import sys
linenum = 1 

print ("Copy and paste the raw text field")
txtraw=raw_input("text: ")
if not txtraw:
    raise ValueError('empty string')

# Parse
textparse = ()
for items in txtraw.split('|'):
    itemx = items.split(',')
    print linenum,"|", itemx, "|", "Number of items: ",len(itemx)
    linenum = linenum +1
