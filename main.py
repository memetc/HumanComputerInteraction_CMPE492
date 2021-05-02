from tkinter import *
from functools import partial
import numpy as np



class PaintApp:


    # Stores current drawing tool used
    drawing_tool = "line"
    option = "draw"
    old_tag = "start"
    new_id = 0
    id=0
    objects = []
    grabbed = False
    grabbed_x1 = 0
    grabbed_x2 = 0
    grabbed_y1 = 0
    grabbed_y2 = 0

    # Tracks whether left mouse is down
    left_but = "up"

    # Tracks x & y when the mouse is clicked and released
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None


    def change_shape(self, num):
        self.option = "draw"
        if num == 0:
            self.drawing_tool = "line"
            root.config(cursor = "pencil")
        elif num == 1:
            self.drawing_tool = "oval"
            root.config(cursor="circle")
        elif num == 2:
            self.drawing_tool = "rectangle"
            root.config(cursor="sizing")
        elif num == 3:
            self.drawing_tool = "square"
            root.config(cursor="dotbox")



    def interact(self, event=None):
        if self.option == "draw":
            if self.drawing_tool == "line":
                tag = str(event.x) + "-" + str(event.y)
                self.x2_line_pt = event.x
                self.y2_line_pt = event.y
                event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=TRUE,
                                         fill="black", tag=tag)
                if self.old_tag != "start":
                    self.drawing_area.delete(self.old_tag)
                self.old_tag = tag

            elif self.drawing_tool == "square":
                tag = str(event.x) + "-" + str(event.y)
                self.x2_line_pt = event.x
                self.y2_line_pt = event.y
                sidex = self.x2_line_pt - self.x1_line_pt
                temp = self.y2_line_pt - self.y1_line_pt
                temp = temp / abs(temp)
                sidey = temp * sidex
                event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt, self.x1_line_pt + sidex,
                                              self.y1_line_pt + sidey, fill="midnight blue", outline="yellow", width=2, tag=tag)


                if self.old_tag != "start":
                    self.drawing_area.delete(self.old_tag)
                self.old_tag = tag

            elif self.drawing_tool == "oval":
                tag = str(event.x) + "-" + str(event.y)
                self.x2_line_pt = event.x
                self.y2_line_pt = event.y
                event.widget.create_oval(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, fill="midnight blue",
                                            outline="yellow",width=2, tag=tag)
                if self.old_tag != "start":
                    self.drawing_area.delete(self.old_tag)
                self.old_tag = tag

            elif self.drawing_tool == "rectangle":
                tag = str(event.x) + "-" + str(event.y)
                self.x2_line_pt = event.x
                self.y2_line_pt = event.y
                event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt,self.x2_line_pt, self.y2_line_pt, fill="midnight blue",outline="yellow",width=2, tag=tag)

                if self.old_tag != "start":
                    self.drawing_area.delete(self.old_tag)
                self.old_tag = tag

        elif self.option == "move":

            id = self.isInside(event.x, event.y)
            object = self.get_item(id)
            r_x = abs(object[2] - object[4]) / 2
            r_y = abs(object[3] - object[5]) / 2
            r_x_line= (object[4] - object[2]) / 2
            r_y_line = (object[5] - object[3]) / 2
            type = object[1]
            tag = str(event.x) + "-" + str(event.y)
            self.drawing_area.delete(id)

            if type == "line":
                print(event.x, "-", event.y)

                new_id = event.widget.create_line(event.x - r_x_line, event.y - r_y_line, event.x + r_x_line, event.y + r_y_line,
                                                  fill="black",
                                                  smooth=True, tag=tag)
            elif type == "oval":
                new_id = event.widget.create_oval(event.x - r_x, event.y - r_y, event.x + r_x, event.y + r_y,
                                                  fill="midnight blue",
                                                  outline="yellow", width=2, tag=tag)
            else:
                new_id = event.widget.create_rectangle(event.x - r_x, event.y - r_y, event.x + r_x, event.y + r_y,
                                         fill="midnight blue",
                                         outline="yellow", width=2, tag=tag)


            if self.old_tag != "start":
                self.drawing_area.delete(self.old_tag)
            self.old_tag = tag
            if r_y_line / r_x_line < 0:
                r_y = 0-r_y
            for i in self.objects:
                if i[0] == id:
                    self.objects.remove(i)
                    temp = []
                    temp.append(new_id)
                    temp.append(type)
                    temp.append(event.x - r_x)
                    temp.append(event.y - r_y)
                    temp.append(event.x + r_x)
                    temp.append(event.y + r_y)

            self.objects.insert(0, temp)
            print(self.objects)


        elif self.option == "erase":
            print(event.x,"-" ,event.y)
            id = self.isInside(event.x, event.y)
            print(id, "--", self.objects, self.drawing_area.find_closest(event.x, event.y))

            for i in self.objects:
                if i[0] == id:
                    self.objects.remove(i)
            self.drawing_area.delete(id)
            self.drawing_area.delete(id-1)

    def get_item(self, id):
        for object in self.objects:
            if object[0] == id:
                return object

    def isInside(self, ex, ey):
        for object in self.objects:
            if object[2]<object[4]:
                small_x=object[2]
                big_x=object[4]
            else:
                small_x = object[4]
                big_x = object[2]
            if object[3]<object[5]:
                small_y=object[3]
                big_y=object[5]
            else:
                small_y = object[5]
                big_y = object[3]

            if object[1] == "oval":
                h = (small_x+big_x)/2
                k = (small_y+big_y)/2
                r_x = h-small_x
                r_y = k-small_y
                isInside = (((ex-h)**2)/(r_x**2)) + (((ey-k)**2)/(r_y**2))

                if isInside <= 1:
                    return object[0]
            elif object[1] == "line":
                h = (small_x + big_x) / 2
                k = (small_y + big_y) / 2
                r_x = h - small_x
                r_y = k - small_y
                isInside = (((ex - h) ** 2) / (r_x ** 2)) + (((ey - k) ** 2) / (r_y ** 2))
                if isInside <= 1:
                    return object[0]
            else:
                if small_x<=ex<=big_x and small_y<=ey<=big_y:
                    return object[0]



        return False

    # ---------- CATCH MOUSE UP ----------

    def left_but_down(self, event=None):
        self.left_but = "down"
        # Set x & y when mouse is clicked
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y


    def left_but_up(self, event=None):
        self.left_but = "up"

        # Reset the line
        self.x_pos = None
        self.y_pos = None

        # Set x & y when mouse is released
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        # If mouse is released and line tool is selected
        # draw the line
        if self.option == "draw":
            if self.drawing_tool == "line":
                self.line_draw(event)
            elif self.drawing_tool == "square":
                self.square_draw(event)
            elif self.drawing_tool == "oval":
                self.oval_draw(event)
            elif self.drawing_tool == "rectangle":
                self.rectangle_draw(event)
        elif self.option == "move":
            self.grabbed = False
            self.old_tag = "start"




    # ---------- DRAW LINE ----------

    def line_draw(self, event=None):

        # Shortcut way to check if none of these values contain None
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            id = event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=TRUE, fill="black")

            shape_info = []
            shape_info.append(id)
            shape_info.append("line")
            shape_info.append(self.x1_line_pt)
            shape_info.append(self.y1_line_pt)
            shape_info.append(self.x2_line_pt)
            shape_info.append(self.y2_line_pt)
            self.objects.append(shape_info)

    # ---------- DRAW OVAL ----------

    def oval_draw(self, event=None):

        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            id = event.widget.create_oval(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt,
                                        fill="midnight blue",
                                        outline="yellow",
                                        width=2)

            shape_info = []
            shape_info.append(id)
            shape_info.append("oval")
            shape_info.append(self.x1_line_pt)
            shape_info.append(self.y1_line_pt)
            shape_info.append(self.x2_line_pt)
            shape_info.append(self.y2_line_pt)
            self.objects.append(shape_info)


    def rectangle_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,self.y2_line_pt):
            id = event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt,self.x2_line_pt, self.y2_line_pt, fill="midnight blue",outline="yellow",width=2)

            shape_info = []
            shape_info.append(id)
            shape_info.append("rectangle")
            shape_info.append(self.x1_line_pt)
            shape_info.append(self.y1_line_pt)
            shape_info.append(self.x2_line_pt)
            shape_info.append(self.y2_line_pt)
            self.objects.append(shape_info)
    def square_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,self.y2_line_pt):
            sidex = self.x2_line_pt - self.x1_line_pt
            temp = self.y2_line_pt - self.y1_line_pt
            temp = temp/abs(temp)
            sidey = temp * sidex
            id = event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt,self.x1_line_pt + sidex, self.y1_line_pt + sidey, fill="midnight blue",outline="yellow",width=2)

            shape_info = []
            shape_info.append(id)
            shape_info.append("square")
            shape_info.append(self.x1_line_pt)
            shape_info.append(self.y1_line_pt)
            shape_info.append(self.x1_line_pt + sidex)
            shape_info.append(self.y1_line_pt + sidey)
            self.objects.append(shape_info)
    def activate_move(self):
        root.config(cursor="hand1")
        self.option = "move"
    def activate_erase(self):
        root.config(cursor="pirate")
        self.option = "erase"

    def __init__(self, root):
        self.root = root
        root.geometry("1500x1000")
        draw_label = Label(root, text="Draw", font='Helvetica 16 bold')
        move_label = Label(root, text="Move", font='Helvetica 16 bold')
        erase_label = Label(root, text="Erase", font='Helvetica 16 bold')

        line_button = Button(root, text="Line", width=10, height=2, command=partial(self.change_shape, 0), cursor="pencil")
        oval_button = Button(root, text="Oval", width=10, height=2, command=partial(self.change_shape, 1), cursor="circle")
        rect_button = Button(root, text="Rectangle", width=10, height=2, command=partial(self.change_shape, 2), cursor="sizing")
        square_button = Button(root, text="Square", width=10, height=2, command=partial(self.change_shape, 3), cursor="dotbox")
        move_button = Button(root, text="Move", width=10, height=2, command=self.activate_move, cursor="hand1")
        erase_button = Button(root, text="Erase", width=10, height=2, cursor="pirate",command=self.activate_erase)

        draw_label.place(x=185,y=20)
        move_label.place(x=600, y=20)
        erase_label.place(x=1000, y=20)

        line_button.place(x=50, y=50)
        oval_button.place(x=140, y=50)
        rect_button.place(x=230, y=50)
        square_button.place(x=320, y=50)
        move_button.place(x=600, y=50)
        erase_button.place(x=1000, y=50)

        self.drawing_area = Canvas(width=1100, height=600, bd=2, bg="#afeeee")
        self.drawing_area.place(x=200, y=150)
        self.drawing_area.create_text(500, 20, fill="darkblue", font="Times 20 italic bold",text="Draw on this canvas")
        self.drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.left_but_up)
        self.drawing_area.bind("<B1-Motion>", self.interact)
        # self.drawing_area.bind("<Enter> ", self.hower)




root = Tk()
paint_app = PaintApp(root)

root.mainloop()