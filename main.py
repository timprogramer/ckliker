import wrap,time,random
chet=0
balance=6
wrap.world.create_world(920,480)
wrap.world.set_back_color(255,255,255)
wrap.add_sprite_dir("mysprite")
dog=wrap.sprite.add("g.dog",60,90,"g.dog")
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def cklic():
    global chet
    chet=chet+balance
    print(chet)
@wrap.always()
def always(pos_x,pos_y):
    global chet
    if chet >=1000 and wrap.sprite.is_collide_point(dog,pos_x,pos_y)  :
        wrap.sprite.remove(dog)
        wrap.sprite.add()
