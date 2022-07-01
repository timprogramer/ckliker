import wrap,time,random
wrap.world.create_world(847,480)
chet=0
balance=6
chengebalance=balance*4
xspawn=60
yspawn=90
wrap.add_sprite_dir("mysprite")
wrap.world.set_back_image('C:/Users/Tim GF63/Downloads/map2.jpg')
trv=wrap.sprite.add("traveler",800,415,"brook")
textobloko=wrap.sprite.add("traveler",780,210,"text")
rbp=wrap.sprite.add("player",424,415,"player")
dog=wrap.sprite.add("g.dog",xspawn,yspawn,"1")
buy=1000

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def cklic():
    global chet
    chet=chet+balance
    print(chet)

@wrap.on_key_always(wrap.K_RIGHT)
def right():
    global rbp
    wrap.sprite.move(rbp,10,0)

@wrap.on_key_always(wrap.K_LEFT)
def left():
    global rbp
    wrap.sprite.move(rbp,-10,0)

@wrap.on_key_always(wrap.K_UP)
def up():
    global rbp
    wrap.sprite.move(rbp,0,-10)

@wrap.on_key_always(wrap.K_DOWN)
def down():
    global rbp
    wrap.sprite.move(rbp,0,10)


@wrap.always()
def always(pos_x,pos_y):
    global chet,balance,pet,buy
    xp=wrap.sprite.get_x(rbp)
    yp=wrap.sprite.get_y(rbp)
    wrap.sprite.move_to(dog,xp-60,yp)
    if chet >=buy and wrap.sprite.is_collide_point(dog,pos_x,pos_y) :
        wrap.sprite.set_costume_next(dog)
        balance=chengebalance
        chet=chet-buy
        buy=buy+1500
    # if wrap.sprite.is_collide_sprite(trv,rbp):
