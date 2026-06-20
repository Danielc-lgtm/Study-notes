---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Stable Module Category over a Frobenius Ring"
  - "Def - Projective Module"
  - "Def - Module"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $R$ be a Frobenius ring. Show that $\operatorname{PHom}(M, N)$ — the set of $R$-module maps $M \to N$ that factor through a [[Def - Projective Module|projective]] module — is a subgroup of $\operatorname{Hom}(M, N)$, and that it is a **two-sided ideal** of the category: closed under pre-composition and post-composition with arbitrary module maps. Conclude that the [[Def - Stable Module Category over a Frobenius Ring|stable module category]] $\underline{\mathbf{Mod}}_R$, with morphisms $\underline{\operatorname{Hom}}(M, N) = \operatorname{Hom}(M,N)/\operatorname{PHom}(M,N)$, is a well-defined category.

**Recall:**

A map $f : M \to N$ is in $\operatorname{PHom}(M, N)$ if $f = \beta \alpha$ for some $\alpha : M \to P$, $\beta : P \to N$ with $P$ projective. A [[Def - Projective Module|projective module]] is a direct summand of a free module; finite direct sums of projectives are projective. A **two-sided ideal of morphisms** $\mathcal{I}$ assigns to each pair $(M,N)$ a subgroup $\mathcal{I}(M,N) \subseteq \operatorname{Hom}(M,N)$ such that $g \circ f \circ h \in \mathcal{I}$ whenever $f \in \mathcal{I}$ and $g, h$ are arbitrary composable maps; the quotient by such an ideal is a category. See [[Def - Stable Module Category over a Frobenius Ring]].

---

# Convergent Strategy

**Problem class:** This is a "well-definedness of a quotient construction" problem — verifying that the stable module category is actually a category. The routine is to check the ideal axioms (subgroup, two-sided absorption) directly from the factor-through-a-projective definition.

**Assumption pattern:** The recognisable structure is "morphisms modulo an ideal". The assumptions are the closure properties of projectives: a finite direct sum of projectives is projective, and a composite through a projective stays through a projective. These are what make $\operatorname{PHom}$ a subgroup and an ideal.

**Theorem routing:** Subgroup: the sum of two maps through projectives factors through the direct sum, which is projective. Two-sided ideal: pre/post-composing a map-through-$P$ with anything still factors through $P$. Quotient is a category: a morphism-ideal quotient is always a category, with composition induced because the ideal absorbs on both sides.

**Key decision point:** The non-obvious step is the *subgroup* (additivity) check: the sum $f + g$ of two maps through projectives $P, Q$ factors through $P \oplus Q$, using that $P \oplus Q$ is projective. Recognising that you must pass to the *direct sum* to factor a sum — rather than expecting a single projective to work — is the decision that makes the additivity proof go through.

---

# Legal Operations Used

1. **Operation 7 from the topic page (quotient out maps through projectives).** The entire exercise verifies that this operation produces a well-defined category.

---

# Hints

> [!note]- Hint 1
> To show $\operatorname{PHom}$ is closed under addition: if $f$ factors through $P$ and $g$ through $Q$, through what single projective does $f + g$ factor? Consider $P \oplus Q$.

> [!note]- Hint 2
> For the two-sided absorption: if $f = \beta\alpha$ with $P$ projective, and $h : M' \to M$, $g : N \to N'$ are arbitrary, write $g \circ f \circ h$ as a factorization through the same $P$. Which maps change?

> [!note]- Hint 3
> A quotient of a category by a two-sided ideal of morphisms is automatically a category: composition $[g]\circ[f] = [g\circ f]$ is well-defined precisely because the ideal absorbs on both sides. Spell out why $[g\circ f]$ does not depend on representatives.

---

# Solution

The proof checks the two ideal axioms from the factor-through-projective definition: additivity via the direct sum of projectives, and two-sided absorption by composing the witnessing factorization with the new maps. The quotient is then a category by the general fact about morphism-ideals.

**Step 1: $\operatorname{PHom}(M,N)$ is a subgroup of $\operatorname{Hom}(M,N)$.**

> [!note]- Derivation
> The zero map factors through the zero module $0$, which is projective, so $0 \in \operatorname{PHom}$. Closure under negation: if $f = \beta\alpha$ through $P$, then $-f = (-\beta)\alpha$ through $P$.
>
> Closure under addition is the substantive part. Suppose $f = \beta\alpha$ with $\alpha : M \to P$, $\beta : P \to N$, $P$ projective, and $g = \delta\gamma$ with $\gamma : M \to Q$, $\delta : Q \to N$, $Q$ projective. Form the [[Def - Projective Module|projective]] module $P \oplus Q$ (a finite direct sum of projectives is projective). Define
> $$\alpha \oplus \gamma : M \to P \oplus Q, \quad m \mapsto (\alpha(m), \gamma(m)), \qquad [\beta, \delta] : P \oplus Q \to N, \quad (p, q) \mapsto \beta(p) + \delta(q).$$
> Then $[\beta, \delta] \circ (\alpha \oplus \gamma)(m) = \beta(\alpha(m)) + \delta(\gamma(m)) = f(m) + g(m)$, so $f + g$ factors through the projective $P \oplus Q$, hence $f + g \in \operatorname{PHom}(M,N)$. Therefore $\operatorname{PHom}(M,N)$ is a subgroup.

