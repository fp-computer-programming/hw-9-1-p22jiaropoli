# Author JRI 1/12/22

def odd_num(lst):
    for i, v in enumerate(lst):
        if i % 2 != 0:
            print(v)
odd_num([1, 3, 4, 6])
