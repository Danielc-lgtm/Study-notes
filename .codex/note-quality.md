# Note quality rubric

Distilled from `.claude/skills/polymath-notes/SKILL.md` ("Core Philosophy",
"Conceptual Insight Standards", "Writing Style", "Page Types", and the 37-item
"Quality Standards — Self-Evaluation Checklist") and its
`references/templates.md`. Those files remain authoritative; this rubric says how
to *score* a unit against them, which criteria apply to which page type, and what
"done" means. It does not restate the templates.

Two rules govern everything below. **Applicability first:** every criterion is
scored applicable / not applicable before it is scored pass / fail, and a
not-applicable criterion is never padded into existence (a theorem with no
natural categorical framing does not get a hollow "Categorical Definition"; a
definition with one axiom gets no per-axiom failure analysis). **Fix, don't
report:** a failing applicable criterion is repaired in this unit, not logged
for later, unless it needs a decision from the user (then it goes under
"Unresolved" in the ledgers).

---

## 0. Priority dimensions for rewrites (score these first)

For improve-mode units these three are diagnosed and fixed before anything in
sections A–F, and a unit cannot be `complete` while any of them fails.
`AGENTS.md` §7 "Rewrite priorities" is the governing text.

**P1. Rigour — complete proofs everywhere.** Applicable to every Thm / Lemma /
Prop / Cor page (Formal Proof section), every Def page (Examples /
Corollaries and Calibration check), and every Ex page (Complete formal
solution). Pass when: every proof is complete with all cases and both
directions; each step's justification is explicit (which hypothesis, which
earlier lemma, which theorem — wikilinked); no "clearly / obviously /
similarly / it is easy to see / the other case is analogous" stands in for an
argument a careful reader could not expand within a minute; interchanges of
limits, sums, integrals, and derivatives cite the theorem that licenses them;
well-definedness and existence are checked before use (Step 0 pattern);
stated facts on Def and Ex pages are proved on the page or transcluded from the
page that proves them. Fail examples: a proof sketch labelled as a proof; a
"Lemma decomposition" whose full proofs are missing; an example asserted
without verification; an equivalence with one direction shown.

**P2. Self-containedness — context is linked or loaded.** Applicable to every
page. Pass when: every definition and theorem used is transcluded or restated
with a wikilink at first use; every symbol is introduced on the page (A3);
every prerequisite resolves to an existing vault page (or is bold plain text
if the vault lacks it, with a one-line inline explanation so the page still
reads); a cold read of the page succeeds with no click needed for necessity.
This is criterion A5 promoted to a gate.

**P3. Explanation quality — replace when clearly superior.** Applicable to
every explanatory section (Motivation, Axiom Motivation, Why Is It True,
Rederivation Scaffold, Convergent Strategy, Key Takeaways, Bridges, Insights)
and to proof architecture. Pass when the explanation is at least as good as
Codex's own best default explanation of the same point; when it is not,
Codex writes its own and replaces the existing text, recording the reason in
the diagnosis. Guard rails: formal statements stay in standard form (A1);
replacement is for clearly better mechanism, examples, or route — not for
stylistic difference; correct content that only needed tightening is
tightened, not regenerated (`AGENTS.md` §3).

**P4. Conciseness without loss.** Applicable to every page, scored after
P1–P3. Pass when no sentence can be deleted or shortened without losing a
mathematical fact, a case, a justification, an example, or a connection. Fail
signals: the same point explained twice in different words on one page;
formulas restated in prose immediately after the display; sentences that only
announce what the next sentence will do; hedges and qualifiers that carry no
information; paragraphs of motivation that repeat the topic page's Motivation
verbatim on a subpage instead of transcluding or linking it. What P4 must
never do: drop a source item, shorten a proof by omitting a step, collapse two
examples into one, or remove a bridge. When a page feels long but every
sentence earns its place, the remedy is structure (a `> [!note]-` callout, a
subpage, a transclusion), not deletion. Measure by content, not by word count:
a diff that is shorter and loses nothing passes; a diff that is shorter and
loses one justification fails P1 and P4 together.

---

## A. Standards that apply to every page

**A1. Formal register where it belongs.** Definitions and theorem statements are
precise, complete, conventional, and stated once in a clearly marked place
(`# The Definition`; `# Statement` with a `> **Theorem (name).**` blockquote,
immediately after `# Notation`). Hypotheses and conclusion sit in one block.

**A2. Tong register everywhere else.** Motivation, axiom motivation, why-is-it-
true, legal operations, strategy, bridges, takeaways: flowing prose, whiteboard
voice, concrete situation before the formal punchline, mixed sentence rhythm.
Fail signals: bullet inventories where prose would work; labelled fragments
("Trigger: … Action: …") outside the permitted inline `*Trigger:*`/`*Pattern:*`
markers in Legal Operations; hedge stacking; inspirational filler; "w.r.t.",
"iff" in prose; corporate parallelism.

