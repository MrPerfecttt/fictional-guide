text = input("Введите текст: ")

with open("user_input.txt", "a") as file:
    file.write(text)



text = input("Введите текст: ")
try:
    fil1 = open("user_input.txt")
    with open("user_input.txt", "a") as file:
        file.write(text)
    print("Текст успешно записан в файл user_input.txt")
except:
    print("Файл user_input.txt не найден")

