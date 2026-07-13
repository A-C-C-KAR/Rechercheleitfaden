## 2026-07-13 - [HIGH] Fix XSS vulnerability in contenteditable fields
**Vulnerability:** Cross-Site Scripting (XSS) via rich text paste in `contenteditable` elements.
**Learning:** This project heavily relies on `contenteditable` elements for user input instead of standard `<input>` or `<textarea>` tags. By default, browsers allow pasting rich text (HTML) into `contenteditable` fields, which bypasses plain-text input assumptions and allows arbitrary HTML/JS execution if the user copies malicious content.
**Prevention:** Intercept the `paste` event globally on `contenteditable` fields, call `e.preventDefault()`, extract `text/plain` from the clipboard data, and manually insert it using `document.execCommand('insertText', false, text)`. This strips any HTML tags from the pasted content.
