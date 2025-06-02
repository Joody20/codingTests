// Sam은 팀장님으로부터 차량이 이동 가능한 시나리오의 수를 찾으라는 업무 지시를 받았습니다. 이동은 숫자 0과 1로만 이루어져 있는 n x n 크기의 격자 위에서 일어납니다. 숫자 0은 빈 칸을 의미하며, 숫자 1은 해당 칸이 벽으로 막혀 있음을 의미합니다. 아래는 n이 3인 경우의 예시입니다.

// 0 0 0
// 0 0 0
// 0 0 1

// 차량은 n x n 격자 내에서 m개의 지점을 순서대로 방문하려고 합니다. 이 때 이동은 항상 상하좌우 중 인접한 칸으로만 이동하되 벽은 지나갈 수 없으며, 한 번 지났던 지점은 다시는 방문해서는 안 됩니다. 이러한 조건 하에서 차량이 이동 가능한 서로 다른 가지 수를 구하는 프로그램을 작성해보세요.

// 방문해야 하는 지점의 첫 지점이 출발점이며, 마지막 지점이 도착점임에 유의합니다.

// 위의 예에서 m = 3, 방문해야 하는 지점이 순서대로 (3행, 1열), (1행, 2열), (2행, 3열)이라면, 다음과 같이 5가지의 시나리오가 가능합니다.

// 즉, 방문해야 하는 지점까지의 방법의 수를 구해라!

const input = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const graph = [];
for (let i = 1; i <= n; i++) {
  graph.push(input[i].split(" ").map(Number));
}

const must = []; // 방문해야하는 지점
for (let i = n + 1; i <= n + m; i++) {
  const [x, y] = input[i].split(" ").map(Number);
  must.push([x - 1, y - 1]);
}

let cnt = 0;

const dfs = (x, y, idx) => {
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];

  if (x === must[idx][0] && y === must[idx][1]) {
    if (idx === m - 1) {
      cnt++;
      return;
    } else {
      idx++;
    }
  }

  for (let i = 0; i <= n; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];

    if (0 <= nx && nx < n && 0 <= ny && ny < n) {
      if (!visited[nx][ny] && graph[nx][ny] === 0) {
        visited[nx][ny] = true;
        dfs(nx, ny, idx);
        visited[nx][ny] = false;
      }
    }
  }
};

const visited = Array.from({ length: n }, () => Array(n).fill(false));
visited[must[0][0]][must[0][1]] = true;
dfs(must[0][0], must[0][1], 0); // 현재ㅏ좌표, 방문해야할 인덱스
console.log(cnt);
