import numpy as np

number=np.random.randint(1,101)
count=0

while True:
    count+=1
    predict_number=int(input('Guess the number from 1 to 100 '))
    if predict_number>number:
        print('Number shall be lower')
    elif predict_number<number:
        print('Number shall be higher')
    else:
        print(f'Bingo! The number = {number}, for {count} tries')
        break
    
        