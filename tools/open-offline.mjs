// Prints where to open the offline copy after a build.
import { resolve } from 'node:path';
console.log('Offline site ready. Open this file in your browser:\n  ' + resolve('dist/index.html'));
