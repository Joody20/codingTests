const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const T = parseInt(input[0]);
let result = [];
for (let i = 1; i <= T; i++) {
  const [a, b] = input[i].split(" ").map(Number);

  result.push(a + b);
}

console.log(result.join("\n"));
