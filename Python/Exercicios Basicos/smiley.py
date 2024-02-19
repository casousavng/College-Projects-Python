import turtle

def draw_smiley( x, y, r ):

    # cabeça
    turtle.penup()
    turtle.goto( x, y )
    turtle.pendown()
    turtle.color('black', 'yellow')
    turtle.begin_fill()
    turtle.circle( r )
    turtle.end_fill()

    # olho esquerdo
    turtle.penup()
    turtle.goto( x-1/4*2*r, y+2/3*2*r )
    turtle.pendown()
    turtle.color('black', 'black')
    turtle.begin_fill()
    turtle.circle( 0.1*r )
    turtle.end_fill()
    turtle.penup()
   
    # olho direito
    turtle.goto( x, y )
    turtle.goto( x+1/4*2*r, y+2/3*2*r )
    turtle.pendown()
    turtle.color('black', 'black')
    turtle.begin_fill()
    turtle.circle( 0.1*r )
    turtle.end_fill()
    turtle.penup()

    # boca
    turtle.goto( x, y )
    turtle.goto( x-1/4*2*r-5, y+1/3*2*r )
    turtle.pendown()
    turtle.right( 30 )
    turtle.circle( 1.2*r, 60 )
    turtle.penup()
    turtle.goto( 0, 0 )
    
if __name__ == '__main__':
    draw_smiley( 100, 100, 100 )
