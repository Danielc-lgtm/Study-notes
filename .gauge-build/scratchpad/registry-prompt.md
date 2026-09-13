You are designing the page-level architecture ("filename manifest and concept registry") of a new thirteen-chapter Obsidian study-note series on gauge theory. You do NOT write any study notes. You design the chapters named in the GROUP ASSIGNMENT at the end of this prompt and produce ONE file (its path is given there).

Inputs (read all of them, in full, in this order):
1. `scratchpad/architecture.md` — the chapter plan (thirteen chapters; source sections per chapter).
2. `scratchpad/conventions.md` — byte-exact chapter titles, series conventions, and the pre-approved list of results that may be imported without proof.
3. `scratchpad/backlink-map.md` — seven definition-page filenames that MUST be used verbatim (they preserve existing links from the rest of the vault) and which chapter each lives in.
4. `scratchpad/content-map-haydys.md` — exhaustive inventory of source A (Haydys), items numbered D/T/E/X/R/I by section; read the header (global conventions) and Appendix B (source typos) in full, and the sections named in your GROUP ASSIGNMENT in full.
5. `scratchpad/content-map-wernli.md` — exhaustive inventory of source B (Christian Bär's *Gauge Theory* lecture notes, Potsdam 2011; the file is misnamed "wernli" — attribute everything to Bär), items numbered the same way; read the header in full and the sections named in your GROUP ASSIGNMENT in full.
6. `scratchpad/vault-index-geometry.txt` — existing vault pages (basename TAB folder) in Geometry, Topology, Linear Algebra, Special Relativity. Pages that already exist are LINKED from the new series, never duplicated — unless the existing page is listed in `scratchpad/unproved-pages.txt` (its proof is missing or sketched), in which case the series writes its own fully proved page under a DIFFERENT name (append " (Gauge Theory)" only if no better name exists; prefer a more specific name).
7. `scratchpad/unproved-pages.txt`.
8. `/home/user/Study-notes/.claude/skills/polymath-notes/SKILL.md` sections "Page Types" and "The Proof Standard" (skim for what each page type is), and `references/prose-and-proof-standard.md` §5 (the rule: every theorem mentioned is proved; the single import exception).

The rules of the design:

A. **Total coverage.** Every D/T/E/X/R item in both inventories is assigned to exactly one destination page (a Def page, a Thm page, an Ex page, or — for a remark/example that is not worth a page — a named section of a specific page, written as `→ inside Def - X (Examples / Corollaries)` or `→ inside Thm - Y (Motivation)`). Every I item (result imported by the source without proof) is assigned either a Thm page in the series where it will be PROVED IN FULL, or a link to an existing proof-complete vault page, or — only if it is on the pre-approved import list in conventions.md — the page whose `Imported without proof` callout will carry it. Nothing is left unassigned. At the end of the manifest, list every inventory item number with its destination, as a table, so coverage can be checked mechanically.

B. **One page per concept, merged across sources.** Where A and B both define/prove the same thing (principal bundle, connection, curvature, structure equation, Bianchi identity, gauge group, associated bundle, Chern classes, holonomy, ...), there is ONE page, with both sources' items assigned to it and both sources' formulations recorded in its spec. Where the two sources' conventions differ, the spec says which convention the page uses (conventions.md decides) and that the other is recorded in a `> [!warning] Convention:` callout.

C. **Page types and naming.** `Def - <Name>.md`, `Thm - <Name>.md` (also for lemmas, propositions, corollaries — the Statement blockquote says which), `Ex - <Description>.md`, `Exercise Index - §N.K <Section Title>.md`, and the topic page `Gauge Theory N — <Title>.md` (title byte-exact from conventions.md) with its subfolder `Gauge Theory N/`. Names are descriptive, Windows-portable (no `< > : " / \ | ? *`; write "Half" not "1/2"; `S^2`, `U(1)`, `SU(2)`, `CP^n`, `R^4` are fine), unique across the WHOLE vault (check vault-index-geometry.txt; also avoid the names of pages in the deleted old folder only when they collide with an existing vault page elsewhere — otherwise reuse of an old name is fine and, for the seven names in backlink-map.md, mandatory). Theorem names state the result ("Thm - Curvature of a Shifted Connection", "Thm - The Space of Connections is an Affine Space"), not "Thm - Theorem 11".

D. **Sections.** Each chapter is divided into sections §N.1, §N.2, … following the sources' subsection structure (merged where the sources overlap), each with a short title used byte-identically in the concept map header, the Exercise Index filename, and the callout. Every section has at least three exercises (from the sources' exercises and examples-worth-drilling; when the sources give fewer than three, specify additional exercises — state them precisely — drawn from standard problem sets on the same material: e.g. Kobayashi–Nomizu, Taubes *Differential Geometry: Bundles, Connections, Metrics and Curvature*, Morgan *The Seiberg–Witten Equations*, Hatcher, Milnor–Husemoller). Every exercise page is assigned a difficulty ⭐/⭐⭐/⭐⭐⭐.

