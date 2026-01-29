const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const arr_n = input[1].split(" ").map(Number);
let arr_m = input[2].split(" ").map(Number);

let P = 0;

for (const b of arr_m) {
  if (b == 0) P *= b;
}

for (const a of arr_n) {
  P += a;
}

arr_m
  .filter((x) => x >= 2)
  .sort((a, b) => b - a)
  .forEach((b) => (P *= b));

console.log(P);
