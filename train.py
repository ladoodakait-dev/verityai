# train.py
# This file understands simple math words and does the math

import re
from math import sqrt, pow

def solve_math(text):
    """
    Solves basic math operations including:
    - Addition (plus, add, +)
    - Subtraction (minus, subtract, -)
    - Multiplication (times, multiply, x, *)
    - Division (divide, div, /)
    - Power/Exponents (power, ^, **)
    - Square root (sqrt, square root)
    """
    text = text.lower().strip()
    
    # Define operation keywords
    plus_words = ["plus", "add", "+"]
    minus_words = ["minus", "subtract", "-"]
    times_words = ["times", "multiply", "x", "*"]
    divide_words = ["divide", "div", "/"]
    power_words = ["power", "^", "**", "to the power"]
    sqrt_words = ["sqrt", "square root"]
    
    # Handle square root separately
    if any(word in text for word in sqrt_words):
        return handle_sqrt(text)
    
    # Try to parse as: number operator number
    # Supports formats like "2 + 3", "2+3", "multiply 5 by 3"
    
    # First try simple format: number operator number
    words = text.split()
    
    if len(words) >= 3:
        first_word = words[0]
        op_word = words[1]
        second_word = words[2]
        
        try:
            num1 = float(first_word)
            num2 = float(second_word)
            
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
            elif op_word in power_words:
                answer = pow(num1, num2)
            else:
                return f"I don't understand '{op_word}'. Try: plus, minus, times, divide, or power"
            
            # Format the answer
            return format_answer(answer)
        
        except ValueError:
            pass
    
    # If simple parsing failed, try regex parsing for more flexible input
    return parse_with_regex(text, plus_words, minus_words, times_words, divide_words, power_words)

def handle_sqrt(text):
    """Handle square root operations"""
    # Extract the number from the text
    numbers = re.findall(r'\d+\.?\d*', text)
    if not numbers:
        return "Please provide a number for square root. Example: 'sqrt 16' or 'square root of 25'"
    
    try:
        num = float(numbers[0])
        if num < 0:
            return "Cannot take square root of a negative number!"
        answer = sqrt(num)
        return format_answer(answer)
    except ValueError:
        return "Invalid number for square root"

def parse_with_regex(text, plus_words, minus_words, times_words, divide_words, power_words):
    """Try to parse math expressions using regex"""
    # Look for patterns like "5 plus 3" or "multiply 2 by 4"
    
    # Pattern: number [keyword] number
    all_keywords = plus_words + minus_words + times_words + divide_words + power_words
    
    for keyword in all_keywords:
        pattern = rf'(\d+\.?\d*)\s*{re.escape(keyword)}\s*(\d+\.?\d*)'
        match = re.search(pattern, text)
        if match:
            num1 = float(match.group(1))
            num2 = float(match.group(2))
            
            if keyword in plus_words:
                answer = num1 + num2
            elif keyword in minus_words:
                answer = num1 - num2
            elif keyword in times_words:
                answer = num1 * num2
            elif keyword in divide_words:
                if num2 == 0:
                    return "Cannot divide by zero!"
                answer = num1 / num2
            elif keyword in power_words:
                answer = pow(num1, num2)
            
            return format_answer(answer)
    
    return "I couldn't understand your math problem. Try formats like: '2 plus 3', '5 times 4', '16 divide 2', '2 power 3', or 'sqrt 16'"

def format_answer(answer):
    """Format the answer nicely"""
    # Show whole numbers without decimal point
    if isinstance(answer, float) and answer == int(answer):
        return int(answer)
    # Round to 2 decimal places for floats
    elif isinstance(answer, float):
        return round(answer, 2)
    return answer