E. **Proof obligations, made explicit.** For every Thm page, the spec says: the exact statement (copy it from the inventory, in LaTeX), which source items feed it, what the sources' proof does and where its gaps are (from the inventory), which OTHER pages the proof will invoke (by exact page name — either new pages in this manifest or existing proof-complete vault pages), and, when the sources omit the proof, the name of a standard reference whose proof the writer should follow (e.g. "Kobayashi–Nomizu I, Ch. II Thm 5.1", "Hatcher Thm 3.30", "Lawson–Michelsohn Thm II.8.8", "Smale 1965 / Abraham–Robbin", "Evans Ch. 5", "Morgan Ch. 4"). For a result on the pre-approved import list, say so and name the page that carries the callout.

F. **Dependency order.** For each chapter, order the pages so that every page's prerequisites (its `prereqs` list of Def/Thm basenames) appear earlier in the same chapter or in an earlier chapter or in the existing vault. Give each page a `prereqs` list of basenames.

G. **Existing vault linkage.** For each chapter, list the existing vault pages (from vault-index-geometry.txt) that the chapter should link to instead of re-defining — Differential Geometry I–XII (manifolds, vector bundles, forms, de Rham, Lie groups), Riemannian Geometry I–IV, Algebraic Topology I–III, Hodge Theory I, Spinors, Special Relativity XXI–XXIII, Topology, Linear Algebra — and note which of those are in unproved-pages.txt and therefore must be re-proved in the series under a new name.

H. **Size discipline.** A Def page covers one concept or one tight cluster (compound page). A Thm page covers one result; a long proof is decomposed into lemmas ON that page, not spread across pages, unless a lemma is reused elsewhere (then it gets its own Thm page). Expect roughly 15–35 pages per chapter; chapter XII (algebraic topology with full proofs of homotopy invariance, excision/Mayer–Vietoris, Hurewicz, orientation theory, Poincaré duality) and chapter IX (Sobolev/elliptic theory with full proofs) will be the largest.

Output format of manifest.md, per chapter:

```
## Gauge Theory N — <Title>            (folder: Gauge Theory N/)
Sources: A §…, B §…
Existing vault pages to link: …
Sections: §N.1 <Title> | §N.2 <Title> | …

### §N.1 <Title>
- `Def - <Name>` — type: definition; source items: D2.1.1, D2.1.2, B-D2.1.3; prereqs: [...]; spec: <2–6 sentences: what it defines, both sources' formulations, convention decisions, which examples/non-examples/remarks to include (by item number), what the calibration check should test>
- `Thm - <Name>` — type: theorem; source items: T2.1.1, R2.1.5; prereqs: [...]; statement: <exact statement in LaTeX>; proof: <source proof status; gaps to fill; pages invoked; reference to follow>; spec: <what else the page needs: sources/targets hints, the mechanism for Why Is It True>
- `Ex - <Description>` — type: exercise; difficulty: ⭐⭐; source items: X2.1.3; prereqs: [...]; spec: <the problem, precisely; the intended route; which Def/Thm pages the solution invokes>
- `Exercise Index - §N.1 <Title>` — lists: [the Ex pages above]
…
```

Close the file with (1) the coverage table (every inventory item → destination), (2) the list of all `Imported without proof` callouts in the series (result, page, chapter) — it must be a subset of the pre-approved list — and (3) a cross-chapter dependency summary (which chapters depend on which).

Be exhaustive and precise: the manifest is the contract every writer works from, and anything missing here is missing from the notes. Your final message is only: the path of the file, the page counts per chapter, and the total.
