t = open("/home/chang/catkin_ws/src/project/a.txt", "r")
with open("/home/chang/catkin_ws/src/project/b.txt", "r") as f:
    lines = f.readlines()
    nums = t.readlines()
    for i, line in enumerate(lines):
        cc = line.split()
        x = float(cc[0])
        y = float(cc[1])
        z = float(cc[2])
        if nums[i] == '1':
            r = 255
            g = 0
            b = 0
        elif nums[i] == '0':
            r = 0
            g = 255
            b = 0
        a = 255
        print(type(nums[i]))
        print(int(nums[i]))
        print(i)