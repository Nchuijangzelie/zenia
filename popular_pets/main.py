#!/bin/python3

import pygal

piechart = pygal.Pie()
piechart.title = 'Favourite Pets'
piechart.add('Pig', 2)
piechart.add('Cow', 1)
piechart.add('Dog', 3)
piechart.add('Fowl', 8)
piechart.add('Duck', 4)
piechart.render()

barchart = pygal.Bar()
barchart.title = 'Birthday'
barchart.add('October', 8)
barchart.add('January', 5)
barchart.add('September', 4)
barchart.add('August', 7)
barchart.add('December', 2)
barchart.render()

piechart2 = pygal.Pie()
piechart2.title = 'Ugly Animals'
#The code below is reading text from pets.txt
file = open('pets.txt', 'r')

#the code below shows that the file reads from pet.txt and shows a piechart 
for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    piechart2.add(label, int(value))
  
file.close()

piechart2.render()

barchart2 = pygal.Bar()
piechart3 = pygal.Pie()
barchart2.title = 'Best Friends'
piechart3.title = 'Best Friends'

file = open('zelie.txt', 'r')

#the code below reads from zelie.txt and shows a barchart and a piechart
for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    barchart2.add(label, int(value))
    piechart3.add(label, int(value))
file.close()

barchart2.render()
piechart3.render()
