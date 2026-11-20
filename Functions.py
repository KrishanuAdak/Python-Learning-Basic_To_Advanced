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