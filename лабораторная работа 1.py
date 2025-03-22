digit_to_word = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять',
    'A': 'десять',
    'B': 'одиннадцать',
    'C': 'двенадцать',
    'D': 'тринадцать',
    'E': 'четырнадцать',
    'F': 'пятнадцать'
}
str = ''
with open('input.txt', 'r') as f:
    block = f.read()
    if not block:
        print("\nФайл input.txt пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл")
    while block:
        lexemes = block.split()
        for lexeme in lexemes:
            try:
                num = int(lexeme, 16)
            except ValueError:
                print("не является шестнадцатеричным числом")
                continue
            if (len(lexeme) > 2) and (lexeme[-3]=='A'):
                str = ''
                for digit in lexeme:
                    str += digit_to_word[digit] + ' '
                print(lexeme + ':' + str)
                break
        if str == '':
            print("не удовлетворяет условию задачи")
        block = f.read()
