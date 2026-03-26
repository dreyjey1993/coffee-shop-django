// Dark Mode Toggle
function initTheme() {
  const saved = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
  updateThemeButton(saved);
}
function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'light';
  const next = current === 'light' ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
  updateThemeButton(next);
}
function updateThemeButton(theme) {
  const btn = document.getElementById('themeToggle');
  if (btn) {
    btn.innerHTML = theme === 'dark'
      ? '<i class="bi bi-sun-fill"></i>'
      : '<i class="bi bi-moon-fill"></i>';
  }
}

// Scroll Reveal
function initReveal() {
  const els = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, { threshold: 0.15 });
  els.forEach(el => observer.observe(el));
}

// Lightbox
function initLightbox() {
  const galleryItems = document.querySelectorAll('.gallery-item');
  const lightbox = document.getElementById('lightbox');
  if (!lightbox) return;
  const img = lightbox.querySelector('img');
  const closeBtn = lightbox.querySelector('.lightbox-close');
  galleryItems.forEach(item => {
    item.addEventListener('click', () => {
      const src = item.getAttribute('data-full') || item.querySelector('img').src;
      img.src = src;
      lightbox.classList.add('active');
    });
  });
  closeBtn.addEventListener('click', () => lightbox.classList.remove('active'));
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) lightbox.classList.remove('active');
  });
}

// WhatsApp Bestell-Button (generische Funktion)
function setupWhatsAppButton(messagePrefix = 'Hallo, ich möchte') {
  const btn = document.getElementById('whatsapp-order');
  if (btn) {
    const productName = btn.getAttribute('data-product');
    const price = btn.getAttribute('data-price');
    const message = `${messagePrefix} ${productName || '...'} (Preis: ${price || ''}€) bestellen.`;
    btn.href = `https://wa.me/49123456789?text=${encodeURIComponent(message)}`;
  }
}

// Lazy Loading
function initLazy() {
  const lazyImages = document.querySelectorAll('img[data-src]');
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.classList.add('loaded');
        img.removeAttribute('data-src');
        observer.unobserve(img);
      }
    });
  });
  lazyImages.forEach(img => imageObserver.observe(img));
}

// Doc ready
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initReveal();
  initLightbox();
  initLazy();
  setupWhatsAppButton();

  // Theme Toggle Button
  const themeBtn = document.getElementById('themeToggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', toggleTheme);
  }
});
