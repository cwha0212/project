def inside_or_outside(polygon, point):
    N = len(polygon)-1
    counter = 0
    p1 = polygon[0]
    for i in range(1, N+1):
        p2 = polygon[i%N]
        if point[2] > min(p1[2], p2[2]) and point[2] <= max(p1[2], p2[2]) and point[0] <= max(p1[0], p2[0]) and p1[2] != p2[2]:
            xinters = (point[2]-p1[2])*(p2[0]-p1[0])/(p2[2]-p1[2]) + p1[0]
            if(p1[0]==p2[0] or point[0]<=xinters):
                counter += 1
        p1 = p2 
    if counter % 2 == 0:
        res = False
    else:
        res = True
    return res

polygon = [[-117.312, -26.1437, -31.7009], [-81.6904, 2.47509, 15.0826], [-27.6202, -4.66261, -52.3082], [-22.211, -34.9372, -67.2226], [-117.312, -26.1437, -31.7009]]
t = open("/home/chang/result1.txt","w")
with open("/home/chang/Downloads/Map_rgb/map_orb_c_noroad.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        cc = line.split()
        x = float(cc[0])
        y = float(cc[1])
        z = float(cc[2])
        r = int(cc[3])
        g = int(cc[4])
        b = int(cc[5])
        if inside_or_outside(polygon, [x,y,z]) :
            t.write(str(x) + " " + str(y) + " " + str(z) + " " + str(r) + " " + str(g) + " " + str(b) + "\n")

polygon = [[-76.8014, 6.03545, 38.0975], [-63.2765, 5.04305, 59.5674], [20.0683, 6.99043, 73.0163], [8.77612, 1.36539, 17.9203], [-76.8014, 6.03545, 38.0975]]
t = open("/home/chang/result2.txt","w")
with open("/home/chang/Downloads/Map_rgb/map2_orb_c_noroad.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        cc = line.split()
        x = float(cc[0])
        y = float(cc[1])
        z = float(cc[2])
        r = int(cc[3])
        g = int(cc[4])
        b = int(cc[5])
        if inside_or_outside(polygon, [x,y,z]) :
            t.write(str(x) + " " + str(y) + " " + str(z) + " " + str(r) + " " + str(g) + " " + str(b) + "\n")