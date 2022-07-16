import time
def repeat():
    def credits():
        time.sleep(1)
        print("Thanks to...\nJeyu Song, for the original idea\nEdwin Chin, for idea for the story\ndosdude1, so i could download a newer verson of OS X so i could have visual studio 2022\nSean Lee(me) for coding this program. aaaaand...\nYOU for playing this short story.\nTHE END")
    def loss():
        yorn = input("You failed to avenge ningning...\n Try again? [y/n]\n>>> ")
        if yorn == "y":
            repeat()
        if yorn == "n":
            quit()
    def win1():
        print("A funeral was held for the great representative Nabi, he was remembered as a kind and just dog. He aimed for a better future of the country, unlike Joe Biden.\n")
        print("R.I.P\nNabi\n2014-2022")
        credits()
    def start():
            print("THE LEGEND OF DOGS.\n"*100)
            print("Press Enter.")
            input()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print('2019: The dogepocolypse begins. The Dogefia takes over the government. Mochi, President. Ningnings 1,2,3,4,5,6,7,8,9,10,11, and Nabi, House of Representatives. The many Coca, Kiki, Kika, Coca II and kongkang, Senate.')
            input()
            print("Present Day: BREAKING NEWS...\n")
            time.sleep(0.5)
            print("Nabi has been assasinated by the cats.")
            print('Your mission as Mochi is to exterminate the cats.........................')
            input()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    def catfight():
        announce = int(input("1) Announce it to the rest of the dogs\n 2) Announce it to the Dogfia\n 3) Do not Announce.\n>>> "))
        if announce == 1:
            print("You have announced that you would avenge Nabi to all the dogs.")
        if announce == 2:
            print("Many of the Dogfia members agree to avenge Nabi.")
        if announce == 3:
            print("The news has been kept between you and the Ningnings")
            print("You carried out an assult with just the Ningnings and you. The cats vastly outnumbered you.")
            loss()
        if announce == 1 or 2: 
            choice = int(input("\n1) Carry out assult immediately.\n2) Plan out assult.\n>>> "))
            if choice == 1:
                print('There was much backlash from Head General of the Army, Graystone. The assult was carried out. Even though dogs outnumber cats. The cats utelized guerrila warfare. Unfortunately you surrenderd.')    
                loss()
            if choice == 2:
                attacktype = int(input("1) Fight head on.\n2) Surround the cats.\n3) Stealthy approach.\n4) Air\n5) Negotiate\n>>> "))
                if attacktype == 1:
                    if announce != 1:
                        print('The cat army did not plan at all and tried to defend, but your army vastly outnumbered them and you WON!')
                    if announce == 1:
                        print("Since you told the public about your plan to avenge some dogs told the cats and they were expecting you and completely ambushed your troops.")
                        loss()
                if attacktype == 2:
                    if announce != 1:
                        print("The cat caught on too late and you surrounded the entire army and WON!")
                    if announce == 1:
                        print("Since you told the public the only half the army was surrounded and the rest of the cats ambushed the army from outside the surrounded area.")
                        loss()
                if attacktype == 3:
                    print("cats have sharp farsighted vision! they saw your ambush coming and prepared!")
                    loss()
                if attacktype == 4:
                    print("UHHHHHH what?")
                    loss()
                if attacktype == 5:
                    print('The negotiation was going well until an assasin shot you two times in the head.')
                    loss()
    def incastle():
        print("There are dog skulls hung on the wall.")
        time.sleep(1)
        if announce != 1:
            print('You hear muffled yelling from downstairs.')
            save = int(input("1) investigate\n2) leave\n>>> "))
            if save == 1:
                print("You investigate the sound and go downstairs.\n WAIT WHAT you think to yourself as you see Nabi still alive tied up. You untie him and sucessfully free him. Nabi was returned safely to his house and security measures were tightened up to preven this again.")
                print("You finished with the GOOD ENDING :)")
                credits()
            else:
                win1()
        else:
            print('You go downstairs and you find Nabi dead all tied up. You fall on your knees crying for your friend. The cats anticipated the assult and some cats were in the basement and killed you.')
            win1()
    def Rescue():
        time.sleep(0.5)
        print("You have defeated the cats!\n There is a large castle that the cats occupied.")
        castle = int(input("1) Enter the palace \n2) Call it a victory and leave.\n>>>  "))
        if castle == 1:
            print("you entered the castle.")
            incastle()
        if castle == 2:
            win1()
    def main():
        start()
        catfight()
        Rescue()
    main()
repeat()