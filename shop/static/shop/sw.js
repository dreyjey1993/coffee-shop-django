const CACHE_NAME = 'coffee-shop-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/menu/',
  '/about/',
  '/events/',
  '/gallery/',
  '/blog/',
  '/kontakt/',
  '/reservation/',
  '/sitemap.xml',
  '/static/shop/css/custom.css',
  '/static/shop/js/main.js',
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js',
  'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css',
  'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap'
];

// Install
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS_TO_CACHE))
  );
  self.skipWaiting();
});

// Activate
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) return caches.delete(key);
        })
      )
    )
  );
  self.clients.claim();
});

// Fetch
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) return cachedResponse;
      return fetch(event.request).then((response) => {
        return caches.open(CACHE_NAME).then((cache) => {
          if (response.status === 200) {
            cache.put(event.request, response.clone());
          }
          return response;
        });
      });
    }).catch(() => caches.match('/') || fetch('/'))
  );
});