#!/usr/bin/node
const argv = process.argv;
if (!argv[2] || !argv[3]) {
  console.log(0);
} else {
  const sortedArgv = argv.sort((a, b) => a - b);
  console.log(sortedArgv[sortedArgv.length - 2]);
}
