function solution(a, d, included) {
    
    let total = 0; 
    
    for (let i=0; i < included.length; i++) {
        
        if (included[i]) {
            total += a + i*d; 
        }
    }
    
    return total;
    
    
    
}