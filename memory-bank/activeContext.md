# Active Context

## Code Changes (2026-08-18 19:50:00)

### Added Files
- `projects/index.html` — portfolio overview page listing completed projects (cards + tags + CTA)
- `projects/solar-portlaoise.html` — project detail page for the Solar PV + Zappi EV charger install in Portlaoise (photos from `Projects/Solar/`, system specs, highlights, CTA)
- `projects.css` — shared styles for the projects pages

### Modified Files
- `index.html` — added "Projects" nav link, linked gallery solar image to the project detail page, added "View All Projects" button in the gallery section, added `.gallery-cta`/`.section-link` styles to the inline CSS
- `sitemap.xml` — added `https://maherelectrical.ie/projects/` and `https://maherelectrical.ie/projects/solar-portlaoise.html`

### Notes
- Project photos are referenced in place from `Projects/Solar/` (user-created folder)
- New pages link `../style.css` and `../projects.css` (homepage keeps its inlined CSS for LCP)


## Code Changes (2026-08-18 19:35:52)

### Added Files
- index.html
- script.js
- sitemap.xml
- style.css
- style.min.css


## Code Changes (2026-06-30 09:15:31)

### Added Files
- index.html
- script.js
- sitemap.xml
- style.css


## Code Changes (2026-06-30 08:54:41)

### Added Files
- index.html
- script.js
- style.css


## Current Work Focus
Domain binding configuration for production deployment.

## Recent Changes
- Added canonical URL (`https://maherelectrical.ie/`) to `index.html`
- Added Open Graph and Twitter Card meta tags for social sharing
- Created `CNAME` file with `maherelectrical.ie` for host-level domain binding
- Updated `techContext.md` with domain and hosting details

## Next Steps
- Configure hosting provider (GitHub Pages/Netlify/Vercel) to use custom domain
- Update DNS records (A/AAAA or CNAME) to point to hosting servers
- Verify HTTPS/SSL is active on the production domain

## Code Changes (2026-06-29 12:08:23)

### Added Files
- index.html
- script.js
- style.css

## Code Changes (2026-06-29)

### Added Files
- `CNAME` — domain binding file for maherelectrical.ie

### Modified Files
- `index.html` — added canonical link, Open Graph, and Twitter Card meta tags
- `memory-bank/techContext.md` — documented domain, hosting, and SEO configuration
