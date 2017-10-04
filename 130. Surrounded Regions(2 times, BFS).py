class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        surr = set()
        not_surr = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) in surr or (i ,j) in not_surr or board[i][j] != 'O':
                    continue
                self.BFS(board, i, j, set(), surr, not_surr)
        for i in surr:
            board[i[0]][i[1]] = 'X'
        #print surr, not_surr 
                           
    def BFS(self, board, i, j, group, surr, not_surr):
        stack = [(i, j)]
        surr_flag = True
        while stack:
            i ,j = curr = stack[0]
            #print curr, stack
            group.add(curr)
            del stack[0]
            if self.isEdge(curr, len(board), len(board[0])):
                surr_flag = False
            if i - 1 >= 0 and (i - 1, j) not in group and board[i - 1][j] == 'O':
                stack.append((i - 1, j))
                group.add((i - 1, j))
            if i + 1 < len(board) and (i + 1, j) not in group and board[i + 1][j] == 'O':
                stack.append((i + 1, j))
                group.add((i + 1, j))
            if j - 1 >= 0 and (i, j - 1) not in group and board[i][j - 1] == 'O':
                stack.append((i, j - 1))
                group.add((i, j - 1))
            if j + 1 < len(board[0]) and (i, j + 1) not in group and board[i][j + 1] == 'O':
                stack.append((i, j + 1))
                group.add((i, j + 1))
        #print group
        if surr_flag:
            for i in group:
                surr.add(i)
        else:
            for i in group:
                not_surr.add(i)

    def isEdge(self, location, row, column):
        i, j = location
        if i == 0 or i == row - 1 or j == 0 or j == column - 1:
            return True
        return False