from pynput.keyboard import Key,Controller
import string
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

special_keylist=special_keymap.keys()
keyboardContoller= Controller()
def execuite(recKey:str,using):
    if recKey=="connected" or recKey.startswith('nickname') or recKey.endswith('left'):
        print(recKey)
        return
    lines=recKey.splitlines()
  
    if(len(lines)<1):
        for line in lines:
            execuite(line,using)
    else:
        key,op= lines[0].split('_=')
        print(f'[{key}, {op}]')
        using.use=True
        if key in special_keylist:
            if op=='P':
                keyboardContoller.press(special_keymap.get(key))
            if op=='R':
                keyboardContoller.release(special_keymap.get(key))  
        if key[1] in string.printable:
            if op=='P':
                keyboardContoller.press(key[1])
            if op=='R':
                keyboardContoller.release(key[1])
        using.use=False
