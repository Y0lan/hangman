import random
import time
import datetime

'''
Constante qui permettent d'afficher le pendu.
Chaque constante correspond au pendu à afficher selon le nombre d'erreur.
HANGMAN_1_ERR affiche __, le début du bas du pieds de la machine à pendre qui s'affiche lors de la 1er erreur.
ETC...
'''
HANGMAN_1_ERR = '__'
HANGMAN_2_ERR = '\n |\n |\n |\n |\n |\n_|_'
HANGMAN_3_ERR = ' ------- \n |\n |\n |\n |\n |\n_|_'
HANGMAN_4_ERR = ' ------- \n |      |\n |\n |\n |\n |\n_|_'
HANGMAN_5_ERR = ' ------- \n |      |\n |      O\n |\n |\n_|_'
HANGMAN_6_ERR = ' ------- \n |      |\n |      O\n |      |\n |\n |\n_|_'
HANGMAN_7_ERR = ' ------- \n |      |\n |      O\n |    --|\n |\n |\n_|_'
HANGMAN_8_ERR = ' ------- \n |      |\n |      O\n |    --|--\n |\n |\n_|_'
HANGMAN_9_ERR = ' ------- \n |      |\n |      O\n |    --|--\n |     /\n |\n_|_'
HANGMAN_10_ERR = ' ------- \n |      |\n |      O\n |    --|--\n |     / \\\n |\n_|_'

'''
Fonction qui permet d'afficher le bon dessin du pendu selon le nombre d'erreur.
'''


def show_hangman(error):
    print("\n")
    if error == 0:  # Si pas d'erreur, ne rien afficher
        print("")
    if error == 1:  # si 1 erreur, afficher le dessin pour une erreur...
        print(HANGMAN_1_ERR)
    if error == 2:
        print(HANGMAN_2_ERR)
    if error == 3:
        print(HANGMAN_3_ERR)  # si 3 erreur, afficher le dessin pour 3 erreurs
    if error == 4:
        print(HANGMAN_4_ERR)
    if error == 5:
        print(HANGMAN_5_ERR)
    if error == 6:
        print(HANGMAN_6_ERR)
    if error == 7:
        print(HANGMAN_7_ERR)
    if error == 8:
        print(HANGMAN_8_ERR)
    if error == 9:
        print(HANGMAN_9_ERR)
    if error == 10:
        print(HANGMAN_10_ERR)


'''
Cette fonction prend en paramètre les options du menu à afficher, et les actions correspondant à chaque options
Dans ce qui peux s'afficher il y'a:
    - Un titre (le titre PENDU pour le menu principal). C'est ce qui se trouve au dessus de la liste des actions du menu.
    Le titre ne sert que de décoration.
    
    - les options, qui sont donc la liste des options du menu :
    1. Jouer
    2. Sauvegarder
    etc.. 
    
    Ce sont les options.
    
    Et les actions sont les les fonctions à appelés selon l'action choisi.
'''


def menu(display, action):
    title, options = display()
    choice = menu_display_template(title, options)
    return action(choice)


def menu_display_template(title, options):
    keep_going = True
    last = len(options)
    while keep_going:
        print(title)
        for number, option in enumerate(options):
            print("{0} - {1}".format(number + 1, option))
        menu_template_choice = int(input("Choisissez une option:\n"))
        if 0 < menu_template_choice <= last:
            return menu_template_choice
        else:
            print("Choix invalide. Veuillez choisir une option entre {0} et {1}".format(1, last))

###############################################
# TOUS LES AFFICHAGES DES MENUS
###############################################


def main_menu_display():
    main_menu_title = "------------------\n|     PENDU      |\n------------------\n"
    main_menu_options = ["Jouer", "Afficher Aide", "Quitter"]
    return main_menu_title, main_menu_options


def play_menu_display():
    play_menu_title = ""
    play_menu_options = ["Jouer contre un ordinateur", "Jouer contre un humain", "Retourner au menu principal"]
    return play_menu_title, play_menu_options


def display_help():
    print("Le jeu du pendu est un jeu de devinette."
          "Vous avez 9 essaies pour deviner le mot."
          "Vous pouvez soit demander à votre ami d'entrer un mot, soit demander à l'ordinateur d'en choisir un."
          "Si vous trouvez le mot en moins de 9 erreurs, vous gagnez."
          "Vous ne pouvez pas répéter les mêmes lettres.")


