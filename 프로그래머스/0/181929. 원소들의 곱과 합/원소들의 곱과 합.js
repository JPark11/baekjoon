function solution(num_list) {
    const prod = num_list.reduce((acc, val) => {       
        return acc * val 
    }, 1)
    
    const total = num_list.reduce((acc, val) => {
        return acc + val 
    }, 0)
    
    return prod < total * total ? 1 : 0
}