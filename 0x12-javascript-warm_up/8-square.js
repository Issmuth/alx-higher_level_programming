#!/usr/bin/node
const num = Number(process.argv[2]);
if (Number.isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
