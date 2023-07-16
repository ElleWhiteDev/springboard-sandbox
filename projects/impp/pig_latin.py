"""Imported to force red text in terminal"""
import colorama
from colorama import Fore

colorama.init()


def main():
    """Translates word to pig latin"""
    print("\n\nWelcome to the pig latin translator.\n")

    while True:
        input_string = input(
            Fore.WHITE + "Enter sentance to translate, else press n to quit:\n").lower().strip()

        if input_string == "n":
            break

        trans_string = ""
        words = input_string.split()
        for word in words:
            first_char = word[0]
            rest_of_word = word[1:]

            if first_char in "aeiou":
                pig_word = (f"{word}way")
            else:
                pig_word = (f"{rest_of_word}{first_char}ay")

            trans_string += pig_word + " "

        trans_string = trans_string.strip()

        print("\n")
        print(Fore.RED + f"{input_string} = {trans_string}\n")
        print("\n")

    input(Fore.RED + "\nPress Enter to exit")


if __name__ == "__main__":
    main()
