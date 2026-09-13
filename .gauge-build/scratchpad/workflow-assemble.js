export const meta = {
  name: 'gauge-theory-assemble',
  description: 'Assemble one Gauge Theory chapter (exercise indices, topic page, legal-operation numbering, mechanical audits) and, when asked, the series map',
  phases: [ { title: 'Assemble', detail: 'exercise indices + topic page for one chapter, or the series map' } ],
}

const S = '/tmp/claude-0/-home-user-Study-notes/a00e52f1-c9a2-537c-a39b-06f8e3c8a9c6/scratchpad'
const VAULT = '/home/user/Study-notes/Study notes/Geometry/Gauge Theory'
const ROMAN = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII']

const ch = args.chapter          // {chapnum,title,manifestFile}
const subResults = args.subResults || []   // [{page:{name}, write:{imports}, review:{verdict}}]
const seriesMap = args.seriesMap || null   // when set: [{ch:{title}, assemble:{written,imports}}] -> write the series map instead

const ASSEMBLE_SCHEMA = {
  type: 'object',
  properties: {
    written: { type: 'array', items: { type: 'string' } },
    imports: { type: 'array', items: { type: 'string' } },
    issues: { type: 'array', items: { type: 'string' } },
  },
  required: ['written', 'imports', 'issues'],
}
function folder(ch) { return `${VAULT}/Gauge Theory ${ROMAN[ch]}` }
function assemblePrompt(ch, subResults) {
  const names = subResults.map(r => r.page.name)
  const imports = subResults.flatMap(r => (r.write && r.write.imports) || [])
  const ok = subResults.filter(r => r.review && r.review.verdict !== 'incomplete').length
  return `You are assembling chapter "${ch.title}" of an Obsidian study-notes vault: writing its Exercise Index pages and its topic page, after every subpage has been written and reviewed. Folder: "${folder(ch.chapnum)}/"; topic page: "${VAULT}/${ch.title}.md".

Read first: ${S}/writer-brief.md (§5 exercise index + topic page templates, §0 non-negotiables), ${S}/conventions.md, /home/user/Study-notes/.claude/skills/polymath-notes/references/prose-and-proof-standard.md Part I (register), /home/user/Study-notes/.claude/skills/polymath-notes/references/templates.md ("Topic Page Template" and "Exercise Index Page Template"), and the chapter's block in ${S}/${ch.manifestFile} (sections, page list, existing vault pages to link). Then read EVERY subpage in the folder (${names.length} pages: ${names.join(' | ')}) — the concept-map statements must match the subpages' actual Statement / The Definition sections, and the Legal Operations, Sources and Targets, Problem-Solving Strategy, Most Reusable Properties, Bridges and Insights are derived from what the subpages actually prove and drill. Also read the topic page of one gold-standard chapter for calibration: "/home/user/Study-notes/Study notes/Algebra/Rings/Rings II — Euclidean Domains, PIDs, and UFDs.md" if it exists, else any "Group Theory I — " page under "Study notes/Algebra/Group Theory/".

Write:
1. One \`Exercise Index - §N.K <Section Title>.md\` per section (title byte-identical to the manifest's section title and to the concept-map header), each with a contextualising preamble paragraph and one bullet per exercise of that section: \`- [[Ex - Name]] (⭐⭐) — one-line technique description ([[Def - A]], [[Thm - B]])\` where the parenthesised list is exactly the Def/Thm pages that exercise's solution invokes (read the solution). At least three exercises per section; if a section has fewer written exercise pages, list what exists and record the shortfall in "issues".
2. The topic page, with every section the brief's §5 lists, in this order: Notation Registry (standing-convention preamble first; every symbol used in any subpage), Motivation (thesis register; hook; backbone display equation when the chapter has one; closing audience-assumption paragraph), Concept Map (one \`## §N.K <Section Title>\` per section; foldable bullets — parent \`- **[[Def - X]]**\` on one line, one indented single-line child bullet with a 3–5 sentence rigorous statement copied faithfully from the subpage; exercises interleaved as \`- **[[Ex - Name]]** (⭐⭐)\` with a one-line child; at least one \`> [!tip] Unlocked: Concept *(from Field)*\` callout per section unless the section genuinely unlocks nothing — forward references to pages that do not exist are bold plain text, never wikilinks; each section ends with \`> [!note] Exercise Index — §N.K\` / \`> [[Exercise Index - §N.K <Section Title>]]\`), Sources and Targets (prose), Legal Operations (numbered, 7+, each a named item plus a prose paragraph; then \`**Illegal but tempting operations:**\` with 3+ \`> [!warning] k. <name>\` callouts each giving a concrete counterexample AND the extra condition that would make it legal), Problem-Solving Strategy (prose; closes with the single unifying question of the chapter), Most Reusable Properties (4–5 full-paragraph bullets), Bridges (numbered paragraphs that explain the construction), Insights (2+ substantive paragraphs), and — ONLY if any subpage carries an "Imported without proof" callout — \`# Imported Results\` listing each (name, page, source, reason). Imports reported by the writers: ${imports.length ? imports.join(' ; ') : 'none reported'} — verify by grepping the folder for "Imported without proof".
3. After the topic page exists, open every \`Ex - \` page in the folder and make its \`# Legal Operations Used\` entries refer to the topic page's Legal Operations by the numbers you assigned ("operation 4 from the topic page"), editing in place; do not change anything else on those pages.
4. Run, from /home/user/Study-notes: \`python3 .claude/skills/polymath-notes/scripts/find-math-bugs.py\`, \`find-latex-bugs.py\`, \`find-wikilink-bugs.py\`, and \`find-unproved-theorems.py "${folder(ch.chapnum)}"\` and fix every finding located in this chapter's folder or topic page (use the matching fix-*.py scripts with --apply where they exist, then re-run). Then check that every wikilink on the pages you wrote resolves to a file in "Study notes/" (basename match) and that every \`![[X#Anchor]]\` you wrote points at an existing heading.

Review status of the subpages: ${ok}/${subResults.length} passed review. Do not rewrite subpages beyond step 3 and step 4 fixes.

Return ONLY the structured output: written (paths); imports (the entries of # Imported Results); issues (sections with fewer than three exercises, concept-map entries whose subpage is missing or inconsistent, audit findings you could not fix, anything else the orchestrator must know).`
}

