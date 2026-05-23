---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Path-Product and the Fundamental Group"
  - "Def - Homotopy of Paths"
  - "Def - Group"
tags: [geometry, algebraic-topology, topology]
---

# Notation

$X$ is a topological space, $x_0 \in X$ a base point. $\Omega(X, x_0)$ is the set of loops $\gamma : I \to X$ with $\gamma(0) = \gamma(1) = x_0$. Loops are concatenated by the path-product $\gamma_1 \cdot \gamma_2$. The constant loop is $c_{x_0}$; the reverse of $\gamma$ is $\gamma^{-1}(t) = \gamma(1-t)$. We write $[\gamma]$ for the homotopy class rel endpoints. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the full registry.

---

# Statement

> **Theorem (Fundamental group is a group).** Let $X$ be a topological space and $x_0 \in X$. The set $\pi_1(X, x_0) := \Omega(X, x_0) / \simeq$ of path-homotopy classes of loops at $x_0$, with operation $[\gamma_1] \cdot [\gamma_2] := [\gamma_1 \cdot \gamma_2]$, identity $[c_{x_0}]$, and inverse $[\gamma]^{-1} := [\gamma^{-1}]$, is a [[Def - Group|group]].

The four things to check are: well-definedness of the operation, associativity, the identity law, and the inverse law. All four are exhibited by explicit homotopies on the unit square.

---

# Motivation

The fundamental group is the central object of the chapter, but it is not obvious that it is even a group. The path-product on raw loops is *not* associative — $(\alpha \cdot \beta) \cdot \gamma$ traverses the three loops with timings $\tfrac14, \tfrac14, \tfrac12$, while $\alpha \cdot (\beta \cdot \gamma)$ uses $\tfrac12, \tfrac14, \tfrac14$. The constant loop is *not* a strict identity: $c_{x_0} \cdot \gamma$ waits at $x_0$ for half the time before traversing $\gamma$ at double speed, which is a different map from $\gamma$. The reverse loop is *not* a strict inverse: $\gamma \cdot \gamma^{-1}$ goes out and comes back, which is not the constant map. So if we want a group, we must work up to a coarser equivalence.

This theorem is the verification that path-homotopy is *exactly* the right equivalence relation. It is fine enough to distinguish different "winding types" of loops (the once-around loop on $S^1$ is not homotopic to the constant), but coarse enough to identify all the reparameterisations that prevent strict associativity, identity, and inverse laws. The proof exhibits, for each axiom, an explicit homotopy showing the failure is "merely" a continuous deformation away.

Why is this important? Because it confirms $\pi_1$ is a *group*, with all the [[Group Theory I — §1.1–1.2|group-theoretic structure]] — kernels, images, normal subgroups, isomorphism theorems, free groups. Without this theorem, $\pi_1$ would be a mere set, and the entire bridge to algebra (which makes covering-space theory possible, makes the Galois correspondence work, makes Brouwer-type obstructions deployable) would collapse.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is bare — any topological space $X$ and any point $x_0$ suffice. The skill is in recognising that the theorem applies in non-obvious contexts.

The first non-obvious source is **a CW complex** built from cells of various dimensions. The space is far from path-connected in a single chart, but each cell is contractible, and the theorem says $\pi_1$ is still a group. The fact that $\pi_1$ is a group regardless of the geometry of $X$ is what makes the **fundamental group of a graph**, of a surface, of a polyhedron, of an arbitrary CW complex all well-defined groups. The bridge: any topological space → group, no smoothness or local Euclidean structure required.

The second non-obvious source is **a smooth manifold** $M$. Here loops are smooth maps $S^1 \to M$ (after reparameterisation), and the question becomes whether smooth-loop classes form a group. The theorem applies because smooth loops are continuous, and the homotopy can be taken smooth by mollification. So $\pi_1(M)$ as a group is the same whether one uses continuous or smooth loops. This is the bridge from continuous topology to differential geometry, and it is the reason $\pi_1$ of a Lie group, $\pi_1$ of a Riemannian manifold, etc. are well-defined.

