num_dict = {
    'one': '1',
    'two': '2',
    "three": '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'    
}

# Part 1
def get_left_digit_p1(string):
    for i in range(len(string)):
        char = string[i]
        if char.isnumeric():
            return char
        
def get_right_digit_p1(string):
    for i in range(len(string) - 1, -1, -1):
        char = string[i]
        if char.isnumeric():
            return char

def get_left_digit_p2(string):
    for i in range(len(string)):
        char = string[i]
        if char.isnumeric():
            return char
        elif char in ['o', 't', 'f', 's', 'e', 'n']:
            spelled_out = check_for_spelled_out(string, i)

            if spelled_out:
                return spelled_out

        
def get_right_digit_p2(string):
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
    
    if three_char in num_dict:
        return num_dict[three_char]
    if four_char in num_dict:
        return num_dict[four_char]
    if five_char in num_dict:
        return num_dict[five_char]
    
if __name__ == '__main__':
    # Part 1
    with open("../inputs/day1.txt") as input:
        sum = 0
        for line in input:            
            left = get_left_digit_p1(line)
            right = get_right_digit_p1(line)
            cal_value = int(left + right)

            sum += cal_value

        print("Part 1: ", sum)
        
    # Part 2
    with open("../inputs/day1.txt") as input:
        sum = 0
        for line in input:            
            left = get_left_digit_p2(line)
            right = get_right_digit_p2(line)
            cal_value = int(left + right)

            sum += cal_value

        print("Part 2: ", sum)
