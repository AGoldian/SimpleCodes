from tkinter import *

root = Tk()
root.title('Болтовое соединение')
root.geometry('1000x700')
root.resizable(0, 0)
root.iconphoto(False, PhotoImage(file='logo.png'))


w = 500
h = 400
first_proection = Canvas(root, width=w, height=h, bg='white')
first_proection.place(x=25, y=250)

w2 = 400
h2 = 400
second_proection = Canvas(root, height=h2, width=w2, bg='white')
second_proection.place(x=575, y=250)


class Draw:
    def __init__(self, flanges, d_bolt, size_for_key=0):
        self.flanges = float(flanges)
        self.d_bolt = float(d_bolt)
        self.size_for_key = float(size_for_key)

    def shading_rectangle(self, left_x, bottom_y, up_y, right_x):
        for i in range(0, int(self.flanges), 5):
            first_proection.create_line(left_x + i, bottom_y,
                                        left_x, bottom_y - i)
            first_proection.create_line(left_x + i, up_y,
                                        right_x, bottom_y - i)

    def drawing_first_projection(self):
        first_proection.delete('all')

        # Other
        first_proection.create_rectangle(w / 2 + self.flanges, h / 2 + 2 * self.d_bolt,
                                         w / 2 + self.flanges + 1.4 * self.d_bolt, h / 2 - 2 * self.d_bolt)
        first_proection.create_rectangle(w / 2 + self.flanges, h / 2 + self.d_bolt,
                                         w / 2 + self.flanges + 1.4 * self.d_bolt, h / 2 - self.d_bolt)
        first_proection.create_rectangle(w / 2 - self.flanges, h / 2 + 2.4 * self.d_bolt,
                                         w / 2 - self.flanges - 0.3 * self.d_bolt, h / 2 - 2.4 * self.d_bolt)
        first_proection.create_rectangle(w / 2 - self.flanges - 0.3 * self.d_bolt, h / 2 + 2 * self.d_bolt,
                                         w / 2 - self.flanges - 1.9 * self.d_bolt, h / 2 - 2 * self.d_bolt)
        first_proection.create_rectangle(w / 2 - self.flanges - 0.3 * self.d_bolt, h / 2 + self.d_bolt,
                                         w / 2 - self.flanges - 0.3 * self.d_bolt - 2 * self.d_bolt,
                                         h / 2 - self.d_bolt)

        # Flanges
        first_proection.create_rectangle(w / 2 - self.flanges, h / 2 + self.d_bolt,
                                         w / 2 + self.flanges, h / 2 + self.d_bolt + self.flanges)
        first_proection.create_line(w / 2, h / 2 + self.d_bolt,
                                    w / 2, h / 2 + self.d_bolt + self.flanges)
        first_proection.create_rectangle(w / 2 - self.flanges, h / 2 - self.d_bolt,
                                         w / 2 + self.flanges, h / 2 - self.d_bolt - self.flanges)
        first_proection.create_line(w / 2, h / 2 - self.d_bolt,
                                    w / 2, h / 2 - self.d_bolt - self.flanges)

        # Upper left square
        Draw.shading_rectangle(self, left_x=w / 2 - self.flanges, bottom_y=h / 2 - self.d_bolt,
                               up_y=h / 2 - self.d_bolt - self.flanges, right_x=w / 2)

        # Upper right square
        Draw.shading_rectangle(self, left_x=w / 2, bottom_y=h / 2 - self.d_bolt,
                               up_y=h / 2 - self.d_bolt - self.flanges, right_x=w / 2 + self.flanges)

        # Down left square
        Draw.shading_rectangle(self, left_x=w / 2 - self.flanges, bottom_y=h / 2 + self.d_bolt + self.flanges,
                               up_y=h / 2 + self.d_bolt, right_x=w / 2)

        # Down right square
        Draw.shading_rectangle(self, left_x=w / 2, bottom_y=h / 2 + self.d_bolt + self.flanges,
                               up_y=h / 2 + self.d_bolt, right_x=w / 2 + self.flanges)

    def drawing_second_projection(self):
        second_proection.delete('all')
        second_proection.create_polygon(w2 / 2, h / 2 + self.size_for_key,
                                        w2 / 2 + self.size_for_key, h2 / 2 + self.size_for_key / 2,
                                        w2 / 2 + self.size_for_key, h2 / 2 - self.size_for_key / 2,
                                        w2 / 2, h / 2 - self.size_for_key,
                                        w2 / 2 - self.size_for_key, h2 / 2 - self.size_for_key / 2,
                                        w2 / 2 - self.size_for_key, h2 / 2 + self.size_for_key / 2,
                                        fill='white',
                                        outline='black')
        second_proection.create_oval(w2 / 2 + self.d_bolt / 2, h / 2 + self.d_bolt / 2,
                                     w2 / 2 - self.d_bolt / 2, h / 2 - self.d_bolt / 2)
        second_proection.create_rectangle(w2 / 2 - 1.5 * self.size_for_key, h / 2 + self.flanges + self.d_bolt,
                                          w2 / 2 + 1.5 * self.size_for_key, h / 2 - self.flanges - self.d_bolt)


