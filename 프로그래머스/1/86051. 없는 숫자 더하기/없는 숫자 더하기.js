function solution(numbers) {
    
    let total = 45; 
    
    numbers.forEach(e=>total-=e)
    
    return total; 
    
}