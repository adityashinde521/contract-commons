// @ts-check
import { defineConfig } from 'astro/config';

// For GitHub Pages under a project path, set SITE_URL and BASE_PATH, for example
// SITE_URL=https://adityashinde521.github.io BASE_PATH=/contract-commons npm run build
export default defineConfig({
  site: process.env.SITE_URL || 'http://localhost:4321',
  base: process.env.BASE_PATH || '/',
  trailingSlash: 'always',
  build: { format: 'directory', assets: 'assets' },
  vite: {
    build: {
      rollupOptions: {
        output: {
          // No file names starting with "_": some static hosts reserve them.
          assetFileNames: (info) => (/\.css$/.test(info.names?.[0] || info.name || '') ? 'assets/site.[hash][extname]' : 'assets/[name].[hash][extname]'),
        },
      },
    },
  },
});
