def main():
    sum = 0
    
    with open("day1part1.txt") as file:
        for line in file:
            left = get_left_digit(line)
            right = get_right_digit(line)
            cal_value = int(left + right)

            sum += cal_value

    return sum


def get_left_digit(string):
    for i in range(len(string)):
        char = string[i]
        if char.isnumeric():
            return char
        elif char in ['o', 't', 'f', 's', 'e', 'n']:
            spelled_out = check_for_spelled_out(string, i)

            if spelled_out:
                return spelled_out

        
def get_right_digit(string):
    for i in range(len(string) - 1, -1, -1):
        char = string[i]
        if char.isnumeric():
            return char
        elif char in ['o', 't', 'f', 's', 'e', 'n']:
            spelled_out = check_for_spelled_out(string, i)
            
            if spelled_out:
                return spelled_out
        

def check_for_spelled_out(string, start_index):
    three_char = string[start_index:start_index+3]
    four_char = string[start_index:start_index+4]
    five_char = string[start_index:start_index+5]
    
    if three_char == 'one':
        return '1'
    if three_char == 'two':
        return '2'
    if five_char == 'three':
        return '3'
    if four_char == 'four':
        return '4'
    if four_char == 'five':
        return '5'
    if three_char == 'six':
        return '6'
    if five_char == 'seven':
        return '7'
    if five_char == 'eight':
        return '8'
    if four_char == 'nine':
        return '9'
    
print(main())
