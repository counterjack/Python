
"""
input = "{[()]}"
output: Boolean (Yes/NO)
"""

from typing import List

opening_paranthesis: List = ["{", "[", "("]
closing_paranthesis: List = ["}", "]", ")"]

opening_xmap_closing_paranthesis = {
        "}": "{",
        "]": "[",
        ")": "("
    }



def get_corresponding_opening_braces(paranthesis: str) -> str:
    if paranthesis not in closing_paranthesis:
        raise "Invalid closing paranthesis"

    return opening_xmap_closing_paranthesis[paranthesis]

def is_balanced(input_string: str) -> bool:
    """
    """
    stack = []

    for item in input_string:
        # Push if the current item is in opening_paranthesis
        if item in opening_paranthesis:
            stack.append(item)
        else:
            # Get the corresponding opening braces for current item
            opening_paran = get_corresponding_opening_braces(item)

            if len(stack) == 0 or opening_paran != stack[-1]:
                return False
            # else pop the last element from the stack
            else:
                stack.pop()

    if len(stack) != 0:
        return False        
    return True


user_input = input("Give a string with paranthesis ");
print (is_balanced(user_input))