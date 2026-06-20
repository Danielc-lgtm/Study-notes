---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Small Object Argument"
  - "Def - Relative Cell Complex"
  - "Def - Transfinite Composition and Smallness"
  - "Def - Pullback and Pushout"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Carry out the [[Thm - The Small Object Argument|small object argument]] in full detail. Let $\mathcal{C}$ be cocomplete and $I$ a set of maps whose domains are [[Def - Transfinite Composition and Smallness|small]] relative to $I\text{-cell}$. Construct, for each map $f : X\to Y$, a factorization $f = p(f)\circ i(f)$ with $i(f)\in I\text{-cell}$ and $p(f)\in I\text{-inj}$, and prove all of:

(a) the transfinite tower is a genuine $\lambda$-sequence (colimit-preserving at limits);

(b) the left factor $i(f)$ is a relative $I$-cell complex;

(c) the right factor $p(f)$ has the RLP against every map of $I$, using smallness;

(d) the factorization is functorial in $f$.

State precisely how the length $\lambda$ is chosen from the smallness data.

**Recall:**

![[Thm - The Small Object Argument#Statement]]

A [[Def - Relative Cell Complex|relative $I$-cell complex]] is a transfinite composite of pushouts of coproducts of maps of $I$; $I\text{-inj} = \mathrm{RLP}(I)$ is the maps lifting against every generator. An object $A$ is [[Def - Transfinite Composition and Smallness|$\kappa$-small relative to $I\text{-cell}$]] if for regular $\lambda\geq\kappa$, maps $A\to\mathrm{colim}_\beta Z_\beta$ out of a $\lambda$-sequence of $I$-cell maps factor essentially uniquely through a bounded stage.

---

# Convergent Strategy

**Problem class:** This is the construction-in-full of the chapter's central machine — the factorization target at its hardest. Where [[Ex - The small object argument sketch]] in the previous chapter sketched the topological case, here the construction is carried out abstractly with every claim proved, including the often-omitted functoriality.

**Assumption pattern:** The two inputs are cocompleteness (so all the colimits exist) and smallness of the domains of $I$ (so the right factor lifts). Recognizing that smallness is used in *exactly one* place — proving the RLP of $p(f)$ — and nowhere in building the tower, is the conceptual key.

**Theorem routing:** The route is: define the tower by canonical cell-attachment indexed by all current lifting squares (giving functoriality); the left factor is a relative cell complex by definition of the tower; the right factor lifts against $I$ because smallness sends every lifting square's top map to a bounded stage where a cell was attached. Choose $\lambda$ regular above the common smallness threshold of the domains of $I$.

**Key decision point:** The non-obvious choice is to index each pushout by the *entire set* of current lifting squares, not by a chosen subset. This canonical indexing is what makes the construction functorial — a map of factorization problems induces a map of index sets, hence of towers — and is the difference between "a factorization exists" and "a functorial factorization exists," the latter being what cofibrant/fibrant replacement needs.

---

# Legal Operations Used

1. **Operation 2 from the topic page (attach a cell to solve a lifting problem).** Each successor stage pushes out the coproduct of generators indexed by current lifting squares, attaching one cell per unsolved problem.

2. **Operation 3 from the topic page (run the small object argument to factor a map).** The exercise is the construction underlying this operation, carried out in full.

3. **Operation 6 from the topic page (close $I\text{-cof}$ under structural operations).** The left factor is a transfinite composite of pushouts of coproducts, which is a relative cell complex and hence an $I$-cofibration by saturation.

---

# Hints

> [!note]- Hint 1
> Set $Z_0 = X$, $f_0 = f$. At each successor, let $S_\beta$ be the set of *all* commuting squares from a generator $i\in I$ to $f_\beta : Z_\beta\to Y$, and push out the coproduct $\coprod_{S_\beta} i$ along the coproduct of top maps. Use the full $S_\beta$, not a subset.

> [!note]- Hint 2
> At limit ordinals take colimits; this makes the tower colimit-preserving by construction, so it is a genuine $\lambda$-sequence. The left factor $Z_0\to Z_\lambda$ is then a transfinite composite of pushouts of coproducts of generators — a relative cell complex.

> [!note]- Hint 3
> For the RLP: a square from $i\in I$ to $p(f) = f_\lambda$ has top map $\mathrm{dom}(i)\to Z_\lambda$. By smallness it factors through some $Z_\alpha$. That square was in $S_\alpha$, so at stage $\alpha+1$ a cell was attached supplying the lift. This is the *only* use of smallness.

> [!note]- Hint 4
> Choose $\lambda$ a regular cardinal strictly above $\kappa := \sup\{\kappa_i\}$, where $\kappa_i$ is the smallness threshold of $\mathrm{dom}(i)$ (a set of generators, so the sup is a cardinal). Regularity is needed so the bounded-stage factorization of smallness applies.

> [!note]- Hint 5
> For functoriality: a square $(a, b)$ from $f$ to $f'$ pushes each lifting square of $f$ forward to one of $f'$, inducing a map $S_\beta(f)\to S_\beta(f')$, hence a map of pushouts at each stage; assemble by transfinite induction to get $Z(f)\to Z(f')$ commuting with $i, p$.

---

# Solution

The construction builds a transfinite tower of cell attachments (Step 1), shows it is a $\lambda$-sequence with cell-complex left factor (Steps 2–3), proves the right factor lifts against $I$ via smallness (Step 4), and verifies functoriality (Step 5). The single subtle input is smallness, used only in Step 4; the single design choice enabling functoriality is canonical indexing, made in Step 1.

**Step 1: Define the tower with canonical cell-attachment.**

> [!note]- Derivation
> Given $f : X\to Y$, set $Z_0 = X$, $f_0 = f$. For a successor $\beta+1 < \lambda$, let
> $$S_\beta = \Big\{ (i, u, v) : i\in I,\ u : \mathrm{dom}(i)\to Z_\beta,\ v : \mathrm{cod}(i)\to Y,\ f_\beta u = v i \Big\}$$
> be the set of all commuting squares from a generator to $f_\beta$. Form the pushout
> $$\begin{array}{ccc}
> \coprod_{(i,u,v)\in S_\beta}\mathrm{dom}(i) & \xrightarrow{\ \langle u\rangle\ } & Z_\beta \\
> {\scriptstyle\coprod i}\downarrow & & \downarrow \\
> \coprod_{(i,u,v)\in S_\beta}\mathrm{cod}(i) & \xrightarrow{\ \ } & Z_{\beta+1}
> \end{array}$$
> and let $f_{\beta+1} : Z_{\beta+1}\to Y$ be induced by $f_\beta$ on $Z_\beta$ and by $\langle v\rangle$ on the cells (these agree on the pushout corner since $f_\beta u = v i$). At a limit ordinal $\gamma$, set $Z_\gamma = \mathrm{colim}_{\beta<\gamma} Z_\beta$, $f_\gamma$ induced. Put $Z(f) = Z_\lambda$, $i(f) : X\to Z_\lambda$ the canonical map, $p(f) = f_\lambda$. Then $p(f)\, i(f) = f$.

**Step 2 (part a): The tower is a genuine $\lambda$-sequence.**

> [!note]- Derivation
> Colimit-preservation at limit ordinals is built in: we *defined* $Z_\gamma = \mathrm{colim}_{\beta<\gamma} Z_\beta$, so the canonical map $\mathrm{colim}_{\beta<\gamma} Z_\beta\to Z_\gamma$ is the identity, hence an isomorphism. At successor ordinals there is no condition. So $\beta\mapsto Z_\beta$ is a colimit-preserving functor $\lambda\to\mathcal{C}$, i.e. a $\lambda$-sequence. Cocompleteness of $\mathcal{C}$ guarantees all the pushouts and colimits exist.

**Step 3 (part b): The left factor is a relative $I$-cell complex.**

> [!note]- Derivation
> Each successor map $Z_\beta\to Z_{\beta+1}$ is, by Step 1, a pushout of $\coprod_{S_\beta} i$, a coproduct of maps of $I$. The map $i(f) : Z_0\to Z_\lambda$ is the transfinite composition of the $\lambda$-sequence (Step 2). A transfinite composite of pushouts of coproducts of maps of $I$ is exactly a [[Def - Relative Cell Complex|relative $I$-cell complex]]. So $i(f)\in I\text{-cell}$.

**Step 4 (part c): The right factor lifts against $I$ (the smallness step).**

> [!note]- Derivation
> Choose $\lambda$ as in Step 0 below. Let a lifting square be given: $i\in I$, $u : \mathrm{dom}(i)\to Z_\lambda$, $v : \mathrm{cod}(i)\to Y$ with $p(f)\, u = v\, i$. The tower $Z_0\to\cdots\to Z_\lambda$ is a $\lambda$-sequence of $I\text{-cell}$ maps, and $\mathrm{dom}(i)$ is $\kappa$-small relative to $I\text{-cell}$ with $\lambda\geq\kappa$ regular, so $u$ factors as $\mathrm{dom}(i)\xrightarrow{u_\alpha} Z_\alpha\to Z_\lambda$ for some $\alpha<\lambda$. Then $(i, u_\alpha, v)\in S_\alpha$, so at stage $\alpha+1$ the cell $\mathrm{cod}(i)$ for this square was attached, giving $\bar v : \mathrm{cod}(i)\to Z_{\alpha+1}$ with $\bar v\, i = (Z_\alpha\to Z_{\alpha+1})u_\alpha$ and $f_{\alpha+1}\bar v = v$. Composing into $Z_\lambda$ yields $w : \mathrm{cod}(i)\to Z_\lambda$ with $w i = u$, $p(f) w = v$ — a diagonal lift. Hence $p(f)\in I\text{-inj}$. Smallness was used precisely to factor $u$ through a bounded stage.

**Step 5 (part d): Functoriality.**

> [!note]- Derivation
> Given a square $(a, b)$ from $f$ to $f'$ ($a : X\to X'$, $b : Y\to Y'$, $f' a = b f$), define $\phi_\beta : Z_\beta(f)\to Z_\beta(f')$ by transfinite induction. $\phi_0 = a$. At a successor, a square $(i, u, v)\in S_\beta(f)$ maps to $(i,\ \phi_\beta u,\ b v)$, which lies in $S_\beta(f')$ because $f'_\beta(\phi_\beta u) = b f_\beta u = b v i = (bv) i$. This map $S_\beta(f)\to S_\beta(f')$ induces a map of the coproducts of generators compatible with the attaching maps, hence by the universal property of the pushout a map $\phi_{\beta+1} : Z_{\beta+1}(f)\to Z_{\beta+1}(f')$ extending $\phi_\beta$. At limits, take the induced map of colimits. The map $\phi_\lambda : Z(f)\to Z(f')$ satisfies $\phi_\lambda\, i(f) = i(f')\, a$ and $p(f')\,\phi_\lambda = b\, p(f)$, so the factorization is functorial.

