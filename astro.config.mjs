// @ts-check
import { defineConfig } from 'astro/config';

// For GitHub Pages under a project path, set SITE_URL and BASE_PATH, for example
// SITE_URL=https://adityashinde521.github.io BASE_PATH=/contract-commons npm run build
export default defineConfig({
  site: process.env.SITE_URL || 'http://localhost:4321',
  base: process.env.BASE_PATH || '/',
  trailingSlash: 'always',
  build: { format: 'directory' },
});
