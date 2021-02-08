def brace(s):
    '''
    int (
    int {
    int [
    stack last <- only put opens
    if a closer pop last if like closer and it's int >= 0 cont
    if pop last is not like closer or its int < 0 false
    '''
    paren = 0
    brackets = 0
    braces = 0
    stack = []
    for i in s:
       if(i == "("):
           paren+=1
           stack.append("(")
       elif(i == "["):
           brackets+=1
           stack.append("[")
       elif(i == "{"):
           braces+=1
           stack.append("{")
       elif(i == ")"):
           paren-=1
           tmp = stack.pop()
           if((paren < 0) or (not(tmp == "("))):
               return False
       elif(i == "]"):
           brackets-=1
           tmp = stack.pop()
           if((not(tmp == "[")) or (brackets < 0)):
               return False
       elif(i == "}"):
           braces-=1
           tmp = stack.pop()
           if((not(tmp == "{")) or (braces < 0)):
               return False
       else:
           print("ERROR")
    if((paren + brackets + braces) > 0):
        return False
    else:
        return True


print(brace("()"))