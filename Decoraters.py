def decoratorTest(word):
    def test():
        return word().upper()
    return test
@decoratorTest
def check():
    return "test"
print(check())


