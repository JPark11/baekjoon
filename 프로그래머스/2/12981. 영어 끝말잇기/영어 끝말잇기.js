function solution(n, words) {
    
    const used = new Set(); 
    
    let start = words[0][0]; 
    
    for (let i=0; i<words.length; i++) {
        
        if (words[i].length === 1 || used.has(words[i]) || words[i][0] !== start) {
            return [i%n+1, Math.floor(i/n)+1];
            
        } else {
            used.add(words[i]); 
            start = words[i][words[i].length-1]; 
        }
    }
    
    return [0, 0];
}