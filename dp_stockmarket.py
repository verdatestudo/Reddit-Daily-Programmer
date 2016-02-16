
'''
Play the Stock Market - Daily Programmer
https://www.reddit.com/r/dailyprogrammer/comments/40h9pd/20160111_challenge_249_easy_playing_the_stock/
2016-Jan-12
Python 2.7
Chris
'''

'''
Find the biggest profit. Notes:
- You must buy before sell
- You must wait one tick between buy and sell. E.g [2, 1, 8] ans = 2 and 8.
'''

import itertools

orgData = '19.35 19.30 18.88 18.93 18.95 19.03 19.00 18.97 18.97 18.98'
chalData = '''
            9.20 8.03 10.02 8.08 8.14 8.10 8.31 8.28 8.35 8.34 8.39 8.45 8.38
            8.38 8.32 8.36 8.28 8.28 8.38 8.48 8.49 8.54 8.73 8.72 8.76 8.74 8.87
            8.82 8.81 8.82 8.85 8.85 8.86 8.63 8.70 8.68 8.72 8.77 8.69 8.65 8.70
            8.98 8.98 8.87 8.71 9.17 9.34 9.28 8.98 9.02 9.16 9.15 9.07 9.14 9.13
            9.10 9.16 9.06 9.10 9.15 9.11 8.72 8.86 8.83 8.70 8.69 8.73 8.73 8.67
            8.70 8.69 8.81 8.82 8.83 8.91 8.80 8.97 8.86 8.81 8.87 8.82 8.78 8.82
            8.77 8.54 8.32 8.33 8.32 8.51 8.53 8.52 8.41 8.55 8.31 8.38 8.34 8.34 8.19 8.17 8.16
            '''

sMarket = [float(i) for i in chalData.split()]  # choose data source here


# one line wonder
print max((y-x, x, y) for (i, x), (j, y) in itertools.combinations(enumerate(sMarket), 2) if j-i > 1)[1:]

#my original solution
profitMinMax = 0
minVal = 0
maxVal = 0

for idx, val in enumerate(sMarket):
    for val2 in sMarket[idx+2:]:
        if val2 - val > profitMinMax:
            profitMinMax = val2 - val
            minVal = val
            maxVal = val2

print profitMinMax, minVal, maxVal
