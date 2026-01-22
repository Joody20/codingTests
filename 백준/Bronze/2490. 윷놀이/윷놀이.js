const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

for (let i = 0; i < input.length; i++) {
  const count_0 = input[i].split("0").length - 1;
  const count_1 = input[i].split("1").length - 1;

  if (count_0 === 1 && count_1 === 3) {
    console.log("A");
  } else if (count_0 === 2 && count_1 === 2) {
    console.log("B");
  } else if (count_0 === 3 && count_1 === 1) {
    console.log("C");
  } else if (count_0 === 4) {
    console.log("D");
  } else if (count_1 === 4) {
    console.log("E");
  }
}
