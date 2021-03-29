# Importations des librairies nécessaires
from random import randint
import os
import sys
import random
from IPython.display import clear_output
import time
import unicodedata
def tim10 ():
  time.sleep(10)
  clear_output()
def tim5 ():
  time.sleep(5)
  clear_output()
def clear():
  clear_output()
  time.sleep(.01)


# Main
def main():
    # Main menu
    leaveGame = False
    while leaveGame == False:
      print()
      print("  الرق والاتجار بالرقيق بجميع صورهما ")
      print()
      print("           🏜️ DUNE 2020  ")
      print()
      print("           .: 1° Jouer")
      print("           .: 2° Reprendre")
      print("           .: 3° À propos")
      print("           .: 4° Sortir")
      print()
      print(" يجوز استرقاق أحد أو استعباده، ويحظر ")
      print()
      option = input(" > ")
      if option == "1":
        playGame(True)
      elif option == "2":
        print("\n Nous ne pouvons pas le faire sur Colab...")
        time.sleep(2)
        main()
        
      elif option == "3":
        credit()
      elif option == "4":
        clear_output()
        print("Êtes-vous sûr de vouloir quitter le jeu?")
        print("1° Oui")
        print("2° Non")
        option = input(" \n> ")
        if option == "1":
          clear_output()
          print("Fin du Programme, à bientôt...")
          SystemExit
        elif option == "2":
          main()
        else:
          clear_output()
          print("! Erreur veuillez choisir la bonne option !")
          time.sleep(3)
          clear_output()
          main()
      else:
        clear_output()
        print(" ! Erreur veuillez choisir la bonne option !")
        time.sleep(3)
        clear_output()
        main()
def credit ():
  clear()
  print("\n    Réalisé par : Amine NAIRI et Nassim YAZI, étudiants en WEB1 à HETIC")

  print("\n Nous sommes fières d’avoir réalisé ce projet, un jeu de rôle inspiré du roman Dune de Frank Herbert et du film Azur et Asmar.")
  print(" La consigne fut donnée par notre intervenant Loic JANIN. Ce projet nous a fait mûrir, progresser en python et dans le travail de groupe.")
  print(" Temps de réalisation, 2 mois.")
  print(" Vous y découvrirez un monde qui ressemble étrangement au désert algérien, pour un léger clin d'œil à nos origines.")

  print("\n Essayez de trouver tous les Easter Eggs ;)")

  print("\n  Remerciement vont à :")
  print(" un proche d’Amine pour son aide dans la réflexion sur la partie code, et Loic JANIN pour la transmission de son savoir...")
  print("\n\n Petit cadeau : https://www.youtube.com/watch?v=ZOfZAf77HUA")
  print("\n\n    Tout droit réservé…")
  input("\n      appuyer sur entrer pour retouner au menu")
  clear()
  main()

