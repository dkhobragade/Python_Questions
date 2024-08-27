# Parenthesis Checker

inp = "([]"
s = []
for i in range(len(inp)):
    if inp[i] == "{" or inp[i] == "[" or inp[i] == "(":
        s.append(inp[i])
    else:
        s.pop()
print(s)
