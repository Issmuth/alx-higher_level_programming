#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
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
