import pygame as py
py.init()

def main():
    sc_width,sc_height=500,500
    screen=py.display.set_mode((sc_width,sc_height))
    py.display.set_caption('color changing sprite')
    colors={
        'red':py.Color('red'),
        'green':py.Color('green'),
        'yellow':py.Color('yellow'),
        'white':py.Color('white'),
        'blue':py.Color('blue'),
        }
    def_color=colors['white']

    x,y=30,30
    sprite_width,sprite_height=60,60
    clock=py.time.Clock()
    done=False
    while not done:
        for event in py.event.get():
            if event.type==py.QUIT:
                done=True
        pressed=py.key.get_pressed()
        if pressed[py.K_LEFT]:
            x-=3
        if pressed[py.K_UP]:
            y-=3
        if pressed[py.K_RIGHT]:
            x+=3
        if pressed[py.K_DOWN]:
            y+=3
        
        x=min(max(0,x), sc_width-sprite_width)
        y=min(max(0,y), sc_height-sprite_height)

        if x==0:
            def_color=colors['blue']
        if y==0:
            def_color=colors['red']
        elif x==sc_width-sprite_width:def_color=colors['yellow']
        elif y==sc_height-sprite_height:def_color=colors['green']

        else:
            def_color=colors['white']
        screen.fill((0,0,0))
        py.draw.rect(screen,def_color,(x,y,sprite_width,sprite_height))
        py.display.flip()
        clock.tick(90)

if __name__=='__main__':
    main()

        

