// Run by Node.js
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  // 입력 종료 후 처리

  // 예시: 2차원 배열로 변환
  const N = Number(input[0]);
  const matrix = input.slice(1).map((row) => row.split(" ").map(Number));
  const visited = Array.from({ length: N }, () => Array(N).fill(false));

  //dfs 함수 구현
  const dfs = (x, y) => {
    // 이 함수에 들어온 x,y true로
    visited[x][y] = true;
    const dx = [0, 1, 0, -1];
    const dy = [1, 0, -1, 0];

    let count = 1; // 카운트 변수 무조건

    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (0 <= nx && nx < N && 0 <= ny && ny < N) {
        if (matrix[nx][ny] === 1 && !visited[nx][ny]) {
          count += dfs(nx, ny);
        }
      }
    }

    return count;
  };

  let countss = [];
  let result = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (matrix[i][j] === 1) {
        const counts = dfs(i, j);
        if (counts > 0) {
          countss.push(counts);
          result++;
        }
      }
    }
  }

  console.log(result);
  console.log(countss.sort((a, b) => a - b).join(" "));
});
