def print_hello_world():
    for i in range(3):
        print("Hello World")

print(print_hello_world())

def aca():
    print("done")

def cs():
    return 3

print(aca())
print(cs())

## args kwarg
def test(**kwargs):
    print(kwargs)
test(name="amir")

