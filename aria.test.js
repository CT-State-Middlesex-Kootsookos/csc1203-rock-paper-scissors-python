//**********************************************************************************
// Tests for ARIA tags in HTML file. 
// https://info340.github.io/standards-and-accessibility.html#aria
//**********************************************************************************
const fs = require('fs');
const path = require('path');

test('Has role attribute', () => {
  const filename = 'index.html'; // make sure the HTML file is named index.html
  const fileContent = fs.readFileSync(filename, 'utf8');
  expect(fileContent).toMatch(/role="/);
});

test('Has header tag', () => {
  const filename = 'index.html'; // make sure the HTML file is named index.html
  const fileContent = fs.readFileSync(filename, 'utf8');
  expect(fileContent).toMatch(/<header(.*)>/);
  expect(fileContent).toMatch(/<\/header>/);
});

test('Has nav tag', () => {
  const filename = 'index.html'; // make sure the HTML file is named index.html
  const fileContent = fs.readFileSync(filename, 'utf8');
  expect(fileContent).toMatch(/<nav(.*)>/);
  expect(fileContent).toMatch(/<\/nav>/);
});

test('Has main tag', () => {
  const filename = 'index.html'; // make sure the HTML file is named index.html
  const fileContent = fs.readFileSync(filename, 'utf8');
  expect(fileContent).toMatch(/<main(.*)>/);
  expect(fileContent).toMatch(/<\/main>/);
});

test('Has section tag', () => {
  const filename = 'index.html'; // make sure the HTML file is named index.html
  const fileContent = fs.readFileSync(filename, 'utf8');
  expect(fileContent).toMatch(/<section(.*)>/);
  expect(fileContent).toMatch(/<\/section>/);
});

test('Has footer tag', () => {
  const filename = 'index.html'; // make sure the HTML file is named index.html
  const fileContent = fs.readFileSync(filename, 'utf8');
  expect(fileContent).toMatch(/<footer(.*)>/);
  expect(fileContent).toMatch(/<\/footer>/);
});





