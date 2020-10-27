from name_function import get_formatted_name
'''' импортируем функцию get_formatted_name() из модуля name_function.py '''

''''
Изучаю pytest от Эльдара ч.2
Здесь я тестю функцию name_function
(дз от Эльдара)
'''
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if first == 'q':
        break

    formated_name = get_formatted_name(first,last)
    print(f"\t\t\tАккуратно оформленное имя: {formated_name}")
    '''' !!! ФИШКА \t делает отступ !!!'''
    print('Конец программы. Либо вводи q, либо опять Имена')