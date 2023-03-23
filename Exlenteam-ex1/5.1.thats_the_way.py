import os

def func(path):
    list=[]
    arr = os.listdir(path)
    for value in arr:
        if value.startswith('deep'):
            list.append(value)

    return list

arr1= func('C:\exelenteam\images')
print (arr1)



