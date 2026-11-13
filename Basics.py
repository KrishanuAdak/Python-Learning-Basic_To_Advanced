from xmlrpc.client import boolean

name="Krishanu"
# print(len(name))
# if name.startswith('Kri'):
#     print(name.upper())
#     print(name.lower())
print(name[::-1])
print("i am",26,"years old",33)

#Type Casting
x=11;
y=str(x);
print(type(y))
z=float(y)
print(type(z))
_my_var='Kri'
_my_var_='ee'
__myy_var='Krrooo'
print(_my_var);
print(__myy_var)
print(_my_var_)
tests=["one","two",'Three']
x,y,z=tests
print(x,y,z)

# Data types
br=True
print(br)
xx=None
print(type(xx))

arr=range(10)
print(list(arr))
for i in list(arr):
    if(i%2==0):
        print(i)
x=bytearray(range(5))
print(x)

poem="""
hey i am there, what's up?
i know you are not well now.
let's meet together
"""
print(len(poem))
a="hello world"
str=a.split(" ")
print(str[1])
for i in str[1]:
    print(i)
print ("worlds" not  in a)
b="   hello , world  "
print(b[2:5])
print(b[::-1])
print(b[:2])
print(b[2:])
print(b[-len(b):-1])
print(b.strip())
print(b.replace('h','H'))
a='13'
print(a.isdigit())
print(a.title(),a.isalnum())
print(bool(a))

num=8
x="Even" if num%2==0  else  "odd" if num%2==0 else "no"
print(x)

# List
li=["2ue","ww","wee3",True,13,"ierrr"]
li.append("ie")
print(type(li))
ll=list(("one","two","three","rone"))
print(ll[0],ll[-1])