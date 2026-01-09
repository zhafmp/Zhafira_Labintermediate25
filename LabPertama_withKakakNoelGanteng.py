# the secret word
secret_word = 'catto'

# input the secret word
input_user = input("guess the letter! ")

# make sure the input is a word, not a number
if len(input_user) == 1 and input_user.isalpha():

    # ignore lower upper cases
    if input_user.lower() in secret_word.lower():
        print('yaaay! congrats. <3')
    else:
        print('nuh uh. try again. :p')

else:
    print('input is invalid. only ONE letter allowed.')
