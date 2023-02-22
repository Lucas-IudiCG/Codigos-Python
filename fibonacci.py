K=3
fib1=1
fib2=1
for i in range(18):
    fib20=fib1+fib2
    fib2=fib1
    fib1=fib20
    print(fib20, end="/")
    print(K)
    K+=1
    
