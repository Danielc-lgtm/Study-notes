---
type: topic
subject: algebraic-topology
chapter: "Frankel §21.2 + Hatcher Ch 1"
title: "Algebraic Topology II — Fundamental Group and Covering Spaces"
tags: [geometry, algebraic-topology, topology]
---

# Notation Registry

Throughout this topic, $X$, $Y$ denote topological spaces, assumed connected and locally path-connected unless stated otherwise. **A "space" means a sufficiently nice space** — Hausdorff, path-connected, locally path-connected, and **semi-locally simply connected** when covering-space constructions appear. These are the standing assumptions under which $\pi_1$ has a clean theory and a universal cover exists. Frankel works in this regime by default (his "manifolds" are even smoother), and we follow him. When a result needs strictly less or strictly more, the local convention is noted on the relevant subpage.

- $I = [0,1] \subset \mathbb{R}$ — the unit interval, the parameter space for paths
- $\gamma, \alpha, \beta : I \to X$ — paths; $\gamma(0)$ is the **start** and $\gamma(1)$ the **end**
- $\gamma_1 \cdot \gamma_2$ — the path-product (concatenation): traverse $\gamma_1$ at double speed on $[0, \tfrac12]$, then $\gamma_2$ at double speed on $[\tfrac12, 1]$
- $\gamma^{-1}(t) := \gamma(1-t)$ — the **reverse** of a path
- $c_{x_0}$ — the constant path at $x_0$, $c_{x_0}(t) = x_0$ for all $t$
- $\gamma_1 \simeq \gamma_2$ (rel endpoints) — $\gamma_1$ is path-homotopic to $\gamma_2$ via a homotopy fixing $\gamma_1(0) = \gamma_2(0)$ and $\gamma_1(1) = \gamma_2(1)$
- $[\gamma]$ — the homotopy class of $\gamma$ rel endpoints
- $\pi_1(X, x_0)$ — the **fundamental group** of $X$ at base point $x_0$: classes of loops $\gamma : I \to X$ with $\gamma(0) = \gamma(1) = x_0$, multiplied by path-product
- $\pi_1(X)$ — the fundamental group up to base-point isomorphism, when $X$ is path-connected
- $f_* : \pi_1(X, x_0) \to \pi_1(Y, f(x_0))$ — the induced homomorphism of a continuous map $f : X \to Y$, $f_*[\gamma] := [f \circ \gamma]$
- $p : \tilde X \to X$ — a **covering map**; $\tilde X$ is the **covering space** (sometimes "total space"), $X$ the **base**
- $p^{-1}(x_0)$ — the **fibre** over $x_0$, a discrete subset of $\tilde X$
- $\tilde\gamma$ — the **lift** of a path $\gamma$ in $X$ to $\tilde X$ (uniquely determined by a chosen starting point in the fibre)
- $\widetilde X$ or $X^{\mathrm{univ}}$ — the **universal cover** of $X$ (simply connected; exists when $X$ is semi-locally simply connected)
- $\mathrm{Deck}(\tilde X / X)$ — the group of **deck transformations** (covering transformations): homeomorphisms $\varphi : \tilde X \to \tilde X$ with $p \circ \varphi = p$
- $F_n = \langle a_1, \dots, a_n \rangle$ — the **free group** on $n$ generators
- $G \ast H$ — the **free product** of groups $G$ and $H$
- $S^n$ — the $n$-sphere; $T^n = (S^1)^n$ — the $n$-torus; $\mathbb{RP}^n$ — real projective $n$-space
- $\mathrm{Ric}(v, v)$ — the Ricci curvature in direction $v$ (for the Myers theorem section); see [[Riemannian Geometry III — Riemann Curvature and Topology]]

---

# Motivation

A topological space looks the same up to small perturbation, and the central problem of topology is to find invariants that survive those perturbations and yet distinguish spaces that ought to be distinguished. Homotopy is the right notion of perturbation: a continuous deformation, taking time. The **fundamental group** $\pi_1(X, x_0)$ is the first non-trivial homotopy invariant — it asks, of every loop based at $x_0$, whether it can be continuously shrunk to the constant loop, and if not, what its "winding type" is. A disc has only one type (everything contracts), a circle has $\mathbb{Z}$-many (one for each integer winding), a figure-eight has a free group on two generators (one for each way of weaving the two loops). $\pi_1$ is the smallest invariant that detects the difference between these.

Two facts make $\pi_1$ exceptionally useful. First, it is **functorial**: every continuous map $f : X \to Y$ induces a group homomorphism $f_* : \pi_1(X, x_0) \to \pi_1(Y, f(x_0))$, so any continuous-map question becomes a group-theory question on $\pi_1$. The proof that $\mathbb{R}^2 \not\cong \mathbb{R}^3$ comes out of nowhere with $\pi_1$ in hand: $\mathbb{R}^2 \setminus \{0\}$ has $\pi_1 = \mathbb{Z}$, but $\mathbb{R}^3 \setminus \{0\}$ has $\pi_1 = 0$, so a homeomorphism cannot exist. Second, $\pi_1$ classifies a geometric structure: connected **covering spaces** of $X$ correspond bijectively to subgroups of $\pi_1(X)$, and the universal cover is the simply-connected total space sitting at the top of the lattice. This is the Galois correspondence of topology, and it lets one compute $\pi_1$ by constructing covers and conversely build covers by inspecting subgroups.

The structural backbone of the topic is the bidirection between $\pi_1$ and covers:
$$
\boxed{\;\{\text{connected covers of } X\} \;\longleftrightarrow\; \{\text{subgroups of } \pi_1(X)\}\;}
$$
with normal subgroups corresponding to **regular** (Galois) covers, the trivial subgroup to the **universal cover**, and the deck group of the universal cover being $\pi_1(X)$ itself. Everything we prove — path lifting, the lifting criterion, the computation $\pi_1(S^1) = \mathbb{Z}$, the universal-covering-group construction for Lie groups, even Myers' theorem ($\mathrm{Ric} > 0 \Rightarrow \pi_1$ finite) — falls naturally on one side or the other of this correspondence.

