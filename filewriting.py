#goal:  save output in a text file that can be picked up by R
#the R import code looks like the line below and simply asks for a comma
#separated file.  
#piracy <- read.csv("piracy.csv")


fout = open('/home/phil/pyoutput.txt', 'w')
line1 = "This here's the wattle,\n"
fout.write(line1)
fout.close() #don't forget the ()'s

#Victory
