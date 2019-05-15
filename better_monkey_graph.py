#!/usr/bin/python3

import random
import math
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

available_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.-()?! "
mutationRate = 0.01
totalPopulation = 250
multiplier = 50

target = "To be or not to be, that is the question"
population = []

fig = plt.figure()
bestplot = fig.add_subplot(1, 1, 1)
medianplot = fig.add_subplot(1, 1, 1)
worstplot = fig.add_subplot(1, 1, 1)

cur_generation = 0
generation_list = []
best_pop = []
median_pop = []
worst_pop = []

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

def draw(n):
  global cur_generation
  cur_generation += 1
  found = 0
  best = 0
  worst = 0
  median = 0

  for i in range(len(population)):
    population[i].calcFitness(target)
    median += population[i].fitness
    if population[i].fitness == 1:
      found = 1
    if population[i].fitness > population[best].fitness:
      best = i
    if population[i].fitness < population[worst].fitness:
      worst = i

  median = median / len(population)
  generation_list.append(cur_generation - 1)
  worst_pop.append(population[worst].fitness)
  median_pop.append(median)
  best_pop.append(population[best].fitness)
  worstplot.clear()
  medianplot.clear()
  bestplot.clear()
  bestplot.plot(generation_list, best_pop)
  medianplot.plot(generation_list, median_pop)
  worstplot.plot(generation_list, worst_pop)

  print(population[best].getPhrase())
  if found:
    print("Found !")
    plt.show()
    sys.exit(0)

  matingPool = []
  for i in range(len(population)):
    fitness = population[i].fitness - population[worst].fitness
    childrenNb = math.floor(math.exp(fitness * multiplier))
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
ani = animation.FuncAnimation(fig, draw, interval=1)
plt.show()