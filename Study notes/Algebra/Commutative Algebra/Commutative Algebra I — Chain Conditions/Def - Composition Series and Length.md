---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Quotient Module"
  - "Def - Noetherian and Artinian Module"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; modules are unital. Let $R$ be a ring and $M$ an [[Def - Module|R-module]]. A **chain of submodules** is a finite strictly decreasing sequence $M = M_0 \supsetneq M_1 \supsetneq \cdots \supsetneq M_n = 0$; its **length** is $n$ (the number of strict steps, equivalently the number of *quotients* $M_i/M_{i+1}$). A module $S \neq 0$ is **simple** if its only [[Def - Submodule|submodules]] are $0$ and $S$. We write $\ell(M)$ or $\ell_R(M)$ for the length of $M$, with the convention $\ell(M) = \infty$ when $M$ has no composition series, and $\ell(0) = 0$. The full registry is on [[Commutative Algebra I — Chain Conditions]].

This is a compound page: it defines three interlocking notions — the **simple module** (the atom), the **composition series** (a maximal chain with simple quotients), and the **length** $\ell(M)$ (the invariant the Jordan–Hölder theorem extracts from it) — because none is usable without the others: length is *defined* through composition series, and a composition series is *defined* as a chain whose quotients are simple.

---

# Axiom Motivation

The goal is a notion of "size" for a module that is genuinely additive — a single integer $\ell(M)$ that behaves like dimension does for vector spaces, in particular $\ell(M) = \ell(N) + \ell(M/N)$ — but that makes sense over an arbitrary ring, where modules have no basis and no well-defined dimension. The path to it is to find the right *atoms*, decompose every module into them, and prove the count of atoms is an invariant.

**Why the atoms are simple modules.** For a vector space the atoms are one-dimensional subspaces, and dimension counts how many you stack. Over a ring "one-dimensional" makes no sense, but the *order-theoretic* content survives: a one-dimensional subspace is one with no proper non-zero subspace, i.e. a **simple** module. So the correct atom is the simple module — a non-zero module whose only submodules are $0$ and itself. These are the indecomposable building blocks for *chains*: you cannot insert a submodule strictly between $0$ and a simple module, by definition. The reason to count simple quotients rather than simple submodules is that a general module need not contain a simple submodule sitting at the bottom, but it always (when finite) has a maximal chain whose *successive quotients* are simple, and it is those quotients — the **composition factors** — that the count is about.

**Why a composition series is a *maximal* chain, and why maximality means simple quotients.** Take any chain $M = M_0 \supsetneq \cdots \supsetneq M_n = 0$. It is **maximal** (cannot be refined by inserting another submodule) exactly when no submodule fits strictly between consecutive terms $M_{i+1} \subsetneq ? \subsetneq M_i$. By the [[Thm - Isomorphism Theorems for Modules|correspondence theorem]], submodules between $M_{i+1}$ and $M_i$ correspond bijectively to submodules of the quotient $M_i/M_{i+1}$; "nothing strictly between" therefore translates to "$M_i/M_{i+1}$ has no proper non-zero submodule", i.e. **$M_i/M_{i+1}$ is simple**. So "maximal chain" and "chain with simple quotients" are the same condition viewed from two angles, and a *composition series* is either name for it. This is the content that makes the length well-behaved: a maximal chain cannot be sneakily lengthened, so its length is a candidate invariant.

**Why the length is independent of the chain — the Jordan–Hölder phenomenon.** The non-trivial fact, without which "length" would be meaningless, is that *any two* composition series of $M$ have the same length (and indeed the same multiset of simple quotients up to isomorphism and reordering). The reason to believe this is an inheritance/induction argument: define $\ell(M)$ provisionally as the length of the *shortest* composition series; one proves that every proper submodule $N \subsetneq M$ has strictly smaller $\ell$, which forces every maximal chain to have exactly this common length, because at each step the length drops by exactly one. The deep point is that simple quotients are *rigid*: you cannot trade a long detour for a short one, because every refinement of a chain to a composition series produces the same count. This rigidity is what upgrades a choice-dependent construction (pick a chain) into a choice-independent invariant (the length).

**Why finite length is exactly "Noetherian and Artinian", and why both are needed.** A composition series exists if and only if you can both *start* a maximal descending chain and have it *terminate*. Termination of every descending chain at $0$ is the Artinian condition (descending chain condition); the dual requirement, that you cannot refine forever and that the ascending pieces also stop, is the Noetherian condition. Drop Artinian and you may have an infinite descending chain with no bottom (e.g. $\mathbb{Z} \supsetneq 2\mathbb{Z} \supsetneq 4\mathbb{Z} \supsetneq \cdots$): no finite composition series, $\ell = \infty$, even though $\mathbb{Z}$ is Noetherian. Drop Noetherian and you may have an infinite ascending chain with no top (e.g. inside $\mathbb{Z}[\tfrac12]/\mathbb{Z}$): again no finite composition series, $\ell = \infty$, even though that module is Artinian. So **finite length is precisely the conjunction of the two chain conditions** — it is the exact common refinement, the condition under which a module is "finite" in the strongest order-theoretic sense, and this is why length is the invariant that unifies the chapter.

