function solution(n) {
    var answer = '';
    let i = 0
    while (i < n) {
        i ++
        if (i % 2) {
            answer += "수"
        } else {
            answer += "박"
        }
    }
    return answer;
}