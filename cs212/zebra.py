#
# Zebra Puzzle
# ------------
# 
#  1 There are five houses.
#  2 The Englishman lives in the red house.
#  3 The Spaniard owns the dog.
#  4 Coffee is drunk in the green house.
#  5 The Ukrainian drinks tea.
#  6 The green house is immediately to the right of the ivory house.
#  7 The Old Gold smoker owns snails.
#  8 Kools are smoked in the yellow house.
#  9 Milk is drunk in the middle house.
# 10 The Norwegian lives in the first house.
# 11 The man who smokes Chesterfields lives in the house next to the man with the fox.
# 12 Kools are smoked in a house next to the house where the horse is kept.
# 13 The Lucky Strike smoker drinks orange juice.
# 14 The Japanese smokes Parliaments.
# 15 The Norwegian lives next to the blue house.
#
# TODO: Who drinks water? Who owns the zebra?
#
# Each house is painted a different color, and their inhabitants are of different nationalities,
# own different pets, drink different beverages and smoke different brands of American cigarettes.

import time
import itertools


def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1

def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )


def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 

def timedcalls(n, fn, *args):
    """If n is an int, call fn(*args) n times. If it is a float,
    call it till n seconds are over. Return min, avg, max of times"""
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for i in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)

def instrument_fn(fn, *args):
    """Prints fn, result, the number of times iterators are created
    and the number of items yielded from all iterators"""
    c.starts, c.items = 0, 0
    result = fn(*args)
    print "%s got %s with %5d iters over %7d items" % (
            fn.__name__, result, c.starts, c.items)

def c(iterable):
    """A small debug helper that keeps track of number of iterators
    started and items yielded"""
    c.starts += 1
    for i in iterable:
        c.items += 1
        yield i

if __name__ == '__main__':
    print "%s drinks water and %s owns the zebra" % zebra_puzzle()
    print "zebra_puzzle took %s seconds" % timedcall(zebra_puzzle)[0]
