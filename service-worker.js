const CACHE_VERSION = "calchive-pwa-v6";
const ROUTE_CACHE = `${CACHE_VERSION}-routes`;
const ASSET_CACHE = `${CACHE_VERSION}-assets`;

const OFFLINE_ROUTES = [
  "/",
  "/bmi-calculator",
  "/mortgage-calculator",
  "/gpa-calculator",
  "/age-calculator",
  "/scientific-calculator",
  "/calorie-calculator",
  "/loan-calculator",
  "/tip-calculator",
  "/percentage-calculator",
  "/compound-interest-calculator"
];

const CORE_ASSETS = [
  "/",
  "/manifest.json",
  "/favicon.ico",
  "/logo-192.png",
  "/logo-512.png",
  "/apple-touch-icon.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    Promise.all([
      caches.open(ROUTE_CACHE).then((cache) => cache.addAll(OFFLINE_ROUTES)),
      caches.open(ASSET_CACHE).then((cache) => cache.addAll(CORE_ASSETS))
    ]).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(
          keys
            .filter((key) => key.startsWith("calchive-pwa-") && !key.startsWith(CACHE_VERSION))
            .map((key) => caches.delete(key))
        )
      )
      .then(() => self.clients.claim())
  );
});

async function cacheRoute(request) {
  const cache = await caches.open(ROUTE_CACHE);
  try {
    const response = await fetch(request);
    if (response && response.ok) {
      cache.put(request, response.clone());
    }
    return response;
  } catch (error) {
    return (await cache.match(request)) || cache.match("/");
  }
}

async function cacheAsset(request) {
  const cache = await caches.open(ASSET_CACHE);
  const url = new URL(request.url);
  const isScript = url.pathname.endsWith(".js");
  const isStyle = url.pathname.endsWith(".css");

  try {
    const response = await fetch(request);
    const contentType = response.headers.get("content-type") || "";
    const isHtmlFallback = contentType.includes("text/html");

    if (
      isHtmlFallback ||
      (isScript && !/javascript|ecmascript/i.test(contentType)) ||
      (isStyle && !/text\/css/i.test(contentType))
    ) {
      return response;
    }

    if (response && response.ok && !isScript && !isStyle) {
      cache.put(request, response.clone());
    }
    return response;
  } catch (error) {
    if (isScript || isStyle) {
      throw error;
    }
    return (await cache.match(request)) || Response.error();
  }
}

self.addEventListener("fetch", (event) => {
  const { request } = event;
  if (request.method !== "GET") return;

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  if (request.mode === "navigate") {
    event.respondWith(cacheRoute(request));
    return;
  }

  if (
    url.pathname.startsWith("/assets/") ||
    url.pathname.endsWith(".png") ||
    url.pathname.endsWith(".webp") ||
    url.pathname.endsWith(".svg") ||
    url.pathname.endsWith(".ico") ||
    url.pathname.endsWith(".css") ||
    url.pathname.endsWith(".js")
  ) {
    event.respondWith(cacheAsset(request));
  }
});
