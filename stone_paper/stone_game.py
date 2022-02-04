import tkinter as tk
import random
def say_pass():
    print('pass')
win = tk.Tk()
width = 300                             # ширина
height = 300                            # высота
win.title('камень-ножницы-бумага')      # заголовок окна
win.minsize(width, height)              # минимальные размеры окна
win.maxsize(width*2, height*2)          # максимальные размеры окна
win.resizable(True, True)               # разрешение на изменение окна
win.config(background="WHITE")          # задний фон окна
photo = tk.PhotoImage(file="282.png")   # загружаем фото-картинку через ткинтер
win.iconphoto(False, photo)             # прикрепляем фото-картинку к окну

button1 = tk.Button(win, text='ножницы',
                    command=say_pass)
button2 = tk.Button(win, text='камень',
                    command=say_pass)
button3 = tk.Button(win,text='бумага',
                    command=say_pass)

button1.pack()
button2.pack()
button3.pack()







































win.mainloop()