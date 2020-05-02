def merge_sort(input_array):
    n = len(input_array)
    C = []
    if n >= 2:
        A = merge_sort(input_array[:int(n/2)])
        B = merge_sort(input_array[int(n/2):])
        i, j = 0, 0
        for k in range(0, n):
            if i < int(n/2):
                if j < n-int(n/2):
                    if A[i] < B[j]:
                        C.append(A[i])
                        i += 1
                else:
                    C.append(A[i])
                    i += 1
            if j < n-int(n/2):
                if i < int(n/2):
                    if A[i] >= B[j]:
                        C.append(B[j])
                        j += 1
                else:
                    C.append(B[j])
                    j += 1
    else:
        C = input_array

    return C

# Initial section will be migrated to a common input file at a later date, with user input for filename and delimiter


file_nm = "sortfil.csv"

with open(file_nm, "r") as f:
    file_dat = f.readlines()

inp_arr = []

for sublist in file_dat:
    for nums in sublist.split(","):
        inp_arr.append(int(nums))

print(inp_arr)
print(merge_sort(inp_arr))