function seriesMapPrompt(chapterResults) {
  const lines = chapterResults.map(c => `${c.ch.title}: ${c.assemble ? c.assemble.written.length + ' pages assembled; imports: ' + (c.assemble.imports.join('; ') || 'none') : 'ASSEMBLY FAILED'}`)
  return `Write the front-door page "${VAULT}/Gauge Theory — Series Map.md" of a thirteen-chapter Obsidian study-note series on gauge theory (folder "${VAULT}/"). Read ${S}/writer-brief.md §0 and §6, ${S}/conventions.md, /home/user/Study-notes/.claude/skills/polymath-notes/references/prose-and-proof-standard.md Part I, and every topic page "${VAULT}/Gauge Theory <N> — ….md" (thirteen files) in full.

The page has YAML frontmatter (type: topic, subject: gauge-theory, title, tags), then: (1) a Motivation in the thesis register explaining what the series is, what the two sources are (Haydys, *Introduction to Gauge Theory*, PCMI lecture notes; Christian Bär, *Gauge Theory*, Potsdam lecture notes 2011 — the file in sources/ is named mathematical_gauge_theory.pdf), and the series' governing rule that every theorem is proved in full with the handful of registered imports listed; (2) a chapter table: each chapter's wikilinked title, one-paragraph summary, its sections, and its prerequisites among the earlier chapters and the existing vault (Differential Geometry, Riemannian Geometry, Algebraic Topology, Hodge Theory, Spinors, Special Relativity); (3) four reading routes as prose paragraphs — the geometric route (I→II→III→IV→V→VI), the physics route (II→IV→VII with XXI–XXIII of Special Relativity), the analytic route (VIII→IX→X→XI), the topological route (XII→XIII with VI and VII); (4) a table "Imported results" collecting every \`# Imported Results\` entry across the thirteen topic pages (result, chapter, page, published source, reason), so a reader can see at a glance exactly what the series does not prove; (5) a short "Conventions at a glance" section restating the series conventions with wikilinks to the pages that state them. Only wikilink pages that exist in "${VAULT}" (check with ls / grep). Assembly report from the chapters:\n${lines.join('\n')}\n\nReturn ONLY the structured output: written (the path); imports (the rows of the imported-results table); issues.`
}

// ---------------------------------------------------------------- run
if (seriesMap) {
  const r = await agent(seriesMapPrompt(seriesMap), { label: 'assemble:series-map', phase: 'Assemble', schema: ASSEMBLE_SCHEMA, effort: 'medium' })
  return { seriesMap: r }
}
log(`Assembling ${ch.title} from ${subResults.length} subpages`)
const r = await agent(assemblePrompt(ch, subResults), { label: `assemble:${ROMAN[ch.chapnum]}`, phase: 'Assemble', schema: ASSEMBLE_SCHEMA, effort: 'high' })
return { chapter: ch.title, assemble: r }
