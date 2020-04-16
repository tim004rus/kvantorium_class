koloda = [6,7,2,3,4,5,8,9,10,11] * 4
import random
random.shuffle(koloda)


print('Давайте сыграем в игру "21 очко"?')
count = 0

while True:
    choice = input('Будете брать карту из колоды? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('Вам попалась карта номиналом %d' %current)
        count += current
        if count > 21:
            print('Увы, но вы проиграли')
            break
        elif count == 21:
            print('Поздравляю, вы набрали 21!')
            break
        else:
            print('У вас %d очков.' %count)
    elif choice == 'n':
        print('У вас %d очков и вы закончили игру.' %count)
        break

print('Удачи')