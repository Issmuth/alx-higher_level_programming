#!/usr/bin/node
const args = process.argv;
let max = Number.NEGATIVE_INFINITY;
if (!args[3]) {
   console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    if (max < args[i]) {
      max = args[i];
    }
  }
  let secMax = Number.NEGATIVE_INFINITY;
  args.filter(function (elements) {
    return elements !== max
  });
  for (i = 0; i < args.length; i++) {
    if (secMax < args[i]) {
	secMax = args[i];
    }
  }
  	console.log(secMax);
}
