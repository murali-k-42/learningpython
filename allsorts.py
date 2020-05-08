import selectionsort as ss
import insertionsort as ins
import bubblesort as bs
import mergesort as ms
import quicksort as qs
import binarysearch as bins
import deterministicselect as dsel
import randomizedselect as rsel

import time

print("------------------------------------------------")
print("Sorting Methods:")
print("------------------------------------------------")
print("1. Selection Sort")
print("2. Insertion Sort")
print("3. Bubble Sort")
print("4. Merge Sort")
print("5. Quick Sort")
print("------------------------------------------------")
print("Selection Methods:")
print("------------------------------------------------")
print("6. Binary Search")
print("7. Randomized ith order selection")
print("8. Deterministic ith order selection")
print("------------------------------------------------")
print("9. Exit")

while True:
    sel = int(input("Selection: "))
    if 0 < sel < 10:
        break
    else:
        print("Enter a valid selection")

inp_arr = []
if sel > 0:
    file_nm = input("Enter csv filename with data: ")
    if file_nm == "":
        file_nm = "sortedfil.csv"

    with open(file_nm, "r") as f:
        file_dat = f.readlines()

    for sublist in file_dat:
        for nums in sublist.split(","):
            inp_arr.append(int(nums))

start_time = time.time()
if sel == 1:
    sorted_array = ss.selection_sort(inp_arr)
elif sel == 2:
    sorted_array = ins.insertion_sort(inp_arr)
elif sel == 3:
    sorted_array = bs.bubble_sort(inp_arr)
elif sel == 4:
    sorted_array, invcount = ms.merge_sort(inp_arr, 0)
elif sel == 5:
    qs.quick_sort(inp_arr, 0, len(inp_arr)-1)

elif sel == 6:

    is_sort = input("Is the input already sorted(Y/N): ")
    if not is_sort.upper().strip() == "Y":
        sorted_arr, x = ms.merge_sort(inp_arr, 0)
    start_time - time.time()
    num = int(input("Enter number to search:"))
    idx, found = bins.binary_search(inp_arr, int(num), 0)

    if found:
        print(f"{num} is found at location {idx} in the input array")
    else:
        print(f"{num} is not found in array, closest match at location {idx} is {inp_arr[idx]}")


elif sel == 7 or sel == 8:

    stat = 0
    while True:
        stat = int(input("Enter order of statistic to search: "))
        if stat < 1 or stat > len(inp_arr):
            print(f"Enter number between 1 and {len(inp_arr)}")
            continue
        break

    start_time - time.time()
    if sel == 7:
        stat_v = rsel.Rselect(inp_arr, 0, len(inp_arr) - 1, stat-1)
    else:
        stat_v = dsel.Dselect(inp_arr, 0, len(inp_arr) - 1, stat - 1)
    print(f"{stat}th order statistic in given input data is {stat_v}")


end_time = time.time()

dt = end_time - start_time
print(f"Operation performed on array of size {len(inp_arr)} is {dt} seconds")