# Cette fonction est appelé pour jouer une partie (nouvellement créée ou chargée)
def playGame(newGame):
    # General objects
    inventoryObject_PotionHealth = {"name": "Health Potion", "type": "potion", "healthPointsGained": 25}
    inventoryObject_AttackBoost = {"name": "Attack Boost", "type": "atkBoost", "boostValue": 25}
    inventoryObject_DefenseBoost = {"name": "Defense Boost", "type": "defBoost", "boostValue": 25}

    bossPositionOnMap = {"coordX" : 0, "coordY" : 2}
    boss = {"name" : "Ver des sables",
            "level" : 5,
            "health": 200,
            "attack": 150,
            "defense": 150}

    basicEnnemy = {"name": "Contre-Bandier",
                   "level" : 1,
                   "health": 50,
                   "attack": 75,
                   "defense": 75}

    mediumEnnemy = {"name": "Orc",
                   "level": 2,
                   "health": 75,
                   "attack": 100,
                   "defense": 100}

    hardEnnemy = {"name": "Corrinos",
                   "level": 3,
                   "health": 100,
                   "attack": 125,
                   "defense": 125}

    # If new game, we initialise the main objects like the character stats and the map
    if newGame == True:
      def pre_intro ():
        def ask_gamer_name ():
          clear()
          print("\n  Salut à toi jeune aventurier !!")
          print("    Dis moi, quel est ton nom ?")
          option = input(" \n> ")
          global PlayerID
          PlayerID = option
        ask_gamer_name()
        clear()
        print("\n Bienvenue", PlayerID,", tu vas entrer dans un monde merveilleux et plein de surprises t'attendent...")
        input("\n       (Appuie sur entrer pour commencer) ")
      pre_intro()
      clear()
      #opening Crawl
      def OpeningCrawl ():
        clear()
        print('\033[36m'+"\n\n     Il y a bien longtemps, dans une galaxie lointaine, très lointaine.... \n\n")
        tim5()

        print("\n\n Dans une époque de Croisade, une guerre sanglante fait rage dans la Planète "+'\033[31m'+"Arrakis"+'\033[0m'".")
        print(" Deux grandes Maisons, Ordos et Harkonnen, se font faces pour la convoitise de "+'\033[33m'+"l’Épice"+'\033[0m'+",") 
        print(" une ressource qui donnerai la victoire stratégiquement à celui qui en détiendrait.\n")
        tim10()

        print("\nUne plaisibe cité ,Atréides, où régné la paix, l'éducation, la culture près de la province d'Izmir, dirigée par l'Emir Leto.") 
        print("Mais le Khalife d'Harkonnen décida d'attaquer la cité près d'Izmir, avec sa grande armée et des mercenaires, pour avoir un avantage géographique.")
        print("\nIl en profita pour assassiner Leto, épouser sa femme Jessica de force, et il banni de la cité en épargnant son fils hétitier du trône: "+'\033[37m'+PlayerID+'\033[0m')
        print()
        print("  Te voilà perdu au fin fond du désert d'Arrakis...")
        input("\n (Appuie sur entrer pour commencer) ")
        clear()
      OpeningCrawl()
    
      character = {"name": PlayerID,
                    "level": 1,
                    "currentExp": 0,
                    "nextLevelExp": 20,
                    "health": 1000,
                    "attack": 300,
                    "defense": 100,
                    "currentPositionOnMap" : {"coordX" : 2, "coordY" : 2},  # on mets les coordonnées de la case où on commence, ici au milieu
                    "inventory": []}
        #character["inventory"].append(inventoryObject_AttackBoost.copy())

      gameMap = [[{"symbol" : ' ', "isACase" : False, "completed" : False}, {"symbol" : ' ', "isACase" : False, "completed" : False}, {"symbol" : '#', "isACase" : True, "completed" : False}, {"symbol" : ' ', "isACase" : False, "completed" : False}, {"symbol" : ' ', "isACase" : False, "completed" : False}],
                  [{"symbol" : ' ', "isACase" : False, "completed" : False}, {"symbol" : '#', "isACase" : True, "completed" : False}, {"symbol" : '#', "isACase" : True, "completed" : False}, {"symbol" : '#', "isACase" : True, "completed" : False}, {"symbol" : ' ', "isACase" : False, "completed" : False}],
                  [{"symbol" : '#', "isACase" : True, "completed" : False}, {"symbol" : '#', "isACase" : True, "completed" : False}, {"symbol" : '+', "isACase" : True, "completed" : True}, {"symbol" : '#', "isACase" : True, "completed" : False}, {"symbol" : '#', "isACase" : True, "completed" : False}],
                  [{"symbol" : ' ', "isACase" : False, "completed" : False}, {"symbol" : '#', "isACase" : True, "completed" : False}, {"symbol" : '#', "isACase" : True, "completed" : False}, {"symbol" : '#', "isACase" : True, "completed" : False}, {"symbol" : ' ', "isACase" : False, "completed" : False}],
                  [{"symbol" : ' ', "isACase" : False, "completed" : False}, {"symbol" : ' ', "isACase" : False, "completed" : False}, {"symbol" : '#', "isACase" : True, "completed" : False}, {"symbol" : ' ', "isACase" : False, "completed" : False}, {"symbol" : ' ', "isACase" : False, "completed" : False}]]

  

    # BOUCLE DE JEU : on joue tant que l'utilisateur n'a pas demandé à quitter OU qu'il n'a pas battu le boss final
    continuePlaying = True
    while continuePlaying == True and boss["health"] > 0:
        # On affiche la map et on demande à l'utilisateur ce qu'il veut faire
        printMap(gameMap, character["currentPositionOnMap"]["coordX"], character["currentPositionOnMap"]["coordY"])
        userChoice = printGameMenu()
        moving = False  # par défaut, à chaque tour
        previousCoordX = character["currentPositionOnMap"]["coordX"]
        previousCoordY = character["currentPositionOnMap"]["coordY"]

        # Tests de son choix
        if userChoice == "N" or userChoice == "n":
            # On vérifie si on peut se déplacer
            caseX = character["currentPositionOnMap"]["coordX"] - 1
            caseY = character["currentPositionOnMap"]["coordY"]
            if caseX >= 0 and gameMap[caseX][caseY]["isACase"] == True:
                print("vous allez au nord !")
                moving = True
            else:
                print("Vous ne pouvez pas aller au nord de vôtre position actuelle.")

        elif userChoice == "W" or userChoice == "w":
            # On vérifie si on peut se déplacer
            caseX = character["currentPositionOnMap"]["coordX"]
            caseY = character["currentPositionOnMap"]["coordY"] - 1
            if caseY >= 0 and gameMap[caseX][caseY]["isACase"] == True:
                print("Vous allez à l'ouest !")
                moving = True
            else:
                print("Vous ne pouvez pas aller à l'ouest de vôtre position actuel.")

        elif userChoice == "E" or userChoice == "e":
            # On vérifie si on peut se déplacer
            caseX = character["currentPositionOnMap"]["coordX"]
            caseY = character["currentPositionOnMap"]["coordY"] + 1
            if caseY < len(gameMap[caseX]) and gameMap[caseX][caseY]["isACase"] == True:
                print("Vous allez à l'est !")
                moving = True
            else:
                print("Vous ne pouvez pas aller à l'ouest de vôtre position actuelle.")


        elif userChoice == "S" or userChoice == "s":
            # On vérifie si on peut se déplacer
            caseX = character["currentPositionOnMap"]["coordX"] + 1
            caseY = character["currentPositionOnMap"]["coordY"]
            if caseX < len(gameMap) and gameMap[caseX][caseY]["isACase"] == True:
                print("Vous allez au Sud !")
                moving = True
            else:
                print("Vous ne pouvez pas aller plus au Sud de vôtre position.")

        # Si on veut sauvegarder
        elif userChoice == "V":
            print("On ne malheureusement peut pas sauvegarder sur colab...")

        # Si on veut quitter
        elif userChoice == "Q":
            print("Etes-vous certain de vouloir quitter le jeu? ?\n1.  Oui\n2.  Non")
            userChoice = input("> ")

            if userChoice == "1":
                print("Vous quittez le jeu")
                continuePlaying = False
            elif userChoice == "2":
                print("Vous ne quittez pas le jeu. vous revenez au menu precedent...")
            else:
                print("Votre option est invalide.")

        else:
            print("Option invalide. Les seuls options possible sont celles ci : N (Aller au nord), W (Aller à l'ouestt), E (Aller à l'est), S (Aller au sud), V (Sauvgarder même si c'est impossible sur colab), Q (Quitter le jeu).\n")


        # Si on se déplace, on va lancer un évènement
        if moving == True :
            # On met à jour la position du personnage
            character["currentPositionOnMap"]["coordX"] = caseX
            character["currentPositionOnMap"]["coordY"] = caseY

            # Si la case n'a pas été complétée, on lance un évènement
            if gameMap[caseX][caseY]["completed"] == False:
                # On vérifie si c'est la case du boss
                if caseX == bossPositionOnMap["coordX"] and caseY == bossPositionOnMap["coordY"]:
                    character, fightState = fight(character, boss)

                    # Si le boss final a été vaincu
                    if fightState == "ended":
                        print("\n\n   Félicitation ! Tu as battu le Boss !")
                        boss["health"] = 0
                        # On marque la case comme complétée
                        gameMap[caseX][caseY]["completed"] = True

                    # Si on a fui le combat
                    elif fightState == "escaped":
                        print("Vous esquivez le combat ! Vous retournez à vôtre précedente position")
                        character["currentPositionOnMap"]["coordX"] = previousCoordX
                        character["currentPositionOnMap"]["coordY"] = previousCoordY

                    # Si on est mort
                    elif fightState == "dead":
                        print("Vous avez perdu ! vous retournez au menu principal !")
                        time.sleep(2)
                        return

                else:
                    probaFight = 60
                    probaObject = 40
                    proba = randint(1, 100)
                    #print(proba)

                    # Find an object
                    if proba <= probaObject:
                        print("\nVous trouvez un object : ", end="")
                        proba2 = randint(0, 2)
                        if proba2 == 0:
                            character["inventory"].append(inventoryObject_PotionHealth.copy())
                            print(f'{inventoryObject_PotionHealth["name"]}')
                        elif proba2 == 1:
                            character["inventory"].append(inventoryObject_AttackBoost.copy())
                            print(f'{inventoryObject_AttackBoost["name"]}')
                        elif proba2 == 2:
                            character["inventory"].append(inventoryObject_DefenseBoost.copy())
                            print(f'{inventoryObject_DefenseBoost["name"]}')
                        # On marque la case comme complétée
                        gameMap[caseX][caseY]["completed"] = True

                    # Have a fight
                    else:
                        character, fightState = fight(character, basicEnnemy.copy())

                        # Si on a gagné le combat, l'évènement est terminé
                        if fightState == "ended":
                            # On marque la case comme complétée
                            gameMap[caseX][caseY]["completed"] = True

                        # Si on a fui le combat
                        elif fightState == "escaped":
                            print("\n Tu as fui le combat, tu as déshonoré ta famille !! Retour à la position précèdente...")
                            character["currentPositionOnMap"]["coordX"] = previousCoordX
                            character["currentPositionOnMap"]["coordY"] = previousCoordY

                        # Si on est mort
                        elif fightState == "dead":
                            print("Game Over ! Retourner au menu !")
                            return

            # Sinon la case a déjà été faite, on affiche juste un message
            else:
                print("\n Vous êtes deja venu ici auparavant. ")


        print("\n")



