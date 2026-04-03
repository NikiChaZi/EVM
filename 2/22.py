class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [("", 0, 0)] 

        while stack:
            cur, open_cnt, close_cnt = stack.pop()

            if len(cur) == 2 * n:
                res.append(cur)
                continue

            if open_cnt < n:
                stack.append((cur + "(", open_cnt + 1, close_cnt))

            if close_cnt < open_cnt:
                stack.append((cur + ")", open_cnt, close_cnt + 1))

        return res