function solution(s) {
    const dict = { "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    let number = ""
    let answer = "";
    for (const i of s) {
        if (!isNaN(i)) {
            answer += i
            continue
        }
        number += i
        if (dict[number]) {
            answer += dict[number]
            number = ""
        }
    }
    
    return Number(answer);
}