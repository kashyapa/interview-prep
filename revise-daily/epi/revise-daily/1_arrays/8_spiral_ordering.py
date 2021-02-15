#

def spiral_arrangement(mat, offset):

    if offset == len(mat)-offset-1:
        spiral_matrix.append(mat[offset][offset])
        return
    spiral_matrix.append(mat[offset][offset:-1-offset])
    spiral_matrix.append(list(zip(*mat[-1-offset][offset: -1-offset])))
    spiral_matrix.append(mat[-1-offset][-1-offset:offset:-1])
    spiral_matrix.append(list(zip(*mat[offset][-1-offset:offset:-1])))


spiral_matrix = []
def spiral_order(mat):
    for offset in range((len(mat)+1)//2):
        spiral_arrangement(mat, offset)
    return spiral_matrix
