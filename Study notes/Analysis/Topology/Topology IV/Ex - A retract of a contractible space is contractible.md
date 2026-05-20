---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Homotopy Equivalence and Contractible Space"
  - "Def - Deformation Retract"
  - "Def - Homotopy"
tags: [analysis, topology, homotopy, contractibility, retract]
---

# Problem Statement

Let $X$ be a contractible space and $A \subseteq X$ a retract — i.e., there is a continuous retraction $r : X \to A$ with $r|_A = 1_A$ (equivalently, $r \circ i = 1_A$ where $i : A \hookrightarrow X$ is the inclusion).

Show that $A$ is also contractible.

**Recall:**

A space $X$ is [[Def - Homotopy Equivalence and Contractible Space|contractible]] if it is homotopy equivalent to a point — equivalently, the identity $1_X$ is homotopic to a constant map $c_{x_0}$ for some $x_0 \in X$.

A subset $A \subseteq X$ is a retract if there is a continuous $r : X \to A$ with $r|_A = 1_A$. (Note: this is weaker than deformation retract — we do *not* require $i \circ r \simeq 1_X$.)

---

# Convergent Strategy

**Problem class:** Transfer a homotopy property (contractibility) from an ambient space to a retract.

**Assumption pattern:** $X$ contractible gives a homotopy $H : 1_X \simeq c_{x_0}$ on $X$. The retract $r : X \to A$ gives a way to "project" everything to $A$. The composition retract ∘ (homotopy on $X$) restricts to a homotopy on $A$ from $1_A$ to a constant.

**Theorem routing:** Construct the homotopy on $A$ by composing the inclusion, the contraction homotopy on $X$, and the retraction.

**Key decision point:** What constant map does $1_A$ become homotopic to? The retraction sends the basepoint $x_0$ to some specific point $a_0 = r(x_0) \in A$, and that is the contraction target.

---

# Legal Operations Used

1. **Compose continuous maps and homotopies.** The composition of continuous maps is continuous.

2. **Restrict a homotopy.** If $H : X \times I \to X$ is a homotopy, then $H|_{A \times I} : A \times I \to X$ is also a homotopy (continuous restriction).

3. **Retract a homotopy.** Composing with the retraction $r$ sends the homotopy from $X$ to a homotopy ending in $A$.

---

# Hints

> [!note]- Hint 1
> $X$ is contractible: there is $H : X \times I \to X$ with $H(x, 0) = x$, $H(x, 1) = x_0$ for some fixed $x_0 \in X$.

> [!note]- Hint 2
> The retract $r : X \to A$ collapses $X$ down to $A$. Compose: define $G : A \times I \to A$ by $G(a, t) := r(H(i(a), t))$. The inclusion $i : A \hookrightarrow X$ is just the identity (as a set map), and $r$ projects back.

> [!note]- Hint 3
> Check endpoints:
> - $G(a, 0) = r(H(a, 0)) = r(a) = a$ (since $r|_A = 1_A$).
> - $G(a, 1) = r(H(a, 1)) = r(x_0) = a_0$, a fixed point in $A$.
>
> So $G$ is a homotopy from $1_A$ to the constant map $c_{a_0}$.

---

# Solution

The proof breaks into five short steps that transport the contraction of $X$ down to $A$ via the retraction. Step 1 invokes contractibility of $X$ to obtain a homotopy $H: 1_X \simeq c_{x_0}$; Step 2 defines $G(a, t) := r(H(a, t))$ as the candidate contraction of $A$; Steps 3–4 verify continuity (composition of continuous maps) and check the endpoint conditions $G(a, 0) = a$ (using $r|_A = 1_A$) and $G(a, 1) = r(x_0) =: a_0$; Step 5 concludes $A$ is contractible. The non-obvious move is in Step 2 — composing with $r$ at every time $t$ (rather than just at the endpoint) is what keeps the homotopy *inside* $A$, which is exactly what the retraction property of $r$ buys.

**Step 1: Set up the contraction on $X$.**

By contractibility of $X$, there is a continuous $H : X \times I \to X$ with $H(x, 0) = x$ for all $x$, and $H(x, 1) = x_0$ for some fixed $x_0 \in X$.

