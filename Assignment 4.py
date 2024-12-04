# Input display of coordinates
x1, y1 = map(float, input("Enter coordinates of (x1,y1) Separate by a space: ").split())

x2, y2 = map(float, input("Enter coordinates of (x2,y2) Sepa4,3rate by a space: ").split())

# Calculate the distance between points

from math import sqrt

distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the output

print("The calculated distance is: ", distance)