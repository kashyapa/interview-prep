def non_attacking_n_queens(n):
    
    def is_valid(col_placements, row_id):
        col_val = col_placements[row_id]
        
        for i, col in enumerate(col_placements[:row_id]):
            if abs(col-col_val) in (0, abs(row_id-i)):
                return False
        return True
    
    
    def solve(row_index, col_placements):

        if row_index == n:
            res.append(col_placements.copy())
        else:
            for col in range(n):
                col_placements[row_index] = col
                if is_valid(col_placements):
                    solve(row_index+1, col_placements)     
            
    col_placements = [0] * n
    res = []
    
    