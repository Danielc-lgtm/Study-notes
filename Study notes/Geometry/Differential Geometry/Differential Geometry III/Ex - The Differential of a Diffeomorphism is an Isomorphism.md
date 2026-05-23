---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Diffeomorphism"
  - "Def - The Differential of a Smooth Map"
  - "Thm - Chain Rule for the Differential"
  - "Def - Linear Map"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $F : M \to N$ be a [[Def - Diffeomorphism|diffeomorphism]] between smooth manifolds, and let $p \in M$.

(a) Show that $dF_{p} : T_{p}M \to T_{F(p)}N$ is a vector-space isomorphism, with inverse $(dF_{p})^{-1} = d(F^{-1})_{F(p)}$.

(b) Conclude that diffeomorphic manifolds have the same [[Def - Dimension|dimension]].

**Recall:**

A **diffeomorphism** $F : M \to N$ is a smooth bijection between smooth manifolds whose inverse $F^{-1}$ is also smooth. See [[Def - Diffeomorphism]].

![[Def - The Differential of a Smooth Map#The Definition]]

The chain rule for the differential: $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$, and $d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$ — see [[Thm - Chain Rule for the Differential]].

The [[Thm - Dimension of the Tangent Space|dimension theorem]]: $\dim T_{p}M = \dim M$ for every $p \in M$.

---

# Convergent Strategy

**Problem class:** This is a *functoriality application* problem — use the chain rule and identity rule to deduce that a smooth map with a smooth inverse must have a linear-isomorphism differential. The general routine is: take a smooth identity (here $F \circ F^{-1} = \mathrm{id}$), apply the chain rule to differentiate it, and read off the linear-algebra conclusion (here that $dF_{p}$ has a two-sided inverse).

**Assumption pattern:** $F$ is smooth and has smooth inverse $F^{-1}$, so both $F \circ F^{-1} = \mathrm{id}_{N}$ and $F^{-1} \circ F = \mathrm{id}_{M}$ are valid smooth-map identities. These are the algebraic inputs. The chain rule and identity rule for the differential are the tools.

**Theorem routing:** Apply the [[Thm - Chain Rule for the Differential|chain rule]] to $F \circ F^{-1} = \mathrm{id}_{N}$ at the point $F(p)$, giving $dF_{p} \circ d(F^{-1})_{F(p)} = d(\mathrm{id}_{N})_{F(p)} = \mathrm{id}_{T_{F(p)}N}$. Similarly apply it to $F^{-1} \circ F = \mathrm{id}_{M}$ at $p$, giving $d(F^{-1})_{F(p)} \circ dF_{p} = \mathrm{id}_{T_{p}M}$. The two equations together say $d(F^{-1})_{F(p)}$ is the two-sided inverse of $dF_{p}$, hence $dF_{p}$ is a vector-space isomorphism. For part (b), apply the [[Thm - Dimension of the Tangent Space|dimension theorem]]: an isomorphism between vector spaces forces equal [[Def - Dimension|dimensions]], hence $\dim T_{p}M = \dim T_{F(p)}N$, hence $\dim M = \dim N$.

**Key decision point:** The non-obvious feature is that *both directions of the inverse* are needed — one application of the chain rule gives one direction; the other direction comes from the *other* composition $F^{-1} \circ F$. The temptation is to apply the chain rule once and declare victory, forgetting that linear-map inversion is a two-sided condition. The choice to apply the chain rule *twice* — once to each composition — is the decisive move.

---

# Legal Operations Used

1. **Apply the chain rule to a composition of smooth maps** (operation 5 from the topic page). The compositions $F \circ F^{-1} = \mathrm{id}_{N}$ and $F^{-1} \circ F = \mathrm{id}_{M}$ are smooth-map identities; differentiating them via the chain rule converts each into a linear-map identity.

2. **Use the identity rule.** The differential of the identity map is the identity, so the right-hand side of each chain-rule application becomes the identity linear map.

3. **Recognize a two-sided inverse.** A linear map between vector spaces is an isomorphism iff it has a two-sided inverse. Both compositions give the same inverse $d(F^{-1})_{F(p)}$.

4. **Apply the dimension theorem.** A linear isomorphism between vector spaces preserves dimension, hence $\dim M = \dim N$ for diffeomorphic manifolds.

---

# Hints

> [!note]- Hint 1
> Recall that $F \circ F^{-1} = \mathrm{id}_{N}$ and $F^{-1} \circ F = \mathrm{id}_{M}$ since $F$ is a diffeomorphism. Apply the chain rule to each composition.

> [!note]- Hint 2
> Use the identity rule $d(\mathrm{id})_{p} = \mathrm{id}_{T_{p}M}$ to simplify the right-hand sides.

> [!note]- Hint 3
> A linear map with a two-sided inverse is an isomorphism. Conclude that $\dim T_{p}M = \dim T_{F(p)}N$, and hence $\dim M = \dim N$ via the dimension theorem.

---

# Solution

The proof proceeds in two steps. Apply the chain rule to $F \circ F^{-1} = \mathrm{id}_{N}$ and to $F^{-1} \circ F = \mathrm{id}_{M}$ to get two compositions of differentials equal to identity linear maps. Read off that $dF_{p}$ has a two-sided inverse, hence is a vector-space isomorphism. Conclude that diffeomorphic manifolds have equal dimension via the dimension theorem.

**Step 1: $dF_{p} \circ d(F^{-1})_{F(p)} = \mathrm{id}_{T_{F(p)}N}$.**

Apply the chain rule to $F \circ F^{-1} = \mathrm{id}_{N}$ at $F(p)$.

> [!note]- Derivation
> Since $F$ is a diffeomorphism, $F^{-1}$ is smooth and $F \circ F^{-1} = \mathrm{id}_{N}$. Apply the chain rule (Theorem 3.6(b) of Lee, or [[Thm - Chain Rule for the Differential]]) at the point $F(p) \in N$:
> $$d(F \circ F^{-1})_{F(p)} = dF_{F^{-1}(F(p))} \circ d(F^{-1})_{F(p)} = dF_{p} \circ d(F^{-1})_{F(p)}.$$
> But $F \circ F^{-1} = \mathrm{id}_{N}$, so by the identity rule, $d(F \circ F^{-1})_{F(p)} = d(\mathrm{id}_{N})_{F(p)} = \mathrm{id}_{T_{F(p)}N}$. Therefore $dF_{p} \circ d(F^{-1})_{F(p)} = \mathrm{id}_{T_{F(p)}N}$.

**Step 2: $d(F^{-1})_{F(p)} \circ dF_{p} = \mathrm{id}_{T_{p}M}$.**

Apply the chain rule to $F^{-1} \circ F = \mathrm{id}_{M}$ at $p$.

> [!note]- Derivation
> Similarly, $F^{-1} \circ F = \mathrm{id}_{M}$. Apply the chain rule at $p \in M$:
> $$d(F^{-1} \circ F)_{p} = d(F^{-1})_{F(p)} \circ dF_{p}.$$
> But $F^{-1} \circ F = \mathrm{id}_{M}$, so $d(F^{-1} \circ F)_{p} = d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}$. Therefore $d(F^{-1})_{F(p)} \circ dF_{p} = \mathrm{id}_{T_{p}M}$.

**Step 3: $dF_{p}$ is a vector-space isomorphism.**

Combine Steps 1 and 2 to conclude.

> [!note]- Derivation
> By Steps 1 and 2, the linear map $d(F^{-1})_{F(p)}$ is a two-sided inverse of $dF_{p}$:
> $$dF_{p} \circ d(F^{-1})_{F(p)} = \mathrm{id}_{T_{F(p)}N}, \qquad d(F^{-1})_{F(p)} \circ dF_{p} = \mathrm{id}_{T_{p}M}.$$
> Hence $dF_{p}$ is a linear bijection $T_{p}M \to T_{F(p)}N$, i.e., a vector-space isomorphism, with $(dF_{p})^{-1} = d(F^{-1})_{F(p)}$.

**Step 4: $\dim M = \dim N$.**

Apply the dimension theorem.

> [!note]- Derivation
> By [[Thm - Dimension of the Tangent Space|the dimension theorem]], $\dim T_{p}M = \dim M$ and $\dim T_{F(p)}N = \dim N$. Since $dF_{p}$ is a linear isomorphism between $T_{p}M$ and $T_{F(p)}N$, the two vector spaces have equal dimension: $\dim T_{p}M = \dim T_{F(p)}N$. Combining: $\dim M = \dim N$.

> [!note]- Complete formal solution
> *Part (a).* Since $F$ is a diffeomorphism, $F^{-1}$ is smooth, and we have $F \circ F^{-1} = \mathrm{id}_{N}$ and $F^{-1} \circ F = \mathrm{id}_{M}$ as smooth maps.
>
> Applying the chain rule (Theorem 3.6(b) of Lee) at $F(p) \in N$:
> $$dF_{p} \circ d(F^{-1})_{F(p)} = d(F \circ F^{-1})_{F(p)} = d(\mathrm{id}_{N})_{F(p)} = \mathrm{id}_{T_{F(p)}N}.$$
>
> Applying the chain rule at $p \in M$:
> $$d(F^{-1})_{F(p)} \circ dF_{p} = d(F^{-1} \circ F)_{p} = d(\mathrm{id}_{M})_{p} = \mathrm{id}_{T_{p}M}.$$
>
> Hence $dF_{p}$ has the two-sided inverse $d(F^{-1})_{F(p)}$, so $dF_{p}$ is a vector-space isomorphism.
>
> *Part (b).* By the [[Thm - Dimension of the Tangent Space|dimension theorem]], $\dim T_{p}M = \dim M$ and $\dim T_{F(p)}N = \dim N$. Since $dF_{p}$ is a linear isomorphism between vector spaces, $\dim T_{p}M = \dim T_{F(p)}N$. Therefore $\dim M = \dim N$. $\qquad\blacksquare$

---

# Key Takeaways

**Differentials of [[Def - Diffeomorphism|diffeomorphisms]] are [[Def - Isomorphism|isomorphisms]] — this is the operational consequence of functoriality.** The theorem this exercise proves is one of the most-used facts in differential geometry: any time you have a diffeomorphism, the tangent-space structure pushes forward isomorphically. This is what licenses the use of charts as "tangent-space [[Def - Isomorphism|isomorphisms]]": a chart is a diffeomorphism, so its differential is an isomorphism, so the chart provides $T_{p}M \cong T_{\varphi(p)}\mathbb{R}^{n}$ canonically. The pattern recurs: a coordinate change between two charts induces an isomorphism between the two coordinate-basis identifications of $T_{p}M$; a diffeomorphism of Lie [[Def - Group|groups]] induces a Lie-algebra isomorphism; a diffeomorphism of Riemannian manifolds induces a metric-preserving isomorphism of tangent spaces (an [[Def - Isometry|isometry]]). Reach for this conclusion whenever you have a diffeomorphism and want to transport some tangent-space construction.

**[[Def - Diffeomorphism|Diffeomorphism]] invariance of dimension is a deep topological fact.** That diffeomorphic manifolds have the same dimension may seem obvious — surely two diffeomorphic things have the same "size"? But the topological version (that two homeomorphic manifolds have the same dimension) is much harder to prove (it requires invariance of domain or Brouwer's theorem). The differentiable version is *easy* by the present argument, which uses only the chain rule. This illustrates a recurring theme: smooth structure can simplify things that are hard at the merely topological level. Differential topology often proves theorems that algebraic topology only proves via cohomology — the chain rule does for dimension what excision does for cohomology.

**The "double-sided inverse" pattern is everywhere.** This exercise's argument structure — "if $G \circ F = \mathrm{id}$ and $F \circ G = \mathrm{id}$, then $F$ is an isomorphism with inverse $G$" — is the fundamental pattern for recognizing isomorphisms in any category. The chain rule + identity rule is what lets the pattern work for differentials. The same pattern recurs in: showing a map is a [[Def - Homeomorphism|homeomorphism]] (two-sided inverse), showing a [[Def - Group|group]] homomorphism is an isomorphism (two-sided inverse), showing a chain map is a quasi-isomorphism (induces an inverse on homology). Whenever you need to show something is an isomorphism in a categorical sense, look for two compositions that equal the appropriate identity — exactly as in this exercise.
