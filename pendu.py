import random

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
    main_menu_options = ["Jouer", "Quitter"]
    return main_menu_title, main_menu_options


def play_menu_display():
    play_menu_title = ""
    play_menu_options = ["Jouer contre un ordinateur", "Jouer contre un humain", "Retourner au menu principal"]
    return play_menu_title, play_menu_options


def play_menu_action(action_play_menu_action):
    if action_play_menu_action == 3:
        menu(main_menu_display, main_menu_action)
    elif action_play_menu_action == 2:
        print("playing against human")
    elif action_play_menu_action == 1:
        play_against_machine()


def play_against_machine():
    # pick a word in file
    word = ""
    while len(word) < 4:
        word = pick_word()
    # display as many _ as there is letter in the word
    print("word to guess: {0}".format(word))
    alpha = get_alphabet()
    letter_already_tried = []
    while not word_is_found(letter_already_tried, word):
        display_alphabet(letter_already_tried)
        show_box_for_letter(word, letter_already_tried)


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


def display_alphabet(letter_guessed):
    alphabet = get_alphabet()
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


def pick_word():
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
    if action_main_menu_action == 2:
        print("Fermeture du jeu en cours ...")
        exit()
    elif action_main_menu_action == 1:
        menu(play_menu_display, play_menu_action)


def menu(display, action):
    title, options = display()
    choice = menu_display_template(title, options)
    action(choice)


if __name__ == '__main__':
    menu(main_menu_display, main_menu_action)
