def binary_search(input_array, find_num, start_idx):

    n = len(input_array)
    curr_idx = 0
    is_found = False
    if n > 1:
        mid_num = input_array[int(n/2)]
        if find_num < mid_num:
            curr_idx, is_found = binary_search(input_array[0:int(n/2)], find_num, 0)
            curr_idx += start_idx
        elif find_num > mid_num:
            curr_idx, is_found = binary_search(input_array[int(n/2)+1:], find_num, int(n/2)+1)
            curr_idx += start_idx
        else:
            curr_idx = start_idx + int(n/2)
            is_found = True
    else:
        curr_idx = start_idx
    if input_array[0] == find_num:
        is_found = True

    return curr_idx, is_found

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

idx, found = binary_search(inp_arr, int(num), 0)

if found:
    print(f"{num} is found at location {idx} in the input array")
else:
    print(f"{num} is not found in array, closest match at location {idx} is {inp_arr[idx]}")


