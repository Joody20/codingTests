// function permute(nums) {
//   const result = [];

//   function backtrack(path) {
//     if (path.length === nums.length) {
//       result.push([...path]);
//       return;
//     }

//     for (let i = 0; i < nums.length; i++) {
//       if (path.includes(nums[i])) continue;
//       path.push(nums[i]);
//       backtrack(path);
//       path.pop();
//     }
//   }

//   backtrack([]);
//   return result;
// }

// console.log(permute([1, 2, 3])); // [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

// function maxMeetings(start, end) {
//   let meetings = [];
//   for (let i = 0; i < start.length; i++) {
//     meetings.push({ start: start[i], end: end[i] });
//   }

//   meetings.sort((a, b) => a.end - b.end); // 종료시간이 빠른 순으로 정렬

//   let count = 1;
//   let lastEnd = meetings[0].end;

//   for (let i = 1; i < meetings.length; i++) {
//     if (meetings[i].start >= lastEnd) {
//       count++;
//       lastEnd = meetings[i].end;
//     }
//   }

//   return count;
// }
// console.log(maxMeetings([1, 2, 3, 3], [2, 3, 4, 5])); // 3

// function bfs(graph, start) {
//   const visited = new Set();
//   const queue = [start];

//   while (queue.length > 0) {
//     const node = queue.shift();
//     if (!visited.has(node)) {
//       console.log(node);
//       visited.add(node);  // 방문처리
//       queue.push(...graph[node]);
//     }
//   }
// }

// // 예시 그래프
// const graph = {
//   A: ["B", "C"],
//   B: ["D", "E"],
//   C: ["F"],
//   D: [],
//   E: ["F"],
//   F: [],
// };

// bfs(graph, "A");

//미로 최단거리
// 0은 길, 1은 벽, 시작점에서 도착점까지의 최단거리

// function Maze(grid, start, end) {
//   const rows = grid.length; // 파이썬은 len(grid)
//   const cols = grid[0].length; // len(grid[0])

//   const visited = Array.from({ length: rows }, () => Array(cols).fill(false));

//   const directions = [
//     [0, 1],
//     [1, 0],
//     [0, -1],
//     [-1, 0],
//   ];

//   const queue = [[...start, 0]]; // [x,y, distance]
//   visited[start[0]][start[1]] = true; // 시작점 방문처리

//   while (queue.length > 0) {
//     const [x, y, dist] = queue.shift();
//     if (x === end[0] && y === end[1]) return dist;

//     for (const [dx, dy] of directions) {
//       const [nx, ny] = [x + dx, y + dy];

//       if (
//         0 <= nx &&
//         nx < rows &&
//         0 <= ny &&
//         ny < cols &&
//         !visited[nx][ny] &&
//         grid[nx][ny] === 0
//       ) {
//         visited[nx][ny] = true;
//         queue.push([nx, ny, dist + 1]);
//       }
//     }
//   }

//   return -1;
// }

// const maze = [
//   [0, 1, 0, 0],
//   [0, 1, 0, 1],
//   [0, 0, 0, 0],
//   [1, 1, 1, 0],
// ];

// console.log(Maze(maze, [0, 0], [2, 3])); // 출력: 5

let [left, right] = [0, 0];
console.log(left, right);
