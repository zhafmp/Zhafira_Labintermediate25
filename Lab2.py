secret_word = "bunny"
tries = 6

print("welcome to the game! ^____^")

while tries > 0:
    guess = input("guess the word: ")

    if guess == secret_word:
        print("you win!")
        break
    else:
        print("wrong guess! try again. ")
        tries = tries - 1
        print("try again. tries left:", tries)

if tries == 0:
    print("you lost. :P the word was:", secret_word)
