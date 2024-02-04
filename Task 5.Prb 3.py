#Using a python Lambda function create a fibonacci series from 1 to 50 elements?
from functools import reduce

n=int(input("Enter the value of n: "))

fib_series= reduce(lambda x,_: x+ [x[-1]+x[-2]],range(n-2),[0,1])
print(fib_series)