---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Operations on Vector Bundles and Pull-Back Bundles"
  - "Def - Bundle Homomorphism"
  - "Thm - Vector Bundle Construction Lemma"
  - "Def - Transition Function of a Vector Bundle"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $E \to M$ and $F \to M$ be smooth real vector bundles over a common base manifold $M$, of ranks $k$ and $\ell$ respectively. From these one builds the **dual bundle** $E^*$, the **tensor-product bundle** $E^* \otimes F$, and the **homomorphism bundle** $\operatorname{Hom}(E, F)$, whose fibres are
$$(E^*)_m = (E_m)^*, \qquad (E^* \otimes F)_m = E_m^* \otimes F_m, \qquad \operatorname{Hom}(E, F)_m = \operatorname{Hom}(E_m, F_m),$$
each equipped, by the [[Thm - Vector Bundle Construction Lemma|vector-bundle construction lemma]], with the unique smooth bundle structure making the fibrewise data above into a vector bundle.

**Prove that $E^* \otimes F$ is isomorphic to $\operatorname{Hom}(E, F)$ as a vector bundle over $M$** (Haydys, Exercise 2, p. 5, item A-X2.1.1). The natural candidate is the fibrewise map
$$\Phi_m : E_m^* \otimes F_m \longrightarrow \operatorname{Hom}(E_m, F_m), \qquad \Phi_m(\alpha \otimes v) = \big(u \mapsto \alpha(u)\, v\big),$$
extended linearly to all of $E_m^* \otimes F_m$; the task is to show that the collection $\Phi = (\Phi_m)_{m \in M}$ is a smooth bundle homomorphism covering the identity of $M$ and is a linear isomorphism on every fibre, hence a bundle isomorphism.

The intended route is the one the manifest records: verify that in local frames the map $\Phi$ carries the coefficient array of an element of $E^* \otimes F$ to the *same* array read as the entries of a matrix in $\operatorname{Hom}(E, F)$, so that $\Phi$ intertwines the two bundles' transition functions and is therefore a smooth, globally well-defined bundle map; fibrewise bijectivity is then the standard finite-dimensional identity $V^* \otimes W \cong \operatorname{Hom}(V, W)$.

**Recall:**

The objects in play are the derived bundles $E^*$, $E^* \otimes F$, $\operatorname{Hom}(E, F)$ together with their transition functions, the notion of a bundle homomorphism, and the construction lemma that manufactures a bundle from fibrewise data.

![[Def - Bundle Homomorphism#The Definition]]

A **bundle isomorphism** covering the identity of $M$ is a bundle homomorphism $\Phi : G \to H$ (a smooth map with $\pi_H \circ \Phi = \pi_G$ that is linear on each fibre) which is a linear isomorphism $\Phi_m : G_m \to H_m$ on every fibre; its fibrewise inverse is then automatically smooth, so $\Phi$ is a diffeomorphism (see [[Def - Bundle Homomorphism|bundle homomorphism]]).

The three derived bundles are constructed on the sibling page **[[Def - Operations on Vector Bundles and Pull-Back Bundles]]**. What that page establishes, and what we use here, is the following. Fix a common trivialising open set $U \subseteq M$ over which $E$ has a local frame $e = (e_1, \dots, e_k)$ and $F$ a local frame $f = (f_1, \dots, f_\ell)$; write $(e^1, \dots, e^k)$ for the dual coframe of $E$ over $U$, characterised by $e^i(e_j) = \delta^i_j$. The corresponding local trivialisations induce, on each derived bundle over $U$, the following frames and transition functions relative to a second trivialisation with frames $e' = e g$ (so $g : U \cap U' \to \mathrm{GL}(k, \mathbb{R})$ is the $E$-transition matrix) and $f' = f h$ (so $h : U \cap U' \to \mathrm{GL}(\ell, \mathbb{R})$ is the $F$-transition matrix):