The reader is assumed to have a working command of point-set topology — continuous maps, homeomorphisms, connectedness, path-connectedness, compactness, the Hausdorff property (refresh from [[Def - Continuous Map]], [[Def - Homeomorphism]], [[Def - Connected Space]], [[Def - Path-Connected Space]], [[Def - Compact Space]], [[Def - Separation Axioms]]) — and elementary group theory: groups, subgroups, normal subgroups, quotients, homomorphisms, kernels and images (refresh from [[Def - Group]], [[Def - Subgroup]], [[Def - Normal Subgroup]], [[Def - Homomorphism]], [[Def - Kernel and Image]], [[Def - Quotient Group]]). Familiarity with [[Def - Smooth Manifold|smooth manifolds]] and [[Def - Lie Group|Lie groups]] (DG I–XI) is helpful but not essential — the topic is purely topological; the Lie-group and Riemannian applications come at the end.

---

# Concept Map

## §2.1 The Fundamental Group

- **[[Def - Homotopy of Paths]]**
	- Two paths $\gamma_0, \gamma_1 : I \to X$ with the same start and end are **path-homotopic** if there is a continuous map $H : I \times I \to X$ with $H(s,0) = \gamma_0(s)$, $H(s,1) = \gamma_1(s)$, and the endpoints are fixed along the homotopy: $H(0,t) = \gamma_0(0)$ and $H(1,t) = \gamma_0(1)$ for all $t$. This is an equivalence relation on paths, and the homotopy class is denoted $[\gamma]$. The key picture is a square whose left and right edges are constant at the endpoints and whose top and bottom are the two paths.

- **[[Def - Path-Product and the Fundamental Group]]**
	- The **path-product** $\gamma_1 \cdot \gamma_2$ (defined when $\gamma_1(1) = \gamma_2(0)$) traverses $\gamma_1$ at double speed on $[0, \tfrac12]$ and $\gamma_2$ at double speed on $[\tfrac12, 1]$. On homotopy classes of *loops* at a fixed base point $x_0$, this product is well-defined, associative up to homotopy, with the constant loop $c_{x_0}$ as identity and the reverse loop $\gamma^{-1}$ as inverse. The resulting group is $\pi_1(X, x_0)$ — the **fundamental group**.

- **[[Thm - The Fundamental Group is a Group]]**
	- The path-product on homotopy classes of based loops satisfies all the group axioms. Associativity is a reparameterization homotopy that slides bracketings continuously into each other. The constant loop is a two-sided identity by another reparameterization. The reverse $\gamma^{-1}$ is a two-sided inverse via the "fold" homotopy that collapses $\gamma \cdot \gamma^{-1}$ to the constant by sliding the midpoint outwards. The proof is entirely elementary — every homotopy is given by an explicit formula on the unit square.

- **[[Def - Simply Connected Space]]**
	- A space $X$ is **simply connected** if it is path-connected and $\pi_1(X, x_0) = \{1\}$ for some (equivalently, any) base point $x_0$. Equivalently, every loop is null-homotopic, or any two paths with the same endpoints are path-homotopic. Examples: $\mathbb{R}^n$, every convex set, every contractible space, $S^n$ for $n \geq 2$, $\mathrm{SU}(n)$ for $n \geq 1$. Non-examples: $S^1$, $T^n$, $\mathbb{RP}^n$ for $n \geq 1$, the figure-eight.

- **[[Thm - Pi_1 of S^1 is Z]]**
	- The fundamental group of the circle is the integers, $\pi_1(S^1, 1) \cong \mathbb{Z}$, with the integer $n$ corresponding to the loop $\theta \mapsto e^{2\pi i n\theta}$ that winds $n$ times. The proof lifts loops to $\mathbb{R}$ via the covering $p(t) = e^{2\pi i t}$: a loop's lift starts at $0$ and ends at an integer (the **winding number**), which is a well-defined homotopy invariant and a group homomorphism. This is the flagship computation of the chapter — once you have $\pi_1(S^1) = \mathbb{Z}$, the entire topology of plane curves, the no-retraction theorem, and the Brouwer fixed-point theorem in dimension 2 follow.

- **[[Ex - Pi_1 of the Torus is Z Squared]]** (⭐⭐)
	- Compute $\pi_1(T^2) = \mathbb{Z}^2$ by combining $\pi_1(S^1) = \mathbb{Z}$ with the product formula $\pi_1(X \times Y) = \pi_1(X) \times \pi_1(Y)$ (proved via projection-and-paste).

- **[[Ex - Pi_1 of a Topological Group is Abelian]]** (⭐⭐)
	- Show that for any topological group $G$ with identity $e$ taken as base point, $\pi_1(G, e)$ is abelian. The key trick: pointwise multiplication of loops gives a second, automatically commutative, product on $\pi_1$, and the **Eckmann-Hilton argument** forces it to agree with the path-product. Consequence: $\pi_1$ of every Lie group is abelian.

> [!tip] Unlocked: Singular Homology and the Hurewicz Theorem *(from Algebraic Topology I)*
> The fundamental group $\pi_1$ is the first homotopy group; **singular homology** $H_1$ is the first homology group, computed from chains and boundaries instead of loops and homotopies. The **Hurewicz theorem** states that for a path-connected space, $H_1(X; \mathbb{Z}) \cong \pi_1(X)^{\mathrm{ab}}$ — the abelianization of $\pi_1$. So $H_1$ is "$\pi_1$ that has forgotten how to be non-commutative". For higher dimensions the higher homotopy groups [[Algebraic Topology III — Higher Homotopy and Chern Forms|$\pi_k$]] map similarly to $H_k$, and the Hurewicz map is an iso in the lowest non-zero degree — see [[Algebraic Topology I — Singular Homology and the de Rham Theorem]].

> [!note] Exercise Index — §2.1
> [[Exercise Index - §2.1 The Fundamental Group]]

## §2.2 Covering Spaces and Lifting

- **[[Def - Covering Space]]**
	- A continuous map $p : \tilde X \to X$ is a **covering map** if every $x \in X$ has an open neighbourhood $U$ — called **evenly covered** — such that $p^{-1}(U)$ is a disjoint union of open sets in $\tilde X$, each mapped homeomorphically onto $U$ by $p$. Examples: $\mathbb{R} \to S^1$ via $t \mapsto e^{2\pi i t}$, $S^n \to \mathbb{RP}^n$ via the antipodal quotient, $\mathbb{R}^n \to T^n$ via componentwise exponentials, $\mathrm{SU}(2) \to \mathrm{SO}(3)$ via the spin double cover. The fibre $p^{-1}(x)$ is a discrete set of constant cardinality (the number of "sheets").

