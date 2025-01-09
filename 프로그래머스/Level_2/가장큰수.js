function solution(numbers) {
  //     const max_Num= Number(numbers.join(''));  // 이건 그냥 지금 numbers에 있는 숫자 join 하는거자나
  //     // 근데 numbers에 있는 모든 숫자의 조합 중 가장 큰 숫자를 출력해야해.
  //     if(max_Num >= numbers)  // ㅎㅕㄴ재 조합된 숫자가 원래 조합했던 숫자보다 크면 계속 업데이트

  const string = numbers.map(String);

  string.sort((a, b) => b + a - (a + b)); // 내림차순 정렬이야

  const result = string.join("");

  return result[0] === "0" ? "0" : result;
}
