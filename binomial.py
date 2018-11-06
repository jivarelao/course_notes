#!/usr/bin/env python
import math # import library math to use de logfactorial function.
import argparse #imports the library 'argparse' to create arguments for the script.
parser = argparse.ArgumentParser()
#Assign arguments to the script, to be called from the command line:
parser.add_argument("-n", type=int, help="Total number of items to choose from")
parser.add_argument("-k", type=int, help="Number of items to choose")
parser.add_argument("-l", "--log", help="returns the log binomial coefficient", action="store_true")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()

def logfactorial(n,k=0):
 """logfactorial function calculates log(n!) for any integer n>0
 it make use of the property log(n!) = log(1) + .... + log (n)
 Example: logfactorial(10) = 15.104412573
 logfactorial is part of a set of functions aimed to calculate binomial coefficients
 #the following tests will be executed if the user adds --test argument in the command line:
 >>> logfactorial(10)
 15.104412573075518
 >>> logfactorial(5,4)
 1.6094379124341003
 >>> logfactorial(5,5)
 0
 >>> logfactorial(5,6)
 0
 """
 if k!=0:
  #If k is different from 0 (not default) check if is an integer, otherwise return message:
  assert type(k) ==int, "Incorrect input, 'k' needs to be an integer"
  #If k is not 0 (not default) check if is positive, otherwise return message:
  assert k > 0, "Incorrect input, 'k' needs to be positive"
  #sum = 0, initiates the local varible sum, as the starting point to iterate over de sum of log(i) 
 sum = 0
  #Checks that n is an integer and positive:
 assert type(n) ==int, "Incorrect input, needs to be an integer"  
 assert n > 0, "Incorrect input, argument must be positive"  
 #The following loop add the log(i) iterating from k to n:
 for i in range(k+1,n+1):
  sum += math.log(i)
 return sum

def choose(n=args.n,k=args.k):
 """ choose() calculates the log of the binomial log(choose(n,k))
 for any integer  n>=0 and 0<=k<= n. It is based on the formula
 to choose k elements among n: choose(n,k) = n! / (k! (n-k)!).
 It uses as input arguments -n and -k from the command line.
 #the following tests will be executed if the user adds --test argument in the command line:
 >>> choose(150,40)
 4408904561911885789946649584764715008
 """
 # The following 3 lines checks that n is an integer, equal or greater than 0 amd that k is 0<=k<=n:
 assert type(n) ==int, "Incorrect input, 'n' needs to be an integer"  
 assert n >= 0, "Incorrect input, 'n' needs to be >= 0"
 assert 0<=k<=n, "Incorrect input 'k' needs to be >= 0 & <=n"
 # The next line is a short and handy way to solve when n==k, in which case logfactorial(n-k)
 # would be undefined, perhaps there are more elegant ways to solve this, but this 
 # is a short and computationally efficient manner. We know that if n=k, nCk would always be 1.
 if n==k:
  print(1)
  #If the user added the -l or --log flag to get the log binomial coefficient:
 else:
  if args.log:
   return print(float(logfactorial(n,k)-logfactorial(n-k)))
   #If the user does not add the flag, the function will print the number of ways
   # to choose k elements among n:
  else:
   return print(int(round(math.exp(logfactorial(n,k)-logfactorial(n-k)))))

# runTest() tests the modules by running the checks inside the docstring of logfactorial() and choose():
def runTests():
 print("testing the module...")
 import doctest
 doctest.testmod(name='logfactorial')
 doctest.testmod(name='choose')
 print("done with tests.")
# The following 'if' statement checks that the modules are not imported, and run runtest()
# if the user adds the --test flag or otherwise run the main function if the user omitted the --test flag.
# both options are incompatible
if __name__ == '__main__':
 if args.test:
  runTests()
 else:
  choose()