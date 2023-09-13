#!/usr/bin/node
exports.esrever = function (list) {
  const myList = [];
  const listIndex = list.length - 1;
  for (let i = listIndex, j = 0; i >= 0; i--, j++) {
    myList[j] = list[i];
  }
  return myList;
};
