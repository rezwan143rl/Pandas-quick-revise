def sum(a,b):
     return a+b
def hel():
    print("Hello ,World")
#as it has to return value if want to save it in another variable it will show "none"
ak= hel() #will return "none"
# hel()
print(sum(1,2))
def avg_3(a,b,c):
     return (a+b+c)/3.0
print(avg_3(10,1,2))
print("sesh","kore dilo",end=" ")#will not create new line as end= is changed from\n to " ".and If we use sep="anything"it will be changedfrom " " to"anything" 
def lenlist(list):
    return len(list)
asd=["das",121,121,3123,131,3123,13123]
print(lenlist(asd)) 
def print_list(list):
    for el in list:
        print(el,end=" ")
    print()
print_list(asd)
def factorial(n):
    fact=1
    for l in range(1,n+1):
        fact*=l
    return fact
print(factorial(5))
def usd_to_bdt(usd):
    return usd*124
print(usd_to_bdt(50))
def odd_even():
    n=float(input("what is the n "))    
    if (n%2==0):
        print("even number")
    else:
        print("odd number")
odd_even()
def show(n):
    if n==0:
        print()
        return
    print(n,end=" ")
    show(n-1)
show(5)
def fac_rec(n):
    if(n==1):
        return 1
    return n+fac_rec(n-1)


print(fac_rec(5))
def plist(list ,x):
    if(x==len(list)):
        return 
  
    print(list[x],end=" ")
    
    plist(list,x+1)
  

asxd =[1,"dsdc","asa",12,122,12121]

plist(asxd,1)