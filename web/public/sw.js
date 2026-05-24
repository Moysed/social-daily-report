// Social Daily Report — minimal service worker.
// Strategy:
//   - HTML/document: network-first with cache fallback (latest reports preferred).
//   - Same-origin static (.css, .js, .svg, .ico, .xml, .webmanifest, /icon*):
//     cache-first with background revalidation.
//   - Cross-origin (Google Fonts, Vercel Insights, etc.): network, opportunistic cache.
// Versioning: bump CACHE_VERSION when you change cache strategy or want to flush.

const CACHE_VERSION = "sdr-v1";
const STATIC_CACHE = `${CACHE_VERSION}-static`;
const PAGE_CACHE = `${CACHE_VERSION}-pages`;

const PRECACHE_URLS = ["/", "/manifest.webmanifest", "/icon.svg"];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(STATIC_CACHE).then((c) => c.addAll(PRECACHE_URLS)).then(() => self.skipWaiting()),
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys.filter((k) => !k.startsWith(CACHE_VERSION)).map((k) => caches.delete(k)),
      ),
    ).then(() => self.clients.claim()),
  );
});

function isStaticAsset(url) {
  return /\.(?:css|js|svg|png|jpg|jpeg|webp|ico|woff2?|webmanifest|xml)$/i.test(url.pathname);
}

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);

  // Cross-origin: pass through; opportunistically cache fonts in the static bucket.
  if (url.origin !== self.location.origin) {
    if (/fonts\.gstatic\.com|fonts\.googleapis\.com/.test(url.host)) {
      event.respondWith(staleWhileRevalidate(req, STATIC_CACHE));
    }
    return;
  }

  // HTML navigations / document requests: network-first.
  if (req.mode === "navigate" || req.destination === "document") {
    event.respondWith(networkFirst(req, PAGE_CACHE));
    return;
  }

  // Same-origin static: cache-first w/ revalidation.
  if (isStaticAsset(url)) {
    event.respondWith(staleWhileRevalidate(req, STATIC_CACHE));
    return;
  }

  // Default: try network, fall back to cache.
  event.respondWith(networkFirst(req, PAGE_CACHE));
});

async function networkFirst(req, cacheName) {
  const cache = await caches.open(cacheName);
  try {
    const fresh = await fetch(req);
    if (fresh && fresh.ok) cache.put(req, fresh.clone());
    return fresh;
  } catch (_err) {
    const cached = await cache.match(req);
    if (cached) return cached;
    // For navigations, fall back to the cached home page so the shell still loads.
    if (req.mode === "navigate") {
      const home = await cache.match("/") || await caches.match("/");
      if (home) return home;
    }
    return new Response("Offline", { status: 503, statusText: "Offline" });
  }
}

async function staleWhileRevalidate(req, cacheName) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(req);
  const fetchPromise = fetch(req)
    .then((resp) => {
      if (resp && resp.ok) cache.put(req, resp.clone());
      return resp;
    })
    .catch(() => cached);
  return cached || fetchPromise;
}

// Web Push hook — wired but inert until a backend pushes events.
// To enable: provide a VAPID-signed push from your push server and the browser
// will deliver `push` events here. We render a Notification using the payload.
self.addEventListener("push", (event) => {
  let data = {};
  try { data = event.data ? event.data.json() : {}; } catch (_) {}
  const title = data.title || "Social Daily Report";
  const body = data.body || "New report available.";
  const url = data.url || "/";
  event.waitUntil(
    self.registration.showNotification(title, {
      body,
      icon: "/icon.svg",
      badge: "/icon.svg",
      tag: data.tag || "sdr-update",
      data: { url },
    }),
  );
});

self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  const target = (event.notification.data && event.notification.data.url) || "/";
  event.waitUntil(
    self.clients.matchAll({ type: "window" }).then((wins) => {
      for (const w of wins) {
        if (w.url.includes(target) && "focus" in w) return w.focus();
      }
      if (self.clients.openWindow) return self.clients.openWindow(target);
    }),
  );
});
