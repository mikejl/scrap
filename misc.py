import sys

# Input raw KER misc
print ("Copy and paste the raw misc field")
miscraw=raw_input("misc: ")
if not miscraw:
    raise ValueError('empty string')

# Parse key value into dictonary miscparse
miscparse = {}
for pair in miscraw.split(';'):
    (key,value) = pair.split('=')
    miscparse[key] = value

# print miscparse with line number 
linenum = 1 #line number
print "line#|  Key   =   Value   | Length of value "
print "--------------------------------------------------------"
for key,value in miscparse.items():
    linenum = linenum +1
    print linenum,"|", key, "=", value, "|", len(value)

