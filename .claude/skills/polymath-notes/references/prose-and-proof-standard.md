# The Prose and Proof Standard — the thesis as baseline

This file is the single authority for two things across every skill in this repository: **the prose register** in which explanatory text is written, and **the minimum level of rigour and detail** at which every proof is written. It is referenced by `polymath-notes`, `paper-notes`, `exercise-builder`, `CLAUDE.md`, `AGENTS.md`, and `.codex/note-quality.md`. Where an older instruction anywhere in the repository names a different prose exemplar (the David Tong lecture-note register that earlier drafts of the vault used), this file supersedes it.

The exemplar for both standards is the owner's thesis:

```
prose/Chiang Sung En-Thesis.pdf
```

Extract it with `pymupdf` (`pip install pymupdf`, then `import pymupdf; doc = pymupdf.open(path); text = "\n".join(p.get_text() for p in doc)`), or with `pdftotext -layout` if poppler is installed. **Read it before writing any note, on every run** — the register drifts back toward terse specification prose within a few pages if the exemplar is not fresh in mind. The page numbers below are PDF page numbers.

The thesis is a baseline in two different senses, and the difference matters:

- For **prose**, the thesis is *the* register. Replicate its manner (not its subject).
- For **proofs**, the thesis is the *minimum*. A proof in the vault is at least as explicit as the thesis's fully written proofs, and the vault goes beyond the thesis wherever the thesis economises (its occasional "similarly" and its labelled "Proof Sketch" items are *below* the vault's floor and are never imitated).

---

## Part I — The prose register

### 1. Calibration passages

Hold these open while writing. Each shows one feature of the register in its purest form.

| Feature | Where in the thesis |
|---|---|
| Motivation that names the question, the competing approaches, and why the chosen one matters | §1.1 Motivation, pp. 11–12: the "globalist" versus "localist" approach to causal discovery |
| A section opener that orients, poses the guiding questions *as questions*, then gives a roadmap | §3.1 opener, p. 43: "Having introduced … we now explore … Can we harness …? Which causal properties …? To address these questions systematically, we begin by … We then … Finally, we synthesize …" |
| General definition → smallest concrete case, immediately | Definition 2.1.1 (Lancaster interaction measure, general product) → the bivariate case $\Delta_L P = P_{XY} - P_X P_Y$ → the three-variable expansion, pp. 15–16 |
| Definition → a remark naming the key insight → a fully worked numeric example | Definition 2.1.3 (Möbius inversion) → Remark 2.1.2 ("The key insight behind Möbius inversion is …") → Example 2.1.1 with the explicit $3 \times 3$ zeta and Möbius matrices and $f(2)$ recovered line by line, pp. 16–17 |
| Formal definition first, intuition re-derived afterwards in a titled remark | Definition 2.1.8 (Kullback–Leibler divergence) → Remark 2.1.3 (Intuition: KL divergence as excess surprise), building entropy, cross-entropy, and the identity $D_{KL}(P\|Q) = H(P,Q) - H(P)$, p. 19 |
| A worked example in which every line carries its justification | Example 2.2.1 (chain factorisation): $p(b \mid a, c) = p(b \mid c)$ derived in four displayed lines, each annotated "(by factorization)", "(since $p(a,c) = p(a)p(c \mid a)$)", pp. 22–23 |
| Both halves of a two-sided claim computed, not asserted | Example 2.2.4 (collider): marginal independence computed by summing out $c$; conditioning-creates-dependence computed via Bayes' theorem, p. 24 |
| Why a hypothesis is needed, with the failure mode | Remark 2.2.5 (Importance of the positive probability assumption), p. 27; Example 4.2.1 (the XOR counterexample to faithfulness), pp. 66–67 |
| An assumption stated, then immediately motivated in its own remark | Assumption 3.2.1 (unique information monotonicity) → Remark 3.2.2 (Intuition for …), p. 54; Assumption 3.2.3 → Remark 3.2.6, p. 57 |
| Verification of a routine claim spelled out clause by clause | Remark 3.1.1: reflexivity, symmetry, transitivity of the equivalence relation each shown, p. 49 |
| Honesty about provenance | "We now prove a result that was stated in Ref. [1] without proof and for which, to the best of our knowledge, a proof is not found in the literature. Here we provide a detailed original proof." p. 44 |
| A result closed with a conclusion in words | The "Conclusion:" paragraphs after Theorem 3.1.3 (p. 47), Theorem 3.1.4 (p. 48), and Theorem 3.1.5 (p. 50) |

