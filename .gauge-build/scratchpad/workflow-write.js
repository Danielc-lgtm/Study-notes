export const meta = {
  name: 'gauge-theory-write-unit',
  description: 'Write one unit of Gauge Theory subpages from their specs with full thesis-floor proofs, then review each page adversarially and fix it in place',
  phases: [
    { title: 'Write', detail: 'one agent per Def/Thm/Ex page, from its spec file' },
    { title: 'Review', detail: 'adversarial proof and self-containment review of every page, fixes applied in place' },
  ],
}

const S = '/tmp/claude-0/-home-user-Study-notes/a00e52f1-c9a2-537c-a39b-06f8e3c8a9c6/scratchpad'
const VAULT = '/home/user/Study-notes/Study notes/Geometry/Gauge Theory'
const ROMAN = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII']

// Two input shapes, both supported (back-compat keeps in-flight resumes cache-valid):
//   single unit:   { unit, jobs: [{pages:[...]}, ...] }
//   many units:    { units: [{unit, jobs:[...]}, ...] }
const unitsIn = args.units ? args.units : [{ unit: args.unit || 'unit', jobs: args.jobs }]
const unitName = args.units ? `${unitsIn.length} units (${unitsIn[0].unit}..${unitsIn[unitsIn.length - 1].unit})` : (args.unit || 'unit')
const jobs = unitsIn.flatMap(u => u.jobs.map(j => ({ ...j, _unit: u.unit })))

const WRITE_SCHEMA = {
  type: 'object',
  properties: {
    paths: { type: 'array', items: { type: 'string' } },
    written: { type: 'boolean' },
    missing_links: { type: 'array', items: { type: 'string' } },
    unproved_invocations: { type: 'array', items: { type: 'string' } },
    imports: { type: 'array', items: { type: 'string' } },
    flags: { type: 'array', items: { type: 'string' } },
  },
  required: ['paths', 'written', 'missing_links', 'unproved_invocations', 'imports', 'flags'],
}
const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    paths: { type: 'array', items: { type: 'string' } },
    findings: { type: 'array', items: { type: 'string' } },
    fixed: { type: 'array', items: { type: 'string' } },
    remaining: { type: 'array', items: { type: 'string' } },
    verdict: { type: 'string', enum: ['complete', 'complete-after-fixes', 'incomplete'] },
  },
  required: ['paths', 'findings', 'fixed', 'remaining', 'verdict'],
}

function folder(ch) { return `${VAULT}/Gauge Theory ${ROMAN[ch]}` }

