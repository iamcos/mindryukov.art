# Coding Conventions

## File Naming
- **Components**: PascalCase (e.g., `Header.astro`, `VideoGallery.astro`)
- **Utilities**: camelCase (e.g., `formatDate.ts`, `fetchData.ts`)
- **Pages**: kebab-case (e.g., `about.astro`, `contact.astro`)
- **Data files**: kebab-case (e.g., `site-config.json`, `projects.json`)

## Component Structure

### Astro Components
```astro
---
// 1. Imports
import type { ComponentProps } from 'astro/types';
import { formatDate } from '../utils/formatDate';

// 2. Props interface
interface Props {
  title: string;
  date?: Date;
}

// 3. Props destructuring
const { title, date } = Astro.props;

// 4. Computed values
const formattedDate = date ? formatDate(date) : null;
---

<!-- 5. Template -->
<div class="component">
  <h2>{title}</h2>
  {formattedDate && <time>{formattedDate}</time>}
</div>

<style>
  .component {
    /* Scoped styles if needed */
  }
</style>
```

## TypeScript Conventions
- Use interfaces for object shapes
- Use types for unions and intersections
- Avoid `any` - use `unknown` if type is truly unknown
- Export types/interfaces from dedicated files

## CSS/Tailwind Conventions
- Prefer Tailwind utilities over custom CSS
- Use `@apply` sparingly for repeated patterns
- Group Tailwind classes logically: layout → spacing → typography → colors → effects
- Example: `flex items-center gap-4 text-lg text-gray-800 hover:text-blue-600`

## Import Organization
1. External libraries
2. Internal utilities
3. Components
4. Types
5. Styles (if needed)

Example:
```typescript
import { format } from 'date-fns';
import { getPosts } from '../utils/posts';
import Header from '../components/Header.astro';
import type { Post } from '../types';
```

## Error Handling
- Use try-catch for async operations
- Provide user-friendly error messages
- Log errors for debugging (remove in production)

## Comments
- Explain "why", not "what"
- Use JSDoc for functions
- Remove commented-out code before committing

## Accessibility
- Always include `alt` attributes for images
- Use proper heading hierarchy (h1 → h2 → h3)
- Ensure interactive elements are keyboard accessible
- Use ARIA labels when semantic HTML isn't sufficient

