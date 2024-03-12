#!/usr/bin/node
if (!process.argv[2]) {
  console.log('No argument');
} else {
  process.argv.forEach(function (element, index) {
    if (index > 1) {
      console.log(element);
    }
  });
}
