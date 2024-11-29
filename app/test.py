import time

def test_print():
    print("hola como estamos")

select = 0

def while_func():
    a = 4
    while(a > 0):
        if select == 0:
            print(0)
        elif select == 1:
            print(1)
        time.sleep(1)
        #a -= 1
