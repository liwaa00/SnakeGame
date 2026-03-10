from turtle import Turtle
class Snake:#هو ليس سلحفة فقط هو يقوم بتنظيم عرض السلاحف على الشاشة لذالك لا استدعي السلحفة 
    #  (اي لا استخدم الوراثة)
    def __init__(self):
        self.position=[(-40,0),(-20,0),(0,0)]
        self.turtels=[]
        self.create_snake()
        self.head=self.turtels[-1]
        
    def create_snake(self):#snake oluşturmak
        for i in range(len(self.position)):
            new_turtle=Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(self.position[i])
            self.turtels.append(new_turtle)
        
    def move(self):#hareket ettirmek
        for i in range(len(self.turtels)-1):
            self.turtels[i].goto(self.turtels[i+1].pos())
        self.head.forward(20)

    def extend(self):#extend=طول
        new_segment=Turtle("square")#segment=قطعة
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.turtels[0].pos())
        self.turtels.insert(0,new_segment)#sifirinci. indexte bana new_segmenti ekle
        #insert=ادخل

    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def right(self):
        self.head.setheading(0)
    def left(self):
        self.head.setheading(180)
        
