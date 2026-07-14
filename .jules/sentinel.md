## 2024-07-14 - Prevent XSS in contenteditable fields
**Vulnerability:** The application heavily relies on `contenteditable` elements for user input. By default, pasting into these elements can include rich HTML, which introduces a significant Cross-Site Scripting (XSS) vulnerability if a user pastes malicious HTML (e.g., `<img src=x onerror=alert(1)>`).
**Learning:** `contenteditable` elements do not behave like standard `<input>` or `<textarea>` fields; they accept and render raw HTML.
**Prevention:** Always intercept the `paste` event on `contenteditable` elements, prevent the default behavior (`e.preventDefault()`), and explicitly insert only the plain text version of the clipboard data.
