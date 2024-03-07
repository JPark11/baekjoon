function solution(a, b) {
    A = a.toString() 
    B = b.toString() 
    const answer = Math.max(parseInt(A+B), parseInt(B+A))
    return answer;
}