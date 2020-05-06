import random
import quicksort as qs


def partition(input_array, l, r):
    i = l
    for j in range(l + 1, r + 1):
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


def Rselect(input_array, l, r, k):
    n = r - l + 1
    piv = 0
    stat_val = -1
    if n > 1:
        piv = random.randint(l, r)
        temp_val = input_array[piv]
        input_array[piv] = input_array[l]
        input_array[l] = temp_val
        pivot_idx = partition(input_array, l, r)
        if pivot_idx == k:
            stat_val = input_array[pivot_idx]
        elif pivot_idx > k:
            stat_val = Rselect(input_array, l, pivot_idx - 1, k)
        else:
            stat_val = Rselect(input_array, pivot_idx + 1, r, k)
    else:
        stat_val = input_array[l]
    return stat_val

# Initial section will be migrated to a common input file at a later date, with user input for filename and delimiter


if __name__ == '__main__':

    file_nm = "sortfil1.csv"

    with open(file_nm, "r") as f:
        file_dat = f.readlines()

    inp_arr = []

    for sublist in file_dat:
        for nums in sublist.split(","):
            inp_arr.append(int(nums))
    stat = 0
    while True:
        stat = int(input("Enter order of statistic to search: "))
        if stat < 1 or stat > len(inp_arr):
            print(f"Enter number between 1 and {len(inp_arr)}")
            continue
        break

    print(inp_arr)
    stat_v = Rselect(inp_arr, 0, len(inp_arr) - 1, stat-1)
    print(f"{stat}th order statistic in given input data is {stat_v}")
    qs.quick_sort(inp_arr,0,len(inp_arr)-1)
    print(inp_arr)