def display_menu_difficulty():
    display_menu_difficulty_title = "DIFFICULTÉ\nChoisissez un niveau de difficulté"
    display_menu_difficulty_actions = ["FACILE - 4 lettres ou moins",
                                       "INTERMEDIAIRE - 4 à 6 lettres",
                                       "DIFFICILE - 6 à 9",
                                       "EXPERT - 10+"]
    return display_menu_difficulty_title, display_menu_difficulty_actions


############################################
# LES ACTIONS DES MENUS
############################################


def play_menu_action(action_play_menu_action):
    if action_play_menu_action == 3:
        clear()
        menu(main_menu_display, main_menu_action)
    elif action_play_menu_action == 2:
        clear()
        play_against_human()
    elif action_play_menu_action == 1:
        clear()
        play_against_machine()


def action_menu_difficulty(action_menu_difficulty_action):
    if action_menu_difficulty_action == 1:
        return 5
    if action_menu_difficulty_action == 2:
        return 7
    if action_menu_difficulty_action == 3:
        return 10
    if action_menu_difficulty_action == 4:
        return 100


def main_menu_action(action_main_menu_action):
    if action_main_menu_action == 3:
        print("Fermeture du jeu en cours ...")
        exit()
    if action_main_menu_action == 2:
        display_help()
        menu(main_menu_display, main_menu_action)
    elif action_main_menu_action == 1:
        menu(play_menu_display, play_menu_action)


'''
Cette fonction sert juste à aller 100 fois à la ligne pour "nettoyer l'écran" du texte affiché dessus.
'''


def clear():
    for i in range(0, 100):
        print("\n")


'''
Ces fonctions permettent de lancer un jeu soit contre un humain, soit contre la machine
Contre la machine, il est nécessaire de choisir le niveau de difficulté.
Contre l'humain, le niveau de difficulté est determiné par la longueur du mot entré par l'humain.
'''


def play_against_machine():
    difficulty = menu(display_menu_difficulty, action_menu_difficulty)
    word = pick_word(difficulty)
    play(word)


def play_against_human():
    word_picked = input_word()
    play(word_picked)


'''
Cette fonction sert à un humain de choisir un mot que vous devrez deviner.
En français, ligne par ligne:
Tu rentre un mot qui sera stocké dans word_chosen
tant que le mot choisi n'est pas dans la liste de tous les mots français du dictionnaire (donc tant que ce n'est pas 
un mot de la langue française), rentre un autre mot
Une fois que le mot entré est un mot de la langue française, donne le moi
'''


def input_word():
    word_chosen = input("Entrez un mot:\n")
    while not is_word_in_list(format_word(word_chosen)):
        word_chosen = input("Mot incorrect.\nEntrez un mot:\n")
        if not is_word_in_list(format_word(word_chosen)):
            clear()
            print("Mot inconnu. Veuillez selectionner un mot de la langue française.")
    return format_word(word_chosen)


'''
Cette fonction permet de savoir si le mot choisi par un humain que vous devrez deviner est dans le dictionnaire
Pour cela la fonction va parcourir la liste de mot de la langue française ligne par ligne.
Comme le jeu ne permet pas de minuscule ni d'accent, alors le mot entrer par le joueur est automatiquement converti
en majuscule et les accents sont converti dans la lettre sans accent.

Pour chaque ligne du fichier contenant tous les mots, mettre la ligne en majuscule sans accent et comparer le résultat
avec le mot entrer par l'utilisateur. Si on atteint la fin de la liste de mot sans trouver de comparaison égale, le mot
n'existe pas. Sinon, le mot existe!

'''


def is_word_in_list(word_to_verify):
    file = open("mots.txt", "r", encoding="ISO-8859-1")
    lines = file.readlines()
    for line in lines:
        line = format_word(line)
        if line[0:-1] == word_to_verify:
            return True
    return False