- **[[Def - Lift of a Map]]**
	- A **lift** of a continuous map $f : Y \to X$ through a covering $p : \tilde X \to X$ is a continuous $\tilde f : Y \to \tilde X$ with $p \circ \tilde f = f$. Lifts are the natural way to factor a map through a cover: instead of $f$ landing in the base, it lands in the bigger total space. Whether a lift exists, and whether it is unique, are exactly the questions Path Lifting, Homotopy Lifting, and the Lifting Criterion answer.

- **[[Thm - Path Lifting and Homotopy Lifting]]**
	- For a covering $p : \tilde X \to X$, every path $\gamma : I \to X$ and every choice of starting lift $\tilde x_0 \in p^{-1}(\gamma(0))$ determines a unique lift $\tilde\gamma : I \to \tilde X$ with $\tilde\gamma(0) = \tilde x_0$. The same holds for homotopies: a homotopy $H : I \times I \to X$ lifts uniquely once an initial lift is specified. The proof is local (chop the interval into small enough pieces that each lands in an evenly covered set) and glues by the local homeomorphism. This is the lemma that makes everything else go: it lets you transport algebraic structure on loops to algebraic structure on lifts.

- **[[Thm - Lifting Criterion for Continuous Maps]]**
	- For a covering $p : \tilde X \to X$ and a continuous map $f : Y \to X$ from a connected, locally path-connected space $Y$, a lift $\tilde f : Y \to \tilde X$ with $\tilde f(y_0) = \tilde x_0$ exists **if and only if** $f_*(\pi_1(Y, y_0)) \subseteq p_*(\pi_1(\tilde X, \tilde x_0))$. The condition says the loops of $Y$, after being pushed forward to $X$, must already be representable by loops in $\tilde X$. When it holds, the lift is unique. This is the master existence theorem for lifts.

- **[[Ex - SU(2) is the Universal Cover of SO(3)]]** (⭐⭐)
	- Show that the spin double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$, sending a unit quaternion $q$ to conjugation by $q$ on the pure imaginaries $\mathbb{R}^3 \cong \mathrm{Im}\,\mathbb{H}$, is a 2-sheeted covering map and a group homomorphism. Conclude $\pi_1(\mathrm{SO}(3)) = \mathbb{Z}/2$, since $\mathrm{SU}(2) \cong S^3$ is simply connected.

- **[[Ex - The Orientable Double Cover of the Möbius Strip]]** (⭐)
	- Construct explicitly the 2-sheeted orientation cover of the Möbius strip $M$ — it is a cylinder $S^1 \times I$, and the covering map identifies antipodal points "after one full loop". This is the toy model for the general orientable double cover.

> [!tip] Unlocked: The Fibration Long Exact Sequence *(from Algebraic Topology III)*
> A covering map is a special **fibre bundle** with discrete fibre. For a general fibre bundle $F \hookrightarrow E \to B$ there is a long exact sequence of homotopy groups $\cdots \to \pi_n(F) \to \pi_n(E) \to \pi_n(B) \to \pi_{n-1}(F) \to \cdots$ that generalises path-lifting to all dimensions. For covers, $F$ is discrete so $\pi_n(F) = 0$ for $n \geq 1$, and the sequence collapses to $\pi_n(\tilde X) \cong \pi_n(X)$ for $n \geq 2$ and the short exact sequence $0 \to \pi_1(\tilde X) \to \pi_1(X) \to F \to 0$ for regular covers. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

> [!note] Exercise Index — §2.2
> [[Exercise Index - §2.2 Covering Spaces and Lifting]]

## §2.3 The Galois Correspondence

- **[[Def - Universal Cover]]**
	- The **universal cover** $\widetilde X \to X$ is a simply-connected covering space. It exists when $X$ is path-connected, locally path-connected, and **semi-locally simply connected** (every point has a neighbourhood in which loops are null-homotopic in $X$). It is unique up to isomorphism of covers, and it covers every other connected cover of $X$ — hence "universal". For $S^1$ it is $\mathbb{R}$; for $T^n$ it is $\mathbb{R}^n$; for $\mathbb{RP}^n$ ($n \geq 2$) it is $S^n$.

- **[[Def - Deck Transformation Group]]**
	- For a cover $p : \tilde X \to X$, a **deck transformation** is a homeomorphism $\varphi : \tilde X \to \tilde X$ commuting with $p$ (i.e., $p \circ \varphi = p$). Deck transformations form a group $\mathrm{Deck}(\tilde X / X)$ under composition, permuting each fibre. For the universal cover, $\mathrm{Deck}(\widetilde X / X) \cong \pi_1(X)$ — this is one of the most beautiful identifications in the subject, and it is what lets you recover $\pi_1$ from the symmetries of the universal cover.

- **[[Def - Regular (Galois) Covering]]**
	- A cover $p : \tilde X \to X$ is **regular** (or **Galois**, or **normal**) if its deck group acts transitively on each fibre. Equivalently, the subgroup $p_*(\pi_1(\tilde X)) \leq \pi_1(X)$ is normal. Regular covers are the "symmetric" ones, with the deck group acting like a Galois group: the quotient $\pi_1(X) / p_*(\pi_1(\tilde X))$ is then the deck group. The universal cover is the largest regular cover (trivial subgroup is normal), the identity cover is the smallest.

- **[[Thm - Galois Correspondence for Covering Spaces]]**
	- For a path-connected, locally path-connected, semi-locally simply connected $X$ with universal cover $\widetilde X$, there is a bijection between (i) **connected covers** of $X$ up to base-point-preserving isomorphism and (ii) **subgroups** of $\pi_1(X, x_0)$, given by $(p : \tilde X \to X, \tilde x_0) \mapsto p_*(\pi_1(\tilde X, \tilde x_0))$. Under this bijection, normal subgroups correspond to **regular covers**, the trivial subgroup to the **universal cover**, and the full group to $X$ itself. This is *the* structural theorem of the topic.

- **[[Def - Free Group and Free Product]]**
	- The **free group** $F_n$ on $n$ generators $a_1, \dots, a_n$ is the group whose elements are reduced words in the $a_i$ and their inverses — no relations whatsoever beyond what the group axioms force. The **free product** $G \ast H$ is the analogous construction for two groups: alternating products of elements from $G$ and $H$, no relations except those within $G$ and within $H$. Both are universal: a homomorphism out of $F_n$ is determined by where the generators go, freely. The wedge of $n$ circles has $\pi_1 = F_n$, and the wedge of any two spaces $X \vee Y$ has $\pi_1 = \pi_1(X) \ast \pi_1(Y)$ (under mild hypotheses).

