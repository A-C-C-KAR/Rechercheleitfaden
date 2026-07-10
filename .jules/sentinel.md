## 2026-07-10 - [Subresource Integrity (SRI)]
**Vulnerability:** CDN scripts loaded without integrity checks
**Learning:** External scripts loaded from CDNs without SRI checks are vulnerable to supply chain attacks. If the CDN is compromised, malicious code can be executed on the client side.
**Prevention:** Always use Subresource Integrity (SRI) attributes ('integrity' and 'crossorigin') when loading external resources from a CDN.