---

# The Definition

Let $R$ be a ring and $M$ an [[Def - Module|R-module]].

## Simple module

A module $S$ is **simple** if $S \neq 0$ and the only [[Def - Submodule|submodules]] of $S$ are $0$ and $S$. Equivalently, $S \cong R/\mathfrak{m}$ for a maximal ideal $\mathfrak{m}$ (when $R$ is commutative): simple modules are the "one-point" modules.

## Composition series

A **composition series** of $M$ is a finite chain of submodules
$$M = M_0 \supsetneq M_1 \supsetneq M_2 \supsetneq \cdots \supsetneq M_n = 0$$
such that each **factor** (or **composition factor**) $M_i/M_{i+1}$ is simple for $0 \leq i < n$. Equivalently, it is a chain of submodules that is **maximal** — it admits no proper refinement, no submodule can be inserted strictly between two consecutive terms. The integer $n$ is the **length** of the series.

## Length

By the **Jordan–Hölder theorem**, if $M$ has a composition series then *all* composition series of $M$ have the same length $n$, and the same multiset of factors $\{M_i/M_{i+1}\}$ up to isomorphism and reordering. This common length is the **length** of $M$, written
$$\ell(M) = \ell_R(M) = n.$$
If $M$ has no composition series, set $\ell(M) = \infty$. By convention $\ell(0) = 0$. The length is finite if and only if $M$ is both [[Def - Noetherian and Artinian Module|Noetherian and Artinian]]; see [[Thm - Length is Additive and Finite iff Noetherian and Artinian]].

---

# Categorical / Structural Definition

In the abelian category of $R$-modules, a composition series exhibits $M$ as built from simple objects by iterated extensions: each inclusion $M_{i+1} \subseteq M_i$ sits in a short exact sequence $0 \to M_{i+1} \to M_i \to M_i/M_{i+1} \to 0$ with simple cokernel. So a finite-length module is precisely an object reachable from the simple objects by finitely many extensions, and length is the number of extensions used. The Jordan–Hölder theorem is the statement that the **simple objects, counted with multiplicity, are an invariant** — the class $[M] = \sum_i [M_i/M_{i+1}]$ is well-defined in the **Grothendieck group** $K_0$ of the category of finite-length modules, which is the free abelian group on isomorphism classes of simple modules. Length is then the homomorphism $K_0 \to \mathbb{Z}$ sending every simple class to $1$, i.e. the total composition-factor count. This is why length is automatically additive on short exact sequences: additivity is built into the definition of $K_0$.

---

# Relate to Other Fields / Compression

The cleanest compression: **length is dimension for modules — the count of simple composition factors, which over a field is the count of one-dimensional factors, i.e. $\dim$.** The whole apparatus is the order-theoretic skeleton of dimension theory, stripped of the vector-space crutch of bases.

**True name:** for problem-solving, the operational meaning of length is **"the number of simple factors in any maximal chain, an additive integer"** — you *use* it by building a composition series and counting, or by splitting a short exact sequence and adding $\ell(N) + \ell(L)$, and you reach for it whenever a quantity should be additive on extensions.

In group theory the exact analogue is the **composition series of a finite group** $G = G_0 \triangleright \cdots \triangleright G_n = 1$ with simple quotients, and the **Jordan–Hölder theorem** there asserting the simple quotients are an invariant; the module version is gentler only because every submodule is automatically normal. In representation theory the composition factors of a module *are* its irreducible constituents, and length-additivity is how characters add. In algebraic geometry, length is the local **multiplicity** — $\ell(\mathcal{O}_{X,x}/I)$ measures the order of vanishing or the intersection multiplicity at a point — and additivity of length is Bézout-type counting. The unifying frame across all of these is that **length counts atoms with multiplicity**, and the atoms are the simple objects of whatever category you are in.

---

# Examples / Corollaries

**Is an instance — a finite-dimensional vector space, $\ell(V) = \dim_k V$.** A composition series of a $k$-vector space $V$ is a maximal flag $V = V_0 \supsetneq V_1 \supsetneq \cdots \supsetneq V_d = 0$ with each $V_i/V_{i+1}$ one-dimensional (hence simple, since a one-dimensional space has no proper non-zero subspace). Any two such flags have length $d = \dim_k V$, so $\ell(V) = \dim_k V$. This is the prototype and the calibration that length generalises dimension.

