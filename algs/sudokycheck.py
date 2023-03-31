

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]



class Solution:
    def check_dublicate(self, *data: list[str]) -> bool:
        for i in data:
            if len(i) > len(set(i)):
                return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        clust1 = []
        clust2 = []
        clust3 = []
        
        index = 0

        while index < 9:

            hor = [q for q in board[index] if q.isdigit()]
            # print(hor)
            if self.check_dublicate(hor):
                return False

            pow = [d for d in [board[i][index] for i in range(9)] if d.isdigit()]
            # print(pow)
            if self.check_dublicate(pow):
                return False
            
            clust1 += [b for b in [board[index][i] for i in range(0, 3)] if b.isdigit()]
            clust2 += [b for b in [board[index][i] for i in range(3, 6)] if b.isdigit()]
            clust3 += [b for b in [board[index][i] for i in range(6, 9)] if b.isdigit()]
            
            index += 1


            if index % 3 == 0:
                if self.check_dublicate(clust1, clust2, clust3):
                    return False
                    
                
                # print(clust1, clust2, clust3)
                # print(len(set(clust1)), len(clust1))
                clust1 = []
                clust2 = []
                clust3 = []


        return True

print(Solution().isValidSudoku(board))