'''
C'est ce qui s'affiche à l'écran quand vous jouez.
En haut le mot PENDU.
En dessous la difficulté du jeu
Ensuite le pendu (si il y'a des erreurs)
ensuite l'alphabet des lettres disponible pour jouer (celle qui n'ont jamais était joué)
ensuite la liste de _ _ _ _ _ _, qui sont les cases vides correspondant au lettre inconnu du mot à deviner.
ensuite, le nombre d'erreurs faite dans la partie.
'''


def print_game_screen(error, word, letter_already_tried, alphabet):
    print("PENDU:\n")
    print_difficulty(word)
    show_hangman(error)
    print("\n\n")
    display_alphabet(letter_already_tried, alphabet)
    print("\n\n")
    show_box_for_letter(word, letter_already_tried)
    print("\n\n")
    print("ERREUR : {0}/10".format(error))


'''
Fonction qui selon la longueur du mot à deviner renvoie la difficulté du jeu à l'écran de jeu (fonction  juste au dessus).
'''


def print_difficulty(word):
    if len(word) <= 4:
        print("FACILE")
    if 4 < len(word) <= 6:
        print("INTERMEDIAIRE")
    if 6 < len(word) < 10:
        print("DIFFICILE")
    if 10 < len(word) < 100:
        print("EXPERT")



'''
Je t'ai décris toutes les fonctions sauf play().
Avec une explication que je t'ai donné de toutes les fonctions, tu devrais être capable assez vite de comprendre
comment fonctionne play().
Si t'as une question bébé écris moi sur snap, je vais dodo je suis ko
Gros bisous bon courage je crois fort en toi t'es ma numéro #1 <3
'''


def play(word):
    clear()
    start = time.time()  # temps au début du jeu
    time_tracker = []  # pour stocker le temps à chaque coup trouvé
    total = 0  # pour trouver le temps total mis pour finir le jeu
    alpha = get_alphabet()
    current_guess = ""
    letter_already_tried = []
    error = 0
    time_start_round = time.time()
    while not word_is_found(letter_already_tried, word) and error < 10:
        if correct_guess(current_guess, word):
            time_start_round = time.time()
        current_guess = ""
        print_game_screen(error, word, letter_already_tried, alpha)
        while not current_guess.isalpha():
            current_guess = input("Entrer une lettre: \n")
            current_guess = format_word(current_guess)
            if len(current_guess) > 1:
                clear()
                print("Vous ne devez rentrer qu'un seul charactère.")
                break
            elif current_guess.isalpha() and current_guess not in alpha:
                clear()
                print("\n Lettre déjà essayé.")
                break
            elif current_guess not in alpha:
                clear()
                print("Charactere invalide. Veuillez entrer une lettre alphabetique non utilisé.")
                break
            else:
                alpha.remove(current_guess)
                letter_already_tried.append(current_guess)
                if not correct_guess(current_guess, word):
                    clear()
                    print("Mauvaise lettre...réeassayez!")
                    error += 1
                if error == 10:
                    clear()
                    print("JEU PERDU")
                    print("Réponse: {0}".format(word))
                    menu(main_menu_display, main_menu_action)
                if correct_guess(current_guess, word):
                    clear()
                    print("LETTRE TROUVÉ EN: {0}\n".format(
                        str(datetime.timedelta(seconds=(time.time() - time_start_round)))))
                    print("Bien joué!")
        time_tracker.append(time.time() - time_start_round)
        total += time.time() - time_start_round

    if word_is_found(letter_already_tried, word):
        print("TEMPS TOTAL: {0} MOYENNE PAR LETTRE: {1}".format(str(datetime.timedelta(seconds=total))
                                                                , str(
                datetime.timedelta(seconds=sum(time_tracker) / len(time_tracker)))))
        print("JEU GAGNÉ!\nMot: {0}".format(word))
        menu(main_menu_display, main_menu_action)


'''
Fonction qui parcours chaque lettre du mot à deviner et qui la compare à la lettre rentrer par l'utilisateur.
Si l'une des lettres est la même, alors une lettre a été trouvé!
'''


def correct_guess(guess, word):
    for letter in word:
        if letter == guess:
            return True
    return False


'''
Calcule combien de lettre correct on été deviné.
Si il y'a autant de lettre correctement deviné que de lettre dans le mots, alors le mot entier est trouvé !
'''


