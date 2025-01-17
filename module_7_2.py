def custom_write(file_name, strings):
    file = open(file_name, 'w')
    file.close()
    counter = 0
    for string in strings:
        file = open(file_name, 'a', encoding= 'utf-8')
        counter += 1
        string_positions[counter, file.tell()] = string
        file.write(f'{string}\n')
        file.close()
    return string_positions

text = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

string_positions = {}
result = custom_write('text.txt', text)
for string in result.items():
    print(string)