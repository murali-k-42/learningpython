def insertion_sort(input_array):

    for i in range(1, len(input_array)):
        for j in reversed(range(1, i+1)):
            if input_array[j] < input_array[j-1]:
                temp_val = input_array[j]
                input_array[j] = input_array[j-1]
                input_array[j - 1] = temp_val
            else:
                break
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
print(insertion_sort(inp_arr))