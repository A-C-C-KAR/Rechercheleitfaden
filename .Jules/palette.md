## 2024-05-24 - Contenteditable Screen Reader Accessibility
**Learning:** Native `contenteditable` elements often lack context for screen readers. Using them without explicit ARIA roles and labels leads to poor accessibility.
**Action:** Always dynamically or statically apply `role="textbox"` and `aria-label` (using a placeholder or title) to `contenteditable` fields to ensure screen readers announce them properly.
