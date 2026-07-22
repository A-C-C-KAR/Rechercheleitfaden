## 2024-05-24 - html2pdf.js Main Thread Blocking
**Learning:** The `html2pdf.js` library blocks the browser's main UI thread during PDF generation. This prevents UI updates (like loading spinners or text changes) from rendering if they are triggered immediately before the generation call.
**Action:** Always wrap the `html2pdf` generation call in a `setTimeout(..., 50)` to yield the main thread back to the browser, allowing the loading state UI (spinners, disabled buttons) to render before the blocking operation begins.
