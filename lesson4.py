original_text = input("Введите сообщение:")
print(original_text) 
lenght_text = len(original_text)
print(f"Кол-во символов: {lenght_text}")
print(f"Второй символ строки: {original_text[1]}")
print(f"Последний символ строки: {original_text[-1]}")
print(f"Первык 3 символа строки: {original_text[:3]}")
print(f"Последние 3 символа строки: {original_text[3:]}")
print((f"Раскраска: \u001b[47m\u001b[32;1m{original_text}\u001b[0m"))
color_start = int(input("Введите номер буквы с которой хотите раскрасить: "))
color_end = int(input("Введите номер буквы по которую хотите раскрасить: "))
color_name = int(input("Введите номер цвета в который хотите раскрасить \n1 - синий\n2 - Красный\n3 - жёлтый"))
if color_name == 1:
    color_name = "\u001b[34m"
elif color_name == 2:
    color_name = "\u001b[31m"
else:
    color_name = "\u001b[33m"
color_text = original_text[:color_start]+color_name+original_text[color_start:color_end]+"\u001b[37m"+original_text[color_end:]
print(f"Ваша расскараска: {color_text}")
old_char = input("Выберете какой символ заменить: ")
new_char = input("Выберете на какой символ заменить: ")
modifiad_text = original_text.replace(old_char, new_char)
print(modifiad_text)

even = original_text[::2]
odd = original_text[1::2]
cipher = odd + even
print(f"срез по чётным символам: {odd}")
print(f"срез по нечётным символам: {even}")
print(f"Соржение срезов: {cipher}") 
print(f"Перевёрнутое: {original_text[::-1]}")
middle_index = len(original_text)//2
swapped_text = f"{original_text[middle_index:]}{original_text[:middle_index]}"
print(f"Текст с заменой местами левой и правой части: {swapped_text}")
