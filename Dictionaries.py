import Dictionaries as dc
test={
    "age":13,
    "1":'2',
    "name":'krishanu',
    "name":'namia',
    "salary":'2'
}
# }
# print(test.get("name"))
# for i in test:
#     print(i.isdigit())

for name in test.items():
    print(name)
for name in test.keys():
    print(name)
cc=dc.test.get("age")
print(cc)
