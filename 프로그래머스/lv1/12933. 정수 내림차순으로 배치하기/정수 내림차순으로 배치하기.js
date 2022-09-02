function solution(n) {
    const b = String(n).split("")
    var answer = Number(b.sort((a, b) => b - a).join(""));
    return answer;
}