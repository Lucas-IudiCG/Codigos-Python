N1= int(input())


if N1 > 100 and N1 < 999:
    x = N1//100
    N2 = N1-(x*100)
    y = N2//10
    N3 = N2- (y*10)
    N4 = N2-N3
    N5 = N4/10
    N6= N5/2
    N7 = N5//2

    if N6 == N7:
        print("DEZENA PAR")

    else:
        print("DEZENA IMPAR") 
