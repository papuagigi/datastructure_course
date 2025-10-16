NEED_TO_SOLVE='stack'
def NEED_TO_SOLVE():
    a = 1

class Stack:
    def __init__(self):
        self._data = []  # list로 top은 맨 끝

    def print(self):
        print(self._data)

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def top(self):
        if not self._data:
            raise IndexError("top from empty stack")
        return self._data[self.size()-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

def is_matched(expression: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    st = Stack()  # 리스트 대신 우리가 만든 스택 사용

    for ch in expression:
        
        if ch in '([{':
            st.push(ch)

        elif ch in ')]}':
            # 비었거나 top이 짝이 아니면 실패
            if st.is_empty() or st.top() != pairs[ch]:
                return False
            
            st.pop()

        else:
            # 기타 문자는 무시
            pass
    # 모두 처리 후 비어 있어야 완전 매칭
    return st.is_empty()


if __name__ == "__main__":
    stack = Stack()
    for v in [7, 3, 6]:
        stack.push(v)
        stack.print()

    print(stack.pop())  # 6
    stack.print()

    stack.push(4)
    stack.print()
    
    while not stack.is_empty():
        print(stack.pop())
        stack.print()

    tests = [
        "()[]{}", "([{}])", "([)]", "(((())))", "([)",
        "{[()]}a+b*(c-d)", ""
    ]
    for t in tests:
        print(t, "=>", "MATCH" if is_matched(t) else "UNMATCH")


