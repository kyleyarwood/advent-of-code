def volume(rectangle):
    return rectangle[0]*rectangle[1]*rectangle[2]

def smallest_face_perimeter(rectangle):
    sorted_dimensions = sorted(rectangle)
    return 2*(sorted_dimensions[0] + sorted_dimensions[1])

def sum_ribbon_feet(rectangle_dimensions):
    total_ribbon_feet = 0

    for rectangle in rectangle_dimensions:
        total_ribbon_feet += smallest_face_perimeter(rectangle) + volume(rectangle)
    
    return total_ribbon_feet

def smallest_face(rectangle):
    return min([rectangle[0]*rectangle[1], rectangle[1]*rectangle[2], rectangle[0]*rectangle[2]])

def surface_area(rectangle):
    return 2*(rectangle[0]*rectangle[1] + rectangle[1]*rectangle[2] + rectangle[0]*rectangle[2])

def sum_wrapping_paper_needed(rectangle_dimensions):
    total_wrapping_paper_needed = 0
    
    for rectangle in rectangle_dimensions:
        total_wrapping_paper_needed += surface_area(rectangle) + smallest_face(rectangle)
    
    return total_wrapping_paper_needed

def get_file_lines(filename):
    with open(filename) as f:
        return f.readlines()

def main():
    file_lines = get_file_lines("day2input.txt")
    rectangle_dimensions = [list(map(int, line.split("x"))) for line in file_lines]
    
    result = sum_wrapping_paper_needed(rectangle_dimensions)
    #part 1 answer
    print(result)

    result = sum_ribbon_feet(rectangle_dimensions)
    #part 2 answer
    print(result)

if __name__ == "__main__":
    main()
