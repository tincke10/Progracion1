# Considering an expression with parenthesis, print a message informing if the among of parenthesis is correct or incorrect, without considering the rest of the expression. Example:


# a+(b*c)-2-a        is correct
# (a+b*(2-c)-2+a)*2  is correct
# when

# (a*b-(2+c)         is incorrect
# 2*(3-a))           is incorrect
# )3+b*(2-c)(        is incorrect

# Resuming, all closing parenthesis must have an open parenthesis and it's not possible a closing parenthesis without a previous open parenthesis, and the quantity of closing and open parenthesis must be the same.

ecuacion = input("")
upper = "("
close = ")"
def parents(ecuacion):
    count = 0

    for i in ecuacion:
        if i == upper:
            count += 1
        elif i == close:
            count -= 1
            if count < 0:
                return "incorrect"
    if count == 0:
        return "correct"
    else:
        return "incorrect"

response = parents(ecuacion)
print (response)