### 2. The shape of an explanation

Every unit of exposition in the vault — a topic page's Motivation, a definition page, a theorem page, an exercise's takeaways — follows the thesis's rhythm:

1. **Orient.** Say where the reader is and what this piece does, in one or two sentences. On a topic page this is the opening of Motivation; on a subpage it is the first sentence after Notation. When the piece answers a question, pose the question as a question.
2. **Motivate.** Name the problem the object solves, the alternatives, and what goes wrong without it. The thesis does this in ordinary academic prose — "The typical framework of causal discovery involves … a fundamentally global approach … In contrast, a local approach enables us to …" — never with a labelled fragment and never with a slogan.
3. **State formally.** The definition or theorem, crisp and complete, in the formal register. When a definition has several clauses, the clauses may be a bulleted list (the thesis's Definition 2.2.1 lists the two components of a directed graph as bullets); when a theorem has several parts, label them (Soundness / Completeness; Part I / Part II; Case 1 / Case 2).
4. **Unpack immediately in the smallest concrete case.** Right after the general statement, write out the $n = 2$ or three-element or two-variable instance with the actual objects in it — the bivariate Lancaster measure, the eight elements of the subset lattice on $\{X, Y, Z\}$, the five partitions of a three-element set with their factorisations. A definition that has not been instantiated is not yet explained.
5. **Re-explain in a remark titled by its purpose.** The thesis's remarks are named for what they do: *(Intuition: …)*, *(Significance of …)*, *(Importance of the … assumption)*, *(Interpretation of …)*, *(Verification of …)*, *(Cancellation property of …)*. The vault's sections already have these roles — Axiom Motivation, Why Is It True, What Makes This Hard, True name — so the named-remark form is realised as those sections; the content standard is the thesis's: an intuition is re-derived, not asserted ("The key insight is that if $g(\pi_1) = g(\pi_2)$ … then partition $\pi_1$ provides no unique contribution beyond what $\pi_2$ already captures").
6. **Close in words.** After a result or a computation, a sentence saying what has just been shown and what it means ("This demonstrates that any factorization of the joint distribution into marginals results in a vanishing Lancaster interaction measure, confirming the definition's goal").

### 3. Sentence-level register

- **Measured academic voice, first person plural, direct.** "We now prove", "We need to show", "Consider", "Note that". Not chatty, not a whiteboard monologue, not marketing. The thesis never performs enthusiasm; it explains.
- **Every claim travels with its reason.** The thesis does not write "conditioning on a collider creates dependence"; it writes the Bayes computation and then says "Since $p(c \mid a, b)$ generally depends on both $a$ and $b$, we have $p(a \mid b, c) \neq p(a \mid c)$." Prose in the vault has the same texture: a claim, then its "since"/"because"/"by".
- **Expansive, not compressed.** The thesis re-explains on purpose ("In other words, …", "Intuitively, …", "This means that …"). Comprehensive standard prose is preferred over compact formalism even when it runs several times longer. Introduce a symbol only when prose would be genuinely worse — a computation, a precisely quantified statement, a signature. Never write a display equation whose only role is to restate the sentence before it.
- **Standard terminology only.** Use the literature's name for every concept, and say which field the name comes from when that helps. No coined compound nouns used as if established; no Capitalised Pseudo-Terms; no repurposed standard symbols. If a concept has no standard name, say so and describe it.
- **Every symbol is declared and typed at first use** — what it denotes, its domain and codomain or the set it belongs to, whether it is fixed, bound, or quantified. One symbol, one meaning, for the whole page.
- **Prose over bullets, bullets for enumerations.** Reasoning is paragraphs. Bullets are for genuinely parallel items: the clauses of a definition, the cases of a theorem, the axioms of a structure, the operations of a lattice.
- **No abbreviations in prose** ("with respect to", "if and only if", "almost everywhere"; the symbol $\iff$ inside a formal statement is fine).
- **No hedge stacking, no inspiration, no filler.** State mathematical facts directly. Do not write "this beautiful theorem reveals deep connections"; write the explanation that makes the connection visible. Do not write labelled fragments ("Trigger: … Action: …") outside the one permitted inline `*Trigger:*` / `*Pattern:*` idiom in Legal Operations.
- **Honest about provenance and difficulty.** Say where a result comes from, say when the notes supply reasoning the source omitted, say what is genuinely hard, and mark anything you could not verify.
- **Concrete before abstract; build from what the reader knows.** Motivate with the specific problem; explain what is outside the owner's background (see `CLAUDE.md`) and do not re-explain what is well inside it.
- **Geometric objects come with formulas.** Every region, contour, neighbourhood, surface, or distribution named in a definition, theorem, or proof carries an explicit set-builder or parametric specification beside the words; where a coordinate proof and a picture proof both exist, the coordinate proof is the one written.
- **Brief historical or philosophical asides only when they illuminate.**

### 4. How the register maps onto the vault's sections

| Vault section | Thesis counterpart | What "in the thesis register" means here |
|---|---|---|
| Topic page: Motivation | §1.1 Motivation; §3.1 opener | Orient, pose the guiding questions, name the competing approaches and what goes wrong without the new one, give the roadmap, close with the audience-assumption paragraph |
| Def page: Axiom Motivation | Definition → *Remark (Intuition …)* / *(Importance of … assumption)* | Desiderata, then per-clause failure analysis with a concrete counterexample for each dropped clause, in the manner of Remark 2.2.5 and Example 4.2.1 |
| Def page: The Definition + Examples | Definition → smallest concrete case → worked Example with every line justified | The formal statement, then its $n = 2$ instance, then instances and non-instances each *verified*, not asserted |
| Thm page: Statement | Theorem with labelled parts | Hypotheses and conclusion in one block; parts labelled |
| Thm page: Why Is It True | *Remark (Intuition …)* after a theorem | The mechanism re-derived in words, with one bolded one-sentence summary |
| Thm page: Formal Proof, Lemma Decomposition | The fully written proofs (Theorems 2.3.3, 3.1.1, 3.1.5, 3.2.1, 3.2.2, 3.2.3) | Part II of this file |
| Ex page: Solution, Key Takeaways | Worked Examples; the "Conclusion:" paragraphs | Every derivation line justified; the takeaway states in words what the computation showed and when the pattern recurs |
| Legal Operations, Bridges, Insights, Sources and Targets | The thesis's explanatory remarks | Full prose paragraphs; each bridge unpacks the construction it names |
| Paper-notes section pages and Whole-Paper Story | §3.1 opener; Chapter 1 | Section openers orient and preview; the Story keeps `paper_source/example.md`'s *structure* (one connected narrative, a mental picture for every object, connective sentences at each boundary, a final total picture) but its *sentences* are in the thesis register |

---

## Part II — The proof standard

### 5. The rule: every theorem mentioned is proved

**A theorem, lemma, proposition, or corollary may appear in the vault only together with a complete, self-contained proof.** "Appear" means any of: stated on a topic page's concept map; given a `Thm -` / `Lemma -` / `Prop -` / `Cor -` page; invoked inside a proof; used in an exercise solution; used to verify an example or a calibration check on a definition page; named in a Bridge, an Unlocked callout, or an Insight as a result the reader may lean on. The proof lives in exactly one place — the `# Formal Proof` section of that result's own page, fed by its `# Lemma Decomposition` — and every other place that uses the result **wikilinks that page and restates the statement at the point of use**.

Consequences:

- **No statement-only pages.** A page named `Thm - X (Statement)`, or a `Thm -` page whose Formal Proof is a sketch, a citation, or empty, violates the rule. Do not create one. When a note being written depends on such a page that already exists in the vault, the writer either supplies the complete proof on that page (preferred) or writes a new fully proved page and links that instead. `find-unproved-theorems.py` (below) reports both the pages and every link into them.
- **Depth is not an excuse.** Elliptic regularity, the Sobolev embedding and Rellich compactness theorems, Sard's theorem and Sard–Smale, the Fredholm property of elliptic operators, the Hodge theorem, Chern–Weil, the Weitzenböck formula, the classification of $U(1)$-bundles by the first Chern class, the compactness of the Seiberg–Witten moduli space — these are proved in full, in the vault, on their own pages, however long that runs. Length is handled by structure (lemma decomposition, collapsible callouts, subpages), never by omission.
- **The single exception: an imported result.** A result whose complete published proof is genuinely book-length — of the order of fifty pages or more even in the most efficient textbook treatment (Freedman's classification of simply connected topological four-manifolds, Donaldson's diagonalisation theorem with its full analytic package, Uhlenbeck's compactness theorem, the Atiyah–Singer index theorem) — may be **used without proof**, but only under all of the following conditions:
  1. It is *not* given a `Thm -` page and is *not* written in a `> **Theorem.**` blockquote on any page. It appears only inside a callout of the form below, so that the reader can never mistake it for a result the vault has established.
  2. The callout states the result exactly (every hypothesis, the precise conclusion, every convention it depends on), cites a complete published proof by author, title, and section or page, and gives a paragraph on the architecture of that proof — what its main steps are and which of them carry the real difficulty.
  3. Every consequence drawn from it is proved in full, with the import invoked as an explicitly labelled hypothesis of the argument.
  4. The topic page carries a section `# Imported Results` listing every such import in the chapter with the reason it could not be proved here. A chapter with no imports has no such section.
  5. Before importing, the writer has tried to prove. "Import" is the last resort for the five-or-so results above, not a category for anything long.

```markdown
> [!warning] Imported without proof: [Name of the result]
> **Statement.** [Exact statement, all hypotheses, all conventions.]
>
> **Source of a complete proof.** [Author, *Title*, edition, section/pages.]
>
> **Architecture of the proof.** [One paragraph: the main steps and where the difficulty lies.]
>
> **Why it is imported rather than proved here.** [One or two sentences.]
>
> Everything below that uses this result says so explicitly at the point of use.
```

### 6. The minimum level of detail (what the thesis's proofs do, and the vault therefore always does)

The thesis's fully written proofs are the floor. Read Theorem 2.3.3 (p. 30), Theorem 3.1.1 (pp. 34–35), Theorem 3.1.5 (p. 40), Theorem 3.2.1 (p. 43), Theorem 3.2.2 (pp. 45–46), and Theorem 3.2.3 (pp. 48–49) and note that every one of them does all of the following. So does every proof in the vault.

1. **It opens by naming what is assumed and what must be shown.** "Direction 1 ($\Rightarrow$): Assume $I(X;Y \mid Z) = 0$. We need to show $X \perp Y \mid Z$." Every proof, and every labelled block inside a proof, begins this way.
2. **It is organised by labelled blocks, each announced with what it establishes.** *Direction 1 / Direction 2* for an equivalence; *Case 1 / Case 2* for a case split (with a sentence establishing that the cases are exhaustive); *Part I / Part II* for a multi-part theorem; *Step 0, Step 1, …* for a linear argument. Each block's first sentence says what the block proves.
3. **Each move is introduced by a bold lead-in naming it before it is made.** "**Apply contrapositive of contraction axiom:**", "**Identify unblocked path through $Z$:**", "**Rule out chain and confounder paths:**", "**Establish $Z$ as collider:**", "**Conclude V-structure:**". The reader always knows what the next paragraph is for.
4. **Every displayed equality, inequality, or implication carries its justification on the same line or the next.** "(by factorization)", "(since $p(a,c) = p(a)p(c \mid a)$)", "(by the self-redundancy axiom)", "(by Lemma 2)", "(by the dominated convergence theorem, with dominating function $g$)". A displayed line without a reason is a gap.
5. **Every hypothesis is invoked by name at the exact point it is used**, and a hypothesis that is never invoked is treated as a bug in the proof or the statement.
6. **Well-definedness, existence, and routine structural checks are written out clause by clause.** Reflexivity, symmetry, and transitivity are each shown (Remark 3.1.1). A map defined on representatives is checked to be independent of the representative. An object that must exist before it can be used is constructed first (the vault's "Step 0 — [precondition]").
7. **Both directions of every equivalence, all cases of every case split, all parts of every multi-part statement.** The thesis's own "Similarly for $Y$ and $Z$" (p. 35) is *below* the vault's floor: the vault writes the parallel case out, or states precisely which substitution turns the written case into the omitted one and checks that every step survives the substitution.
8. **Numbered intermediate results are combined explicitly.** "Combining equations (3.58) and (3.59), we have …" — the reader is told which earlier lines are being used, not left to search.
9. **It closes in words.** "Therefore, $X_k$ must be a co-parent of $X_i$." / "Hence the conditional mutual information consists exactly of the unique information from $S_2$ plus the synergistic information." The last sentence says what was shown.
10. **When a proof is by contradiction, the contradiction is named**: what was assumed, which earlier line it contradicts.
11. **Every new symbol introduced inside the proof is typed at its introduction**, and no symbol changes meaning inside a proof.

To this floor the vault adds its own standing requirements, which remain in force:

12. Every interchange of limit, sum, integral, or derivative cites the theorem that licenses it, with its hypotheses checked on the page.
13. Every measurability, smoothness, integrability, convergence, or regularity condition is verified where it is used, not assumed.
14. No "clearly", "obviously", "it is easy to see", "one checks", "similarly", "analogously", "left to the reader", "omitted". Each of these is replaced by the argument it was standing in for. (The P1 grep in `.codex/note-quality.md` enforces this.)
15. The `# Lemma Decomposition` breaks the proof into independently practiceable lemmas, each with `**Statement:**`, `**Hint:**`, `**Why needed:**`, and a nested `> [!note]- Full proof` that is itself complete at the level above; the `# Formal Proof` may cite those lemmas by number and is otherwise complete.
16. The `# Rederivation Scaffold` remains: a proof that is complete but has no scaffold fails the spaced-practice purpose of the vault.

### 7. Where proofs live and how they are invoked

- **On a theorem page:** `# Formal Proof` holds the complete proof in a `> [!note]- Complete formal proof` callout; `# Lemma Decomposition` holds the lemmas with their full proofs. Between them, nothing is left to another page except results that have their own fully proved page, which are wikilinked and restated at the point of use ("By the [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]] — for $k > n/2$ the inclusion $W^{k,2}(M) \hookrightarrow C^0(M)$ is bounded — the sequence …").
- **On a definition page:** every example is *verified* to be an instance and every non-example *verified* to fail, on the page; every corollary in Examples / Corollaries is proved on the page or wikilinked to the page that proves it; the calibration checks are things the reader can actually carry out from what is on the page.
- **On an exercise page:** the `> [!note]- Complete formal solution` is a complete proof at the level of §6; every theorem it invokes is wikilinked to a page with a complete proof and restated at the point of use; every "by a standard argument" is written out.
- **On a topic page:** the concept-map child bullet states the result; the page does not carry proofs. Any imported result is listed in `# Imported Results`.
- **In paper notes:** an external result the paper cites is proved in full on its own atomic page in the paper's `Subpages/` folder (or wikilinked to an existing fully proved vault page), not merely stated in an external-input callout. The callout remains the place where the *paper's* use of the result is recorded; the proof lives on the atomic page.
- **In exercise-builder output:** the `> [!note]- Full solution` toggle meets §6; every theorem used links to its proved page.

### 8. A model proof in the required form

The following is the format — not the length; a real proof is as long as it needs to be. It is a lemma from the vector-bundle chapter of the gauge theory notes, chosen because it is short enough to show every feature at once.

> **Lemma (curvature is tensorial).** Let $E \to M$ be a smooth vector bundle and $\nabla$ a connection on $E$. Define $F_\nabla(X,Y)s = \nabla_X \nabla_Y s - \nabla_Y \nabla_X s - \nabla_{[X,Y]} s$ for vector fields $X, Y$ on $M$ and sections $s$ of $E$. Then $F_\nabla(X,Y)s$ is $C^\infty(M)$-linear in each of $X$, $Y$, and $s$; consequently $F_\nabla$ is a well-defined section of $\Lambda^2 T^*M \otimes \operatorname{End}(E)$.
>
> *Proof.* Fix vector fields $X, Y$ on $M$, a section $s$ of $E$, and a smooth function $f \in C^\infty(M)$. We need to show three identities: $F_\nabla(fX, Y)s = f F_\nabla(X,Y)s$, $F_\nabla(X, fY)s = f F_\nabla(X,Y)s$, and $F_\nabla(X,Y)(fs) = f F_\nabla(X,Y)s$; antisymmetry in $(X,Y)$ is immediate from the definition, so the second identity follows from the first, and we prove the first and the third.
>
> **Linearity in $X$.** By the definition of a connection, $\nabla_{fX} = f \nabla_X$ (a connection is $C^\infty(M)$-linear in the vector-field slot), and by the Leibniz rule for the Lie bracket, $[fX, Y] = f[X,Y] - (Yf)X$. Substituting,
> $$F_\nabla(fX,Y)s = f\nabla_X \nabla_Y s - \nabla_Y (f \nabla_X s) - \nabla_{f[X,Y] - (Yf)X}\, s \qquad \text{(definition of } F_\nabla \text{, } \nabla_{fX} = f\nabla_X\text{, bracket identity)}$$
> $$= f\nabla_X \nabla_Y s - (Yf)\nabla_X s - f\nabla_Y \nabla_X s - f\nabla_{[X,Y]}s + (Yf)\nabla_X s \qquad \text{(Leibniz rule } \nabla_Y(f\sigma) = (Yf)\sigma + f\nabla_Y \sigma \text{; } C^\infty\text{-linearity in the vector slot)}$$
> $$= f\big(\nabla_X\nabla_Y s - \nabla_Y \nabla_X s - \nabla_{[X,Y]}s\big) = f F_\nabla(X,Y)s \qquad \text{(the two } (Yf)\nabla_X s \text{ terms cancel).}$$
>
> **Linearity in $s$.** Apply the Leibniz rule twice:
> $$\nabla_X\nabla_Y(fs) = \nabla_X\big((Yf)s + f\nabla_Y s\big) = (XYf)s + (Yf)\nabla_X s + (Xf)\nabla_Y s + f\nabla_X\nabla_Y s \qquad \text{(Leibniz rule, then Leibniz rule again on each term)},$$
> and by the same computation with $X$ and $Y$ exchanged, $\nabla_Y\nabla_X(fs) = (YXf)s + (Xf)\nabla_Y s + (Yf)\nabla_X s + f\nabla_Y\nabla_X s$. Also $\nabla_{[X,Y]}(fs) = ([X,Y]f)s + f\nabla_{[X,Y]}s$ (Leibniz rule). Subtracting,
> $$F_\nabla(X,Y)(fs) = \big(XYf - YXf - [X,Y]f\big)s + f F_\nabla(X,Y)s = f F_\nabla(X,Y)s \qquad \text{(since } [X,Y]f = XYf - YXf \text{ by definition of the bracket; the mixed } (Xf)\nabla_Y s,\ (Yf)\nabla_X s \text{ terms cancel in pairs).}$$
>
> **Conclusion.** $F_\nabla(X,Y)s$ is $C^\infty(M)$-linear in $X$, in $Y$ (by antisymmetry and the first identity), and in $s$. A map that is $C^\infty(M)$-multilinear in vector fields and sections is induced by a bundle map — this is the tensor characterisation lemma, [[Thm - Tensor Field is C-Infinity Multilinear over C-Infinity Functions]], whose proof shows that the value at $p$ depends only on $X_p, Y_p, s_p$ — so $F_\nabla$ defines a section of $\Lambda^2 T^*M \otimes \operatorname{End}(E)$. Therefore the curvature is a tensor. $\blacksquare$

Every feature of §6 is visible: the opening "We need to show", the bold lead-ins, a reason on every displayed line, the named cancellation, the explicit invocation of the one external result (wikilinked and restated), the closing sentence in words.

### 9. Mechanical enforcement

Run from the repository root after any batch of theorem, definition, or exercise pages:

```
python3 .claude/skills/polymath-notes/scripts/find-unproved-theorems.py "Study notes/<area>/<subject>"
```

It reports statement-only pages, `Thm -`/`Lemma -`/`Prop -`/`Cor -` pages with a missing, empty, or self-confessed-incomplete `# Formal Proof`, lemma callouts without a nested `Full proof`, and every wikilink into a statement-only page. It must come back clean for the unit before the unit is committed. It is one-directional: a clean run is necessary, never sufficient — the line-by-line P1 audit in `.codex/note-quality.md` still has to be done, and the eleven-point list in §6 is what that audit checks.

The P1 grep stays in force as well:

```
grep -n -i "clearly\|obviously\|it is easy to see\|similarly\|analogous\|left to the reader\|omitted\|sketch" "<unit>"/*.md
```

Every hit is expanded into the argument it stood for, or justified in one line as a genuinely non-mathematical use of the word.

### 10. Self-check (added to every skill's checklist)

- **Prose register.** Spot-read three explanatory sections against the calibration passages in §1: do they orient, motivate, state, unpack in the smallest case, re-explain, and close in words? Is the voice the thesis's measured academic voice? Is every general statement instantiated?
- **Every theorem mentioned is proved.** For every `Thm -`/`Lemma -`/`Prop -`/`Cor -` page in the unit, `# Formal Proof` is complete at the level of §6; for every theorem *invoked* anywhere in the unit, the invocation wikilinks a page whose Formal Proof is complete and restates the statement at the point of use. `find-unproved-theorems.py` is clean on the unit.
- **No statement-only pages** were created, and no new link points at one.
- **Imports are registered.** Every use of a result without proof is in the `Imported without proof` callout form, meets all five conditions of §5, and is listed in the topic page's `# Imported Results`.
- **Thesis-floor audit of two proofs.** Pick the two longest proofs in the unit and check the eleven points of §6 one by one on each.
