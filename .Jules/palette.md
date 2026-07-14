## 2026-07-14 - Yielding UI before blocking operations
**Learning:** html2pdf.js blocks the browser's main UI thread. Attempting to update the UI (like adding a loading spinner or changing text) immediately before calling html2pdf() will fail to render because the thread gets blocked before the browser can repaint.
**Action:** Wrap the blocking operation in a setTimeout (e.g., 50ms) to yield execution back to the browser. This allows the loading UI to render before the heavy processing begins, greatly improving perceived performance and UX.
