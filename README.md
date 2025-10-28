# mindrtukov

Archive of `@mindryukov_films` + Multilingual Portfolio (Astro)

## Structure

- `scripts/`: Python tools for download, repair, verify
- `website/`: Astro static site (EN/RU/AR/ZH)
- `data/`: Telegram metadata (ignored except `website_summary.json`)
- `media/`: Local media cache (ignored; only small thumbs in `website/public/assets/thumbs`)

## Setup

### Python
```bash
python -m venv .venv
source .venv/bin/activate
pip install telethon python-dotenv
```

Run downloader:
```bash
python scripts/downloader/main.py
```

Repair missing media/text:
```bash
python scripts/repair/missing_media.py
python scripts/repair/missing_text.py
```

Verify dataset:
```bash
python scripts/verify/dataset.py
```

### Website
```bash
cd website
npm install
npm run dev
```

Build for GitHub Pages:
```bash
npm run build
```
`dist/` is output at repository root as configured.

## Secrets
Copy `.env.example` to `.env` and fill `API_ID` and `API_HASH` from `my.telegram.org`.

## Notes
- Large media (`media/videos`, `media/audio`, `media/documents`) are git-ignored.
- `data/posts_metadata` and `data/profile_info` are ignored; use `data/website_summary.json` to feed the website.
- Legacy tool remains under `scripts/legacy/telegram-mcp`.

## GitHub Pages
- Default branch: `main`
- Workflow: `.github/workflows/gh-pages.yml` builds the Astro site and deploys Pages on push to `main`.
- In repo settings → Pages: set Source to "GitHub Actions".
