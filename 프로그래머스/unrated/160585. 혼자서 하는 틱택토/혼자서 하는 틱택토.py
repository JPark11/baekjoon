def solution(board):
    
    def find_winner(board):
        
        board = [x for b in board for x in b]
        
        o_wins = x_wins = 0
        cals = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
              [0, 3, 6], [1, 4, 7], [2, 5, 8], 
              [0, 4, 8], [2, 4, 6]]
        for cal in cals: 
            if board[cal[0]] == board[cal[1]] == board[cal[2]]: 
                if board[cal[0]] == 'O': 
                    o_wins += 1
                elif board[cal[0]] == 'X': 
                    x_wins += 1 
                
        return o_wins, x_wins
                
        
    
    o_num = x_num = 0 
    for line in board:
        for cell in line: 
            if cell == "O": 
                o_num += 1 
            elif cell == "X": 
                x_num += 1 
    
    
    if not (x_num <= o_num <= x_num + 1 ): 
        return 0 
    
    o_wins, x_wins = find_winner(board)
    
    if o_wins >=1 and x_wins >=1: 
        return 0
    
    if o_wins >= 1: 
        if not x_num == o_num - 1: 
            return 0 
    elif x_wins >= 1:
        if not x_num == o_num: 
            return 0 
    return 1
