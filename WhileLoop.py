i=1
while i<=10:
    print(i)
    i+=1
print('Done')

answer=9
guessCount=0
guessLimit=3
while guessCount<guessLimit:
    guess=int(input('Guess: '))
    guessCount+=1
    if guess==answer:
        print('Correct!')
        break
    print('Guess again^^')
else:
    print('Sorry you dont have chance')