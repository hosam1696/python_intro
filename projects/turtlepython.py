import turtle


class Draw_turtle():

    def __init__(self):
        self.window = turtle.Screen()
        self.hosam = turtle.Turtle()
        self.init_window()
        self.render()

    def init_window(self):
        self.window.screensize(canvwidth=200, canvheight=200)
        self.window.bgcolor('#333333')
        self.hosam.color('#eeeeee')
        self.hosam.shape('turtle')
        self.hosam.color('yellow')
        self.hosam.fillcolor('white')
        self.hosam.speed(10)

    def render(self):
        self.loop_in_circle(self.draw_rectangle)
        """self.hosam.begin_fill()
        self.hosam.end_fill()"""
        self.window.exitonclick()

    @staticmethod
    def draw_square(turtle):
        for i in range(0, 4):
            turtle.fd(100)
            turtle.right(90)

    def draw_rectangle(self, turtle):
        for i in range(0, 2):
            turtle.fd(100)
            turtle.right(120)
        turtle.fd(100)


    def loop_in_circle(self, cb):
        for i in range(0, 360, 10):
            self.hosam.right(i+120)
            cb(self.hosam)
            self.hosam.left(i)

drawturtle = Draw_turtle()

def log_name(name: str, age: int):
    print(f'> Name: {name}\n>Age: {age}')

log_name(545, 545)

million = 1_000_000