- **[[Thm - Seifert-van Kampen Theorem (Statement)]]**
	- If $X = U \cup V$ with $U, V, U \cap V$ all open and path-connected, and $x_0 \in U \cap V$, then $\pi_1(X, x_0) \cong \pi_1(U, x_0) \ast_{\pi_1(U \cap V, x_0)} \pi_1(V, x_0)$ — the amalgamated free product. In plain language: $\pi_1(X)$ is generated by loops in $U$ and loops in $V$, subject to the relations forced by loops in $U \cap V$ (the same loop, viewed in $U$ and in $V$, must give the same class). This is the computational engine — almost every $\pi_1$ computation goes through it.

- **[[Ex - The Universal Cover of the Figure-Eight is the Cayley Graph of F_2]]** (⭐⭐⭐)
	- Show that the universal cover of the figure-eight $S^1 \vee S^1$ is the infinite 4-valent tree, which is precisely the Cayley graph of the free group $F_2 = \langle a, b \rangle$ with the generators as edge labels. The deck group acts on this tree as $F_2$, recovering $\pi_1(S^1 \vee S^1) = F_2$.

> [!tip] Unlocked: The Étale Fundamental Group *(from Algebraic Geometry)*
> Grothendieck observed that the Galois correspondence has nothing essentially topological about it: replace "covering spaces" with **étale covers** (finite, unramified, "covering-like" morphisms) of an algebraic variety or scheme, replace "deck transformations" with field-theoretic automorphisms, and you get the **étale fundamental group** $\pi_1^{\mathrm{ét}}(X, \bar x)$, a profinite group that classifies finite étale covers of $X$. For $X = \mathrm{Spec}\,\mathbb{Q}$ this profinite group is the absolute Galois group of $\mathbb{Q}$ — Galois theory and covering-space theory are two specialisations of a single phenomenon. Further generalisations lead to **Bass-Serre theory** for groups acting on trees and **HNN extensions** as an algebraic analogue of attaching a 1-cell to a circle.

> [!note] Exercise Index — §2.3
> [[Exercise Index - §2.3 The Galois Correspondence]]

## §2.4 Applications: Orientability, Lie Groups, and Riemannian Geometry

- **[[Def - Orientable Double Cover]]**
	- For a connected manifold $M$ (smooth or topological), the **orientable double cover** $\widetilde M^{\mathrm{or}} \to M$ is the 2-sheeted cover whose fibre over $x$ is the two local orientations of $M$ at $x$, glued together using the orientation-preserving status of paths. It is always orientable, and it is connected if and only if $M$ is non-orientable. For the Möbius strip $M$, $\widetilde M^{\mathrm{or}}$ is the cylinder; for the Klein bottle, it is the torus; for $\mathbb{RP}^n$, it is $S^n$.

- **The universal covering group.**
	- For a connected Lie group $G$, the universal cover $\widetilde G$ inherits a canonical Lie-group structure such that the covering map $p : \widetilde G \to G$ is a Lie-group homomorphism with discrete kernel $\ker p \cong \pi_1(G)$ (a central subgroup, since $\pi_1$ of a [[Def - Lie Group|Lie group]] is abelian — see [[Ex - Pi_1 of a Topological Group is Abelian]]). The fundamental example: $\mathrm{SU}(2) \cong S^3$ is the universal cover of $\mathrm{SO}(3) \cong \mathbb{RP}^3$, with $\pi_1(\mathrm{SO}(3)) = \mathbb{Z}/2$ (see [[Ex - SU(2) is the Universal Cover of SO(3)]]). This unlocks **spinors**: the spin representations of $\mathfrak{so}(n)$ exponentiate not to $\mathrm{SO}(n)$ but to $\mathrm{Spin}(n) = \widetilde{\mathrm{SO}(n)}$. See [[Spinors and the Dirac Equation]].

- **[[Thm - Myers Theorem (Pi_1 Finite for Positive Ricci)]]**
	- Let $M^n$ be a complete connected Riemannian manifold with Ricci curvature bounded below by $\mathrm{Ric}(v,v) \geq (n-1)\kappa > 0$ for all unit $v$. Then $M$ is compact, has diameter $\leq \pi/\sqrt{\kappa}$, and its **fundamental group $\pi_1(M)$ is finite**. The proof: lift the metric to the universal cover $\widetilde M$, which inherits the same Ricci lower bound, conclude $\widetilde M$ is also compact (diameter bound), and observe that a compact covering of a compact manifold must be finite-sheeted. This is the headline application of $\pi_1$ to Riemannian geometry. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

- **[[Ex - Pi_1 of RP^n is Z over 2 for n at least 2]]** (⭐⭐)
	- Compute $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$ for $n \geq 2$ using the antipodal double cover $S^n \to \mathbb{RP}^n$ and the fact that $S^n$ is simply connected for $n \geq 2$. The non-trivial loop is a "great half-circle" in $\mathbb{RP}^n$, joining antipodal points of $S^n$; its square lifts to a closed loop and is null-homotopic.

- **[[Ex - The Brouwer Fixed Point Theorem in Dimension 2 via Pi_1]]** (⭐⭐)
	- Use $\pi_1(S^1) = \mathbb{Z}$ to prove that every continuous map $f : D^2 \to D^2$ from the closed disc to itself has a fixed point. The classical argument: assume no fixed point and construct a retraction $D^2 \to S^1$; apply $\pi_1$ to derive $\mathbb{Z} = 0$, contradiction.

> [!tip] Unlocked: Synge's Theorem and the Mapping Class Group *(from Riemannian Geometry / Geometric Topology)*
> Myers' theorem is one of several **curvature-controls-topology** results. Synge's theorem refines it: a compact even-dimensional orientable manifold with strictly positive sectional curvature is *simply* connected (not merely finite $\pi_1$) — see [[Riemannian Geometry III — Riemann Curvature and Topology]]. **Cartan-Hadamard** goes the other way: non-positive sectional curvature implies the universal cover is diffeomorphic to $\mathbb{R}^n$. A different downstream subject — the **mapping class group** $\mathrm{MCG}(\Sigma_g)$ of a surface — packages $\pi_0$ of the homeomorphism group, and is closely tied to outer automorphisms of $\pi_1(\Sigma_g)$. Both Synge and Cartan-Hadamard, and the mapping class group, build on the basic Galois correspondence here.

> [!note] Exercise Index — §2.4
> [[Exercise Index - §2.4 Applications]]

---

# Sources and Targets

**Targets — What do we usually try to prove?**

