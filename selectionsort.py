def selection_sort(input_array):

    for i in range(0,len(input_array)):
        min_val = input_array[i]
        min_idx = i
        for j in range(i+1,len(input_array)):
            if input_array[j]<min_val:
                min_idx = j
                min_val = input_array[j]
        temp_val = input_array[i]
        input_array[i] = input_array[min_idx]
        input_array[min_idx] = temp_val
    return input_array

# Initial section will be migrated to a common input file at a later date, with user input for filename and delimiter

file_nm = "sortfil.csv"

with open(file_nm, "r") as f:
    file_dat = f.readlines()

inp_arr = []

for sublist in file_dat:
    for nums in sublist.split(","):
        inp_arr.append(int(nums))

print(inp_arr)
print(selection_sort(inp_arr))