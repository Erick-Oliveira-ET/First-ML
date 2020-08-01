import csv
import random

for i in range(1000):
    with open("Dataset/buffed_dataset.csv", 'a', newline='') as csvfile:
        print("entrou")
        fieldName = ['seal_name','RT','RI','RM','RR','RP','LP','LR','LM','LI','LT']
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames = fieldName)

        seal_list = [
            ['rooster',1,1,0,0,1,1,0,0,1,1],
            ['dog',0,0,0,0,0,1,1,1,1,1],
            ['boar',0,0,0,0,0,0,0,0,0,0],
            ['dragon',1,0,0,0,1,1,0,0,0,1],
            ['hare',0,0,0,0,1,0,0,0,1,1],
            ['horse',0,1,0,0,0,0,0,0,1,0],
            ['monkey',1,1,1,1,1,1,1,1,1,1],
            ['ox',1,1,1,1,1,1,0,0,1,0],
            ['ram',0,1,1,0,0,0,0,1,1,0],
            ['rat',0,0,0,0,0,0,0,1,1,0]
        ]

        random_seal = random.choice(seal_list) 

        writer.writerow({
            'seal_name': random_seal[0],
            'RT':random_seal[1],
            'RI':random_seal[2],
            'RM':random_seal[3],
            'RR':random_seal[4],
            'RP':random_seal[5],
            'LP':random_seal[6],
            'LR':random_seal[7],
            'LM':random_seal[8],
            'LI':random_seal[9],
            'LT':random_seal[10]
 
        })

print("Nham Nham! Delicious!!!")
