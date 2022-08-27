function solution(survey, choices) {
    dict = { "R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0 }
    
    for (const i of survey.keys()) {
        const N = choices[i]
        if (N < 4) {
            dict[survey[i][0]] += 4 - N
        } else if (N > 4) {
            dict[survey[i][1]] += N - 4
        }
    }
    
    var answer = '';
    if (dict["R"] >= dict["T"]) {
        answer += "R"
    } else {
        answer += "T"
    } 
    if (dict["C"] >= dict["F"]) {
        answer += "C"
    } else {
        answer += "F"
    } 
    if (dict["J"] >= dict["M"]) {
        answer += "J"
    } else {
        answer += "M"
    } 
    if (dict["A"] >= dict["N"]) {
        answer += "A"
    } else {
        answer += "N"
    } 
    return answer;
}