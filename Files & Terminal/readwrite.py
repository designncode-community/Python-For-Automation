f = open('example.txt','r')
passFile = open('passFile.txt','w')
failFile = open('failFile.txt','w')
for line in f:
    if line.split( )[1]=='22':
        print(line)
passFile.close()
failFile.close()        
f.close()