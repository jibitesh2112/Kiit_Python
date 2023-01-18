string = str(input("Enter a string: "))
freq = {}
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Count of all characters in string is :\n "+ str(freq))
#%%
string = str(input("enter a string:"))
ctr = 0
y=len(string)
if(y<=2):
    print("error")
else:
    x = string[0:2] + string [y - 2: y ]
    print("The string is ")
    print(string)
    print("The new string is ")
    print(x)
#%%
string = str(input("enter a string:"))
print("before replace :",string)
ch = string[0]
string = string.replace(ch, '$')
string = ch + string[1:]
print("After replace :",string)
#%%
a = str(input("enter a string:"))
b = str(input("enter a string:"))
print("Before Swap :",a," ",b)
a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]
print("After Swap :",a1," ",b1)
#%%
string = str(input("enter a string: "))
if len(string) < 3:
    print(string)
elif string[-3:] == 'ing':
    print(string + 'ly')
else:
    print(string + 'ing')
#%%
def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')


    if spoor > snot and snot>0 and spoor>0:
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        return str1

string=str(input("enter a string having a sequenences for example ,the begger is not that poor, or the begger is poor"))
print(not_poor(string))
#%%
def longest_length_string(string):
    len_str = len(string[0])
    temp_val = string[0]

    for i in string:
        if(len(i) > len_str):

            len_str = len(i)
            temp_val = i

    print("The word with the longest length is:", temp_val, " and length is ", len_str)

my_string = ['car','house',"appartment"]
print("The list is :")
print(my_string)
print("The method to find the longest string in the list is called")
longest_length_string(my_string)