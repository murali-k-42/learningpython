import csv

file_str = input("Enter csv file name: ")
if not(file_str.endswith(".csv")):
    file_str += ".csv"
d_lim = input("Delimiter (default is ',')")
if len(d_lim.strip()) == 0:
    d_lim = ","
with open(file_str) as csv_file, open(file_str.replace("csv", "inp"), "w", newline='') as inp_file:
    csv_reader = csv.DictReader(csv_file, delimiter=d_lim)
    inp_writer = csv.writer(inp_file, delimiter=d_lim)
    inp_writer.writerow(["*NODE"])
    node_num = 1
    for row in csv_reader:
        inp_writer.writerow([node_num, float(row['X (m)'])*1000, float(row['Y (m)'])*1000, float(row['Z (m)'])*1000])
        node_num += 1

print("Converted csv to inp file!")