**A3. Notation typed and complete.** Every pivotal symbol in a Statement, The
Definition, or display math is introduced earlier on the same page (Notation
section or inline "Let $X$ be …"). Standing conventions (units, signs, default
assumptions such as "all rings commutative with 1") open the Notation section as
a preamble paragraph, with a `> [!warning] Convention:` callout when sources
diverge. `find-notation-gaps.py` is the triage tool.

**A4. Geometric objects have formulas.** Every contour, region, neighbourhood,
surface, or distribution named in a definition, theorem, or proof carries an
explicit set-builder or parametric specification next to the words. Coordinate
proofs are preferred over picture proofs when both exist.

**A5. Self-contained on arrival.** A reader landing cold understands the page
from its own text plus transclusions (`![[Def - X#The Definition]]`) or brief
restatements-with-wikilinks of every concept it uses. Spot-test three subpages
per unit without clicking any link.

**A6. Graph integrity.** Every `[[target]]` outside math/code resolves; every
`![[page#section]]` hits a real heading; forward references to pages that do not
exist are **bold plain text**, not wikilinks; every jargon occurrence links to
its introducing page (except inside Unlocked, Bridges, Insights, Sources and
Targets, True name, Notation Registry, which keep bold forward references);
display-text wikilinks carry no LaTeX or markdown inside the brackets. YAML
frontmatter present with `type`, `subject`, `tags`, `prereqs` (+ `difficulty`
on exercises, `chapter`/`title` on topic pages).

**A7. Re-entry after months.** The page's first screen gives the conceptual
handle (hook, unifying frame, true name, or one-line mechanism) before any
machinery. Detail is progressively revealed through collapsible `> [!note]-`
callouts and linked subpages — never through omission. No HTML `<details>`.

**A8. Insight density without subtraction.** Multiple perspectives, examples,
and connections are present; nothing from the sources is dropped; no caps on
hints, unlocks, bridges, or legal operations. Length is justified by
correctness, understanding, rederivability, connection, or self-containedness —
not by restating formulas in words.

---

## B. Topic page (chapter-level) criteria

Applicable to every topic page. Section list and formats are in
`templates.md` "Topic Page Template"; SKILL.md "Topic Page" gives the bar.

**B1. Notation Registry** — visible (not collapsed), covers every symbol used in
the subpages, standing-convention preamble when relevant.

**B2. Motivation** — opening hook in sentence one; structural backbone (a
hierarchy, classification, or implication flow) shown as a display equation
when the topic has one; closing audience-assumption paragraph.

**B3. Concept Map** — foldable bullets, wikilinked name on the parent, 3–5
substantive sentences on the child (details, example or non-example,
connection); definitions, theorems, and exercises interleaved in source order;
exercises tagged `(⭐)`/`(⭐⭐)`/`(⭐⭐⭐)` inline; each `## §` section ends with a
`> [!note] Exercise Index — §X.Y` callout; at least one `> [!tip] Unlocked:`
per section unless the section unlocks nothing (aim just above range).

**B4. Sources and Targets (topic-level)** — prose, not lists: about five
recurring targets, five recurring sources, and the routes between them, derived
from the exercises.

**B5. Legal Operations** — 7+ numbered, named, prose-explained operations with
input type and known bridges; 3+ "illegal but tempting" items each naming (a) a
concrete counterexample and (b) the extra condition that would legalise it.
Trigger-reaction patterns are written where they arise.

**B6. Problem-Solving Strategy** — self-contained paragraphs; closes with the
single unifying question of the chapter.

**B7. Most Reusable Properties** — bullets that are full paragraphs with
wikilinks and typical use.

**B8. Bridges** — each bridge explains the construction; wikilink count never
exceeds sentence count.

