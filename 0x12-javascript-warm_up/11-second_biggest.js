#!/usr/bin/node
const args = process.argv;
let max = args[0];
let max2 = args[0];
if (!args[3]) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    if (max < args[i]) {
      max2 = max;
      max = args[i];
    } else if (max2 < args[i] && max2 !== max) {
      max2 = args[i];
    }
  }
  console.log(max2);
}
