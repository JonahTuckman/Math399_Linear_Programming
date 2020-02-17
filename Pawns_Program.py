import itertools

def queens_and_pawns(n):
    max = 0
    chess_board = []
    for i in range(0, n):
        for j in range(0, n):
            word = '(%d, %d)' % (i, j)
            chess_board.append(word)
    board = findsubsets(chess_board, n)
    num_options = len(board)
    print(num_options)
            
    for k in range(0, num_options - 1):
        unsafe_board = board[k][k]
        num_pawns = 0
        # pawn cannot be on a diagonal, or any side of it
        right_left = []
        top_bottom = []
        diagonal_right = []
        diagonal_left = []
        for l in range(0, n):
            right_left.append(unsafe_board[l, 1])
            top_bottom.append(unsafe_board[l, 2])
            diagonal_right.append((unsafe_board[l, 1] - unsafe_board[l, 2]))
            diagonal_left.append(unsafe_board[l,1] + unsafe_board[l,2])
        for i in range(0,n):
            for j in range(0,n):
                if i not in top_bottom and j not in right_left and (i-j) not in diagonal_right and (j + 1) not in diagonal_left:
                    num_pawns += 1
        if num_pawns > max:
            max = num_pawns
        
    print("For %dx%d board, the max amount of pawns safe are %d" % (n, n, max))
    
            
def empty_nested_list(n):
    matrix = []
      
    for i in range(n):
          
        # Append an empty sublist inside the list
        matrix.append([])
          
        for j in range(n):
            matrix[i].append(0)
    return matrix
    #print(matrix)
    

  
def findsubsets(s, n):
    return list(itertools.combinations(s, n))


def main():
    n = 5
    #empty_nested_list(n)
    queens_and_pawns(n)

if __name__== "__main__":
    main()
