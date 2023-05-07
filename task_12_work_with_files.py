## Practice

# 1.

import random
import csv

# 1. Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

file_names = [chr(i) + '.txt' for i in range (65, 91)]  # Створюємо список file_names з використанням генератора списку. 
                                                        # Він починається з ASCII-коду символу "A" (65) і закінчується на ASCII-коді символу "Z" (90), 
                                                        # які перетворюються у символи за допомогою функції chr(). 
                                                        # До кожного символу додається розширення .txt, щоб створити ім'я файлу.

# 2. To each file append a random number between 1 and 100.

for file_name in file_names:                            # Запускаємо цикл, в якому функція random.randint(1, 100) 
    with open(file_name, 'a') as f:                     # генерує випадкове ціле число в діапазоні від 1 до 100, 
        f.write(str(random.randint(1, 100)) + '\n')     # яке потім перетворюється на рядок і записується до файлу за допомогою 
                                                        # методу write().

# 3. Create a summary file (summary.txt) that contains name of the file and number in that file:

with open('summary.txt', 'w') as summary_file:                  # Файл summary.txt створюється за допомогою режиму 'w' (запис).
    for file_name in file_names:                                # Для кожного файлу у списку file_names зчитуються дані файлу за допомогою 
        with open(file_name, 'r') as f:                         # методу read(), обрізаються зайві пропуски з використанням методу strip(),  
            contents = f.read().strip()                         # а потім об'єднуються з ім'ям файлу і двокрапкою. 
            summary_file.write(f'{file_name}: {contents}\n')    # Отриманий рядок записується до файлу summary.txt за допомогою методу write().


# 2. 
# 1. Create file with some content. As example you can take this one.

with open('content_file.txt', 'w') as file:             # Створюємо файл content_file.txt та методом write() записуємо в нього текст.
    file.write('''
    Тому що ніколи тебе не вирвеш,
    ніколи не забереш,
    тому що вся твоя свобода
    складається з меж,
    тому що в тебе немає
    одного вантажу,
    тому що ти ніколи не слухаєш,
    оскільки знаєш і так,
    що я скажу,''')
     
# 2. Create second file and copy content of the first file to the second file in upper case.

with open('content_file.txt', 'r') as file:             # Відкриваємо content_file.txt для читання та зчитуємо його вміст
    content = file.read()
                                                 
content_upper = content.upper()                         # Переводимо вміст у верхній регістр методом upper()

with open('copy_content_file.txt', 'w') as file:        # Відкриваємо файл-копію для запису та записуємо вміст 
    file.write(content_upper)


## Practice

# 3. Write a program that will simulate user score in a game. Create a list with 5 player's names. 
#    After that simulate 100 games for each player. As a result of the game create a list with player's name and his score (0-1000 range). 
#    And save it to a CSV file. File should looks like this:
'''
    Player name, Score
    Josh, 56
    Luke, 784
    Kate, 90
    Mark, 125
    Mary, 877
    Josh, 345
    ...
'''

# Список імен гравців
players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

# Створюємо список для зберігання результатів кожного гравця
player_scores = []

# Симулюємо 100 ігор для кожного гравця
for player in players:
    for game in range(100):
        # Генеруємо випадковий результат від 0 до 1000
        score = random.randint(0, 1000)
        # Додаємо ім'я гравця та його результат до списку
        player_scores.append([player, score])
        
# Зберігаємо дані у CSV файл
with open('player_scores.csv', 'w', newline='') as csvfile:       # Відкриваємо новий файл player_scores.csv у режимі запису 
    writer = csv.writer(csvfile)                                  # та створюємо об'єкт csv.writer для запису даних у файл. 
    writer.writerow(["Player's name", "Scores"])                  # Спочатку записуємо рядок заголовка з назвами стовпців "Player's name" 
    for player, score in player_scores:                           # та "Scores", а потім записуємо кожний рядок результатів гравців у файл. 
        writer.writerow([player, score])                          # Кожен рядок містить ім'я гравця та його результат для однієї гри.


# 4. Write a script that reads the data from previous CSV file and creates a new file called high_scores.csv 
#    where each row contains the player name and their highest score. Final score should sorted by descending of highest score
'''
The output CSV file should look like this:

    
    Player name, Highest score
    Kate, 907
    Mary, 897
    Luke, 784
    Mark, 725
    Josh, 345
'''
# Set для зберігання найкращих результатів кожного гравця
best_scores = {}
# Зчитуємо дані з CSV файлу
with open('player_scores.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Пропускаємо перший рядок зі заголовками стовпців
    next(reader)
    # Проходимося по кожному рядку і додаємо найкращий результат кожного гравця до словника
    for row in reader:
        player_name = row[0]
        score = int(row[1])
        if player_name in best_scores:
            best_scores[player_name] = max(best_scores[player_name], score)
        else:
            best_scores[player_name] = score 

# Сортуємо результати за спаданням найкращого результату
sorted_scores = sorted(best_scores.items(), key=lambda x: x[1], reverse=True)

# Зберігаємо дані у CSV файл
with open('high_scores.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    writer.writerow(['Player name', 'Highest score'])
    for player, score in sorted_scores:
        writer.writerow([player, score])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    