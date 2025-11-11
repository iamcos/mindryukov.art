# Website Redesign Plan

## Design Philosophy
- **Authentic & Personal**: Reflect genuine personality and journey
- **Minimal & Clean**: Focus on content, not clutter
- **Warm & Inviting**: Convey the sense of home and connection mentioned in context
- **Modern & Professional**: Showcase creative work effectively

## Color Palette
- **Primary**: Warm earth tones (inspired by India, Thailand, nature)
- **Accent**: Soft blues/greens (wellness, calm)
- **Neutral**: Warm grays and whites
- **Text**: High contrast for readability

## Typography
- **Headings**: Modern, clean sans-serif
- **Body**: Readable serif or sans-serif
- **Supporting**: Monospace for technical/code content

## Page Structure

### 1. Home Page
- Hero section with personal introduction
- Featured work grid
- Quick links to main sections
- Brief about interests (Art, AI, Finance)

### 2. Work / Portfolio
- Film/video gallery
- Festival coverage
- Project descriptions
- Filter by category/type

### 3. About
- Personal journey
- Values and interests
- Travel experiences
- Growth and practices

### 4. Interests
- Art projects
- AI exploration
- Finance interests
- Intersection of these fields

### 5. Wellness
- Meditation and yoga practices
- Retreat center interests
- Personal growth journey
- Resources and reflections

### 6. Contact / Connect
- Social links
- Contact form (optional)
- Collaboration inquiries

## Components Needed

### Layout Components
- `Header.astro` - Navigation and language switcher
- `Footer.astro` - Links and copyright
- `BaseLayout.astro` - Main layout wrapper

### Content Components
- `Hero.astro` - Landing hero section
- `WorkGrid.astro` - Portfolio grid
- `VideoCard.astro` - Individual video/film card
- `Section.astro` - Reusable section wrapper
- `LanguageSwitcher.astro` - i18n language selector

### Feature Components
- `ImageGallery.astro` - Image gallery with lightbox
- `VideoPlayer.astro` - Embedded video player
- `Timeline.astro` - Journey/timeline component
- `Quote.astro` - Quote/testimonial component

## Responsive Design
- Mobile-first approach
- Breakpoints: 640px, 768px, 1024px, 1280px
- Touch-friendly interactions
- Optimized images for all devices

## Performance
- Lazy load images and videos
- Optimize assets
- Use Astro's static generation
- Minimal JavaScript

## Internationalization
- Support: English, Russian, Arabic, Chinese
- Language switcher in header
- RTL support for Arabic
- Translated content in data files

## Content Strategy
- Showcase best work prominently
- Tell personal story authentically
- Balance professional and personal
- Regular updates for new projects