**Is an instance — $\mathbb{Z}/12$ as a $\mathbb{Z}$-module, $\ell = 3$.** One composition series is $\mathbb{Z}/12 \supsetneq 2\mathbb{Z}/12 \supsetneq 4\mathbb{Z}/12 \supsetneq 0$ wait — better: $\mathbb{Z}/12 \supsetneq (2)/12 \supsetneq (4)/12 \supsetneq 0$ has factors $\mathbb{Z}/2$, $\mathbb{Z}/2$, $\mathbb{Z}/3$. Another is $\mathbb{Z}/12 \supsetneq (3)/12 \supsetneq (6)/12 \supsetneq 0$ with factors $\mathbb{Z}/3$, $\mathbb{Z}/2$, $\mathbb{Z}/2$. Both have length $3$, and the factor multisets agree up to reordering — exactly $12 = 2^2 \cdot 3$ has three prime factors with multiplicity. So $\ell(\mathbb{Z}/n)$ equals the number of prime factors of $n$ counted with multiplicity, illustrating Jordan–Hölder concretely.

**Is NOT an instance (length infinite, Noetherian not Artinian) — $\mathbb{Z}$ as a $\mathbb{Z}$-module.** The module $\mathbb{Z}$ has no composition series: any chain $\mathbb{Z} \supsetneq M_1 \supsetneq \cdots$ has $M_1 = n_1\mathbb{Z}$, and $\mathbb{Z}/n_1\mathbb{Z}$ is simple only if $n_1$ is prime, but then $n_1\mathbb{Z} \supsetneq n_1 q\mathbb{Z} \supsetneq \cdots$ continues forever — the descending chain never reaches $0$. So $\ell(\mathbb{Z}) = \infty$, witnessing that Noetherian alone (which $\mathbb{Z}$ is) does not give finite length; Artinian fails.

**Is NOT an instance (length infinite, Artinian not Noetherian) — $\mathbb{Z}[\tfrac12]/\mathbb{Z}$.** Its submodules $\tfrac{1}{2^n}\mathbb{Z}/\mathbb{Z}$ form an infinite ascending chain with no top, so any attempted composition series cannot terminate at the top: $\ell = \infty$, even though the module is Artinian. The two failures ($\mathbb{Z}$ and $\mathbb{Z}[\tfrac12]/\mathbb{Z}$) together show finite length needs *both* chain conditions.

**Corollary — a simple module has length $1$.** If $S$ is simple, its only composition series is $S \supsetneq 0$, so $\ell(S) = 1$. Conversely $\ell(M) = 1 \iff M$ is simple. This is the calibration that simple modules are the unit of length.

**Calibration check.** Verify that $\ell(\mathbb{Z}/p) = 1$ for $p$ prime (the module is simple) and $\ell(\mathbb{Z}/p^2) = 2$ (the chain $\mathbb{Z}/p^2 \supsetneq p\mathbb{Z}/p^2 \supsetneq 0$ has both factors $\cong \mathbb{Z}/p$). Confirm that $\ell(V) = \dim_k V$ for a finite-dimensional vector space. If you can explain why $\ell(\mathbb{Z}) = \infty$ by exhibiting a non-terminating descending chain, and why finite length requires *both* Noetherian and Artinian, you have understood the definition.

---

# Unlocked by This

> [!tip] Multiplicity and intersection numbers *(from Algebraic Geometry)*
> For a point $x$ on a variety with local ring $\mathcal{O}_{X,x}$, the **length** $\ell(\mathcal{O}_{X,x}/I)$ of a quotient by an ideal is the **multiplicity** — it counts, with the right weighting, how many times a subvariety passes through the point. Bézout's theorem, that two plane curves of degrees $d, e$ meet in $de$ points counted with multiplicity, is additivity of length made geometric. Intersection theory is built on length as the local multiplicity invariant.

> [!tip] The Grothendieck group $K_0$ and characters *(from Representation Theory)*
> The composition factors of a representation are its irreducible constituents, and the class in the **Grothendieck group** $K_0$ records them with multiplicity. Characters are additive on short exact sequences for exactly the Jordan–Hölder reason, so the character of $M$ is the sum of the characters of its composition factors — the foundation of the theory of Brauer characters and decomposition matrices in modular representation theory.

> [!tip] Hilbert–Samuel functions and dimension *(from Commutative Algebra)*
> For a Noetherian local ring $(A, \mathfrak{m})$, the lengths $\ell(A/\mathfrak{m}^n)$ grow like a polynomial in $n$ — the **Hilbert–Samuel polynomial** — whose degree is the Krull dimension of $A$ and whose leading coefficient is the multiplicity. Length is thus the raw material from which dimension theory is built; this is developed in Commutative Algebra XII.
