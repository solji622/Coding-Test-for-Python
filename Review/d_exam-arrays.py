arr = [3, 5, 6, 1, 2, 4]

def is_number_exist(num, arr):
    for i in arr:
        if (i == num):
            return True
    return False

print(is_number_exist(3, arr)) # True
print(is_number_exist(120, arr)) # False