def intersection(foo:str, bar:str) -> str | None:
    intersection_answer = ""
    for letter in foo:
        if letter in bar and letter not in intersection_answer:
            intersection_answer += letter
    return intersection_answer if intersection_answer != "" else None

def is_alphabetical(string:str) -> bool:
    counter = 0
    all_alp = True
    while counter < len(string):
        alp_ASCII = ord(string[counter])
        if not(65 <= alp_ASCII <= 90 or 97 <= alp_ASCII <= 122):
            all_alp = False
        counter += 1
    return all_alp

def letter_only(string:str) -> str | None:
    letter_container = ""
    for char in string:
        if (65 <= ord(char) <= 90 or 97 <= ord(char) <=122):
            letter_container += char
    container = letter_container if letter_container != "" else None
    return letter_container


def generate_palindrome(string:str) -> str|None:
    letter_check = True
    rev_lettering = ""
    pos_string = len(string) - 1
    for char in string:
        if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
            letter_check = False
    if letter_check == True:
        while pos_string >= 0:
            rev_lettering += string[pos_string]
            pos_string -= 1
        string += rev_lettering
    else:
        string = None
    return string 


def is_palindrome(string:str) -> bool:
    string = string.lower()
    letter_check_IP = True
    for char in string:
        if not(65<= ord(char) <= 90 or 97 <= ord(char) <= 122):
            letter_check_IP = False

    palindrome_check = True
    if letter_check_IP == True:
        left_side = 0
        right_side = len(string) - 1
        while left_side < right_side:
            if string[left_side] != string[right_side]:
                palindrome_check = False
            left_side += 1
            right_side -= 1
    else:
        palindrome_check = False
    return palindrome_check

        







#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
