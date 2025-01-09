function solution(brown, yellow) {
  // 가로 * 세로 === brown의 격자수 + yellow의 격자수 인거야
  // 근데 여기서 가로 , 세로가 같거나, 가로의 길이가 세로보다 길어야돼

  let grid = brown + yellow; // 총 격자의 수

  for (let x = 1; x <= Math.sqrt(grid); x++) {
    if (grid % x === 0) {
      let y = grid / x;

      if (y >= x) {
        return [y, x];
      }
    }
  }

  return [];
}
