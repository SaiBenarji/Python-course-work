try:
    #a=int(input())
    k={1:22,4:55}
    print(k[14])
    l=[22,644]
    print(1[10])
    print(10/0)
    print('1'+1)
except ValueError:
    print('Enter the correct data type')
except KeyError:
    print('key is not there')
except IndexError:
    print('index out range')
except ZeroDivisionError:
    print('cant divide with zero')
except TypeError:
    print('Enter the correct data type')
except NameError:
    print('define the varable')
else:
    print('error free program')
finally:
    print('end the program')            
