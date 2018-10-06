
import os


def main():

   i = 0
   path = "H:\\Farewell Vipes\\"
   directory = os.listdir(path)

   for filename in directory:
       dst = "fareWell"+ str(i) + ".jpg"
       src = path + filename
       dst = path + dst

       os.rename(src, dst)
       i += 1



if __name__ == '__main__':
    main()
    



