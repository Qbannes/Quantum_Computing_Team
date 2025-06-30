def istSchaltjahr(jahr: int):
    a = False
    if jahr % 4 == 0:
        a = True
    if jahr % 100 == 0:
        a = False
    if jahr % 400 == 0:
        a = True
    return a


while True:
    jahr = input ("Welches Jahr soll geprüft werden? \"Exit\" um abzubrechen. -")
    if jahr == "Exit":
        break
    print(istSchaltjahr(int(jahr)))
