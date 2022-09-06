function solution(board, moves) {
    const stack = []
    let count = 0
    for (const i of moves) {
        for (let j = 0; j < board.length; j++) {
            if (board[j][i - 1] != 0){
                stack.push(board[j][i - 1])
                if (stack[stack.length - 1] === stack[stack.length - 2]) {
                    stack.pop()
                    stack.pop()
                    count += 2
                }
                board[j][i - 1] = 0
                break
            }
        }
    }

    
    return count;
}