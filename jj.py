print("hello")
#%%
print("jj")
#%%
print("t")
#%%
x=5
prin(type(x))
#%%
x=5
print(type(x))
#%%
n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Factors do not exist")
elif n == 0:
    print("1")
else:
    for i in range(1,n + 1):
        f = f*i
    print("factorial is",f)
#%%
year = int(input("Enter a year: "))
if( ((year%4==0)and(year % 100 != 0)) or (year % 400==0) ):
    print("Leap Year")
else:
    print("Not leap Year")

#%%
celsius = int(input("Enter a temperature: "))
fahrenheit = (celsius * 1.8) + 32
print(str(celsius )+ " degree Celsius is equal to " + str(fahrenheit )+ " degree Fahrenheit.")
#%%
a = float(input('Enter length of side a: '))
b = float(input('Enter length of side b: '))
c = float(input('Enter length of side c: '))
if  a==b and b==c:
    print('Triangle is Equilateral.')
elif a==b or b==c or a==c:
    print('Triangle is Isosceles.')
else:
    print('Triangle is Scalane')

s=float(a+b+c)/2
area=float(s*(s-a)(s-b)(s-c))**(1/2)
print(area)
#%%
import cmath

a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

#%%
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")