

def main():
    
    bufferSize = 50000
    infile = open('olives.jpg', 'rb')
    outfile = open('newOlives.jpg', 'wb')
    
    for buffer in readfromFile(bufferSize, infile):
        outfile.write(buffer)
   
    #while len(buffer):
    #   outfile.write(buffer)
    #   buffer = infile.read(bufferSize)

    print("Done")



def readfromFile(bufferSize, infile):
    buffer = infile.read(bufferSize)
    while len(buffer):     
        yield buffer
        buffer = infile.read(bufferSize)
     

if __name__ == '__main__':
    main()
    