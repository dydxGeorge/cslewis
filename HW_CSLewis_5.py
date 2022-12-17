global gravity
gravity=9.8 #gravity = 9.8 (m/s^2)

# falling_distance takes t in seconds as input.
def falling_distance(t):
    d=.5*gravity*(t*t)
    return(d)

def main():
    print("enter the time in seconds that the object has been falling.")
    t = int(input())
    answer = falling_distance(t)
    print("the distance the object was falling was", answer)
    return 0

if __name__=="__main__":
    main()