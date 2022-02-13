import turtle
# Recursion
# The sum of the elements of the list
# li = [1, 3, 5, 7, 9, 10]
#
#
# def sum_list(arr):
#     if len(arr) == 1:
#         return arr[0]
#     return arr[0] + sum_list(arr[1:])
#
#
# print(sum_list(li))

# Convert integer number to string (base 2 - 16)


# def convert(n, base):
#     st = "0123456789ABCDEF"
#     if n < base:
#         return st[n]
#     # return convert(n // base, base) + convert(n % base, base)
#     return convert(n // base, base) + st[n % 2]
#
#
# print(convert(10, 2))

# String reverse

# def reversed_st(s):
#     if len(s) == 1:
#         return s[-1]
#     return s[-1] + reversed_st(s[:-1])
#
#
# print(reversed_st('abcde'))

# Visualization of recursion

# myturtle = turtle.Turtle()
# mywin = turtle.Screen()
#
#
# def drawspiral(myturtle, lineLen):
#     if lineLen > 0:
#         myturtle.forward(lineLen)
#         myturtle.right(90)
#         drawspiral(myturtle, lineLen - 5)
#
#
# drawspiral(myturtle, 100)
# mywin.exitonclick()

# def tree(branchLen, t):
#     if branchLen > 5:
#         t.forward(branchLen)
#         t.right(20)
#         tree(branchLen - 15, t)
#         t.left(40)
#         tree(branchLen - 15, t)
#         t.right(20)
#         t.backward(branchLen)
#
#
# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("green")
#     tree(75, t)
#     myWin.exitonclick()
#
#
# main()

# The Sierpinski triangle


# def drawTriangle(points, color, myTurtle):
#     myTurtle.fillcolor(color)
#     myTurtle.up()
#     myTurtle.goto(points[0][0], points[0][1])
#     myTurtle.down()
#     myTurtle.begin_fill()
#     myTurtle.goto(points[1][0], points[1][1])
#     myTurtle.goto(points[2][0], points[2][1])
#     myTurtle.goto(points[0][0], points[0][1])
#     myTurtle.end_fill()
#
#
# def getMid(p1, p2):
#     return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
#
#
# def sierpinski(points, degree, myTurtle):
#     colormap = ['blue', 'red', 'green', 'white', 'yellow',
#                 'violet', 'orange']
#     drawTriangle(points, colormap[degree], myTurtle)
#     if degree > 0:
#         sierpinski([points[0],
#                     getMid(points[0], points[1]),
#                     getMid(points[0], points[2])],
#                    degree - 1, myTurtle)
#         sierpinski([points[1],
#                     getMid(points[0], points[1]),
#                     getMid(points[1], points[2])],
#                    degree - 1, myTurtle)
#         sierpinski([points[2],
#                     getMid(points[2], points[1]),
#                     getMid(points[0], points[2])],
#                    degree - 1, myTurtle)
#
#
# def main():
#     myTurtle = turtle.Turtle()
#     myWin = turtle.Screen()
#     myPoints = [[-100, -50], [0, 100], [100, -50]]
#     sierpinski(myPoints, 3, myTurtle)
#     myWin.exitonclick()
#
#
# main()
