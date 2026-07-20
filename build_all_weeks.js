const fs = require('fs');
const path = require('path');

const baseDir = '/home/thededar/Downloads/Workspace/test2/German-A1-Self-Study';

function ensureDir(filePath) {
  const dirname = path.dirname(filePath);
  if (!fs.existsSync(dirname)) {
    fs.mkdirSync(dirname, { recursive: true });
  }
}

console.log("Generator script initialized.");
