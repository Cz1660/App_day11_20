a = [2,3,4]
def i():
    for i in a:
        if 2 == 2:
            print(i)
            try:
                assert 2 == 4
            except Exception as E:
                print(E)
        else:
            print(3)
print(i())
