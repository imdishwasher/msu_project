import tkinter as tk
from task34 import *
# def check(even):
#     global x0, dx, N, f
#     x0 = x0_tk.get()
#     dx = dx_tk.get()
#     N = N_tk.get()
#     foo = foo_tk.get()
#     label_checked_pars["text"] = x0, dx, N, foo

win = tk.Tk()
x0_tk = tk.IntVar()
dx_tk = tk.IntVar()
N_tk = tk.IntVar()
foo_tk = tk.StringVar()

win.title('Чертежник')
win.geometry('1200x1200+600+300')
head = tk.Label(text='Пользователь может задать входные данные и построить графики разные')
head.pack()

def add_to_frame(variable,text):
    fr = tk.Frame(win, bg='red', height=40, width=300,borderwidth=10)
    label = tk.Label(fr,text=text)
    label.grid(row=0,column=0,padx=2)
    entry = tk.Entry(fr,textvariable=variable)
    entry.grid(row=0,column=1,padx=5)
    fr.pack(anchor='w')

add_to_frame(x0_tk,"Введите начальную точку")
add_to_frame(dx_tk,"Введите шаг")
add_to_frame(N_tk,"Введите количество точек")
add_to_frame(foo_tk,"Введите функцию")

fr1 = tk.Frame(win,bg='green',height=40,width=300,borderwidth=10)
b_input_pars = tk.Button(fr1,text='Задать параметры')
b_input_pars.grid(row=0,column=0,padx=5)
b_check_pars = tk.Button(fr1,text='Проверить параметры')
b_check_pars.grid(row=0,column=1,padx=5)
b_calculate_tab = tk.Button(fr1,text='Рассчитать таблицу значений')
b_calculate_tab.grid(row=1,column=0)
b_wr_tab = tk.Button(fr1,text='Записать таблицу значений в файл')
b_wr_tab.grid(row=1,column=1)
b_readcalc_tab = tk.Button(fr1,text='Считать таблицу значений из файла')
b_readcalc_tab.grid(row=2,column=0)
b_draw_graph = tk.Button(fr1,text='Нарисовать график')
b_draw_graph.grid(row=2,column=1)
b_save_graph = tk.Button(fr1,text='Сохранить график')
b_save_graph.grid(row=3,column=0)
b_clear_graph = tk.Button(fr1,text='Очистить график')
b_clear_graph.grid(row=3,column=1)
b_close = tk.Button(fr1,text='Закрыть')
b_close.grid(row=4,column=0)
fr1.pack(anchor='w')


img = tk.PhotoImage(file="pic.png") # загружаем картинку из файла
pict=tk.Canvas(width=738,height=519) # создаем холст, размеры картинки
pict.create_image(10,10,anchor=tk.NW, image = img) # помещаем картинку на холст
pict.pack()#

# b_check_pars.bind('<Button-1>', check)
#
# label_check_pars = tk.Label(text='Проверка ввода = ')
# label_check_pars.grid(row=6,column=0)
# label_checked_pars = tk.Label(text='-')
# label_checked_pars.grid(row=6,column=1)
# b_calculate_tab = tk.Button(text='Рассчитать таблицу значений')
# b_calculate_tab.grid(row=7,column=0)

# b_wr_tab = tk.Button(text='Записать таблицу значений в файл')
# b_wr_tab.pack()
# b_readcalc_tab = tk.Button(text='Считать таблицу значений из файла')
# b_readcalc_tab.pack()
# b_draw_graph = tk.Button(text='Нарисовать график')
# b_draw_graph.pack()
# b_save_graph = tk.Button(text='Сохранить график')
# b_save_graph.pack()
# b_clear_graph = tk.Button(text='Очистить график')
# b_clear_graph.pack()
# b_close = tk.Button(text='Закрыть')
# b_close.pack()

#def input_pars(even):

#b_input_pars.bind('<Button-1>',get)

win.mainloop()