function pageList(job) { return job.pages.map(p => `"${folder(p.chapnum)}/${p.name}.md" (type: ${p.type}; spec: ${S}/specs/${p.id}.md)`).join('; ') }
function manifestFor(p) { return `${S}/manifest-${p.chapnum <= 6 ? 1 : (p.chapnum <= 11 ? 2 : 3)}.md` }
function writePrompt(job) {
  const p = job.pages[0]
  const multi = job.pages.length > 1
  return `You are writing ${multi ? job.pages.length + ' pages' : 'ONE page'} of an Obsidian study-notes vault: ${pageList(job)}. Create the folder(s) if they do not exist.${job.note ? '\n\nSPECIAL INSTRUCTION FOR THIS JOB: ' + job.note : ''}

Read, in this order, before writing anything:
1. ${S}/writer-brief.md — the binding brief (page template for your page type, the prose register, the proof floor, Obsidian mechanics, return format).
2. ${S}/conventions.md — series conventions (signs, actions, Hodge star, the pre-approved import list).
3. /home/user/Study-notes/.claude/skills/polymath-notes/references/prose-and-proof-standard.md — Part I §1–§3 (the register) and Part II §5, §6, §8 (the rule, the eleven-point proof floor, the model proof). Read §6 and §8 in full.
4. The spec file of each page you write (paths above): what it must contain, which source items it covers, the exact statement (for a theorem), the proof obligations, the pages it may invoke.
5. The manifest block for each page's chapter (${[...new Set(job.pages.map(q => manifestFor(q) + ' — find "## Gauge Theory ' + ROMAN[q.chapnum] + ' —"'))].join('; ')}) — the exact names of every sibling page you may wikilink; and ${S}/anchors.md for the cross-chapter page names.
6. The source items your spec cites: look up each item id (e.g. D2.1.7, T2.2.4, X3.1.2, R2.6.3; ids prefixed "B-" or drawn from Bär's sections are in content-map-wernli.md, Haydys items in content-map-haydys.md — grep the id) in ${S}/content-map-haydys.md / ${S}/content-map-wernli.md, then read the cited PDF pages in the matching excerpt file under ${S}/src/ (A-… files are Haydys, B-… files are Bär; page markers "===== PDF PAGE N ====="). Read the actual source text, not only the inventory.
7. ${S}/vault-index.txt (grep it) for the exact names of existing vault pages you link to, and ${S}/unproved-pages.txt (never cite a page listed there as the proof of anything).
8. For calibration of the vault's page shape, read ONE existing gold-standard page of your type: definition → "/home/user/Study-notes/Study notes/Algebra/Group Theory/Group Theory I/Def - Normal Subgroup.md"; theorem → "/home/user/Study-notes/Study notes/Algebra/Group Theory/Group Theory I/Thm - First Isomorphism Theorem.md"; exercise → "/home/user/Study-notes/Study notes/Algebra/Rings/Rings II/Ex - In a principal ideal domain irreducibles are prime.md" (if that path does not exist, any "Ex - " page under "Study notes/Algebra/Group Theory/Group Theory I/"). Match its section structure and depth; exceed it in proof detail.

Then write the page in full. Non-negotiables (details in the brief): every theorem you state or invoke is proved — on this page if it is yours, otherwise wikilinked to a page (in the manifest or in vault-index minus unproved-pages) whose proof is complete, with the statement restated at the point of use; every proof at or above the thesis floor (named goal, labelled blocks, bold lead-ins, a justification on EVERY displayed line, every hypothesis invoked by name, all cases and directions, closing sentence); the thesis prose register everywhere else; every example on a definition page verified clause by clause; every exercise solution complete with the three-tier structure; YAML frontmatter; exact section headers from the brief (\`# Statement\` on theorem pages, \`# The Definition\` on definition pages — other pages transclude these anchors); correct Obsidian syntax (no whitespace inside \`$…$\` boundaries, no LaTeX inside \`[[ ]]\`, no HTML). The spec's cited source items must ALL be covered; where the source has a typo (see Appendix B of content-map-haydys.md / the typo appendix of content-map-wernli.md) use the corrected form and say so. Length is whatever completeness requires; a theorem page with a serious proof is typically 300–700 lines.

Use the Write tool to create ${multi ? 'each file at exactly the path listed above (all of them, in the order listed)' : 'the file at exactly "' + folder(p.chapnum) + '/' + p.name + '.md"'}. Do not create any other file. Do not modify any existing file.

Return ONLY the structured output: paths (every file you wrote); written (true only if every listed page was written in full); missing_links (wikilink targets you used that are in neither the manifest nor vault-index); unproved_invocations (results you needed whose complete proof you could not point at — with the page you would want); imports (every "Imported without proof" callout you wrote, as "<result> — <page>"); flags (every ⚠️ marker you left, and any spec item you could not cover, with reasons).`
}

