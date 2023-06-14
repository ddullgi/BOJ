function solution(today, terms, privacies) {
    var answer = [];
    const tday = new Date(today)
    const termInfo = {}
    terms.forEach(term => {
        const info = term.split(" ")
        termInfo[info[0]] = info[1]
    })
    
    privacies.forEach((privacy, i) => {
        const info = privacy.split(" ")
        const day = new Date(info[0])
        day.setMonth(day.getMonth() + Number(termInfo[info[1]]))
        console.log()
        if (day <= tday){
            answer.push(i + 1)
        }
    })
    return answer;
}