const input = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n");
const N = Number(input[0]);
const arr_A = input[1].split(" ").map(Number);
const arr_B = input[2].split(" ").map(Number);

arr_A.sort((a, b) => a - b); // A는 오름차순으로 정렬
arr_B.sort((a, b) => b - a); // B는 내림차순으로 정렬

let cur_sum = 0;

for (let i = 0; i < N; i++) {
  cur_sum += arr_A[i] * arr_B[i];
}

// min_sum = Math.min(min_sum, cur_sum);

console.log(cur_sum);
