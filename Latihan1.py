# swap or smth
a = 'hello'
b = 'hi'
a,b = b,a
print(a,b)

# lists
words = ['a','b','c','d']
input = input('Insert a word:')
if input in words:
    print('One same word')
else: 
    print('Nothing similiar')