Most problems in this topic chase one of five targets. First, **computing $\pi_1(X)$ for a specific space** — write it as a free group, a quotient by relations, or recognise it as $\mathbb{Z}^n$, $\mathbb{Z}/k$, the free product of pieces. Second, **deciding whether a continuous map exists** between two spaces, typically by an obstruction argument on $\pi_1$ (no continuous retraction $D^2 \to S^1$, no homeomorphism $\mathbb{R}^2 \cong \mathbb{R}^3$). Third, **constructing or classifying covers** of a given space, via subgroups of $\pi_1$. Fourth, **proving a space is simply connected** — usually by exhibiting a contraction, a covering by simply-connected pieces, or showing it is the universal cover of something. Fifth, **deriving topological constraints from geometric data**, the Myers and Synge style: $\mathrm{Ric} > 0$, $\sec > 0$, $\sec \leq 0$ each force $\pi_1$ to look a certain way.

**Sources — What assumptions do we usually leverage?**

The recurring assumptions are equally stereotyped. **A covering map is given** — instantly opens path lifting, homotopy lifting, and the Galois correspondence; the covering reduces $\pi_1$ questions about the base to *simpler* questions about the cover, often a simply-connected one. **A simply-connected space is in sight** — every loop contracts, all lifts of homotopic paths land at the same endpoint, and the universal cover, if available, makes $\mathrm{Deck} \cong \pi_1$. **A group action by homeomorphisms on a simply-connected space** with appropriate freeness/properness — produces a covering and identifies $\pi_1$ of the quotient with the group. **A topological group structure** is in sight — forces $\pi_1$ to be abelian via the Eckmann-Hilton argument. **A Riemannian metric with curvature bound** is given — feeds Myers, Synge, Cartan-Hadamard, all of which translate metric inequalities into $\pi_1$ structure. The recurring move is to find which source is hidden in the problem (a covering map masquerading as a quotient map, a topological group structure visible only after you notice the space is $\mathrm{SO}(3)$, a curvature bound that promises compactness) and route it through the appropriate theorem.

---

# Legal Operations

The moves below are the workhorses for problems in this topic. When stuck, scan the list and try each in turn. Each is self-contained: nothing assumes prior topology background beyond the standing conventions.

**Legal operations:**

1. **Lift a path through a covering.** Given a covering $p : \tilde X \to X$, a path $\gamma$ in $X$, and a choice of starting lift $\tilde x_0 \in p^{-1}(\gamma(0))$, there is a unique lift $\tilde\gamma$ in $\tilde X$ starting at $\tilde x_0$ ([[Thm - Path Lifting and Homotopy Lifting]]). *Trigger:* a covering map and a loop or path in the base. *Pattern:* "the lift of a loop is a path from $\tilde x_0$ to some other point in the fibre — the endpoint records information about the loop's class in $\pi_1$."

2. **Lift a homotopy through a covering.** Same theorem, applied to a homotopy $H : I \times I \to X$ with a chosen initial lift on the bottom edge: $H$ lifts uniquely. *Trigger:* a homotopy in the base together with a covering map. *Pattern:* "homotopic paths in the base lift to paths in $\tilde X$ with the *same* endpoint" — the essential well-definedness lemma for $\pi_1$-invariants.

3. **Apply the lifting criterion.** To decide whether a continuous map $f : Y \to X$ lifts through a covering $p : \tilde X \to X$, check whether $f_*\pi_1(Y) \subseteq p_*\pi_1(\tilde X)$ ([[Thm - Lifting Criterion for Continuous Maps]]). *Trigger:* asked whether a continuous map factors through a cover, or asked to construct one. *Pattern:* the condition becomes trivial when $Y$ is simply connected — any map from a simply-connected space lifts through any cover.

4. **Identify the fundamental group of a quotient via covering.** If a group $\Gamma$ acts freely and properly discontinuously on a simply-connected space $\tilde X$ by homeomorphisms, then $\tilde X \to \tilde X / \Gamma$ is a covering with deck group $\Gamma$, and $\pi_1(\tilde X/\Gamma) \cong \Gamma$. *Trigger:* a free, proper, discontinuous group action with a simply-connected total space. *Pattern:* "$\mathbb{R}^n / \mathbb{Z}^n = T^n$ and $\mathbb{R}^n$ is simply connected, so $\pi_1(T^n) = \mathbb{Z}^n$" and "$S^n / \{\pm 1\} = \mathbb{RP}^n$, so $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$ for $n \geq 2$".

5. **Compute $\pi_1$ via Seifert-van Kampen.** Decompose $X = U \cup V$ with $U, V$, and $U \cap V$ all open and path-connected; $\pi_1(X)$ is the free product $\pi_1(U) \ast \pi_1(V)$ amalgamated over $\pi_1(U \cap V)$ ([[Thm - Seifert-van Kampen Theorem (Statement)]]). *Trigger:* a space presented as a union of pieces with known $\pi_1$'s. *Pattern:* "loops in $U$ and loops in $V$ generate; loops in $U \cap V$ give relations." For a wedge $X \vee Y$ this collapses to $\pi_1(X) \ast \pi_1(Y)$.

6. **Pass to the universal cover.** When $\pi_1(X)$ is hard to compute directly, pass to the universal cover $\widetilde X$ (if it exists). Loops in $X$ become paths in $\widetilde X$ between points of the fibre, and $\pi_1(X)$ acts on the fibre by deck transformations. *Trigger:* the space is too tangled but admits a recognisable simply-connected cover. *Pattern:* "to find $\pi_1(\mathrm{SO}(3))$, lift to $\mathrm{SU}(2) \cong S^3$ — the kernel of the covering is the fibre over $e$, which is $\{\pm I\} = \mathbb{Z}/2$."

7. **Use functoriality to obstruct or construct.** A continuous map $f : X \to Y$ induces $f_* : \pi_1(X) \to \pi_1(Y)$, a homomorphism that is identity on identity maps and respects composition. A continuous map that would yield an impossible homomorphism (e.g., $\mathbb{Z} \to 0$ that is required surjective on a non-trivial element) does not exist. *Trigger:* asked to show a map does not exist, or to derive a contradiction from an assumed map. *Pattern:* the classical Brouwer fixed-point argument is one line of $f_*$.

