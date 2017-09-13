def fib(n):
    a=0
    b=1
    for x in range(n):
        a=b
        b=a+b
        print(a,'\n')
    return  b
num=int(input("enter n value"))
print(fib(num))