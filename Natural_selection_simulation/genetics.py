import json
import random as rnd
import csv
import subprocess

population = []
newPopulation = []

fitness = 0

with open('population.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        population.append(row)
for row in population:
    print (row)

population = population[-6:]
for row in population:
    for i in range(len(row)):
        row[i] = float(row[i])

print('#################')
for row in population:
    print (row)

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

print('#################')
for row in newPopulation:
    print(row)

for i in range(0,6,2):
    slice = rnd.randint(0,14)
    left1 = newPopulation[i][:slice]
    right1 = newPopulation[i][slice:]
    left2 = newPopulation[i+1][:slice]
    right2 = newPopulation[i+1][slice:]
    population.append(left1+right2)
    population.append(left2+right1)

print('#################')
for row in population:
    print (row)

for row in population:
    if rnd.uniform(0,1) <=0.10:
        temp = rnd.randint(0,14)
        row[temp] += rnd.choice(-1,1)
