## 2024-07-19 - Add loading state to synchronous PDF generation
**Learning:** `html2pdf.js` operates synchronously and blocks the main UI thread during PDF generation. This prevents DOM updates (like showing a loading spinner) from rendering before the freeze.
**Action:** Always wrap heavy synchronous operations (like PDF generation) in a `setTimeout(..., 100)` to yield to the main thread and allow loading states to paint before the browser is blocked.
