## 2024-05-24 - [HIGH] contenteditable DOM-based XSS Risk
**Vulnerability:** Elements with `contenteditable="true"` naturally accept rich-text pasting, including arbitrary HTML. This opens up the application to self-XSS or DOM-based XSS if users copy-paste malicious payloads, as the browser will render the pasted HTML.
**Learning:** Even simple static HTML apps are vulnerable if they allow unsanitized input via `contenteditable`. The `contenteditable` attribute is dangerous out-of-the-box because it trusts clipboard content implicitly.
**Prevention:** Intercept the `paste` event on `contenteditable` elements, call `e.preventDefault()`, extract only the `text/plain` representation from the clipboard, and insert it manually (e.g., using `document.execCommand('insertText', false, text)`).
