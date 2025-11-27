console.log("SW: Instalando…");

const CACHE = "v1";
const FILES_TO_CACHE = [
    "/",
    "/static/manifest.json",

    // Si usas imágenes, debes incluirlas aquí también
    "/static/img/umbra nexus.webp", 
    "/static/img/fondo4.webp",
    "/static/img/fondo3.webp",
    "/static/img/fondo2.webp",

    // Recursos externos (CORS Problem)
    "https://cdn.tailwindcss.com",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css",
];

self.addEventListener("install", (event) => {
    console.log("SW: Cacheando archivos...");
    
    event.waitUntil(
        caches.open(CACHE).then(cache => {
            
            // 1. Cachear los recursos internos (que no deberían dar problemas de CORS)
            const internalFiles = FILES_TO_CACHE.filter(url => !url.startsWith('http'));
            
            const internalCachePromise = cache.addAll(internalFiles)
                .catch(err => console.error("[SW] Error al cachear archivos internos:", err));
                
            // 2. Cachear los recursos externos (CDNs) uno por uno usando fetch y no-cors
            const externalFiles = FILES_TO_CACHE.filter(url => url.startsWith('http'));
            
            const externalCachePromises = externalFiles.map(url => {
                return fetch(url, { mode: 'no-cors' })
                    .then(response => {
                        // Una respuesta opaca (no-cors) no permite ver el status,
                        // pero se puede guardar en caché.
                        if (response && response.ok || response.type === 'opaque') {
                            return cache.put(url, response);
                        }
                        // Si falla, loguear y no lanzar error
                        console.warn(`[SW] Fallo en fetch (opaco) para: ${url}`);
                        return Promise.resolve(); // Resuelve para no romper Promise.all
                    })
                    .catch(error => {
                        console.warn(`[SW] Error al obtener la CDN: ${url}`, error.message);
                        return Promise.resolve();
                    });
            });
            
            // Esperar a que todos los procesos terminen
            return Promise.all([internalCachePromise, ...externalCachePromises]);
            
        }).catch((err) => console.error("[SW] Error general en instalación (afuera):", err))
    );
    
    self.skipWaiting(); 
});


self.addEventListener("activate", (event) => {
    console.log("SW: Activado");
    return self.clients.claim(); // Toma control de la página inmediatamente
});


self.addEventListener("fetch", (event) => {
    event.respondWith(
        fetch(event.request).catch(() => {
            return caches.match(event.request);
        })
    );
});