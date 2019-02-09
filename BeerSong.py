
def Ninety_Nine_Bottles_of_Beer(n):
  p = n
    #p will be a variable used as 99

    #99 times we will be passing around the beer
    while (n <= p):

        m = n-1 #this is used in the 2nd line(take one down.....)
        print(n," bottles of beer on the wall, ",n, " bottles of beer")
        print("take one down, pass it around, ",m," bottles of beer on the wall.")
        n -= 1 # n goes down by 1 every 2 lines
        if n == 1: #once n = 0, we have no beer left thus ending the song
            print(n, " bottles of beer on the wall, ", n, " bottles of beer")
            print("take one down, pass it around, no more bottles of beer on the wall.")
            break
    return n
def main():
  n= 99 #99 bottles starting
  print(n) #just to show how many beer bottles we are starting with
  Ninety_Nine_Bottles_of_Beer(n);
main()
