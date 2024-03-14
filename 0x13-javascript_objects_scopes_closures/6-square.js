#!/usr/bin/node
const Sq = require('./5-rectangle');
module.exports = class Square extends Sq {
  constructor (size) {
	  super(size, size);
  }

  charPrint (c) {
    let ch = c;
    if (!ch) {
      ch = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row = row + ch;
      }
      console.log(row);
    }
  }
};
