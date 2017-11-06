def get_distance(prev,vel):
    dis = (vel/3600) * 5
    return prev + dis;

def get_temperature(i,prev):
    if(i>=0 and i<60):
        return prev+0.3
    if(i>=60 and i<190):
        return prev+0.1
    else:
        return prev
      

def get_velocity(i,prev):
    if(i>=0 and i<24):
        return prev+2.1
    elif(i>=24 and i<34):
        return prev+1.6
    elif(i>=34 and i<124):
        if((i%2) == 0):
            return prev+0.5
        else:
            return prev-0.5
    elif(i>=124 and i<140):
        return prev+0.5
    elif(i>=140 and i<170):
        return prev-0.5
    elif(i>=170 and i<240):
        if((i%2) == 0):
            return prev+0.5
        else:
            return prev-0.5
    elif(i>=240 and i<270):
        return prev+0.5
    elif(i>=270 and i<300):
        return prev-0.5
    elif(i>=300 and i<400):
        if((i%2) == 0):
            return prev+0.5
        else:
            return prev-0.5
    elif(i>=400 and i<430):
        return prev+0.5
    elif(i>=430 and i<470):
        return prev-0.5
    elif(i>=470 and i<580):
        if((i%2) == 0):
            return prev+0.5
        else:
            return prev-0.5
    elif(i>=580 and i<610):
        return prev+0.5
    elif(i>=610 and i<650):
        return prev-0.5
    elif(i>=650 and i<695):
        if((i%2) == 0):
            return prev+0.5
        else:
            return prev-0.5
    else:
        val = prev-2
        if(val < 0):
            return 0
        else:
            return val

print("################Starting Outpu####################t")
velocity = 0
temperature = 70
distance=10000
for i in range(720):
    velocity = get_velocity(i,velocity)
    temperature = get_temperature(i,temperature)
    distance = get_distance(distance,velocity)
    print(i,velocity,temperature,distance)
