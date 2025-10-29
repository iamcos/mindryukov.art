import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://iamcos.github.io',
  base: '/mindryukov.art/',
  outDir: '../dist',
  build: { assets: 'assets' },
  integrations: [tailwind()],
});
