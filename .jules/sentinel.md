## 2026-07-22 - Prevent XSS in contenteditable elements via paste intercept
**Vulnerability:** Cross-Site Scripting (XSS) risk in `contenteditable` fields via rich HTML pasting.
**Learning:** `contenteditable` fields inherently accept and render rich HTML pasted from the clipboard, which can include malicious scripts.
**Prevention:** Intercept the `paste` event on `contenteditable` elements, prevent the default behavior, extract only the `text/plain` content from the clipboard data, and use `document.execCommand('insertText', false, text)` to safely insert the plain text.
