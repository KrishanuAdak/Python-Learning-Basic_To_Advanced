import Functions as fc
def add(a,b):
    return a+b

def test(a,b,c):
    print(a+b+c)
a=add(1,2)
test(1,2,3)
print(a)

def argsCheck(*args):
    print(len(args))
argsCheck(1,2,3,4,5)

def argsCheck2(greet,*names):
    for name in names:
        print(greet,name)
argsCheck2("Welcome","Kri","khan","Stifu","Bob")

def tes():
    x = 1111
    def eeee():
      #    x is not accessible
      print(x)
    eeee()
tes()


def test1():
     test2()
def test2():
    print('hey test2')
test1()

x=range(1,21)
for i in x:
    print(i)

# Iterator
fruits_list=['apple','banana','mango']
itr=iter(fruits_list)
print(next(itr))
fc.test2()