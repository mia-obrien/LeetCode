class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False

        mylist = []

        for char in s:
            if char == '(':
                mylist.append(')')
            elif char == '[':
                mylist.append(']')
            elif char == '{':
                mylist.append('}')
            elif char == ')' and mylist:
                if mylist.pop() !=')':
                    return False
            elif char == ']' and mylist:
                if mylist.pop() !=']':
                    return False
            elif char == '}' and mylist:
                if mylist.pop() !='}':
                    return False
            else:
                return False

        return len(mylist) == 0   