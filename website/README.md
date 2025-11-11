# mindryukov films Website

A modern, personal portfolio website built with Astro, showcasing film work, creative projects, and personal journey.

## Features

- 🎨 Modern, responsive design
- 🌍 Multi-language support (English, Russian, Arabic, Chinese)
- ⚡ Fast static site generation with Astro
- 🎭 Beautiful UI with Tailwind CSS
- 📱 Mobile-first responsive design
- ♿ Accessible and semantic HTML

## Tech Stack

- **Framework**: [Astro](https://astro.build/)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Language**: TypeScript
- **Package Manager**: npm

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open [http://localhost:4321](http://localhost:4321) in your browser

### Build

Build for production:
```bash
npm run build
```

Preview the production build:
```bash
npm run preview
```

## Project Structure

```
website/
├── public/          # Static assets
├── src/
│   ├── components/  # Reusable components
│   ├── layouts/    # Page layouts
│   ├── pages/      # Astro pages
│   └── data/       # Data files (i18n)
├── astro.config.mjs
├── tailwind.config.mjs
└── package.json
```

## Pages

- **Home** (`/`) - Landing page with hero and featured work
- **Work** (`/work`) - Portfolio of projects
- **About** (`/about`) - Personal journey and values
- **Interests** (`/interests`) - Art, AI, Finance
- **Wellness** (`/wellness`) - Practices and growth
- **Contact** (`/contact`) - Get in touch

## Development

See `.cursor/development-standards.md` for detailed development guidelines and coding conventions.

## License

All rights reserved.

