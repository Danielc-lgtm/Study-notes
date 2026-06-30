---
type: definition
subject: higher-categories
prereqs:
  - "Def - Globular Set"
  - "Def - Category"
  - "Def - 2-Category and Bicategory"
  - "Def - Enriched Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

We build on globular sets. As in [[Def - Globular Set]], $X_n$ is the set of **$n$-cells**, with source and target $s, t : X_n \to X_{n-1}$. Two $n$-cells are **parallel** when they have the same source and target (all $0$-cells count as parallel). For $0 \leq p < n$ we write $s_p, t_p : X_n \to X_p$ for the **iterated** source and target obtained by applying $s$ (respectively $t$) $n - p$ times; by globularity these are well-defined and $s_p$ and $t_p$ of an $n$-cell are parallel $p$-cells. Two $n$-cells $x, y$ are **$p$-composable** (for $p < n$) when the $p$-target of $x$ equals the $p$-source of $y$: $t_p(x) = s_p(y)$. The composite is written $y \circ_p x$. The identity (degenerate) $n$-cell on a $p$-cell $a$ is $1_a$ or $\mathrm{id}_a$. The full registry is on [[Higher Categories — Strict n-Categories and Notions of Monoidal Category]].

This is a compound page: it defines two interlocking notions — the **strict $n$-category** (cells up to dimension $n$) and the **strict $\omega$-category** (cells in all dimensions) — because the $\omega$-version is the $n \to \infty$ limit of the $n$-version, and the two are stated by the same axioms with the dimension bound removed.

---

# Axiom Motivation

We have the bare cellular skeleton — a [[Def - Globular Set|globular set]] — and we want to make it into something we can *compute* in: a higher category. The single design principle is that **everything an ordinary category can do, a higher category should be able to do in every dimension at once, and strictly.** An ordinary category lets you compose arrows: given $f : a \to b$ and $g : b \to c$ you form $g \circ f : a \to c$, associatively and with identities. A strict $\omega$-category should let you compose $n$-cells too — but here a new feature appears: $n$-cells can be glued along boundaries of *any* lower dimension, so there is not one composition but a whole family $\circ_0, \circ_1, \dots, \circ_{n-1}$.

Consider $2$-cells, the first genuinely new dimension. A $2$-cell $\alpha : f \Rightarrow g$ lives between parallel arrows $f, g : a \to b$. Two such bigons can be glued in two distinct ways. **Vertical** gluing ($\circ_1$): if $\beta : g \Rightarrow h$ has source equal to the target of $\alpha$, stack them to get $\beta \circ_1 \alpha : f \Rightarrow h$ — this is composition *along the shared $1$-cell* $g$. **Horizontal** gluing ($\circ_0$): if $\gamma : f' \Rightarrow g'$ lives between arrows $f', g' : b \to c$, then $\gamma \circ_0 \alpha : f' \circ f \Rightarrow g' \circ g$ glues *along the shared $0$-cell* $b$. The general pattern is now visible: for each dimension $p$ below $n$ there is a composition $\circ_p$ of $n$-cells that agree on their $p$-dimensional boundary, and it produces an $n$-cell.

Each composition $\circ_p$ should be **associative** and have **identities**, for the same reason ordinary composition does: a long chain of cells glued along their $p$-boundaries must have an unambiguous total composite, and gluing on a degenerate cell must change nothing. So far this is just "a category in each dimension, in each direction." If that were all, the axioms would say: for each $p < n$, the $n$-cells and $p$-cells form a category under $\circ_p$. This is necessary but not sufficient, and seeing what is missing is the crux.

The missing axiom is **interchange**, and it is forced the moment two different compositions can act on the same cells. Take four $2$-cells arranged in a $2 \times 2$ grid: $\alpha, \beta$ stacked vertically on the left, $\gamma, \delta$ stacked vertically on the right, with left and right composable horizontally. You can compose the grid two ways: first vertically (getting two horizontal-composable cells) then horizontally, or first horizontally (getting two vertical-composable cells) then vertically. The **interchange law** demands these agree:
$$(\delta \circ_1 \gamma) \circ_0 (\beta \circ_1 \alpha) = (\delta \circ_0 \beta) \circ_1 (\gamma \circ_0 \alpha).$$
Drop interchange and a pasting diagram has no well-defined value: "the composite of the grid" depends on the order you contract it, and the entire calculus of pasting diagrams — the reason higher categories are useful at all — collapses. Interchange is exactly the law that makes a grid of cells have a single composite, and in dimension $2$ it is what we already saw makes horizontal composition a *functor* in the [[Def - 2-Category and Bicategory|2-category]] $\mathbf{Cat}$. In general there is an interchange law for *every pair* of distinct composition [[Def - Dimension|dimensions]] $p \neq q$.

