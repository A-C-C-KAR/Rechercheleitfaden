## 2024-07-11 - Prevent XSS in contenteditable via Plain Text Paste
**Vulnerability:** XSS injection via pasting rich HTML content into `contenteditable` elements.
**Learning:** Default paste behavior in `contenteditable` allows arbitrary HTML, which can be executed if not sanitized. Using deprecated `document.execCommand` is bad practice.
**Prevention:** Use event delegation on `document` to listen for `paste` events. If the target is `isContentEditable`, `e.preventDefault()`, extract plain text from clipboard, create a text node (`document.createTextNode`), and insert it into the DOM using `window.getSelection().getRangeAt(0).insertNode()`.
