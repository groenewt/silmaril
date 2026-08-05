// Minimal JS for Silmaril pages
// Currently handles scroll-based nav highlighting and simple interactions

document.addEventListener('DOMContentLoaded', () => {
    // Smooth scroll for nav links
    const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            if (href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });

    // Intersection Observer for section highlighting
    const sections = document.querySelectorAll('section[id]');
    const navLinkMap = new Map();
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href.startsWith('#')) {
            navLinkMap.set(href.slice(1), link);
        }
    });

    const observerOptions = {
        rootMargin: '-50% 0px -50% 0px',
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinkMap.forEach((link, linkId) => {
                    link.style.color = linkId === id ? 'var(--color-accent-dark)' : '';
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => observer.observe(section));
});
