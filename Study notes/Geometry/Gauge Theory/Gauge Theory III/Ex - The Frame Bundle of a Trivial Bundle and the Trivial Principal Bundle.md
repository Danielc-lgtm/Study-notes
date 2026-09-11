---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Frame Bundle of a Vector Bundle"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Def - Principal G-Bundle"
  - "Def - Vector Bundle"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M$ be a smooth manifold and let $\underline{\mathbb{R}}^k := M \times \mathbb{R}^k$ denote the **trivial** real vector bundle of rank $k$ over $M$, with projection $\operatorname{pr}_1 : M \times \mathbb{R}^k \to M$ onto the first factor and fibre $E_m = \{m\} \times \mathbb{R}^k$ over $m \in M$. Write $GL_k(\mathbb{R})$ for the Lie group of invertible real $k \times k$ matrices, acting on the frames of a vector bundle on the right by precomposition. Prove the following.

**(a) The frame bundle of the trivial bundle is the trivial principal bundle.** There is an isomorphism of principal $GL_k(\mathbb{R})$-bundles over $M$
$$\operatorname{Fr}(M \times \mathbb{R}^k) \;\cong\; M \times GL_k(\mathbb{R}),$$
that is, a diffeomorphism $\Phi : M \times GL_k(\mathbb{R}) \to \operatorname{Fr}(M \times \mathbb{R}^k)$ that covers the identity of $M$ and is $GL_k(\mathbb{R})$-equivariant, $\Phi\big((m, h) \cdot h'\big) = \Phi(m, h) \cdot h'$ for all $m \in M$ and $h, h' \in GL_k(\mathbb{R})$.

**(b) A global frame is a global section, and this is exactly what makes the trivial bundle's frame bundle trivial.** For an arbitrary rank-$k$ vector bundle $E \to M$, show that a smooth global section $\sigma : M \to \operatorname{Fr}(E)$ of the frame bundle is the same datum as a smooth global frame $(\sigma_1, \dots, \sigma_k)$ of $E$; deduce, using the correspondence between sections and triviality of a principal bundle, that $\operatorname{Fr}(E)$ is trivial if and only if $E$ is trivial. Exhibit the tautological global section of $\operatorname{Fr}(M \times \mathbb{R}^k)$ that realises the trivial bundle as its own witness, and check that the trivialisation it induces is precisely the isomorphism $\Phi$ of part (a).

This is Haydys's construction of the frame bundle (Definition unlabelled, pp. 11–12, our item **D2.2.2**) run on the simplest possible input, together with his Exercise 25 (**X2.2.1**) — the section–triviality correspondence — applied to it. The point is to see, in the one case where every object can be written down explicitly, that the frame-bundle construction sends the trivial vector bundle to the trivial principal bundle, and that the abstract equivalence "global section $\iff$ triviality" reduces here to the tautology "the standard basis is a global frame".

**Recall:**

The objects in play are the frame bundle of a vector bundle, the notion of a principal $G$-bundle and of an isomorphism of principal bundles, and the correspondence between sections and triviality.

![[Def - Frame Bundle of a Vector Bundle#The Definition]]

For the trivial bundle $E = M \times \mathbb{R}^k$ the fibre over $m$ is $E_m = \{m\} \times \mathbb{R}^k$, and we write $\iota_m : \mathbb{R}^k \xrightarrow{\ \cong\ } E_m$ for the canonical linear isomorphism $\iota_m(x) = (m, x)$. A [[Def - Frame Bundle of a Vector Bundle|frame]] of $E_m$ is then a linear isomorphism $p : \mathbb{R}^k \to E_m$, and $\iota_m^{-1} \circ p : \mathbb{R}^k \to \mathbb{R}^k$ is an element of $GL_k(\mathbb{R})$; the right action of $GL_k(\mathbb{R})$ on frames is $p \cdot h = p \circ h$.

![[Def - Principal G-Bundle#The Definition]]

An **isomorphism of principal $G$-bundles** $P \to P'$ over $M$ is a diffeomorphism $\Phi : P \to P'$ that covers the identity of $M$ (so $\pi' \circ \Phi = \pi$) and is $G$-equivariant, $\Phi(p \cdot g) = \Phi(p) \cdot g$ for all $p \in P$, $g \in G$; a bundle isomorphic to $M \times G$ (with $\operatorname{pr}_1$ as projection and $G$ acting by right multiplication on the second factor) is called **trivial**.

![[Thm - Sections of a Principal Bundle and Triviality#Statement]]

We use parts (ii) and (iii): a principal $G$-bundle is trivial if and only if it admits a global section, and a vector bundle $E$ is trivial if and only if its frame bundle $\operatorname{Fr}(E)$ admits a global section.

---

# Convergent Strategy

**Problem class.** This is a *compute-the-frame-bundle-of-an-explicit-bundle* problem, the base case of the frame-bundle construction. Its shape is: an object is defined by a chart-by-chart recipe, and we are asked to evaluate it on an input where the charts collapse to a single global chart, so that the recipe produces a formula rather than an atlas. The strategic content is not a clever idea but the discipline of writing the general construction and specialising each clause; the interest is that the two halves of the problem — the explicit isomorphism in (a) and the abstract section–triviality equivalence in (b) — turn out to be the same statement seen from two directions.

**Assumption pattern.** The only hypothesis is that the bundle is trivial, and it is used in exactly one way: a trivial vector bundle admits a *global* frame, namely the constant frame $e_0(m) = \iota_m$ built from the standard basis of $\mathbb{R}^k$ in every fibre. A global frame is what makes the frame bundle admit a single global chart $\Psi_M$ instead of a genuine atlas, and it is what supplies the global section demanded by the section–triviality theorem. Recognising "trivial vector bundle $\leadsto$ global frame $\leadsto$ global section of $\operatorname{Fr}$" is the whole recognition step.

**Theorem routing.** For part (a) the route is: take the definition of $\operatorname{Fr}(E)$; note that for $E = M \times \mathbb{R}^k$ the constant frame $e_0$ is a global local frame, so the single chart $\Psi_M(m, h) = e_0(m) \circ h$ of [[Def - Frame Bundle of a Vector Bundle|the frame-bundle definition, equation (24)]] is defined over all of $M$; verify by hand that this $\Psi_M =: \Phi$ satisfies the four requirements of an isomorphism of principal bundles (covers the identity, bijective, a diffeomorphism, equivariant). For part (b) the route is: unwind the definition of a section of $\operatorname{Fr}(E)$ into a global frame; then invoke [[Thm - Sections of a Principal Bundle and Triviality|the section–triviality correspondence]], part (ii) ($P$ trivial $\iff$ $P$ has a global section) and part (iii) ($E$ trivial $\iff$ $\operatorname{Fr}(E)$ has a global section), to convert the existence of the global frame into the triviality of $\operatorname{Fr}(E)$.

**Key decision point.** The one genuine decision is to *identify the isomorphism $\Phi$ of part (a) with the single chart $\Psi_M$ of the frame-bundle construction*, rather than inventing a new map. Once one sees that the trivial bundle has a global frame, the chart $\Psi_M$ is already defined over all of $M$ and is already equivariant and a diffeomorphism by the general construction, so there is nothing left to build. The second, smaller decision is to notice that the tautological section $\sigma_0(m) = e_0(m) = \iota_m$ and the isomorphism $\Phi$ are related by $\Phi(m, h) = \sigma_0(m) \cdot h$, which is exactly the trivialisation-from-a-section formula $\psi^{-1}(m, g) = s(m) \cdot g$ of the section–triviality theorem: parts (a) and (b) are one construction, and seeing this is the payoff of the exercise.

---

# Legal Operations Used

The operations below are the legal moves of [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles|the topic page's Legal Operations]], applied here; where the topic page is not yet assembled they are named descriptively.

1. **Specialise a bundle construction to the trivial bundle by producing a global frame.** The frame-bundle atlas is built from local frames; on $M \times \mathbb{R}^k$ the constant frame $e_0(m) = \iota_m$ is global, so the atlas collapses to a single global chart. This is the move that turns the general recipe into a closed formula.

2. **Read a point of $\operatorname{Fr}(E)$ over $m$ as an isomorphism $\mathbb{R}^k \to E_m$.** Throughout we use the isomorphism picture of a frame (rather than the ordered-basis picture), because it makes the right action $p \cdot h = p \circ h$ a composition and the equivariance check a one-line associativity computation.

3. **Verify an isomorphism of principal bundles clause by clause.** To certify a map $\Phi$ as an isomorphism of principal $G$-bundles, check separately that it covers the identity of the base, is a bijection, is a diffeomorphism, and is $G$-equivariant; each is checked directly from the definitions.

4. **Convert a global frame into a global section of the frame bundle, and back.** A smooth section of $\operatorname{Fr}(E)$ assigns a frame to each point smoothly, which is exactly a global frame of $E$; this dictionary is used in both directions in part (b).

5. **Invoke the section–triviality correspondence to pass between "has a global section" and "is trivial".** With a global section in hand, [[Thm - Sections of a Principal Bundle and Triviality|the correspondence]] supplies triviality (part (ii)), and conversely; and part (iii) transfers this between $E$ and $\operatorname{Fr}(E)$.

---

# Hints

> [!note]- Hint 1
> What is a frame of the fibre $E_m = \{m\} \times \mathbb{R}^k$ of the trivial bundle? It is a linear isomorphism $p : \mathbb{R}^k \to \{m\} \times \mathbb{R}^k$. There is a canonical such isomorphism, $\iota_m(x) = (m, x)$; compose your $p$ with $\iota_m^{-1}$ and you land in $GL_k(\mathbb{R})$. So a frame over $m$ *is* a matrix, once you strip off the harmless $\iota_m$. This already suggests the map $M \times GL_k(\mathbb{R}) \to \operatorname{Fr}(E)$ you want.

> [!note]- Hint 2
> Do not build a new map for part (a). The trivial bundle has a global frame — the constant frame $e_0(m) = \iota_m$ (the standard basis of $\mathbb{R}^k$ in every fibre). Look at the single chart of the frame-bundle definition, $\Psi_U(m, h) = e(m) \circ h$, with $U = M$ and $e = e_0$. Because $e_0$ is defined over *all* of $M$, this chart is a global map. Set $\Phi := \Psi_M$ and check it is an isomorphism of principal bundles.

> [!note]- Hint 3
> For equivariance, remember the right action on frames is precomposition, $p \cdot h' = p \circ h'$. Then $\Phi(m, h) \cdot h' = (\iota_m \circ h) \circ h' = \iota_m \circ (h h') = \Phi(m, h h')$ by associativity of composition — that is all equivariance is here. For "diffeomorphism", note that $\Phi$ is literally the chart $\Psi_M$ of $\operatorname{Fr}(E)$, so it is a diffeomorphism by the very construction of the smooth structure.

> [!note]- Hint 4
> For part (b), a global section $\sigma : M \to \operatorname{Fr}(E)$ assigns to each $m$ a frame $\sigma(m)$ of $E_m$, smoothly; writing $\sigma_j(m) := \sigma(m)(\hat{e}_j)$ turns $\sigma$ into a $k$-tuple of smooth sections that is a basis at each point — a global frame — and every global frame arises this way. Now feed this into [[Thm - Sections of a Principal Bundle and Triviality|the section–triviality theorem]]: existence of a global section is equivalent to triviality (part (ii)), and part (iii) says this holds for $\operatorname{Fr}(E)$ exactly when $E$ is trivial. For the trivial bundle the tautological section is $\sigma_0(m) = \iota_m$; check that $\Phi(m, h) = \sigma_0(m) \cdot h$.

---

# Solution

The plan is to do both parts by writing down the constant global frame $e_0(m) = \iota_m$ of the trivial bundle and reading everything off it. In part (a) this frame turns the single chart $\Psi_M$ of the frame-bundle construction into a globally defined map $\Phi$, which we certify as an isomorphism of principal bundles by checking the four defining clauses directly. In part (b) the same frame is the tautological global section $\sigma_0$ of $\operatorname{Fr}(E)$, and the section–triviality theorem converts its existence into the triviality of $\operatorname{Fr}(M \times \mathbb{R}^k)$; we close by observing that $\Phi(m, h) = \sigma_0(m) \cdot h$, so the two parts are one construction.

## Part (a)

**Step 1: Write down the constant global frame and the induced global map $\Phi$.**

The trivial bundle $E = M \times \mathbb{R}^k$ has a global frame, and the frame-bundle chart it determines is defined over all of $M$; call it $\Phi$.

> [!note]- Derivation
> We must produce an isomorphism $\Phi : M \times GL_k(\mathbb{R}) \to \operatorname{Fr}(M \times \mathbb{R}^k)$ of principal $GL_k(\mathbb{R})$-bundles over $M$.
>
> For each $m \in M$ let $\iota_m : \mathbb{R}^k \to E_m = \{m\} \times \mathbb{R}^k$ be the canonical linear isomorphism $\iota_m(x) = (m, x)$. The tuple $e_0 = (e_{0,1}, \dots, e_{0,k})$ with $e_{0,j}(m) := \iota_m(\hat{e}_j) = (m, \hat{e}_j)$ (where $\hat{e}_1, \dots, \hat{e}_k$ is the standard basis of $\mathbb{R}^k$) is a smooth **global frame** of $E$: each $e_{0,j}$ is a smooth section of $M \times \mathbb{R}^k$, and $(e_{0,1}(m), \dots, e_{0,k}(m)) = (\iota_m(\hat{e}_1), \dots, \iota_m(\hat{e}_k))$ is a basis of $E_m$ at every $m$ because $\iota_m$ is an isomorphism. Viewed as a map into the frame bundle, $e_0(m) = \iota_m \in \operatorname{Fr}(E_m)$.
>
> By the definition of the frame bundle, any local frame $e$ over an open set $U$ yields the chart
> $$\Psi_U : U \times GL_k(\mathbb{R}) \longrightarrow \pi^{-1}(U), \qquad \Psi_U(m, h) = e(m) \circ h \qquad \text{(equation (24))},$$
> the chart from **[[Def - Frame Bundle of a Vector Bundle]]**.
> Because our frame $e_0$ is defined over $U = M$, the chart $\Psi_M$ is a map defined on all of $M \times GL_k(\mathbb{R})$. Define
> $$\Phi := \Psi_M : M \times GL_k(\mathbb{R}) \longrightarrow \operatorname{Fr}(M \times \mathbb{R}^k), \qquad \Phi(m, h) = e_0(m) \circ h = \iota_m \circ h \qquad \text{(definition of } \Phi \text{, } e_0(m) = \iota_m\text{)}.$$
> Concretely, $\Phi(m, h)$ is the frame $x \mapsto (m, h x)$ of $E_m$.

**Step 2: $\Phi$ covers the identity and is a bijection.**

The map $\Phi$ sends the fibre $\{m\} \times GL_k(\mathbb{R})$ bijectively onto the fibre $\operatorname{Fr}(E_m)$ over the same point $m$.

> [!note]- Derivation
> **Covers the identity.** For $(m, h) \in M \times GL_k(\mathbb{R})$ the point $\Phi(m, h) = \iota_m \circ h$ is a frame of $E_m$, so
> $$\pi\big(\Phi(m, h)\big) = m = \operatorname{pr}_1(m, h) \qquad \text{(} \Phi(m,h) \in \operatorname{Fr}(E_m)\text{, and } \operatorname{pr}_1 \text{ is projection to } M\text{)},$$
> i.e. $\pi \circ \Phi = \operatorname{pr}_1$, so $\Phi$ covers the identity of $M$.
>
> **Bijective.** We show $\Phi$ restricts to a bijection on each fibre; together with the previous line, that makes $\Phi$ a bijection. Fix $m$. The map $h \mapsto \iota_m \circ h$ from $GL_k(\mathbb{R})$ to $\operatorname{Fr}(E_m)$ is:
> - *injective* — if $\iota_m \circ h = \iota_m \circ h'$, precompose with $\iota_m^{-1}$ (an isomorphism, hence left-cancellable) to get $h = h'$;
> - *surjective* — given any frame $p \in \operatorname{Fr}(E_m)$, the matrix $h := \iota_m^{-1} \circ p : \mathbb{R}^k \to \mathbb{R}^k$ is a composition of isomorphisms, so $h \in GL_k(\mathbb{R})$, and $\Phi(m, h) = \iota_m \circ \iota_m^{-1} \circ p = p$.
>
> Since $\Phi$ maps $\{m\} \times GL_k(\mathbb{R})$ onto $\operatorname{Fr}(E_m)$ bijectively for each $m$, and distinct fibres map to distinct fibres (as $\Phi$ covers the identity), $\Phi$ is a bijection with inverse $\Phi^{-1}(p) = \big(\pi(p),\ \iota_{\pi(p)}^{-1} \circ p\big)$.

**Step 3: $\Phi$ is a diffeomorphism.**

The map $\Phi$ is the single global chart of $\operatorname{Fr}(E)$ determined by $e_0$, hence a diffeomorphism by the construction of the smooth structure.

> [!note]- Derivation
> The smooth structure on $\operatorname{Fr}(E)$ is *defined* by declaring each chart $\Psi_U$ (for $U$ a trivialising open with local frame) to be a diffeomorphism onto the open set $\pi^{-1}(U)$; this is the smooth structure verified in full on **[[Def - Frame Bundle of a Vector Bundle]]** (the complete verification that $\operatorname{Fr}(E)$ is a principal bundle establishes that the charts are smoothly compatible and the topology is Hausdorff and second countable). Here $E = M \times \mathbb{R}^k$ is trivial over $U = M$ with the global frame $e_0$, so $\pi^{-1}(M) = \operatorname{Fr}(E)$ and $\Psi_M$ is a global chart. Therefore
> $$\Phi = \Psi_M : M \times GL_k(\mathbb{R}) \xrightarrow{\ \cong\ } \operatorname{Fr}(M \times \mathbb{R}^k)$$
> is a diffeomorphism, being by definition one of the charts of the manifold $\operatorname{Fr}(E)$; its smooth inverse is the coordinate map $\Psi_M^{-1}$. No separate coordinate computation is needed, because the trivial bundle's frame bundle *is* covered by this one chart.

**Step 4: $\Phi$ is $GL_k(\mathbb{R})$-equivariant.**

Equivariance is associativity of composition, using that the right action on frames is precomposition.

> [!note]- Derivation
> The right action of $GL_k(\mathbb{R})$ on the trivial principal bundle $M \times GL_k(\mathbb{R})$ is right multiplication on the second factor, $(m, h) \cdot h' = (m, h h')$; the right action on the frame bundle is precomposition, $p \cdot h' = p \circ h'$. For all $m \in M$ and $h, h' \in GL_k(\mathbb{R})$,
> $$\Phi\big((m, h) \cdot h'\big) = \Phi(m, h h') = \iota_m \circ (h h') \qquad \text{(action on } M \times GL_k(\mathbb{R})\text{, then definition of } \Phi\text{)},$$
> $$\iota_m \circ (h h') = (\iota_m \circ h) \circ h' = \Phi(m, h) \circ h' = \Phi(m, h) \cdot h' \qquad \text{(associativity of composition; definition of } \Phi\text{; action on } \operatorname{Fr}(E)\text{)}.$$
> Combining the two displays, $\Phi\big((m, h) \cdot h'\big) = \Phi(m, h) \cdot h'$, which is equivariance.
>
> By Steps 2–4, $\Phi$ covers the identity of $M$, is a diffeomorphism, and is $GL_k(\mathbb{R})$-equivariant; therefore $\Phi$ is an isomorphism of principal $GL_k(\mathbb{R})$-bundles, and $\operatorname{Fr}(M \times \mathbb{R}^k) \cong M \times GL_k(\mathbb{R})$.

## Part (b)

**Step 5: A global section of $\operatorname{Fr}(E)$ is the same datum as a global frame of $E$.**

For any rank-$k$ vector bundle $E$, sections of $\operatorname{Fr}(E)$ correspond bijectively to global frames of $E$.

> [!note]- Derivation
> Let $\sigma : M \to \operatorname{Fr}(E)$ be a smooth global section, so $\pi \circ \sigma = \operatorname{id}_M$, i.e. $\sigma(m) \in \operatorname{Fr}(E_m)$ for every $m$: to each point $\sigma$ assigns a frame $\sigma(m) : \mathbb{R}^k \to E_m$. Define
> $$\sigma_j(m) := \sigma(m)(\hat{e}_j) \in E_m \qquad (j = 1, \dots, k),$$
> the image of the $j$-th standard basis vector under the frame $\sigma(m)$. Each $\sigma_j$ is a smooth section of $E$ (it is $\sigma$ followed by the smooth evaluation-at-$\hat{e}_j$ map on the frame bundle), and $(\sigma_1(m), \dots, \sigma_k(m))$ is a basis of $E_m$ at every $m$ because $\sigma(m)$ is an isomorphism. Thus $(\sigma_1, \dots, \sigma_k)$ is a smooth **global frame** of $E$.
>
> Conversely, a global frame $(s_1, \dots, s_k)$ of $E$ defines a section $\sigma$ of $\operatorname{Fr}(E)$ by letting $\sigma(m)$ be the isomorphism $\hat{e}_j \mapsto s_j(m)$; this $\sigma$ is smooth (in a local trivialisation of $E$ over $U$ the frame becomes a smooth $GL_k(\mathbb{R})$-valued function, which is exactly the coordinate expression of $\sigma$ in the chart $\Psi_U$) and satisfies $\pi \circ \sigma = \operatorname{id}_M$. The two constructions are mutually inverse, so global sections of $\operatorname{Fr}(E)$ and global frames of $E$ are the same datum.

**Step 6: $\operatorname{Fr}(E)$ is trivial if and only if $E$ is trivial.**

Feeding the section–frame dictionary into the section–triviality correspondence gives the equivalence.

> [!note]- Derivation
> We invoke the following, proved in full on **[[Thm - Sections of a Principal Bundle and Triviality]]**.
>
> > **Theorem (sections and triviality of a principal bundle), parts (ii) and (iii).** A principal $G$-bundle $P \to M$ is trivial (isomorphic as a principal $G$-bundle to $M \times G$) if and only if it admits a global section. A vector bundle $E \to M$ is trivial if and only if its frame bundle $\operatorname{Fr}(E)$ admits a global section.
>
> Applying part (ii) to $P = \operatorname{Fr}(E)$ (with $G = GL_k(\mathbb{R})$): $\operatorname{Fr}(E)$ is trivial if and only if it has a global section. By Step 5, $\operatorname{Fr}(E)$ has a global section if and only if $E$ has a global frame, and $E$ has a global frame if and only if $E$ is trivial (a global frame gives the trivialisation $\psi^{-1}(m, x) = \sum_j x_j s_j(m)$, and a trivialisation gives the global frame $s_j(m) = \psi^{-1}(m, \hat{e}_j)$). Chaining these equivalences,
> $$\operatorname{Fr}(E) \text{ trivial} \iff \operatorname{Fr}(E) \text{ has a global section} \iff E \text{ has a global frame} \iff E \text{ trivial},$$
> which is exactly part (iii) of the theorem, now seen as a consequence of part (ii) and the section–frame dictionary.

**Step 7: The tautological section of $\operatorname{Fr}(M \times \mathbb{R}^k)$ and its identity with $\Phi$.**

The constant frame is the tautological global section, and the trivialisation it induces is the isomorphism $\Phi$ of part (a).

> [!note]- Derivation
> For $E = M \times \mathbb{R}^k$, the global frame $e_0$ of Step 1 is a global section
> $$\sigma_0 : M \to \operatorname{Fr}(M \times \mathbb{R}^k), \qquad \sigma_0(m) = e_0(m) = \iota_m,$$
> so $\operatorname{Fr}(M \times \mathbb{R}^k)$ has a global section and is therefore trivial by Step 6 — a second proof of part (a), now through the section–triviality theorem rather than by exhibiting $\Phi$ directly. That the two proofs coincide is the content of the theorem's part (i): the trivialisation built from a section $s$ is $\psi^{-1}(m, g) = s(m) \cdot g$. Taking $s = \sigma_0$,
> $$\psi^{-1}(m, h) = \sigma_0(m) \cdot h = \iota_m \circ h = \Phi(m, h) \qquad \text{(} \sigma_0(m) = \iota_m\text{; right action } p \cdot h = p \circ h\text{; definition of } \Phi\text{)}.$$
> Hence the isomorphism $\Phi$ of part (a) is exactly the trivialisation induced by the tautological section $\sigma_0$, and parts (a) and (b) are the same construction: the constant global frame, read once as a chart and once as a section.

> [!note]- Complete formal solution
> **Claim.** For a smooth manifold $M$: (a) $\operatorname{Fr}(M \times \mathbb{R}^k) \cong M \times GL_k(\mathbb{R})$ as principal $GL_k(\mathbb{R})$-bundles over $M$; (b) for any rank-$k$ vector bundle $E$, global sections of $\operatorname{Fr}(E)$ are global frames of $E$, and $\operatorname{Fr}(E)$ is trivial if and only if $E$ is, with the trivial bundle witnessed by its constant frame.
>
> Write $E = M \times \mathbb{R}^k$, $E_m = \{m\} \times \mathbb{R}^k$, and $\iota_m : \mathbb{R}^k \to E_m$, $\iota_m(x) = (m, x)$, the canonical isomorphism.
>
> *(a).* The tuple $e_0(m) = \iota_m$ (that is, $e_{0,j}(m) = (m, \hat{e}_j)$) is a smooth global frame of $E$, since each $e_{0,j}$ is a smooth section and $\iota_m$ is an isomorphism for every $m$. By equation (24) of the frame-bundle construction it determines the chart $\Psi_M(m, h) = e_0(m) \circ h = \iota_m \circ h$, defined on all of $M \times GL_k(\mathbb{R})$ because $e_0$ is global; set $\Phi := \Psi_M$, so $\Phi(m, h)$ is the frame $x \mapsto (m, h x)$.
>
> $\Phi$ *covers the identity*: $\Phi(m, h) \in \operatorname{Fr}(E_m)$, so $\pi \circ \Phi = \operatorname{pr}_1$. $\Phi$ *is a bijection*: on each fibre, $h \mapsto \iota_m \circ h$ is injective (precompose with $\iota_m^{-1}$) and surjective (given $p \in \operatorname{Fr}(E_m)$, take $h = \iota_m^{-1} \circ p \in GL_k(\mathbb{R})$), with inverse $\Phi^{-1}(p) = (\pi(p), \iota_{\pi(p)}^{-1} \circ p)$. $\Phi$ *is a diffeomorphism*: it is the single global chart $\Psi_M$ of the manifold $\operatorname{Fr}(E)$, which is a diffeomorphism by the definition of the smooth structure (verified on [[Def - Frame Bundle of a Vector Bundle]]). $\Phi$ *is equivariant*: for $h, h' \in GL_k(\mathbb{R})$,
> $$\Phi((m,h)\cdot h') = \Phi(m, hh') = \iota_m \circ (hh') = (\iota_m \circ h) \circ h' = \Phi(m,h) \cdot h',$$
> using the trivial-bundle action $(m,h)\cdot h' = (m, hh')$, associativity of composition, and the frame action $p \cdot h' = p \circ h'$. Hence $\Phi$ is an isomorphism of principal $GL_k(\mathbb{R})$-bundles, proving (a).
>
> *(b).* Let $E$ be any rank-$k$ vector bundle. A global section $\sigma : M \to \operatorname{Fr}(E)$ assigns to each $m$ a frame $\sigma(m) : \mathbb{R}^k \to E_m$; setting $\sigma_j(m) := \sigma(m)(\hat{e}_j)$ gives a smooth global frame $(\sigma_1, \dots, \sigma_k)$, and conversely a global frame $(s_1, \dots, s_k)$ gives the section $m \mapsto (\hat{e}_j \mapsto s_j(m))$; the two are mutually inverse, so sections of $\operatorname{Fr}(E)$ are global frames of $E$. By [[Thm - Sections of a Principal Bundle and Triviality|the section–triviality theorem]], part (ii), $\operatorname{Fr}(E)$ is trivial if and only if it has a global section; combining with the dictionary and the equivalence "$E$ has a global frame $\iff$ $E$ is trivial" yields
> $$\operatorname{Fr}(E) \text{ trivial} \iff \operatorname{Fr}(E) \text{ has a global section} \iff E \text{ has a global frame} \iff E \text{ trivial},$$
> which is the theorem's part (iii). For $E = M \times \mathbb{R}^k$ the constant frame is the tautological global section $\sigma_0(m) = \iota_m$, so $\operatorname{Fr}(M \times \mathbb{R}^k)$ is trivial; and the trivialisation it induces via the section-to-trivialisation formula $\psi^{-1}(m, h) = \sigma_0(m) \cdot h = \iota_m \circ h$ is precisely the map $\Phi$ of part (a). $\blacksquare$

> [!warning] Illegal but tempting: "the fibre of $\operatorname{Fr}(E_m)$ is $GL_k(\mathbb{R})$, so $\operatorname{Fr}(E) = M \times GL_k(\mathbb{R})$ always"
> It is true that every fibre $\operatorname{Fr}(E_m)$ is *isomorphic* to $GL_k(\mathbb{R})$, because it is a torsor under the free transitive action. But an isomorphism of each fibre with the group is not an isomorphism of bundles: to glue the fibrewise identifications into a global $\Phi$ one needs a *smooth global choice* of reference frame, that is a global section, and that is exactly what a non-trivial bundle lacks. The frame bundle $\operatorname{Fr}(TS^2)$ has every fibre a copy of $GL_2(\mathbb{R})$ yet is not trivial, because $TS^2$ has no global frame (see [[Ex - The Frame Bundle of TS^2 Admits No Global Section]]). The step from "fibrewise isomorphic to $G$" to "isomorphic to $M \times G$" is legal *only* when a global section is produced — which for the trivial bundle is the constant frame, and in general is forbidden by the section–triviality theorem.

> [!note]- Independent sanity check: dimensions and the case $M = \{\text{pt}\}$
> The total space $\operatorname{Fr}(M \times \mathbb{R}^k)$ has dimension $\dim M + k^2$, and so does $M \times GL_k(\mathbb{R})$ (since $\dim GL_k(\mathbb{R}) = k^2$); the isomorphism $\Phi$ is consistent with the dimension count. In the extreme case $M = \{\text{pt}\}$ the bundle $M \times \mathbb{R}^k$ is just the vector space $\mathbb{R}^k$, its frame bundle is the set of bases of $\mathbb{R}^k$, and $\Phi$ specialises to the classical bijection "a basis of $\mathbb{R}^k$ is an invertible matrix, once the standard basis is fixed as reference" — the finite-dimensional linear-algebra fact of which the whole exercise is the bundle version.

---

# Key Takeaways

**A construction defined by an atlas becomes a formula on the trivial input, because the atlas collapses to one global chart.** The frame bundle is built patch by patch: over each trivialising open $U$ one chooses a local frame $e$ and declares $\Psi_U(m, h) = e(m) \circ h$ a chart, then glues. The trivial bundle $M \times \mathbb{R}^k$ has a *global* frame — the constant standard basis in every fibre — so a single chart covers everything and the gluing is vacuous; the chart itself is the sought isomorphism $\Phi$. This is the recurring diagnostic for any bundle construction: to evaluate it on a trivial bundle, produce the global frame or global trivialisation, plug it into the one-patch formula, and there is nothing left to check beyond the defining clauses of the target object. The same collapse is what makes computations on $M \times \mathbb{R}^k$, on pull-backs along constant maps, and on bundles over contractible bases tractable — the atlas has one element.

**"Fibrewise isomorphic to $G$" is strictly weaker than "isomorphic to $M \times G$"; the gap is exactly a global section.** Every fibre of a principal $G$-bundle is a torsor, hence abstractly a copy of $G$, so pointwise there is never any obstruction. The obstruction is entirely in assembling the pointwise identifications smoothly and globally, and it is measured precisely by whether a global section exists — which is the content of the section–triviality correspondence. The trivial bundle is trivial not because its fibres are copies of $GL_k(\mathbb{R})$ (all frame bundles have that) but because it has the constant global section. When one meets a bundle and wants to decide triviality, the useless question is "what is the fibre?" and the decisive question is "is there a global section?"; the frame bundle of $TS^2$ is the standard reminder, having the same fibres as a trivial bundle and no global section.

**A global frame, a global section of the frame bundle, and a trivialisation are three names for one object, and translating between them is the core dictionary of the chapter.** A trivialisation $E \cong M \times \mathbb{R}^k$ reads off the global frame $s_j(m) = \psi^{-1}(m, \hat{e}_j)$; a global frame reassembles into a section $\sigma(m) = (\hat{e}_j \mapsto s_j(m))$ of $\operatorname{Fr}(E)$; and a section of a principal bundle is equivalent to a trivialisation by $\psi^{-1}(m, g) = \sigma(m) \cdot g$. The trigger to use this dictionary is any question about the *global* structure of a vector bundle — is it trivial, does it have a nowhere-vanishing section, does it admit a metric or orientation — because each such question becomes a question about sections of $\operatorname{Fr}(E)$ or one of its reductions, where the principal-bundle machinery applies. This exercise is the dictionary in its simplest instance, where all three objects are the constant standard basis; the companion pages [[Ex - The Frame Bundle of TS^2 Admits No Global Section]] and [[Ex - The Tangent Bundle of S^2 is Nontrivial]] are the same dictionary read on a bundle where none of the three objects exists, which is what makes the non-triviality visible.
