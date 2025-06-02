const { debugPort } = require("process");

const input = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m, k] = input[0].split(" ").map(Number);
const weights = input[1].split(" ").map(Number);

let res = Infinity;

// DFS - backtracking
const simulate = (order) => {
  let box = 0;
  let work = 0;
  let total = 0;
  let idx = 0;

  while (work < k) {
    if (box + order[idx] <= m) {
      box += order[idx];
      idx = (idx + 1) % n;
    } else {
      total += box;
      box = 0;
      work++;
    }
  }
  res = Math.min(res, total);
};

const dfs = (depth, visited, order) => {
  if (depth === n) {
    simulate(order);
    return;
  }

  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      visited[i] = true;
      order.push(weights[i]);
      dfs(depth + 1, visited, order);
      order.pop();
      visited[i] = false;
    }
  }
};

dfs(0, Array(n).fill(false), []);

console.log(res);

// // 순열 알고리즘 구현
// const permutaions = (arr, num) => {
//   if (num === 1) return arr.map((v) => [v]);

//   const result = [];

//   arr.forEach((fixed, idx, origin) => {
//     const rest = origin.filter((_, i) => i != idx);
//     const perms = permutaions(rest, num - 1);
//     const attached = perms.map((p) => [fixed, ...p]);

//     result.push(...attached);
//   });

//   return result;
// };

// // n개의 레일로 할 수 있는 모든 방안
// let railInfos = permutaions(weights, n);

// let res = Infinity; // 초ㅣ대치

// for (let w of railInfos) {
//   let rails = [...w];

//   let i = 0;
//   let box = 0;
//   let work = 0;
//   let this_all = 0;

//   while (work != k) {
//     if (box + rails[i] <= m) {
//       box += rails[i];
//       i = (i + 1) % n; // 이걸 꼭 해줘야돼.
//       //   rails.push(rails[i]);
//     } else {
//       this_all += box;
//       box = 0;
//       work++;
//     }
//   }

//   res = Math.min(res, this_all);
// }

// console.log(res);
