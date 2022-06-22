import wrap,time,random
chet=0
balance=6
xspawn=60
yspawn=90
wrap.world.create_world(847,480)
wrap.add_sprite_dir("mysprite")
wrap.world.set_back_image('C:/Users/Tim GF63/Downloads/map2.jpg')
rbp=wrap.sprite.add("player",424,415,"player")
dog=wrap.sprite.add("g.dog",xspawn,yspawn,"g.dog")
goldcow = wrap.sprite.add("g.cow", xspawn, yspawn, "g.cow")
goldcorg=wrap.sprite.add("g.corg",xspawn,yspawn,"g1.crgie")
goldtiger=wrap.sprite.add("g.tigerr",xspawn,yspawn,"tigerr")
wrap.sprite.hide(goldtiger)
wrap.sprite.hide(goldcorg)
wrap.sprite.hide(goldcow)
pet=dog

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
    global chet,balance,pet
    xp=wrap.sprite.get_x(rbp)
    yp=wrap.sprite.get_y(rbp)
    wrap.sprite.move_to(pet,xp-60,yp)
    if chet >=1000 and wrap.sprite.is_collide_point(pet,pos_x,pos_y) and pet==dog:
        wrap.sprite.remove(pet)
        wrap.sprite.show(goldcow)
        pet=goldcow
        balance=21
        chet=chet-1000

    if chet >=3250 and wrap.sprite.is_collide_point(pet,pos_x,pos_y) and pet==goldcow:
        wrap.sprite.remove(pet)
        wrap.sprite.show(goldcorg)
        pet=goldcorg
        balance=75
        chet=chet-3250

    if chet >=12500 and wrap.sprite.is_collide_point(pet,pos_x,pos_y) and pet==goldcorg:
        wrap.sprite.remove(pet)
        wrap.sprite.show(goldtiger)
        pet=goldtiger
        balance=195
        chet=chet-12500