The third non-obvious source is **a loop space $\Omega Y$ at a point**. Loops in $\Omega Y$ are *homotopies of loops in $Y$*, and the theorem applied to $\Omega Y$ gives $\pi_1(\Omega Y) = \pi_2(Y)$, the second homotopy group. The bridge "$\pi_1$ of a loop space = $\pi_2$ of the original" is the recursive structure that defines higher homotopy.

**Targets (Output Amplification)**

The conclusion is "the set $\pi_1$ is a group." Combined with other tools, this conclusion amplifies.

The first combination is **with the functoriality of $\pi_1$**: a continuous map $f : X \to Y$ with $f(x_0) = y_0$ induces a homomorphism $f_* : \pi_1(X, x_0) \to \pi_1(Y, y_0)$. The combination "$\pi_1$ is a group AND $\pi_1$ is functorial" upgrades the basic group structure to a powerful obstruction tool: a continuous map between spaces that would yield an impossible homomorphism cannot exist. This is the engine of the Brouwer fixed-point theorem, the no-retraction theorem, the impossibility of $\mathbb{R}^2 \cong \mathbb{R}^3$, etc.

The second combination is **with the Galois correspondence for covers**: the group structure on $\pi_1$ has a corresponding lattice structure on subgroups, which corresponds to a lattice structure on connected covers of $X$. The combination "$\pi_1$ is a group AND covers ↔ subgroups" lets you transport algebraic constructions on $\pi_1$ (kernels, normal subgroups, quotients) to geometric constructions on covers (universal cover, regular covers, intermediate covers). This is [[Thm - Galois Correspondence for Covering Spaces]].

The third combination is **with the Hurewicz theorem**: $H_1(X; \mathbb{Z}) \cong \pi_1(X)^{\mathrm{ab}}$, so $\pi_1$ being a group lets you abelianise and recover $H_1$ — a fact used to *compute* $\pi_1$ when $H_1$ is more accessible, or to *bound* the size of $\pi_1$ when $H_1$ is known to be small. The combination "$\pi_1$ is a group AND $\pi_1^{\mathrm{ab}} = H_1$" routes between homotopy and homology.

---

# Why Is It True

The truth of the theorem is that **path-homotopy is the precise equivalence relation under which path-product becomes a group operation**.

The strategy is: the failure of associativity, identity, and inverse on raw paths is *purely a reparameterisation issue*. Two paths that differ only in their traversal speeds (with no change in image or qualitative behaviour) are always path-homotopic, via the straight-line interpolation in the parameter. So once you mod out by path-homotopy, all reparameterisation differences vanish, and the group axioms hold.

**The bolded one-liner: path-homotopy is exactly the equivalence relation generated by reparameterisations, so it is precisely the coarsest equivalence that recovers strict associativity, identity, and inverse from the (only-up-to-reparameterisation) versions of those laws on raw paths.**

Concretely:
- **Associativity.** $(\alpha \cdot \beta) \cdot \gamma$ uses timings $(\tfrac14, \tfrac14, \tfrac12)$; $\alpha \cdot (\beta \cdot \gamma)$ uses $(\tfrac12, \tfrac14, \tfrac14)$. The two are reparameterisations of each other (same images in the same order, only the speeds differ), so they are homotopic. The homotopy slides the timings continuously from one bracketing to the other.

- **Identity.** $c_{x_0} \cdot \gamma$ traverses the constant at $x_0$ for the first half-time, then $\gamma$ at double speed. It is $\gamma$ "with a wait at the start," and the wait can be continuously shrunk to zero by reparameterisation. Similarly $\gamma \cdot c_{x_0}$.

- **Inverse.** $\gamma \cdot \gamma^{-1}$ goes out along $\gamma$ then comes back. The "fold" homotopy reels the path back: at homotopy time $t$, only go out a fraction $1-t$ of the way before turning back, so at $t = 1$ you stay put.

All three failures are reparameterisation-style: same image (or empty image, for the inverse case) up to changes in the speed of traversal. Path-homotopy absorbs all such changes, so the group axioms hold on the quotient.

