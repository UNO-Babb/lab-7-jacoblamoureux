#Problem10.py
#Project Euler problem 10

from NumberTests import isPrime

def main():
    total = 0
    for i in range(2000000):
       if isPrime(i):
          total += i
    print(total)
    #my computer could not handle 2000000 but it worked with smaller numbers.
if __name__ == '__main__':
  main()