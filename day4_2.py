
if __name__ == '__main__':
    with open("./input/day4.txt", "r") as f:
        lines = f.readlines()

    result = 0
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[0])-1):
            if lines[i][j] == 'A':
                if {lines[i-1][j-1], lines[i+1][j+1]} == {'M', 'S'} and {lines[i-1][j+1], lines[i+1][j-1]} == {'M', 'S'}:
                    result += 1
    print(result)