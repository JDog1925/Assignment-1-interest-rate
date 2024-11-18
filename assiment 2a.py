rectangleLength = float(input( "enter length of rectangle: "))

rectangleWidth = float(input( "enter width of rectangle: "))

if rectangleLength < 0 or rectangleWidth < 0:
     raise ValueError('a should be a positive number')


rectangleArea = rectangleLength * rectangleWidth

print("Area of rectangle= %.2f" %rectangleArea )


