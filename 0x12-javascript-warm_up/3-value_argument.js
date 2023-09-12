#!/usr/bin/node
const argumentsPassed = process.argv;
if (argumentsPassed[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argumentsPassed[2]);
}
