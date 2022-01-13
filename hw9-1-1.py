# Author JRI 1/12/22

even_list = []

def even_id(lst):
    for index, value in enumerate(lst):
        if int(index) % 2 == 0:
            even_list.append(value)
    return ("Even numbered indexes: {0}".format(even_list))

test_lst = [1,2,3,4,5,6]

print(even_id(test_lst))