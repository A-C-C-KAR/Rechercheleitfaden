## 2026-07-21 - [UI Rendering Blocked by html2pdf.js]
**Learning:** The `html2pdf.js` library blocks the browser's main UI thread during PDF generation. This prevents loading spinners or button states from rendering before the PDF generation begins.
**Action:** When implementing UI feedback before generating a PDF, wrap the generation call (`html2pdf().set(opt).from(element).save()`) in a `setTimeout(() => { ... }, 50)` to yield to the browser and allow the loading state to render.
