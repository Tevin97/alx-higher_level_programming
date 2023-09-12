#!/usr/bin/node
const count = process.argv.length;
if (count < 3) {
	console.log('No argument');
} else {
	console.log('Argument found');
}
