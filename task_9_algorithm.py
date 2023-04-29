### Practice
'''
**You have 100 cats.**

One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. 
You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). 
Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
1. The first round, you stop at every cat, placing a hat on each one.
2. The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
3. The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
4. You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
Write a program that simply outputs which cats have hats at the end.

Optional: Make function that can calculate hat with any amount of rounds and cats.

Here you should write an algorithm, after that, try to make pseudo code. Only after that start to work. 
Code is simple here, but you might struggle with algorithm. Therefore don`t try to write a code from the first attempt. 
'''

'''
Алгоритм:

1. Створити список котів (100 елементів), у яких немає капелюхів.
2. Запустити цикл від 1 до 100 раундів.
3. У кожному раунді проходити по списку котів з кроком, який відповідає номеру раунда 
   (2-й раунд - кожен другий кіт, 3-й раунд - кожен третій кіт тощо).
4. Якщо на поточному коті є капелюх, зняти його. Якщо немає - надіти.
5. Вивести список котів, які мають капелюхи.

Складність: O(n2), цикл в циклі


Pseudo code:

Set cats as a list of 100 elements, all initialized to 0
Set rounds to 100

For each round from 0 to rounds - 1:
    For each index i in the range of round to the length of cats with step size of round + 1:
        cats[i] = 1 - cats[i]  # Toggle the value of the ith element in cats

For each index i and element cat in the list cats:
    If cat is equal to 1:
        Print "Cat №" concatenated with i+1, concatenated with "has a hat"


'''

cats = [0] * 100  # Створити список 100 котів без капелюхів
rounds = 100

for r in range(rounds):
    for i in range(r, len(cats), r+1):
        cats[i] = 1 - cats[i]  # Додати капелюх на кота без капелюха і зняти капелюх з кота з капелюхом

# Вивести список котів з капелюхами
for i, cat in enumerate(cats):
    if cat == 1:
        print("Cat №", i+1, "has a hat")



# Функція, що обраховує капелюхи для будь-якої кількості котів та раундів
def hat_game(num_cats, num_rounds):
    cats = [0] * num_cats  # Створити список котів без капелюхів

    for r in range(num_rounds):
        for i in range(r, len(cats), r+1):
            cats[i] = 1 - cats[i]  # Додати капелюх на кота без капелюха і зняти капелюх з кота з капелюхом

    # Створити список котів з капелюхами
    hatted_cats = []
    for i, cat in enumerate(cats):
        if cat == 1:
            hatted_cats.append(i+1)

    return hatted_cats
