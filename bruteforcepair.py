import math


class point:

    x = 0.0
    y = 0.0

    def __init__(self, a, b):

        self.x = a
        self.y = b


def dist_calc(p1, p2):

    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2+dy**2)
    return dist


if __name__ == '__main__':

    file_nm = input("Enter csv filename with point data: ")
    if file_nm == "":
      file_nm = "pointsfil.csv"

      inp_arr = []

    with open(file_nm, "r") as f:
        for line in f:
            p = point(float(line.split(",")[0]), float(line.split(",")[1]))
            inp_arr.append(p)

    px = inp_arr[0]
    py = inp_arr[1]
    mindist = dist_calc(px, py)
    for i in range(0, len(inp_arr)-1):
        for j in range(i+1, len(inp_arr)):
            dist = dist_calc(inp_arr[i], inp_arr[j])
            if dist < mindist:
                px = inp_arr[i]
                py = inp_arr[j]
                mindist = dist

    print(f"Closest pair are ({px.x},{px.y}) and ({py.x},{py.y}) with distance {mindist}")