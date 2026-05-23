---
type: definition
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
tags: [algebra, group-theory]
---

# Notation

$(G, \cdot, e_G)$ and $(H, *, e_H)$ are groups, with their own operations and identities; we usually drop the operation symbols and write both as juxtaposition. A homomorphism is written $\varphi : G \to H$ (also $f, \rho, \pi$). Its [[Def - Kernel and Image|kernel]] is $\ker\varphi$ and its [[Def - Kernel and Image|image]] is $\operatorname{im}\varphi$. A bijective homomorphism is an [[Def - Isomorphism|isomorphism]], written $G \cong H$. The full symbol registry is on [[Group Theory I — §1.1–1.2]].

---

# Axiom Motivation

We have spent §1.1 studying [[Def - Group|groups]] one at a time. But a single group in isolation reveals little; mathematics gets its power from *comparing* objects, and to compare two [[Def - Group|groups]] we need maps between them. The motivating desideratum is therefore: *single out the functions $G \to H$ that are worth studying — the ones that see $G$ and $H$ as groups, not merely as sets.*

An arbitrary function $f : G \to H$ is useless for group theory. It can shuffle elements with no regard for multiplication: it might send a product $g_1 g_2$ anywhere at all, unrelated to where it sends $g_1$ and $g_2$. Such a function carries no group-theoretic information; it cannot transport a single theorem from $G$ to $H$. We want instead the functions that *respect the structure*. A group's structure is entirely contained in its multiplication — the identity and inverses are forced by it — so "respecting the structure" can only mean one thing: the function must commute with multiplication. The product of the images should be the image of the product. That is the desideratum, and it admits exactly one formalisation:
$$\varphi(g_1 g_2) = \varphi(g_1)\,\varphi(g_2),$$
where the left product is computed in $G$ and the right product in $H$.

What is striking — and a sign the definition is right — is how much this *single* condition forces. We do not need to separately demand that $\varphi$ preserve the identity or inverses; both follow. For the identity: $\varphi(e_G) = \varphi(e_G \cdot e_G) = \varphi(e_G)\varphi(e_G)$, and cancelling $\varphi(e_G)$ (legal, in the group $H$) gives $\varphi(e_G) = e_H$. For inverses: see the derivation in *The Definition* below. So the structure-preservation condition, stated for the operation alone, automatically drags the identity and the inverses along — exactly because in a group the operation determines everything. This is the test of a good definition: it captures what we wanted (compatibility with all the group structure) by demanding the least (compatibility with one operation).

What breaks if we *weaken* the condition? Drop it entirely and "homomorphism" means "arbitrary function", and the [[Def - Kernel and Image|kernel]], the [[Thm - First Isomorphism Theorem|first isomorphism theorem]], the very notion of two groups being "the same" — all collapse, because none of them survives without $\varphi(g_1 g_2) = \varphi(g_1)\varphi(g_2)$. A near-miss weakening: require the condition only for $g_1 = g_2$, i.e. only $\varphi(g^2) = \varphi(g)^2$. This is genuinely weaker and lets through pathological maps that are not homomorphisms; it fails to give $\varphi(e) = e$ or kernel normality. What breaks if we *strengthen*? If we additionally demand $\varphi$ be injective we have an *embedding* — useful, but it excludes the most important homomorphism of all, the [[Def - Quotient Group|quotient map]] $G \to G/N$, which is deliberately non-injective. If we demand bijectivity we get an [[Def - Isomorphism|isomorphism]] — again useful, again too narrow, because we constantly want to compare groups of *different sizes*. The plain homomorphism, with no injectivity or surjectivity attached, is the right level of generality: it is exactly "structure-preserving map", and the isomorphism theorems are built to extract every drop of information from one.

---

# The Definition

Let $(G, \cdot, e_G)$ and $(H, *, e_H)$ be groups. A function $\varphi : G \to H$ is a **(group) homomorphism** if it preserves the operation:
$$\varphi(g_1 \cdot g_2) = \varphi(g_1) * \varphi(g_2) \qquad \text{for all } g_1, g_2 \in G.$$

From this single axiom, two facts follow automatically (so they need not be assumed, though it does no harm to list them):

