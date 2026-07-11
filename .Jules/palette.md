## 2025-03-09 - Accessible ContentEditable Fields
**Learning:** `contenteditable` elements are opaque to screen readers by default. They don't announce their editability or purpose without explicit ARIA roles.
**Action:** Always add `role="textbox"` and an appropriate `aria-label` (often derived from a placeholder data attribute) when creating custom editable fields using `contenteditable`.