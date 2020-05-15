import json
import random as rnd
import csv
import os
import subprocess

def alg():
    population = []
    newPopulation = []
    resultList = []
    fitness = 0

    with open('population.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            population.append(row)


    population = population[-6:]
    for row in population:
        for i in range(len(row)):
            row[i] = float(row[i])


    for row in population:
        fitness += row[0]

    roulette = [population[0][0]/fitness]

    for i in range(1,len(population)):
        roulette.append(roulette[i-1]+(population[i][0]/fitness))

    for gene in population:
        temp = rnd.uniform(0,1)
        for i in range(len(roulette)):
            if temp <= roulette[i]:
                newPopulation.append(population[i][1:])
                break
    population = []


    for i in range(0,6,2):
        slice = rnd.randint(0,14)
        left1 = newPopulation[i][:slice]
        right1 = newPopulation[i][slice:]
        left2 = newPopulation[i+1][:slice]
        right2 = newPopulation[i+1][slice:]
        population.append(left1+right2)
        population.append(left2+right1)


    for row in population:
        if rnd.uniform(0,1) <= 0.40:
            temp = rnd.randint(0,14)
            if temp == 7 or temp == 12 or temp == 13:
                mutationPosibilities = [-0.1,0.1]
            else:
                mutationPosibilities = [1,-1]
            row[temp] += rnd.choice(mutationPosibilities)



    for row in population:
        with open ('para.json', 'r') as f:
            config = json.load(f)

        config['RABBIT_MOVEMENT_SPEED'] = int(row[0])
        config['WOLF_MOVEMENT_SPEED'] = int(row[1])
        config['WOLF_SENSE'] = int(row[2])
        config['RABBIT_SENSE'] = int(row[3])
        config['CARROT_REP'] = int(row[4])
        config['WOLF_ENERGY'] = int(row[5])
        config['WOLF_MAX_ENERGY'] = int(row[6])
        config['WOLF_REPRODUCTION'] = row[7]
        config['WOLF_MAX_AGE'] = int(row[8])
        config['RABBIT_ENERGY'] = int(row[9])
        config['RABBIT_ENERGY_REP'] = int(row[10])
        config['RABBIT_MAX_ENERGY'] = int(row[11])
        config['RABBIT_REPRODUCTION'] = row[12]
        config['REPRODUCTION_COST'] = row[13]
        config['CARROT_ENERGY_REP'] = int(row[14])

        os.remove('para.json')
        with open('para.json', 'w') as f:
            json.dump(config, f)

        for i in range  (3):
            cmd = "C:\\Users\\1\\source\\repos\\Natural_selection_simulation\\Natural_selection_simulation\\main.exe"
            process = subprocess.Popen(cmd,creationflags=0x08000000)
            process.wait()
    
        with open('result.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            resultList = []
            for r in reader:
                resultList.append(int(r[0]))
        resultList = resultList[-3:]
        resultList.sort()
        result = [resultList[1]]

        with open('population.csv', 'a', newline='') as pop:
            row = (result+row)
            writer = csv.writer(pop)
            writer.writerow(row)
    
while True:
    alg()
    print('next gen')