There is no fancier idea here — the theorem is true because the equivalence relation has been chosen to make it true. The genuine work is the explicit construction of the homotopies, which is computational but conceptually transparent.

---

# What Makes This Hard

The hardest part is not believing the theorem — the intuition is clear once one sees the "wait then run" or "out and back" pictures — but rather **writing down the homotopies explicitly**, with care about piecewise formulas and the boundary conditions on the unit square. Most people get the homotopies wrong on the first try because they forget that the homotopy must (a) be continuous across the piecewise transitions, (b) start at the correct path on $t = 0$ and end at the correct path on $t = 1$, and (c) keep the basepoint fixed on the vertical edges $s = 0$ and $s = 1$. A common error is to give a homotopy that fixes only one endpoint, not both. Another is to give a homotopy of pieces that does not match up at $s = \tfrac12$, breaking continuity.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** verify each group axiom by exhibiting an explicit homotopy on the unit square $I \times I$. Each homotopy is a piecewise-linear reparameterisation of the path-product variant in question, sliding continuously to the canonical form.

**Subgoal decomposition:**

1. **Well-definedness of the product.** Show that if $\gamma_1 \simeq \gamma_1'$ and $\gamma_2 \simeq \gamma_2'$ (with appropriate endpoints), then $\gamma_1 \cdot \gamma_2 \simeq \gamma_1' \cdot \gamma_2'$.
   - *Hint:* The "obvious" homotopy is to concatenate the two homotopies side-by-side on the bottom and top halves.
   - *Why needed:* Without well-definedness on classes, the operation is not defined on $\pi_1(X, x_0)$.

2. **Associativity.** Construct $H : I \times I \to X$ with bottom edge $(\alpha \cdot \beta) \cdot \gamma$ and top edge $\alpha \cdot (\beta \cdot \gamma)$, and vertical edges constant at $x_0$.
   - *Hint:* Slide the two "cut points" of the piecewise-defined path. At time $t$, the first cut is at $s = \tfrac{1 + t}{4}$ (between $\alpha$ and $\beta$), the second at $s = \tfrac{2 + t}{4}$ (between $\beta$ and $\gamma$).
   - *Why needed:* Without associativity, the operation on $\pi_1$ is not a group operation.

3. **Identity law.** Construct $H : I \times I \to X$ with bottom edge $c_{x_0} \cdot \gamma$ and top edge $\gamma$, constant on vertical edges.
   - *Hint:* The "wait" segment shrinks from length $\tfrac12$ at $t = 0$ to length $0$ at $t = 1$. At time $t$, $\gamma$ is traversed on $[\tfrac{1-t}{2}, 1]$ at speed $\tfrac{2}{1+t}$.
   - *Why needed:* Without the identity law, $\pi_1$ has no identity.

4. **Inverse law.** Construct $H : I \times I \to X$ with bottom edge $\gamma \cdot \gamma^{-1}$ and top edge $c_{x_0}$, constant on vertical edges.
   - *Hint:* "Fold" the path: at time $t$, go out along $\gamma$ only to the midpoint $\gamma(1-t)$, then return.
   - *Why needed:* Without the inverse law, $\pi_1$ has no inverses.

---

# Lemma Decomposition

Each lemma is independently practiceable in roughly five minutes.

