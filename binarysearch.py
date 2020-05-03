def binary_search(input_array, find_num, start_idx):
    print(input_array)
    n = len(input_array)
    curr_idx = 0
    if n > 1:
        mid_num = input_array[int(n/2)]
        if find_num < mid_num:
            curr_idx = start_idx + binary_search(input_array[0:int(n/2)], find_num, 0)
        elif find_num > mid_num:
            curr_idx = start_idx + binary_search(input_array[int(n/2)+1:], find_num, int(n/2)+1)
        else:
            curr_idx = start_idx + int(n/2)
    else:
        if input_array[0] == find_num:
            curr_idx = start_idx
        else:
            curr_idx = float("NaN")

    return curr_idx

# Initial section will be migrated to a common input file at a later date, with user input for filename and delimiter


file_nm = "sortedfil.csv"

with open(file_nm, "r") as f:
    file_dat = f.readlines()

inp_arr = []

for sublist in file_dat:
    for nums in sublist.split(","):
        inp_arr.append(int(nums))

print(inp_arr)
num = input("Enter number to search for: ")

print(f"{num} found at location {binary_search(inp_arr, int(num), 0)}")