**Step 2: $\operatorname{PHom}$ is a two-sided ideal.**

> [!note]- Derivation
> Let $f = \beta\alpha \in \operatorname{PHom}(M, N)$ with $P$ projective, and let $h : M' \to M$ and $g : N \to N'$ be arbitrary module maps. Then
> $$g \circ f \circ h = g \circ \beta \circ \alpha \circ h = (g\beta) \circ (\alpha h),$$
> with $\alpha h : M' \to P$ and $g\beta : P \to N'$, a factorization through the *same* projective $P$. Hence $g \circ f \circ h \in \operatorname{PHom}(M', N')$. So $\operatorname{PHom}$ absorbs composition on both sides: it is a two-sided ideal of morphisms.

**Step 3: the quotient is a category.**

> [!note]- Derivation
> Define $\underline{\mathbf{Mod}}_R$ with the same objects as $\mathbf{Mod}_R$ and $\underline{\operatorname{Hom}}(M,N) = \operatorname{Hom}(M,N)/\operatorname{PHom}(M,N)$. Composition is $[g] \circ [f] := [g \circ f]$. This is well-defined: if $f' = f + p$ with $p \in \operatorname{PHom}$ and $g' = g + q$ with $q \in \operatorname{PHom}$, then
> $$g' f' = (g + q)(f + p) = gf + gp + qf + qp,$$
> and each of $gp, qf, qp$ lies in $\operatorname{PHom}$ by the two-sided ideal property (Step 2), so $[g'f'] = [gf]$. Identities are $[\mathrm{id}_M]$, and associativity is inherited from $\mathbf{Mod}_R$. Hence $\underline{\mathbf{Mod}}_R$ is a category (in fact additive, since each $\underline{\operatorname{Hom}}$ is a quotient of an abelian group by a subgroup, and composition is bilinear modulo $\operatorname{PHom}$).

> [!note]- Complete formal solution
> $\operatorname{PHom}(M,N)$ contains $0$ (factors through $0$), is closed under negation ($-\beta\alpha = (-\beta)\alpha$), and under addition: $f = \beta\alpha$ through $P$ and $g = \delta\gamma$ through $Q$ give $f + g = [\beta,\delta]\circ(\alpha\oplus\gamma)$ through the projective $P \oplus Q$. So it is a subgroup. It is a two-sided ideal: $g(\beta\alpha)h = (g\beta)(\alpha h)$ factors through the same $P$. Therefore $\underline{\operatorname{Hom}}(M,N) = \operatorname{Hom}(M,N)/\operatorname{PHom}(M,N)$ with $[g]\circ[f] = [gf]$ is well-defined (the error terms $gp, qf, qp$ lie in $\operatorname{PHom}$), giving a category $\underline{\mathbf{Mod}}_R$. $\blacksquare$

---

# Key Takeaways

**To kill a class of objects in a category, kill the maps that factor through them — and check it forms a two-sided ideal.** The construction here is the universal recipe for "quotienting out" a subcategory: rather than deleting objects, you delete morphisms that pass through them, and the result is a category exactly when those morphisms form a two-sided ideal. The two checks — subgroup (additivity) and two-sided absorption — are the ideal axioms, and they are what you verify every time. The trigger is "make these objects negligible / zero"; the reaction is "form the ideal of maps factoring through them and quotient". This same construction produces the homotopy category of any model category (kill the null-homotopic maps), the Calkin algebra (kill compact operators), and the stable category here (kill maps through projectives).

**Additivity of a morphism-ideal always routes through the direct sum.** The subtle step — that the sum of two maps through projectives factors through a *single* projective — is solved by passing to the direct sum $P \oplus Q$, using that direct sums of projectives are projective. This is a recurring pattern: whenever you must show a class of morphisms defined by "factors through an object of type $\mathcal{T}$" is closed under addition, the move is to factor the sum through the direct sum of the two witnessing objects, which works precisely when $\mathcal{T}$ is closed under finite direct sums. The diagnostic: a "factors-through" class is a subgroup if and only if the target class is closed under finite biproducts, and the proof is always the biproduct factorization.

**Two-sided absorption is what makes composition descend to the quotient.** The reason $[g]\circ[f] = [gf]$ is well-defined is exactly that $\operatorname{PHom}$ absorbs composition on both sides — the cross-terms $gp$, $qf$, $qp$ all land back in the ideal. This is the categorical analogue of the fact that a ring quotient $R/I$ is a ring only when $I$ is a two-sided ideal; here the "ring" is the (many-object) category and the "ideal" is $\operatorname{PHom}$. The transferable principle: a quotient of a category by a collection of morphisms is a category if and only if that collection is a two-sided ideal, and the verification is always the same bilinear expansion showing the error terms stay in the ideal. Recognising a construction as "category modulo a morphism-ideal" immediately tells you the one thing to check.
