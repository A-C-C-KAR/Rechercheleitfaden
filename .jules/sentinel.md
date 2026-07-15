## 2024-07-16 - Prevent XSS in contenteditable fields
**Vulnerability:** XSS vulnerability through pasting rich HTML into `contenteditable` elements.
**Learning:** The application heavily relies on `contenteditable` elements instead of standard input fields. When users paste content into these fields, the browser might paste rich HTML, which could contain malicious scripts.
**Prevention:** Intercept the `paste` event on `contenteditable` elements, prevent the default action, and extract only the `text/plain` content from the clipboard to insert as plain text.