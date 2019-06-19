# Exception Handling(try ~ except)
s = "123"

try:
    print(int(s) + 1)
    # print(int(s) / 0) #ZeroDivisionError
    print(int(s) / 1)
except ValueError as ve:
    print("ValueError occurs!!!", ve)
except ZeroDivisionError as e:
    print("ZeroDivisionError occurs!!!", e)
except:
    print("Error occurs!!!")
else:
    print("else!!!!!!!!!!!!!!!!")
finally:
    print("FINALLY!!!")