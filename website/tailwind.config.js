/***** Tailwind config *****/
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './src/**/*.{astro,html,js,jsx,ts,tsx,md,mdx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        background: '#1a1a1a',
        foreground: '#fafafa',
        accent: '#d4a574'
      },
      fontFamily: {
        inter: ['Inter', 'system-ui', 'sans-serif'],
        rubik: ['Rubik', 'system-ui', 'sans-serif'],
        notoSC: ['"Noto Sans SC"', 'sans-serif'],
        notoArabic: ['"Noto Sans Arabic"', 'sans-serif']
      }
    }
  },
  plugins: []
}