**It preserves the identity:** $\varphi(e_G) = e_H$. Proof: $\varphi(e_G) = \varphi(e_G \cdot e_G) = \varphi(e_G) * \varphi(e_G)$; multiplying both sides by $\varphi(e_G)^{-1}$ in $H$ gives $e_H = \varphi(e_G)$.

**It preserves inverses:** $\varphi(g^{-1}) = \varphi(g)^{-1}$. Proof: compute $\varphi(g \cdot g^{-1})$ two ways. On one hand $\varphi(g \cdot g^{-1}) = \varphi(e_G) = e_H$, using identity-preservation. On the other hand $\varphi(g \cdot g^{-1}) = \varphi(g) * \varphi(g^{-1})$. So $\varphi(g) * \varphi(g^{-1}) = e_H$, and by uniqueness of inverses in the group $H$, the element $\varphi(g^{-1})$ must be $\varphi(g)^{-1}$.

By induction the operation-preservation extends to all finite products and to all integer powers: $\varphi(g_1 \cdots g_n) = \varphi(g_1) \cdots \varphi(g_n)$ and $\varphi(g^k) = \varphi(g)^k$ for every $k \in \mathbb{Z}$.

A homomorphism that is also a bijection is an [[Def - Isomorphism|isomorphism]]. A homomorphism from a group to itself, $\varphi : G \to G$, is an **endomorphism**; a bijective one is an **automorphism**.

---

# Categorical Definition

Homomorphisms are not an instance of a universal property — rather, they *are* the raw material out of which category theory is built. A **category** consists of objects together with *morphisms* (arrows) between them, equipped with an associative composition and an identity morphism on each object. The category $\mathbf{Grp}$ has groups as its objects and group homomorphisms as its morphisms: the composite $\psi \circ \varphi$ of two homomorphisms $G \xrightarrow{\varphi} H \xrightarrow{\psi} K$ is again a homomorphism (one checks $(\psi\varphi)(g_1 g_2) = \psi(\varphi(g_1)\varphi(g_2)) = (\psi\varphi)(g_1)(\psi\varphi)(g_2)$ directly), composition is associative because function composition is, and the identity function $\mathrm{id}_G$ on any group is a homomorphism serving as the identity morphism. So "homomorphism" is the answer to the question *what are the morphisms in the category of groups* — and every universal property in this topic (the [[Def - Quotient Group|quotient]], the [[Def - Kernel and Image|kernel]]) is phrased in terms of homomorphisms. They are the arrows; the constructions are the universal objects those arrows pick out. An [[Def - Isomorphism|isomorphism]] is, in this language, exactly an *invertible* morphism in $\mathbf{Grp}$.

---

# Relate to Other Fields / Compression

A homomorphism is the group instance of *structure-preserving map*, the notion every algebraic theory possesses. A ring homomorphism preserves both ring operations; a linear map preserves vector-space structure; a module homomorphism preserves the module operations; a continuous map preserves topological structure. Each is the morphism of its category, and each is defined by the same template: a function that commutes with the structure. The group case is the cleanest illustration because a group has *one* operation, so "preserve the structure" reduces to a single equation.

The most consequential compression: a **linear representation** of $G$ is *literally* a homomorphism $\rho : G \to \mathrm{GL}(V)$ into the invertible linear maps of a vector space $V$. Representation theory — an entire subject — is the systematic study of all homomorphisms out of $G$ into matrix groups at once. There is nothing extra in the definition of a representation; it is a homomorphism whose target happens to be a group of matrices. Likewise a **group action** of $G$ on a set $X$ is a homomorphism $G \to \mathrm{Sym}(X)$ into the symmetric group on $X$. Three apparently different ideas — homomorphism, representation, action — are one idea, distinguished only by the target. This is why §1.2 insists that a group is understood through its homomorphisms: the maps *are* the structure.

---

# Examples / Corollaries

**Is an instance — the determinant $\det : \mathrm{GL}_n(\mathbb{R}) \to \mathbb{R}^\times$.** The determinant is a homomorphism from invertible matrices (under multiplication) to nonzero reals (under multiplication), because $\det(AB) = \det(A)\det(B)$ — the multiplicativity of the determinant is *exactly* the homomorphism condition. Its [[Def - Kernel and Image|kernel]] is $\mathrm{SL}_n(\mathbb{R})$, the determinant-$1$ matrices; its image is all of $\mathbb{R}^\times$.

