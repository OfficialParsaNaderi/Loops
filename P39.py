from turtle import pensize,color,bgcolor,shape,penup,fd,lt,pendown,done
pensize(width=10)
color("white")
bgcolor("red")
shape("turtle")
penup()
fd(-200)
pendown()
for x in range(3):
    fd(100)
    lt(120)
color("cyan")
done()