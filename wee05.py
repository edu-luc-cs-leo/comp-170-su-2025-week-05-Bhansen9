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

        




#MID TERM ESSAY

"""I think I have definitely learned a lot more in this course and part of this new understanding is really paying 
attention to the syntax of python. I think I have done a great job at understanding the rules and some of the tools
 needed to get around most problems we have worked on in the course. I feel very satisfied with my devotion to this class 
 and feel like I am putting full effort in learning most of the things we talk about in class. I have only missed 1 class 
 and I feel like I show up on time with my camera on. I have not missed a single assignment and have made sure to complete 
 it every time on time. I feel like I could do a little better asking more questions. I try to ask a handful at least every
   few or if not try to respond to some asked in class. Some things I need to work on is adding more comments to my code 
   which is something I tried to do more of in week 5. Other than comments I feel very good overall about the class and feel
     like I am doing very well with the material that is given in the readings and assignments each week. I fully understand
       each lecture and follow along with the code being written in class on VS Code, this way I am able to test live during
         the class and discover new ways to write the code. Overall I feel well prepared and look forward to the final creation
           of a project where I will be able to push myself and create something wonderful using all the skills I have learned 
           here and researched on my own.
"""



# reflection
"""Looking over the answers I had and the solutions posted I think this was my best week I have had on how accurate
 the answers were to the solution posted. I think my code was spot on and matched up with what was expected of my code. 
 The only thing I could have changed a little was to include more comments. I think that comments have a bigger impact for 
 people reading the code and helps them understand the thought process more on what is going on. For the future I MUST include
   more comments in order to improve my code. I think this could also help with seeing more error in the code and the baseline
     of where the code should look like at the end. Overall I thought I understood the topic pretty well and how to manipulate
       the strings contained inside the arrays. I thought the code for the first 4 were pretty much the same as the code in the 
       solutions although the only difference was number 5. I had a hard time with the intersection between 2 strings however it 
       does pass the testing provided. I do see that mine just checks over all the strings all at once and still may not be 
       entirely the right answer. The solutions code uses 2 pointers to go through the length of the lists and compares them 
       together to see if they are the same. I think in the future this is a better way to go about this problem as it scans 
       the arrays value by value through the length of the list.
"""















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
