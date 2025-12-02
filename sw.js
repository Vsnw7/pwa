console.log("SW: Cargando…");

// CACHE PRINCIPAL
const STATIC_CACHE = "static-v1";
const DYNAMIC_CACHE = "dynamic-v1";

const STATIC_FILES = [
    "/",               // Inicio
    "/static/manifest.json",

    // Imágenes base
    "/static/img/umbra nexus.webp",
    "/static/img/fondo4.webp",
    "/static/img/fondo3.webp",
    "/static/img/fondo2.webp"
];

// INSTALACIÓN – solo cache estático inicial
self.addEventListener("install", (event) => {
    console.log("SW: Instalando…");

    event.waitUntil(
        caches.open(STATIC_CACHE).then(cache => {
            console.log("SW: Cacheando estáticos iniciales");
            return cache.addAll(STATIC_FILES);
        })
    );

    self.skipWaiting();
});

// ACTIVACIÓN – limpia cachés viejos
self.addEventListener("activate", (event) => {
    console.log("SW: Activado");

    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.map(key => {
                    if (key !== STATIC_CACHE && key !== DYNAMIC_CACHE) {
                        console.log("SW: Borrando cache viejo:", key);
                        return caches.delete(key);
                    }
                })
            );
        })
    );

    self.clients.claim();
});

// FETCH – estrategia incremental
self.addEventListener("fetch", (event) => {
    event.respondWith(
        caches.match(event.request)
            .then(cachedResponse => {
                if (cachedResponse) {
                    // Existe en cache → úsalo
                    return cachedResponse;
                }

                // No está en cache → tratar de obtenerlo
                return fetch(event.request)
                    .then(networkResponse => {
                        // Solo insertar en cache dinámico si es una ruta válida
                        if (
                            event.request.method === "GET" &&
                            event.request.url.startsWith(self.location.origin)
                        ) {
                            return caches.open(DYNAMIC_CACHE).then(cache => {
                                cache.put(event.request, networkResponse.clone());
                                return networkResponse;
                            });
                        }

                        return networkResponse;
                    })
                    .catch(() => {
                        // Si falla el fetch y tampoco está en cache, retornar nada
                        // (puedes poner aquí un fallback si quieres)
                        return caches.match("/");
                    });
            })
    );
});
