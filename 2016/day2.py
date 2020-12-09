from file_lines import get_file_lines



def bathroom_code_for_grid(lines, grid):
    row,col=len(grid)//2,len(grid[len(grid)//2])//2
    code = []
    for line in lines:
        for instr in line:
            if instr == 'U':
                row -= 1
                if row < 0 or grid[row][col] == 0:
                    row += 1
            elif instr == 'D':
                row += 1
                if row > len(grid)-1 or grid[row][col] == 0:
                    row -= 1
            elif instr == 'L':
                col -= 1
                if col < 0 or grid[row][col] == 0:
                    col += 1
            else:
                col += 1
                if col > len(grid[row])-1 or grid[row][col] == 0:
                    col -= 1
        code.append(grid[row][col])
    return ''.join(map(str, code))

def get_bathroom_code(lines):
    g = [[1,2,3],[4,5,6],[7,8,9]]
    return bathroom_code_for_grid(lines, g)

def get_new_bathroom_code(lines):
    g = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]
    return bathroom_code_for_grid(lines, g)

def main():
    lines = get_file_lines('day2.in')
    result = get_bathroom_code(lines)
    print(result)

    #part 2
    result = get_new_bathroom_code(lines)
    print(result)

if __name__ == "__main__":
    main()
