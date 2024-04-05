function solution(s)
{
    const stack = []; 
    let idx = 0; 
    
    while (idx < s.length) {
        if (stack.length && stack[stack.length-1] === s[idx]) {
            stack.pop(); 
        } else {
            stack.push(s[idx]); 
        }  
        idx += 1; 
    }
    
    return stack.length ? 0 : 1
    
    
}