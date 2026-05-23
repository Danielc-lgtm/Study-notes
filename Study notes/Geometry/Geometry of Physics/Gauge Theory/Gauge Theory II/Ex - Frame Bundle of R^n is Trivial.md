---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Vector Bundle"
  - "Def - The Tangent Bundle"
tags: [geometry, gauge-theory, frame-bundles]
---

# Problem Statement

Show that the frame bundle of the tangent bundle of $\mathbb{R}^n$ is trivial:
$$\mathrm{Fr}(T\mathbb{R}^n) \;\cong\; \mathbb{R}^n \times \mathrm{GL}(n, \mathbb{R})$$
as principal $\mathrm{GL}(n, \mathbb{R})$-bundles over $\mathbb{R}^n$. Exhibit an explicit global section and verify that the induced trivialization is smooth.

**Recall:**

![[Def - Frame Bundle of a Vector Bundle#The Definition]]

![[Def - Vector Bundle#The Definition]]

A vector bundle $E \to M$ is **trivial** iff it admits a global frame (equivalently, $E \cong M \times \mathbb{R}^k$). A principal $G$-bundle is **trivial** iff it admits a global section (equivalently, $P \cong M \times G$).

---

# Convergent Strategy

**Problem class:** This is a *triviality verification* problem — showing a bundle is trivial by exhibiting a global section. The topic-page strategy "construct a global section to detect triviality" applies (Operation 6).

**Assumption pattern:** The key assumption is that $\mathbb{R}^n$ has a *global coordinate system* — the standard Cartesian coordinates $x^1, \ldots, x^n$. This gives globally defined coordinate vector fields $\partial/\partial x^1, \ldots, \partial/\partial x^n$, which form a global frame for $T\mathbb{R}^n$, hence a global section of $\mathrm{Fr}(T\mathbb{R}^n)$.

**Theorem routing:** The Frankel-corollary statement "principal bundle has global section iff trivial" (see [[Thm - Principal Bundles are Locally Trivial via G-Action]], Lemma 4) does the work: produce the section, and the trivialization is automatic.

**Key decision point:** The global coordinate frame is the obvious choice; the only subtle point is verifying the induced trivialization is *smooth* (rather than just continuous).

---

# Legal Operations Used

1. **Operation 6 from the topic page (Construct a global section to detect triviality).** Construct the global section using the coordinate frame on $\mathbb{R}^n$; this immediately gives triviality of $\mathrm{Fr}(T\mathbb{R}^n)$.

2. **Operation 1 from the topic page (Pass between a vector bundle and its frame bundle).** Use the equivalence: $T\mathbb{R}^n$ trivial $\Leftrightarrow$ admits global frame $\Leftrightarrow$ $\mathrm{Fr}(T\mathbb{R}^n)$ admits global section $\Leftrightarrow$ $\mathrm{Fr}(T\mathbb{R}^n)$ trivial.

---

# Hints

> [!note]- Hint 1
> What is the most natural global frame on $T\mathbb{R}^n$?

> [!note]- Hint 2
> A global frame $(\sigma_1, \ldots, \sigma_n)$ of $T\mathbb{R}^n$ is the same data as a global section of $\mathrm{Fr}(T\mathbb{R}^n)$ — namely $p \mapsto (\sigma_1(p), \ldots, \sigma_n(p))$.

> [!note]- Hint 3
> The trivialization $\Phi : \mathbb{R}^n \times \mathrm{GL}(n) \to \mathrm{Fr}(T\mathbb{R}^n)$ is given by $\Phi(p, g) =$ "the frame obtained by transforming the standard frame at $p$ by $g$".

---

# Solution

The proof is short and direct. Step 1 identifies the canonical global frame on $T\mathbb{R}^n$. Step 2 uses it to construct the section of $\mathrm{Fr}(T\mathbb{R}^n)$. Step 3 builds the trivialization via the right $\mathrm{GL}(n)$-action. The non-obvious move is essentially the recognition that $\mathbb{R}^n$ is "globally Euclidean" in a strong sense — it admits a single coordinate system covering everything — which is what gives the global frame.

**Step 1: The standard coordinate frame on $T\mathbb{R}^n$.**

The coordinate vector fields $\partial/\partial x^1, \ldots, \partial/\partial x^n$ form a smooth global frame for $T\mathbb{R}^n$.

> [!note]- Derivation
> $\mathbb{R}^n$ is covered by a single chart (the identity chart $\varphi = \mathrm{id}$), with coordinates $x^1, \ldots, x^n$. The coordinate vector fields $\partial/\partial x^i$ are defined on all of $\mathbb{R}^n$ and are smooth (they are the canonical basis vectors of $T_p\mathbb{R}^n \cong \mathbb{R}^n$ at each point $p$). They are linearly independent at every point — they form a basis of every tangent space — so they form a global frame.

**Step 2: A global section of $\mathrm{Fr}(T\mathbb{R}^n)$.**

The global frame $(\partial/\partial x^1, \ldots, \partial/\partial x^n)$ defines a smooth global section $s : \mathbb{R}^n \to \mathrm{Fr}(T\mathbb{R}^n)$.

> [!note]- Derivation
> Define $s(p) := (\partial/\partial x^1|_p, \ldots, \partial/\partial x^n|_p) \in \mathrm{Fr}(T\mathbb{R}^n)_p$. This is a frame at $p$ by Step 1 (linearly independent), and smoothness follows from the smoothness of the coordinate vector fields. The composition $\pi \circ s$ sends $p$ to $p$ (the projection of the frame at $p$), so $s$ is indeed a section.

**Step 3: The global trivialization.**

The section $s$ together with the right $\mathrm{GL}(n)$-action gives the trivialization $\Phi : \mathbb{R}^n \times \mathrm{GL}(n, \mathbb{R}) \to \mathrm{Fr}(T\mathbb{R}^n)$.

> [!note]- Derivation
> By [[Thm - Principal Bundles are Locally Trivial via G-Action]] (Lemma 3), the section $s$ over $U = \mathbb{R}^n$ gives a global trivialization
> $$\Phi : \mathbb{R}^n \times \mathrm{GL}(n, \mathbb{R}) \to \mathrm{Fr}(T\mathbb{R}^n), \qquad \Phi(p, g) = s(p) \cdot g.$$
> Explicitly, $(\Phi(p, g))_\beta = \sum_\alpha (\partial/\partial x^\alpha)_p \cdot g^\alpha{}_\beta$, the frame at $p$ obtained from the standard frame by applying $g$.
>
> $\Phi$ is smooth (smooth section + smooth right action). It is $\mathrm{GL}(n)$-equivariant: $\Phi(p, gh) = s(p) \cdot (gh) = (s(p) \cdot g) \cdot h = \Phi(p, g) \cdot h$. It is bijective on fibres (a frame at $p$ is $s(p) \cdot g$ for the unique change-of-basis matrix $g$ that takes the standard frame to the given frame). The inverse $\Phi^{-1}$ is smooth as well (computing the change-of-basis matrix is smooth in the frame entries). So $\Phi$ is a diffeomorphism, confirming $\mathrm{Fr}(T\mathbb{R}^n) \cong \mathbb{R}^n \times \mathrm{GL}(n, \mathbb{R})$.

> [!note]- Complete formal solution
> Define the global section $s : \mathbb{R}^n \to \mathrm{Fr}(T\mathbb{R}^n)$ by $s(p) = (\partial/\partial x^1|_p, \ldots, \partial/\partial x^n|_p)$ (Step 1: this is smooth, by smoothness of the coordinate vector fields). The trivialization $\Phi : \mathbb{R}^n \times \mathrm{GL}(n, \mathbb{R}) \to \mathrm{Fr}(T\mathbb{R}^n)$, $\Phi(p, g) = s(p) \cdot g$, is a $\mathrm{GL}(n)$-equivariant diffeomorphism (Step 2: smoothness from smooth section + smooth right action; bijectivity on fibres from freeness + transitivity of the right action). Therefore $\mathrm{Fr}(T\mathbb{R}^n) \cong \mathbb{R}^n \times \mathrm{GL}(n, \mathbb{R})$. ∎

---

# Key Takeaways

**Triviality of $T\mathbb{R}^n$ is the prototype of parallelizability.** A smooth manifold $M$ is **parallelizable** iff $TM$ is trivial — equivalently, iff $\mathrm{Fr}(TM)$ has a global section. Examples: $\mathbb{R}^n$, all Lie groups (left-invariant frames), $T^n$, $S^1$, $S^3 = \mathrm{SU}(2)$, $S^7$. Non-examples: $S^2$ (hairy-ball theorem), $S^{2n}$ for all $n \geq 1$ (Euler characteristic is 2). The Adams theorem (1962) classifies parallelizable spheres exactly: $S^n$ is parallelizable iff $n \in \{1, 3, 7\}$. The trigger-reaction pattern: "is this manifold parallelizable?" → "compute $\chi$; if nonzero, no" (necessary but not sufficient — $T^4$ has $\chi = 0$ and *is* parallelizable, but $S^5$ has $\chi = 0$ and is *not* parallelizable, by Adams).

**Global coordinate systems trivialize all tensor bundles automatically.** Once $\mathbb{R}^n$ has a global frame for $T\mathbb{R}^n$, the same global frame trivializes $T^*\mathbb{R}^n$ (dual frame $dx^1, \ldots, dx^n$), all tensor bundles $\bigotimes^r T\mathbb{R}^n \otimes \bigotimes^s T^*\mathbb{R}^n$, and all density bundles. The pattern: *one global frame on $TM$ trivializes everything functorially associated to $TM$*. This is the differential-geometric advantage of working on $\mathbb{R}^n$ — there are no global obstructions to bundle-theoretic constructions.

**The triviality of $\mathrm{Fr}(T\mathbb{R}^n)$ as a $\mathrm{GL}(n)$-bundle is the simplest case of $G$-structure triviality.** Reductions of $\mathrm{Fr}(T\mathbb{R}^n)$ to subgroups $H \leq \mathrm{GL}(n)$ are unobstructed on $\mathbb{R}^n$ because $\mathbb{R}^n$ is contractible — the principal bundle is trivial, and every smaller-structure-group reduction is also trivial. On non-contractible spaces, the corresponding reductions can be obstructed: spin structures on $M$ are obstructed by $w_2(M) \in H^2(M; \mathbb{Z}/2)$, almost-complex structures on $M^{2n}$ are obstructed by characteristic-class conditions. The "trigger": on a contractible space, every bundle is trivial; this is why local computations on $\mathbb{R}^n$ are always unobstructed.
