const input = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input[0]);
const classes = [];
for (let i = 1; i <= N; i++) {
  classes.push(input[i].split(" ").map(Number));
}

classes.sort((a, b) => {
  if (a[1] === b[1]) return a[0] - b[0];
  return a[1] - b[1];
});

let heap = [classes[0][1]];

for (let i = 1; i < N; i++) {
  if (heap[0] <= classes[i][0]) {
    heap.shift();
  }
  heap.push(classes[i][1]);
}

console.log(heap.length);
