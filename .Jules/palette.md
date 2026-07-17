## 2024-05-18 - html2pdf.js Main Thread Blocking
**Learning:** The html2pdf.js library blocks the browser's main UI thread during PDF generation, which prevents any synchronous UI updates (like loading text) from rendering before the operation starts.
**Action:** Always wrap the html2pdf generation call in a `setTimeout()` to yield control back to the browser. This allows loading spinners and disabled states to be painted before the thread is blocked.