**Step 2: Define the contraction on $A$ via the retract.**

Let $i : A \hookrightarrow X$ be the inclusion. Define
$$G : A \times I \to A, \quad G(a, t) := r(H(i(a), t)) = r(H(a, t)).$$

**Step 3: Verify $G$ is continuous.**

> [!note]- Derivation
> $G = r \circ H \circ (i \times 1_I)$ — a composition of continuous maps. $i \times 1_I : A \times I \to X \times I$ is continuous (the inclusion in the first factor and the identity in the second). $H$ is continuous. $r$ is continuous. So $G$ is continuous.

**Step 4: Verify endpoint conditions.**

> [!note]- Derivation
> $G(a, 0) = r(H(a, 0)) = r(a) = a$ (using $r|_A = 1_A$). So $G(\cdot, 0) = 1_A$.
>
> $G(a, 1) = r(H(a, 1)) = r(x_0)$. Let $a_0 := r(x_0) \in A$. Then $G(\cdot, 1) = c_{a_0}$, the constant map at $a_0$.

**Step 5: Conclude $A$ is contractible.**

$G$ is a homotopy from $1_A$ to the constant map $c_{a_0}$. By [[Def - Homotopy Equivalence and Contractible Space]], $A$ is contractible.

> [!note]- Complete formal solution
> Choose a contraction homotopy $H : X \times I \to X$ on the contractible $X$, with $H(\cdot, 0) = 1_X$ and $H(\cdot, 1) = c_{x_0}$ for some $x_0 \in X$.
>
> Define $G : A \times I \to A$ by $G(a, t) := r(H(a, t))$. Continuous (composition of continuous maps). At $t = 0$: $G(a, 0) = r(H(a, 0)) = r(a) = a$ (retraction). At $t = 1$: $G(a, 1) = r(H(a, 1)) = r(x_0) =: a_0$, a fixed point.
>
> So $G : 1_A \simeq c_{a_0}$, hence $A$ is contractible. $\blacksquare$

---

# Key Takeaways

**Contractibility is hereditary under retraction.** Many topological properties are preserved when passing to retracts: connectedness, path-connectedness, compactness (sometimes), and (this theorem) contractibility. The reason is that a retract is, in some sense, a quotient — a continuous image of a continuous self-map — and retract-respecting properties are continuous-image-respecting.

**Construction recipe.** The proof is a single line of construction: restrict the ambient homotopy via composition with $r$. The trigger-reaction pattern: "want to show $A$ has property $P$ that $X$ has + $A$ is a retract of $X$ $\Rightarrow$ try composing the property-witnessing structure on $X$ with $r$".

**Distinction between retract and deformation retract.** A retract is a *weaker* notion than a deformation retract: we only require $r \circ i = 1_A$ (strict equality), not $i \circ r \simeq 1_X$ (homotopy to identity). For deformation retracts, we get a homotopy equivalence $A \simeq X$ automatically; for plain retracts, we don't. *But* if $X$ is contractible, then $X \simeq *$ and a retract $A$ is contractible too (this exercise) — so $A \simeq *$. Hence in the special case of contractible $X$, retract is enough to conclude $A \simeq X$ up to homotopy.

**Counterexample without contractibility.** If $X$ is not contractible, retracts can be very different from $X$. The circle $S^1$ is a retract of itself (trivially) but also a retract of nothing larger that is contractible — in fact, $S^1$ is not a retract of $D^2$ (this is the input to Brouwer's fixed-point theorem!). So the retract property interacts with contractibility in subtle ways, and this exercise is the simplest positive result.

**Application: convex sets and star-shaped sets.** Every convex set in $\mathbb{R}^n$ is contractible (linear interpolation to any point). A retract of a convex set is also contractible — even if the retract is wildly non-convex. *Example:* the unit interval $[0, 1] \subseteq \mathbb{R}^2$ is a retract of $\mathbb{R}^2$ (the retraction is the projection onto the $x$-axis restricted to $[0, 1]$, with appropriate clamping). Both are contractible.
