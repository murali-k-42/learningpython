import math


class point:

    x = 0.0
    y = 0.0

    def __init__(self, a, b):

        self.x = a
        self.y = b


def merge_sort_pt(input_array, sort_by):

    n = len(input_array)
    C = []
    if n >= 2:
        A = merge_sort_pt(input_array[:int(n/2)], sort_by)
        B = merge_sort_pt(input_array[int(n/2):], sort_by)
        i, j = 0, 0
        for k in range(0, n):
            if i < int(n/2):
                if j < n-int(n/2):
                    if getattr(A[i],sort_by) < getattr(B[j],sort_by):
                        C.append(A[i])
                        i += 1
                else:
                    C.append(A[i])
                    i += 1
            if j < n-int(n/2):
                if i < int(n/2):
                    if getattr(A[i],sort_by) >= getattr(B[j],sort_by):
                        C.append(B[j])
                        j += 1
                else:
                    C.append(B[j])
                    j += 1
    else:
        C = input_array

    return C


def dist_calc(p1, p2):

    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2+dy**2)
    return dist


def split_pair(sy, delta):

    n = len(sy)
    p3 = None
    p4 = None
    for i in range(0, n-1):
        for j in range(1, min(8, n-i)):
            dx = dist_calc(sy[i], sy[i + j])
            if dx < delta:
                p3 = sy[i]
                p4 = sy[i+j]
                delta = dx
    return p3, p4


def closest_pair(px, py):

    n = len(px)
    if n > 4:
        qx = px[:int(n/2)]
        rx = px[int(n/2):]
        qy = []
        ry = []
        mid = px[int(n/2)]
        for z in py:
            if z.x < mid.x:
                qy.append(z)
            else:
                ry.append(z)
        p1, p2 = closest_pair(qx, qy)
        p3, p4 = closest_pair(rx, ry)
        d1 = dist_calc(p1, p2)
        d2 = dist_calc(p3, p4)
        if d1 < d2:
            pa = p1
            pb = p2
            delta = d1
        else:
            pa = p3
            pb = p4
            delta = d2
        sy = []
        for z in py:
            if abs(z.x-mid.x) < delta:
                sy.append(z)
        p4, p5 = split_pair(sy, delta)
        if p4 is not None:
            pa = p4
            pb = p5

        return pa, pb

    else:

        pa = px[0]
        pb = px[1]
        mindist = dist_calc(pa, pb)
        for i in range(0, len(px)-1):
            pi = px[i]
            for j in range(i+1, len(px)):
                pj = px[j]
                if dist_calc(pi, pj) < mindist:
                    pa = pi
                    pb = pj

        return pa, pb


if __name__ == '__main__':

    file_nm = input("Enter csv filename with point data: ")
    if file_nm == "":
      file_nm = "pointsfil.csv"

      inp_arr = []

    with open(file_nm, "r") as f:
        for line in f:
            p = point(float(line.split(",")[0]), float(line.split(",")[1]))
            inp_arr.append(p)

    px, py = closest_pair(merge_sort_pt(inp_arr, "x"), merge_sort_pt(inp_arr, "y"))
    d = dist_calc(px, py)

    print(f"Closest pair are ({px.x},{px.y}) and ({py.x},{py.y}) with distance {d}")