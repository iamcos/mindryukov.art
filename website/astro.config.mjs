import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import react from '@astrojs/react';

// https://astro.build/config
export default defineConfig({
  base: process.env.BASE_URL ?? '/',
  integrations: [
    tailwind({
      applyBaseStyles: false,
    }),
    react(),
  ],
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'ru', 'ar', 'zh'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
});

