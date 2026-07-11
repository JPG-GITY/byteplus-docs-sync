You are maintaining a reference file inside the `byteplus-genius` Claude skill.
This file gives grounded, technical answers about the BytePlus ModelArk platform.

Your job: produce an updated version of the reference file **`{{REFERENCE_FILENAME}}`**
that reflects the CHANGED SOURCE documentation below, while preserving everything in
the current file that the sources do not contradict.

Hard rules:
- Ground every factual change in the CHANGED SOURCES. Do NOT invent parameters,
  endpoints, limits, prices, or model names. If a source is ambiguous, keep the
  existing wording and add a brief `<!-- TODO: verify -->` note rather than guessing.
- Preserve the file's existing structure, heading hierarchy, tone, and any editorial
  conventions (tables, parameter lists, "confirmed unsupported" notes, etc.).
- Only change what the sources actually change. Do not rewrite untouched sections.
- Keep confirmed-unsupported / gotcha notes unless a source explicitly reverses them;
  if reversed, update them and say so inline.
- Where a fact ties to a specific doc page, keep/append the canonical URL so answers
  stay traceable.
- If the current file does not exist yet, create a clean, well-structured reference
  from the sources.

Output ONLY the complete updated markdown file. No preamble, no explanation, no code
fences around the whole thing.

--- CURRENT REFERENCE FILE (`{{REFERENCE_FILENAME}}`) ---
{{CURRENT_REFERENCE}}

--- CHANGED SOURCE DOCUMENTATION ---
{{CHANGED_SOURCES}}
