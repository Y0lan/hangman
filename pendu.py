import random
import time
import datetime

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


def show_hangman(error):
    print("\n")
    if error == 0:
        print("")
    if error == 1:
        print(HANGMAN_1_ERR)
    if error == 2:
        print(HANGMAN_2_ERR)
    if error == 3:
        print(HANGMAN_3_ERR)
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


def main_menu_display():
    main_menu_title = "------------------\n|     PENDU      |\n------------------\n"
    main_menu_options = ["Jouer", "Afficher Aide", "Quitter"]
    return main_menu_title, main_menu_options


def play_menu_display():
    play_menu_title = ""
    play_menu_options = ["Jouer contre un ordinateur", "Jouer contre un humain", "Retourner au menu principal"]
    return play_menu_title, play_menu_options


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


def clear():
    for i in range(0, 100):
        print("\n")


def play_against_human():
    word_picked = input_word()
    play(word_picked)


def input_word():
    word_chosen = input("Entrez un mot:\n")
    while not is_word_in_list(format_word(word_chosen)):
        word_chosen = input("Mot incorrect.\nEntrez un mot:\n")
        if not is_word_in_list(format_word(word_chosen)):
            clear()
            print("Mot inconnu. Veuillez selectionner un mot de la langue française.")
    return format_word(word_chosen)


def is_word_in_list(word_to_verify):
    file = open("mots.txt", "r", encoding="ISO-8859-1")
    lines = file.readlines()
    for line in lines:
        line = format_word(line)
        if line[0:-1] == word_to_verify:
            return True
    return False


def action_menu_difficulty(action_menu_difficulty_action):
    if action_menu_difficulty_action == 1:
        return 5
    if action_menu_difficulty_action == 2:
        return 7
    if action_menu_difficulty_action == 3:
        return 10
    if action_menu_difficulty_action == 4:
        return 100


def display_menu_difficulty():
    display_menu_difficulty_title = "DIFFICULTÉ\nChoisissez un niveau de difficulté"
    display_menu_difficulty_actions = ["FACILE - 4 lettres ou moins",
                                       "INTERMEDIAIRE - 4 à 6 lettres",
                                       "DIFFICILE - 6 à 9",
                                       "EXPERT - 10+"]
    return display_menu_difficulty_title, display_menu_difficulty_actions


def play_against_machine():
    difficulty = menu(display_menu_difficulty, action_menu_difficulty)
    word = pick_word(difficulty)
    play(word)


def print_game_screen(error, word, letter_already_tried, alphabet):
    print("PENDU: \n")
    print_difficulty(word)
    show_hangman(error)
    print("\n\n")
    display_alphabet(letter_already_tried, alphabet)
    print("\n\n")
    show_box_for_letter(word, letter_already_tried)
    print("\n\n")
    print("ERREUR : {0}/10".format(error))


def print_difficulty(word):
    if len(word) <= 4:
        print("FACILE")
    if 4 < len(word) <= 6:
        print("INTERMEDIAIRE")
    if 6 < len(word) < 10:
        print("DIFFICILE")
    if 10 < len(word) < 100:
        print("EXPERT")


def play(word):
    clear()
    start = time.time()
    time_tracker = []
    total = 0
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


def correct_guess(guess, word):
    for letter in word:
        if letter == guess:
            return True
    return False


def word_is_found(letter_guessed, word_to_find):
    counter = 0
    for letter in word_to_find:
        if letter in letter_guessed:
            counter += 1
    return counter == len(word_to_find)


def get_alphabet():
    letter = 65
    alphabet = []
    while letter < 91:
        alphabet.append(chr(letter))
        letter += 1
    return alphabet


def display_alphabet(letter_guessed, alphabet):
    for letter in alphabet:
        if letter in letter_guessed:
            alphabet.remove(letter)
    print(alphabet)


def show_box_for_letter(word_to_guess, guessed_letter):
    string_to_show = ''
    for letter in word_to_guess:
        if letter in guessed_letter:
            string_to_show += letter
        else:
            string_to_show += '_'
            string_to_show += ' '
    print(string_to_show)


def get_range_for_difficulty(difficulty):
    if difficulty == 5:
        return 1, 4
    if difficulty == 7:
        return 4, 6
    if difficulty == 10:
        return 6, 9
    if difficulty == 100:
        return 9, 100


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


def main_menu_action(action_main_menu_action):
    if action_main_menu_action == 3:
        print("Fermeture du jeu en cours ...")
        exit()
    if action_main_menu_action == 2:
        display_help()
        menu(main_menu_display, main_menu_action)
    elif action_main_menu_action == 1:
        menu(play_menu_display, play_menu_action)


def display_help():
    print("Le jeu du pendu est un jeu de devinette."
          "Vous avez 10 essaies pour deviner le mot."
          "Vous pouvez soit demander à votre ami d'entrer un mot, soit demander à l'ordinateur d'en choisir un."
          "Si vous trouvez le mot en moins de 10 erreurs, vous gagnez."
          "Vous ne pouvez pas répéter les mêmes lettres.")


def menu(display, action):
    title, options = display()
    choice = menu_display_template(title, options)
    return action(choice)


if __name__ == '__main__':
    menu(main_menu_display, main_menu_action)