8. **Exploit deck-transformation symmetry.** For a regular cover $p : \tilde X \to X$ with deck group $\Gamma$, the base is the quotient $X = \tilde X / \Gamma$, and any $\Gamma$-equivariant object on $\tilde X$ descends to an object on $X$. Conversely, a function on $X$ lifts canonically to a $\Gamma$-invariant function on $\tilde X$. *Trigger:* you have a cover and want to transport an object up or down. *Pattern:* "to construct a vector field on $\mathbb{RP}^n$, construct an antipodally-invariant vector field on $S^n$" — this is how the orientable double cover is used to study non-orientable manifolds.

9. **Use the Eckmann-Hilton argument on topological groups.** If $X$ carries a continuous binary operation $\mu : X \times X \to X$ with a two-sided unit $e$, the multiplication descends to a *second* product on $\pi_1(X, e)$ (multiply two loops pointwise). Eckmann-Hilton says: a set with two unital binary operations satisfying interchange must agree, and the common operation is commutative. So $\pi_1$ of any topological group is abelian. *Trigger:* the space is a topological group, a topological monoid, or an $H$-space. *Pattern:* whenever $\pi_1$ might be non-abelian, the presence of any "multiplication" structure forces commutativity.

10. **Decompose covers using subgroup intersections and conjugations.** Under the Galois correspondence, conjugate subgroups of $\pi_1$ correspond to isomorphic (but non-base-pointedly) covers; the intersection of subgroups corresponds to the fibre product of covers; the smallest normal subgroup containing $H$ corresponds to the largest regular cover dominating $\tilde X_H$. *Trigger:* asked to manipulate covers algebraically. *Pattern:* problems about classifying intermediate covers reduce to lattice theory of subgroups of $\pi_1$.

**Illegal but tempting operations:**

> [!warning] 1. Treating $\pi_1$ as a base-point-independent group
> It is tempting to write "$\pi_1(X)$" without specifying a base point and assume the resulting group is unambiguous. For path-connected $X$ the groups at different base points are isomorphic via the change-of-basepoint isomorphism, but the isomorphism depends on a choice of path between the base points, so the identification is *not canonical* — different paths give isomorphisms differing by an inner automorphism. The right resolution: when only the abstract group matters (as for the assertion "$\pi_1(S^1) = \mathbb{Z}$"), drop the base point; when comparing different $\pi_1$'s or studying maps $f_* : \pi_1(X, x_0) \to \pi_1(Y, f(x_0))$, the base point is essential and inner-automorphism ambiguity matters. The operation becomes legal exactly when you are explicit about the path used to identify base points, or when the inner-automorphism ambiguity is benign for the question at hand.

> [!warning] 2. Assuming every continuous map between two spaces lifts to a covering
> One might guess that since $p : \tilde X \to X$ is "richer" than $X$, any map into $X$ should lift. It fails: with $X = S^1$, $\tilde X = \mathbb{R}$, and $f = \mathrm{id}_{S^1} : S^1 \to S^1$, no continuous lift $\tilde f : S^1 \to \mathbb{R}$ exists (it would imply the identity factors through a simply-connected space). The lifting criterion is precise: lifts exist iff $f_*\pi_1(Y) \subseteq p_*\pi_1(\tilde X)$. The operation becomes legal exactly when this subgroup inclusion holds, or when $Y$ is simply connected (so $f_*\pi_1(Y) = 0$ is trivially inside anything).

> [!warning] 3. Concluding that a finite covering implies a finite $\pi_1$
> "$\tilde X$ is a $k$-sheeted cover of $X$, so $\pi_1(X)$ has $k$ elements" — false in general. A $k$-sheeted cover corresponds to a *subgroup of index $k$*, not a group of order $k$. For $S^1 \to S^1$ via $z \mapsto z^k$, the cover is $k$-sheeted, and $p_*\pi_1(S^1) = k\mathbb{Z} \leq \mathbb{Z}$ is the index-$k$ subgroup — but $\pi_1$ of the base is still $\mathbb{Z}$. The operation becomes legal only when the cover is the universal cover, in which case sheets $\leftrightarrow$ elements of $\pi_1$, so a finite universal cover does imply finite $\pi_1$.

> [!warning] 4. Identifying $\pi_1$ with $H_1$ in non-abelian cases
> It is tempting to compute $\pi_1$ by computing $H_1$ (which is often easier), because they agree for many familiar examples. They agree only up to abelianization: $H_1(X; \mathbb{Z}) = \pi_1(X)^{\mathrm{ab}}$ (Hurewicz). For the figure-eight $\pi_1 = F_2$ but $H_1 = \mathbb{Z}^2$; for any non-abelian $\pi_1$, the abelianization throws information away. The operation becomes legal exactly when $\pi_1$ is already abelian (e.g., for topological groups, surfaces of genus 0 or 1).

---

# Problem-Solving Strategy

Problems in this topic break into five main shapes, and recognising which shape you are looking at chooses the route.

If the problem **asks you to compute $\pi_1$** of an explicit space, the first question is whether the space has a usable cover. If a simply-connected cover $\tilde X$ is in sight together with a free, proper, discontinuous group action $\Gamma \curvearrowright \tilde X$ with $X = \tilde X / \Gamma$, the answer is $\pi_1(X) = \Gamma$, no calculation needed. This handles $S^1$ (with $\tilde X = \mathbb{R}$, $\Gamma = \mathbb{Z}$), $T^n$ (with $\mathbb{R}^n$ and $\mathbb{Z}^n$), $\mathbb{RP}^n$ ($n \geq 2$, with $S^n$ and $\mathbb{Z}/2$), and the Klein bottle. If no such cover is obvious, the next move is [[Thm - Seifert-van Kampen Theorem (Statement)|Seifert-van Kampen]]: write $X = U \cup V$ with $U, V, U \cap V$ path-connected and open, find $\pi_1(U)$, $\pi_1(V)$, $\pi_1(U \cap V)$, and amalgamate. This handles wedges of spheres, surfaces (genus $g$), graphs, and most CW complexes. If neither works, the problem is asking you to *develop new theory*, not just apply it.

If the problem **asks whether a continuous map exists or has a fixed point**, the route runs through functoriality of $\pi_1$. Assume the map exists, push it forward to a homomorphism $f_* : \pi_1(X) \to \pi_1(Y)$, and look for a contradiction in the resulting group homomorphism. The Brouwer fixed-point theorem in dimension 2 is the canonical example: assuming no fixed point produces a retraction $D^2 \to S^1$, which would have to induce a surjection $\pi_1(D^2) = 0 \to \pi_1(S^1) = \mathbb{Z}$, an impossibility. The same pattern proves "no continuous map $S^2 \to S^1$ inducing a surjection on $\pi_1$" trivially (the source is simply connected) and proves the absence of retractions in many other settings.

