---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Left and Right Translations and Conjugation on a Lie Group"
  - "Def - Lie Group"
  - "Def - Lie Group Homomorphism"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $G$ be a [[Def - Lie Group|Lie group]] with identity element $e$. For a fixed $g\in G$ recall the three maps
$$L_g:G\to G,\quad L_g(h)=g\cdot h;\qquad R_g:G\to G,\quad R_g(h)=h\cdot g;\qquad \alpha_g:G\to G,\quad \alpha_g(h)=g\cdot h\cdot g^{-1},$$
the left translation, right translation, and conjugation by $g$, with $\alpha_g=L_g\circ R_{g^{-1}}$. Prove the following.

1. For every $g\in G$, conjugation $\alpha_g$ is a Lie group automorphism of $G$; that is, $\alpha_g\in\operatorname{Aut}(G)$.
2. Conjugation is a group homomorphism into $\operatorname{Aut}(G)$: $\alpha_{gh}=\alpha_g\circ\alpha_h$ for all $g,h\in G$ (and $\alpha_e=\operatorname{id}_G$, $(\alpha_g)^{-1}=\alpha_{g^{-1}}$).
3. Left translation $L_g$ is a group homomorphism if and only if $g=e$. The same holds for $R_g$.

Here $\operatorname{Aut}(G)$ denotes the group, under composition, of **Lie group automorphisms** of $G$ — bijective [[Def - Lie Group Homomorphism|Lie group homomorphisms]] $\varphi:G\to G$ whose inverse $\varphi^{-1}$ is again a Lie group homomorphism.

**Recall:**

