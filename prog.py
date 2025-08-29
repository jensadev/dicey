from random import randint
print("Välkommen till rulla tärningsspelet!")
spelare1 = input("Spelare 1, var god skriv ditt namn: ")
print(f"Hej {spelare1}, nu är det dax att rulla tärning.")
spela = True
spelare1_vinster = 0
spelare2_vinster = 0
while spela == True:
    for i in range(3):
        spelare1_slag = randint(1, 6)
        spelare2_slag = randint(1, 6)
        if spelare1_slag > spelare2_slag:
            print(f"{spelare1} krossar den usla datormaskinen!")
            spelare1_vinster += 1
        elif spelare2_slag > spelare1_slag:
            print("Spelare 2 är dig övermäktig, muhahah!")
            spelare2_vinster += 1
        else:
            print("Meh, lika")

    if spelare1_vinster > spelare2_vinster:
        print("Grattis du vann besegrade datorn")
    elif spelare2_vinster > spelare1_vinster:
        print("Datorn besegrade dig")
    else:
        print("Attans, oavgjort")

    spela_igen = input("Vill du köra en till runda? [J/n]")
    if spela_igen.lower() == "n":
        spela = False
        print("Ok, avslutar")
