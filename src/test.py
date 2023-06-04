def inside_or_outside(polygon, point):
    """
    한 점(point)이 다각형(polygon)내부에 위치하는지 외부에 위치하는지 판별하는 함수
    입력값
        polygon -> 다각형을 구성하는 리스트 정보
        point -> 판별하고 싶은 점
    출력값
        내부에 위치하면 res = 1
        외부에 위치하면 res = 0
    """
    N = len(polygon)-1    # N각형을 의미
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
        res = False  # point is outside
    else:
        res = True  # point is inside
    return res

result = inside_or_outside([[1,0],[2,1],[1,2],[0,1]],[1.5,1.5])
print(result)

x = [1,2,3]
for i,x in enumerate(x):
    print(i)