const input = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const cards = input[1].split(" ").map(Number);

cards.sort((a, b) => a - b);

let count = 0;
let sum = 0;
let res = 0;

for (let i = 0; i < n; i++) {
  if (count === m) break;

  sum = cards[i] + cards[i + 1];
  cards[i] = sum;
  cards[i + 1] = sum;
  count++;
}

res = cards.reduce((a, b) => a + b, 0);

console.log(res);
