# Active Context

## Code Changes (2026-09-12 — UI/UX overhaul, phases 0-2)

### Modified Files
- `style.css` — global `img { max-width:100%; height:auto }` (fixes stretched images sitewide); `scroll-padding-top` for fixed header; skip-link styles; `.nav-call` desktop call button; mobile nav breakpoint 768→1024px and menu offset 72→88px; `.hero` photo background + trust badges; compact horizontal `.cert-card` + `.cert-dialog` lightbox; `.about-quote`; consolidated `.card-link` / `.area-card a` / `.contact-facebook`; JS-gated `.reveal` with `prefers-reduced-motion`; section padding 100→80px (56px mobile); hero CTA hidden on mobile (sticky bar covers it)
- `areas.css` — removed duplicate `.reveal` and `.card-link` (now in style.css)
- `projects.css` — `.page-hero` 60vh→44vh; `.feature-image` 16/10 ratio; masonry natural-ratio `.project-gallery` (3/2/1 columns); compact `.coming-soon`
- `index.html` — inlined CSS replaced with `style.css` link (single source of truth); hero badges + visible phone number; About photo now `images/solar-install.jpg` with `<picture>`/srcset; community quote merged into About section (dedicated section removed); certificate thumbnails clickable with lightbox dialog; featured image app-screenshot replaced with Zappi installation photo
- `projects/index.html`, `projects/solar-portlaoise.html` — featured/feature images replaced with Zappi photo via `<picture>`/srcset; gallery rebuilt with 5 unique photos + captions; og:image updated
- `solar-pv/index.html`, `areas/laois|offaly|kildare|carlow-kilkenny/index.html` — featured project image replaced with Zappi photo (picture/srcset)
- all 27 HTML pages — skip link, `<main id="main-content" tabindex="-1">`, JS-enabled class for reveal animations, `.nav-call` desktop button

### Added Files
- `images/hero-solar-800.jpg`, `images/hero-solar-1600.jpg`
- Responsive variants (`-400`/`-800`/`-1200` JPG + WebP) for `projects/Solar/*` photos, `images/solar-install`, `images/inspection-cert-1`, `images/inspection-cert-2`, `images/seai-cert`

### Removed Files
- `screenshot-hero.png` (unused), `images/team-photo.jpg` (unused football photo)

### Notes
- Root cause of "stretched" photos: HTML `height` attributes acted as CSS height hints because `.about-image img` set `width:100%` without `height:auto` (photo rendered 552×1920 from a 1440×1920 source)
- Homepage: 7,475px → 5,455px desktop; 11,651px → 8,686px mobile (10.3 screens)
- Lighthouse 100/100/100/100 (accessibility / best practices / SEO / agentic browsing) verified on homepage + solar project page
- `.playwright-mcp` review artifacts removed from the repo

## Code Changes (2026-09-12 11:53:28)

### Added Files
- index.html
- projects\index.html
- projects\solar-portlaoise.html
- projects.css
- script.js
- sitemap.xml
- style.css
- style.min.css


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