If the problem **asks you to classify covers** of $X$ — describe all connected covers, all regular covers, all $k$-sheeted covers — apply the [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]]. Connected covers correspond to subgroups of $\pi_1(X)$; regular covers to normal subgroups; $k$-sheeted covers to subgroups of index $k$; the universal cover to $\{1\}$; the trivial cover ($X$ itself) to all of $\pi_1(X)$. The combinatorial work is entirely on the algebraic side once you know $\pi_1$.

If the problem **establishes simply-connectedness** of a space, the routes are (i) exhibit a contraction (the space is contractible), (ii) recognise it as a universal cover of something familiar (then it is simply connected by definition), (iii) use a covering by simply-connected open sets and a Seifert-van Kampen argument, or (iv) compute $\pi_1$ directly and observe it is trivial. For spheres $S^n$ with $n \geq 2$, route (iii) is cleanest: cover by two open hemispheres and apply Seifert-van Kampen.

If the problem **gives geometric data and asks for topological output** — Ricci or sectional curvature bounds, dimension constraints — the route is through one of the curvature-controls-topology theorems. Positive Ricci $\Rightarrow$ finite $\pi_1$ ([[Thm - Myers Theorem (Pi_1 Finite for Positive Ricci)|Myers]]); non-positive sectional $\Rightarrow$ universal cover is $\mathbb{R}^n$ (Cartan-Hadamard); positive sectional + even-dimensional + orientable $\Rightarrow$ simply connected (Synge). These belong to [[Riemannian Geometry III — Riemann Curvature and Topology]] but are constantly invoked in $\pi_1$ problems with geometric flavor.

The meta-strategy threading all five: **every problem about loops becomes a problem about lifts of loops, every problem about $\pi_1$ becomes a problem about the universal cover, and every problem about covers becomes a problem about subgroups of $\pi_1$**. The Galois correspondence is the single unifying question of the chapter: *which side of the correspondence is your problem on, and is it easier on the other side?*

---

# Most Reusable Properties

- **[[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]]**: subgroups of $\pi_1(X)$ ↔ connected covers of $X$, with normal subgroups ↔ regular covers and trivial subgroup ↔ universal cover. This is the most-reused single fact in the topic. Use it whenever you need to classify covers (algebra side easier), to compute $\pi_1$ via constructed covers (geometry side easier), or to translate between deck-transformation symmetries and group-theoretic structure. The recognition is: any time the question mentions "covers", look at subgroups; any time it mentions "$\pi_1$", consider building a cover.

- **[[Thm - Path Lifting and Homotopy Lifting|Path/homotopy lifting]]**: every path lifts uniquely once a starting lift is fixed, and homotopic paths lift to paths with the same endpoint. This is the engine under every algebraic property of $\pi_1$. Use it to define $\pi_1$-invariants (the winding number, the deck-transformation action on fibres), to prove well-definedness of constructions, and to lift loops up to the universal cover where everything contracts. Trigger: any time you see "loop in $X$ and covering $\tilde X$".

- **[[Thm - Pi_1 of S^1 is Z|$\pi_1(S^1) = \mathbb{Z}$]]**: the prototype non-trivial $\pi_1$, and via Brouwer/no-retraction the gateway to almost every classical topology theorem about the plane. Use it as the *first* example whenever building intuition, and as the *engine* of the Brouwer fixed-point theorem and the fundamental theorem of algebra. The recognition trigger: anything involving rotation, winding, or maps to or from a circle.

- **[[Thm - Seifert-van Kampen Theorem (Statement)|Seifert-van Kampen]]**: $\pi_1$ of a union is the amalgamated free product of $\pi_1$'s of the pieces. The single most useful computational tool for $\pi_1$. Use it to compute $\pi_1$ of CW complexes, surfaces, wedges, graphs, and any space built from simpler pieces by gluing. Trigger: the space is given as a union, a CW complex, or a quotient by an open relation.

- **Deck group of universal cover = $\pi_1$**: for the universal cover $\widetilde X \to X$, $\mathrm{Deck}(\widetilde X / X) \cong \pi_1(X)$ canonically. Use this to *recover* $\pi_1$ from a known universal cover (as in $\mathrm{SU}(2) \to \mathrm{SO}(3)$), to identify $\pi_1$ with a known group of symmetries acting on $\widetilde X$, and to understand $\pi_1$ as a group of geometric transformations rather than as homotopy classes of loops. Trigger: you know $\widetilde X$ but want to know $\pi_1$.

---

# Bridges

1. **Algebraic Topology I — Singular Homology and the de Rham Theorem.** The fundamental group is the lowest-degree homotopy invariant; singular homology $H_*(X)$ is the same idea applied to higher-dimensional cycles (simplices instead of loops, boundaries instead of homotopies). The bridge between them is the **Hurewicz theorem**: $H_1(X; \mathbb{Z}) \cong \pi_1(X)^{\mathrm{ab}}$, so $H_1$ recovers $\pi_1$ exactly when $\pi_1$ is already abelian. For higher $k$, the Hurewicz map $\pi_k(X) \to H_k(X)$ is an isomorphism in the lowest non-vanishing degree (for simply-connected $X$). Together, $\pi_*$ and $H_*$ are the two complementary algebraic-topology functors — homotopy is sensitive but hard to compute, homology is computable but coarse, and the Hurewicz theorem mediates between them. See [[Algebraic Topology I — Singular Homology and the de Rham Theorem]].

2. **Group Theory — the isomorphism theorems and Galois correspondences.** The bijection between connected covers and subgroups of $\pi_1$ is *literally* a [[Group Theory I — §1.1–1.2|Galois correspondence]], with the same structural features: normal subgroups correspond to "symmetric" covers (regular covers, where the deck group acts transitively on fibres), and the quotient $\pi_1(X) / p_*\pi_1(\tilde X)$ for a regular cover is the deck group of that cover. The cover-to-cover quotient map corresponds to the subgroup inclusion, and the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] reads on the cover side as "the deck group is the quotient $\pi_1(X)/p_*\pi_1(\tilde X)$". This is the same algebra; only the geometric objects change.