Why insist on **strict** equality everywhere — strict associativity, strict identities, strict interchange — rather than equality up to coherent isomorphism? Two reasons, one practical and one cautionary. Practically, strictness is the right notion for the leading example: composition of [[Def - Functor|functors]] and the various composites of [[Def - Natural Transformation|natural transformations]] in $\mathbf{Cat}$ are all strictly associative and unital, so $\mathbf{Cat}$ is an honest strict $2$-category and a great deal of category theory is strict $2$-categorical. Cautionarily, strictness is *too strong* past dimension $2$: there is a genuine theorem (the failure of strictification in dimension $3$ and above, traceable to the [[Higher Categories — Strict n-Categories and Notions of Monoidal Category#§3 Coherence and the Periodic Table|Eckmann–Hilton]] phenomenon) that not every weak $3$-category is equivalent to a strict one. So strict $\omega$-categories are the clean, computable, but ultimately *too rigid* notion; understanding precisely where they fail is what motivates the weak theory. This page pins down the rigid notion exactly so the later relaxation has a target.

---

# The Definition

A **strict $\omega$-category** (also: **strict $\infty$-category**) is a [[Def - Globular Set|globular set]] $X$ together with, for each pair of dimensions $0 \leq p < n$, a **composition** operation
$$\circ_p : \{(y, x) \in X_n \times X_n : t_p(x) = s_p(y)\} \longrightarrow X_n, \qquad (y, x) \mapsto y \circ_p x,$$
defined on $p$-composable pairs, and for each $p$-cell $a$ a **degenerate** (identity) $n$-cell $1_a^{(n)} \in X_n$ for every $n > p$ (we write $1_a$ when the dimension is clear), subject to the following axioms for all dimensions where they make sense.

- **Sources and targets of composites.** For a $p$-composite, $s_p(y \circ_p x) = s_p(x)$ and $t_p(y \circ_p x) = t_p(y)$; for $q > p$ the $q$-source and $q$-target are inherited compatibly (the boundary of a gluing is the gluing of the boundaries).
- **Associativity.** Each $\circ_p$ is associative: $(z \circ_p y) \circ_p x = z \circ_p (y \circ_p x)$ whenever both sides are defined.
- **Identities.** The degenerate cells are two-sided units: $x \circ_p 1_{s_p(x)} = x = 1_{t_p(x)} \circ_p x$, and the degenerate of a composite is the composite of degenerates ($1$ is functorial).
- **Interchange.** For any two distinct dimensions $q > p$ and cells composable in both, the two ways of contracting agree:
$$(w \circ_q z) \circ_p (y \circ_q x) = (w \circ_p y) \circ_q (z \circ_p x).$$
- **Identities interchange.** $1_a \circ_p 1_b = 1_{a \circ_p b}$ for composable lower cells, so degenerate cells compose to degenerate cells.

A **strict $n$-category** is the same data and axioms but for an **$n$-truncated** globular set — cells only in dimensions $0$ through $n$, compositions $\circ_p$ for $0 \leq p < n$. A strict $0$-category is a **set**; a strict $1$-category is an ordinary [[Def - Category|category]]; a strict $2$-category is a [[Def - 2-Category and Bicategory|2-category]] in the usual sense, with $\circ_0$ horizontal and $\circ_1$ vertical composition.

A **strict $\omega$-functor** $F : X \to Y$ is a morphism of underlying globular sets that preserves all composites and all degenerate cells: $F(y \circ_p x) = F(y) \circ_p F(x)$ and $F(1_a) = 1_{F(a)}$. Strict $\omega$-categories and strict $\omega$-functors form a category $\omega\text{-}\mathbf{Cat}$ (and $n\text{-}\mathbf{Cat}$ for the truncated version).

---

# Categorical / Structural Definition

There is a beautiful inductive definition by **iterated enrichment** that bypasses globular sets entirely. Recall (see [[Def - Enriched Category]]) that a category **enriched** in a [[Def - Monoidal Category|monoidal category]] $(\mathcal{V}, \otimes, I)$ has, for each pair of objects, a hom-*object* $\mathcal{C}(A, B) \in \mathcal{V}$ rather than a hom-set, with composition a morphism $\mathcal{C}(B,C) \otimes \mathcal{C}(A,B) \to \mathcal{C}(A,C)$ in $\mathcal{V}$ and identities picked out by maps $I \to \mathcal{C}(A,A)$.

Now define the categories of strict $n$-categories by induction. Let $\mathbf{0\text{-}Cat} = \mathbf{Set}$, with monoidal product the cartesian product. Given that $n\text{-}\mathbf{Cat}$ is a cartesian monoidal category, set
$$(n{+}1)\text{-}\mathbf{Cat} = \mathbf{Cat}(n\text{-}\mathbf{Cat}) := \big[\text{categories enriched in } n\text{-}\mathbf{Cat}\big].$$
This category is again cartesian monoidal, so the induction continues. **A strict $(n+1)$-category is exactly a category enriched in strict $n$-categories.** Unwinding: a strict $2$-category is a category enriched in $\mathbf{Cat} = 1\text{-}\mathbf{Cat}$ (its hom-objects are categories, exactly the [[Def - 2-Category and Bicategory|2-category]] definition); a strict $3$-category is a category enriched in $2$-categories; and so on. The strict $\omega$-category is the limit of the truncations $\cdots \to n\text{-}\mathbf{Cat} \to (n{-}1)\text{-}\mathbf{Cat} \to \cdots$.

The two definitions agree because enrichment in $n\text{-}\mathbf{Cat}$ reproduces exactly one new layer of cells (the morphisms of the hom-$n$-categories are the $(n+1)$-cells) together with one new composition ($\circ_0$, the enriched composition) that automatically interchanges with the inherited ones (the enriched composition is a *functor*, and functoriality *is* interchange — exactly as in the [[Def - 2-Category and Bicategory|2-category]] case where interchange is functoriality of horizontal composition). The strict, on-the-nose nature of the axioms is what makes the iterated enrichment land in a strict (rather than weak) structure: enriched associativity and unit laws are *equalities* of morphisms in $\mathcal{V}$.

---

# Relate to Other Fields / Compression

A strict $\omega$-category is the **fully iterated category**: a set, then a category, then a category-of-categories, climbing one dimension of morphisms at a time, with everything strictly associative. The compression that organises the whole subject is the slogan **strict $n$-category : globular set :: category : graph** — composition imposed strictly on the cellular skeleton, in every dimension. Every property of categories that is "structural" (associativity, identities, functoriality of composition) recurs verbatim in each dimension; the only new ingredient is interchange between dimensions.

**True name:** a strict $\omega$-category is "a globular set in which you can compose cells along a boundary of any dimension, associatively, unitally, and compatibly across dimensions (interchange)." Operationally, when you meet one, reach for the pasting-diagram picture: any labelled globular pasting diagram has a *unique* composite, and that uniqueness — guaranteed by strict associativity plus interchange — is the entire reason strict $\omega$-categories are easy to compute in. The corresponding weak notion replaces "unique composite" by "composite defined up to a contractible space of choices," which is exactly where the difficulty of higher category theory lives.

The most important compression for downstream work: the **free strict $\omega$-category** on a globular set is generated by *globular pasting diagrams*, and the resulting monad $T$ on $\mathbf{GSet}$ is **cartesian**. This single fact — that the free-strict-$\omega$-category monad is well-behaved enough to support an operad theory — is the foundation of the Batanin–Leinster definition of weak $\omega$-category. Strictness is studied not because it is the right final notion, but because the *free* strict structure is the scaffold on which the weak notion is built.

---

# Examples / Corollaries

**Is an instance — any set, as a strict $0$-category.** No composition, no cells above dimension $0$; the axioms are vacuous. This anchors the induction: $0\text{-}\mathbf{Cat} = \mathbf{Set}$.

**Is an instance — any ordinary category, as a strict $1$-category.** Objects are $0$-cells, arrows are $1$-cells, $\circ_0$ is ordinary composition, degenerate $1$-cells are identity morphisms. Associativity and identities are the [[Def - Category|category]] axioms; there is no interchange because there is only one composition. A strict $1$-category is *exactly* a category.

**Is an instance — $\mathbf{Cat}$ as a strict $2$-category.** The $0$-cells are small [[Def - Category|categories]], $1$-cells are [[Def - Functor|functors]], $2$-cells are [[Def - Natural Transformation|natural transformations]]; $\circ_1$ is vertical composition $(\beta \circ_1 \alpha)_X = \beta_X \circ \alpha_X$, $\circ_0$ is horizontal composition (whiskering and Godement product). [[Def - Functor|Functor]] composition is strictly associative, so $\mathbf{Cat}$ is strict on the nose, and interchange holds by naturality. This is the canonical strict higher category and the reason the strict theory is worth having.

**Is an instance — a strict $\omega$-category from a chain complex (the linear case).** A chain complex of abelian [[Def - Group|groups]] gives rise to a strict $\omega$-category (a "linear" or "additive" $\omega$-category) where $n$-cells are degree-$n$ elements and composition is addition along boundaries; this is the additive shadow of the general picture and shows strict $\omega$-categories arise in homological algebra.

**Is NOT an instance — a bicategory that is not strict.** The [[Def - 2-Category and Bicategory|bicategory]] of [[Def - Ring|rings]], bimodules, and bimodule maps, with horizontal composition $N \otimes_B M$, is *not* a strict $2$-category: associativity of $\otimes$ holds only up to the canonical isomorphism $(P \otimes_C N)\otimes_B M \cong P \otimes_C (N \otimes_B M)$, never as an equality of sets. It is a strict $\omega$-category only after replacing it by an equivalent strict model (which exists in dimension $2$ by [[Thm - Strictification of Bicategories|strictification]], but not in general dimension).

**Is NOT an instance — a globular set with composition that fails interchange.** Equip the $2$-truncated globular set underlying $\mathbf{Cat}$ with the correct $\circ_1$ but a *wrong* $\circ_0$ on $2$-cells that ignores naturality. Then a $2 \times 2$ grid of $2$-cells has two unequal contractions, so interchange fails and the structure is not a strict $2$-category. The data — cells and a vertical and a horizontal composition — is present, but the cross-dimensional compatibility is missing, and that compatibility is exactly what the definition requires.

**Calibration check.** Verify that a strict $1$-category is precisely an ordinary [[Def - Category|category]] (the single composition $\circ_0$ is the category composition; there is no interchange to check). Confirm that in $\mathbf{Cat}$ the interchange law $(\delta \circ_1 \gamma)\circ_0(\beta \circ_1 \alpha) = (\delta \circ_0 \beta)\circ_1(\gamma \circ_0 \alpha)$ for natural transformations is just naturality applied twice. And check that the iterated-enrichment definition reproduces the truncation $n\text{-}\mathbf{Cat}$: a category enriched in $\mathbf{Set} = 0\text{-}\mathbf{Cat}$ is an ordinary category $= 1\text{-}\mathbf{Cat}$, as it must be.

---

# Unlocked by This

> [!tip] Unbiased Monoidal Category *(from this chapter)*
> A one-object strict $2$-category is a strict [[Def - Monoidal Category|monoidal category]] — composition becomes the tensor. Relaxing strictness in the one-object case and recording *all* arities of tensoring at once is the [[Def - Unbiased Monoidal Category|unbiased monoidal category]] of §2, the cleanest home for coherence.

> [!tip] Weak ω-Categories and the Batanin–Leinster Definition *(from Higher Category Theory)*
> The free *strict* ω-category monad $T$ on globular sets is **cartesian**, and a **globular operad** is a cartesian morphism $P \to T$. Algebras for the initial contractible such operad are **weak ω-categories**: strictness provides the scaffold, the operad provides the coherent (rather than strict) composites.

> [!tip] The Homotopy Hypothesis and ∞-Groupoids *(from Algebraic Topology)*
> A strict ω-**groupoid** (all cells invertible) is far too rigid to model homotopy types — strict ω-groupoids capture only products of Eilenberg–MacLane spaces. The failure of the strict notion here is precisely what **Grothendieck's homotopy hypothesis** says must be repaired by weakening: weak ω-groupoids ≃ spaces.
