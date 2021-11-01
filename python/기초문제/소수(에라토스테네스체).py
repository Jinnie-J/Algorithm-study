
n = int(input())
a= [True]*(n+1)
a[0]=False
a[1]=False
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(i*2, n+1, i):
            a[j]=False

print(len(primes))