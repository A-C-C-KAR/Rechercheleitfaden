## 2026-07-23 - Prevent XSS in contenteditable via paste interception
**Vulnerability:** XSS vulnerability through rich HTML paste in `contenteditable` elements. Users could copy and paste malicious HTML payloads which the browser would render and execute.
**Learning:** `contenteditable` fields natively support rich HTML insertion from the clipboard by default. This project heavily relies on them instead of standard input fields.
**Prevention:** Intercept the `paste` event on `contenteditable` elements, call `e.preventDefault()`, extract `text/plain` from the `clipboardData`, and insert it as raw text using `document.execCommand('insertText', false, text)`.
