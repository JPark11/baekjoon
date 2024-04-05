function solution(brown, yellow) {
    const sum = (brown - 4) / 2; 
    
    for (let i=1; i<sum; i++) {
        if (i * (sum-i) === yellow) {
            return [sum-i+2, i+2]; 
        }
    }
}