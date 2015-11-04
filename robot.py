import sys

run = True
while run:
	line = sys.stdin.readline()
        if line:
                   cmd = line.rstrip()
                   if len(cmd):
	               print "BUFFER: ", cmd
                   else:
                        print "EXECUTE BUFFER"
        else:
               run = False 
