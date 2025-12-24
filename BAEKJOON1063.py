#https://www.acmicpc.net/problem/1063

#정말 무식하게 풀었다...

def chess():
    king_first, stone_first, frames = input().split()
    encoder = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
    king_location = [encoder[king_first[0]], int(king_first[1])]
    stone_location = [encoder[stone_first[0]], int(stone_first[1])]
    movements = {
        'R':[1,0],
        'L':[-1,0],
        'B':[0,-1],
        'T':[0,1],
        'RT':[1,1],
        'LT':[-1,1],
        'RB':[1,-1],
        'LB':[-1,-1]
    }
    for _ in range(int(frames)):
        next_step = movements[input()]
        if (king_location[0] + next_step[0] == stone_location[0] and
            king_location[1] + next_step[1] == stone_location[1]):
            if (stone_location[0] + next_step[0] > 8 or
                stone_location[1] + next_step[1] > 8 or
                stone_location[0] + next_step[0] < 1 or
                stone_location[1] + next_step[1] < 1):
                continue
            else:
                stone_location[0] += next_step[0]
                stone_location[1] += next_step[1]
                king_location[0] += next_step[0]
                king_location[1] += next_step[1]
        elif (king_location[0] + next_step[0] > 8 or 
              king_location[1] + next_step[1] > 8 or 
              king_location[0] + next_step[0] < 1 or 
              king_location[1] + next_step[1] < 1):
            continue
        else:
            king_location[0] += next_step[0]
            king_location[1] += next_step[1]
    
    print(list(encoder.keys())[king_location[0]-1]+str(king_location[1]))
    print(list(encoder.keys())[stone_location[0]-1]+str(stone_location[1]))

chess()
