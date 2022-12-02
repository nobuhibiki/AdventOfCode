# Nobu Hibiki's attempt at Advent of Code ^_^
# Is fun!

# Day 2

# Puzzle 1
with open('day2_input.txt') as text:
    
    # Start by seeing what you're playing, adding the score,
    # and then adding the amount of point you would get depending
    # on what the other side is playing.
    #
    # Done in this way in order to accomodate bigger games that
    # might have different scores for different pairings or for
    # rock, paper, scissors game with moves greater than N = 3 such
    # as rock-paper-scissors-lizard-Spock (atleast i think it should work)
    
    plays = [["X",1],["Y",2],["Z",3]]
    winnings = {'X' : [["A",3],["B",0],["C",6]], 
                'Y' : [["A",6],["B",3],["C",0]],
                'Z' : [["A",0],["B",6],["C",3]]}
    
    gameState = []
    allScore = []
    
    for line in text:
        score = 0
        i = 0
        while i < len(plays):
            if line[2] == plays[i][0]:
                score += plays[i][1]
                
                j = 0
                while j < len(plays):
                    if line[0] == winnings.get(plays[i][0])[j][0]:
                        score += winnings.get(plays[i][0])[j][1]
                    j += 1
            
            i += 1
        allScore.append(score)
        
    totalScore = sum(allScore)
    print(totalScore)
    
    
# Puzzle 2
with open('day2_input.txt') as text:

    # Because XYZ correlate to whether you win or not, I decided
    # that we should start from seeing what the other side is playing
    # and seeing what the additional "score" you would get from
    # what you're playing before adding the score from the game itself.
    #
    # This took way too long for me to connect in my head (pics from
    # my notes in the folder) because I tried to keep the "expandable"
    # mindset still working, and also because I want to see if I can
    # do this without having to resort to 3!*3!*3! if-else statements :)
    
    enemyPlays = ["A","B","C"]
    yourPlays = {'A' : [["X",3],["Y",1],["Z",2]], 
                 'B' : [["X",1],["Y",2],["Z",3]],
                 'C' : [["X",2],["Y",3],["Z",1]]}
    winnings = {'X' : 0, 'Y' : 3, 'Z' : 6}
    
    gameState = []
    allScore = []
    
    for line in text:
        score = 0
        i = 0
        while i < len(enemyPlays):
            if line[0] == enemyPlays[i][0]:
                j = 0
                while j < len(enemyPlays):
                    if line[2] == yourPlays.get(enemyPlays[i][0])[j][0]:
                        score += yourPlays.get(enemyPlays[i][0])[j][1]
                        score += winnings.get(line[2])
                    j += 1  
            i += 1
        allScore.append(score)
        
    totalScore = sum(allScore)
    print(totalScore)
    