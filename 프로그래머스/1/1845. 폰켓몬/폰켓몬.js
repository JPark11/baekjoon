function solution(nums) {
    
    const pokeTypes = [...new Set(nums)];
    const half = nums.length / 2;
    
    return pokeTypes.length > half ? half : pokeTypes.length; 
    
}