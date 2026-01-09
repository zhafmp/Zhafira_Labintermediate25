# the secret word
secret_word = 'catto'

# input the secret word
input_user = input("guess the secret word! ")

# make sure the input is a word, not a number
if input_user.isalpha():

    # lower upper cases
    if input_user.lower() == secret_word.lower():
        print('yaaay! congrats. <3')
    else:
        print('nuh uh. try again. :p')

else:
    print('input is invalid. only words allowed.')