class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    if self.rec(board, [i, j], word[1:], visited):
                        return True
        return False
    
    def rec(self, board, current, remain, visited):
        if not remain:
            #print current, visited
            return True
        i, j = current
        #print current, visited
        if i - 1 >= 0 and (i - 1, j) not in visited and board[i - 1][j] == remain[0]:
            t_visited = set(visited)
            t_visited.add((i - 1, j))
            if self.rec(board, [i - 1, j], remain[1:], t_visited):
                return True
        
        if j - 1 >= 0 and (i, j - 1) not in visited and board[i][j - 1] == remain[0]:
            t_visited = set(visited)
            t_visited.add((i, j - 1))
            if self.rec(board, [i, j - 1], remain[1:], t_visited):
                return True
        
        if i + 1 < len(board) and (i + 1, j) not in visited and board[i + 1][j] == remain[0]:
            t_visited = set(visited)
            t_visited.add((i + 1, j))
            if self.rec(board, [i + 1, j], remain[1:], t_visited):
                return True
        
        if j + 1 < len(board[0]) and (i, j + 1) not in visited and board[i][j + 1] == remain[0]:
            t_visited = set(visited)
            t_visited.add((i, j + 1))
            if self.rec(board, [i, j + 1], remain[1:], t_visited):
                return True
        
        return False
            
                
            