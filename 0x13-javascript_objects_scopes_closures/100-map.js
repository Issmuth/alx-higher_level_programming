#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newlist = list.map((val, index) => {
  return val * index;
});
console.log(newlist);
