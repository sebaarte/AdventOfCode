

from itertools import product

def in_content(content,x,y,x_prime,y_prime,factor):
    try:
        new_y = y+(y_prime*factor)
        new_x = x+(x_prime*factor)
        if new_x < 0 or new_y < 0:
            return 'B'
        return content[new_y][new_x]
    except IndexError:
        return 'B'


def search_in_direction(content,x,y,direction):
    x_prime = direction[0]
    y_prime = direction[1]

    xmas = "XMAS"
    found_word = content[y][x]

    for factor in range(1,4,1):
        found_word += in_content(content,x,y,x_prime,y_prime,factor)
    
    if found_word == xmas:
        return 1
    else:
        return 0

def search_around(content,x,y):
    summ = 0
    directions = list(product([-1,0,1],[-1,0,1]))
    directions.remove((0,0))


    for direction in directions:
        summ += search_in_direction(content,x,y,direction)
    
    return summ
            



def search_santa():
    summ = 0
    file = open("day4/data.txt")
    content = file.readlines()
    file.close()
    for y in range(len(content)):
        for x in range(len(content)):
            if content[y][x] == 'X':
                summ += search_around(content,x,y)

    print(summ)

def is_x_mas(content,x,y):
    check1 = [(x+1,y+1),(x-1,y-1)]
    check2 = [(x-1,y+1),(x+1,y-1)]
    
    word1 = ''.join(sorted( content[y+1][x+1] + content[y-1][x-1]))
    word2 = ''.join(sorted( content[y+1][x-1] + content[y-1][x+1]))

    if word1 == "MS" and word2 == "MS":
        return True
    return False


def search_x_mas():
    summ = 0
    file = open("day4/data.txt")
    content = file.readlines()
    file.close()

    for y in range(1,len(content)-1,1):
        for x in range(1,len(content)-1,1):
            if content[y][x] == 'A':
                if is_x_mas(content,x,y):
                    summ+=1

    print(summ)

if __name__ == "__main__":
    search_x_mas()