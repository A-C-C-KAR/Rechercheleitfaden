## 2026-07-18 - XSS via contenteditable paste
**Vulnerability:** XSS injection possible by pasting rich HTML containing malicious scripts/payloads into `contenteditable` elements.
**Learning:** `contenteditable` elements by default accept rich HTML input from the clipboard, bypassing standard input sanitization if not explicitly handled.
**Prevention:** Intercept the `paste` event globally on `contenteditable` elements, prevent the default action, extract only `text/plain` from the clipboard, and insert it as raw text using `document.execCommand('insertText')`.
