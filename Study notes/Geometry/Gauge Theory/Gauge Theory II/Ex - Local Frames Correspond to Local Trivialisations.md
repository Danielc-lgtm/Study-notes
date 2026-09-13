---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Local Frame"
  - "Def - Local Trivialization"
  - "Def - Vector Bundle"
  - "Thm - Local Frames Span Sections"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi : E \to M$ is a smooth real vector bundle of rank $k$ over a smooth manifold $M$, and $U \subseteq M$ is an open subset. We write $E|_U := \pi^{-1}(U)$ for the restricted total space, $E_m := \pi^{-1}(m)$ for the fibre over $m$, and $\Gamma(U; E)$ for the smooth local sections of $E$ over $U$. A **local frame** over $U$ is an ordered $k$-tuple $e = (e_1, \dots, e_k)$ with $e_j \in \Gamma(U; E)$ such that $e(m) := (e_1(m), \dots, e_k(m))$ is a basis of $E_m$ for every $m \in U$. We use the row-of-sections convention of the series: $e$ is a row and, for a column $x = (x^1, \dots, x^k)^t \in \mathbb{R}^k$, we write $e(m) \cdot x := \sum_{j=1}^{k} x^j e_j(m) \in E_m$. The standard basis of $\mathbb{R}^k$ is $(\epsilon_1, \dots, \epsilon_k)$, so $\epsilon_j$ has a $1$ in slot $j$ and zeros elsewhere. A **local trivialisation** over $U$ is a diffeomorphism $\psi_U : E|_U \to U \times \mathbb{R}^k$ that commutes with the projections and is linear on each fibre; the bundle $E$ is **trivial over $U$** when such a $\psi_U$ exists on all of $U$ (equivalently, $E|_U$ is isomorphic to the product bundle $U \times \mathbb{R}^k$).

> [!warning] Convention: frame-change labelling in R2.1.3
> The standing series convention writes a change of frame as $e' = e g$ with $g \in \Gamma(U \cap U'; \mathrm{GL}_k)$ (Haydys equation (14)). The source's Remark A-R2.1.3 states the frame-change law for components with the primed and unprimed roles reversed, $e = e' g$, and derives $\sigma' = g\sigma$. We follow the source's labelling in the final part of this exercise, because that is the exact statement item A-R2.1.3 records. To pass between the two conventions, swap the primed and unprimed frames and replace $g$ by $g^{-1}$: under $e' = e g$ the same computation gives $\sigma = g \sigma'$, i.e. $\sigma' = g^{-1}\sigma$.

---

# Problem Statement

Let $\pi : E \to M$ be a smooth vector bundle of rank $k$ and let $U \subseteq M$ be open. **Prove that $E$ is trivial over $U$ if and only if there exist $k$ sections $e = (e_1, \dots, e_k)$, $e_j \in \Gamma(U; E)$, such that $e(m)$ is a basis of $E_m$ for each $m \in U$** — that is, if and only if $E$ admits a local frame over $U$ (Haydys, Exercise 5, p. 6, item A-X2.1.3).

More precisely, establish the explicit correspondence:

- **From a frame to a trivialisation.** Given a local frame $e$ over $U$, the map
$$\psi_U^{-1} : U \times \mathbb{R}^k \longrightarrow E|_U, \qquad (m, x) \longmapsto e(m) \cdot x = \sum_{j=1}^{k} x^j e_j(m)$$
is a diffeomorphism that is linear on each fibre, so its inverse $\psi_U$ is a local trivialisation.
- **From a trivialisation to a frame.** Given a local trivialisation $\psi_U$ over $U$, the sections $e_j := \psi_U^{-1}(\,\cdot\,, \epsilon_j)$ form a local frame over $U$.
- **The two constructions are mutually inverse**, so they set up a one-to-one correspondence between $k$-tuples of pointwise linearly independent sections over $U$ and local trivialisations of $E$ over $U$.

