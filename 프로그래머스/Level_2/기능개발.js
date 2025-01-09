function solution(progresses, speeds) {
  const complete = 100; // 진도 100
  let stack = []; // taskDays를 넣을거야.
  let maxDays = 0;
  let count = 0; // 배포 카운트
  let res = []; // 최종으로 들어가는 카운트이고,

  for (let i = 0; i < progresses.length; i++) {
    const remaining = complete - progresses[i]; // 남은 진도율
    const speed = speeds[i];

    const taskDays = Math.ceil(remaining / speed);

    stack.push(taskDays);
  }

  for (let j = 0; j < stack.length; j++) {
    if (stack[j] > maxDays) {
      // 0보다 지금 수가 커
      if (count > 0) {
        // 근데 count가 0보다 크면
        res.push(count); //그 count res에 push해
      }
      count = 1; // 그 때 count 1 !
      maxDays = stack[j]; // 이제 days가 더 큰게 나타나면 바꿔줌
    } else {
      // maxDays보다 지금 자신이 더 작아
      count++; // 그러면 count ++
    }
  }

  res.push(count); // 이제 다 합해서
  return res;
}
