function solution(s) {
  // s에 있는 문자열을 하나씩 어떤 stack 안에 순차대로 넣어
  // ( , ) 의 개수가 맞게 있다면 true, 짝지어져 있지 않으면 false

  let stack = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push("(");
    } else if (s[i] === ")") {
      if (stack.length === 0) {
        return false;
      }
      stack.pop();
    }
  }

  if (stack.length === 0) {
    return true;
  } else {
    return false;
  }
}
