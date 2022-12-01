# Nobu Hibiki's attempt at Advent of Code ^_^
# Is fun!

# Day 1 - Puzzle 1

# Open the input text (I should try to set up a user input next time)
with open('day1_input.txt') as text:

    # Create a list that will be filled with the total calories a
    # certain elf will hold.
    elf = []
    calories = 0
    
    # Get one line from the text file and if there is a number in the 
    # line, add them to the calories. Once there is an extra space,
    # append that to the elf list and empty out the calories variable.
    for line in text:
        if line != "\n":
            calories += int(line.strip())
        else:
            elf.append(calories)
            calories = 0
    
    # Because the last line of the input is a number and not an extra space
    # I need to add a special append for the last elf. There is probably a
    # much more elegant solution to this but my brain is not beeg enough.
    elf.append(calories)
    
    # Print the total calories of all elves.
    # print("Total Calories per Elf:")
    # print(elf)
    
    # Create a new list where all the elves are sorted from highest to lowest
    # and create a new list with the relevant list. Done this way in order to
    # allow for multiple elves with the same amount of calories to have the same
    # ranking (doens't matter in this specific case but it seemed fun to implement).
    sortedElf = sorted(elf, reverse = True)
    rank = 1
    sortedRankList = [1]
    
    for i in range(1, len(sortedElf)):
        if sortedElf[i] !=  sortedElf[i-1]:
            rank += 1
        sortedRankList.append(rank)
    
    # Match the ranking with which elves have the ranking.
    rankList = []
    for item in elf:
        for x, y in enumerate(sortedElf):
            if y == item:
                rankList.append(sortedRankList[x])
                break                
    
    # Print rank of all the elves.
    # print("\nRank of all the Elves")
    # print(rankList)
    
    # Find from the rank available which elves is the number one and how many
    # calories does it have.
    for i in range(1, len(rankList)):
        if rankList[i] == 1:
            print("\nElf number " + str(i+1) + " has the most calories with " + str(elf[i]) + " calories\n")
    
    
    topThreeElves = 0
    for i in range(1, len(rankList)):
        if rankList[i] == 1:
            print("Elf number " + str(i+1) + " has the most calories with " + str(elf[i]) + " calories")
            topThreeElves += elf[i]
        if rankList[i] == 2:
            print("Elf number " + str(i+1) + " has the second most calories with " + str(elf[i]) + " calories")
            topThreeElves += elf[i]
        if rankList[i] == 3:
            print("Elf number " + str(i+1) + " has the third most calories with " + str(elf[i]) + " calories")
            topThreeElves += elf[i]
            
    print("\nThe total calories of the top three elves is " + str(topThreeElves) + "!")