> [!note]- Lemma 1: Path-product is well-defined on homotopy classes
> **Statement:** If $\gamma_1 \simeq \gamma_1'$ and $\gamma_2 \simeq \gamma_2'$ are path-homotopies rel endpoints, with $\gamma_1(1) = \gamma_1'(1) = \gamma_2(0) = \gamma_2'(0)$, then $\gamma_1 \cdot \gamma_2 \simeq \gamma_1' \cdot \gamma_2'$.
>
> **Hint:** Concatenate the two homotopies side-by-side. The bottom-half-square uses $H_1$, the top-half uses $H_2$.
>
> **Why needed:** The product $[\gamma_1] \cdot [\gamma_2] := [\gamma_1 \cdot \gamma_2]$ depends only on the classes.
>
> > [!note]- Full proof
> > Let $H_1 : I \times I \to X$ be a homotopy from $\gamma_1$ to $\gamma_1'$ rel endpoints, and $H_2 : I \times I \to X$ be a homotopy from $\gamma_2$ to $\gamma_2'$ rel endpoints. Define
> > $$H(s, t) = \begin{cases} H_1(2s, t) & 0 \leq s \leq \tfrac12 \\ H_2(2s - 1, t) & \tfrac12 \leq s \leq 1. \end{cases}$$
> > At $s = \tfrac12$ the two pieces meet at the common value $\gamma_1(1) = \gamma_2(0)$ (which is preserved by both homotopies via rel-endpoints), so $H$ is continuous. At $t = 0$: $H(s, 0) = (\gamma_1 \cdot \gamma_2)(s)$. At $t = 1$: $H(s, 1) = (\gamma_1' \cdot \gamma_2')(s)$. At $s = 0$: $H(0, t) = H_1(0, t) = \gamma_1(0)$. At $s = 1$: $H(1, t) = H_2(1, t) = \gamma_2(1)$. So $H$ is a path-homotopy rel endpoints from $\gamma_1 \cdot \gamma_2$ to $\gamma_1' \cdot \gamma_2'$.

> [!note]- Lemma 2: Associativity up to homotopy
> **Statement:** $(\alpha \cdot \beta) \cdot \gamma \simeq \alpha \cdot (\beta \cdot \gamma)$.
>
> **Hint:** Both sides traverse $\alpha$, then $\beta$, then $\gamma$ — they differ only in timings. Slide the two cut points continuously from $(\tfrac14, \tfrac12)$ to $(\tfrac12, \tfrac34)$.
>
> **Why needed:** The group operation on classes is then associative: $([\alpha] \cdot [\beta]) \cdot [\gamma] = [\alpha] \cdot ([\beta] \cdot [\gamma])$.
>
> > [!note]- Full proof
> > Define $H : I \times I \to X$ by
> > $$H(s, t) = \begin{cases} \alpha\bigl(\frac{4s}{1+t}\bigr) & 0 \leq s \leq \frac{1+t}{4} \\ \beta(4s - 1 - t) & \frac{1+t}{4} \leq s \leq \frac{2+t}{4} \\ \gamma\bigl(\frac{4s - 2 - t}{2 - t}\bigr) & \frac{2+t}{4} \leq s \leq 1. \end{cases}$$
> > One verifies: continuity at the seam points (both pieces evaluate to $\alpha(1) = \beta(0)$ and $\beta(1) = \gamma(0)$ respectively); the bottom edge $t = 0$ recovers $(\alpha \cdot \beta) \cdot \gamma$ (timings $\tfrac14, \tfrac14, \tfrac12$); the top edge $t = 1$ recovers $\alpha \cdot (\beta \cdot \gamma)$ (timings $\tfrac12, \tfrac14, \tfrac14$); the vertical edges are constant at $\alpha(0)$ and $\gamma(1)$. So $H$ is the required homotopy.

> [!note]- Lemma 3: Identity law
> **Statement:** $c_{x_0} \cdot \gamma \simeq \gamma$ and $\gamma \cdot c_{x_0} \simeq \gamma$ for any loop $\gamma$ at $x_0$.
>
> **Hint:** The "wait" segment of length $\tfrac12$ at the start of $c_{x_0} \cdot \gamma$ can be continuously shrunk to length $0$, leaving the full traversal of $\gamma$ at unit speed.
>
> **Why needed:** $[c_{x_0}]$ is the identity element of $\pi_1(X, x_0)$.
>
> > [!note]- Full proof
> > For $c_{x_0} \cdot \gamma \simeq \gamma$, define
> > $$H(s, t) = \begin{cases} x_0 & 0 \leq s \leq \frac{1-t}{2} \\ \gamma\bigl(\frac{2s - (1-t)}{1+t}\bigr) & \frac{1-t}{2} \leq s \leq 1. \end{cases}$$
> > At $t = 0$: bottom edge is $c_{x_0} \cdot \gamma$ (wait until $s = \tfrac12$, then traverse $\gamma$ at speed 2). At $t = 1$: top edge is $\gamma$ (no wait, traverse $\gamma$ at unit speed). At $s = 0$: $H(0, t) = x_0$ (lies in the "wait" region for all $t \in [0, 1)$, and at $t = 1$ the formula gives $\gamma(0) = x_0$). At $s = 1$: $H(1, t) = \gamma(1) = x_0$. Continuous, hence the required homotopy. Similar for $\gamma \cdot c_{x_0} \simeq \gamma$.

