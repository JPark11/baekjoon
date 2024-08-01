function solution(answers) {
    
    const p1 = [1, 2, 3, 4, 5]; 
    const p2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const p3 = [3, 1, 2, 4, 5];
    
    const correct = [0, 0, 0]; 
    
    for (let i=0; i<answers.length; i++) {
        
        if (p1[i%5] === answers[i]) correct[0] += 1; 
        if (p2[i%8] === answers[i]) correct[1] += 1; 
        if (p3[Math.floor(i/2) %5] === answers[i]) correct[2] += 1;       
    }
    
    const ans = [];
    
    for (i=0; i<3; i++) {
        if (correct[i] === Math.max(...correct)) {
            ans.push(i+1); 
        }
    }
    
    ans.sort((a,b)=>a-b); 
    
    return ans;
    
    return ans; 
                   
                   
}