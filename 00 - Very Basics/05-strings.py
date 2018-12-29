"""

  Strings - some tricks with strings

"""

lyrics = 'Nothing Else Matters\n\t\tBy Metallica\n\nSo close, no matter how far\nCouldn\'t be much more from the heart\nForever trusting who we are\nAnd nothing else matters';
print(lyrics)

message = r'The path is c:\program files\temp\new program'
print(message);

lyrics = '''

Nothing Else Matters
        by Metallica

    So close, no matter how far
    Couldn't be much more from the heart
    Forever trusting who we are
    And nothing else matters

    Never opened myself this way
    Life is ours, we live it our way
    All these words I don't just say
    And nothing else matters

    Trust I seek and I find in you
    Every day for us something new
    Open mind for a different view
    And nothing else matters

    Never cared for what they do
    Never cared for what they know
    But I know

    So close, no matter how far
    Couldn't be much more from the heart
    Forever trusting who we are
    And nothing else matters

    Never cared for what they do
    Never cared for what they know
    But I know

    I never opened myself this way
    Life is ours, we live it our way
    All these words I don't just say
    And nothing else matters
'''
print(lyrics)
print('-' * 25)
print(lyrics[45: 150])
print('-' * 25)
print(lyrics[286:])
print('-' * 25)
print(lyrics[::-1])
print('-' * 25)
print(lyrics[::2])
print('-' * 25)
print(lyrics[-1:-150:-1])

print(ord('a'), ord('b'), ord('A'), ord('B'))

word1 = input('Write a word ')
word2 = input('Write another word ')
# word1="looser"
# word2="you"
if word1 < word2:
  print('The bigger word is %s'%word2)
else:
  print('The bigger word is %s'%word1)