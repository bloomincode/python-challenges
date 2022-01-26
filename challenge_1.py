# Convert radians into degrees - https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
import math

def convert_degrees_to_rad(deg):
    return round(deg * (math.pi/180), 4)


# unit test
expected = [0.0175, 0.1745, 0.2618, 0.7854, 1.5708, 2.0944, 3.1416, 6.2832]
input = [1, 10, 15, 45, 90, 120, 180, 360]
for idx, i in enumerate(input):
    output = convert_degrees_to_rad(i)
    print(f"Test Result", idx+1, ":", output == expected[idx])