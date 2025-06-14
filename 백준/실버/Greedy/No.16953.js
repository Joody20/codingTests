const input = require("fs").readFileSync("input.txt", "utf-8").trim();

let [a, b] = input.split(" ").map(Number);

let count = 0;

while (a < b) {
  if (b % 10 === 1) {
    b = (b - 1) / 10;
  } else if (b % 2 === 0) {
    b /= 2;
  } else {
    break;
  }
  count += 1;
}

if (a === b) {
  console.log(count + 1);
} else {
  console.log(-1);
}