function reviewPrompt(job, w) {
  const p = job.pages[0]
  const multi = job.pages.length > 1
  const paths = job.pages.map(q => `"${folder(q.chapnum)}/${q.name}.md" (type: ${q.type}; spec: ${S}/specs/${q.id}.md)`).join('; ')
  return `You are the adversarial reviewer of ${multi ? job.pages.length + ' pages' : 'ONE page'} of an Obsidian study-notes vault: ${paths}. Review ${multi ? 'every one of them, one after the other, with the same rigour' : 'it'}.${job.note ? ' SPECIAL INSTRUCTION FOR THIS JOB: ' + job.note : ''} Your job is to find every violation of the vault's Proof Standard and prose standard on this page and FIX it in place, then report honestly. Assume the page has defects until you have checked otherwise; do not be polite to the author.

Read first:
1. /home/user/Study-notes/.claude/skills/polymath-notes/references/prose-and-proof-standard.md — Part II §5, §6 (the eleven-point proof floor), §8 (model proof), §10 (self-check), and Part I §2–§3 (register).
2. ${S}/writer-brief.md (page templates, mechanics) and ${S}/conventions.md (series conventions).
3. The spec file(s) listed above — the spec each page was written from (statement, source items, proof obligations).
4. The page(s) themselves, in full.
5. ${S}/vault-index.txt and ${S}/unproved-pages.txt and the chapter manifest block(s) (${[...new Set(job.pages.map(q => manifestFor(q)))].join(', ')}), for checking link targets.
${job.pages.some(q => q.type === 'theorem') ? `6. The source proof, if the source gives one: look up the spec's source items in ${S}/content-map-haydys.md / ${S}/content-map-wernli.md and the PDF pages in ${S}/src/.` : ''}

Check, and fix:
A. **Mathematical correctness.** Verify every displayed line of every proof / derivation / solution by hand: is each equality actually true with the stated justification? Are the hypotheses sufficient? Are signs and factors right under the series conventions (${S}/conventions.md)? Do the source typos listed in the inventories' appendices survive into the page? A wrong step is the worst possible defect — fix it with a correct argument, or, if you cannot repair it, replace the step by an explicit ⚠️ marker stating exactly what is unproved.
B. **The proof floor (§6, all eleven points).** Named assumptions and goal at the top; labelled blocks; bold lead-ins; a justification on every displayed line; every hypothesis invoked by name; well-definedness / existence / equivalence-relation checks spelled out; both directions, all cases, all parts (no "similarly", "analogously", "clearly", "obviously", "it is easy to see", "one checks", "standard", "well known", "left to the reader", "omitted", "sketch"); numbered lines combined explicitly; closing sentence; typed symbols; contradictions named; interchanges of limit/sum/integral/derivative licensed by a cited theorem; regularity verified where used. Expand every gap you find into the argument.
C. **Every theorem mentioned is proved.** For every result the page invokes (grep the page for "[[Thm -", "by the … theorem", "Lemma", "Proposition", "Corollary", "it is known", "recall that"): is the invocation a wikilink to a page whose Formal Proof is complete — a series page named in the manifests, or an existing vault page NOT in unproved-pages.txt — with the statement restated at the point of use? If it points nowhere, at a "(Statement)" page, at an unproved page, or at a page that does not exist in the manifests or vault-index, fix it: prove the result on this page as a lemma if it is short, otherwise record it in "remaining" with the page that should carry it. Any "Imported without proof" callout must be for a result on the pre-approved list in conventions.md and must have all four fields.
D. **Definition pages:** every example verified clause by clause, at least one non-example with the failing clause exhibited, every corollary proved or wikilinked to its proof, per-clause failure analysis in Axiom Motivation, a Calibration check paragraph. **Exercise pages:** plan paragraph, per-step Derivation callouts, one "Complete formal solution" callout that is itself a complete proof, four labelled Convergent Strategy paragraphs, graduated hints, every invoked theorem linked to a proved page.
E. **Structure and mechanics.** Section headers exactly as the brief (\`# Statement\` right after \`# Notation\` on theorem pages; \`# The Definition\` on definition pages; the lemma callouts with all four fields and nested \`> > [!note]- Full proof\`; \`> [!note]- Complete formal proof\`); YAML frontmatter with type/subject/prereqs/tags (+difficulty on exercises); no whitespace just inside \`$\` delimiters; no dangling operator before a closing \`$\`; only core KaTeX commands; no LaTeX or markdown inside \`[[ ]]\`; no HTML; wikilink targets exist (manifest or vault-index); transclusion anchors are \`#The Definition\` / \`#Statement\`.
F. **Register.** Explanatory sections in the thesis register (orient → motivate → state → unpack in the smallest concrete case → re-explain → close in words; measured first-person-plural academic voice; every claim with its reason; standard terminology; typed symbols; no filler, no slogans, no chattiness). Rewrite sentences that fail.
G. **Spec coverage.** Every source item the spec assigns to this page is actually covered.

Make the fixes with the Edit tool (or rewrite the file with Write if the fixes are extensive). Do not create other files. Be thorough: a review that finds nothing on a 500-line proof page is almost certainly a review that did not check the lines.

Return ONLY the structured output: paths (the files reviewed); findings (every defect found, one line each, most severe first); fixed (the ones you repaired); remaining (defects you could not repair, each with what is needed — e.g. "needs page Thm - X with full proof of …"); verdict.`
}

// ---------------------------------------------------------------- run (one unit: write -> review, no barrier)
const npages = jobs.reduce((n, j) => n + j.pages.length, 0)
log(`Unit ${unitName}: writing and reviewing ${npages} pages in ${jobs.length} jobs`)
const results = await pipeline(
  jobs,
  j => agent(writePrompt(j), { label: `write:${ROMAN[j.pages[0].chapnum]}:${j.pages.map(q => q.name.slice(0, 30)).join('+')}`, phase: 'Write', schema: WRITE_SCHEMA, effort: j.pages.some(q => q.type === 'theorem') ? 'high' : 'medium' })
    .then(w => ({ job: j, write: w })),
  r => (r.write && r.write.written)
    ? agent(reviewPrompt(r.job, r.write), { label: `review:${ROMAN[r.job.pages[0].chapnum]}:${r.job.pages.map(q => q.name.slice(0, 30)).join('+')}`, phase: 'Review', schema: REVIEW_SCHEMA, effort: r.job.pages.some(q => q.type === 'theorem') ? 'high' : 'medium' })
        .then(rv => ({ ...r, review: rv }))
    : Promise.resolve({ ...r, review: null }),
)
const clean = results.filter(Boolean)
const jobReport = r => ({
  unit: r.job._unit,
  names: r.job.pages.map(q => q.name), types: r.job.pages.map(q => q.type), chapnum: r.job.pages[0].chapnum,
  written: !!(r.write && r.write.written),
  verdict: r.review ? r.review.verdict : 'not-reviewed',
  remaining: (r.review && r.review.remaining) || [],
  missing_links: (r.write && r.write.missing_links) || [],
  unproved_invocations: (r.write && r.write.unproved_invocations) || [],
  imports: (r.write && r.write.imports) || [],
  flags: ((r.write && r.write.flags) || []).slice(0, 6),
})
// per-unit rollup so a chapter-sized run is legible
const byUnit = {}
for (const u of unitsIn) byUnit[u.unit] = { unit: u.unit, written: 0, total: u.jobs.length, passed: 0, jobs: [] }
for (const r of clean) {
  const b = byUnit[r.job._unit]
  if (!b) continue
  b.jobs.push(jobReport(r))
  if (r.write && r.write.written) b.written++
  if (r.review && r.review.verdict !== 'incomplete') b.passed++
}
const report = {
  unit: unitName,
  units: Object.values(byUnit).map(b => ({ unit: b.unit, written: b.written, total: b.total, passed: b.passed })),
  jobs: clean.map(jobReport),
  lost: jobs.length - clean.length,
}
log(`${unitName}: ${clean.filter(r => r.write && r.write.written).length}/${jobs.length} jobs written; ${clean.filter(r => r.review && r.review.verdict !== 'incomplete').length} passed review`)
return report
