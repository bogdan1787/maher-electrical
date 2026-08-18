# Active Context

## Code Changes (2026-08-18 - Lighthouse/SEO pass)

### Modified Files
- `index.html` - fixed color contrast on `.contact-facebook h3` and `.footer-social` (Facebook blue `#1877F2` -> `#4B9CFF`, WCAG AA); fixed `.mobile-cta-whatsapp` (white on `#25D366` -> dark green `#0A3D24` text); added `width`/`height` attributes to all images (incl. footer logo - CLS fix); wrapped main content in `<main>` landmark
- `projects/index.html` - wrapped content in `<main>`; aria-label on featured project link now includes visible "Featured" text (label-content-name-mismatch fix); added `width`/`height` to images
- `projects/solar-portlaoise.html` - wrapped content in `<main>`; added `width`/`height` to all gallery images (CLS fix)
- `style.css` - `.mobile-cta-whatsapp` color `#fff` -> `#0A3D24`
- `projects.css` - `.tag` color `var(--accent)` -> `#4B9CFF` (4.2:1 -> 4.86:1)

### Notes
- Lighthouse (mobile + desktop) now 100/100/100/100 (a11y / best-practices / SEO / agentic-browsing) on all three pages, verified locally
- Homepage performance: LCP ~480ms, CLS 0.04 (font-swap only)
- `script.js` and `style.min.css` are not referenced by any HTML (dead files, kept for reference)

## Code Changes (2026-08-18)

### Modified Files
- `index.html` — removed the "Our Work" gallery section (redundant with the Featured Project section and the Projects page); removed the Gallery nav link; removed now-unused `.gallery-*` / `.section-link` inline CSS; removed the two photos from the Community section and centered the quote (`.community-content` now single column)
- `projects/index.html` — removed the Gallery nav link
- `projects/solar-portlaoise.html` — removed the Gallery nav link
- `style.css` — removed unused `.gallery-*`, `.gallery-cta`, `.section-link` styles

### Notes
- Nav order everywhere: Home, Services, Projects, Areas, About, Certifications, Contact
- Portfolio content now lives solely on the Projects page (`projects/`)

## Code Changes (2026-08-18 20:30:00)

### Modified Files
- `index.html` — nav reordered (Projects now 3rd, before Areas); added `#projects` "Featured Project" section on the homepage (split image/text card with cover photo, spec chips, View Project / All Projects CTAs); new `.featured-*` styles in the inline CSS
- `projects/index.html` — nav reordered; featured full-width card layout (`grid-column: 1 / -1`) with the new cover photo `766194664` and "Featured" badge; og:image updated to cover photo
- `projects/solar-portlaoise.html` — nav reordered; added full-width cover photo feature image above the intro/sidebar layout; og:image updated to cover photo
- `projects.css` — added `.project-card.featured`, `.project-tag`, `.feature-image` styles + responsive rules
- `style.css` / `style.min.css` — synced with the new `.featured-*`, `.gallery-cta`, `.section-link` styles

### Notes
- Cover photo for the Solar project is now `projects/Solar/766194664_122125223781262619_1213147107600065272_n.jpg` (portrait 1440x1919)
- Nav order everywhere: Home, Services, Projects, Areas, About, Gallery, Certifications, Contact

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
