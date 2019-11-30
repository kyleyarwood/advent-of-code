
def look_and_say(numbers, n):
    if (n == 0):
        return numbers
    
    curr_char = ''
    curr_len = 0
    result = ""
    
    for number in numbers:
        if number == curr_char:
            curr_len += 1
        else:
            if curr_len != 0:
                result += str(curr_len) + curr_char
            curr_len = 1
            curr_char = number
    
    if curr_len != 0:
        result += str(curr_len) + curr_char

    return look_and_say(result, n - 1)

def main():
    fourty_iterations = look_and_say("1113222113", 40)
    result = len(fourty_iterations)
    #part 1
    print(result)

    result = len(look_and_say(fourty_iterations, 10))
    #part 2
    print(result)


if __name__ == "__main__":
    main()