> [!note]- Lemma 4: Inverse law
> **Statement:** $\gamma \cdot \gamma^{-1} \simeq c_{x_0}$ and $\gamma^{-1} \cdot \gamma \simeq c_{x_0}$ for any loop $\gamma$ at $x_0$, where $\gamma^{-1}(t) := \gamma(1-t)$.
>
> **Hint:** The "fold" homotopy: at homotopy time $t$, go out along $\gamma$ to $\gamma(1-t)$, then come back. At $t = 0$ this is the full out-and-back loop; at $t = 1$ it stays put at $x_0$.
>
> **Why needed:** $[\gamma]^{-1} = [\gamma^{-1}]$ is the inverse of $[\gamma]$ in $\pi_1(X, x_0)$.
>
> > [!note]- Full proof
> > Define
> > $$H(s, t) = \begin{cases} \gamma(2s(1-t)) & 0 \leq s \leq \tfrac12 \\ \gamma(2(1-s)(1-t)) & \tfrac12 \leq s \leq 1. \end{cases}$$
> > At $s = \tfrac12$ both pieces give $\gamma(1-t)$, so continuous. At $t = 0$: $H(s, 0)$ is $\gamma(2s)$ on $[0, \tfrac12]$ and $\gamma(2-2s)$ on $[\tfrac12, 1]$, which is $\gamma \cdot \gamma^{-1}$. At $t = 1$: $H(s, 1) = \gamma(0) = x_0$ for all $s$, the constant loop. At $s = 0$: $H(0, t) = \gamma(0) = x_0$. At $s = 1$: $H(1, t) = \gamma(0) = x_0$. So $H$ is the required homotopy. Similar for $\gamma^{-1} \cdot \gamma \simeq c_{x_0}$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $X$ be a topological space, $x_0 \in X$. The set $\pi_1(X, x_0)$ of path-homotopy classes of loops at $x_0$, with operation $[\gamma_1] \cdot [\gamma_2] := [\gamma_1 \cdot \gamma_2]$, identity $[c_{x_0}]$, inverse $[\gamma]^{-1} := [\gamma^{-1}]$, is a group.
>
> *Proof.* We verify the four conditions.
>
> **Well-definedness.** By Lemma 1, the operation $[\gamma_1] \cdot [\gamma_2] := [\gamma_1 \cdot \gamma_2]$ does not depend on representatives. (The inverse operation is well-defined similarly: if $\gamma \simeq \gamma'$ via $H$, then $\gamma^{-1} \simeq (\gamma')^{-1}$ via $H'(s, t) = H(1-s, t)$.)
>
> **Associativity.** By Lemma 2, $(\alpha \cdot \beta) \cdot \gamma \simeq \alpha \cdot (\beta \cdot \gamma)$, so $([\alpha] \cdot [\beta]) \cdot [\gamma] = [\alpha] \cdot ([\beta] \cdot [\gamma])$ in $\pi_1(X, x_0)$.
>
> **Identity.** By Lemma 3, $c_{x_0} \cdot \gamma \simeq \gamma$ and $\gamma \cdot c_{x_0} \simeq \gamma$, so $[c_{x_0}] \cdot [\gamma] = [\gamma] = [\gamma] \cdot [c_{x_0}]$ in $\pi_1(X, x_0)$.
>
> **Inverse.** By Lemma 4, $\gamma \cdot \gamma^{-1} \simeq c_{x_0}$ and $\gamma^{-1} \cdot \gamma \simeq c_{x_0}$, so $[\gamma] \cdot [\gamma^{-1}] = [c_{x_0}] = [\gamma^{-1}] \cdot [\gamma]$ in $\pi_1(X, x_0)$. Hence every element has a two-sided inverse.
>
> All four group axioms hold, so $\pi_1(X, x_0)$ is a group. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Knot theory: $\pi_1$ of a knot complement.** Take any knot $K \subset S^3$ and consider the **knot complement** $S^3 \setminus K$. This is a 3-manifold, and its fundamental group is the **knot group** $\pi_1(S^3 \setminus K)$ — a powerful (though not complete) invariant of the knot. The theorem says this is a group, and the entire subject of knot theory hinges on computing it via the Wirtinger presentation. For the trefoil knot, $\pi_1(S^3 \setminus K) = \langle a, b \mid aba = bab \rangle$ — the braid group $B_3$.

