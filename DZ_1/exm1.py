#Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

day = int(input('Введите день недели'))
if day >7 or day <1:
    print(' \n это не день недели')
elif day == 6 or day == 7:
    print(' \n это выходной день недели ')
else :
    print(' \n это не выходной день ')