---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Path-Product and the Fundamental Group"
  - "Def - Group"
  - "Def - Homotopy of Paths"
tags: [geometry, algebraic-topology, lie-groups, topology]
---

# Problem Statement

Let $G$ be a topological group with identity $e$ (or more generally, an $H$-space — a topological space with a continuous binary operation having a two-sided identity up to homotopy). Show that $\pi_1(G, e)$ is **abelian**.

In particular: $\pi_1$ of every Lie group is abelian. So $\pi_1(\mathrm{SO}(n))$, $\pi_1(\mathrm{U}(n))$, $\pi_1(\mathrm{SU}(n))$, $\pi_1(\mathrm{Sp}(n))$, $\pi_1(T^n)$ are all abelian.

**Recall:**

The fundamental group:

![[Def - Path-Product and the Fundamental Group#The Definition]]

What it means to be a group:

![[Def - Group#The Definition]]

---

# Convergent Strategy

**Problem class:** A *structural* result about $\pi_1$ that holds whenever the underlying space has extra (algebraic) structure. The pattern is the **Eckmann-Hilton argument**: a set with two unital binary operations satisfying the interchange law must have both operations equal and commutative. Applying this to $\pi_1(G)$, which has the path-product *and* (inherited from the group multiplication) a *pointwise product* of loops, forces commutativity.

**Assumption pattern:** $G$ is a topological group (or $H$-space). The multiplication $\mu : G \times G \to G$ is continuous with two-sided unit $e$. The fundamental group $\pi_1(G, e)$ inherits a *second* binary operation from $\mu$: pointwise multiply two loops, $(\alpha \cdot_\mu \beta)(t) := \mu(\alpha(t), \beta(t))$, well-defined on classes by continuity of $\mu$.

**Theorem routing:** Show the two operations distribute (interchange law): $(\alpha \cdot \beta) \cdot_\mu (\gamma \cdot \delta) = (\alpha \cdot_\mu \gamma) \cdot (\beta \cdot_\mu \delta)$. Apply Eckmann-Hilton: two unital operations on the same set with interchange must agree and be commutative. So path-product on $\pi_1(G, e)$ is commutative.

**Key decision point:** The crux is the *interchange law*. It says: doing $(A \cdot B)$ and $(C \cdot D)$ in path-product and then $\mu$ng them pointwise = doing $(A \cdot_\mu C)$ and $(B \cdot_\mu D)$ pointwise and then path-producting them. The trick is choosing $A = C = e$ (the constant identity loop) or $B = D = e$ — Eckmann-Hilton then forces equalities that collapse to commutativity. Recognising this combinatorial trick is the non-obvious step.

---

# Legal Operations Used

1. **Operation 9 from the topic page (Eckmann-Hilton argument on topological groups).** This exercise *is* the Eckmann-Hilton argument in action: two unital products on $\pi_1(G, e)$, one from path-product and one from pointwise multiplication, distribute, hence are equal and commutative. The pattern recurs whenever a space carries a continuous binary operation: $\pi_1$ inherits a second product, and Eckmann-Hilton applies.

2. **Operation 7 from the topic page (use functoriality).** The continuous multiplication $\mu : G \times G \to G$ induces a homomorphism $\mu_* : \pi_1(G \times G, (e, e)) \to \pi_1(G, e)$. Combined with the product formula $\pi_1(G \times G) = \pi_1(G) \times \pi_1(G)$, this gives a second binary operation on $\pi_1(G, e)$.

3. **Operation 8 from the topic page (deck-transformation symmetry — used loosely as "structure-of-the-group descends to $\pi_1$").** The group structure on $G$ propagates to a group structure on $\pi_1(G)$ via pointwise multiplication, and this structure must be compatible with the path-product structure already present.

---

# Hints

> [!note]- Hint 1
> A topological group has *two* natural binary operations on loops at $e$: (i) the path-product $\alpha \cdot \beta$ (concatenate paths); (ii) the pointwise product $(\alpha \cdot_\mu \beta)(t) := \alpha(t) \cdot \beta(t)$ (multiply pointwise using the group operation). Both are unital (the constant loop $c_e$ is the identity for both).

> [!note]- Hint 2
> Show that these two operations satisfy the **interchange law**: $(\alpha \cdot \beta) \cdot_\mu (\gamma \cdot \delta) = (\alpha \cdot_\mu \gamma) \cdot (\beta \cdot_\mu \delta)$. This is a pointwise computation using only the group axioms.

> [!note]- Hint 3
> **Eckmann-Hilton argument:** if a set $X$ has two unital binary operations $\circ_1$ and $\circ_2$ satisfying the interchange law, then $\circ_1 = \circ_2$ and the common operation is commutative. The proof is short — substitute $1$ (the common unit) at strategic positions.

> [!note]- Hint 4
> Apply Eckmann-Hilton to $\pi_1(G, e)$ with the two operations from Step 1. The two products agree and are commutative; hence path-product on $\pi_1(G, e)$ is abelian.

---

# Solution

**Plan:** First, define both operations on $\pi_1(G, e)$ and verify they are unital. Second, prove the interchange law via pointwise computation. Third, apply Eckmann-Hilton to conclude commutativity of path-product.

**Step 1: Both operations on $\pi_1(G, e)$ are unital.**

> [!note]- Derivation
> *Path-product.* The path-product $\alpha \cdot \beta$ on loops at $e$ is well-defined on homotopy classes (Lemma 1 of [[Thm - The Fundamental Group is a Group]]), with two-sided identity $[c_e]$ (the constant loop at $e$) by Lemma 3 of the same theorem.
>
> *Pointwise product.* Define $\alpha \cdot_\mu \beta : I \to G$ by $(\alpha \cdot_\mu \beta)(t) := \mu(\alpha(t), \beta(t)) = \alpha(t) \beta(t)$. This is continuous (composition of continuous maps), and is a loop at $e$ (since $\alpha(0) = \beta(0) = e$ and $\mu(e, e) = e$, similarly at $t = 1$).
>
> Pointwise product is well-defined on classes: if $\alpha \simeq \alpha'$ via $H_\alpha$ and $\beta \simeq \beta'$ via $H_\beta$ (rel endpoints), then $H(s, t) := \mu(H_\alpha(s, t), H_\beta(s, t))$ is a homotopy from $\alpha \cdot_\mu \beta$ to $\alpha' \cdot_\mu \beta'$, rel endpoints.
>
> *Identity for pointwise product:* $\alpha \cdot_\mu c_e = \alpha$ since $\mu(\alpha(t), e) = \alpha(t)$ for all $t$ (right identity of $\mu$). Similarly $c_e \cdot_\mu \alpha = \alpha$. So $[c_e]$ is the two-sided identity for $\cdot_\mu$ as well.

**Step 2: Interchange law.**

> [!note]- Derivation
> Claim: for any four loops $\alpha, \beta, \gamma, \delta$ at $e$, $(\alpha \cdot \beta) \cdot_\mu (\gamma \cdot \delta) = (\alpha \cdot_\mu \gamma) \cdot (\beta \cdot_\mu \delta)$ as loops (i.e., as maps $I \to G$).
>
> Compute both sides at $t \in I$:
>
> **Left side:** $((\alpha \cdot \beta) \cdot_\mu (\gamma \cdot \delta))(t) = \mu((\alpha \cdot \beta)(t), (\gamma \cdot \delta)(t))$. For $t \in [0, \tfrac12]$: $(\alpha \cdot \beta)(t) = \alpha(2t)$ and $(\gamma \cdot \delta)(t) = \gamma(2t)$, so this is $\mu(\alpha(2t), \gamma(2t))$. For $t \in [\tfrac12, 1]$: $(\alpha \cdot \beta)(t) = \beta(2t - 1)$ and $(\gamma \cdot \delta)(t) = \delta(2t - 1)$, so this is $\mu(\beta(2t - 1), \delta(2t - 1))$.
>
> **Right side:** $((\alpha \cdot_\mu \gamma) \cdot (\beta \cdot_\mu \delta))(t)$. For $t \in [0, \tfrac12]$: this is $(\alpha \cdot_\mu \gamma)(2t) = \mu(\alpha(2t), \gamma(2t))$. For $t \in [\tfrac12, 1]$: $(\beta \cdot_\mu \delta)(2t - 1) = \mu(\beta(2t - 1), \delta(2t - 1))$.
>
> The two sides agree on both halves of $I$, hence as maps. So the interchange law holds *exactly* (not just up to homotopy).

**Step 3: Apply Eckmann-Hilton.**

> [!note]- Derivation
> **Eckmann-Hilton Lemma.** Let $X$ be a set with two binary operations $\circ_1, \circ_2$, each having a two-sided identity (both $1$), and satisfying the interchange law $(a \circ_1 b) \circ_2 (c \circ_1 d) = (a \circ_2 c) \circ_1 (b \circ_2 d)$. Then the two identities agree, the two operations agree, and the common operation is commutative.
>
> *Proof of the lemma.* First, $1_1 = 1_1 \circ_2 1_1$ (identity for $\circ_2$). Also $1_1 = 1_1 \circ_1 1_1$ (identity for $\circ_1$). Combining: $1_1 = (1_1 \circ_1 1_1) \circ_2 (1_1 \circ_1 1_1)$. By interchange: $= (1_1 \circ_2 1_1) \circ_1 (1_1 \circ_2 1_1) = 1_1 \circ_1 1_1 = 1_1$. (Self-consistent but uninformative so far.) Now compute using interchange with $1$ in strategic positions: $a \circ_1 b = (a \circ_2 1) \circ_1 (1 \circ_2 b)$ (where $1$ is the common identity) — by interchange this equals $(a \circ_1 1) \circ_2 (1 \circ_1 b) = a \circ_2 b$. So $\circ_1 = \circ_2$. Apply the same trick with $a$ and $b$ swapped: $a \circ_1 b = (1 \circ_2 a) \circ_1 (b \circ_2 1) = (1 \circ_1 b) \circ_2 (a \circ_1 1) = b \circ_2 a = b \circ_1 a$. Hence commutativity.
>
> *Application.* The two operations $\cdot$ (path-product) and $\cdot_\mu$ (pointwise product) on $\pi_1(G, e)$ are both unital with identity $[c_e]$, and satisfy the interchange law (Step 2, descending to classes — well-defined on classes by Step 1, then equality of class equalities follows from equality of representatives).
>
> By Eckmann-Hilton, $\cdot = \cdot_\mu$ on $\pi_1(G, e)$, and the common operation is commutative. Hence $\pi_1(G, e)$ is abelian.

**Step 4: Conclude.**

> [!note]- Derivation
> $\pi_1(G, e)$ is abelian for any topological group $G$. In particular, $\pi_1$ of every Lie group is abelian: $\pi_1(\mathrm{SO}(n)), \pi_1(\mathrm{U}(n)), \pi_1(\mathrm{SU}(n)), \pi_1(T^n), \pi_1(\mathrm{Sp}(n))$, etc.
>
> Concrete consequences:
> - $\pi_1(T^n) = \mathbb{Z}^n$ (abelian), consistent with [[Ex - Pi_1 of the Torus is Z Squared]].
> - $\pi_1(\mathrm{SO}(3)) = \mathbb{Z}/2$ (abelian, consistent with [[Ex - SU(2) is the Universal Cover of SO(3)]]).
> - $\pi_1(\mathrm{U}(n)) = \mathbb{Z}$ (abelian, generated by the determinant loop $\det : \mathrm{U}(n) \to S^1$).
> - $\pi_1(\mathrm{SU}(n)) = 0$ (trivially abelian, since $\mathrm{SU}(n)$ is simply connected for all $n \geq 1$).

> [!note]- Complete formal solution
> **Theorem.** For any topological group $G$ (with continuous multiplication and identity), $\pi_1(G, e)$ is abelian.
>
> *Proof.* Define two binary operations on the set of homotopy classes of loops in $G$ at $e$:
>
> 1. **Path-product** $\cdot$: $[\alpha] \cdot [\beta] := [\alpha \cdot \beta]$ where $(\alpha \cdot \beta)$ is the path-concatenation.
>
> 2. **Pointwise product** $\cdot_\mu$: $[\alpha] \cdot_\mu [\beta] := [\alpha \cdot_\mu \beta]$ where $(\alpha \cdot_\mu \beta)(t) := \mu(\alpha(t), \beta(t))$ is the pointwise multiplication via the group operation $\mu$ of $G$.
>
> Both are well-defined on classes (Step 1 above) and both have $[c_e]$ as a two-sided identity. The interchange law $(\alpha \cdot \beta) \cdot_\mu (\gamma \cdot \delta) = (\alpha \cdot_\mu \gamma) \cdot (\beta \cdot_\mu \delta)$ holds exactly on representatives (Step 2), hence on classes.
>
> By the Eckmann-Hilton lemma, $\cdot$ and $\cdot_\mu$ agree on $\pi_1(G, e)$, and the common operation is commutative. Hence $\pi_1(G, e)$ is abelian. $\qquad\blacksquare$

> [!warning] Illegal but tempting alternative route: "$G$ is abelian implies $\pi_1(G)$ abelian"
> One might think: "Many of the standard Lie groups are *non*-abelian ($\mathrm{SO}(3)$, $\mathrm{SU}(2)$, etc.), so the result must require commutativity of $G$." This is wrong — the Eckmann-Hilton argument does not need $G$ to be abelian at all. The key is the *existence* of a continuous binary operation with identity, not its commutativity. The interchange law is automatic (computed pointwise), and Eckmann-Hilton does the rest. The argument applies to *every* topological group, abelian or not.

---

# Key Takeaways

**Eckmann-Hilton is the algebraic content of $\pi_1$ of $H$-spaces being abelian, and it generalises.** The argument is a *categorical* statement: any unital "double monoid" object collapses to a commutative monoid. The same argument applied to $\pi_n(X)$ for $n \geq 2$ shows the higher homotopy groups are *always* abelian (the loop-space structure gives an extra product, and Eckmann-Hilton forces commutativity). This is why "$\pi_n$ is abelian for $n \geq 2$" is not a special property of nice spaces but a structural consequence of the existence of the loop-space multiplication. The trigger condition: any space with extra binary structure (group, monoid, $H$-space). The transferable diagnostic: Eckmann-Hilton applies whenever you have two unital binary operations satisfying the interchange law; the conclusion is commutativity, often non-obvious from the operations themselves.

**$\pi_1$ of a topological group is finite when the group is compact and semisimple.** Combining the Eckmann-Hilton commutativity result with Myers' theorem (compact $\mathrm{Ric} > 0$ → finite $\pi_1$): for any compact connected Lie group $G$ with bi-invariant metric (which has $\mathrm{Ric} > 0$ when the centre is trivial, as proved in Frankel §21.4), $\pi_1(G)$ is *finite abelian*. Examples: $\pi_1(\mathrm{SO}(n)) = \mathbb{Z}/2$ for $n \geq 3$; $\pi_1(\mathrm{U}(n)) = \mathbb{Z}$ (not finite — but $\mathrm{U}(n)$ has non-trivial centre, so Myers does not apply directly); $\pi_1(\mathrm{SU}(n)) = 0$, finite. The trigger condition: compact Lie group with trivial centre algebra. The transferable diagnostic: most "standard" compact simple Lie groups have finite $\pi_1$, often $\mathbb{Z}/n$ for some small $n$ — see [[Thm - Myers Theorem (Pi_1 Finite for Positive Ricci)]] and [[Riemannian Geometry III — Riemann Curvature and Topology]].

**The pattern "homotopy invariants of an algebraic structure are themselves algebraic" is the start of $\infty$-category theory.** Path components, $\pi_1$, $\pi_n$, $H_*$, $H^*$ of an $H$-space (or topological group, or Lie group) are all algebraic objects (groups, abelian groups, rings, modules) reflecting the underlying algebraic structure. This pattern, when fully exploited, is the **homotopical algebra** of $E_\infty$-spaces and infinite loop spaces. The lowest example is just commutativity of $\pi_1$; the higher examples include the *ring* structure on $H^*(BG)$ for a Lie group $G$, and the operad structure on the chains of $\Omega^\infty X$. The trigger condition: any topological space with extra algebraic structure. The transferable diagnostic: the homotopy invariants inherit a corresponding amount of structure, often more than is immediately visible.

**Whenever you see a continuous binary operation, $\pi_1$ becomes abelian without further work.** This is the most useful triggering pattern for the chapter. If a problem mentions a Lie group, a topological group, an $H$-space, or even a topological monoid, the very first observation should be: $\pi_1$ is abelian. This often closes problems instantly. For example: $\mathrm{SO}(3)$ is a Lie group, so $\pi_1(\mathrm{SO}(3))$ is abelian; we know it has 2 elements (from $\mathrm{SU}(2) \to \mathrm{SO}(3)$), so it must be $\mathbb{Z}/2$ (the only 2-element abelian group). The Eckmann-Hilton argument turns "two elements" into "$\mathbb{Z}/2$" for free.
