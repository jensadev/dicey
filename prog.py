from random import randint
print("Välkommen till rulla tärningsspelet!")
spelare1 = input("Spelare 1, var god skriv ditt namn: ")
print(f"Hej {spelare1}, nu är det dax att rulla tärning.")
spela = True
while spela == True:
    spelare1_slag = randint(1, 6)
    spelare2_slag = randint(1, 6)
    if spelare1_slag > spelare2_slag:
        print(f"{spelare1} krossar den usla datormaskinen!")
    elif spelare2_slag > spelare1_slag:
        print("Spelare 2 är dig övermäktig, muhahah!")
    else:
        print("Meh, lika")
    spela_igen = input("Vill du spela en runda till? [J/n] ")
    if spela_igen == "n":
        spela = False
# skapa en variabel eller två variabler för att komma ihåg vem som har vunnit