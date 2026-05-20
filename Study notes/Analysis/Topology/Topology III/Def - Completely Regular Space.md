---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Separation Axioms"
  - "Def - Continuous Map"
tags: [analysis, topology]
---

# Notation

$X$ is a topological space. $C \subseteq X$ closed means the complement is open. A map $f : X \to [0, 1]$ is continuous in the usual sense (preimages of opens are open). The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Axiom Motivation

The separation axioms — $T_0, T_1, T_2 = \text{Hausdorff}, T_3 = \text{regular}, T_4 = \text{normal}$ — measure how well a topological space distinguishes its points and closed sets using open sets. Each axiom is *qualitative*: it says we can separate by *open neighborhoods* of one kind or another. But analysis often needs a stronger, *quantitative* form of separation: not just an open set containing $x$ but disjoint from $C$, but a continuous *function* that takes value $0$ at $x$ and $1$ on $C$. The continuous function is the analytic substitute for an indicator: it varies smoothly between $0$ and $1$, can be used to weight, average, or interpolate.

Complete regularity is the axiom that *demands* such functions exist. A Hausdorff space $X$ is completely regular if for every point $x$ and every closed set $C$ not containing $x$, there is a continuous $f : X \to [0, 1]$ with $f(x) = 0$ and $f \equiv 1$ on $C$. This is strictly stronger than regularity (which only asks for disjoint open neighborhoods) and strictly weaker than normality (which asks for separating functions for *any* two disjoint closed sets, not just point-versus-closed).

Why is this the right intermediate level? Because it is exactly what is needed for **embedding into a product of intervals**: the family of all continuous functions $f : X \to [0, 1]$ gives a map $X \to [0, 1]^{C(X, [0,1])}$ by $x \mapsto (f(x))_f$. Complete regularity is exactly the condition for this map to be an *embedding* — injective and a homeomorphism onto its image. So a space is completely regular if and only if it embeds in a product of unit intervals (a Tychonoff space). This is the operational meaning: complete regularity says "the space has enough continuous functions to be coordinatized by them".

The intermediate position between regular and normal is reflected in examples. **Metric spaces** are normal (and hence completely regular). **Locally compact Hausdorff spaces** are completely regular (proved via the one-point compactification, which is compact Hausdorff hence normal, hence has Urysohn functions, which restrict). **Topological groups** are completely regular (a nontrivial theorem). But there exist completely regular spaces that are not normal — they are honest examples showing that the hierarchy is strict. And there exist regular but not completely regular spaces (the Niemytzki tangent disk is a classical example), though these are pathological.

The phrase **$T_{3\frac{1}{2}}$** (Tychonoff) for completely regular reflects the placement: between $T_3$ (regular Hausdorff) and $T_4$ (normal Hausdorff), the fraction $\frac{1}{2}$ acknowledging that the gap is genuine but smaller than the gap from $T_3$ to $T_4$.

