function solution(array, commands) {
    var answer = [];
    
    for (const command of commands) {
        const arr = array.slice(command[0] - 1,command[1])
        answer.push(arr.sort((a, b) => a - b)[command[2] - 1])
    }
    
    return answer;
}