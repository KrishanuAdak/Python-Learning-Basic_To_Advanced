add=lambda a,b,c:a+b
print(add(1,2,3))

a=[1,3,4,2]
i=0
while i<len(a):
    print(a[i]*a[i])
    i=i+1

dict=dict({"name":"krii",
           "2":[1,2,3,],
           "age":12})
# # print(dict)
# sum=0
# for names in dict.values():
#     if names.isdigit():
#         print(names)
# dict["name"]="Krishanu"
# print(dict," ",sum)
# dict.clear()
dict.pop("name")
print(dict)



