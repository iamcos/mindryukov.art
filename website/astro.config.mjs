import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://mindryukov.com',
  base: '/',
  outDir: '../dist',
  build: { assets: 'assets' },
  integrations: [tailwind()],
});
