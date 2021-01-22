# This programm shall be translated into C for the arduino.
# Note: For educational purposes this implementation is not pythonic!
# For the same reason no comments are included here.

values=[934,-3623,12,-432,0,83,253,7653,-1837,26,845,-24,-135,-8218,4251,124,-252,-25123,1412,29897,'end']

def getSize(l):
    i=0
    while isinstance(l[i],int):
        i+=1
    return i

def program(values):
    result=0
    i=0
    while(i<getSize(values)):
        j=0
        while(j<=abs(values[i])):
            result+=j
            j+=1
        i+=1
    i=0
    while(i<getSize(values)):
        x,y,z=0,0,0
        j=1
        while(j<=abs(values[i])):
            k=1
            while(k<=abs(values[i])):
                l=1
                while(l<=abs(values[i])):
                    z=x*y
                    l+=1
                y+=1
                x+=k
                k+=1
            x=0
            z=y
            j+=1
        result+=x+y+z
        i+=1
    i=0
    while(i<getSize(values)):
        if values[i] < 0:
            values[i]+=1
            result-=1
        elif values[i] > 0:
            values[i]-=1
            result+=1
        else:
            i+=1
    return result

print(program(values))
