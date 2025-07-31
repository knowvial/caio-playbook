# CAIO Playbook - AI Transformation Guide

A comprehensive blog series documenting strategies and best practices for Chief AI Officers leading AI transformation in 100-500 person organizations.

## Overview

This GitHub Pages blog provides practical, actionable guidance for AI governance, strategy, implementation, and organizational change management specifically tailored for mid-sized organizations.

## Local Development

To run this blog locally:

```bash
# Install Jekyll (requires Ruby)
gem install bundler jekyll

# Install dependencies
bundle install

# Run the development server
bundle exec jekyll serve

# View the site at http://localhost:4000/caio-play-book/
```

## Deployment to GitHub Pages

1. Create a new repository on GitHub named `[your-username].github.io/caio-play-book` or any name you prefer
2. Push this code to your repository:

```bash
git init
git add .
git commit -m "Initial commit - CAIO Playbook blog"
git branch -M main
git remote add origin https://github.com/[your-username]/caio-play-book.git
git push -u origin main
```

3. In your GitHub repository settings:
   - Go to Settings > Pages
   - Under "Source", select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Click "Save"

4. Update `_config.yml`:
   - Change `baseurl` to match your repository name (e.g., `/caio-play-book`)
   - Change `url` to `https://[your-username].github.io`
   - Update author information and email

5. Your blog will be available at `https://[your-username].github.io/caio-play-book/`

## Content Structure

- `_posts/`: Blog posts in Markdown format (YYYY-MM-DD-title.md)
- `_layouts/`: Page templates
- `assets/css/`: Custom styling
- `index.md`: Homepage
- `about.md`: About page
- `archive.md`: Blog archive

## Adding New Posts

Create a new file in `_posts/` with the format `YYYY-MM-DD-post-title.md`:

```markdown
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD
categories: [category1, category2]
tags: [tag1, tag2, tag3]
excerpt: "Brief description of the post"
---

Your content here...
```

## Customization

- Edit `_config.yml` for site-wide settings
- Modify `assets/css/style.scss` for custom styling
- Update `index.md` for homepage content
- Edit `about.md` to personalize the about section

## Topics Covered

1. **AI Strategy & Governance** (First post available)
2. People & Culture (Coming soon)
3. Technology & Implementation (Coming soon)
4. Metrics & ROI (Coming soon)
5. Industry-specific insights (Coming soon)

## License

This content is provided as a reference implementation. Feel free to adapt for your organization's needs.

## Contributing

Contributions, corrections, and suggestions are welcome! Please open an issue or submit a pull request.