**Is an instance — the sign $\operatorname{sgn} : S_n \to \{\pm 1\}$.** Every permutation is even or odd, and the sign of a composite is the product of signs, $\operatorname{sgn}(\sigma\tau) = \operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)$ — the homomorphism condition. Its kernel is the alternating group $A_n$; its image is the order-$2$ group $\{\pm 1\}$.

**Is an instance — reduction mod $n$, $\ \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$.** The map $k \mapsto k + n\mathbb{Z}$ sending an integer to its [[Def - Residue|residue]] class is a homomorphism of additive groups: the residue of a sum is the sum of [[Def - Residue|residues]]. This is a special case of the next example.

**Is an instance — the quotient map $\pi : G \to G/N$.** For any [[Def - Normal Subgroup|normal subgroup]] $N$, the map $g \mapsto gN$ is a homomorphism, since $\pi(g_1 g_2) = g_1 g_2 N = (g_1 N)(g_2 N) = \pi(g_1)\pi(g_2)$ — this is essentially the definition of the [[Def - Quotient Group|quotient group]] operation. It is the most important homomorphism in the subject, deliberately non-injective: it forgets exactly $N$.

**Is NOT an instance — $f(g) = g^2$ on a non-abelian group.** On $S_3$ the squaring map $f(g) = g^2$ is not a homomorphism: $f(g_1 g_2) = (g_1 g_2)^2 = g_1 g_2 g_1 g_2$, whereas $f(g_1)f(g_2) = g_1^2 g_2^2 = g_1 g_1 g_2 g_2$, and these differ unless $g_1, g_2$ commute. Squaring *is* a homomorphism on every [[Def - Abelian Group|abelian]] group and *only* on those — a clean illustration that the homomorphism condition is genuine content, not automatic.

**Is NOT an instance — $f : \mathbb{Z} \to \mathbb{Z}$, $f(n) = n + 1$.** This bijection of the underlying set is not a homomorphism of $(\mathbb{Z}, +)$: it fails $f(0) = 0$ (it gives $f(0) = 1 \neq 0$), and indeed $f(m + n) = m + n + 1 \neq (m+1) + (n+1) = f(m) + f(n)$. A function can be a perfectly good map of sets and still destroy all group structure — which is precisely why the homomorphism condition has to be imposed.

**Corollary — homomorphisms preserve element order.** If $\varphi$ is a homomorphism and $g^m = e$, then $\varphi(g)^m = \varphi(g^m) = \varphi(e) = e$, so $\operatorname{ord}(\varphi(g))$ divides $\operatorname{ord}(g)$. Consequently no homomorphism can send an element of order $2$ to an element of order $3$, which is the basis of many non-existence arguments.

**Corollary — a composite of homomorphisms is a homomorphism.** If $\varphi : G \to H$ and $\psi : H \to K$ are homomorphisms, so is $\psi \circ \varphi$. This is what makes $\mathbf{Grp}$ a category and licenses the one-line proofs of the second and third isomorphism theorems, which factor a homomorphism through an inclusion.

**Calibration check.** Verify directly from the single axiom that $\varphi(e_G) = e_H$ and $\varphi(g^{-1}) = \varphi(g)^{-1}$ — if you can reproduce both derivations, you have understood the definition. Check that the constant map $g \mapsto e_H$ is always a homomorphism (the *trivial* homomorphism) and that $\mathrm{id}_G$ is one.

---

# Unlocked by This

> [!tip] Kernel and Image, and the Isomorphism Theorems *(from this topic)*
> Every homomorphism comes bundled with two subgroups, its [[Def - Kernel and Image|kernel and image]], and the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] ties them together. The homomorphism is the input from which the entire machinery of §1.2 runs.

> [!tip] Group Representations *(from Representation Theory)*
> A representation of $G$ on a vector space $V$ is exactly a homomorphism $\rho : G \to \mathrm{GL}(V)$. With homomorphisms and the matrix groups in hand, all of representation theory is available — it is the study of homomorphisms from $G$ into matrix groups.

> [!tip] Group Actions *(from Group Theory II)*
> An action of $G$ on a set $X$ is a homomorphism $G \to \mathrm{Sym}(X)$ into the symmetric group on $X$. The orbit–stabiliser theorem and the class equation all rest on viewing actions as homomorphisms.