**B9. Insights** — at least two substantive paragraphs: unifying frame, true
names, trigger-reaction patterns, inheritance ("where does the property come
from"), local-to-global mechanisms, platonic-vs-representation distinctions,
density / truncation–anti-truncation levers, escape-to-infinity or other
failure mechanisms — whichever genuinely apply to this chapter.

---

## C. Definition subpage criteria

Applicable to every `Def - *.md`.

**C1. Axiom Motivation is inventive.** Desiderata; what the definition must
capture and exclude; **per-axiom failure analysis** when there are ≥ 2
independent axioms (concrete counterexample for dropping each, what
strengthening would exclude); forward-reference motivation via a theorem that
would fail otherwise, where apt. Test: could a reader invent the definition from
the motivation alone? 4+ paragraphs for any non-trivial definition; gold
standards `Def - Group.md`, `Def - Normal Subgroup.md`, `Def - The Total
Derivative.md`, `Def - Topological Space.md`.

**C2. The Definition** — primary form, then equivalent formulations.

**C3. Categorical / Structural Definition** — *applicable* for group, ring,
module, ring homomorphism, ideal, topological space, continuous map, σ-algebra,
measurable function, holomorphic function, manifold, Lie group, and any
definition with a natural universal-property or functorial reading; otherwise
not applicable. When applicable it is self-contained.

**C4. Relate to Other Fields / Compression with a True name** — the
maximally operational characterisation, labelled `**True name:**`, when it
differs from the official definition (compactness ↦ "bounded sequence has a
convergent subsequence"; continuity of linear maps ↦ boundedness). Not
applicable when the official definition already *is* the operational one — say
so in one sentence rather than inventing a second name.

**C5. Examples / Corollaries** — instances *and* at least one non-instance for
any non-trivial definition, each probing a different aspect; ends with a
`**Calibration check.**` paragraph naming 2–3 verifications.

**C6. Unlocked by This** — downstream previews, no length cap, bold plain text
for missing pages.

**C7. Compound pages** — if the title lists several notions, every one gets a
complete definition and the page announces its compound nature in one sentence
between Notation and Axiom Motivation.

---

## D. Theorem subpage criteria

Applicable to every `Thm - *.md` (and `Lemma - *.md`, `Cor - *.md`, `Prop - *.md`
where the vault uses them).

**D1. Statement** — `# Statement` header exactly, after Notation, before
Motivation; blockquote form; companion/specialised forms as back-to-back
blockquotes plus a tying remark when they exist.

**D2. Motivation** — role and importance, not a restatement.

**D3. Sources and Targets (theorem-level)** — at least three *disguised sources*
(properties B with a non-obvious B → A bridge to the hypothesis A, each with a
bridge argument and an example problem) and at least three *target
combinations* (C + D → E with the extra ingredient D named and the payoff E
explained). This is input-type broadening made concrete. A block that only
restates the precondition fails. Not applicable only for purely technical
lemmas that are never invoked outside one proof — and then the page says so.

**D4. Why Is It True** — intuition independent of the proof, not a sketch; at
least one **bolded one-line mechanism summary**; names the inheritance
("completeness comes from ℝ"), the local-to-global step, or the failure
mechanism the hypotheses rule out, whichever is the real engine.

**D5. What Makes This Hard** — 2–3 sentences: the non-obvious step, the common
error.

**D6. Rederivation Scaffold** — opens with the self-sufficiency contract;
high-level strategy plus subgoal decomposition with minimal hints; passes the
"forgotten but seen before" reconstruction test.

**D7. Lemma Decomposition** — each lemma a `> [!note]-` callout with
`**Statement:**`, `**Hint:**`, `**Why needed:**`, and a nested
`> [!note]- Full proof`; each practiceable in about five minutes.

**D8. Formal Proof** — complete, collapsible, opens with "Step 0 — [precondition]"
when well-posedness needs checking; no hidden steps.

**D9. Cross-Field Exercise Suggestions** — 3+ genuinely different contexts;
applicable unless the theorem is narrowly technical.

**D10. Bridges / Unlocked** — as B8 / C6.

---

## E. Exercise subpage and exercise index criteria

Applicable to every `Ex - *.md` and `Exercise Index - *.md`.

**E1. Problem Statement with Recall** — transclusion by default for every
definition and theorem used; wikilinks throughout.

**E2. Convergent Strategy** — four labels (`**Problem class:**`,
`**Assumption pattern:**`, `**Theorem routing:**`, `**Key decision point:**`),
each a multi-sentence paragraph.

**E3. Legal Operations Used** — numbered references to the topic page's
operations, each explained in prose for this instance.

**E4. Hints** — graduated `> [!note]-` callouts, each strictly more revealing;
as many as the descent needs.

**E5. Solution three-tier** — plan paragraph; bold per-step summaries;
`> [!note]- Derivation` under each step; one `> [!note]- Complete formal
solution` at the end; theorems restated at point of use. Optional and welcome:
an "illegal but tempting alternative route" warning, an independent sanity
check, a frame-invariance check in physics.

**E6. Key Takeaways** — 3+ paragraphs of 6+ lines each: reusable principle,
trigger condition, transferable diagnostic.

**E7. Difficulty** — `difficulty` in YAML and inline tag everywhere the
exercise is listed.

**E8. Exercise Index** — ≥ 3 exercises per sub-chapter section (web-search to
add if fewer and the environment allows); contextualising preamble paragraph;
each entry = wikilink + inline tag + one-line technique description +
parenthesised list of every Def/Thm used.

---

## F. Unit-level (whole topic graph) criteria

**F1. Source coverage** — every definition, theorem, proof, and exercise in the
repository sources for this chapter appears (create mode) or nothing existing
and correct was lost (improve mode).

**F2. Concept map ↔ subpages agree** — every subpage is in the map, every map
entry has a subpage, statements match.

**F3. Neighbour consistency** — conventions, names, and notation agree with the
preceding/following topic pages and with the DAG entry's framing.

**F4. Cross-subject parity** — sample one topic page, two Def, two Thm, two Ex
from the unit and compare against the gold-standard subjects (Group Theory,
Multivariate Analysis, Special Relativity). Any dimension materially behind
triggers a rewrite of that section. The bar is "as good as the best existing
subject", not "meets the minimum".

**F5. Mechanical audits clean** — the five scripts in `workflow.md` Phase 4.2
plus the link audit.

**F6. No leakage** — no planning text, diagnosis notes, or `.scratch/` content
inside a note; no spec text copied into notes.

---

## G. Final checklist — execute before marking a unit `complete`

Run top to bottom; every line is a command or a yes/no you can actually answer.
Record the result in `progress.json` → `units[<id>].review`.

1. `python3 .claude/skills/polymath-notes/scripts/find-math-bugs.py` → 0 hits in the unit.
2. `python3 .claude/skills/polymath-notes/scripts/find-latex-bugs.py` → 0 hits in the unit.
3. `python3 .claude/skills/polymath-notes/scripts/find-wikilink-bugs.py` → 0 hits in the unit.
4. Link audit: every `[[...]]` and `![[...#...]]` in the unit resolves (grep the targets against `find "Study notes" -name "*.md"`).
5. `grep -L "^# Statement$" "<unit>/Thm - "*.md` → empty.
6. `grep -L "Calibration check" "<unit>/Def - "*.md` → empty (or each exception is trivial and noted).
7. For each Thm: count of `> [!note]- Lemma` equals count of `**Hint:**` equals count of `**Why needed:**`.
8. For each Ex: ≥ 1 `> [!note]- Derivation`, exactly 1 `> [!note]- Complete formal solution`, all four Convergent-Strategy labels present.
9. `grep -E "^- \*\*\[\[Ex - " "<topic page>" | grep -v "(⭐"` → empty; every `## §` section has a `> [!tip] Unlocked:` or a one-line justification for none.
10. Each `Exercise Index - *.md` in the unit has ≥ 3 `[[Ex -` links, inline tags, and a preamble paragraph.
11. Every page in the unit has complete YAML frontmatter.
12. Three-subpage cold-read self-containedness test passed (A5).
13. Every Def: axiom motivation passes the "could invent it" test (C1); true name present or explicitly not applicable (C4); at least one non-example (C5).
14. Every Thm: ≥ 3 disguised sources and ≥ 3 target combinations, or explicit not-applicable (D3); bold mechanism one-liner in Why Is It True (D4); What Makes This Hard present (D5); scaffold contract present (D6).
15. Topic page: hook, backbone (if any), audience paragraph (B2); ≥ 7 legal + ≥ 3 illegal operations with counterexample and legalising condition (B5); unifying-question close (B6); ≥ 2 Insights paragraphs (B9); bridges unpacked (B8).
16. Concept map ↔ subpages reconciled (F2); neighbours and DAG consistent (F3).
17. Parity sample against a gold-standard subject done; every "materially behind" section rewritten (F4).
18. Nothing correct from the pre-edit version was lost (diff reviewed); no planning text leaked (F6).
19. Improve mode only: every "fail" in the Phase-3 diagnosis is now "pass" or listed under Unresolved with a reason.
20. **P1 rigour gate:** `grep -n -i "clearly\|obviously\|it is easy to see\|similarly\|analogous\|left to the reader\|omitted" "<unit>"/*.md` reviewed line by line — every hit either expanded into an argument or justified as genuinely trivial; every Thm/Lemma/Prop/Cor page has a non-empty `Formal Proof` covering all cases and directions; every `> [!note]- Full proof` inside a lemma callout is present and complete; every Ex page has its `Complete formal solution`.
21. **P2 self-containedness gate:** for every page in the unit, the first use of each Def/Thm is a transclusion or a restatement-with-wikilink (grep each `[[Def -` / `[[Thm -` target and confirm a `![[` or restatement precedes or accompanies it); cold-read test done on every Thm page and every Ex page, not just three samples.
22. **P3 explanation gate:** the diagnosis names, per explanatory section, `keep / tighten / replace`, and every `replace` has a one-line reason; replaced sections re-read against A2 (register) and A1 (statements untouched).
23. **P4 conciseness gate:** a final tightening pass was made over every page in the unit; for each page the pre/post diff was checked to confirm that every deleted or shortened passage carried no fact, case, justification, example, or connection that is absent from the final text (`git diff --word-diff` on the page, read the removals); no proof step, source item, example, or bridge was removed.
24. Unit committed with a descriptive message; ledgers updated; branch pushed.

A unit with any line unresolved stays `review`, not `complete`.
