#!/usr/bin/python3

import random
import math
import sys

available_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.-()?! "
mutationRate = 0.01
totalPopulation = 250
multiplier = 50

target = "To be or not to be, that is the question"
population = []

def setup():
  for i in range(totalPopulation):
    population.append(Monkey(len(target)))

def newChar():
  return (random.choice(available_letters))






class Monkey:
  def __init__(self, size):
    self.genes = []
    self.fitness = 0
    for i in range(size):
      self.genes.append(newChar())
  
  def getPhrase(self):
    return "".join(self.genes)

  def calcFitness(self, target):
    score = 0
    for i in range(len(self.genes)):
      if self.genes[i] == target[i]:
        score += 1
    self.fitness = score / len(target)
  
  def crossover(self, partner):
    child = Monkey(len(self.genes))
    midpoint = math.floor(random.randrange(len(self.genes)))

    for i in range(len(self.genes)):
      if i > midpoint:
        child.genes[i] = self.genes[i]
      else:
        child.genes[i] = partner.genes[i]
    return child

  def mutate(self, mutationRate):
    for i in range(len(self.genes)):
      if random.random() < mutationRate:
        self.genes[i] = newChar()









def generation():
  found = 0
  best = 0
  worst = 0

  for i in range(len(population)):
    population[i].calcFitness(target)
    if population[i].fitness == 1:
      found = 1
    if population[i].fitness > population[best].fitness:
      best = i
    if population[i].fitness < population[worst].fitness:
      worst = i

  print(population[best].getPhrase())
  if found:
    print("Found !")
    sys.exit(0)

  matingPool = []
  for i in range(len(population)):
    fitness = population[i].fitness 
    childrenNb = math.floor(fitness * multiplier)
    for j in range(childrenNb):
      matingPool.append(population[i])
  
  for i in range(len(population)):
    a = math.floor(random.randrange(len(matingPool)))
    b = math.floor(random.randrange(len(matingPool)))
    partnerA = matingPool[a]
    partnerB = matingPool[b]
    child = partnerA.crossover(partnerB)
    child.mutate(mutationRate)
    population[i] = child

setup()
while 1:
  generation()