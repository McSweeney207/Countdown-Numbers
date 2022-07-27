import random
import time 

big = [25, 50, 75, 100]

select1 = input('Big or Small? ')

if select1 == 'Big':
  choice1 = random.choice(big)
elif select1 == 'Small':
  choice1 = random.randint(1,10) 

print(choice1)
select2 = input('Big or Small? ')

if select2 == 'Big':
  choice2 = random.choice(big)
elif select2 == 'Small':
  choice2 = random.randint(1,10) 

print(choice2)
select3 = input('Big or Small? ')

if select3 == 'Big ':
  choice3 = random.choice(big)
elif select3 == 'Small':
  choice3 = random.randint(1,10) 

print(choice3)
select4 = input('Big or Small?')

if select4 == 'Big':
  choice4 = random.choice(big)
elif select4 == 'Small':
  choice4 = random.randint(1,10) 

print(choice4)
select5 = input('Big or Small?')

if select5 == 'Big':
  choice5 = random.choice(big)
elif select5 == 'Small':
  choice5 = random.randint(1,10) 

print(choice5)
select6 = input('Big or Small?')

if select6 == 'Big':
  choice6 = random.choice(big)
elif select6 == 'Small':
  choice6 = random.randint(1,10) 

number = random.randint(101,999)
print(f'And the number to get is: {number}')
print(choice1, choice2, choice3, choice4, choice5, choice6)