def printMap(_map, playerCoordX, playerCoordY):
    print("\n   ARRAKIS\n")
    print("=============")
    for i in range(0, len(_map)):
        print("|", end=" ")
        for j in range(0, len(_map[i])):
            if playerCoordX == i and playerCoordY == j:
                print("@", end=" ")
            elif _map[i][j]["isACase"] == True:
                if _map[i][j]["completed"] == True and _map[i][j]["symbol"] == "#":
                    _map[i][j]["symbol"] = "+"
                print(_map[i][j]["symbol"], end=" ")
            else:
                print(" ", end=" ")
        print("|")
    print("=============")



def printGameMenu():
    print("\n Où voulez-vous aller ?")
    print("   ↑ N ↑ ")
    print(" ←       →")
    print(" W       E")
    print(" ←       →")
    print("   ↓ S ↓ ")
    print("\nV.  Sauvegarder")
    print("Q.  Quitter le jeu.")
    choice = input("\n > ")
    return choice

def fight(_character, _ennemy):
    

    # Combats
    print("\033[31m\n   DEBUT DU COMBAT ! PRÉPAREZ-VOUS !\033[0m")
    initialAttack = _character['attack']
    initialDefense = _character['defense']
    """
    def PVbar (pv):
      emoredheart= "\u2764\ufe0f"
      emoblackheart="\u2764"
      if pv < 10 and pv > 0:
        pv1 = int(pv/10)
        pv = int(pv/)
        emoredheart="💔"
        a = emoredheart+emoblackheart*(10-pv)
        return a
      else:
        pv = int (pv/10)
        b = emoredheart*pv+emoblackheart*(10-pv)
        return b
    """

    while _character["health"] > 0 and _ennemy["health"] > 0:
        print()
        print(f"{_character['name']}: {_character['health']} PV (LvL {_character['level']})       Vs       {_ennemy['name']}: {_ennemy['health']} PV (LvL {_ennemy['level']})")
        print()


        # Affichage du menu du mode combat
        print("\nQue voulez vous faire ?\n1. ⚔️ Attaquer\n2.  Acceder à mon inventaire\n3.  S'échapper")
        correctChoice = False

        while correctChoice == False:
            choice = input("\n> ")

            # Test du choix de l'utilisateur
            if choice == "1":
                print(" Vous avez decidé d'attaquer")
                correctChoice = True

                # On calcule les dégats reçus par l'ennemi
                _ennemy['health'] -= attack(_character, _ennemy)

            elif choice == "2":
                if len(_character["inventory"]) == 0:
                    print(" Attention vôtre inventaire est vide!")
                    correctChoice = False

                else:
                    clear()
                    print("Vôici vôte inventaire:")
                    for i in range(0, len(_character["inventory"])):
                        print(f"{i+1}.  {_character['inventory'][i]['name']}")

                    correctChoice2 = False
                    while correctChoice2 == False:
                        choice2 = input("> ")

                        try:
                            choice2 = int(choice2)
                            if choice2 < 0 or choice2 > len(_character['inventory'])+1 :
                                raise ValueError
                            else:
                                # On applique l'effet de la potion
                                print(f" Vous utilisez l'objet suivant: {_character['inventory'][choice2-1]['name']}")

                                if _character['inventory'][choice2-1]["type"] == "potion":
                                    _character["health"] += _character['inventory'][choice2-1]["healthPointsGained"]

                                elif _character['inventory'][choice2-1]["type"] == "atkBoost":
                                    _character["attack"] += _character['inventory'][choice2-1]["boostValue"]

                                elif _character['inventory'][choice2-1]["type"] == "defBoost":
                                    _character["defense"] += _character['inventory'][choice2-1]["boostValue"]

                                # On retire l'objet de la liste
                                _character["inventory"].pop(choice2-1)
                                correctChoice2 = True

                        except ValueError:
                            print(f"Vous devez entrez un nombre entre 1 et  {len(_character['inventory'])+1} inclu.")

                    correctChoice = True

            elif choice == "3":
                print("Fuir !!")
                correctChoice = True
                return _character, "escaped"

            else:
                print("Option invalide. Choisir un nombre entre 1 et 3.")


        # C'est au tour de l'ennemi d'attaquer (il doit être en vie)
        if _ennemy['health'] > 0:
            _character["health"] -= attack(_ennemy, _character)

    # En sortant de la boucle, on vérifie qui est mort
    if _character["health"] < 0:
        print("\n\n    ","☠️","Vous êtes mort !\n\n")
        return _character, "dead"
    elif _ennemy["health"] < 0:
        print(f"\n       Félicitation {_character['name']}!! Vous avez vaincu {_ennemy['name']}")
        # + calcul de l'exp
        previousLevel = _character['level']
        _character = calculateExp(_character, _ennemy, _ennemy['level'] * 10)

        # On restaure les possibles boost du combat (dans le cas où on a pas monté de niveau)
        if previousLevel == _character["level"]:
            _character['attack'] = initialAttack
            _character['defense'] = initialDefense

    return _character, "ended"


# Fonction qui réalise une attaque par "attacker" contre "defenser"
def attack(attacker, defenser):
    clear()
    degatsTotaux = int((attacker["attack"] / 10) - (defenser["defense"] / 50))
    print(f"{attacker['name']} a infligé {degatsTotaux} points de dégâts : {defenser['name']} !")
    
    return degatsTotaux



# Fonction qui calcule l'expérience gagnée
def calculateExp(_character, _ennemy, xp):
    _character["currentExp"] += xp
    while _character["currentExp"] >= _character["nextLevelExp"] :
        _character["level"] += 1
        print(f"Vous maintenant au level {_character['level']} !")
        _character["currentExp"] = _character["currentExp"] - _character["nextLevelExp"]
        _character["nextLevelExp"] = _character["nextLevelExp"] * 2

        # + augmenter les stats
        _character["health"] = 1000 + (_character["level"] * 5)
        _character["attack"] = 100 + (_character["level"] * 5)
        _character["defense"] = 100 + (_character["level"] * 5)

    return _character


# Lancement du main
main()
