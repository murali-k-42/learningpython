import random


def partition(input_array, l, r):
    i = l
    for j in range(l+1, r+1):
        if input_array[j] < input_array[l]:
            i += 1
            if i == j:
                continue
            else:
                temp_val = input_array[j]
                input_array[j] = input_array[i]
                input_array[i] = temp_val
    
    temp_val = input_array[l]
    input_array[l] = input_array[i]
    input_array[i] = temp_val

    return i


def quick_sort(input_array, l, r):
    n = r-l+1
    piv = 0

    if n > 1:
        piv = random.randint(l, r)
        temp_val = input_array[piv]
        input_array[piv] = input_array[l]
        input_array[l] = temp_val
        pivot_idx = partition(input_array, l, r)
        quick_sort(input_array, l, pivot_idx-1)
        quick_sort(input_array, pivot_idx+1, r)


# Initial section will be migrated to a common input file at a later date, with user input for filename and delimiter


if __name__ == '__main__':

    file_nm = input("Enter csv filename with data: ")
    if file_nm == "":
        file_nm = "sortfil.csv"

    with open(file_nm, "r") as f:
        file_dat = f.readlines()

    inp_arr = []

    for sublist in file_dat:
        for nums in sublist.split(","):
            inp_arr.append(int(nums))

    print(inp_arr)
    quick_sort(inp_arr, 0, len(inp_arr)-1)
    print(inp_arr)