![[Def - Left and Right Translations and Conjugation on a Lie Group#The Definition]]

A [[Def - Lie Group Homomorphism|Lie group homomorphism]] is a smooth map $\varphi:G\to H$ between Lie groups that respects the group operations: $\varphi(h_1h_2)=\varphi(h_1)\varphi(h_2)$ for all $h_1,h_2$. Two consequences of this defining property are used repeatedly below and follow in one line each: a homomorphism sends the identity to the identity, $\varphi(e)=e$ — because $\varphi(e)=\varphi(e\cdot e)=\varphi(e)\varphi(e)$, and cancelling one factor $\varphi(e)$ gives $\varphi(e)=e$ — and it sends inverses to inverses, $\varphi(h^{-1})=\varphi(h)^{-1}$ — because $\varphi(h)\varphi(h^{-1})=\varphi(hh^{-1})=\varphi(e)=e$.

A [[Def - Lie Group|Lie group]] is a smooth manifold $G$ that is also a group for which multiplication $(g,h)\mapsto gh$ and inversion $g\mapsto g^{-1}$ are smooth. In particular the left and right translations $L_g$ and $R_g$ are smooth, with smooth inverses $L_{g^{-1}}$ and $R_{g^{-1}}$, hence diffeomorphisms of $G$; this smoothness is what lets us speak of $\alpha_g$ as a candidate *Lie group* automorphism rather than a bare group automorphism.

---

# Convergent Strategy

**Problem class.** This is a *structure-preservation* problem: three explicit self-maps of a group are presented, and we must decide which of them respect the group operation and in what sense. It is the archetype for the distinction, ubiquitous in gauge theory, between maps that are merely diffeomorphisms of the total space and maps that additionally intertwine the algebraic structure — the same distinction that later separates a general fibre-preserving diffeomorphism of a principal bundle from a genuine gauge transformation, which must in addition be equivariant. Getting the elementary case of translations versus conjugation exactly right fixes the habit of always asking "homomorphism, or only diffeomorphism?".

**Assumption pattern.** The only hypotheses are the group axioms and the smoothness built into the definition of a Lie group; there is no metric, no topology beyond smoothness, and no dimension assumption. Everything is proved by manipulating products and inverses. The assumption that $G$ is a Lie group (rather than an abstract group) enters only to certify smoothness of $\alpha_g$ and of its inverse, upgrading "group automorphism" to "Lie group automorphism"; the algebraic heart of every claim uses nothing but associativity, inverses, and the identity.

**Theorem routing.** For assertion 1 we verify the homomorphism identity $\alpha_g(h_1h_2)=\alpha_g(h_1)\alpha_g(h_2)$ directly, exhibit the two-sided inverse $\alpha_{g^{-1}}$ to get bijectivity, and note that $\alpha_g=L_g\circ R_{g^{-1}}$ is smooth with smooth inverse, so $\alpha_g\in\operatorname{Aut}(G)$. For assertion 2 we compute $\alpha_{gh}(k)$ and $\alpha_g(\alpha_h(k))$ and see they agree for all $k$. For assertion 3 we use the one-line fact that a homomorphism fixes the identity: $L_g$ homomorphism $\Rightarrow L_g(e)=e\Rightarrow g=e$, and conversely $L_e=\operatorname{id}_G$ is a homomorphism.

**Key decision point.** The decisive observation is that a group homomorphism *must fix the identity*, and $L_g$ moves the identity to $g$. This single fact collapses assertion 3 to a triviality: the only translation that can possibly be a homomorphism is the one that fixes $e$, namely $L_e$, and that one manifestly is. Recognising that "$\varphi(e)=e$" is a free necessary condition — costing nothing yet immediately obstructing every $L_g$ with $g\neq e$ — is what turns a potential product-by-product computation into a one-line argument. The complementary decision for assertion 2 is to check the homomorphism property of $\alpha:G\to\operatorname{Aut}(G)$ on an arbitrary test element $k$, since two maps are equal exactly when they agree at every point.

---

# Legal Operations Used

This solution deploys the following legal operations of the chapter (named descriptively; the topic-page Legal Operations list will assign them numbers).

1. **Verify the homomorphism property on a general product.** To decide whether a self-map $\varphi$ of $G$ is a homomorphism, evaluate $\varphi(h_1h_2)$ and $\varphi(h_1)\varphi(h_2)$ symbolically and compare. Applied to $\alpha_g$ (they agree) and, in contrapositive form, to $L_g$ (they disagree unless $g=e$).

2. **Certify a bijection by exhibiting a two-sided inverse.** Rather than proving injectivity and surjectivity separately, produce an explicit inverse map. Here $\alpha_g\circ\alpha_{g^{-1}}=\alpha_{g^{-1}}\circ\alpha_g=\operatorname{id}_G$ follows from the composition law of assertion 2, so $\alpha_g$ is bijective with inverse $\alpha_{g^{-1}}$.

3. **Upgrade a group automorphism to a Lie group automorphism using smoothness of translations.** Since $\alpha_g=L_g\circ R_{g^{-1}}$ is a composite of diffeomorphisms and its inverse $\alpha_{g^{-1}}$ is of the same form, both $\alpha_g$ and $\alpha_g^{-1}$ are smooth; combined with the homomorphism property this places $\alpha_g$ in $\operatorname{Aut}(G)$.

4. **Use the identity-preservation of homomorphisms as an obstruction.** A homomorphism fixes $e$. Reading this as a necessary condition immediately rules out any candidate map that moves $e$, which is the whole of the "only if" direction for translations.

---

# Hints

> [!note]- Hint 1
> For assertion 1, do not think about manifolds yet — first check the purely algebraic homomorphism identity $\alpha_g(h_1h_2)=\alpha_g(h_1)\alpha_g(h_2)$ by inserting $g^{-1}g$ in the middle. For assertion 3, remember one fact about *any* group homomorphism $\varphi$: where must it send the identity $e$? Now ask where $L_g$ sends $e$.

> [!note]- Hint 2
> To finish assertion 1, you need $\alpha_g$ bijective and smooth-with-smooth-inverse. Both come from assertion 2: compute $\alpha_{gh}=\alpha_g\circ\alpha_h$ and specialise to $h=g^{-1}$ to find the inverse of $\alpha_g$. Smoothness is free because $\alpha_g=L_g\circ R_{g^{-1}}$ is a composite of diffeomorphisms.

> [!note]- Hint 3
> For assertion 3, prove both directions. If $g=e$ then $L_e(h)=h$, the identity map — certainly a homomorphism. Conversely, if $L_g$ is a homomorphism then $L_g(e)=e$; but $L_g(e)=g$, so $g=e$. If you prefer an argument that never quotes "homomorphisms fix the identity", expand $L_g(h_1h_2)=L_g(h_1)L_g(h_2)$ and cancel to isolate a condition on $g$.

---

# Solution

The plan is to treat the three assertions in order, each by a short manipulation of products and inverses. Assertion 1 verifies the homomorphism identity for $\alpha_g$, produces the explicit inverse $\alpha_{g^{-1}}$, and records smoothness; assertion 2 is a two-line associativity computation; assertion 3 uses that a homomorphism must fix the identity while $L_g$ moves it to $g$. We prove assertion 2 before completing assertion 1, since the inverse of $\alpha_g$ is read off from the composition law.

**Step 1: $\alpha_g$ is a group homomorphism.**

For every $g$, conjugation $\alpha_g$ respects products: inserting $g^{-1}g=e$ between the two factors shows $\alpha_g(h_1h_2)=\alpha_g(h_1)\alpha_g(h_2)$.

> [!note]- Derivation
> Fix $g\in G$ and let $h_1,h_2\in G$ be arbitrary. Then
> $$\alpha_g(h_1h_2)=g(h_1h_2)g^{-1}=gh_1\,(g^{-1}g)\,h_2g^{-1}\qquad\text{(definition of }\alpha_g\text{; insert }e=g^{-1}g\text{ between }h_1\text{ and }h_2\text{)}$$
> $$=(gh_1g^{-1})(gh_2g^{-1})=\alpha_g(h_1)\,\alpha_g(h_2)\qquad\text{(regroup by associativity; definition of }\alpha_g\text{).}$$
> Since $h_1,h_2$ were arbitrary, $\alpha_g$ is a group homomorphism.

**Step 2: The composition law $\alpha_{gh}=\alpha_g\circ\alpha_h$, with $\alpha_e=\operatorname{id}_G$ and $(\alpha_g)^{-1}=\alpha_{g^{-1}}$.**

Conjugation by a product is the composite of the conjugations, so $\alpha:G\to\operatorname{Aut}(G)$ is itself a homomorphism; specialising gives the identity and inverse formulas.

> [!note]- Derivation
> Fix $g,h\in G$ and let $k\in G$ be arbitrary. Using $(gh)^{-1}=h^{-1}g^{-1}$,
> $$\alpha_{gh}(k)=(gh)\,k\,(gh)^{-1}=ghk\,h^{-1}g^{-1}=g\,(hkh^{-1})\,g^{-1}\qquad\text{(definition of }\alpha_{gh}\text{; }(gh)^{-1}=h^{-1}g^{-1}\text{; associativity)}$$
> $$=g\,\alpha_h(k)\,g^{-1}=\alpha_g(\alpha_h(k))=(\alpha_g\circ\alpha_h)(k)\qquad\text{(definition of }\alpha_h\text{, then of }\alpha_g\text{).}$$
> As $k$ was arbitrary, $\alpha_{gh}=\alpha_g\circ\alpha_h$. Taking $g=h=e$, or directly, $\alpha_e(k)=eke^{-1}=k$, so $\alpha_e=\operatorname{id}_G$. Taking $h=g^{-1}$ in the composition law,
> $$\alpha_g\circ\alpha_{g^{-1}}=\alpha_{gg^{-1}}=\alpha_e=\operatorname{id}_G,\qquad \alpha_{g^{-1}}\circ\alpha_g=\alpha_{g^{-1}g}=\alpha_e=\operatorname{id}_G,$$
> so $\alpha_g$ is invertible with $(\alpha_g)^{-1}=\alpha_{g^{-1}}$.

**Step 3: $\alpha_g$ is a Lie group automorphism, $\alpha_g\in\operatorname{Aut}(G)$.**

Combining Steps 1 and 2 with the smoothness of translations shows $\alpha_g$ is a bijective Lie group homomorphism with smooth inverse.

> [!note]- Derivation
> By Step 1, $\alpha_g$ is a group homomorphism. By Step 2 it is bijective, with inverse $\alpha_{g^{-1}}$. It remains to check the smoothness demanded by the word *Lie* in "Lie group automorphism". By its definition $\alpha_g=L_g\circ R_{g^{-1}}$, and on a [[Def - Lie Group|Lie group]] each translation is smooth with smooth inverse (multiplication and inversion are smooth), so $L_g$ and $R_{g^{-1}}$ are diffeomorphisms and their composite $\alpha_g$ is smooth. Its inverse $\alpha_{g^{-1}}=L_{g^{-1}}\circ R_{g}$ is smooth for the same reason. Therefore $\alpha_g$ is a smooth bijective group homomorphism with smooth inverse — a [[Def - Lie Group Homomorphism|Lie group homomorphism]] that is a Lie group isomorphism from $G$ to itself — that is, $\alpha_g\in\operatorname{Aut}(G)$.

**Step 4: $L_g$ is a homomorphism if and only if $g=e$ (and likewise $R_g$).**

A group homomorphism must fix the identity, and $L_g$ sends $e$ to $g$; so $L_g$ can be a homomorphism only when $g=e$, and $L_e=\operatorname{id}_G$ indeed is one.

> [!note]- Derivation
> We prove both directions.
>
> *($\Leftarrow$) If $g=e$, then $L_g$ is a homomorphism.* Here $L_e(h)=e\cdot h=h$ for all $h$, so $L_e=\operatorname{id}_G$, the identity map of $G$, which satisfies $\operatorname{id}_G(h_1h_2)=h_1h_2=\operatorname{id}_G(h_1)\operatorname{id}_G(h_2)$ and is therefore a group homomorphism.
>
> *($\Rightarrow$) If $L_g$ is a homomorphism, then $g=e$.* Every group homomorphism $\varphi$ fixes the identity: $\varphi(e)=\varphi(ee)=\varphi(e)\varphi(e)$, and multiplying by $\varphi(e)^{-1}$ gives $\varphi(e)=e$. Applying this to $\varphi=L_g$ yields $L_g(e)=e$. But by definition $L_g(e)=g\cdot e=g$. Comparing, $g=e$.
>
> For completeness, here is the same conclusion drawn without quoting the identity-preservation lemma. If $L_g$ were a homomorphism, then for all $h_1,h_2\in G$,
> $$g\,h_1h_2=L_g(h_1h_2)=L_g(h_1)L_g(h_2)=(gh_1)(gh_2)=gh_1gh_2.$$
> Cancelling $gh_1$ on the left (valid since $G$ is a group, so $gh_1$ is invertible) gives $h_2=gh_2$ for all $h_2$; taking $h_2=e$ gives $e=g$. Either argument shows $g=e$.
>
> The identical reasoning applies to right translation: $R_g$ is a group homomorphism if and only if $g=e$, because a homomorphism fixes $e$ while $R_g(e)=e\cdot g=g$, and $R_e=\operatorname{id}_G$. In particular, for $g\neq e$ neither $L_g$ nor $R_g$ is a homomorphism, although both remain diffeomorphisms of $G$ (with smooth inverses $L_{g^{-1}}$, $R_{g^{-1}}$).

> [!note]- Complete formal solution
> Fix a [[Def - Lie Group|Lie group]] $G$ with identity $e$ and an element $g\in G$.
>
> *Conjugation is a homomorphism.* For $h_1,h_2\in G$, inserting $e=g^{-1}g$ gives $\alpha_g(h_1h_2)=gh_1h_2g^{-1}=(gh_1g^{-1})(gh_2g^{-1})=\alpha_g(h_1)\alpha_g(h_2)$, so $\alpha_g$ respects products.
>
> *Composition law.* For $k\in G$, using $(gh)^{-1}=h^{-1}g^{-1}$, $\alpha_{gh}(k)=ghk h^{-1}g^{-1}=g(hkh^{-1})g^{-1}=\alpha_g(\alpha_h(k))$; hence $\alpha_{gh}=\alpha_g\circ\alpha_h$. In particular $\alpha_e=\operatorname{id}_G$ (since $\alpha_e(k)=k$) and $\alpha_g\circ\alpha_{g^{-1}}=\alpha_{g^{-1}}\circ\alpha_g=\alpha_e=\operatorname{id}_G$, so $\alpha_g$ is bijective with inverse $\alpha_{g^{-1}}$.
>
> *Conjugation is a Lie group automorphism.* Because $\alpha_g=L_g\circ R_{g^{-1}}$ is a composite of translations, which are diffeomorphisms of the Lie group $G$, $\alpha_g$ is smooth; its inverse $\alpha_{g^{-1}}=L_{g^{-1}}\circ R_g$ is smooth likewise. A smooth bijective group homomorphism with smooth inverse is a [[Def - Lie Group Homomorphism|Lie group]] automorphism, so $\alpha_g\in\operatorname{Aut}(G)$.
>
> *Translations are homomorphisms only trivially.* If $g=e$, then $L_e=\operatorname{id}_G$ is a homomorphism. Conversely, any homomorphism $\varphi$ satisfies $\varphi(e)=e$ (from $\varphi(e)=\varphi(e)\varphi(e)$ after cancellation); applied to $L_g$, this gives $g=L_g(e)=e$. Hence $L_g$ is a homomorphism if and only if $g=e$. The same argument with $R_g(e)=g$ shows $R_g$ is a homomorphism if and only if $g=e$. For $g\neq e$ the maps $L_g,R_g$ are diffeomorphisms of $G$ but not group homomorphisms. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> One might try to argue that $L_g$ fails to be a homomorphism "because $L_g(h_1)L_g(h_2)=gh_1gh_2$ has two factors of $g$ while $L_g(h_1h_2)=gh_1h_2$ has one", and stop there. This is the right idea but not yet a proof, because in a non-abelian group with special elements the two expressions could in principle coincide for a particular $g$ without $g=e$ — the count of symbols is not an argument. The honest step is to *equate* the two expressions and *cancel*: $gh_1h_2=gh_1gh_2$ forces $h_2=gh_2$ for all $h_2$, hence $g=e$. Only after the cancellation, valid because every element of a group is invertible, is the conclusion secured for every group at once.

---

# Key Takeaways

**"Homomorphism" and "diffeomorphism" are independent conditions, and translations show they can come apart completely.** The reusable principle is that a self-map of a group can preserve all of the smooth structure while destroying all of the algebraic structure, or vice versa. Left translation $L_g$ is a perfect diffeomorphism — smooth, invertible, smooth inverse — yet for $g\neq e$ it is not a homomorphism at all, because it does not even fix the identity. Conjugation, by contrast, preserves both. The trigger for invoking this distinction is any problem that asks whether a natural map "respects the structure": one must specify *which* structure, and check each separately. The transferable diagnostic is the identity test — a homomorphism sends $e$ to $e$, so any structure-preserving-map candidate that moves the identity is disqualified before any product is computed. This exact distinction reappears when a principal bundle's automorphisms are sorted into gauge transformations (which cover the identity and are equivariant) versus arbitrary fibre-preserving diffeomorphisms, so the reflex trained here is the one used there.

**Conjugation packages the group's self-symmetries: $g\mapsto\alpha_g$ is a homomorphism into $\operatorname{Aut}(G)$, and this is the seed of the adjoint representation.** The identity $\alpha_{gh}=\alpha_g\circ\alpha_h$ says exactly that conjugation is a group homomorphism $\alpha:G\to\operatorname{Aut}(G)$, whose image consists of the *inner* automorphisms. The trigger to recognise this pattern is any family of maps indexed by group elements that composes according to the group law; whenever $T_gT_h=T_{gh}$, one is looking at a representation of $G$ on whatever the $T_g$ act. Here the payoff is immediate and structural: differentiating $\alpha_g$ at the identity produces $\operatorname{Ad}_g=d_e\alpha_g$, the adjoint representation on the Lie algebra $\mathfrak g=T_eG$, and the composition law $\alpha_{gh}=\alpha_g\circ\alpha_h$ differentiates to $\operatorname{Ad}_{gh}=\operatorname{Ad}_g\operatorname{Ad}_h$. The whole edifice of $\operatorname{Ad}$ and $\operatorname{ad}$, and thence the curvature and Bianchi identities of gauge theory, rests on the elementary composition law verified in Step 2.

**A necessary condition that is free to check is often the whole obstruction; deploy it before computing.** The engine of the translation half of this exercise is that "homomorphisms fix the identity" costs one line to prove and instantly settles an "if and only if". The transferable lesson is to front-load cheap necessary conditions: before grinding through a general verification, ask what a candidate map is *forced* to do at distinguished points — the identity, idempotents, fixed points — and test those first. If the candidate fails a free necessary condition it is dead, with no computation; if it passes, the necessary condition has usually pinned down enough structure to make the remaining verification short. Here the condition $\varphi(e)=e$ both kills every $L_g$ with $g\neq e$ and, in the surviving case $g=e$, hands over the identity map, which is trivially a homomorphism. The same instinct — check what the identity forces first — recurs whenever one must decide membership in a group of structure-preserving maps.
