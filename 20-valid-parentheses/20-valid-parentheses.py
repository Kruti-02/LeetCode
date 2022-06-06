class Solution:
    def isValid(self, s: str) -> bool:
        new_stack = []
        closetopen = {")":"(", "}" : "{", "]":"["}
        for c in s:
            if c in closetopen:
                if new_stack and new_stack[-1] == closetopen[c]:
                    new_stack.pop()
                else:
                    return False
            else:
                new_stack.append(c)
        return True if not new_stack else False
                    
        