What breaks if we strengthen to "$f : X \to [0, 1]$ with $f \equiv 0$ on $C$ and $f \equiv 1$ on $C'$" for two disjoint closed sets? That is the *normality* axiom (in the form of Urysohn's lemma). The strengthening genuinely buys more — Tietze extension, Urysohn's metrization, partitions of unity all need normality. But it excludes some natural examples: there exist completely regular spaces (e.g., the Tychonoff plank) that are not normal.

What breaks if we weaken to "regular" (closed-set separation without functions)? You lose the ability to *embed in $[0, 1]^A$*, which is the key operational tool. Many constructions — Stone–Čech compactification, the Gelfand transform, the duality between locally compact Hausdorff spaces and commutative $C^*$-algebras — require complete regularity, not mere regularity.

---

# The Definition

A topological space $X$ is **completely regular** (or **$T_{3\frac{1}{2}}$**, or **Tychonoff**) if:

1. $X$ is **Hausdorff** ($T_2$): distinct points have disjoint open neighborhoods;
2. For every point $x \in X$ and every closed set $C \subseteq X$ with $x \notin C$, there exists a continuous function $f : X \to [0, 1]$ such that
$$f(x) = 0 \quad \text{and} \quad f \equiv 1 \text{ on } C.$$

(Some sources omit the Hausdorff hypothesis from the definition and add $T_1$ separately; the convention here, following Bredon §9.5, includes Hausdorff in the definition of completely regular.)

An equivalent definition often used: $X$ is **Tychonoff** if it can be embedded as a subspace of a product of unit intervals $[0, 1]^A$ for some index set $A$. The two definitions are equivalent (this is essentially the Tychonoff embedding theorem).

By post-composing the Urysohn function with a continuous map $[0, 1] \to [0, 1]$ that is $0$ on $[0, 1/2]$ and stretches $[1/2, 1]$ to $[0, 1]$, one can additionally arrange that $f \equiv 0$ on a neighborhood of $x$. This strengthened form is often more useful.

---

# Relate to Other Fields / Compression

In **algebraic geometry**, the Zariski topology on $\operatorname{Spec}(R)$ for $R$ a commutative ring is generally *not* completely regular, even when it is $T_0$ — there are not enough continuous real-valued functions on $\operatorname{Spec}(R)$ to separate points from closed sets. This is one of the reasons one studies sheaves of rings rather than continuous functions in algebraic geometry; the topology is too coarse for analysis-style arguments.

In **functional analysis**, the **Gelfand duality** says that the category of compact Hausdorff spaces (which are normal, hence completely regular) is equivalent to the category of commutative $C^*$-algebras. The compact Hausdorff space $X$ corresponds to $C(X)$, its algebra of continuous complex-valued functions. The duality requires complete regularity (in fact, normality) of $X$ to ensure that $C(X)$ has enough functions to recover $X$. The locally compact Hausdorff version (where $C_0(X)$ plays the role) gives a duality with commutative $C^*$-algebras without identity.

In **probability theory**, **Polish spaces** (separable completely metrizable) are completely regular (since metric implies normal implies completely regular). Most of measure-theoretic probability is set in completely regular spaces, where the supply of bounded continuous functions is rich enough to characterize measures (by Riesz representation, or by the Portmanteau theorem for weak convergence).

In **descriptive set theory**, completely regular spaces are the setting for **Borel-measurable functions** to behave well: the bounded continuous functions separate points and closed sets, and Borel sets are generated by closed sets, making everything well-behaved.

---

# Examples / Corollaries

**Is an instance — every metric space.** Metric spaces are normal (a stronger condition), hence completely regular. The explicit Urysohn function is $f(y) = d(y, \{x\})/(d(y, \{x\}) + d(y, C)) = d(x, y)/(d(x, y) + d(y, C))$, which is $0$ at $x$ and $1$ on $C$ (where $d(y, C)$ vanishes).

**Is an instance — every locally compact Hausdorff space.** Given $x$ and closed $C$ with $x \notin C$, find a compact neighborhood $K$ of $x$ disjoint from $C$ (possible by local compactness and Hausdorff). The one-point compactification $K^+$ is compact Hausdorff, hence normal, so Urysohn's lemma gives a continuous $g : K^+ \to [0, 1]$ with $g(x) = 0$ and $g \equiv 1$ on $\{\infty\} \cup (K^+ \setminus K)$. Restrict to $X$, extending by $1$ on $X \setminus K$, and the result is continuous. So LCH spaces are completely regular — see [[Thm - LCH Implies Completely Regular]].

**Is an instance — every topological group.** A topological group $G$ admits a continuous "almost-distance" $f$ separating any point from any closed set not containing it, constructed via the group operation and an arbitrary nontrivial neighborhood of the identity. The proof uses left translations and convolution-like arguments.

**Is NOT an instance — the Sierpiński space $\{0, 1\}$ with topology $\{\emptyset, \{1\}, \{0, 1\}\}$.** This is not even $T_1$ (the point $0$ is not closed), let alone Hausdorff or completely regular. It has no continuous map to $[0, 1]$ separating $1$ from the closed set $\{0\}$, because any such map would be locally constant (the only continuous maps from Sierpiński to $[0, 1]$ are constants and step functions, and a step function would require an open set whose preimage equals the open subset $\{1\}$, which already has closure equal to the whole space).

**Is NOT an instance — generic Zariski topology.** $\operatorname{Spec}(\mathbb{Z})$ with the Zariski topology is $T_0$ but not Hausdorff (the generic point is in the closure of every nonempty closed set), hence not completely regular.

**Corollary — subspaces of completely regular are completely regular.** If $X$ is completely regular and $A \subseteq X$, then $A$ is completely regular: separating functions on $X$ restrict to separating functions on $A$ (a closed set in $A$ is the intersection of $A$ with a closed set in $X$, with appropriate manipulation).

**Corollary — products of completely regular are completely regular.** If each $X_\alpha$ is completely regular, $\prod_\alpha X_\alpha$ is completely regular. Given $(x_\alpha)$ and closed $C$ not containing it, find a basic open neighborhood $\prod V_\alpha$ of $(x_\alpha)$ disjoint from $C$, where $V_\alpha = X_\alpha$ for cofinitely many $\alpha$; use complete regularity on the finite remaining coordinates to build the separating function.

**Corollary — embedding into $[0, 1]^A$.** A space $X$ is completely regular if and only if it embeds in some product $[0, 1]^A$ for some index set $A$ (the **Tychonoff embedding theorem**). The map is $\Phi : X \to [0, 1]^{C(X, [0, 1])}$, $\Phi(x)(f) = f(x)$, and complete regularity is exactly what makes $\Phi$ a homeomorphism onto its image.

**Calibration check.** Verify: (i) every compact Hausdorff space is completely regular (compact Hausdorff implies normal implies completely regular); (ii) $\mathbb{R}^n$ is completely regular; (iii) the Tychonoff plank — the product $[0, \omega_1] \times [0, \omega]$ minus the corner $(\omega_1, \omega)$ — is completely regular but not normal (a classical exercise; both products are compact Hausdorff hence completely regular, so a product is completely regular, but the deleted version fails normality); (iv) the **Stone–Čech compactification** $\beta X$ exists for $X$ if and only if $X$ is completely regular — see [[Thm - Stone–Čech Compactification]].

---

# Unlocked by This

> [!tip] Stone–Čech Compactification *(from this topic)*
> A completely regular space $X$ has a unique (up to homeomorphism) compactification $\beta X$ — the **Stone–Čech compactification** — characterized by a universal property: every bounded continuous $f : X \to \mathbb{R}$ extends uniquely to $\beta X$. The construction embeds $X$ in $[0, 1]^{C_b(X)}$ and takes the closure; complete regularity makes the embedding faithful. See [[Thm - Stone–Čech Compactification]].

> [!tip] Tychonoff Embedding Theorem *(from this topic)*
> Completely regular spaces are exactly the **subspaces of products of intervals**. This is the topological characterization that justifies the alternative name "Tychonoff space".

> [!tip] Gelfand Duality *(from Functional Analysis)*
> The category of compact Hausdorff spaces is equivalent to the category of commutative unital $C^*$-algebras, via $X \leftrightarrow C(X)$. Complete regularity is the "enough functions" condition that makes the duality possible; the locally compact version uses $C_0(X)$ and complete regularity of LCH spaces.
