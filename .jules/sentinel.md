## 2026-07-12 - contenteditable XSS Vulnerability
**Vulnerability:** XSS vulnerability via copy-pasting rich text into `contenteditable=true` fields.
**Learning:** `contenteditable` elements by default accept rich text (HTML), making them vulnerable to DOM-based XSS when users paste content from the clipboard. This app relies heavily on `contenteditable` for user input instead of standard inputs.
**Prevention:** Always intercept the `paste` event on `contenteditable` elements, prevent the default behavior, extract only `text/plain` from the clipboard data, and manually insert it as text to prevent HTML/Script injection.
