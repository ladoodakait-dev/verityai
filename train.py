# train.py
# This file understands simple math words and does the math

def solve_math(text):
    text = text.lower().strip()
    words = text.split()

    # Words that mean each operation
    plus_words = ["plus", "add"]
    minus_words = ["minus", "sub"]
    times_words = ["times", "x", "multiply"]
    divide_words = ["div", "divide"]

    # We expect: number word number  (like: 2 x 3)
    if len(words) != 3:
        return "Please write it like: 2 x 3"

    first_word, op_word, second_word = words

    try:
        num1 = float(first_word)
        num2 = float(second_word)
    except ValueError:
        return "Please use numbers, like: 2 x 3"

    if op_word in plus_words:
        answer = num1 + num2
    elif op_word in minus_words:
        answer = num1 - num2
    elif op_word in times_words:
        answer = num1 * num2
    elif op_word in divide_words:
        if num2 == 0:
            return "Cannot divide by zero!"
        answer = num1 / num2
    else:
        return "I don't understand that word. Try: plus, minus, times, divide"

    # Show whole numbers without .0 at the end
    if answer == int(answer):
        answer = int(answer)

    return answer