**Lie groups: $\pi_1$ of every Lie group is abelian.** Combine this theorem with the Eckmann-Hilton argument: $\pi_1$ of a topological group has *two* unital products (path-product and pointwise multiplication of loops), they distribute, hence by Eckmann-Hilton they agree and are commutative. So $\pi_1(G)$ is automatically abelian for any [[Def - Lie Group|Lie group]] $G$. Examples: $\pi_1(\mathrm{SO}(n)) = \mathbb{Z}/2$ for $n \geq 3$, $\pi_1(\mathrm{U}(n)) = \mathbb{Z}$ — both abelian. See [[Ex - Pi_1 of a Topological Group is Abelian]].

**Function spaces: $\pi_1$ of a function space.** Consider $\mathrm{Map}(X, Y)$ (continuous maps with compact-open topology) and a base point $f_0 : X \to Y$. The fundamental group $\pi_1(\mathrm{Map}(X, Y), f_0)$ is the set of homotopy classes of homotopies of $f_0$ to itself — *isotopy classes* in some sense. For $X = S^n$ and $Y$ a manifold, this is related to the higher homotopy groups $\pi_{n+1}(Y, f_0(*))$. The theorem says these are groups regardless of the complexity of the function space.

**Algebraic geometry: étale fundamental group is profinite.** Replace continuous covers with étale covers of an algebraic variety; the corresponding fundamental group $\pi_1^{\mathrm{ét}}$ classifies finite étale covers. The same Lemma-1-style proof shows $\pi_1^{\mathrm{ét}}$ is a (profinite) group. This is Grothendieck's bridge from topology to number theory.

---

# Bridges

- **[[Def - Path-Product and the Fundamental Group|Path-product and definition of $\pi_1$]]** — this theorem is the verification of the group axioms for the construction given in the definition. The definition introduces the path-product on loops; the theorem checks that path-product passes to classes and satisfies the group axioms. They are inseparable: the definition does not make sense as a group definition without this theorem.

- **[[Group Theory I — §1.1–1.2|Group axioms]]** — the theorem is a direct verification of the group axioms of [[Def - Group]] applied to a specific construction. The four conditions of well-definedness, associativity, identity, inverse are exactly those of a group operation. So this theorem is a bridge: a topological object (loops up to homotopy) is shown to be an algebraic object (a group), and the bridge goes through verifying the axioms one by one.

- **Functoriality of $\pi_1$** — once $\pi_1$ is a group, the next theorem is that continuous maps induce *homomorphisms* of these groups (proved by checking that $f \circ (\gamma_1 \cdot \gamma_2) = (f \circ \gamma_1) \cdot (f \circ \gamma_2)$ and that $f_*$ is well-defined on classes). This upgrade — from "$\pi_1$ is a group" to "$\pi_1$ is a *functor*" to $\mathbf{Grp}$ — is the foundation of all the subsequent applications.

- **Eckmann-Hilton argument** — when $X$ carries an additional structure (a topological group, an $H$-space), $\pi_1(X)$ inherits a *second* product from the multiplication on $X$, and the interchange law (since the multiplication is a homomorphism) forces the two products to agree and be commutative. This is the bridge from "$\pi_1$ is a group" to "$\pi_1$ is sometimes abelian," and it explains why $\pi_1$ of a Lie group is always abelian. See [[Ex - Pi_1 of a Topological Group is Abelian]].
