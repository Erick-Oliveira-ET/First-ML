import csv
import random

for i in range(1000):
    with open("Dataset/buffed_dataset.csv", 'a', newline='') as csvfile:
        print("entrou")
        fieldName = ['seal_name','bucket_list','number']
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames = fieldName)

        seal_list = [
            ['rooster',[1,1,0,0,1,1,0,0,1,1],[1,0,0,0,0,0,0,0,0,0]],
            ['dog',[0,0,0,0,0,1,1,1,1,1],[0,0,1,0,0,0,0,0,0,0]],
            ['boar',[0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0]],
            ['dragon',[1,0,0,0,1,1,0,0,0,1],[0,0,0,1,0,0,0,0,0,0]],
            ['hare',[0,0,0,0,1,0,0,0,1,1],[0,0,0,0,1,0,0,0,0,0]],
            ['horse',[0,1,0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0]],
            ['monkey',[1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,1,0,0,0]],
            ['ox',[1,1,1,1,1,1,0,0,1,0],[0,0,0,0,0,0,0,1,0,0]],
            ['ram',[0,1,1,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,1,0]],
            ['rat',[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,1]]
        ]

        random_seal = random.choice(seal_list) 

        writer.writerow({
            'seal_name': random_seal[0],
            'bucket_list': list(random_seal[1]),
            'number': random_seal[2]
        })

print("Nham Nham! Delicious!!!")