def countPrimes(n):
        result = 0
        if(n >= 2):
            primeList = [True for i in range(n)]
            index = 2 

            while(index**2 <= n):
                if(primeList[index] == True):
                    for i in range(index**2, n, index):
                        primeList[i] = False
                index += 1
            primeList = [x for x in range(2,n) if primeList[x] == True]
            result = len(primeList)
        return result
      
def main():
  print(countPrimes(10))

  
  if __name__ == "__main__":
    main()
