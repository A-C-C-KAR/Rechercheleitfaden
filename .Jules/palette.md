## 2024-05-18 - [Yielding Main Thread for UI Updates]
**Learning:** Heavy blocking operations like HTML to PDF generation (e.g. html2pdf.js) block the main UI thread. If you add a loading state right before calling it, the browser doesn't have a chance to paint the update.
**Action:** Use `setTimeout(..., 50)` to wrap the blocking call, which yields the main thread allowing the loading UI to render before the heavy work begins.