> [!note]- Complete formal solution
> **Step 0 — length.** For each $i\in I$ let $\kappa_i$ be a smallness threshold of $\mathrm{dom}(i)$ relative to $I\text{-cell}$; since $I$ is a set, $\kappa = \sup_i\kappa_i$ is a cardinal. Fix a regular cardinal $\lambda > \kappa$. Cocompleteness gives all colimits below.
>
> **Tower.** $Z_0 = X$, $f_0 = f$; at successors $Z_{\beta+1}$ is the pushout of $\coprod_{S_\beta} i$ along the coproduct of top maps, $S_\beta$ the set of all squares from a generator to $f_\beta$, with $f_{\beta+1}$ induced; at limits, colimits. $Z(f) = Z_\lambda$, $i(f) : X\to Z_\lambda$, $p(f) = f_\lambda$; $p(f) i(f) = f$.
>
> (a) Colimits at limits are built in, so the tower is a colimit-preserving functor $\lambda\to\mathcal{C}$, a $\lambda$-sequence. (b) Each successor map is a pushout of a coproduct of generators, so $i(f)$ is the transfinite composite of such — a relative $I$-cell complex. (c) For a square from $i\in I$ to $p(f)$, smallness factors the top map through some $Z_\alpha$; the square is in $S_\alpha$, a cell was attached at $\alpha+1$, and it supplies a lift, so $p(f)\in I\text{-inj}$. (d) A map $(a,b) : f\to f'$ induces $S_\beta(f)\to S_\beta(f')$, hence maps of pushouts, hence $\phi_\lambda : Z(f)\to Z(f')$ commuting with $i, p$.
>
> Hence every map factors functorially as a relative $I$-cell complex followed by an $I$-injective. $\blacksquare$

---

# Key Takeaways

**Smallness enters in exactly one step, and knowing which one demystifies the whole construction.** The tower is built, and its left factor is a cell complex, for *any* set $I$ whatsoever — cocompleteness alone suffices. Smallness is invoked only to prove the right factor $p(f)$ lifts against $I$, by sending each lifting square's top map to a bounded stage. Internalizing this localization of the hypothesis is the single most clarifying fact about the small object argument: it tells you that when the construction "fails," it fails by producing a non-injective right factor, and that the fix is always to establish smallness of the generator domains. This is the diagnostic to carry into every application, from $\mathbf{Top}$ to chain complexes to algebras over an operad.

**Canonical indexing is what upgrades existence to functoriality, and functoriality is what the rest of the theory needs.** A non-canonical version — "attach a cell for each lifting problem you happen to choose" — produces a valid factorization but no functor, because there is no canonical map between two such towers. Indexing each pushout by the *entire* set of current lifting squares makes a map of factorization problems push squares forward to squares, inducing a map of towers. The payoff is large: functorial factorization is exactly what makes cofibrant replacement $Q$ and fibrant replacement $R$ into functors, which is what lets the total derived functors $\mathbf{L}F = F\circ Q$, $\mathbf{R}U = U\circ R$ of the previous chapter exist. The general lesson — that choosing constructions canonically (over the full index set) buys naturality — recurs whenever one wants a construction to assemble into a functor.

**The transfinite tower is "solve every lifting problem by gluing, then iterate until smallness catches them all."** Stripping away the bookkeeping, the construction is a single idea repeated: a lifting problem with no solution is solved by attaching its solution as a cell, and iteration handles the new problems this creates, with smallness guaranteeing the iteration is long enough that nothing escapes. This reframes a cofibration as "a retract of the universal record of solved lifting problems," and the small object argument as the explicit construction of that record. Recognizing this pattern — build by forcing the desired property cell-by-cell, terminate by a smallness/compactness bound — lets you anticipate analogous constructions (free algebras, injective resolutions, Bousfield localizations) as instances of one machine.
