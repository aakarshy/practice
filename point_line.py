from shapely.geometry import Point, LineString, Polygon
point1 = Point(2.2,4.2)
point2 = Point(7.2,-25.1)
point3 = Point(9.26,-2.456)
point3D = Point(9.26, -2.45, 0.57)
point_type = type(point1)
print(point1)
print(point3D)
dist=point1.distance(point2)
print("{0:.2f}".format(dist))
line = LineString([point1, point2, point3])
print(line)







