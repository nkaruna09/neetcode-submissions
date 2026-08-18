class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        nums = []

        for ch in tokens:
            if ch not in '+-*/':
                nums.append(int(ch))
            else:
                num1 = nums.pop()
                num2 = nums.pop()

                if ch == '+':
                    res = num2 + num1
                elif ch == '-':
                    res = num2 - num1
                elif ch == '*':
                    res = num2 * num1
                elif ch == '/':
                    res = int(num2 / num1)

                nums.append(res)

        return nums[0]
