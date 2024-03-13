#!/usr/bin/node
exports.esrever = function (list) {
  newlist = [];
  for (j = list.length - 1; j >= 0; j--) {
    newlist.push(list[j]);
  }
  return newlist;
};
