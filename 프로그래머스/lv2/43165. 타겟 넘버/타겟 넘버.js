
function solution(numbers, target) {
    let cnt = 0
    const maxI = numbers.length
    function tree(index, result) {
        if (index === maxI) {
            if (result === target) {
                cnt += 1
                }
            return
        }
        
        tree(index + 1, result + numbers[index])
        tree(index + 1, result - numbers[index])
    }
    tree(0, 0)
    var answer = cnt;
    return answer;
}

