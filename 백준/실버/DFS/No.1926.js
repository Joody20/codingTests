const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
let graph = [];
for (let i = 1; i <= n; i++) {
  graph.push(input[i].split(" ").map(Number));
}

let result = 0;
let pic_counts = [];

const dfs = (x, y) => {
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];

  let count = 1;
  graph[x][y] = 0; // 방문 처리

  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];

    if (0 <= nx && nx < n && 0 <= ny && ny < m) {
      if (graph[nx][ny] === 1) {
        count += dfs(nx, ny);
      }
    }
  }

  return count;
};

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (graph[i][j] === 1) {
      let pic_count = dfs(i, j);
      if (pic_count > 0) {
        pic_counts.push(pic_count);
        result++;
      }
    }
  }
}

console.log(result);
console.log(pic_counts.sort((a, b) => a - b).join(" "));

// JS에서 배열을 문자열로 하려면 pic_counts.sort((a, b) => a - b) 배열에. join(" ")로 해줌!