- **Dual bundle $E^*$.** Frame $(e^1, \dots, e^k)$; transition function $\tau_{E^*} = (g^{-1})^{t}$ (the contragredient of the $E$-transition), so a covector with column of components $\xi$ in the primed coframe has components $\xi_{\text{unprimed}} = (g^{-1})^{t} \xi$.
- **Tensor bundle $E^* \otimes F$.** Frame $(e^i \otimes f_a)_{1 \le i \le k,\, 1 \le a \le \ell}$; transition function $\tau_{E^* \otimes F} = (g^{-1})^{t} \otimes h$ acting on the array of coefficients.
- **Homomorphism bundle $\operatorname{Hom}(E, F)$.** Frame of "matrix units" $(E_{ai})_{1 \le a \le \ell,\, 1 \le i \le k}$, where $E_{ai} : E_m \to F_m$ is the linear map determined by $E_{ai}(e_j) = \delta_{ij}\, f_a$; transition function $\tau_{\operatorname{Hom}} : \phi \mapsto h \, \phi \, g^{-1}$ acting on the matrix of $\phi$.

![[Def - Transition Function of a Vector Bundle#The Definition]]

![[Thm - Vector Bundle Construction Lemma#Statement]]

Finally, the underlying linear-algebra fact, which we prove inside the solution rather than assume: for finite-dimensional real vector spaces $V$ and $W$, the map $\Phi_{V,W} : V^* \otimes W \to \operatorname{Hom}(V, W)$, $\Phi_{V,W}(\alpha \otimes w)(u) = \alpha(u)\, w$, is a linear isomorphism.

---

# Convergent Strategy

**Problem class.** This is a *canonical-isomorphism* problem in the category of vector bundles: two bundles are built from the same data by two different fibrewise recipes, and we must show that the tautological fibrewise map between them assembles into a global smooth isomorphism. The characteristic difficulty is never the algebra on a single fibre — that is the familiar identity $V^* \otimes W \cong \operatorname{Hom}(V, W)$ — but the passage from a *fibrewise* isomorphism to a *bundle* isomorphism, which requires smoothness and compatibility with the way fibres are glued.

**Assumption pattern.** The only hypotheses are that $E$ and $F$ are smooth vector bundles, so both carry trivialising covers with smooth transition functions valued in a general linear group. The recognisable trigger for the route below is that the candidate map $\Phi$ is defined *without reference to any frame* — its formula $\alpha \otimes v \mapsto (u \mapsto \alpha(u) v)$ uses only the evaluation pairing $E_m^* \times E_m \to \mathbb{R}$, which is intrinsic. Whenever a fibrewise map is frame-independent in this way, global well-definedness is free, and the entire content of "it is a bundle map" collapses to *smoothness*, which one checks in a single arbitrary trivialisation.

**Theorem routing.** The route is: (i) prove $\Phi_{V,W}$ is a linear isomorphism on a single abstract fibre, exhibiting its inverse explicitly; (ii) assemble the fibrewise maps into a global $\Phi : E^* \otimes F \to \operatorname{Hom}(E, F)$ covering $\mathrm{id}_M$, well-defined because the formula is intrinsic; (iii) show smoothness by computing the coordinate expression of $\Phi$ in the induced frames — it is the *identity* array-to-matrix map, hence constant, hence smooth — which is exactly the statement that $\Phi$ intertwines $\tau_{E^* \otimes F} = (g^{-1})^{t} \otimes h$ with $\tau_{\operatorname{Hom}} : \phi \mapsto h \phi g^{-1}$; (iv) conclude by the criterion that a fibrewise-bijective smooth bundle homomorphism is a bundle isomorphism (its inverse is smooth by the same coordinate computation). The [[Thm - Vector Bundle Construction Lemma|construction lemma]] is what legitimises reading "the coordinate expression is the identity" as "the local pieces glue to a smooth global map".

**Key decision point.** The one genuine decision is *not* to prove smoothness by grinding through partial derivatives of the map $\alpha \otimes v \mapsto (u \mapsto \alpha(u) v)$ in charts, but to notice that in the *induced* frames — the dual coframe on $E^*$, the tensor frame $e^i \otimes f_a$, and the matrix-unit frame $E_{ai}$ — the map $\Phi$ sends the basis element $e^i \otimes f_a$ to the basis element $E_{ai}$, so its matrix is a fixed permutation of coordinates, independent of $m$. Constant coordinate expressions are trivially smooth. The transition-function computation is then not an extra burden but the very same fact, phrased so that it certifies the local expressions are consistent across overlaps.

---

# Legal Operations Used

This solution deploys the following operations, each named descriptively (the topic page's Legal Operations for chapter II will be numbered when it is assembled; the orchestrator reconciles the numbering):

1. **Define a bundle map by an intrinsic fibrewise formula.** Because $\Phi_m(\alpha \otimes v)(u) = \alpha(u) v$ uses only the intrinsic evaluation pairing, the family $(\Phi_m)$ defines a single map $\Phi : E^* \otimes F \to \operatorname{Hom}(E, F)$ with $\pi_{\operatorname{Hom}} \circ \Phi = \pi_{E^* \otimes F}$, with no compatibility to check on overlaps.

2. **Prove a fibrewise linear isomorphism by exhibiting the inverse.** On an abstract fibre, produce an explicit two-sided inverse of $\Phi_{V,W}$ using a basis and its dual basis; this proves bijectivity without a dimension count alone.

3. **Read smoothness off the induced frames.** Trivialise $E$ and $F$ over a common $U$ by frames $e, f$; the induced frames $e^i \otimes f_a$ and $E_{ai}$ turn $\Phi|_U$ into the identity map on coefficient arrays, which is smooth because it is constant in $m$.

4. **Certify gluing by intertwining transition functions.** Verify $\Phi \circ \big((g^{-1})^{t} \otimes h\big) = (\phi \mapsto h \phi g^{-1}) \circ \Phi$ on each overlap $U \cap U'$; this is what the [[Thm - Vector Bundle Construction Lemma|construction lemma]] requires to conclude that the local coordinate expressions of $\Phi$ patch to a globally smooth bundle map.

5. **Upgrade a fibrewise-bijective smooth bundle homomorphism to a bundle isomorphism.** A smooth bundle map covering the identity that is a linear isomorphism on every fibre has a smooth fibrewise inverse (visible in the same trivialisation, where inversion is a constant matrix), hence is a bundle isomorphism.

---

# Hints

> [!note]- Hint 1
> The formula $\Phi_m(\alpha \otimes v)(u) = \alpha(u) v$ never mentions a frame. What does that immediately give you for free about whether the different fibrewise maps are consistent — that is, whether $(\Phi_m)_m$ is a single well-defined map $E^* \otimes F \to \operatorname{Hom}(E, F)$? Once you have well-definedness, only two things remain: bijectivity on each fibre, and smoothness.

> [!note]- Hint 2
> For the single-fibre isomorphism, do not count dimensions and invoke "injective plus equal dimension". Instead write down the inverse. Pick a basis $(e_j)$ of $V$ with dual basis $(e^j)$ of $V^*$; given $T \in \operatorname{Hom}(V, W)$, which element of $V^* \otimes W$ does $\Phi_{V,W}$ send to $T$? Try $\sum_j e^j \otimes T(e_j)$ and evaluate.

> [!note]- Hint 3
> For smoothness, choose local frames $e = (e_j)$ of $E$ and $f = (f_a)$ of $F$ over a common open $U$. The bundle $E^* \otimes F$ then has the frame $(e^i \otimes f_a)$, and $\operatorname{Hom}(E, F)$ has the frame of matrix units $E_{ai}$ defined by $E_{ai}(e_j) = \delta_{ij} f_a$. Compute $\Phi(e^i \otimes f_a)$. If it equals $E_{ai}$, what is the coordinate expression of $\Phi$ in these frames, and why is it smooth?

> [!note]- Hint 4
> To be certain the local computation is legitimate globally, verify that $\Phi$ intertwines the transition functions. With $g$ the $E$-transition and $h$ the $F$-transition, the transition of $E^* \otimes F$ is $(g^{-1})^{t} \otimes h$ and that of $\operatorname{Hom}(E, F)$ is $\phi \mapsto h \phi g^{-1}$. Evaluate both $\Phi \circ \big((g^{-1})^{t} \otimes h\big)(\alpha \otimes v)$ and $\big(h \, \Phi(\alpha \otimes v) \, g^{-1}\big)$ on an arbitrary $u$; both should collapse to $\alpha(g^{-1} u)\, h v$.

---

# Solution

The proof separates the two logically distinct claims that a "bundle isomorphism" bundles together. The pointwise claim is pure linear algebra: on each fibre, $\Phi_m$ is the standard isomorphism $V^* \otimes W \cong \operatorname{Hom}(V, W)$, and we prove it by writing its inverse. The global claim is that these pointwise maps fit into a smooth bundle map; because the defining formula is intrinsic, well-definedness is automatic, and smoothness is read directly off the induced frames, where $\Phi$ becomes the identity on coefficient arrays. The transition-function computation is the same identity phrased as a compatibility check, so that the construction lemma certifies the gluing.

**Step 1: $\Phi_m$ is a linear isomorphism of each fibre.**

Fix $m \in M$ and abbreviate $V = E_m$, $W = F_m$, of dimensions $k$ and $\ell$. The map $\Phi_{V,W} : V^* \otimes W \to \operatorname{Hom}(V, W)$, $\Phi_{V,W}(\alpha \otimes w)(u) = \alpha(u) w$, is a linear isomorphism.

> [!note]- Derivation
> We must show three things: that $\Phi_{V,W}$ is well-defined and linear, that it is surjective, and that it is injective. We prove surjectivity and injectivity together by producing a two-sided inverse.
>
> **Well-definedness and linearity.** The assignment $(\alpha, w) \mapsto (u \mapsto \alpha(u) w)$ is bilinear in $(\alpha, w)$: for fixed $w$ it is linear in $\alpha$ because $u \mapsto (\alpha_1 + c\alpha_2)(u) w = \alpha_1(u) w + c\,\alpha_2(u) w$, and for fixed $\alpha$ it is linear in $w$ because $u \mapsto \alpha(u)(w_1 + c w_2) = \alpha(u) w_1 + c\,\alpha(u) w_2$ (both by bilinearity of the pairing and of scalar multiplication in $W$). By the universal property of the tensor product $V^* \otimes W$, this bilinear map factors through a unique linear map $\Phi_{V,W} : V^* \otimes W \to \operatorname{Hom}(V, W)$ (by the [[Def - Tensor Product of Vector Spaces|universal property of the tensor product]]). Each $\Phi_{V,W}(\alpha \otimes w)$ is indeed a linear map $V \to W$: $u \mapsto \alpha(u) w$ is linear because $\alpha$ is linear and scalar multiplication by the fixed $w$ is linear.
>
> **Construction of the inverse.** Choose a basis $(e_1, \dots, e_k)$ of $V$ with dual basis $(e^1, \dots, e^k)$ of $V^*$, characterised by $e^i(e_j) = \delta^i_j$. Define
> $$\Psi : \operatorname{Hom}(V, W) \to V^* \otimes W, \qquad \Psi(T) = \sum_{j=1}^{k} e^j \otimes T(e_j),$$
> which is linear in $T$ because $T \mapsto T(e_j)$ is linear for each $j$ and the tensor is linear in its second slot.
>
> **$\Psi$ is a right inverse: $\Phi_{V,W} \circ \Psi = \mathrm{id}$.** For $T \in \operatorname{Hom}(V, W)$ and any $u \in V$,
> $$\big(\Phi_{V,W}(\Psi(T))\big)(u) = \Phi_{V,W}\!\Big(\sum_j e^j \otimes T(e_j)\Big)(u) = \sum_{j=1}^{k} e^j(u)\, T(e_j) \qquad \text{(definition of } \Phi_{V,W} \text{, linearity)}.$$
> Write $u = \sum_i u^i e_i$ in the basis; then $e^j(u) = u^j$ (since $e^j(e_i) = \delta^j_i$), so
> $$\sum_{j=1}^{k} e^j(u)\, T(e_j) = \sum_{j=1}^{k} u^j\, T(e_j) = T\Big(\sum_{j} u^j e_j\Big) = T(u) \qquad \text{(linearity of } T\text{)}.$$
> As this holds for every $u$, we get $\Phi_{V,W}(\Psi(T)) = T$.
>
> **$\Psi$ is a left inverse: $\Psi \circ \Phi_{V,W} = \mathrm{id}$.** It suffices to check on the spanning elements $\alpha \otimes w$ of $V^* \otimes W$, since both composites are linear. Compute
> $$\Psi\big(\Phi_{V,W}(\alpha \otimes w)\big) = \sum_{j=1}^{k} e^j \otimes \big(\Phi_{V,W}(\alpha \otimes w)\big)(e_j) = \sum_{j=1}^{k} e^j \otimes \big(\alpha(e_j)\, w\big) \qquad \text{(definitions of } \Psi \text{ and } \Phi_{V,W}\text{)}.$$
> Pull the scalar $\alpha(e_j)$ into the first tensor slot and use linearity of $\alpha$:
> $$\sum_{j=1}^{k} \alpha(e_j)\, e^j \otimes w = \Big(\sum_{j=1}^{k} \alpha(e_j)\, e^j\Big) \otimes w = \alpha \otimes w \qquad \text{(since } \sum_j \alpha(e_j)\, e^j = \alpha \text{: both sides agree on each } e_i\text{, giving } \alpha(e_i)\text{)}.$$
> Hence $\Psi \circ \Phi_{V,W} = \mathrm{id}$ on generators, therefore everywhere.
>
> Having a two-sided inverse, $\Phi_{V,W}$ is a linear isomorphism. Applying this with $V = E_m$, $W = F_m$ shows each $\Phi_m$ is a linear isomorphism of fibres.

**Step 2: the fibrewise maps assemble into a global bundle map covering the identity.**

Define $\Phi : E^* \otimes F \to \operatorname{Hom}(E, F)$ by $\Phi|_{(E^* \otimes F)_m} = \Phi_m$ for each $m$. Then $\pi_{\operatorname{Hom}} \circ \Phi = \pi_{E^* \otimes F}$, and $\Phi$ is linear on each fibre; it is a well-defined map because the defining formula is intrinsic.

> [!note]- Derivation
> An element $\xi$ of the total space $E^* \otimes F$ lies in exactly one fibre $(E^* \otimes F)_m$, namely $m = \pi_{E^* \otimes F}(\xi)$; setting $\Phi(\xi) := \Phi_m(\xi)$ therefore assigns to each $\xi$ a single value, and that value lies in $\operatorname{Hom}(E, F)_m = \operatorname{Hom}(E_m, F_m)$, whose base point is again $m$. Hence $\pi_{\operatorname{Hom}}(\Phi(\xi)) = m = \pi_{E^* \otimes F}(\xi)$, so $\Phi$ covers the identity. Linearity on each fibre is Step 1. No consistency condition arises across different fibres: the formula $\alpha \otimes v \mapsto (u \mapsto \alpha(u) v)$ refers only to $\alpha$, $v$, and the intrinsic pairing on the single fibre $E_m$, so there is no dependence on any auxiliary choice (such as a frame) that would have to be checked for compatibility. What remains to prove is that this well-defined fibrewise-linear map is *smooth*.

**Step 3: $\Phi$ is smooth, because in the induced frames it is the identity on coefficient arrays.**

Over any open $U$ carrying frames $e = (e_1, \dots, e_k)$ of $E$ and $f = (f_1, \dots, f_\ell)$ of $F$, the map $\Phi$ sends the induced frame element $e^i \otimes f_a$ of $E^* \otimes F$ to the matrix unit $E_{ai}$ of $\operatorname{Hom}(E, F)$. Consequently the coordinate expression of $\Phi$ in these frames is a fixed (constant-in-$m$) relabelling of coordinates, hence smooth.

> [!note]- Derivation
> Recall the matrix unit $E_{ai} \in \operatorname{Hom}(E, F)$ over $U$ is defined fibrewise by $E_{ai}(m) : E_m \to F_m$, $E_{ai}(m)(e_j(m)) = \delta_{ij}\, f_a(m)$, extended linearly; these $E_{ai}$ form a frame of $\operatorname{Hom}(E, F)$ over $U$ (there are $k\ell$ of them, and at each $m$ they are the standard basis of $\operatorname{Hom}(E_m, F_m)$ relative to the bases $e(m)$, $f(m)$).
>
> Evaluate $\Phi(e^i \otimes f_a)$ at $m$ on the basis vector $e_j(m)$:
> $$\Phi\big(e^i \otimes f_a\big)(m)\big(e_j(m)\big) = e^i(m)\big(e_j(m)\big)\, f_a(m) = \delta^i_j\, f_a(m) \qquad \text{(definition of } \Phi \text{; } e^i(e_j) = \delta^i_j\text{)}.$$
> This is exactly $E_{ai}(m)(e_j(m)) = \delta_{ij} f_a(m)$, and two linear maps agreeing on the basis $(e_j(m))$ are equal, so
> $$\Phi\big(e^i \otimes f_a\big) = E_{ai} \qquad \text{over } U.$$
> Now let $\xi \in \Gamma(U; E^* \otimes F)$ have components $\xi = \sum_{i,a} X^{a}{}_{i}\, e^i \otimes f_a$ with $X^{a}{}_{i} \in C^\infty(U)$. By linearity over $C^\infty(U)$,
> $$\Phi(\xi) = \sum_{i,a} X^{a}{}_{i}\, \Phi(e^i \otimes f_a) = \sum_{i,a} X^{a}{}_{i}\, E_{ai}.$$
> Thus, in the trivialisation of $E^* \otimes F$ by the frame $(e^i \otimes f_a)$ and of $\operatorname{Hom}(E, F)$ by the frame $(E_{ai})$, the map $\Phi$ carries the coordinate array $(X^a{}_i)$ to the coordinate array $(X^a{}_i)$ unchanged. Its coordinate expression $U \times \mathbb{R}^{k\ell} \to U \times \mathbb{R}^{k\ell}$ is $(m, X) \mapsto (m, X)$, the identity, which is smooth. A bundle map is smooth if and only if its coordinate expression in one (equivalently any) pair of local trivialisations covering the base is smooth; the frames $e, f$ exist over a neighbourhood of every point, so $\Phi$ is smooth on all of $M$.

**Step 4: $\Phi$ intertwines the transition functions, so the local expressions patch (construction-lemma check).**

To confirm that the "identity on coefficient arrays" computation of Step 3 is consistent across overlaps — and not an artefact of one frame — verify directly that $\Phi$ intertwines $\tau_{E^* \otimes F} = (g^{-1})^{t} \otimes h$ with $\tau_{\operatorname{Hom}} : \phi \mapsto h \phi g^{-1}$.

> [!note]- Derivation
> Let $U, U'$ overlap, with $E$-transition $g : U \cap U' \to \mathrm{GL}(k, \mathbb{R})$ (so the frames satisfy $e = e' g$ and the contragredient acts on covectors as $\alpha \mapsto \alpha \circ g^{-1}$, i.e. by the matrix $(g^{-1})^{t}$ on components) and $F$-transition $h : U \cap U' \to \mathrm{GL}(\ell, \mathbb{R})$. Take an arbitrary decomposable element $\alpha \otimes v \in E_m^* \otimes F_m$ and an arbitrary $u \in E_m$.
>
> **Left side — transport in $E^* \otimes F$, then apply $\Phi$.** The transition $(g^{-1})^{t} \otimes h$ sends $\alpha \otimes v$ to $(\alpha \circ g^{-1}) \otimes (h v)$ (the contragredient $(g^{-1})^{t}$ acting on the covector $\alpha$ is precomposition with $g^{-1}$; $h$ acts on $v$). Applying $\Phi$ and evaluating at $u$,
> $$\Phi\big((\alpha \circ g^{-1}) \otimes (h v)\big)(u) = (\alpha \circ g^{-1})(u)\, (h v) = \alpha\big(g^{-1} u\big)\, h v \qquad \text{(definition of } \Phi\text{)}.$$
>
> **Right side — apply $\Phi$, then transport in $\operatorname{Hom}(E, F)$.** First $\Phi(\alpha \otimes v) = (u' \mapsto \alpha(u') v)$. The transition $\phi \mapsto h \phi g^{-1}$ sends this to $u \mapsto h\big(\Phi(\alpha \otimes v)(g^{-1} u)\big)$, and
> $$h\big(\Phi(\alpha \otimes v)(g^{-1} u)\big) = h\big(\alpha(g^{-1} u)\, v\big) = \alpha\big(g^{-1} u\big)\, h v \qquad \text{(definition of } \Phi \text{; } h \text{ linear, and } \alpha(g^{-1}u) \text{ is a scalar)}.$$
>
> The two sides agree for every $u$, hence
> $$\Phi \circ \big((g^{-1})^{t} \otimes h\big) = \big(\phi \mapsto h \phi g^{-1}\big) \circ \Phi \qquad \text{on } U \cap U'.$$
> By linearity both composites extend from decomposable elements to all of $E^* \otimes F$ over the overlap, so the intertwining holds identically. This is precisely the compatibility that the [[Thm - Vector Bundle Construction Lemma|construction lemma]] demands: the local coordinate expressions of $\Phi$ (each the identity, by Step 3) are related on overlaps exactly by the two bundles' transition functions, so they define one smooth global bundle map — reconfirming Step 3 without reference to a preferred frame.

**Step 5: conclude that $\Phi$ is a bundle isomorphism.**

$\Phi$ is a smooth bundle homomorphism covering the identity (Steps 2–4) and a linear isomorphism on each fibre (Step 1); therefore it is a bundle isomorphism, and $E^* \otimes F \cong \operatorname{Hom}(E, F)$.

> [!note]- Derivation
> It remains to see that the fibrewise inverse $\Phi^{-1}$, defined by $(\Phi^{-1})_m = (\Phi_m)^{-1}$, is itself smooth, so that $\Phi$ is a diffeomorphism and hence a bundle isomorphism in the strict sense. In the frames of Step 3 the coordinate expression of $\Phi$ is the identity $(m, X) \mapsto (m, X)$; the coordinate expression of $\Phi^{-1}$ is therefore also the identity, which is smooth. (Equivalently: a smooth bundle map covering $\mathrm{id}_M$ that is fibrewise a linear isomorphism has smooth inverse, because in any local trivialisation it is $(m, X) \mapsto (m, B(m) X)$ with $B : U \to \mathrm{GL}(N, \mathbb{R})$ smooth — here $B \equiv \mathrm{id}$ — and $B \mapsto B^{-1}$ is smooth on $\mathrm{GL}(N, \mathbb{R})$ by Cramer's rule.) Thus $\Phi$ and $\Phi^{-1}$ are both smooth, and $\Phi$ is the required isomorphism.

> [!note]- Complete formal solution
> **Claim.** For smooth real vector bundles $E, F \to M$ of ranks $k, \ell$, the fibrewise map $\Phi_m(\alpha \otimes v) = (u \mapsto \alpha(u) v)$ assembles into a bundle isomorphism $\Phi : E^* \otimes F \xrightarrow{\ \sim\ } \operatorname{Hom}(E, F)$ over $M$.
>
> *Fibrewise isomorphism.* Fix $m$ and set $V = E_m$, $W = F_m$. The bilinear map $(\alpha, w) \mapsto (u \mapsto \alpha(u) w)$ induces, by the universal property of $V^* \otimes W$, a linear map $\Phi_m : V^* \otimes W \to \operatorname{Hom}(V, W)$. Choosing a basis $(e_j)$ of $V$ with dual basis $(e^j)$, the linear map $\Psi_m(T) = \sum_j e^j \otimes T(e_j)$ satisfies, for all $u = \sum_i u^i e_i$, $\Phi_m(\Psi_m(T))(u) = \sum_j e^j(u) T(e_j) = \sum_j u^j T(e_j) = T(u)$, and $\Psi_m(\Phi_m(\alpha \otimes w)) = \sum_j e^j \otimes \alpha(e_j) w = \big(\sum_j \alpha(e_j) e^j\big) \otimes w = \alpha \otimes w$. Hence $\Phi_m$ is a linear isomorphism with inverse $\Psi_m$.
>
> *Global bundle map.* Define $\Phi$ fibrewise. It covers $\mathrm{id}_M$ (each $\xi \in (E^* \otimes F)_m$ maps into $\operatorname{Hom}(E_m, F_m)$) and is well-defined because the formula uses only the intrinsic evaluation pairing on the single fibre $E_m$.
>
> *Smoothness.* Over any $U$ with frames $e$ of $E$ and $f$ of $F$, one has $\Phi(e^i \otimes f_a)(e_j) = e^i(e_j) f_a = \delta^i_j f_a = E_{ai}(e_j)$, so $\Phi(e^i \otimes f_a) = E_{ai}$; hence for $\xi = \sum X^a{}_i\, e^i \otimes f_a$ one has $\Phi(\xi) = \sum X^a{}_i\, E_{ai}$, i.e. in the induced trivialisations $\Phi$ is $(m, X) \mapsto (m, X)$, which is smooth. Compatibility across overlaps holds because, with $E$-transition $g$ and $F$-transition $h$, both $\Phi \circ ((g^{-1})^{t} \otimes h)(\alpha \otimes v)$ and $(h\,\Phi(\alpha \otimes v)\,g^{-1})$ evaluate at $u$ to $\alpha(g^{-1} u)\, h v$, so $\Phi$ intertwines $\tau_{E^* \otimes F} = (g^{-1})^{t} \otimes h$ with $\tau_{\operatorname{Hom}} : \phi \mapsto h\phi g^{-1}$; by the [[Thm - Vector Bundle Construction Lemma|construction lemma]] the local expressions patch to a smooth global map.
>
> *Isomorphism.* $\Phi$ is a smooth fibrewise-linear map covering $\mathrm{id}_M$ that is bijective on each fibre; in the induced frames its coordinate expression and that of $\Phi^{-1}$ are both the identity, hence smooth. Therefore $\Phi$ is a bundle isomorphism and $E^* \otimes F \cong \operatorname{Hom}(E, F)$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: "isomorphic on each fibre, therefore isomorphic as bundles"
> It is tempting to stop after Step 1: since $\dim (E_m^* \otimes F_m) = k\ell = \dim \operatorname{Hom}(E_m, F_m)$ and $\Phi_m$ is a fibrewise isomorphism, one might declare the bundles isomorphic. This is a genuine error in bundle theory. Two bundles can be fibrewise isomorphic at every point and still fail to be isomorphic as bundles if no *smooth, globally coherent* family of fibrewise isomorphisms exists — equal fibre dimension only guarantees each bundle is *locally* trivial, not that they are globally the same (for example, the trivial and Möbius line bundles over $S^1$ have one-dimensional fibres yet are non-isomorphic; see [[Ex - The Möbius Bundle is Nontrivial]]). What rescues the present problem is not the dimension count but the fact that the *specific* map $\Phi$ is intrinsic and smooth, established in Steps 2–4. The extra condition that turns fibrewise isomorphism into bundle isomorphism is exactly a *smooth* choice of the fibrewise isomorphisms, and here it is furnished automatically by the intrinsic formula.

---

# Key Takeaways

**An intrinsic fibrewise formula automatically gives a well-defined bundle map; the only remaining work is smoothness.** The engine of the whole proof is that $\Phi_m(\alpha \otimes v)(u) = \alpha(u) v$ mentions no frame, no chart, no partition of unity — only the tautological evaluation pairing $E_m^* \times E_m \to \mathbb{R}$ that every fibre carries by definition. Whenever a map between derived bundles can be written using only such intrinsic operations (the pairing, composition, trace, transpose against a metric, the wedge and interior products), you get well-definedness across fibres for free, and the theorem "this is a bundle map" reduces to a single smoothness check that may be performed in any one convenient trivialisation. The diagnostic to carry forward: *before proving a bundle map is well-defined, ask whether its formula secretly depends on a frame; if it does not, skip straight to smoothness.* This is why canonical isomorphisms of tensor and hom bundles are almost never hard — the difficulty in bundle theory lives in objects defined by gluing choices, not in objects defined by universal formulas.

**Smoothness of a bundle map is a constant-matrix statement in the induced frames.** The proof never differentiates the map $\alpha \otimes v \mapsto (u \mapsto \alpha(u) v)$; instead it computes the map on the induced basis and finds $\Phi(e^i \otimes f_a) = E_{ai}$, so the coordinate expression is the identity permutation of coefficients — visibly smooth because it is constant in the base point. The reusable principle is that the induced frames on $E^*$, $E^* \otimes F$, and $\operatorname{Hom}(E, F)$ are *designed* so that natural maps between these bundles become the standard array-to-matrix identifications of multilinear algebra, which have constant (often identity) coordinate expressions. The trigger condition is any claim "such-and-such natural bundle map is smooth": pass to induced frames, evaluate on basis sections, and read off a constant coordinate matrix. The same tactic proves that the trace $\operatorname{End} E \to \underline{\mathbb{R}}$, the transpose $E^* \otimes E^* \to E^* \otimes E^*$, and the evaluation $\operatorname{Hom}(E, F) \otimes E \to F$ are smooth bundle maps.

**Fibrewise isomorphism plus a smooth coherent family equals bundle isomorphism — and the second half is the whole content.** The most transferable lesson is the precise boundary between linear algebra and geometry drawn by the illegal-shortcut warning. Equal fibre dimensions and a pointwise isomorphism are *necessary but not sufficient* for two bundles to be isomorphic; what is needed in addition is a single smooth section of the bundle $\operatorname{Isom}(E^* \otimes F, \operatorname{Hom}(E, F))$ of fibrewise isomorphisms. In this problem that section exists canonically, but the very same abstract picture — "is there a global smooth trivialising/identifying section?" — is what governs *every* nontrivial classification result later in the series: whether a bundle is trivial (a global frame), whether two principal bundles agree (a global equivariant map), whether a connection is flat (a global parallel frame). Recognising that "$\cong$ on fibres" is cheap and "$\cong$ smoothly and globally" is the real theorem is the habit this exercise instils; it recurs the moment one leaves canonically-defined bundles for bundles built by clutching. Compare the companion exercises [[Ex - Local Frames Correspond to Local Trivialisations]] (where a global frame is exactly a global trivialisation) and [[Ex - Local Triviality of Dual, Tensor, and Exterior Power Bundles]] (where the transition-function check of Step 4 is done for its own sake).