def output_draw():
    f = enter_f.get()
    d = enter_d.get()
    s = enter_s.get()
    scale = enter_scale.get()
    # crutch
    try:
        Draw(f, d, s).drawing_first_projection()
        Draw(f, d, s).drawing_second_projection()
        for aboba in first_proection.find_all():
            first_proection.scale(aboba, w / 2, h / 2, scale, scale)
        for rtf in second_proection.find_all():
            second_proection.scale(rtf, w2/2, h2/2, scale, scale)
    except ValueError:
        pass


def calculation_bolt_length():
    f = float(enter_f.get())
    ts = float(enter_ts.get())
    m = float(enter_m.get())
    d = float(enter_d.get())
    try:
        length_bolt = 2 * f + ts + m + 0.3 * d
        output_i.set(length_bolt)

        Label(root,
              text=f'Болт М{d} x {round(length_bolt, 2)} ГОСТ 7798-70  |  Гайка М{d} x {round(m / d, 2)} ГОСТ 5915-70 '
                   f' |  Шайба 1.{d}.01 ГОСТ 11371-78',
              font='Roboto 10').place(x=90, y=665)
    except ValueError:
        pass


Label(root, text='Фланцы (F)', font='Roboto 15').grid(row=0, column=0)
enter_f = Entry(root, width=8)
enter_f.grid(row=0, column=1)
Label(root, text='Диаметр болта (d)', font='Roboto 15').grid(row=1, column=0)
enter_d = Entry(root, width=8)
enter_d.grid(row=1, column=1)
Label(root, text='Размер под ключ (S)', font='Roboto 15').grid(row=2, column=0)
enter_s = Entry(root, width=8)
enter_s.grid(row=2, column=1)
Label(root, text='Толщина головки (H)', font='Roboto 15').grid(row=3, column=0)
enter_h = Entry(root, width=8)
enter_h.grid(row=3, column=1)
Label(root, text='Диаметр окружности (D)', font='Roboto 15').grid(row=4, column=0)
enter_do = Entry(root, width=8)
enter_do.grid(row=4, column=1)
Label(root, text='Высота гайки (m)', font='Roboto 15').grid(row=5, column=0)
enter_m = Entry(root, width=8)
enter_m.grid(row=5, column=1)
Label(root, text='Толщина шайбы (S)', font='Roboto 15').grid(row=6, column=0)
enter_ts = Entry(root, width=8)
enter_ts.grid(row=6, column=1)

Button(root, text='Длина болта (I):', font='Roboto 15', command=calculation_bolt_length).place(x=500, y=200)
output_i = StringVar()
Message(root, textvariable=output_i, font='Roboto 15').place(x=670, y=207)

Button(root, text='Построить чертёж', font='Roboto 15', command=output_draw).place(x=300, y=200)

Label(root, text='Госты:', font='Roboto 15').place(x=15, y=660)
Label(root, font='GOST 10').place(x=90, y=660)

Label(root, text='Масштабирование:', font='Roboto 15').place(x=350, y=100)
enter_scale = Entry(root, width=5)
enter_scale.place(x=550, y=107)


def variant():
    first_proection.delete('all')
    second_proection.delete('all')
    first_proection.create_text(w / 2, h / 2, text='Серов А.И.', font='ROBOTO 20')
    second_proection.create_text(w2 / 2, h2 / 2, text='Вариант №9', font='ROBOTO 20')


Button(root, text='Вариант', font='Roboto 15', command=variant).place(x=900, y=10)

root.mainloop()
