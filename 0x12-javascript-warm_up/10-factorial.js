#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);
function factorial (num) {
  if (num === 0 | num === 1 | isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const result = factorial(num);
console.log(result);