Finally, derive the transformation law of the local representation of a section under a change of frame (Haydys, Remark A-R2.1.3): if $e$ and $e'$ are local frames over $U$ and $U'$ related on the overlap by $e = e' g$ with $g : U \cap U' \to \mathrm{GL}(k, \mathbb{R})$, and a section $s$ has component columns $\sigma$ in $e$ and $\sigma'$ in $e'$ (so $s = e\sigma = e'\sigma'$), then
$$\sigma' = g \sigma \qquad \text{on } U \cap U'.$$

**Recall:**

The objects in play are the vector bundle and its fibres, the two equivalent packagings of local data — the local trivialisation and the local frame — and the uniqueness of components in a frame.

![[Def - Vector Bundle#The Definition]]

![[Def - Local Trivialization#The Definition]]

![[Def - Local Frame#The Definition]]

The bridge between the two packagings is the theorem that a local frame turns sections into tuples of smooth functions, with uniquely determined components — this is exactly what makes the correspondence a bijection and what powers the frame-change law:

![[Thm - Local Frames Span Sections#Statement]]

A single standing fact about the general linear group is used for smoothness of inverses: matrix inversion $\mathrm{GL}(k, \mathbb{R}) \to \mathrm{GL}(k, \mathbb{R})$, $A \mapsto A^{-1}$, is smooth, because by Cramer's rule the entries of $A^{-1}$ are polynomials in the entries of $A$ divided by $\det A \neq 0$.

---

# Convergent Strategy

**Problem class.** This is a *dictionary* problem: two definitions — "trivial over $U$" (a diffeomorphism $E|_U \cong U \times \mathbb{R}^k$) and "admits a frame over $U$" (a smooth field of bases) — are two encodings of the same local structure, and the task is to translate each into the other explicitly and check the translations are inverse. Such problems are proved by *constructing both directions of the correspondence by hand* and then composing them to see the identity, rather than by an abstract existence argument.

**Assumption pattern.** The only structural hypothesis is that $E$ is a vector bundle, so it is *locally* trivial: every point has a neighbourhood over which a trivialisation exists. This local triviality is used in exactly one place — to prove that the frame-built map $\psi_U^{-1}$ is a diffeomorphism, its smoothness being checked in an auxiliary pre-existing trivialisation where the map becomes multiplication by a smooth $\mathrm{GL}_k$-valued matrix. The recognisable trigger is the pairing "a basis at each point (frame) $\leftrightarrow$ a linear coordinate identification of the fibre ($\mathbb{R}^k$)": a basis *is* a linear isomorphism $\mathbb{R}^k \to E_m$ (send $\epsilon_j$ to the $j$-th basis vector), and doing this smoothly in $m$ is precisely a trivialisation.

**Theorem routing.** The route is: (⇐) given a frame $e$, define $\psi_U^{-1}(m, x) = \sum x^j e_j(m)$; prove it is a fibrewise-linear bijection (basis $\Rightarrow$ isomorphism on each fibre) and a diffeomorphism (smooth, with smooth inverse, checked in an auxiliary trivialisation using [[#Notation|smoothness of matrix inversion]]); conclude $E$ is trivial over $U$. (⇒) given a trivialisation $\psi_U$, set $e_j = \psi_U^{-1}(\cdot, \epsilon_j)$; prove each $e_j$ is a smooth section (projection compatibility) and that $(e_j(m))$ is a basis (linearity on fibres sends the basis $(\epsilon_j)$ to a basis). Then compose the two constructions and use [[Thm - Local Frames Span Sections|uniqueness of components]] to see they are mutually inverse. The frame-change law is a one-line consequence of substituting $e = e'g$ into $s = e\sigma$ and invoking uniqueness of components in $e'$.

**Key decision point.** The single non-routine step is the *smoothness of the inverse* of $\psi_U^{-1}$ in the (⇐) direction. One cannot differentiate "solve $\sum x^j e_j(m) = \xi$ for $x$" directly; the decision is to import a pre-existing local trivialisation $\Phi$ from the bundle's own local triviality, express the frame in it as a smooth matrix $A(m) = [\Phi(e_1(m)) \mid \dots \mid \Phi(e_k(m))]$, observe $A(m) \in \mathrm{GL}_k$ because the frame is a basis, and then read the inverse map as multiplication by the smooth matrix $A(m)^{-1}$. Everything else is bookkeeping; this is where the vector-bundle hypothesis genuinely enters.

---

# Legal Operations Used

This solution deploys the following operations, each named descriptively (the topic page's Legal Operations for chapter II will be numbered when it is assembled; the orchestrator reconciles the numbering):

1. **Turn a frame into a fibrewise coordinate map.** Given a frame $e$, form $\psi_U^{-1}(m, x) = \sum_j x^j e_j(m)$; a basis at each point yields a linear isomorphism $\mathbb{R}^k \to E_m$, so this map is a fibrewise-linear bijection covering the identity.

2. **Check smoothness in an auxiliary trivialisation.** Import a pre-existing local trivialisation $\Phi$ (local triviality of $E$) and express the frame-built map as $(m, x) \mapsto (m, A(m) x)$ with $A$ smooth into $\mathrm{GL}_k$; smoothness of the map and of its inverse then follow from smoothness of $A$ and of matrix inversion.

3. **Extract a frame from a trivialisation by feeding in the standard basis.** Given $\psi_U$, define $e_j = \psi_U^{-1}(\cdot, \epsilon_j)$; projection compatibility makes each $e_j$ a smooth section, and linearity on fibres makes $(e_j(m))$ a basis.

4. **Compose the two constructions and invoke uniqueness of components.** Feed a frame's trivialisation back through operation 3 (and vice versa) and use [[Thm - Local Frames Span Sections|uniqueness of the component expansion]] to conclude the two constructions are inverse.

5. **Read off a transformation law by substituting one frame into another and matching components.** Substitute $e = e'g$ into $s = e\sigma$ to get $s = e'(g\sigma)$, then match against $s = e'\sigma'$ using uniqueness of components in $e'$ to obtain $\sigma' = g\sigma$.

---

# Hints

> [!note]- Hint 1
> A basis of a $k$-dimensional space $V$ is the same thing as a linear isomorphism $\mathbb{R}^k \to V$ (send the standard basis vector $\epsilon_j$ to the $j$-th basis element). A frame gives such an isomorphism $E_m$ at every $m$. What map $U \times \mathbb{R}^k \to E|_U$ does this suggest, and why is it a bijection on each fibre?

> [!note]- Hint 2
> For the harder direction (frame $\Rightarrow$ trivialisation), the only real work is smoothness of the inverse of $(m, x) \mapsto \sum_j x^j e_j(m)$. You cannot invert "$\sum x^j e_j(m) = \xi$" by hand, so borrow structure: the bundle is locally trivial, so near any point there is *some* trivialisation $\Phi$. Write each $e_j(m)$ in $\Phi$ as a smooth column $a_j(m) \in \mathbb{R}^k$. What matrix appears, and why is it invertible?

> [!note]- Hint 3
> With $A(m) = [a_1(m) \mid \dots \mid a_k(m)]$, the map becomes $\Phi \circ \psi_U^{-1} : (m, x) \mapsto (m, A(m) x)$. Because $e(m)$ is a basis and $\Phi_m$ is an isomorphism, the columns $a_j(m)$ are a basis of $\mathbb{R}^k$, so $A(m) \in \mathrm{GL}_k$. Now $A^{-1}$ is smooth (Cramer's rule), so the inverse map $(m, y) \mapsto (m, A(m)^{-1} y)$ is smooth. Conclude that $\psi_U^{-1}$ is a diffeomorphism onto $E|_U$.

> [!note]- Hint 4
> For the reverse direction, set $e_j(m) = \psi_U^{-1}(m, \epsilon_j)$. Why is $e_j$ a smooth section (look at $\pi \circ e_j$)? Why is $(e_j(m))_j$ a basis of $E_m$ (what does linearity of $\psi_U^{-1}$ on the fibre $\{m\} \times \mathbb{R}^k$ do to the standard basis)? Then compose the two constructions both ways; the identity $\psi_U^{-1}(m, x) = \sum_j x^j \psi_U^{-1}(m, \epsilon_j)$ is just linearity on the fibre.

> [!note]- Hint 5
> For the frame-change law, write $s = e\sigma$, substitute $e = e'g$ to get $s = e'(g\sigma)$, and compare with $s = e'\sigma'$. Two expansions of the same section in the *same* frame $e'$ must have equal component columns — that is uniqueness of components. Read off $\sigma' = g\sigma$.

---

# Solution

The correspondence is the bundle-theoretic form of the elementary fact that a basis of a $k$-dimensional vector space is the same datum as a linear isomorphism with $\mathbb{R}^k$; the only geometry beyond that fact is smoothness, and smoothness of the one map that resists direct inversion is obtained by borrowing a pre-existing trivialisation and reducing to smoothness of matrix inversion. We prove the two directions as an explicit construction each way, verify the constructions are mutually inverse, and then read the frame-change law off uniqueness of components.

**Direction 1 (⇐): a frame over $U$ produces a trivialisation, so $E$ is trivial over $U$.**

Let $e = (e_1, \dots, e_k)$ be a local frame over $U$. Define
$$\Psi : U \times \mathbb{R}^k \to E|_U, \qquad \Psi(m, x) = \sum_{j=1}^{k} x^j e_j(m).$$
Then $\Psi$ is a fibrewise-linear diffeomorphism onto $E|_U$ commuting with the projections, so $\psi_U := \Psi^{-1}$ is a local trivialisation and $E$ is trivial over $U$.

> [!note]- Derivation
> **Projection compatibility and fibrewise linearity.** For each $(m, x)$, the vector $\Psi(m, x) = \sum_j x^j e_j(m)$ lies in $E_m$, so $\pi(\Psi(m, x)) = m$: the map covers the identity of $U$ and sends the slice $\{m\} \times \mathbb{R}^k$ into $E_m$. On that slice, $x \mapsto \sum_j x^j e_j(m)$ is linear (linear combination with fixed vectors $e_j(m)$).
>
> **Fibrewise bijectivity.** Fix $m$. Because $e(m) = (e_1(m), \dots, e_k(m))$ is a *basis* of $E_m$, the linear map $x \mapsto \sum_j x^j e_j(m)$ is a bijection $\mathbb{R}^k \to E_m$: it is surjective because a basis spans, and injective because $\sum_j x^j e_j(m) = 0$ forces $x = 0$ by linear independence. Hence $\Psi$ is a bijection on each fibre; since it also covers the identity of $U$, it is a bijection $U \times \mathbb{R}^k \to E|_U$ (every $\xi \in E|_U$ lies in a unique $E_m$ with $m = \pi(\xi) \in U$, and has a unique preimage in $\{m\} \times \mathbb{R}^k$).
>
> **Smoothness of $\Psi$.** Smoothness is local on $U$, so fix $m_0 \in U$. By local triviality of the vector bundle $E$ (part of the [[Def - Vector Bundle|definition of a vector bundle]]), there is an open $V \ni m_0$ and a local trivialisation $\Phi : E|_V \to V \times \mathbb{R}^k$. Shrink to $W := U \cap V$, an open neighbourhood of $m_0$. Since each $e_j$ is a smooth section and $\Phi$ is smooth, the composite $m \mapsto \Phi(e_j(m)) = (m, a_j(m))$ is smooth, so each $a_j : W \to \mathbb{R}^k$ is smooth. For $(m, x) \in W \times \mathbb{R}^k$,
> $$\Phi\big(\Psi(m, x)\big) = \Phi\Big(\sum_j x^j e_j(m)\Big) = \sum_j x^j \Phi(e_j(m)) = \Big(m, \sum_j x^j a_j(m)\Big) = \big(m, A(m) x\big) \qquad \text{(}\Phi_m \text{ linear on } E_m\text{)},$$
> where $A(m) := [\,a_1(m) \mid \dots \mid a_k(m)\,]$ is the matrix with columns $a_j(m)$, smooth in $m$. The map $(m, x) \mapsto (m, A(m) x)$ is smooth (polynomial in $x$ with smooth coefficients), and $\Phi^{-1}$ is smooth, so $\Psi = \Phi^{-1} \circ (m, x) \mapsto (m, A(m)x)$ is smooth on $W$. As $m_0$ was arbitrary, $\Psi$ is smooth on $U \times \mathbb{R}^k$.
>
> **Smoothness of the inverse.** Because $e(m)$ is a basis of $E_m$ and $\Phi_m : E_m \to \{m\} \times \mathbb{R}^k \cong \mathbb{R}^k$ is a linear isomorphism, the columns $a_j(m) = \Phi_m(e_j(m))$ form a basis of $\mathbb{R}^k$; hence $A(m) \in \mathrm{GL}(k, \mathbb{R})$ for every $m \in W$. The inverse of $\Psi$ on $E|_W$ is, in the trivialisation $\Phi$,
> $$\Psi^{-1}\big(\Phi^{-1}(m, y)\big) = \big(m, A(m)^{-1} y\big),$$
> and $m \mapsto A(m)^{-1}$ is smooth because matrix inversion is smooth on $\mathrm{GL}(k, \mathbb{R})$ (Cramer's rule: the entries of $A^{-1}$ are polynomials in those of $A$ over $\det A \neq 0$). Therefore $\Psi^{-1}$ is smooth near every point of $E|_U$. A smooth bijection with smooth inverse is a diffeomorphism, so $\Psi$ is a diffeomorphism $U \times \mathbb{R}^k \to E|_U$.
>
> **Conclusion.** Set $\psi_U := \Psi^{-1} : E|_U \to U \times \mathbb{R}^k$. It is a diffeomorphism; it commutes with the projections (since $\Psi$ covers the identity) and is linear on each fibre (as the inverse of the fibrewise-linear isomorphism $\Psi$). Thus $\psi_U$ is a local trivialisation over $U$, and $E$ is trivial over $U$.

**Direction 2 (⇒): a trivialisation over $U$ produces a frame over $U$.**

Let $\psi_U : E|_U \to U \times \mathbb{R}^k$ be a local trivialisation. Define
$$e_j(m) := \psi_U^{-1}(m, \epsilon_j) \in E_m \qquad (j = 1, \dots, k).$$
Then each $e_j$ is a smooth section over $U$ and $(e_1(m), \dots, e_k(m))$ is a basis of $E_m$ for every $m \in U$, so $e = (e_1, \dots, e_k)$ is a local frame.

> [!note]- Derivation
> **Each $e_j$ is a smooth section.** The map $m \mapsto (m, \epsilon_j)$ is a smooth map $U \to U \times \mathbb{R}^k$ (constant in the second slot), and $\psi_U^{-1}$ is smooth, so $e_j = \psi_U^{-1}(\cdot, \epsilon_j)$ is smooth. It is a section because projection compatibility of $\psi_U$ (hence of $\psi_U^{-1}$) gives $\pi(e_j(m)) = \pi(\psi_U^{-1}(m, \epsilon_j)) = m$, so $\pi \circ e_j = \mathrm{id}_U$ and $e_j(m) \in E_m$.
>
> **$(e_j(m))$ is a basis.** For fixed $m$, the restriction $\psi_U^{-1}|_{\{m\} \times \mathbb{R}^k} : \{m\} \times \mathbb{R}^k \to E_m$ is a linear isomorphism (linearity on fibres of $\psi_U$, and the inverse of a linear isomorphism is a linear isomorphism). A linear isomorphism carries the standard basis $(\epsilon_1, \dots, \epsilon_k)$ of $\mathbb{R}^k$ to a basis of the target; its image is exactly $(e_1(m), \dots, e_k(m))$. Hence $(e_j(m))$ is a basis of $E_m$ for every $m \in U$, and $e$ is a local frame.

**Direction 3: the two constructions are mutually inverse.**

Writing $\mathcal{F}$ for the operation "frame $\mapsto$ trivialisation $\psi_U = \Psi^{-1}$" of Direction 1 and $\mathcal{T}$ for the operation "trivialisation $\mapsto$ frame" of Direction 2, we have $\mathcal{T}(\mathcal{F}(e)) = e$ and $\mathcal{F}(\mathcal{T}(\psi_U)) = \psi_U$.

> [!note]- Derivation
> **$\mathcal{T} \circ \mathcal{F} = \mathrm{id}$.** Start with a frame $e$; Direction 1 gives $\psi_U = \Psi^{-1}$ where $\Psi(m, x) = \sum_j x^j e_j(m)$, so $\psi_U^{-1} = \Psi$. Direction 2 applied to $\psi_U$ returns the sections
> $$\hat e_j(m) = \psi_U^{-1}(m, \epsilon_j) = \Psi(m, \epsilon_j) = \sum_{i=1}^{k} (\epsilon_j)^i\, e_i(m) = e_j(m) \qquad \text{(the } i\text{-th component of } \epsilon_j \text{ is } \delta_{ij}\text{)}.$$
> Hence $\hat e_j = e_j$ for all $j$, so $\mathcal{T}(\mathcal{F}(e)) = e$.
>
> **$\mathcal{F} \circ \mathcal{T} = \mathrm{id}$.** Start with a trivialisation $\psi_U$; Direction 2 gives $e_j = \psi_U^{-1}(\cdot, \epsilon_j)$. Direction 1 applied to this frame gives the trivialisation whose inverse is $\Psi(m, x) = \sum_j x^j e_j(m)$. Compute, using linearity of $\psi_U^{-1}$ on the fibre $\{m\} \times \mathbb{R}^k$,
> $$\Psi(m, x) = \sum_{j=1}^{k} x^j\, \psi_U^{-1}(m, \epsilon_j) = \psi_U^{-1}\Big(m, \sum_{j=1}^{k} x^j \epsilon_j\Big) = \psi_U^{-1}(m, x).$$
> Thus $\Psi = \psi_U^{-1}$, i.e. $\Psi^{-1} = \psi_U$, so $\mathcal{F}(\mathcal{T}(\psi_U)) = \psi_U$.
>
> Therefore $\mathcal{F}$ and $\mathcal{T}$ are mutually inverse bijections between local frames over $U$ and local trivialisations over $U$, establishing the claimed one-to-one correspondence.

**Direction 4: the frame-change law $\sigma' = g\sigma$ (item A-R2.1.3).**

Let $e$ be a frame over $U$ and $e'$ a frame over $U'$, related on $U \cap U'$ by $e = e' g$ with $g : U \cap U' \to \mathrm{GL}(k, \mathbb{R})$ smooth; that is, $e_j = \sum_i e'_i\, g^i{}_j$. Let $s \in \Gamma(U \cap U'; E)$ have component column $\sigma = (\sigma^1, \dots, \sigma^k)^t$ in $e$ and $\sigma' = (\sigma'^1, \dots, \sigma'^k)^t$ in $e'$, so $s = e\sigma = e'\sigma'$. Then $\sigma' = g\sigma$ on $U \cap U'$.

> [!note]- Derivation
> By [[Thm - Local Frames Span Sections|the local-frames-span-sections theorem]] applied over $U \cap U'$, the section $s$ has a *unique* component column in each of the frames $e$ and $e'$; write $s = e\sigma = \sum_j \sigma^j e_j$ and $s = e'\sigma' = \sum_i \sigma'^i e'_i$.
>
> Substitute the frame relation $e = e'g$, i.e. $e_j = \sum_i e'_i g^i{}_j$, into the first expansion:
> $$s = \sum_{j=1}^{k} \sigma^j e_j = \sum_{j=1}^{k} \sigma^j \sum_{i=1}^{k} e'_i\, g^i{}_j = \sum_{i=1}^{k} \Big(\sum_{j=1}^{k} g^i{}_j\, \sigma^j\Big) e'_i = \sum_{i=1}^{k} (g\sigma)^i\, e'_i \qquad \text{(reindex; } (g\sigma)^i = \sum_j g^i{}_j \sigma^j\text{)}.$$
> This exhibits $g\sigma$ as *a* component column of $s$ in the frame $e'$. But $s = \sum_i \sigma'^i e'_i$ exhibits $\sigma'$ as a component column of $s$ in the *same* frame $e'$. By uniqueness of the component expansion in $e'$,
> $$\sigma' = g\sigma \qquad \text{on } U \cap U'.$$
> This is exactly Haydys's Remark A-R2.1.3, in the source's labelling $e = e'g$. (The source writes the same conclusion via $e' = e g^{-1}$: $s = e'\sigma' = e g^{-1} \sigma' = e\sigma$ forces $\sigma = g^{-1}\sigma'$, again $\sigma' = g\sigma$.)

> [!note]- Complete formal solution
> **Claim.** For a rank-$k$ vector bundle $\pi : E \to M$ and open $U \subseteq M$: $E$ is trivial over $U$ if and only if $E$ admits a local frame over $U$; the maps $e \mapsto \big[\psi_U^{-1}(m, x) = \sum_j x^j e_j(m)\big]$ and $\psi_U \mapsto \big[e_j = \psi_U^{-1}(\cdot, \epsilon_j)\big]$ are mutually inverse; and under $e = e'g$ the component columns satisfy $\sigma' = g\sigma$.
>
> ($\Leftarrow$) Given a frame $e$, set $\Psi(m, x) = \sum_j x^j e_j(m)$. It covers $\mathrm{id}_U$ and is linear on each fibre; on each fibre it is a bijection because $e(m)$ is a basis, so $\Psi$ is a bijection $U \times \mathbb{R}^k \to E|_U$. In any local trivialisation $\Phi$ of $E$ over $V$, $\Phi \circ \Psi(m, x) = (m, A(m)x)$ with $A(m) = [\Phi_m e_1(m) \mid \dots \mid \Phi_m e_k(m)]$ smooth and, since $e(m)$ is a basis and $\Phi_m$ an isomorphism, $A(m) \in \mathrm{GL}_k$; hence $\Psi$ and $\Psi^{-1}$ (which is $(m, y) \mapsto \Phi^{-1}(m, A(m)^{-1}y)$, smooth as inversion is smooth on $\mathrm{GL}_k$) are smooth, so $\Psi$ is a diffeomorphism and $\psi_U := \Psi^{-1}$ is a local trivialisation. Thus $E$ is trivial over $U$.
>
> ($\Rightarrow$) Given a trivialisation $\psi_U$, set $e_j = \psi_U^{-1}(\cdot, \epsilon_j)$. Each $e_j$ is smooth (composition of smooth maps) and a section ($\pi \circ e_j = \mathrm{id}_U$ by projection compatibility). On each fibre $\psi_U^{-1}|_{\{m\}\times \mathbb{R}^k}$ is a linear isomorphism, carrying the standard basis $(\epsilon_j)$ to the basis $(e_j(m))$; so $e$ is a frame.
>
> (Inverse) For a frame $e$: applying ($\Rightarrow$) to $\psi_U = \Psi^{-1}$ returns $\psi_U^{-1}(m, \epsilon_j) = \Psi(m, \epsilon_j) = e_j(m)$. For a trivialisation $\psi_U$: applying ($\Leftarrow$) to $e_j = \psi_U^{-1}(\cdot, \epsilon_j)$ returns $\Psi(m, x) = \sum_j x^j \psi_U^{-1}(m, \epsilon_j) = \psi_U^{-1}(m, x)$ by fibrewise linearity. So the constructions are mutually inverse.
>
> (Frame change) With $e = e'g$ and $s = e\sigma = e'\sigma'$, substituting $e_j = \sum_i e'_i g^i{}_j$ gives $s = \sum_i (g\sigma)^i e'_i$; uniqueness of components in $e'$ (local-frames-span-sections) yields $\sigma' = g\sigma$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: taking $\psi_U^{-1}(m,x) = \sum_j x^j e_j(m)$ to be a diffeomorphism "because it is a fibrewise isomorphism"
> Fibrewise linearity and fibrewise bijectivity are *not* enough to conclude that $\Psi(m, x) = \sum_j x^j e_j(m)$ is a diffeomorphism; a map can be a linear isomorphism on every fibre yet fail to be smooth, or have a non-smooth inverse, if the fibrewise data do not vary smoothly. The substantive content — the only place the vector-bundle hypothesis is used — is the passage to a pre-existing trivialisation $\Phi$ in which $\Psi$ becomes $(m, x) \mapsto (m, A(m)x)$ with $A$ *smooth into* $\mathrm{GL}_k$, whence smoothness of both $\Psi$ and $\Psi^{-1}$. The condition that upgrades a pointwise isomorphism to a diffeomorphism is the smoothness of $m \mapsto A(m)$ together with $A(m) \in \mathrm{GL}_k$; drop either and the conclusion fails.

---

# Key Takeaways

**A basis is a coordinate isomorphism, and a smoothly varying basis is a trivialisation — this is the entire correspondence.** At a single point, choosing an ordered basis $(v_1, \dots, v_k)$ of a $k$-dimensional space $V$ is literally the same as choosing a linear isomorphism $\mathbb{R}^k \to V$, namely $x \mapsto \sum_j x^j v_j$; the inverse isomorphism reads off coordinates. A local frame does this at every point of $U$, smoothly; a local trivialisation packages the same coordinate isomorphisms as one diffeomorphism $E|_U \cong U \times \mathbb{R}^k$. Recognising that "frame" and "trivialisation" are two names for one datum lets you switch freely to whichever is convenient — frames to compute with sections as tuples of functions, trivialisations to compare bundles as spaces — and it is the reason the frame bundle $\mathrm{Fr}(E)$, whose sections are frames, controls triviality of $E$. The trigger to apply this: any statement mentioning "there exist $k$ pointwise independent sections", or "a global frame", is a statement about triviality, and conversely.

**Smoothness of an inverse is proved by borrowing a trivialisation and reducing to inversion in $\mathrm{GL}_k$.** The one genuinely non-formal step in the whole exercise is showing that the frame-built map $\Psi$ has a smooth inverse, and the technique is worth isolating because it recurs throughout bundle theory: you cannot invert $\Psi$ by an explicit formula, so you express it, in a pre-existing local trivialisation, as multiplication by a smooth matrix-valued function $A(m)$; invertibility of $A(m)$ comes from the basis hypothesis, and smoothness of $A(m)^{-1}$ comes from the standing fact that inversion is smooth on $\mathrm{GL}(k, \mathbb{R})$ (Cramer's rule). The same manoeuvre proves that a bundle map that is a fibrewise isomorphism is a bundle isomorphism, that the transition functions of a bundle are smooth, and that gauge transformations have smooth inverses. Whenever you must invert a fibrewise-linear construction, reach for a trivialisation and a $\mathrm{GL}_k$-valued matrix; never assert smoothness of an inverse from fibrewise bijectivity alone, as the illegal-shortcut warning records.

**Transformation laws fall out of substitution plus uniqueness of components.** The frame-change law $\sigma' = g\sigma$ is not computed by any special device: one writes the section in one frame, substitutes the relation $e = e'g$ that connects the frames, collects terms into the second frame, and then invokes the uniqueness of the component expansion to equate the two coordinate columns. This substitute-and-match pattern is the source of *every* transformation law in the series — the connection-matrix law $A' = g^{-1}Ag + g^{-1}dg$, the curvature law $F' = g^{-1}Fg$, the gauge action on connections — each is obtained by substituting a frame or gauge relation into a defining identity and reading off the coefficients against a fixed frame. The uniqueness that licenses "read off the coefficients" is exactly [[Thm - Local Frames Span Sections|the local-frames-span-sections theorem]]; keeping that uniqueness in view is what makes such derivations mechanical rather than mysterious. The companion exercises [[Ex - Hom(E,F) is Isomorphic to E-Dual Tensor F]] and [[Ex - Local Triviality of Dual, Tensor, and Exterior Power Bundles]] use the same transition-function bookkeeping in the setting of derived bundles.
