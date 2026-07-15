# Variable Decelartion
secret_number = 3
guess = 0

while guess!= secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! try again.')

print('You got it!')

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names :
    if developer == 'Naomi':
        break
    print(developer)

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")

# one way to add even numbers
# even_numbers =[]

# for i in range(21):
#     if i%2==0:
#         even_numbers.append(i)

# Refractored version of doing this
even_numbers = [num for num in range(21) if num%2==0]
odd_numbers = [num for num in range(21) if num%2!=0]
print(even_numbers)
print(odd_numbers)


# Trying the more refractored list
numbers = [1,2,3,4,5]
result = [(num, 'Even') if num%2==0 else (num,'Odd') for num in numbers]
print(result)

# now trying the filter function
#filter() : Takes two arguments one is funtion and other is iterable.
# Now filter funtion will make create a list with all who satisfy the condtition

words = [ 'tree', 'sky', 'mountain', 'river', 'cloud','sun']

def is_long_word(word):
    return len(word)>4

long_words = filter(is_long_word,words)
print(long_words)

for i in long_words:
    print(i)

# Now learn abou the mapp function
# map() takes an iterable and applies a function to each of its elements.
# take an example for the mapp function

celsius = [0,10,20,30,40]

def to_fahrenheit(temp):
    return (temp* 9/5) +32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)

# refactored function
# lambda function()
x = list(map(lambda num: num**2, [2,3,4,5]))
print(x)
