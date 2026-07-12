## 2026-07-12 - Missing Subresource Integrity (SRI) on External Libraries
**Vulnerability:** External CDNs (Tailwind CSS and html2pdf.js) are loaded without Subresource Integrity (SRI) checks. If the CDN is compromised, malicious scripts could be injected into the application.
**Learning:** Even simple static HTML apps rely on third-party scripts. Without SRI, the app implicitly trusts the CDN to serve the exact expected file. Tailwind CSS via CDN is used here.
**Prevention:** Always include `integrity` and `crossorigin="anonymous"` attributes for `<script>` and `<link>` tags loading external resources.
