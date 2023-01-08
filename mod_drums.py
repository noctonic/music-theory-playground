for z in range(1,256):
    for y in range(0,256):
        pattern = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for x in range(0,256):
            #print(x,y,z)
            pattern[(((x * y)//z)%17)] = 1
        print(pattern[1:])