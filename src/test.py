i = 0
f = open("./pairs-sfm.txt","w")

for i in range(0,1775):
  name = "frame" + str(i).zfill(5) + ".jpg"
  name2 = "frame" + str(i+1).zfill(5) + ".jpg"
  aa = name + " " + name2 + "\n"
  f.write(aa)