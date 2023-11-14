function solution(board) {
    const N = board.length;
    const dydx = [[1, 0], [-1, 0], [0, -1], [0, 1]];
    const dp = Array(N).fill().map(() => Array(N).fill().map(() => Array(4).fill(Infinity)));
    const isValid = (y, x) => y >= 0 && y < N && x >= 0 && x < N && board[y][x] !== 1;

    
    const Q = [[0, 0, 0, 0], [0, 0, 0, 3]];

    while(Q.length) {
        const [y, x, cost, dir] = Q.shift();
        
        for(let i = 0; i < dydx.length; i++) {
            const [my, mx] = dydx[i];
            const [ny, nx] = [y + my, x + mx];
            if(isValid(ny, nx)) {
                let newCost = cost + 100;

                if(dir !== i) newCost += 500;

                if(newCost < dp[ny][nx][i]) {
                    dp[ny][nx][i] = newCost;
                    Q.push([ny, nx, newCost, i]);
                }
            }
        }
    }
    return Math.min(...dp[N - 1][N - 1]);
}