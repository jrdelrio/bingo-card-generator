import csv
import random

# Open the CSV file in read mode
with open('palabras.csv', 'r') as file:
    reader = csv.reader(file)
    words_list = []
    for row in reader:
        words_list.append(row[0])


for carton in range(1, 31):
    selected_words = []
    while len(selected_words) < 24:
        random_word = random.choice(words_list)
        if random_word not in selected_words:
            selected_words.append(random_word)


    with open('carton_{}.csv'.format(carton), 'w', newline='') as file:
        writer = csv.writer(file)
        for word in selected_words:
            writer.writerow([word])


