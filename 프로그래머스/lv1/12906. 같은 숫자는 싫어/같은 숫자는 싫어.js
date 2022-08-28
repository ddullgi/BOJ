function solution(arr)
{
    let number = -1
    var answer = [];
    for (const i of arr) {
        if (i === number) {
            continue
        } else {
            number = i
            answer.push(i)
        }
    }
    return answer;
}