

def main():
    try :
        for line in readFile('ravens.doc'):
            print(line.strip())
    except IOError as e:
        print("can't open the file", e)
    except ValueError as e:
        print('Bad filename', e)   
      


def readFile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
         raise ValueError('filename should end with .txt')



if __name__ == '__main__':
    main()
    