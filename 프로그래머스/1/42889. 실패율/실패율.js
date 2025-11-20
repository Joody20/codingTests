function solution(N, stages) {
    const stage_counts = {}
    let users = stages.length
    let result = {}
    
    for(const v of stages){
        stage_counts[v] = (stage_counts[v] || 0) + 1;
    }
    
    for(let i=1; i<N+1; i++){
        let counts = stage_counts[i]
        if(counts == undefined){
            counts = 0
        }
        
        if (users === 0){
            result[i] = 0
        }
        else{
            result[i] = counts / users
        }
        
        users = users - counts
    }
    
    const ans = Object.entries(result).sort((a,b) => b[1] - a[1]).map(([key]) => +key)
    
    return ans
            
}