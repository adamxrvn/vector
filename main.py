import numpy as np
import math


def rotate_x(vector, theta):
    R = np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])
    return np.dot(R, vector)


def rotate_y(vector, theta):
    R = np.array([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]])
    return np.dot(R, vector)


def rotate_z(vector, theta):
    R = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
    return np.dot(R, vector)


print('Choose dimension: 2/3')
dimension = int(input())
print('Input coordinates: ')
v = np.asarray([0.0, 0.0, 0.0])
for i in range(dimension):
    v[i] = float(input())

if dimension == 2:
    print(f'Length: {math.sqrt((v[0] ** 2 + v[1] ** 2))}')
elif dimension == 3:
    print(f'Length: {(v[0] ** 2 + v[1] ** 2 + v[2] ** 2) ** (1 / 2)}')

print('Scale by value: ')

v *= float(input())
print(v[0:2])

print('Rotate scale by an angle (degrees)')

if dimension == 3:
    print('X: ', end="")
    x = float(input())
    print('Y: ', end="")
    y = float(input())
    print('Z: ', end="")
    z = float(input())
    v = rotate_x(v, x)
    v = rotate_y(v, y)
    v = rotate_z(v, z)
    print(v)
elif dimension == 2:
    print('X: ', end="")
    x = float(input())
    print('Y: ', end="")
    y = float(input())
    v = rotate_x(v, x)
    v = rotate_y(v, y)
    print(v[0:2])
