---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Stable Model Category"
  - "Def - Chain Map and Chain Homotopy"
  - "Def - Module"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $R$ be a [[Def - Ring|ring]] and let $\mathbf{Ch}(R)$ be the category of [[Def - Chain Map and Chain Homotopy|chain complexes]] of $R$-[[Def - Module|modules]], with the projective model structure (weak equivalences $=$ quasi-isomorphisms). Show that $\mathbf{Ch}(R)$ is a [[Def - Stable Model Category|stable model category]] by establishing:

(a) $\mathbf{Ch}(R)$ is pointed: the zero complex is both initial and terminal.

(b) The suspension on $\mathrm{Ho}(\mathbf{Ch}(R)) = D(R)$ is the degree shift $\Sigma X = X[1]$, with $X[1]_n = X_{n-1}$ and differential $d_{X[1]} = -d_X$.

(c) The shift $X \mapsto X[1]$ is an equivalence of $D(R)$, with inverse $X \mapsto X[-1]$, so $\mathbf{Ch}(R)$ is stable and $D(R)$ is triangulated.

**Recall:**

![[Def - Stable Model Category#The Definition]]

A [[Def - Chain Map and Chain Homotopy|chain complex]] is a sequence $\cdots \to X_{n+1} \xrightarrow{d} X_n \xrightarrow{d} X_{n-1} \to \cdots$ of $R$-modules with $d^2 = 0$. The **derived category** $D(R) = \mathrm{Ho}(\mathbf{Ch}(R))$ is obtained by inverting quasi-isomorphisms (maps inducing isomorphisms on all homology $H_n$). Suspension in a pointed model category is the homotopy cofiber of $X \to 0$.

---

# Convergent Strategy

**Problem class:** This is a "verify stability for a concrete model category" problem — the topic page's strategy of checking the single defining property (invertibility of $\Sigma$) rather than re-deriving any triangulated axioms.

**Assumption pattern:** The resource is the *explicit, algebraic* nature of $\mathbf{Ch}(R)$: the suspension is a literal degree shift, so its invertibility is a one-line check rather than an abstract argument. The zero complex being a zero object (initial $=$ terminal) is what makes $\mathbf{Ch}(R)$ pointed in the first place.

**Theorem routing:** Establish pointedness (so suspension exists); compute the suspension as the degree shift (homotopy cofiber of $X \to 0$); exhibit the explicit inverse $X[-1]$, concluding via the definition of stability that $\mathbf{Ch}(R)$ is stable, and via [[Thm - The Homotopy Category of a Stable Model Category is Triangulated|the main theorem]] that $D(R)$ is triangulated.

**Key decision point:** The non-obvious point is that one must compute the suspension *on the homotopy category* $D(R)$, not naively in $\mathbf{Ch}(R)$ — and that the homotopy cofiber of $X \to 0$ (built from the mapping cone) is quasi-isomorphic to the degree shift $X[1]$. Identifying "homotopy cofiber of $X \to 0$" with "$X[1]$" is the crux.

---

# Legal Operations Used

1. **Operation 4 from the topic page (suspend or desuspend).** This exercise verifies that this operation is legal in $\mathbf{Ch}(R)$ by exhibiting the explicit inverse shift.

2. **Operation 5 from the topic page (replace by a cofiber sequence).** Used to compute the suspension as the homotopy cofiber of $X \to 0$ via the mapping cone.

---

# Hints

> [!note]- Hint 1
> The zero complex $0$ (all modules zero) receives a unique map from every complex and maps uniquely to every complex, so it is both initial and terminal: $\mathbf{Ch}(R)$ is pointed with zero object $0$.

> [!note]- Hint 2
> The suspension is the homotopy cofiber of $X \to 0$, i.e. the mapping cone of $X \to 0$. The mapping cone of the zero map $X \to 0$ is the complex $X$ shifted up by one degree: $C(X \to 0)_n = X_{n-1}$ with differential $-d_X$. That is $X[1]$.

> [!note]- Hint 3
> Shifting up by one degree, $X \mapsto X[1]$, and shifting down by one, $X \mapsto X[-1]$, are visibly mutually inverse functors on $\mathbf{Ch}(R)$ (apply one then the other to return to $X$ on the nose), and both preserve quasi-isomorphisms, so they descend to mutually inverse equivalences of $D(R)$.

---

# Solution

The plan: confirm pointedness, compute the suspension as the degree shift via the mapping cone, then exhibit the inverse shift and conclude stability.

**Step 1: $\mathbf{Ch}(R)$ is pointed.**

> [!note]- Derivation
> The zero complex $0$, with $0_n = 0$ for all $n$, admits exactly one chain map $0 \to X$ and exactly one chain map $X \to 0$ for every complex $X$ (each is zero in every degree). Hence $0$ is both initial and terminal, so it is a **zero object** and $\mathbf{Ch}(R)$ is a pointed model category. The zero morphism $X \to Y$ is the composite $X \to 0 \to Y$.

**Step 2: The suspension is the degree shift $X[1]$.**

> [!note]- Derivation
> In a pointed model category, $\Sigma X$ is the homotopy cofiber of the map $X \to 0$, computed as the mapping cone. The mapping cone of a chain map $h \colon A \to B$ is $C(h)_n = A_{n-1} \oplus B_n$ with differential $\begin{pmatrix} -d_A & 0 \\ -h & d_B \end{pmatrix}$. Taking $h \colon X \to 0$ (so $B = 0$), the cone is $C(h)_n = X_{n-1}$ with differential $-d_X$. This is precisely the degree shift $X[1]$, with $X[1]_n = X_{n-1}$ and $d_{X[1]} = -d_X$. Hence $\Sigma X \simeq X[1]$ in $D(R)$. (Geometrically: crushing $X$ to a point shifts its homology up one degree, $H_n(X[1]) = H_{n-1}(X)$, the algebraic echo of $\Sigma S^n = S^{n+1}$.)

**Step 3: The shift is invertible; $\mathbf{Ch}(R)$ is stable.**

> [!note]- Derivation
> Define $X[-1]_n = X_{n+1}$ with differential $-d_X$. Then $(X[1])[-1]_n = X[1]_{n+1} = X_n$ with differential $(-1)(-1)d_X = d_X$, so $(X[1])[-1] = X$ on the nose, and likewise $(X[-1])[1] = X$. Both functors send quasi-isomorphisms to quasi-isomorphisms (a degree shift relabels homology: $H_n(X[1]) = H_{n-1}(X)$), so they descend to functors on $D(R)$ that are mutually inverse equivalences. Therefore $\Sigma = [1]$ is an equivalence of $D(R)$, which is exactly the definition of stability. By [[Thm - The Homotopy Category of a Stable Model Category is Triangulated|the main theorem]], $D(R)$ is triangulated, with shift $[1]$ and distinguished triangles the mapping-cone sequences.

> [!note]- Complete formal solution
> *Pointed.* The zero complex is initial and terminal, so $\mathbf{Ch}(R)$ has a zero object and is pointed.
>
> *Suspension.* $\Sigma X$ is the homotopy cofiber of $X \to 0$, the mapping cone $C(X \to 0)$, which has $C_n = X_{n-1}$ and differential $-d_X$ — i.e. $\Sigma X = X[1]$, the degree shift, with $H_n(X[1]) = H_{n-1}(X)$.
>
> *Invertibility.* The functor $X \mapsto X[-1]$ (with $X[-1]_n = X_{n+1}$, differential $-d_X$) satisfies $(X[1])[-1] = X = (X[-1])[1]$ on the nose, and both preserve quasi-isomorphisms, hence descend to mutually inverse equivalences of $D(R)$. So $[1]$ is an equivalence of $D(R)$.
>
> By the definition of a stable model category, $\mathbf{Ch}(R)$ is stable; by the main theorem $D(R)$ is triangulated. $\blacksquare$

---

# Key Takeaways

**Stability is checked by one invertibility computation, never by verifying triangulated axioms.** The entire content of "is this model category stable?" is "is $\Sigma$ invertible on $\mathrm{Ho}$?", and for chain complexes that is the trivial observation that a degree shift can be un-shifted. The trigger to install: when asked whether a concrete model category is stable, immediately locate its suspension functor and test invertibility — do not touch TR1–TR4, which the main theorem supplies automatically. This is the cheapest, most reliable route to "triangulated."

**The algebraic suspension is the degree shift, and it is the exact algebraic shadow of topological suspension.** The identity $H_n(X[1]) = H_{n-1}(X)$ mirrors $\widetilde{H}_n(\Sigma A) = \widetilde{H}_{n-1}(A)$ and $\Sigma S^n = S^{n+1}$. Recognizing the degree shift as "suspension" is the bridge that lets every topological intuition about suspension and cofiber sequences transfer verbatim to homological algebra. The transferable diagnostic: whenever a degree shift appears in a chain-complex problem, read it as suspension and expect the long exact sequence machinery to apply.

**$\mathbf{Ch}(R)$ is the calibration example for the whole chapter, because everything is explicit.** Spectra make suspension invertible by an elaborate construction; chain complexes make it invertible by a one-line relabeling, which is why $D(R)$ is the place to build intuition. Every abstract statement of the chapter — cofiber sequences are triangles, the long exact sequence, the octahedral axiom, compact generation by $R$ — has a transparent realization here. When a stable-homotopy statement is confusing, the reflex is to test it in $D(R)$ first, where it becomes ordinary (derived) homological algebra.
