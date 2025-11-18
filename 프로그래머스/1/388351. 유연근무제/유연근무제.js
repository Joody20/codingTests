function solution(schedules, timelogs, startday) {
    
    let count = 0;
    const n = schedules.length // 직원의 수
   
    const schedules_submit = schedules.map((time) =>{
        let hour = Math.floor(time/100)
        let minute = time % 100
        
        minute += 10
        
        if (minute >= 60){
            hour += Math.floor(minute/60)
            minute %= 60
        }
        if(hour >= 24) hour %= 24;
        
        return hour * 100 + minute
    }); // 출근 인정 시간
    
    let results = Array.from({length: n}, () => Array(7).fill(0))  // true/false값 넣은 배열
    
    
    for(let i=0; i<n; i++){
        for (let j=0; j<7;j++){
            // 주말 건너뛰기
            if ((j + startday) % 7 === 6 || (j + startday) % 7 === 0) continue;    
            
            if (timelogs[i][j] <= schedules[i] ||
                schedules[i] <= timelogs[i][j] &&  
                timelogs[i][j] <= schedules_submit[i]){
                results[i][j] = 0
            }
            else{
                results[i][j] = 1
            }
        }
    }
    
    
    for(const result of results){
        if(!result.includes(1)){
            count++;
        }
    }
    
    return count
    
 
}