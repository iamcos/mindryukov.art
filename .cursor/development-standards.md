# Development Standards & Guidelines

## Project Overview
This is a personal website for mindryukov_films - a creative portfolio showcasing film work, festivals, and personal projects.

## Technology Stack

### Frontend
- **Framework**: Astro
- **Styling**: Tailwind CSS
- **Language**: TypeScript
- **Package Manager**: npm

### Backend/Utilities
- **Python**: For data processing scripts
- **Virtual Environment**: `.venv` (local Python environment)

## Project Structure

```
mindrtukov/
├── .cursor/              # Development standards and guides
├── .venv/                # Python virtual environment
├── website/              # Astro website
│   ├── src/
│   │   ├── components/  # Reusable components
│   │   ├── layouts/      # Page layouts
│   │   ├── data/         # Data files (i18n: en, ru, ar, zh)
│   │   └── pages/        # Astro pages
│   ├── public/           # Static assets
│   └── package.json      # Node dependencies
├── context/              # Context files and chatlogs
├── mindryukov_films/      # Telegram channel data
└── scripts/              # Utility scripts
```

## Code Standards

### TypeScript/JavaScript
- Use TypeScript for type safety
- Follow ESLint configuration
- Use meaningful variable names
- Comment complex logic
- Prefer functional components

### Astro Components
- Use `.astro` file extension
- Keep components focused and reusable
- Use Astro's component syntax: `---` for script, HTML for template
- Leverage Astro's built-in optimizations

### Styling
- Use Tailwind CSS utility classes
- Create custom components for repeated patterns
- Ensure responsive design (mobile-first)
- Maintain consistent spacing and typography

### Python Scripts
- Use type hints where possible
- Follow PEP 8 style guide
- Document functions with docstrings
- Use virtual environment (`.venv`)

## Git Workflow

### Branch Naming
- `main` - Production-ready code
- `develop` - Development branch
- `feature/feature-name` - New features
- `fix/bug-name` - Bug fixes

### Commit Messages
- Use clear, descriptive messages
- Format: `type: description`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Development Workflow

### Starting Development
1. Activate Python virtual environment: `source .venv/bin/activate`
2. Install Node dependencies: `cd website && npm install`
3. Start Astro dev server: `npm run dev`

### Building
- Frontend: `cd website && npm run build`
- Python scripts: Run from `.venv` environment

## Environment Variables
- Store sensitive data in `.env` files (not committed)
- Use `.env.example` as template
- Document required variables in README

## Testing
- Test components in isolation
- Verify responsive design on multiple devices
- Check browser compatibility

## Performance
- Optimize images before adding to `public/`
- Use Astro's built-in image optimization
- Minimize JavaScript bundle size
- Leverage Astro's static site generation

## Accessibility
- Use semantic HTML
- Include alt text for images
- Ensure keyboard navigation
- Maintain proper heading hierarchy
- Test with screen readers

## Internationalization (i18n)
- Support: English (en), Russian (ru), Arabic (ar), Chinese (zh)
- Store translations in `src/data/{lang}/`
- Use consistent translation keys
- Test all language versions

## Deployment
- Build command: `npm run build`
- Output directory: `website/dist`
- Ensure all static assets are in `public/`

