## 2024-05-30 - XSS via contenteditable
**Vulnerability:** contenteditable elements allow rich text (HTML) pasting, leading to Cross-Site Scripting (XSS).
**Learning:** Browsers preserve HTML formatting when pasting into contenteditable by default, bypassing standard sanitization if not explicitly handled.
**Prevention:** Intercept the 'paste' event on contenteditable elements, call e.preventDefault(), and manually extract and insert only 'text/plain' data.