3. **Galois theory of fields — same correspondence, different category.** In Galois theory, finite separable extensions of a field $K$ correspond to subgroups of the absolute Galois group $\mathrm{Gal}(\bar K / K)$, with normal subgroups corresponding to *normal* (Galois) extensions and the quotient giving the Galois group of the extension. The structural parallel with covering-space theory is exact, and Grothendieck made it precise: the **étale fundamental group** $\pi_1^{\mathrm{ét}}(X)$ unifies both. For $X$ a topological space, $\pi_1^{\mathrm{ét}}$ is the profinite completion of $\pi_1$; for $X = \mathrm{Spec}\,K$, it is the absolute Galois group of $K$.

4. **Lie groups and the universal covering group — DG XI.** A connected Lie group $G$ has a universal cover $\widetilde G$ which inherits a Lie group structure with the same [[Def - Lie Algebra|Lie algebra]]. The covering $\widetilde G \to G$ is a Lie group homomorphism whose kernel $\pi_1(G)$ is a discrete central subgroup of $\widetilde G$. So *the same Lie algebra can correspond to several different Lie groups*, all quotients of the unique simply-connected one — the universal covering group is the "fundamental" Lie group with that algebra. This is the conceptual reason behind the existence of spinor representations: they live on $\mathrm{Spin}(n) = \widetilde{\mathrm{SO}(n)}$ rather than $\mathrm{SO}(n)$ itself, because the spin representation does not descend through the $\mathbb{Z}/2$ quotient. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] and [[Spinors and the Dirac Equation]].

5. **Riemannian Geometry III — curvature controls topology.** Myers' theorem ($\mathrm{Ric} \geq (n-1)\kappa > 0 \Rightarrow \pi_1$ finite), Synge's theorem ($\sec > 0$ + even-dim + orientable $\Rightarrow$ simply connected), and Cartan-Hadamard ($\sec \leq 0$ + complete $\Rightarrow$ universal cover is $\mathbb{R}^n$) all translate metric curvature bounds into $\pi_1$-theoretic conclusions. The bridge is the universal cover: lift the metric to $\widetilde M$, prove a topological property of $\widetilde M$ from the lifted curvature, then convert it to a $\pi_1$ statement about $M$ via $\pi_1(M) = \mathrm{Deck}(\widetilde M / M)$. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

---

# Insights

**The unifying frame: every $\pi_1$ question becomes a question about the universal cover.** The fundamental group is hard to compute directly because loops are hard to enumerate up to homotopy. The universal cover trades this for an easier problem: loops in $X$ become *paths between specific points of the fibre* in $\widetilde X$, and since $\widetilde X$ is simply connected, two such paths are homotopic if and only if they have the same endpoints. So $\pi_1(X)$ is *exactly* the discrete fibre $p^{-1}(x_0)$, with the group operation coming from the deck action. Every concrete computation in the chapter — $\pi_1(S^1) = \mathbb{Z}$, $\pi_1(T^n) = \mathbb{Z}^n$, $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$, $\pi_1(\mathrm{SO}(3)) = \mathbb{Z}/2$ — is "find the universal cover, identify the fibre, read off the deck group." When you cannot find the universal cover directly, Seifert-van Kampen is the algebraic substitute; but conceptually, the universal cover is always the right object.

**The true name of $\pi_1$ is "deck group of the universal cover", not "homotopy classes of loops".** The textbook definition of $\pi_1$ — homotopy classes of loops with concatenation — is the right thing to *prove things about* but the wrong thing to *picture*. The picture should be: $X$ has a universal cover $\widetilde X$, and $\pi_1(X)$ is the group of symmetries of $\widetilde X$ that cover the identity of $X$. For $S^1$ this is integer translations of $\mathbb{R}$; for $T^n$ it is lattice translations of $\mathbb{R}^n$; for $\mathbb{RP}^n$ it is the antipodal map on $S^n$. This viewpoint makes everything geometric: the group operation is composition of symmetries, the inverse is the inverse symmetry, conjugation of subgroups corresponds to changing base point in the fibre. The lift-of-loops definition is the *proof technique*; the deck-group definition is the *idea*.

**A trigger-reaction pattern: see a topological group, conclude $\pi_1$ is abelian.** The Eckmann-Hilton argument — two unital operations that distribute over each other must agree and be commutative — applies to $\pi_1$ of any topological group, $H$-space, or topological monoid, because the group multiplication gives a second product on $\pi_1$ that is automatically a homomorphism with respect to the path-product. Once internalised, this means: every time a problem mentions a Lie group, an $H$-space, or anything carrying a continuous binary structure with identity, $\pi_1$ is automatically abelian, no calculation needed. Examples worth committing to memory: $\pi_1(\mathrm{SO}(n)) = \mathbb{Z}/2$ for $n \geq 3$ (abelian), $\pi_1(\mathrm{U}(n)) = \mathbb{Z}$ (abelian), $\pi_1(S^1) = \mathbb{Z}$ (abelian, also because $S^1$ is a Lie group). The pattern fails the moment you leave $H$-spaces: $\pi_1$ of a surface of genus $\geq 2$ is highly non-abelian.

**Inheritance: $\pi_1$ of a quotient inherits from the action group.** Where does $\pi_1(T^n) = \mathbb{Z}^n$ come from? Not from the torus itself — the torus is a quotient $\mathbb{R}^n / \mathbb{Z}^n$, and the $\mathbb{Z}^n$ is *already there*, acting on $\mathbb{R}^n$ by translation. The same is true throughout: $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$ inherits from the antipodal $\mathbb{Z}/2$-action on $S^n$; $\pi_1$ of a hyperbolic surface inherits from the Fuchsian group action on $\mathbb{H}^2$; $\pi_1$ of the Klein bottle inherits from the orientation-reversing $\mathbb{Z} \ltimes \mathbb{Z}$ action on $\mathbb{R}^2$. *When you see a quotient by a discontinuous group action on a simply-connected space, $\pi_1$ of the quotient is the group, full stop.* This is the most efficient single technique for computing $\pi_1$ — when applicable, it skips both lifting arguments and Seifert-van Kampen.

**Local-to-global: the universal cover exists exactly when local simply-connectedness assembles globally.** A space has a universal cover if and only if it is path-connected, locally path-connected, and **semi-locally simply connected**. The last condition says: every point has a neighbourhood $U$ such that any loop in $U$ is null-homotopic *in $X$* (not necessarily in $U$). This local condition is sharp: the **Hawaiian earring** (a wedge of shrinking circles) is locally path-connected but fails semi-local simple connectedness, and indeed has no universal cover. The pattern is local-to-global propagation: local triviality of loops near every point assembles into the global existence of a simply-connected cover.
