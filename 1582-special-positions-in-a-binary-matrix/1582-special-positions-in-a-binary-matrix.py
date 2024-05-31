class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def get_col_sum(col_idx):
            return sum(row[col_idx] for row in mat)

        count = 0
        for row in mat:
            if sum(row) == 1:
                col_idx = row.index(1)
                if get_col_sum(col_idx) == 1:
                    count += 1
        return count
                        