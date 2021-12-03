# Введите предложение на русском языке, для перевода на язык символьный язык.
def alphaChange(n):
    for syb in n:
        print(alphabet[syb], end='')


russianAlphabet = [chr(j) for j in range(ord('а'), ord('я') + 1)]
vasyakinAlphabet = ['@', '6', '8', '|_', '9', '3', '#', '°3°', '1', '!',
                    '|×', '7', '|\\/|', '|-|', '0', 'π', '₽', '5', '|°', '✓',
                    '°|°', '4', '¢', '4~', '|_|_|', '|_|_|•', '¶', '∆', '¶`',
                    '€', '|-0', '&', " ", '-', ',', '.', '?']
russianAlphabet.extend([" ", '-', ',', '.', '?'])

alphabet = {russianAlphabet[i]: vasyakinAlphabet[i]
            for i in range(len(vasyakinAlphabet))}
s = input()

print(f'Версия на русском:\n{s}\nВерсия на васякинском:')
alphaChange(s.lower())
