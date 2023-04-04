function solution(k, tangerine) {
    var answer = 0;
    
    const tDict = {}
    
    tangerine.forEach((t) => tDict[t] = (tDict[t] || 0) + 1)
    
    const arr = Object.values(tDict).sort((a,b) => b - a)
    
    for (const i of arr) {
        answer++
        
        if (k > i) {
            k -= i
        } else {
            break
        }
    }
    
    return answer;
}