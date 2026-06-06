class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

       d = {i: [] for i in range(9)}
       d3 = {i: [] for i in range(9)}
       row = 0
       for array in board:
            s = []
            for i in range (len(array)):
                region = (row // 3) * 3 + i // 3

                if array[i] == ".":
                    continue
                
                # Checks each row of the board
                if array[i] not in s:
                    s.append(array[i])
                else:
                    return False 
                
                # Checks each column of the board
                if array[i] not in d[i]:
                    d[i].append(array[i])
                else:
                    return False
                
                # Checks each 3x3 grid
                if array[i] not in d3[region]:
                    d3[region].append(array[i])
                else:
                    return False
            
            row += 1
                
        
       return True
                
        

            

        