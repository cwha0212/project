t = open("/home/chang/images_map4.txt", "w")
with open("/home/chang/.ros/traj/map4.txt", "r") as f:
    lines = f.readlines()
    i = 1
    for j, line in enumerate(lines):
        name = "frame" + str(i-1).zfill(5) + ".jpg"
        cc = line.split()
        x = float(cc[1])
        y = float(cc[2])
        z = float(cc[3])
        qw = float(cc[7])
        qx = float(cc[4])
        qy = float(cc[5])
        qz = float(cc[6])
        a = 255
        t.write(str(i)+ " ")
        t.write(str(qw)+" "+str(qx)+" "+str(qy)+" "+str(qz)+" "+str(x)+" "+str(y)+" "+str(z)+" "+"1"+" "+name)
        t.write("\n\n")
        i += 1