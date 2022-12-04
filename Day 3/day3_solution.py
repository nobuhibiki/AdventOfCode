# Nobu Hibiki's attempt at Advent of Code ^_^
# Is fun!

# Day 3

# Puzzle 1
with open('day3_input.txt') as text:

    # Divide the rucksacks into two, put the different part in different
    # variables, and then iterate through it all. I wish there was a better
    # way for me to check if something is available that is not just doing
    # a bunch of while loops but brain cannot even start to comprehend how you
    # do this (brain moves toward matrix calculation but like before, not good
    # at matrix calculations.
    
    bothRucksack = []
    priorityValue = []
    
    for line in text:
        totalRucksack = line.strip()
        lineLength = len(totalRucksack)
        rucksackLength = int(lineLength/2)
        rucksackOne = totalRucksack[0:rucksackLength]
        rucksackTwo = totalRucksack[rucksackLength:lineLength]
        
        i = 0
        getOut = False
        while i < rucksackLength:
            j = 0
            while j < rucksackLength:
                if rucksackOne[i] == rucksackTwo[j]:
                    bothRucksack.append(rucksackOne[i])
                    if rucksackOne[i].isupper() == True:
                        priorityValue.append(int(ord(rucksackOne[i])-38))
                    if rucksackOne[i].isupper() == False:
                        priorityValue.append(int(ord(rucksackOne[i])-96))
                    getOut = True
                if getOut == True:
                    break
                j += 1
            if getOut == True:
                break
            i += 1
                
    print(sum(priorityValue))
    
# Puzzle 2
with open('day3_input.txt') as text:

    # Pretty hacky, doing something similar with the first puzzle but instead of
    # working with one line at a time we iterate through three rucksack at a time,
    # once again done by doing a bunch of while loops. To save on time I created a
    # new list that consist of the the related letters from the first two rucksack
    # and check just that to the third rucksack.
    
    priorityValue = []
    rucksack = []
    for line in text:
        rucksack.append(line.strip())
        
    groupRucksack = []
    group = 0
    while group < len(rucksack):
        tempGroupRucksack = []
        i = 0
        getOut = False
        while i < len(rucksack[group]):
            j = 0
            while j < len(rucksack[group+1]):
                if rucksack[group][i] == rucksack[group+1][j]:
                    tempGroupRucksack.append(rucksack[group][i])
                j += 1
            i += 1
        k = 0
        
        while k < len(tempGroupRucksack):
            l = 0
            while l < len(rucksack[group+2]):
                if tempGroupRucksack[k] == rucksack[group+2][l]:
                    groupRucksack.append(tempGroupRucksack[k])
                    if tempGroupRucksack[k].isupper() == True:
                        priorityValue.append(int(ord(tempGroupRucksack[k])-38))
                    if tempGroupRucksack[k].isupper() == False:
                        priorityValue.append(int(ord(tempGroupRucksack[k])-96))
                    getOut = True
                if getOut == True:
                    break
                l += 1
            if getOut == True:
                    break
            k += 1
        group += 3
        
    print(groupRucksack)
    print(sum(priorityValue))