def word_is_found(letter_guessed, word_to_find):
    counter = 0
    for letter in word_to_find:
        if letter in letter_guessed:
            counter += 1
    return counter == len(word_to_find)


'''
Fonction simple qui renvoie l'alphabet en majuscule de A à Z
'''


def get_alphabet():
    letter = 65
    alphabet = []
    while letter < 91:
        alphabet.append(chr(letter))
        letter += 1
    return alphabet


'''
Fonction qui affiche l'alphabet en majuscule SANS les lettres déjà devinés
Si je tape le A dans le jeu, je n'ai pas le droit de retaper le A, alors le A ne s'affiche plus dans l'alphabet des
lettres que je peux utiliser.
'''


def display_alphabet(letter_guessed, alphabet):
    for letter in alphabet:
        if letter in letter_guessed:
            alphabet.remove(letter)
    print(alphabet)


'''
Fonction simple permettant d'afficher les _ _ _ _ nécessaires pour remplacer les lettres du mots à deviner dans le jeu.
'''


def show_box_for_letter(word_to_guess, guessed_letter):
    string_to_show = ''
    for letter in word_to_guess:
        if letter in guessed_letter:
            string_to_show += letter
        else:
            string_to_show += '_'
            string_to_show += ' '
    print(string_to_show)


'''
Si le niveau est FACILE, alors le mot doit faire entre 2 et 4 caractère, soit être > 1 et <= 4
Si le niveau est INTERMEDIAIRE, alors le mot doit faire entre 5 et 6, soit être > 4 et <= 6
Si le niveau est DIFFICILE, alors le mot doit faire entre 7 et 9, soit être > 6 et <= 10 
...
5, 7, 10, 100 correspondent à la limite 'inférieur à'.
FACILE = inférieur à 5
INTERMEDIAIRE = inférieur à 7 
DIFFICILE = inférieur à 10
EXPERT = inférieur à 100

'''


def get_range_for_difficulty(difficulty):
    if difficulty == 5:
        return 1, 4
    if difficulty == 7:
        return 4, 6
    if difficulty == 10:
        return 6, 9
    if difficulty == 100:
        return 9, 100


'''
récupère un mot au hasard de la liste tant qu'il n'est pas de la longueur adéquate supérieur à x et inférieur à y caractère
selon à la difficulté choisie

'''


def pick_word(difficulty):
    line = ""
    lowest, highest = get_range_for_difficulty(difficulty)
    while not (lowest < len(line[0:-1]) <= highest):
        file = open("mots.txt", "r", encoding="ISO-8859-1")
        lines = file.readlines()
        line = lines[random.randrange(1, len(lines))]
        file.close()
        line = format_word(line)
    return line[0:-1]


'''
Enlève tous les accents et met le mot en majuscule
'''


def format_word(word):
    word = remove_accent(word)
    word = uppercase(word)
    return word


def remove_accent(remove_accent_word):
    e = ['é', 'è', 'ê', 'ë']
    o = ['ô']
    a = ['à', 'â']
    u = ['û', 'ù']
    c = ['ç']
    i = ['î', 'ï']
    for index in range(0, len(remove_accent_word)):
        current_letter = remove_accent_word[index]
        if current_letter in e:
            remove_accent_word = remove_accent_word.replace(current_letter, 'e')
        elif current_letter in o:
            remove_accent_word = remove_accent_word.replace(current_letter, 'o')
        elif current_letter in a:
            remove_accent_word = remove_accent_word.replace(current_letter, 'a')
        elif current_letter in u:
            remove_accent_word = remove_accent_word.replace(current_letter, 'u')
        elif current_letter in c:
            remove_accent_word = remove_accent_word.replace(current_letter, 'c')
        elif current_letter in i:
            remove_accent_word = remove_accent_word.replace(current_letter, 'i')
    return remove_accent_word


def uppercase(uppercase_word):
    for index in range(0, len(uppercase_word)):
        uppercase_word = uppercase_word.replace(uppercase_word[index], uppercase_word[index].capitalize())
    return uppercase_word


'''
Là ou le programme commence. Si tu veux comprendre, suis le fil... ;)
'''
if __name__ == '__main__':
    menu(main_menu_display, main_menu_action)
