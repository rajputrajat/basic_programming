import turtle
turtle.color('red', 'yellow')
# color(1.0, 1.0, 0.0)
turtle.begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()