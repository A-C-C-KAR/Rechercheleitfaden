## 2024-05-18 - Prevent XSS in contenteditable elements
**Vulnerability:** Cross-Site Scripting (XSS) via rich text paste into `contenteditable="true"` elements.
**Learning:** By default, browsers allow pasting raw HTML into `contenteditable` fields, leading to script injection or layout breaking. This project relies entirely on `contenteditable` for user inputs.
**Prevention:** Intercept the `paste` event on all `contenteditable` elements, extract `text/plain` using `e.clipboardData`, call `e.preventDefault()`, and safely insert it using `document.execCommand('insertText', false, text)`.
