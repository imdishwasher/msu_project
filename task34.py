from tkinter1 import *
def get_float(prompt="Введите число"):
    while True:
        try:
            num = float(input(prompt + ": "))
            return num
        except ValueError:
            print("Ошибка! Введите корректное вещественное число.")
def get_int(prompt="Введите целое число"):
    while True:
        try:
            num = int(input(prompt + ": "))
            return num
        except ValueError:
            print("Ошибка! Введите корректное целое число.")

import sys

class Matrix2:
    
    def __init__(self, x0, dx, N):
        self.x0 = x0
        self.dx = dx
        self.N = N
        self.x = [0.0] * N
        self.y = [0.0] * N
#заполняет список x значениями, используя начальное значение и шаг
    def set_x(self):
        for i in range(self.N):
            self.x[i] = self.x0 + i * self.dx
#принимает функцию f и использует ее для заполнения списка y значениями, полученными из f для каждого значения x
    def set_y(self, f):
        for i in range(self.N):
            self.y[i] = f(self.x[i])
# Выводит содержимое списков x и y в указанный файл 
    def out(self, file=sys.stdout):
        for i in range(self.N):
            print(f"{self.x[i]:.4f} {self.y[i]:.4f}", file=file)
#Строит график данных из списков x и y на указанном объекте Axes возвращает объекты линий для графиков
    def plot(self, ax, **kwargs):
        return ax.plot(self.x, self.y, **kwargs)

import matplotlib.pyplot as plt
import math as M

# x0 = get_float("Введите начальное значение X")
# dx = get_float("Введите шаг по X")
# N = get_int("Введите число точек")

#Метод set_x/y вызывается для обоих объектов, чтобы заполнить списки x/y
mat1 = Matrix2(x0, dx, N)
mat1.set_x()
mat1.set_y(M.sin)

mat3 = Matrix2(x0, dx, N)
mat3.set_x()
mat3.set_y(lambda x: M.sqrt(x))

mat2 = Matrix2(x0, dx, N)
mat2.set_x()
mat2.set_y(M.cos)

with open("output5.txt", "w") as f:
    mat1.out(f)
    mat2.out(f)
    mat3.out(f)


fig2, ax2 = plt.subplots(1, 3, figsize=(15, 5))
fig2.suptitle('Графики')
ax2[0].set_title("sin(x)")
ax2[1].set_title("cos(x)")
ax2[2].set_title("sqrt(x)")
mat1.plot(ax2[0], label='sin(x)')
mat2.plot(ax2[1], label='cos(x)')
mat3.plot(ax2[2], label='sqrt(x)')
ax2[0].legend()
ax2[1].legend()
ax2[2].legend()


fig1, ax1 = plt.subplots()
mat1.plot(ax1, label='sin(x)')
mat2.plot(ax1, label='cos(x)')
mat3.plot(ax1, label= 'sqrt(x)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
plt.show()

