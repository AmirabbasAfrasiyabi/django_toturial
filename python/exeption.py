try:
    print('befor')
    print(7/0)
    print('after')
except ZeroDivisionError:
    print('didnt excute exception')

finally:
    print('end of the program')

    