def draw_branch(t, length, level):
    if level == 0:
        return

    t.forward(length)

    t.left(45)
    draw_branch(t, length * 0.67, level - 1)
    
    t.right(90)
    draw_branch(t, length * 0.67, level - 1)
    
    t.left(45)
    t.backward(length)

def draw_fractal_circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    
    t.circle(radius)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.left(90)
    draw_branch(t, radius // 2, 5)
    t.right(90)
