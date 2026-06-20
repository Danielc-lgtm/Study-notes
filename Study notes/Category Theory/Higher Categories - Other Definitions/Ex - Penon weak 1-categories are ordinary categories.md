---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Penon Weak ω-Category"
  - "Def - Category"
  - "Def - Monad and Comonad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $X$ be a **[[Def - Penon Weak ω-Category|Penon weak ω-category]]** whose underlying reflexive globular set has no nondegenerate cells above dimension $1$ — i.e. $X_n$ consists only of identities for $n \ge 2$. (This is the Penon weak *$1$*-category, the $1$-truncation.) Show that $X$ is exactly an ordinary **[[Def - Category|category]]**: the chosen composition is strictly associative and unital, so the weak structure collapses to a strict one. Conversely, show every ordinary category arises this way. This is the level-$1$ sanity check that Penon's definition recovers ordinary categories.

**Recall:**

![[Def - Penon Weak ω-Category#The Definition]]

A **[[Def - Category|category]]** $\mathcal{C}$ consists of objects, a hom-set $\mathcal{C}(x,y)$ for each pair, an associative composition, and identities; equivalently, a reflexive globular set concentrated in dimensions $0$ and $1$ with strictly associative, strictly unital composition of $1$-cells.

The key feature: in a Penon weak ω-category, associativity and unitality of $1$-cell composition hold only up to chosen **coherence $2$-cells** (supplied by the contraction). When there are no nondegenerate $2$-cells, those coherence cells are forced to be identities.

---

# Convergent Strategy

**Problem class:** This is a *truncation / sanity-check* problem — verify a higher-categorical definition reduces to the expected classical notion at low dimension. It is one of the two mandatory tests (level $1$ gives categories, level $2$ gives bicategories) that every definition of weak higher category must pass, and the routine is to track where the coherence cells live and observe that truncation forces them to be identities.

**Assumption pattern:** The decisive assumption is that there are *no nondegenerate cells above dimension $1$*. Every coherence cell in a Penon weak ω-category — the associator $2$-cell relating $(h\,g)\,f$ to $h\,(g\,f)$, the unitor $2$-cells — is a $2$-cell. With no nondegenerate $2$-cells available, each such coherence cell must be a *degenerate* (identity) $2$-cell, and a degenerate $2$-cell whose source and target are parallel $1$-cells forces those $1$-cells to be *equal*. So associativity-up-to-coherence becomes associativity-on-the-nose.

**Theorem routing:** The route is: the $H$-algebra structure map $\theta : HX \to X$ supplies, in dimension $1$, a chosen composite of composable $1$-cells (this is the composition of the category) and chosen identities (degeneracies $i : X_0 \to X_1$); in dimension $2$, the contraction would supply associator/unitor $2$-cells, but truncation forces these to be identities, yielding the strict associativity and unit laws of a [[Def - Category|category]]. The converse routes through the previous exercise: an ordinary category, regarded as a strict ω-category concentrated in dimensions $0,1$, is a Penon weak ω-category.

**Key decision point:** The non-obvious step is recognising that a coherence cell is *data of dimension one higher than the law it governs*. Associativity is a statement about $1$-cells, but the *weak* associativity is witnessed by a $2$-cell. So the right thing to truncate is not the $1$-cells but the $2$-cells, and it is their absence that strictifies the $1$-dimensional laws.

---

# Legal Operations Used

1. **Operation 8 from the topic page (truncate to recover a low-dimensional case).** We set the top dimension to $1$ and read off the surviving structure, which is the entire content of the exercise.

2. **Operation 4 from the topic page (take algebras for a monad).** The composition and identities of the resulting category are read off from the $H$-algebra structure map $\theta$ in dimensions $0$ and $1$.

3. **Operation 3 from the topic page (contraction), observed in its trivialised form.** The contraction's associator and unitor $2$-cells are forced to be identities by the truncation, which is precisely what strictifies the laws.

---

# Hints

> [!note]- Hint 1
> Ask where the *associativity* of composition lives in a Penon weak ω-category. It is not an equation between $1$-cells; it is a $2$-cell connecting the two bracketings. What dimension is that cell, and what does the truncation hypothesis say about cells of that dimension?

> [!note]- Hint 2
> A degenerate (identity) $2$-cell has the same $1$-cell as both its source and its target. If the associator $2$-cell from $(h\,g)\,f$ to $h\,(g\,f)$ is forced to be degenerate, what does that say about the two bracketings as $1$-cells?

> [!note]- Hint 3
> For the converse, you have already shown (in the companion exercise) that any strict ω-category is a Penon weak ω-category. An ordinary category *is* a strict ω-category with nothing above dimension $1$. So the two directions together give a bijection (indeed an equivalence) between Penon weak $1$-categories and ordinary categories.

---

# Solution

The argument is short once the bookkeeping is right. Step 1 reads the $0$- and $1$-dimensional structure off the algebra map and identifies it as objects, morphisms, composition, and identities. Step 2 observes that the coherence $2$-cells are forced to be identities, strictifying the laws. Step 3 supplies the converse.

**Step 1: the $0$- and $1$-dimensional data is a category-without-laws.**

> [!note]- Derivation
> Let $(X, \theta)$ be the truncated $H$-algebra. The $0$-cells $X_0$ are the objects. The $1$-cells $X_1$, with source/target $s, t : X_1 \to X_0$, are the morphisms; $X(x,y) := \{f \in X_1 : s f = x,\ t f = y\}$ are the hom-sets. The algebra map $\theta : HX \to X$ includes, among the operations of $HX$ in dimension $1$, the *binary composite* of a composable pair: $HX$ contains the formal composite of $x \xrightarrow{f} y \xrightarrow{g} z$, and $\theta$ sends it to a $1$-cell $g \cdot f : x \to z$. This defines a composition $\mathcal{C}(y,z) \times \mathcal{C}(x,y) \to \mathcal{C}(x,z)$. Identities are the degeneracies: $\mathrm{id}_x := i(x) = s_0 x \in X_1$. So far we have objects, morphisms, a composition, and identities — everything but the *laws*.

**Step 2: the laws hold strictly, because the coherence $2$-cells are forced to be degenerate.**

> [!note]- Derivation
> In a general Penon weak ω-category, associativity is *weak*: $\theta$ supplies, from the contraction, an associator $2$-cell
> $$\alpha_{f,g,h} : (h \cdot g) \cdot f \;\Rightarrow\; h \cdot (g \cdot f)$$
> a genuine $2$-cell whose source and target are the two bracketings (parallel $1$-cells $x \to w$). By hypothesis $X$ has *no nondegenerate $2$-cells*: every element of $X_2$ is a degeneracy $i(p)$ of some $1$-cell $p$. A degenerate $2$-cell $i(p)$ has source $p$ and target $p$. Therefore $\alpha_{f,g,h}$, being a $2$-cell, is some $i(p)$, and its source and target — which are $(h \cdot g)\cdot f$ and $h \cdot (g\cdot f)$ — must both equal $p$. Hence
> $$(h \cdot g) \cdot f = h \cdot (g \cdot f),$$
> strict associativity. The identical argument applied to the unitor $2$-cells $\lambda_f : \mathrm{id} \cdot f \Rightarrow f$ and $\rho_f : f \cdot \mathrm{id} \Rightarrow f$ forces $\mathrm{id} \cdot f = f = f \cdot \mathrm{id}$, the strict unit laws. Therefore $(X,\theta)$ is an ordinary [[Def - Category|category]].

**Step 3: the converse.**

> [!note]- Derivation
> Conversely, let $\mathcal{C}$ be an ordinary category. View it as a strict ω-category $Q_{\mathcal{C}}$ concentrated in dimensions $0$ and $1$ (objects, morphisms, strict composition, no higher cells). By the companion result that *every strict ω-category is a Penon weak ω-category*, $Q_{\mathcal{C}}$ is a Penon weak ω-category; and it has no nondegenerate cells above dimension $1$, so it is a Penon weak $1$-category. The two constructions are mutually inverse on objects (truncate-then-include and include-then-truncate are the identity), and they extend to functors, giving an equivalence between Penon weak $1$-categories and ordinary categories.

> [!note]- Complete formal solution
> Let $(X,\theta)$ be a Penon weak ω-category with $X_n$ purely degenerate for $n \ge 2$.
>
> **Objects, morphisms, composition, identities.** Set objects $= X_0$, morphisms $= X_1$ (with source $s$, target $t$), hom-sets $X(x,y) = s^{-1}(x) \cap t^{-1}(y)$. The algebra map $\theta$ evaluates the formal binary composite of a composable pair $f, g$ to a $1$-cell $g \cdot f$, defining composition; $\mathrm{id}_x = i(x)$ defines identities.
>
> **Strict laws.** The contraction component of $\theta$ would supply an associator $2$-cell $\alpha_{f,g,h} : (h\cdot g)\cdot f \Rightarrow h\cdot(g\cdot f)$ and unitor $2$-cells $\lambda_f, \rho_f$. Each is a $2$-cell, hence by hypothesis degenerate, hence of the form $i(p)$ with source $=$ target $= p$. Equating source and target gives $(h\cdot g)\cdot f = h\cdot(g\cdot f)$ and $\mathrm{id}\cdot f = f = f\cdot \mathrm{id}$. Thus $(X,\theta)$ is an ordinary category.
>
> **Converse.** An ordinary category $\mathcal{C}$ is a strict ω-category concentrated in dimensions $\le 1$, hence (by the companion exercise) a Penon weak ω-category with nothing nondegenerate above dimension $1$, i.e. a Penon weak $1$-category. Truncation and inclusion are mutually inverse and functorial, giving an equivalence
> $$\{\text{Penon weak } 1\text{-categories}\} \simeq \{\text{ordinary categories}\}. \qquad \blacksquare$$

---

# Key Takeaways

**A coherence cell lives one dimension above the law it governs, so truncating the cells strictifies the laws.** This is the single most reusable idea in the chapter for sanity checks. Weak associativity of $1$-cells is a $2$-cell; weak associativity of $2$-cells is a $3$-cell; and in general the failure of a $k$-dimensional law to hold on the nose is recorded by a $(k{+}1)$-cell. Consequently, killing all cells above dimension $n$ forces every law at dimension $n$ to hold strictly, which is exactly why a weak $n$-category truncated at its top dimension behaves rigidly there. The trigger is "what happens at the top dimension of a weak $n$-category", and the reaction is "the top-dimensional laws are strict because their witnessing cells would be one dimension too high".

**Sanity checks at levels $1$ and $2$ are the acceptance test for any definition of weak higher category.** A definition is only trustworthy if it reproduces the structures we already understand: ordinary categories at level $1$, bicategories at level $2$. Several historically-proposed definitions *failed* one of these tests (Penon's original non-reflexive version among them), which is how they were discovered to be defective. When you meet an unfamiliar definition of weak $n$-category, the first thing to do is truncate to $1$ and to $2$ and check you recover categories and bicategories; if you do not, the definition is wrong, however elegant. This exercise is the level-$1$ test for Penon, and the companion Tamsamani–Simpson exercise is the level-$2$ test for the geometric side.

**Truncation and inclusion exhibit the classical world as a full subcategory of the higher one.** The converse direction matters as much as the forward one: it is not enough that *every* Penon weak $1$-category is a category; we also need *every* category to arise, and for the correspondence to be an equivalence (not just a surjection). This pattern — truncate-down and include-up being mutually inverse — is how one proves that a higher-categorical world genuinely *extends* the classical one rather than merely overlapping it. The same shape of argument recurs whenever a generalisation is shown to be conservative: discrete categories inside categories, strict inside weak, ordinary categories inside $(\infty,1)$-categories via the nerve.
