function solution(code) {
    
    let mode = 0; 
    let ret = ""; 
    
    for (let i=0; i < code.length; i++) {
        
        if (code[i] === "1") {
            mode = (mode === 0) ? 1 : 0; 
        } else {
            
            if ((i%2 && mode===1) || (i%2===0 && mode===0)){
                ret += code[i]; 
            }
            
        }
        
    }
    
    return ret.length ? ret : "EMPTY";
    
}