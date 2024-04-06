def gif ():
    for i in range(0,9):
        frame='frame_0'+str(i)+'_delay-0.08s.gif'
        time.sleep(0.1)
        wn.bgpic(frame)
        wn.update()
    for i in range(10,61):
        frame='frame_'+str(i)+'_delay-0.08s.gif'
        time.sleep(0.1)
        wn.bgpic(frame)
        wn.update()
    clear_spirale()