<!-- Paste this block into byteplus-genius/SKILL.md, e.g. under a
     "## Staying current / missing details" section. -->

## Resolving missing details (do this before asking the user)

The bundled reference files are refreshed automatically from BytePlus docs, but they
may lag the newest page or omit a niche parameter. When a needed detail (a parameter,
limit, endpoint, price, model name, error code) is NOT present in the references:

1. Open `sources.json` (bundled with this skill). It maps every tracked BytePlus doc
   page to its canonical URL. Find the entry whose `product`/`title` best matches the
   topic in question.
2. Fetch that URL live and read the current content before answering.
3. Only if the live fetch fails or no relevant entry exists, tell the user what you
   could not confirm and ask them to paste the specific page.

Never fabricate a parameter or limit to fill a gap. Prefer "let me check the live doc"
over guessing, and prefer checking `sources.json` over asking the user to copy-paste.
