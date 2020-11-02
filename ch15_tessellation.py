import math
import cmath
import cairo


#Define the configuration of the image. 
canvas_size = (500, 500)
numberSubdivisions = 4


#Define the Golden Ratio - gr
gr = (1 + math.sqrt(5)) / 2

def subdivide(triangles):
    result = []
    for color, A, B, C in triangles:
        if color == 0:
            P = A + (B - A) / gr
            result += [(0, C, P, B), (1, P, C, A)]
        else:
            Q = B + (A - B) / gr
            R = B + (C - B) / gr
            result += [(1, R, C, A), (1, Q, R, B), (0, R, Q, A)]
    return result

#Wheel of teal triangles
triangles = []
for i in range(10):
    B = cmath.rect(1, (2*i - 1) * math.pi / 10)
    C = cmath.rect(1, (2*i + 1) * math.pi / 10)
    if i % 2 == 0:
        B, C = C, B  # Make sure to mirror every second triangle
    triangles.append((0, 0j, B, C))

for i in range(numberSubdivisions):
    triangles = subdivide(triangles)

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas_size[0], canvas_size[1])
cr = cairo.Context(surface)
cr.translate(canvas_size[0] / 2.0, canvas_size[1] / 2.0)
wheelRadius = 1.2 * math.sqrt((canvas_size[0] / 2.0) ** 2 + (canvas_size[1] / 2.0) ** 2)
cr.scale(wheelRadius, wheelRadius)

#Define the teal triangles
for color, A, B, C in triangles:
    if color == 0:
        cr.move_to(A.real, A.imag)
        cr.line_to(B.real, B.imag)
        cr.line_to(C.real, C.imag)
        cr.close_path()
cr.set_source_rgb(.2, .8, .8)
cr.fill()    

#Define the purple triangles
for color, A, B, C in triangles:
    if color == 1:
        cr.move_to(A.real, A.imag)
        cr.line_to(B.real, B.imag)
        cr.line_to(C.real, C.imag)
        cr.close_path()
cr.set_source_rgb(0.7, 0, 0.7)
cr.fill()

color, A, B, C = triangles[0]
cr.set_line_width(abs(B - A) / 10.0)
cr.set_line_join(cairo.LINE_JOIN_ROUND)

#Triangle borders
for color, A, B, C in triangles:
    cr.move_to(C.real, C.imag)
    cr.line_to(A.real, A.imag)
    cr.line_to(B.real, B.imag)
cr.set_source_rgb(0.3, 0.5, 0.3)
cr.stroke()

surface.write_to_png('tessellation.png')
