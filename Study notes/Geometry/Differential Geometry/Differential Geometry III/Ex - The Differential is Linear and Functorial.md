---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - The Differential of a Smooth Map"
  - "Def - The Tangent Space"
  - "Def - Derivation at a Point"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $F : M \to N$ and $G : N \to P$ be smooth maps between smooth manifolds, and let $p \in M$. Verify directly from the precomposition definition of the differential that:

(a) **Linearity.** $dF_{p} : T_{p}M \to T_{F(p)}N$ is $\mathbb{R}$-linear.

(b) **Chain rule.** $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$.

(c) **Identity rule.** $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$ for the identity map on $M$.

**Recall:**

![[Def - The Differential of a Smooth Map#The Definition]]

A [[Def - Derivation at a Point|derivation at p]] is a linear map $v : C^{\infty}(M) \to \mathbb{R}$ satisfying the Leibniz product rule $v(fg) = f(p)\,v(g) + g(p)\,v(f)$. The [[Def - The Tangent Space|tangent space TₚM]] is the real vector space of all derivations at $p$, with operations $(v_{1} + v_{2})(f) = v_{1}(f) + v_{2}(f)$ and $(cv)(f) = c\,v(f)$.

---

# Convergent Strategy

**Problem class:** This is a *verification* problem — given a definition (the differential as precomposition), verify it satisfies stated algebraic properties (linearity, chain rule, identity). The general routine for verification problems is: state the definition, unfold both sides of the proposed equality, simplify using the underlying algebraic axioms (here, the linearity and Leibniz rule of derivations and the associativity of composition), and conclude. No surprises — the proof reduces to repeated application of the definition.

**Assumption pattern:** The assumption is "$F$ and $G$ are smooth maps". The required input is exactly the precomposition definition $(dF_{p}(v))(f) = v(f \circ F)$, which is purely algebraic — no smoothness is used in the algebraic verifications below (smoothness is implicit in ensuring $f \circ F \in C^{\infty}(M)$ when $f \in C^{\infty}(N)$, but this is a standing assumption). Linearity comes from the linearity of $v$ as a map $C^{\infty}(M) \to \mathbb{R}$. The chain rule comes from associativity of function composition. The identity rule comes from $f \circ \mathrm{id} = f$.

**Theorem routing:** For each part, the route is *unfold the definition*: $(dF_{p}(v))(f) = v(f \circ F)$. (a) Linearity of $dF_{p}$ in $v$ reduces to linearity of $v$ as a derivation. (b) The chain rule reduces to the associativity $f \circ (G \circ F) = (f \circ G) \circ F$. (c) The identity rule reduces to $f \circ \mathrm{id} = f$. The argument is a one-step computation in each case — see [[Thm - Chain Rule for the Differential]] for the formal statement.

**Key decision point:** The non-obvious feature is that *all three statements follow from a single algebraic identity — the precomposition definition*. The temptation is to verify each property separately, using charts and coordinate computations. The clean approach uses only the definition; charts are unnecessary. The choice to work *coordinate-free* is the key decision; coordinate verification would be longer and obscure the structural insight.

---

# Legal Operations Used

1. **Unfolding the precomposition definition** (operation 5 from the topic page, applied without using charts). The definition $(dF_{p}(v))(f) = v(f \circ F)$ is unfolded at every step, converting the abstract differential into a derivation acting on a precomposed function. This is the only computational move needed.

2. **Linearity of derivations as maps $C^{\infty}(M) \to \mathbb{R}$**. A tangent vector $v$ is a linear operator on functions, so $v(\alpha h + \beta k) = \alpha\,v(h) + \beta\,v(k)$. We use this to commute scalars and sums through $v$.

3. **Associativity of function composition.** $f \circ (G \circ F) = (f \circ G) \circ F$ — this is the algebraic input for the chain rule. The composition of functions is associative because applying $G \circ F$ to a point means applying $F$ then $G$, regardless of bracketing.

---

# Hints

> [!note]- Hint 1
> For linearity, unfold $dF_{p}(v_{1} + v_{2})$ acting on $f$, and use the fact that $v$ is linear as a map $C^{\infty}(M) \to \mathbb{R}$.

> [!note]- Hint 2
> For the chain rule, unfold both sides on a function $f \in C^{\infty}(P)$, and use the associativity of composition $f \circ (G \circ F) = (f \circ G) \circ F$.

> [!note]- Hint 3
> For the identity rule, recognize that $f \circ \mathrm{id} = f$, so the precomposition definition immediately yields $d(\mathrm{id})_{p}(v) = v$.

---

# Solution

The proof breaks into three parts, each a one-line application of the precomposition definition. Linearity uses the linearity of $v$ as a derivation; the chain rule uses associativity of composition; the identity rule uses $f \circ \mathrm{id} = f$. The whole verification fits on one page.

**Step 1: Linearity of $dF_{p}$.**

Show that for $v_{1}, v_{2} \in T_{p}M$ and $\alpha, \beta \in \mathbb{R}$, $dF_{p}(\alpha v_{1} + \beta v_{2}) = \alpha\, dF_{p}(v_{1}) + \beta\, dF_{p}(v_{2})$.

> [!note]- Derivation
> For any $f \in C^{\infty}(N)$:
> $(dF_{p}(\alpha v_{1} + \beta v_{2}))(f) = (\alpha v_{1} + \beta v_{2})(f \circ F)$ by the precomposition definition.
> $= \alpha\,v_{1}(f \circ F) + \beta\,v_{2}(f \circ F)$ since $\alpha v_{1} + \beta v_{2}$ acts on functions as $(\alpha v_{1} + \beta v_{2})(h) = \alpha\,v_{1}(h) + \beta\,v_{2}(h)$ (linearity of the vector-space operation on $T_{p}M$).
> $= \alpha\,(dF_{p}(v_{1}))(f) + \beta\,(dF_{p}(v_{2}))(f)$ by the precomposition definition again.
>
> This holds for every $f$, so $dF_{p}(\alpha v_{1} + \beta v_{2}) = \alpha\,dF_{p}(v_{1}) + \beta\,dF_{p}(v_{2})$ as derivations at $F(p)$. Hence $dF_{p}$ is $\mathbb{R}$-linear.

**Step 2: Chain rule $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$.**

Apply both sides to a tangent vector $v \in T_{p}M$ and a function $f \in C^{\infty}(P)$.

> [!note]- Derivation
> Left side: $(d(G \circ F)_{p}(v))(f) = v(f \circ (G \circ F))$ by the precomposition definition with $G \circ F$ in place of "the map".
>
> Right side:
> $((dG_{F(p)} \circ dF_{p})(v))(f) = (dG_{F(p)}(dF_{p}(v)))(f)$ by composition.
> $= (dF_{p}(v))(f \circ G)$ by the precomposition definition for $dG_{F(p)}$, with $f \circ G$ as the function on $N$.
> $= v((f \circ G) \circ F)$ by the precomposition definition for $dF_{p}$, with $f \circ G$ as the function.
>
> The two sides differ only in the order of composition: $f \circ (G \circ F)$ versus $(f \circ G) \circ F$. By the associativity of function composition, these are equal as functions $M \to \mathbb{R}$. Applying $v$ to equal functions gives equal numbers.
>
> So $(d(G \circ F)_{p}(v))(f) = ((dG_{F(p)} \circ dF_{p})(v))(f)$ for every $f$ and every $v$. Hence $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$ as linear maps.

**Step 3: Identity rule $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$.**

Apply $d(\mathrm{id}_{M})_{p}$ to a tangent vector $v$ and a function $f$.

> [!note]- Derivation
> $(d(\mathrm{id}_{M})_{p}(v))(f) = v(f \circ \mathrm{id}_{M})$ by the precomposition definition.
> $= v(f)$ since $f \circ \mathrm{id}_{M} = f$ as functions on $M$.
>
> So $d(\mathrm{id}_{M})_{p}(v) = v$ as derivations at $p$, for every $v$. Hence $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$ as a linear map.

> [!note]- Complete formal solution
> *(a) Linearity.* For $v_{1}, v_{2} \in T_{p}M$, $\alpha, \beta \in \mathbb{R}$, and $f \in C^{\infty}(N)$:
> $$(dF_{p}(\alpha v_{1} + \beta v_{2}))(f) = (\alpha v_{1} + \beta v_{2})(f \circ F) = \alpha\,v_{1}(f \circ F) + \beta\,v_{2}(f \circ F) = \alpha\,(dF_{p}(v_{1}))(f) + \beta\,(dF_{p}(v_{2}))(f).$$
> This holds for every $f$, so $dF_{p}$ is $\mathbb{R}$-linear.
>
> *(b) Chain rule.* For $v \in T_{p}M$ and $f \in C^{\infty}(P)$:
> $$(d(G \circ F)_{p}(v))(f) = v(f \circ (G \circ F)) = v((f \circ G) \circ F) = (dF_{p}(v))(f \circ G) = (dG_{F(p)} \circ dF_{p}(v))(f),$$
> where the second equality uses associativity of composition.
>
> *(c) Identity rule.* For $v \in T_{p}M$ and $f \in C^{\infty}(M)$:
> $$(d(\mathrm{id}_{M})_{p}(v))(f) = v(f \circ \mathrm{id}_{M}) = v(f).$$
> So $d(\mathrm{id}_{M})_{p}(v) = v$ for every $v$, i.e., $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$.
>
> All three parts follow directly from the precomposition definition and the linearity-and-associativity of the underlying algebraic operations. $\qquad\blacksquare$

---

# Key Takeaways

**The precomposition definition is the right one — everything follows by unfolding it.** This exercise illustrates the design principle of the precomposition definition $(dF_{p}(v))(f) = v(f \circ F)$: it is set up so that linearity, the chain rule, and the identity rule are *all* one-line consequences. Other natural-looking definitions of the differential (via charts, via curves, via Taylor expansions) would require longer proofs of these basic properties. The lesson is that "choose the definition that makes the theorems trivial" is a real strategy in mathematics; the precomposition definition is its own justification because of how cleanly it yields the algebraic content. When proving anything about $dF$ at the abstract level, your first move should be to unfold the precomposition definition — that almost always works.

**Functoriality is the deeper statement.** The chain rule and identity rule together say that the tangent-space construction is a *functor* from pointed smooth manifolds to vector spaces. Functoriality is not just a name for these two properties — it is the categorical content that makes the tangent-space construction *natural*: any reasonable construction defined in terms of tangent spaces and differentials is automatically coordinate-independent and well-behaved under composition. The fact that this exercise verifies the functor axioms means it is establishing the *most fundamental property of differential geometry*, dressed up in a simple computational form.

**Associativity of composition is the algebraic input for the chain rule.** The chain rule may look like a calculus statement (about derivatives of compositions), but its proof uses no calculus — only the associativity $f \circ (G \circ F) = (f \circ G) \circ F$, which is a pure set-theoretic property. The "calculus" content is hidden in the definition of $dF_{p}$ via precomposition with $F$, which is itself an algebraic construction. This is why the chain rule generalizes to any setting where one has "morphisms" and "linear operators dual to precomposition" — for instance, in algebraic geometry where morphisms of schemes induce maps of structure sheaves, and the chain rule follows from associativity.
