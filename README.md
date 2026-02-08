# Social Bio Website

A modern, responsive social bio website perfect for creators, developers, and professionals. Features a clean design with profile information, social media links, and quick action buttons.

## Features

- ✨ Modern gradient design with dark theme
- 📱 Fully responsive (mobile, tablet, desktop)
- 🎨 Smooth animations and transitions
- 🔗 Easy-to-customize social media links
- 📦 No dependencies (pure HTML/CSS/JavaScript)
- ⚡ Fast loading and performance optimized
- 🎯 SEO-friendly structure

## Quick Start

1. **Clone or download** this repository
2. **Edit `index.html`** to customize:
   - Your name and title
   - Bio/description
   - Profile picture URL
   - Social media links (Twitter, Instagram, LinkedIn, GitHub, Email)
   - Portfolio/Blog/Resume links
3. **Open `index.html`** in your browser to view

## Customization Guide

### Change Profile Picture
Replace the `src` URL in the profile picture element:
```html
<img src="YOUR_IMAGE_URL" alt="Profile Picture">
```

Use services like:
- Unsplash: `https://images.unsplash.com/...`
- Gravatar: `https://gravatar.com/avatar/...`
- Your own hosting

### Update Social Links
Edit the social links section with your actual URLs:
```html
<a href="https://twitter.com/yourhandle" target="_blank">
```

### Add More Link Cards
Duplicate a link-card and modify:
```html
<a href="YOUR_URL" class="link-card">
    <i class="fas fa-icon-name"></i>
    <div>
        <h3>Label</h3>
        <p>Description</p>
    </div>
</a>
```

### Change Colors
Edit the CSS variables in `styles.css`:
```css
:root {
    --primary-color: #6366f1;      /* Main brand color */
    --secondary-color: #8b5cf6;    /* Gradient secondary */
    --accent-color: #ec4899;       /* Highlight color */
}
```

## Icons

Icons are provided by [Font Awesome 6](https://fontawesome.com/icons). Browse available icons and replace the class names like `fa-twitter`, `fa-briefcase`, etc.

## Deployment

### Free Options:
- **Vercel**: Drag and drop files at vercel.com
- **Netlify**: Drag and drop files at netlify.com
- **GitHub Pages**: Push to repo, enable Pages in settings
- **Cloudflare Pages**: Connect your GitHub repo

### With a Domain:
Add your custom domain in the deployment platform's settings.

## File Structure

```
website/
├── index.html          # Main page
├── styles.css          # Styling
└── README.md           # This file
```

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## License

Free to use and modify.

## Tips

- Keep bio text concise (2-3 sentences)
- Use a clear, professional profile picture
- Include relevant social media links
- Add actual URLs instead of placeholders
- Test on mobile devices before deploying
