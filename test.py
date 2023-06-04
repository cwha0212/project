def inside_or_outside(polygon, point):
    N = len(polygon)-1
    counter = 0
    p1 = polygon[0]
    for i in range(1, N+1):
        p2 = polygon[i%N]
        if point[1] > min(p1[1], p2[1]) and point[1] <= max(p1[1], p2[1]) and point[0] <= max(p1[0], p2[0]) and p1[1] != p2[1]:
            xinters = (point[1]-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1]) + p1[0]
            if(p1[0]==p2[0] or point[0]<=xinters):
                counter += 1
        p1 = p2 
    if counter % 2 == 0:
        res = False
    else:
        res = True
    return res


print(inside_or_outside([[0,0],[10,0],[10,10],[0,10]],[4,9]))