function solution(word) {
  let answer = 0;
  let c = [781, 156, 31, 6, 1];
  let arr = ["A", "E", "I", "O", "U"];
  for (let i = 0; i < word.length; i++) {
    answer += arr.indexOf(word[i]) * c[i] + 1;
  }
  return answer;
}
