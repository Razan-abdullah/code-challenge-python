# Write here the code challenge solution
def valid_paren(input_str):
  stack = []
  for paren in input_str:
  
    if paren == '(' or paren == '[' or paren == '{':
      stack.append(paren)
    else:
     
      if not stack:
        print(input_str, "contains invalid parentheses.")
        return
      else:
  
        top = stack[-1]
        if paren == ')' and top == '(' or \
        paren == ']' and top == '[' or \
        paren == '}' and top == '{':
          stack.pop()
        else:
           print(input_str, "contains invalid parentheses.")
           return

  if not stack:
    print(input_str, "contains valid parentheses.")
  else:
    print(input_str, "contains invalid parentheses.")

input1 = "{{}}()[()]"
input2 = "{][}"
input3 = "(])"
valid_paren(input1)
valid_paren(input2)
valid_paren(input3)

