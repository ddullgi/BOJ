function solution(numbers) {
    numbers.sort(compare)
    var answer = numbers.join("");
    if (answer[0] === "0" ) {
        answer = "0"
    }
    return answer;
}

const compare = (a, b) => {
    const ab = String(a) + String(b)
    const ba = String(b) + String(a)  
    return  ba - ab
}