
'''
Daily Programmer
https://www.reddit.com/r/dailyprogrammer/comments/3twuwf/20151123_challenge_242_easy_funny_plant/

2015-Nov-24
Python 2.7
Chris

Description

Scientist have discovered a new plant.
The fruit of the plant can feed 1 person for a whole week
 and best of all, the plant never dies.
Fruits needs 1 week to grow, so each weak you can harvest it fruits.
Also the plant gives 1 fruit more than the week before
 and to get more plants you need to plant a fruit.

Now you need to calculate after how many weeks,
you can support a group of x people, given y fruits to start with.
'''
# x = people, y = plants, z = fruits
x = 15
y = 1
z = y-1
fruits = []
fruits.append(z)
week = 1

def weekAct():
    global y, z, week, fruits
    z = 0
    week += 1
    fruits = [x+1 for x in fruits]
    for fruit in fruits:
        if fruit > 0:
            for i in range(fruit):
                fruits.append(0)
        z += fruit

while z < x:
    print "Week %s , Plants %s, No. of fruits %s" % (week, len(fruits), z)
    weekAct()

print "Week %s , Plants %s, No. of fruits %s" % (week, len(fruits), z)
