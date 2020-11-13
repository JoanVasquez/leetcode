var isHappy = function(n) {
    
    const seen = {}
    
    while (n != 1) {
        if (n in seen) {
            return false 
        } else {
            seen[n] = n
            n = n.toString().split('').reduce((acc, num) => acc + (num * num), 0)
        }
    }
    return true 
};
