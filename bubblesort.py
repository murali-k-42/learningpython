def bubble_sort(input_array):

    swap_count = 1
    while swap_count > 0:
        swap_count = 0
        for i in range(0, len(input_array)-1):
            if input_array[i] > input_array[i+1]:
                temp_val = input_array[i+1]
                input_array[i+1] = input_array[i]
                input_array[i]=temp_val
                swap_count += 1
    return input_array

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
    print(bubble_sort(inp_arr))
