const fs = require('fs');
const path = require('path');

const baseDir = __dirname;

function ensureDir(filePath) {
  const dirname = path.dirname(filePath);
  if (!fs.existsSync(dirname)) {
    fs.mkdirSync(dirname, { recursive: true });
  }
}

console.log("Generator script initialized.");
