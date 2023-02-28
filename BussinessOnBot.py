#!/usr/bin/env python
# coding: utf-8

# In[1]:


def solve_math_operation(math_expression):
    """Solves a basic math expression and returns the result."""
    if "+" in math_expression:
        operands = math_expression.split("+")
        result = int(operands[0]) + int(operands[1])
    elif "-" in math_expression:
        operands = math_expression.split("-")
        result = int(operands[0]) - int(operands[1])
    elif "*" in math_expression:
        operands = math_expression.split("*")
        result = int(operands[0]) * int(operands[1])
    elif "/" in math_expression:
        operands = math_expression.split("/")
        result = int(operands[0]) / int(operands[1])
    else:
        result = None
    return result


# In[2]:


def chatbot():
    """Main function for the chatbot."""
    print("Hello! I am a math solver chatbot.")
    while True:
        user_input = input("What math problem would you like me to solve? ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        result = solve_math_operation(user_input)
        if result is not None:
            print("The answer is:", result)
        else:
            print("I'm sorry, I can only solve basic mathematical operations.")


# In[ ]:


chatbot()


# In[ ]:




