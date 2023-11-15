function solution(s) {
    let answer = s.length;
    
    for(let i = 1; i <= s.length / 2; i++) {
        let temp = "";
        let cnt = 1;
        
        for(let j = 0; j < s.length; j += i) {
            let s1 = s.slice(j, j + i);
            
            while(true) {
                j += i;
                let s2 = s.slice(j, j + i);
                if(s1 === s2) {
                    cnt++;
                } else {
                    break;
                }
            }
            temp += cnt >= 2 ? cnt + s1 : s1;
            j -= i;
            cnt = 1;
        }
        answer = Math.min(temp.length, answer);
    }
    return answer;
}