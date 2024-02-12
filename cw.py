my_list = [1, 2, 3, "four", 5.0]
print(my_list)
print(type(my_list))
print(type(my_list[0]))
print(type(my_list[3]))
print(type(my_list[4]))
print(my_list[0])
print((my_list[3]))
print(my_list[4])
fruits=["apple","banana","strawberry","grapes","melon","watermelon","orange"]
if "banana" in fruits:
    print("Guave is in the fruit list")
else:
    print("No, Guava is not in the fruit list")
a="jhdh"
if "o" in a:
    print("yes") 
else:
    print("no")
l=["banana","apple"]
l.sort(reverse=True)
print(l)
l.sort()
print(l) 
#sort and reverse orinal list mai changing karta hai
#::-1 wala orignl mai changing nahi krta
l=[-2,5,8,9,7,-8,-222,444,0,-2,5,5]
l.reverse()
print(l)
print(l[::-1])
print(l)

l=[-2,5,8,9,7,-8,-222,444,0,-2,5,5]
print(l.index(5))  #first occurence
print(l[5:11].index(5)) #5 wala index ab 0 bn chuka hai
m=l.copy() #ab "l" mai changing nahi ay gi 
m[0]=12
print(m)
print(l)
#append hmaisha end par
l.append(6)
print(l)
#apni marzi sy karny k liye insert
l.insert(len(l),99)
print(l)
l.insert(len(l)-1,99)
print(l)
#extend (orignal ko change kr deta)
l=[-2,5,8,9,7,-8,-222,444,0,-2,5,5]
m=["hello","UET"]
l.extend(m)
print(l)

#khali pop last waly ko remove karta hai
l=[-2,5,8,9,7,-8,-222,444,0,-2,5,5]
l.pop()
print(l)
l.pop(8)
print(l)



#just like extend function (ye orignal mai changing nhi krta, new bna rha hai)
fruits=["apple","banana","strawberry","grapes","melon","watermelon","orange"]
new_fruits=["kiwi","guava"]
total_fruits=fruits+new_fruits
print(total_fruits)

for i in range(1,4):
    total_fruits=total_fruits+["mango"]
    print(total_fruits)

fruits=["apple","banana","strawberry","grapes"]
new_fruits=["kiwi","guava"]
total_fruits=fruits+new_fruits
print(total_fruits*2) 

L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(type(L[2]))

fruits=["apple","banana","strawberry","grapes","melon","watermelon","orange"]
new_fruits=[x for x in fruits if len(x)<=6]
print(new_fruits)
new_fruits=[x[::-1] for x in fruits if len(x)>5 and x.endswith("n") ]
print(new_fruits)

country=("Pakistan")
print(type(country))
country1=("Pakistan",)
print(type(country1))

country=("Pakistan","Italy","France","Switzerland","Pakistan")
temp=list(country)
temp[1]="China"
temp.append("Canada")
temp.remove("France")
country=tuple(temp)
print(country)





