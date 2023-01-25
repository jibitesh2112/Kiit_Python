b = int(input("Input the base : "))
h = int(input("Input the height : "))
area = b*h/2
print("area = ", area)
#%%
def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)

a = int(input("Input the integer : "))
b = int(input("Input the integer : "))
print(hcf(a,b))
#%%
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a,b):
    return (a // gcd(a,b))* b
a = int(input("Input the integer : "))
b = int(input("Input the integer : "))
print(lcm(a,b))
#%%
x = int(input("Input the integer : "))
y = int(input("Input the integer : "))
z = int(input("Input the integer : "))

if x == y or y == z or x==z:
    sum = 0
    print(sum)
else:
    sum = x + y + z
    print(sum)
#%%
x = int(input("Input the integer : "))
y = int(input("Input the integer : "))
sum = x + y
if sum in range(15, 20):
    print(20)
else:
    print(sum)
#%%
def personal_details():
    name, age = "Jibitesh", 21
    address = "bhubaneswar,odisha,India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()
#%%
amt = int(input("Input the amount : "))
rate = float(input("Input the rate : "))
years = int(input("Input the years : "))
future_value = amt*((1+(0.01*rate)) ** years)
print(round(future_value,2))
#%%
x1=int(input("enter x1 : "))
x2=int(input("enter x2 : "))
y1=int(input("enter y1 : "))
y2=int(input("enter y2 : "))
result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)
