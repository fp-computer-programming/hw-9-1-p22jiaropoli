# Author JRI 1/13/22

def find_thing(lst,x):
    for i, v in enumerate(lst):
        if v == x:
            index = i
        else:
            index = -1
            break
    return index

print(find_thing([1,2,3,7,5,17,7,8,7],9))
