import math

def convex_hull(points):
    # Step 1: Sort the points by their polar angle with respect to the lowest point
    lowest_point = min(points, key=lambda p: (p[1], p[0]))
    sorted_points = sorted(points, key=lambda p: (math.atan2(p[1]-lowest_point[1], p[0]-lowest_point[0]), -p[1], p[0]))
    
    # Step 2: Initialize the hull with the lowest point and the first two sorted points
    hull = [sorted_points[0], sorted_points[1]]
    
    # Step 3: Iterate through the remaining sorted points
    for point in sorted_points[2:]:
        # Step 3a: While the last three points make a non-left turn, remove the middle point
        while len(hull) > 1 and (point[0]-hull[-2][0])*(hull[-1][1]-hull[-2][1]) <= (point[1]-hull[-2][1])*(hull[-1][0]-hull[-2][0]):
            hull.pop()
        # Step 3b: Add the current point to the hull
        hull.append(point)
    
    # Step 4: Return the hull
    return hull

# Example usage
points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
hull = convex_hull(points)
print(hull)
