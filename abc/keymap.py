from pynput.keyboard import Key,Controller
special_keymap = {
    "Key.enter" : Key.enter ,
    "Key.esc" : Key.esc ,
    "Key.backspace" : Key.backspace ,
    "Key.tab" : Key.tab ,
    "Key.space" : Key.space ,
    "Key.caps_lock" : Key.caps_lock ,
    "Key.print_screen" : Key.print_screen ,
    "Key.scroll_lock" : Key.scroll_lock ,
    "Key.pause" : Key.pause ,
    "Key.insert" : Key.insert ,
    "Key.home" : Key.home ,
    "Key.page_up" : Key.page_up ,
    "Key.delete" : Key.delete ,
    "Key.end" : Key.end ,
    "Key.page_down" : Key.page_down ,
    "Key.right" : Key.right ,
    "Key.left" : Key.left ,
    "Key.down" : Key.down ,
    "Key.up" : Key.up ,
    "Key.num_lock" : Key.num_lock ,
    "Key.cmd" : Key.cmd ,
    "Key.alt_l" : Key.alt_l ,
    "Key.alt_gr" : Key.alt_gr ,
    "Key.menu" : Key.menu ,
    "Key.shift" : Key.shift ,
    "Key.shift_r" : Key.shift_r ,
    "Key.ctrl_l" : Key.ctrl_l ,
    "Key.ctrl_r" : Key.ctrl_r ,
    "Key.f1":Key.f1,
    "Key.f2":Key.f2,
    "Key.f3":Key.f3,
    "Key.f4":Key.f4,
    "Key.f5":Key.f5,
    "Key.f6":Key.f6,
    "Key.f7":Key.f7,
    "Key.f8":Key.f8,
    "Key.f9":Key.f9,
    "Key.f10":Key.f10,
    "Key.f11":Key.f11,
    "Key.f12":Key.f12,
}
keyboardContoller= Controller()
def execuite(recKey:str):
    if recKey==connected:
        print(recKey)
        return
    lines=recKey.splitlines()
    print(lines)
    if(len(lines)<1):
        for line in lines:
            execuite(l)
    else:
        op,key= lines[1].split('_=')
        print(f'[{key}, {op}]')
