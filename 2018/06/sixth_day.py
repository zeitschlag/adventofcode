# read all coordinates, name them
# get miny, minx and maxy, maxX, these are my border-values, they build a rectangle
# run a thress times nested loop and calculate the manhattan-distance for each point in the rectangle
# manhattan distance = abs(coordinate.y, point.y), abs(coordinate.x, point.x)
# if there are at least two points with the same distance to a coordinate, set a point. otherwise set the coordinate-name
# just count how many points are named by a coordinate-name and count them. that's it
