---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Operations on Vector Bundles and Pull-Back Bundles"
  - "Def - Vector Bundle"
  - "Def - Local Trivialization"
  - "Def - Local Frame"
  - "Def - Bundle Homomorphism"
  - "Def - Dual Space"
  - "Def - Tensor Product of Vector Spaces"
  - "Thm - Universal Property of the Tensor Product"
  - "Thm - Local Frames Span Sections"
tags: [geometry, gauge-theory, vector-bundles]
---

# Problem Statement

Throughout, manifolds are smooth, Hausdorff and second countable, and "smooth" means $C^\infty$; $\Gamma(E)$ denotes the space of smooth sections of a vector bundle $E$. This is Haydys's Exercise 2 (item A-X2.1.1 of the content map, PDF page 5).

Let $\pi_E : E \to M$ and $\pi_F : F \to M$ be smooth real vector bundles over a common base manifold $M$, of ranks $k$ and $l$ respectively. On the page [[Def - Operations on Vector Bundles and Pull-Back Bundles]] the bundles $E^*$, $E^* \otimes F$ and $\operatorname{Hom}(E, F)$ are defined fibrewise — $(E^*)_m = (E_m)^*$, $(E^* \otimes F)_m = (E_m)^* \otimes F_m$, $\operatorname{Hom}(E,F)_m = \operatorname{Hom}(E_m, F_m)$ — and given the smooth structure induced from local trivialisations of $E$ and $F$. Prove that
$$E^* \otimes F \;\cong\; \operatorname{Hom}(E, F)$$
as smooth vector bundles over $M$. More precisely, show that the map $\Theta : E^* \otimes F \to \operatorname{Hom}(E, F)$ whose restriction to the fibre over $m \in M$ is the linear map
$$\Theta_m : (E_m)^* \otimes F_m \longrightarrow \operatorname{Hom}(E_m, F_m), \qquad \alpha \otimes v \longmapsto \big(u \mapsto \alpha(u)\, v\big),$$
is well defined, is a linear isomorphism on every fibre, is smooth, and has a smooth inverse — that is, $\Theta$ is an isomorphism of vector bundles over $M$ in the sense of [[Def - Bundle Homomorphism]].

The intended route: work in local frames. A frame $e = (e_1, \dots, e_k)$ of $E$ and a frame $f = (f_1, \dots, f_l)$ of $F$ over an open set $U \subseteq M$ furnish frames of both $E^* \otimes F$ and $\operatorname{Hom}(E, F)$ over $U$, namely $(\varepsilon^i \otimes f_a)$ and $(f_a \varepsilon^i)$ (the elementary map $e_i \mapsto f_a$), and $\Theta$ carries the first frame to the second. Hence, in the coordinates supplied by these frames, $\Theta$ is the identity on the $l \times k$ coefficient matrices, so it is smooth, bijective, and smoothly invertible; and because the same identity holds for every choice of frames, $\Theta$ respects the transition functions of the two bundles.

**Recall:**

The objects in play are the fibrewise operations on vector bundles, the dual space and tensor product of finite-dimensional vector spaces, the universal property that makes a map out of a tensor product well defined, local trivialisations and frames, and the notion of a bundle isomorphism.

![[Def - Operations on Vector Bundles and Pull-Back Bundles#The Definition]]

For the present exercise the relevant clauses are the three fibrewise constructions $(E^*)_m := (E_m)^*$, $(E^* \otimes F)_m := (E_m)^* \otimes F_m$ and $\operatorname{Hom}(E, F)_m := \operatorname{Hom}(E_m, F_m)$, together with the way these families of vector spaces are made into smooth bundles: if $\psi_E : E|_U \to U \times \mathbb{R}^k$ and $\psi_F : F|_U \to U \times \mathbb{R}^l$ are local trivialisations, with fibre components $\psi_{E,m} : E_m \to \mathbb{R}^k$ and $\psi_{F,m} : F_m \to \mathbb{R}^l$ (the linear isomorphisms with $\psi_E(u) = (m, \psi_{E,m}(u))$ for $u \in E_m$), then the induced local trivialisations are
$$\psi_{E^*}(\alpha) := \big(m,\ \alpha \circ \psi_{E,m}^{-1}\big) \in U \times (\mathbb{R}^k)^* \quad (\alpha \in (E_m)^*),$$
$$\psi_{E^* \otimes F}(\alpha \otimes v) := \big(m,\ (\alpha \circ \psi_{E,m}^{-1}) \otimes \psi_{F,m}(v)\big) \in U \times \big((\mathbb{R}^k)^* \otimes \mathbb{R}^l\big) \quad \text{(extended linearly)},$$
$$\psi_{\operatorname{Hom}(E,F)}(\phi) := \big(m,\ \psi_{F,m} \circ \phi \circ \psi_{E,m}^{-1}\big) \in U \times \operatorname{Hom}(\mathbb{R}^k, \mathbb{R}^l) \quad (\phi \in \operatorname{Hom}(E_m, F_m)),$$
and the smooth structures on the total spaces are the unique ones (by [[Thm - Vector Bundle Construction Lemma]], restated below) for which these maps are smooth local trivialisations; the corresponding transition functions are $(\tau_E^{-1})^{t}$, $(\tau_E^{-1})^t \otimes \tau_F$ and $\phi \mapsto \tau_F\, \phi\, \tau_E^{-1}$. (The model spaces $(\mathbb{R}^k)^*$, $(\mathbb{R}^k)^* \otimes \mathbb{R}^l$ and $\operatorname{Hom}(\mathbb{R}^k, \mathbb{R}^l)$ are finite-dimensional real vector spaces, identified with $\mathbb{R}^k$, $\mathbb{R}^{kl}$ and $\mathbb{R}^{lk}$ by the standard bases named in Step 1 below.)

![[Def - Dual Space#The Definition]]

![[Def - Tensor Product of Vector Spaces#The Definition]]

![[Thm - Universal Property of the Tensor Product#Statement]]

The universal property is the tool that makes $\Theta_m$ well defined: a linear map out of $V \otimes W$ may be specified by its values on elementary tensors $v \otimes w$ provided that the assignment $(v, w) \mapsto (\text{value})$ is bilinear.

![[Def - Local Trivialization#The Definition]]

![[Def - Local Frame#The Definition]]

![[Thm - Local Frames Span Sections#Statement]]

![[Def - Bundle Homomorphism#The Definition]]

A **bundle isomorphism over $M$** is therefore a smooth map $\Theta : E' \to F'$ between bundles over $M$ with $\pi_{F'} \circ \Theta = \pi_{E'}$, linear on each fibre, which is a diffeomorphism whose inverse is again a bundle homomorphism. We shall verify each clause directly.

![[Thm - Vector Bundle Construction Lemma#Statement]]

---

# Convergent Strategy

**Problem class.** This is a *verify-a-canonical-isomorphism* problem of the kind that recurs whenever a linear-algebra identity — here $V^* \otimes W \cong \operatorname{Hom}(V, W)$ for finite-dimensional $V$, $W$ — is to be promoted from vector spaces to vector bundles. The pointwise statement is pure linear algebra; the bundle statement adds exactly one demand, smoothness of the fibrewise map and of its inverse, and that demand is met by exhibiting the map in local trivialisations. The pattern "natural fibrewise isomorphism plus smoothness in trivialisations equals bundle isomorphism" is the engine of the whole page.

**Assumption pattern.** The hypotheses are minimal — two smooth vector bundles over the same base — and the only structure used is the one every vector bundle carries by definition: local trivialisations, and hence local frames. The recognisable trigger is a map between derived bundles that is defined *fibrewise by a formula not involving any choice*: such a map is automatically compatible with every trivialisation, and the question reduces to checking that its expression in one trivialisation (equivalently, one pair of frames) is smooth. The two facts about finite-dimensional linear algebra that are used are that a linear map out of a tensor product is determined by a bilinear map on the factors (the universal property), and that a linear map sending a basis to a basis is an isomorphism.

**Theorem routing.** The route is: define $\Theta_m$ on elementary tensors by the formula $\alpha \otimes v \mapsto \alpha(\cdot)\, v$, check bilinearity in $(\alpha, v)$, and invoke [[Thm - Universal Property of the Tensor Product]] to obtain a well-defined linear map on $(E_m)^* \otimes F_m$; then pick a basis $e_i$ of $E_m$ with dual basis $\varepsilon^i$ (see [[Def - Dual Basis]]) and a basis $f_a$ of $F_m$, compute $\Theta_m(\varepsilon^i \otimes f_a)$ to be the elementary map $f_a \varepsilon^i$, and observe that these $kl$ elementary maps are a basis of $\operatorname{Hom}(E_m, F_m)$, so that $\Theta_m$ maps a basis to a basis and is an isomorphism; finally choose local frames $e$, $f$ over $U$, use [[Thm - Local Frames Span Sections]] to identify sections of both bundles with smooth coefficient matrices $c : U \to \operatorname{Mat}_{l \times k}(\mathbb{R})$, and read off that $\Theta$ is the identity on coefficient matrices — hence its expression in the induced trivialisations is $\operatorname{id}_U \times \Theta_0$ for a fixed linear isomorphism $\Theta_0$ of model spaces, which is smooth with smooth inverse.

**Key decision point.** The one non-obvious decision is *which coordinates to compute in*. Computing in an arbitrary trivialisation of $E^* \otimes F$ and an unrelated trivialisation of $\operatorname{Hom}(E, F)$ produces a matrix-valued function that must then be shown smooth. Computing in the trivialisations *induced from the same pair* $(\psi_E, \psi_F)$ makes $\Theta$ become the constant model map $\Theta_0$, whose smoothness is trivial. The reason this works is *naturality*: $\Theta_m$ is defined by a formula that commutes with every linear isomorphism of $E_m$ and of $F_m$, in particular with $\psi_{E,m}$ and $\psi_{F,m}$. Recognising that a choice-free fibrewise formula is automatically natural, and that naturality lets one transport the computation to the model spaces $\mathbb{R}^k$, $\mathbb{R}^l$, is the whole art.

---

# Legal Operations Used

The topic page [[Gauge Theory II — Vector Bundles, Covariant Derivatives, and Curvature]] numbers the chapter's legal operations; the ones deployed here are named descriptively so the orchestrator can reconcile the numbers.

1. **Define a fibrewise map on elementary tensors and extend by the universal property.** The prescription $\alpha \otimes v \mapsto \alpha(\cdot)\, v$ is only a formula on elementary tensors; the operation that turns it into a linear map on all of $(E_m)^* \otimes F_m$ is the universal property of the tensor product, applicable because the prescription is bilinear in $(\alpha, v)$.

2. **Test a linear map on a basis.** A linear map between finite-dimensional spaces of equal dimension that sends a basis to a basis is an isomorphism; this is how the fibrewise isomorphism is established, with the basis $\varepsilon^i \otimes f_a$ of the source and the elementary maps $f_a \varepsilon^i$ of the target.

3. **Pass from a local trivialisation to a local frame and back.** A local trivialisation $\psi_E$ over $U$ yields the frame $e_i := \psi_E^{-1}(\cdot, \epsilon_i)$ and conversely; this is the content of [[Ex - Local Frames Correspond to Local Trivialisations]]. Here it is used to translate the induced trivialisations of $E^* \otimes F$ and $\operatorname{Hom}(E, F)$ into the induced frames $(\varepsilon^i \otimes f_a)$ and $(f_a \varepsilon^i)$.

4. **Write a section in a frame and compute with its coefficient functions.** By [[Thm - Local Frames Span Sections]] every section of $E^* \otimes F$ over $U$ is $\sum_{a,i} c_{ai}\, \varepsilon^i \otimes f_a$ for unique smooth $c_{ai} \in C^\infty(U)$, and every section of $\operatorname{Hom}(E,F)$ over $U$ is $\sum_{a,i} c_{ai}\, f_a \varepsilon^i$; $\Theta$ acts on the coefficient matrix $c = (c_{ai})$ as the identity.

5. **Verify smoothness of a bundle map in trivialisations.** A fibrewise linear map $\Theta$ over $M$ is smooth if and only if, for trivialisations $\psi$, $\psi'$ of source and target over each $U$ in an open cover, the composite $\psi' \circ \Theta \circ \psi^{-1} : U \times \mathbb{R}^p \to U \times \mathbb{R}^q$ is smooth; smoothness is a local property, and $\psi$, $\psi'$ are diffeomorphisms.

6. **Check compatibility with transition functions to confirm a map is globally defined.** Under frame changes $e = e' g$, $f = f' h$ the coefficient matrix of a section of either bundle transforms as $c \mapsto h\, c\, g^{-1}$; since $\Theta$ is the identity on coefficient matrices in *every* frame pair, the local descriptions of $\Theta$ agree on overlaps, which is a second, independent confirmation that the fibrewise formula defines one global map.

---

# Hints

> [!note]- Hint 1
> Start at a single point $m \in M$ and forget the manifold. You are asked to compare $(E_m)^* \otimes F_m$ with $\operatorname{Hom}(E_m, F_m)$; both are real vector spaces of dimension $kl$. The candidate map sends $\alpha \otimes v$ to the rank-one linear map $u \mapsto \alpha(u) v$. Before anything else, why is this a *well-defined* linear map on the tensor product, given that an element of the tensor product has many expressions as a sum of elementary tensors?

> [!note]- Hint 2
> Bilinearity of $(\alpha, v) \mapsto (u \mapsto \alpha(u) v)$ plus the universal property of the tensor product answers Hint 1. To see that $\Theta_m$ is an isomorphism, pick a basis $e_1, \dots, e_k$ of $E_m$, its dual basis $\varepsilon^1, \dots, \varepsilon^k$ of $(E_m)^*$, and a basis $f_1, \dots, f_l$ of $F_m$. Compute $\Theta_m(\varepsilon^i \otimes f_a)$ on each basis vector $e_j$. What linear map do you get, and do the $kl$ maps so obtained form a basis of $\operatorname{Hom}(E_m, F_m)$?

> [!note]- Hint 3
> $\Theta_m(\varepsilon^i \otimes f_a)(e_j) = \delta^i_j f_a$: the image is the elementary map "$e_i \mapsto f_a$, all other $e_j \mapsto 0$", whose matrix with respect to $(e_j)$ and $(f_b)$ is the matrix unit $E_{ai}$ with a single $1$ in row $a$, column $i$. Matrix units form a basis of $\operatorname{Mat}_{l \times k}(\mathbb{R}) \cong \operatorname{Hom}(E_m, F_m)$. So $\Theta_m$ sends the basis $(\varepsilon^i \otimes f_a)$ to a basis and is an isomorphism. Now for smoothness: let the bases vary — take local frames $e$ of $E$ and $f$ of $F$ over $U$. Then $(\varepsilon^i \otimes f_a)$ is a local frame of $E^* \otimes F$ and $(f_a \varepsilon^i)$ a local frame of $\operatorname{Hom}(E,F)$, and a section of either bundle is a smooth coefficient matrix $c : U \to \operatorname{Mat}_{l \times k}(\mathbb{R})$. What does $\Theta$ do to $c$?

> [!note]- Hint 4
> $\Theta$ is the identity on coefficient matrices: $\Theta\big(\sum c_{ai}\, \varepsilon^i \otimes f_a\big) = \sum c_{ai}\, f_a \varepsilon^i$. In the trivialisations induced by the frames, $\Theta$ is therefore $(m, c) \mapsto (m, c)$ — the identity of $U \times \mathbb{R}^{lk}$ up to the fixed linear identification of the two model spaces. That is smooth, bijective, with smooth inverse. Cover $M$ by such $U$ and conclude. To see the same fact from the transition-function side, change frames by $e = e'g$ and $f = f'h$ and check that the coefficient matrix of a section of $E^* \otimes F$ and that of a section of $\operatorname{Hom}(E,F)$ both transform as $c \mapsto h c g^{-1}$.

---

# Solution

The proof separates cleanly into a pointwise part and a smoothness part. Pointwise, $\Theta_m$ is well defined by the universal property of the tensor product and is an isomorphism because it carries the basis $\varepsilon^i \otimes f_a$ of $(E_m)^* \otimes F_m$ onto the basis of elementary maps of $\operatorname{Hom}(E_m, F_m)$. For smoothness we let those bases come from local frames: then sections of both bundles over $U$ are smooth $l \times k$ coefficient matrices, $\Theta$ is the identity on coefficient matrices, and consequently in the induced trivialisations $\Theta$ is $\operatorname{id}_U \times \Theta_0$ for a fixed linear isomorphism $\Theta_0$ of model spaces — smooth, with smooth inverse.

**Step 0: Fix notation and the model map — what is to be shown.**

We fix ranks $k = \operatorname{rk} E$, $l = \operatorname{rk} F$, write $\epsilon_1, \dots, \epsilon_k$ for the standard basis of $\mathbb{R}^k$ and $\epsilon^1, \dots, \epsilon^k$ for its dual basis of $(\mathbb{R}^k)^*$ (so $\epsilon^i(\epsilon_j) = \delta^i_j$), and similarly $\phi_1, \dots, \phi_l$ for the standard basis of $\mathbb{R}^l$. We must show four things: (i) $\Theta_m$ is a well-defined linear map for every $m$; (ii) $\Theta_m$ is bijective for every $m$; (iii) $\Theta$ is smooth and covers the identity of $M$; (iv) $\Theta^{-1}$ is smooth (and is then automatically fibrewise linear, being the inverse of a fibrewise linear bijection).

> [!note]- Derivation
> **The model map.** Define $\Theta_0 : (\mathbb{R}^k)^* \otimes \mathbb{R}^l \to \operatorname{Hom}(\mathbb{R}^k, \mathbb{R}^l)$ by the same formula as $\Theta_m$, that is $\Theta_0(\lambda \otimes y) := (x \mapsto \lambda(x)\, y)$ for $\lambda \in (\mathbb{R}^k)^*$ and $y \in \mathbb{R}^l$. Steps 1 and 2 below, applied to the vector spaces $V = \mathbb{R}^k$ and $W = \mathbb{R}^l$ in place of $E_m$ and $F_m$, show that $\Theta_0$ is a well-defined linear isomorphism; being a linear map between finite-dimensional vector spaces, $\Theta_0$ is smooth, and so is its inverse (a linear map $\mathbb{R}^p \to \mathbb{R}^q$ is given by a matrix, hence is a polynomial map, hence smooth).
>
> **Covering the identity.** By construction $\Theta$ maps the fibre $(E^* \otimes F)_m$ into the fibre $\operatorname{Hom}(E,F)_m$, so $\pi_{\operatorname{Hom}(E,F)} \circ \Theta = \pi_{E^* \otimes F}$: the covering condition of [[Def - Bundle Homomorphism]] holds with base map $\operatorname{id}_M$.
>
> **Reduction of (iv) to (iii).** Once (ii) and (iii) are known, $\Theta$ is a smooth bijection $E^* \otimes F \to \operatorname{Hom}(E,F)$; the inverse map $\Theta^{-1}$ exists as a set map, is fibrewise linear (the inverse of a linear bijection $\Theta_m$ is linear), and covers $\operatorname{id}_M$. What remains for (iv) is its smoothness, which Step 4 supplies together with (iii).

**Step 1: $\Theta_m$ is a well-defined linear map — the universal property.**

For fixed $m$, the assignment $(\alpha, v) \mapsto (u \mapsto \alpha(u) v)$ is a bilinear map $(E_m)^* \times F_m \to \operatorname{Hom}(E_m, F_m)$, so by the universal property of the tensor product there is a unique linear map $\Theta_m$ on $(E_m)^* \otimes F_m$ with $\Theta_m(\alpha \otimes v) = (u \mapsto \alpha(u) v)$.

> [!note]- Derivation
> Fix $m \in M$ and abbreviate $V := E_m$, $W := F_m$. Define $B : V^* \times W \to \operatorname{Hom}(V, W)$ by
> $$B(\alpha, v) := \big(u \mapsto \alpha(u)\, v\big) \qquad (\alpha \in V^*,\ v \in W).$$
>
> **$B(\alpha, v)$ is a linear map $V \to W$:** for $u_1, u_2 \in V$ and $\lambda \in \mathbb{R}$,
> $$B(\alpha, v)(u_1 + \lambda u_2) = \alpha(u_1 + \lambda u_2)\, v = \big(\alpha(u_1) + \lambda \alpha(u_2)\big) v = B(\alpha,v)(u_1) + \lambda B(\alpha, v)(u_2) \qquad \text{(linearity of } \alpha \text{, then the vector-space axioms of } W\text{)}.$$
>
> **$B$ is bilinear:** for $\alpha_1, \alpha_2 \in V^*$, $\lambda \in \mathbb{R}$, $v \in W$ and every $u \in V$,
> $$B(\alpha_1 + \lambda \alpha_2, v)(u) = (\alpha_1 + \lambda \alpha_2)(u)\, v = \alpha_1(u) v + \lambda\, \alpha_2(u) v = \big(B(\alpha_1, v) + \lambda B(\alpha_2, v)\big)(u) \qquad \text{(pointwise operations in } V^* \text{; vector-space axioms of } W\text{)},$$
> and for $v_1, v_2 \in W$,
> $$B(\alpha, v_1 + \lambda v_2)(u) = \alpha(u)\,(v_1 + \lambda v_2) = \alpha(u) v_1 + \lambda\, \alpha(u) v_2 = \big(B(\alpha, v_1) + \lambda B(\alpha, v_2)\big)(u) \qquad \text{(distributivity in } W\text{)}.$$
> Since two linear maps $V \to W$ that agree on every $u$ are equal, $B$ is linear in each argument separately.
>
> **Apply the universal property.** By [[Thm - Universal Property of the Tensor Product]] — for finite-dimensional $V$, $W$ and any vector space $U'$, every bilinear map $\Gamma : V^* \times W \to U'$ factors uniquely as $\Gamma = \hat\Gamma \circ \otimes$ with $\hat\Gamma : V^* \otimes W \to U'$ linear — applied to $\Gamma = B$ and $U' = \operatorname{Hom}(V, W)$, there is a unique linear map $\Theta_m := \hat B : V^* \otimes W \to \operatorname{Hom}(V, W)$ with $\Theta_m(\alpha \otimes v) = B(\alpha, v) = (u \mapsto \alpha(u) v)$ for all $\alpha$, $v$. The hypotheses of the theorem are met: $V^* = (E_m)^*$ and $W = F_m$ are finite-dimensional (of dimensions $k$ and $l$, by [[Thm - Dimension of Dual Space]] for the first). This is (i).

**Step 2: $\Theta_m$ is an isomorphism — it carries a basis to a basis.**

With a basis $(e_j)$ of $E_m$, its dual basis $(\varepsilon^i)$, and a basis $(f_a)$ of $F_m$, one has $\Theta_m(\varepsilon^i \otimes f_a) = f_a \varepsilon^i$, the linear map sending $e_i$ to $f_a$ and every other $e_j$ to $0$; the $kl$ maps $f_a \varepsilon^i$ form a basis of $\operatorname{Hom}(E_m, F_m)$, so $\Theta_m$ maps the basis $(\varepsilon^i \otimes f_a)$ of $(E_m)^* \otimes F_m$ bijectively onto a basis, and is therefore a linear isomorphism.

> [!note]- Derivation
> Keep $V = E_m$, $W = F_m$. Choose a basis $e_1, \dots, e_k$ of $V$ (possible since $\dim V = k$), let $\varepsilon^1, \dots, \varepsilon^k \in V^*$ be the dual basis ([[Def - Dual Basis]]: the unique functionals with $\varepsilon^i(e_j) = \delta^i_j$; they form a basis of $V^*$ by [[Thm - Dimension of Dual Space]]), and choose a basis $f_1, \dots, f_l$ of $W$.
>
> **The source basis.** By the basis clause of [[Def - Tensor Product of Vector Spaces]] (if $(x_i)$ is a basis of $X$ and $(y_a)$ a basis of $Y$ then $(x_i \otimes y_a)$ is a basis of $X \otimes Y$), the $kl$ elements $\varepsilon^i \otimes f_a$, $1 \le i \le k$, $1 \le a \le l$, form a basis of $V^* \otimes W$.
>
> **Images of the source basis.** For each $i$, $a$ and each $j$,
> $$\Theta_m(\varepsilon^i \otimes f_a)(e_j) = \varepsilon^i(e_j)\, f_a = \delta^i_j\, f_a \qquad \text{(definition of } \Theta_m \text{ on elementary tensors; definition of the dual basis)}.$$
> Write $f_a \varepsilon^i \in \operatorname{Hom}(V, W)$ for the linear map determined by $e_j \mapsto \delta^i_j f_a$ (a linear map is determined by its values on a basis, and any prescription of values on a basis extends uniquely to a linear map). Then $\Theta_m(\varepsilon^i \otimes f_a) = f_a \varepsilon^i$.
>
> **The target basis.** We claim that $\{f_a \varepsilon^i\}_{a, i}$ is a basis of $\operatorname{Hom}(V, W)$.
>
> *Spanning:* let $\phi \in \operatorname{Hom}(V, W)$. Expand each $\phi(e_j) \in W$ in the basis $(f_a)$: $\phi(e_j) = \sum_{a=1}^l c_{aj} f_a$ for unique scalars $c_{aj} \in \mathbb{R}$ (uniqueness of coordinates in a basis). Then for every $j$,
> $$\Big(\sum_{a,i} c_{ai}\, f_a \varepsilon^i\Big)(e_j) = \sum_{a,i} c_{ai}\, \delta^i_j\, f_a = \sum_a c_{aj} f_a = \phi(e_j) \qquad \text{(definition of } f_a \varepsilon^i\text{; the Kronecker delta collapses the } i\text{-sum)},$$
> so the two linear maps $\sum_{a,i} c_{ai} f_a \varepsilon^i$ and $\phi$ agree on the basis $(e_j)$ and hence are equal.
>
> *Linear independence:* if $\sum_{a,i} c_{ai} f_a \varepsilon^i = 0$ in $\operatorname{Hom}(V, W)$, evaluate at $e_j$: $0 = \sum_{a,i} c_{ai} \delta^i_j f_a = \sum_a c_{aj} f_a$, and linear independence of $(f_a)$ gives $c_{aj} = 0$ for all $a$; as $j$ was arbitrary, all $c_{ai}$ vanish.
>
> Hence $\{f_a \varepsilon^i\}$ is a basis of $\operatorname{Hom}(V, W)$; in particular $\dim \operatorname{Hom}(V, W) = kl = \dim(V^* \otimes W)$.
>
> **Conclusion of Step 2.** $\Theta_m$ is linear (Step 1) and maps the basis $(\varepsilon^i \otimes f_a)$ of the source bijectively onto the basis $(f_a \varepsilon^i)$ of the target. A linear map that sends a basis onto a basis is an isomorphism: it is surjective because its image contains a spanning set, and injective because if $\Theta_m\big(\sum c_{ai} \varepsilon^i \otimes f_a\big) = \sum c_{ai} f_a \varepsilon^i = 0$ then all $c_{ai} = 0$ by linear independence of the target basis. This is (ii). Note also, for later use, that the coordinate description of $\Theta_m$ in these bases is the identity on coefficient arrays: $\Theta_m\big(\sum_{a,i} c_{ai}\, \varepsilon^i \otimes f_a\big) = \sum_{a,i} c_{ai}\, f_a \varepsilon^i$ (linearity of $\Theta_m$ and the images just computed).

**Step 3: Local frames of $E^* \otimes F$ and $\operatorname{Hom}(E,F)$ induced from frames of $E$ and $F$, and the identification of sections with coefficient matrices.**

If $e = (e_1, \dots, e_k)$ and $f = (f_1, \dots, f_l)$ are local frames of $E$ and $F$ over $U$, then the pointwise dual coframe $\varepsilon = (\varepsilon^1, \dots, \varepsilon^k)$ is a local frame of $E^*$ over $U$, $(\varepsilon^i \otimes f_a)$ is a local frame of $E^* \otimes F$ over $U$, and $(f_a \varepsilon^i)$ is a local frame of $\operatorname{Hom}(E, F)$ over $U$; every section of either bundle over $U$ is $\sum_{a,i} c_{ai}(\cdot)\, (\text{frame element})$ for a unique smooth coefficient matrix $c = (c_{ai}) : U \to \operatorname{Mat}_{l \times k}(\mathbb{R})$.

> [!note]- Derivation
> Let $\psi_E : E|_U \to U \times \mathbb{R}^k$ be the local trivialisation corresponding to $e$ — namely $\psi_E^{-1}(m, x) = \sum_j x_j e_j(m)$, which is a local trivialisation by [[Ex - Local Frames Correspond to Local Trivialisations]] (given a local frame $e$ over $U$, the map $(m, x) \mapsto e(m) \cdot x$ is a fibrewise linear diffeomorphism $U \times \mathbb{R}^k \to E|_U$ covering $\operatorname{id}_U$, and $e_j = \psi_E^{-1}(\cdot, \epsilon_j)$) — and $\psi_F : F|_U \to U \times \mathbb{R}^l$ the one corresponding to $f$. In fibre components, $\psi_{E,m}(e_j(m)) = \epsilon_j$ and $\psi_{F,m}(f_a(m)) = \phi_a$.
>
> **The coframe.** Define $\varepsilon^i(m) \in (E_m)^*$ as the dual basis of $(e_j(m))$, that is $\varepsilon^i(m)(e_j(m)) = \delta^i_j$. Then $\varepsilon^i(m) \circ \psi_{E,m}^{-1} = \epsilon^i$ for every $m$ (both sides are functionals on $\mathbb{R}^k$ taking the value $\delta^i_j$ on $\epsilon_j$), so in the induced trivialisation of $E^*$ recalled in the Problem Statement, $\psi_{E^*}(\varepsilon^i(m)) = (m, \epsilon^i)$: the map $m \mapsto \varepsilon^i(m)$ equals $\psi_{E^*}^{-1} \circ (m \mapsto (m, \epsilon^i))$, a composition of smooth maps (the second factor is smooth as a map into a product with constant second component; $\psi_{E^*}^{-1}$ is smooth because $\psi_{E^*}$ is a diffeomorphism), hence a smooth section of $E^*$ over $U$; and $(\varepsilon^i(m))_i$ is a basis of $(E_m)^*$ at every $m$. So $\varepsilon$ is a local frame of $E^*$ over $U$ in the sense of [[Def - Local Frame]].
>
> **The frames of the derived bundles.** By the same computation,
> $$\psi_{E^* \otimes F}\big(\varepsilon^i(m) \otimes f_a(m)\big) = \big(m,\ \epsilon^i \otimes \phi_a\big), \qquad \psi_{\operatorname{Hom}(E,F)}\big(f_a(m) \varepsilon^i(m)\big) = \big(m,\ \psi_{F,m} \circ f_a(m)\varepsilon^i(m) \circ \psi_{E,m}^{-1}\big) = \big(m,\ \phi_a \epsilon^i\big),$$
> where the last equality holds because both sides send $\epsilon_j$ to $\delta^i_j \phi_a$: indeed $\psi_{F,m}\big(f_a(m)\varepsilon^i(m)(\psi_{E,m}^{-1}\epsilon_j)\big) = \psi_{F,m}\big(f_a(m)\varepsilon^i(m)(e_j(m))\big) = \psi_{F,m}(\delta^i_j f_a(m)) = \delta^i_j \phi_a$ (definition of $\psi_E$, definition of the elementary map, linearity of $\psi_{F,m}$). Hence each $m \mapsto \varepsilon^i(m) \otimes f_a(m)$ and each $m \mapsto f_a(m)\varepsilon^i(m)$ is the composite of a smooth map $m \mapsto (m, \text{constant})$ with the smooth inverse of a trivialisation, so is a smooth section; and at each $m$ the values form bases of $(E_m)^* \otimes F_m$ and of $\operatorname{Hom}(E_m, F_m)$ respectively (Step 2). Therefore $(\varepsilon^i \otimes f_a)_{a,i}$ and $(f_a \varepsilon^i)_{a,i}$ are local frames over $U$ of $E^* \otimes F$ and of $\operatorname{Hom}(E,F)$.
>
> **Sections as coefficient matrices.** By [[Thm - Local Frames Span Sections]] — for a smooth local frame $(\sigma_1, \dots, \sigma_r)$ of a rank-$r$ bundle over $U$, every smooth section over $U$ is uniquely $\sum_\mu c^\mu \sigma_\mu$ with $c^\mu \in C^\infty(U)$, and conversely every such tuple defines a smooth section — every $\omega \in \Gamma(U; E^* \otimes F)$ is $\omega = \sum_{a,i} c_{ai}\, \varepsilon^i \otimes f_a$ and every $\phi \in \Gamma(U; \operatorname{Hom}(E,F))$ is $\phi = \sum_{a,i} c_{ai}\, f_a \varepsilon^i$, in each case for a unique smooth $c = (c_{ai}) : U \to \operatorname{Mat}_{l \times k}(\mathbb{R})$. For $\phi$ the entries have a direct meaning: $c_{ai}$ is the $(a, i)$ entry of the matrix of $\phi(m)$ with respect to the bases $e(m)$, $f(m)$, that is $\phi(m)(e_i(m)) = \sum_a c_{ai}(m) f_a(m)$ (Step 2, spanning argument).

**Step 4: $\Theta$ is the identity on coefficient matrices, hence smooth with smooth inverse.**

For every frame pair $(e, f)$ over $U$, $\Theta\big(\sum c_{ai}\, \varepsilon^i \otimes f_a\big) = \sum c_{ai}\, f_a \varepsilon^i$; in the induced trivialisations this reads $\psi_{\operatorname{Hom}(E,F)} \circ \Theta \circ \psi_{E^* \otimes F}^{-1} = \operatorname{id}_U \times \Theta_0$, which is a diffeomorphism of $U \times \mathbb{R}^{kl}$ onto $U \times \mathbb{R}^{lk}$. Since the sets $U$ over which frames exist cover $M$, $\Theta$ is smooth and $\Theta^{-1}$ is smooth.

> [!note]- Derivation
> **The coefficient-matrix form.** By Step 2 (last sentence) applied at each $m \in U$, $\Theta_m\big(\sum_{a,i} c_{ai}(m)\, \varepsilon^i(m) \otimes f_a(m)\big) = \sum_{a,i} c_{ai}(m)\, f_a(m) \varepsilon^i(m)$. Thus, on sections over $U$, $\Theta$ sends the section with coefficient matrix $c$ in the frame $(\varepsilon^i \otimes f_a)$ to the section with the same coefficient matrix $c$ in the frame $(f_a \varepsilon^i)$.
>
> **The trivialised form.** For $(m, z) \in U \times \big((\mathbb{R}^k)^* \otimes \mathbb{R}^l\big)$ write $z = \sum_{a,i} c_{ai}\, \epsilon^i \otimes \phi_a$ with constants $c_{ai}$ (basis clause of the tensor product). Then
> $$\psi_{E^* \otimes F}^{-1}(m, z) = \sum_{a,i} c_{ai}\, \varepsilon^i(m) \otimes f_a(m) \qquad \text{(Step 3: } \psi_{E^* \otimes F}(\varepsilon^i(m) \otimes f_a(m)) = (m, \epsilon^i \otimes \phi_a)\text{, and } \psi_{E^* \otimes F, m} \text{ is linear)},$$
> $$\Theta\big(\psi_{E^* \otimes F}^{-1}(m, z)\big) = \sum_{a,i} c_{ai}\, f_a(m) \varepsilon^i(m) \qquad \text{(coefficient-matrix form of } \Theta\text{)},$$
> $$\psi_{\operatorname{Hom}(E,F)}\Big(\sum_{a,i} c_{ai}\, f_a(m)\varepsilon^i(m)\Big) = \Big(m,\ \sum_{a,i} c_{ai}\, \phi_a \epsilon^i\Big) = \big(m,\ \Theta_0(z)\big) \qquad \text{(Step 3; linearity of } \psi_{\operatorname{Hom}(E,F), m}\text{; Step 2 for } \Theta_0 \text{ in the standard bases)}.$$
> Combining the three displayed lines,
> $$\psi_{\operatorname{Hom}(E,F)} \circ \Theta \circ \psi_{E^* \otimes F}^{-1} = \operatorname{id}_U \times \Theta_0 : U \times \big((\mathbb{R}^k)^* \otimes \mathbb{R}^l\big) \to U \times \operatorname{Hom}(\mathbb{R}^k, \mathbb{R}^l).$$
>
> **Smoothness.** The map $\operatorname{id}_U \times \Theta_0$ is smooth (each component is smooth: the identity, and a linear map between finite-dimensional spaces), bijective (Step 0: $\Theta_0$ is an isomorphism), with inverse $\operatorname{id}_U \times \Theta_0^{-1}$, also smooth. Therefore, on $\pi^{-1}(U) \subseteq E^* \otimes F$,
> $$\Theta|_{\pi^{-1}(U)} = \psi_{\operatorname{Hom}(E,F)}^{-1} \circ (\operatorname{id}_U \times \Theta_0) \circ \psi_{E^* \otimes F}$$
> is a composition of smooth maps (the trivialisations are diffeomorphisms by [[Def - Local Trivialization]]), hence smooth, and likewise $\Theta^{-1}|_{\pi^{-1}(U)} = \psi_{E^* \otimes F}^{-1} \circ (\operatorname{id}_U \times \Theta_0^{-1}) \circ \psi_{\operatorname{Hom}(E,F)}$ is smooth. Every point of $M$ lies in some open $U$ over which $E$ and $F$ both admit local frames (intersect a trivialising neighbourhood of $E$ with one of $F$, and take the frames $\psi_E^{-1}(\cdot, \epsilon_j)$, $\psi_F^{-1}(\cdot, \phi_a)$ by [[Ex - Local Frames Correspond to Local Trivialisations]]), and smoothness of a map is a local property (a map is smooth if and only if it is smooth on the members of an open cover of its domain, [[Def - Smooth Map between Manifolds]]). Hence $\Theta$ and $\Theta^{-1}$ are smooth on all of their domains. This is (iii) and (iv).
>
> **Second confirmation: compatibility with the transition functions.** The manifest's route asks that we also see directly that "the identity on coefficient matrices" is consistent across frame changes. Let $e' = (e'_1, \dots, e'_k)$ and $f' = (f'_1, \dots, f'_l)$ be second frames over $U$, and let $g : U \to GL_k(\mathbb{R})$, $h : U \to GL_l(\mathbb{R})$ be the smooth matrix functions with $e = e' g$ and $f = f' h$, meaning $e_j = \sum_i e'_i g_{ij}$ and $f_a = \sum_b f'_b h_{ba}$ (they exist and are smooth by [[Ex - Local Frames Correspond to Local Trivialisations]], part (e)). The dual coframes are related by $\varepsilon'^{\,i} = \sum_j g_{ij}\, \varepsilon^j$, because $\big(\sum_j g_{ij} \varepsilon^j\big)(e_l) = g_{il}$ and $\varepsilon'^{\,i}(e_l) = \varepsilon'^{\,i}\big(\sum_r e'_r g_{rl}\big) = g_{il}$ (definition of the dual basis; $e = e'g$), so the two functionals agree on the basis $(e_l)$; inverting, $\varepsilon^j = \sum_i (g^{-1})_{ji}\, \varepsilon'^{\,i}$.
>
> *Coefficients in $E^* \otimes F$:*
> $$\sum_{a,i} c_{ai}\, \varepsilon^i \otimes f_a = \sum_{a,i} c_{ai} \Big(\sum_r (g^{-1})_{ir}\, \varepsilon'^{\,r}\Big) \otimes \Big(\sum_b h_{ba} f'_b\Big) = \sum_{b,r} \Big(\sum_{a,i} h_{ba}\, c_{ai}\, (g^{-1})_{ir}\Big) \varepsilon'^{\,r} \otimes f'_b = \sum_{b,r} (h\, c\, g^{-1})_{br}\, \varepsilon'^{\,r} \otimes f'_b \qquad \text{(bilinearity of } \otimes\text{; definition of matrix product)}.$$
>
> *Coefficients in $\operatorname{Hom}(E,F)$:* for $\phi = \sum_{a,i} c_{ai} f_a \varepsilon^i$, so that $\phi(e_i) = \sum_a c_{ai} f_a$, the matrix $c'$ with respect to $(e', f')$ is read off from
> $$\phi(e'_r) = \phi\Big(\sum_j e_j (g^{-1})_{jr}\Big) = \sum_j (g^{-1})_{jr} \sum_a c_{aj} f_a = \sum_{j,a,b} (g^{-1})_{jr}\, c_{aj}\, h_{ba}\, f'_b = \sum_b (h\, c\, g^{-1})_{br}\, f'_b \qquad \text{(} e' = e g^{-1} \text{ from } e = e'g\text{; linearity of } \phi\text{; } f = f'h\text{)},$$
> so $c' = h c g^{-1}$ as well. Both coefficient matrices transform by the same rule $c \mapsto h c g^{-1}$ (these are the transition functions $(\tau_E^{-1})^t \otimes \tau_F$ and $\phi \mapsto \tau_F \phi \tau_E^{-1}$ recalled in the Problem Statement, written on coefficient matrices with $\tau_E = g$, $\tau_F = h$). Consequently "the identity on coefficient matrices" defines the same map whether computed in $(e, f)$ or in $(e', f')$: the local descriptions of $\Theta$ over overlapping frame domains agree, which is exactly the statement that $\Theta$ respects the transition functions of the two bundles. (This is of course automatic, since $\Theta$ was defined fibrewise without any choices; the computation makes the automatic fact visible.)

> [!note]- Complete formal solution
> **Claim.** Let $E$, $F$ be smooth real vector bundles over $M$ of ranks $k$, $l$. The map $\Theta : E^* \otimes F \to \operatorname{Hom}(E, F)$, $\Theta(\alpha \otimes v) = (u \mapsto \alpha(u) v)$ on elementary tensors of each fibre, is an isomorphism of vector bundles over $M$.
>
> We must show that $\Theta$ is well defined and linear on each fibre, bijective on each fibre, smooth, covers $\operatorname{id}_M$, and has a smooth inverse.
>
> **Step 1 (fibrewise well-definedness).** Fix $m \in M$. The map $B : (E_m)^* \times F_m \to \operatorname{Hom}(E_m, F_m)$, $B(\alpha, v) = (u \mapsto \alpha(u) v)$, takes values in linear maps (linearity of $\alpha$) and is bilinear (pointwise operations in $(E_m)^*$; distributivity in $F_m$). By the [[Thm - Universal Property of the Tensor Product|universal property of the tensor product]] — every bilinear map out of $V \times W$, for finite-dimensional $V$, $W$, factors uniquely through a linear map on $V \otimes W$ — there is a unique linear $\Theta_m : (E_m)^* \otimes F_m \to \operatorname{Hom}(E_m, F_m)$ with $\Theta_m(\alpha \otimes v) = B(\alpha, v)$. Since $\Theta_m$ maps the fibre over $m$ to the fibre over $m$, $\Theta$ covers $\operatorname{id}_M$.
>
> **Step 2 (fibrewise isomorphism).** Choose a basis $(e_j)$ of $E_m$ with dual basis $(\varepsilon^i)$ and a basis $(f_a)$ of $F_m$. The elements $\varepsilon^i \otimes f_a$ form a basis of $(E_m)^* \otimes F_m$ (basis clause of [[Def - Tensor Product of Vector Spaces]]). For each $j$, $\Theta_m(\varepsilon^i \otimes f_a)(e_j) = \varepsilon^i(e_j) f_a = \delta^i_j f_a$ (definition of $\Theta_m$; definition of the dual basis), so $\Theta_m(\varepsilon^i \otimes f_a) = f_a \varepsilon^i$, the linear map with $e_j \mapsto \delta^i_j f_a$. The maps $f_a \varepsilon^i$ span $\operatorname{Hom}(E_m, F_m)$: given $\phi$, write $\phi(e_j) = \sum_a c_{aj} f_a$; then $\sum_{a,i} c_{ai} f_a \varepsilon^i$ agrees with $\phi$ on every $e_j$, hence equals $\phi$. They are linearly independent: $\sum_{a,i} c_{ai} f_a \varepsilon^i = 0$ evaluated at $e_j$ gives $\sum_a c_{aj} f_a = 0$, so $c_{aj} = 0$ by linear independence of $(f_a)$. Hence $\Theta_m$ maps a basis bijectively onto a basis and is a linear isomorphism, with $\Theta_m\big(\sum c_{ai} \varepsilon^i \otimes f_a\big) = \sum c_{ai} f_a \varepsilon^i$ (linearity).
>
> **Step 3 (local frames and coefficient matrices).** Let $U \subseteq M$ be open with local frames $e$ of $E$ and $f$ of $F$ over $U$, with associated trivialisations $\psi_E$, $\psi_F$ ([[Ex - Local Frames Correspond to Local Trivialisations]]: $\psi_E^{-1}(m, x) = \sum_j x_j e_j(m)$, so $\psi_{E,m}(e_j(m)) = \epsilon_j$, and likewise $\psi_{F,m}(f_a(m)) = \phi_a$). Let $\varepsilon^i(m)$ be the dual basis of $e(m)$. In the induced trivialisations of $E^* \otimes F$ and $\operatorname{Hom}(E,F)$ (recalled in the Problem Statement from [[Def - Operations on Vector Bundles and Pull-Back Bundles]]), $\psi_{E^* \otimes F}(\varepsilon^i(m) \otimes f_a(m)) = (m, \epsilon^i \otimes \phi_a)$ and $\psi_{\operatorname{Hom}(E,F)}(f_a(m)\varepsilon^i(m)) = (m, \phi_a \epsilon^i)$, because $\varepsilon^i(m) \circ \psi_{E,m}^{-1} = \epsilon^i$ and $\psi_{F,m} \circ f_a(m)\varepsilon^i(m) \circ \psi_{E,m}^{-1}$ sends $\epsilon_j$ to $\delta^i_j \phi_a$ (both verified on the standard basis). Hence $m \mapsto \varepsilon^i(m) \otimes f_a(m)$ and $m \mapsto f_a(m) \varepsilon^i(m)$ are smooth sections (composites of $m \mapsto (m, \text{const})$ with the diffeomorphisms $\psi^{-1}$), pointwise bases (Step 2), so local frames of $E^* \otimes F$ and $\operatorname{Hom}(E,F)$ over $U$.
>
> **Step 4 (trivialised form of $\Theta$ and smoothness).** Let $\Theta_0 : (\mathbb{R}^k)^* \otimes \mathbb{R}^l \to \operatorname{Hom}(\mathbb{R}^k, \mathbb{R}^l)$ be the map of Steps 1–2 for $V = \mathbb{R}^k$, $W = \mathbb{R}^l$: a linear isomorphism with $\Theta_0(\epsilon^i \otimes \phi_a) = \phi_a \epsilon^i$, smooth with smooth inverse (linear maps between finite-dimensional spaces are polynomial). For $(m, z) \in U \times ((\mathbb{R}^k)^* \otimes \mathbb{R}^l)$ with $z = \sum c_{ai} \epsilon^i \otimes \phi_a$,
> $$\psi_{\operatorname{Hom}(E,F)}\Big(\Theta\big(\psi_{E^* \otimes F}^{-1}(m, z)\big)\Big) = \psi_{\operatorname{Hom}(E,F)}\Big(\Theta\Big(\sum c_{ai}\, \varepsilon^i(m) \otimes f_a(m)\Big)\Big) = \psi_{\operatorname{Hom}(E,F)}\Big(\sum c_{ai}\, f_a(m)\varepsilon^i(m)\Big) = \Big(m, \sum c_{ai}\, \phi_a \epsilon^i\Big) = (m, \Theta_0 z)$$
> (Step 3 and linearity of the fibre maps of $\psi_{E^* \otimes F}$; Step 2; Step 3 and linearity of the fibre maps of $\psi_{\operatorname{Hom}(E,F)}$; definition of $\Theta_0$). Thus $\psi_{\operatorname{Hom}(E,F)} \circ \Theta \circ \psi_{E^* \otimes F}^{-1} = \operatorname{id}_U \times \Theta_0$, a diffeomorphism. Since the trivialisations are diffeomorphisms ([[Def - Local Trivialization]]), $\Theta|_{\pi^{-1}(U)} = \psi_{\operatorname{Hom}(E,F)}^{-1} \circ (\operatorname{id}_U \times \Theta_0) \circ \psi_{E^* \otimes F}$ and $\Theta^{-1}|_{\pi^{-1}(U)} = \psi_{E^* \otimes F}^{-1} \circ (\operatorname{id}_U \times \Theta_0^{-1}) \circ \psi_{\operatorname{Hom}(E,F)}$ are smooth. The open sets $U$ carrying frames of both $E$ and $F$ cover $M$ (intersect trivialising neighbourhoods and use $\psi^{-1}(\cdot, \epsilon_j)$), and smoothness is local, so $\Theta$ and $\Theta^{-1}$ are smooth everywhere.
>
> **Conclusion.** $\Theta$ is a smooth map $E^* \otimes F \to \operatorname{Hom}(E,F)$ covering $\operatorname{id}_M$, linear and bijective on every fibre, with smooth (and fibrewise linear) inverse; by [[Def - Bundle Homomorphism]] it is an isomorphism of vector bundles over $M$. Therefore $E^* \otimes F \cong \operatorname{Hom}(E, F)$. $\blacksquare$

> [!warning] Illegal but tempting: "the fibres are isomorphic, so the bundles are isomorphic"
> It is tempting to stop after Step 2: every fibre $(E_m)^* \otimes F_m$ is isomorphic to $\operatorname{Hom}(E_m, F_m)$, so "the bundles are isomorphic". This inference is invalid in general — two bundles of the same rank over the same base always have isomorphic fibres (both are $\mathbb{R}^r$), yet the Möbius bundle over $S^1$ and the trivial line bundle $S^1 \times \mathbb{R}$ have isomorphic fibres and are not isomorphic ([[Ex - The Möbius Bundle is Nontrivial]]). What rescues the present case is that the fibrewise isomorphisms $\Theta_m$ are chosen *coherently*: they are given by one formula with no choices, so they assemble into a map that is smooth in the trivialisations. The extra condition that makes "fibrewise isomorphic" into "isomorphic as bundles" is precisely that the family $(\Theta_m)_m$ be smooth as a map of total spaces — Steps 3–4.

**Sanity check.** Take $k = l = 1$, so $E$ and $F$ are line bundles. Then $E^* \otimes F$ and $\operatorname{Hom}(E, F)$ are line bundles, a local frame of $E$ is a single nowhere-vanishing section $e_1$, with dual coframe $\varepsilon^1 = 1/e_1$ in the sense $\varepsilon^1(e_1) = 1$, and a frame of $F$ is a nowhere-vanishing $f_1$. The exercise says that a section $c\, \varepsilon^1 \otimes f_1$ of $E^* \otimes F$ corresponds to the homomorphism $e_1 \mapsto c f_1$; under $e_1 = g e'_1$, $f_1 = h f'_1$ with nowhere-vanishing scalar functions $g$, $h$ the coefficient transforms as $c \mapsto h c g^{-1}$ on both sides, as computed. For $E = F$ this identifies $\operatorname{End}(L) = L^* \otimes L$ with the trivial line bundle: the coefficient $c$ is then frame-independent ($h = g$), and the identity section $\operatorname{id}_L$ corresponds to $c \equiv 1$, that is to $\varepsilon^1 \otimes e_1$ — the calibration check on [[Def - Operations on Vector Bundles and Pull-Back Bundles]] that $\operatorname{End} E$ has the identity section.

---

# Key Takeaways

**A canonical linear-algebra isomorphism becomes a bundle isomorphism as soon as its expression in induced trivialisations is smooth — and a choice-free formula makes that expression constant.** The structural lesson is the separation of the problem into a pointwise statement and a smoothness statement. Pointwise, $V^* \otimes W \cong \operatorname{Hom}(V, W)$ is elementary: the map $\alpha \otimes v \mapsto \alpha(\cdot)v$ is defined on elementary tensors by a bilinear rule, so it is a well-defined linear map, and it sends the basis $\varepsilon^i \otimes f_a$ to the basis of matrix units, so it is an isomorphism. The bundle statement adds smoothness, and the efficient way to obtain smoothness is not to compute the map in arbitrary coordinates but in coordinates *induced from a common choice* — a frame $e$ of $E$ and a frame $f$ of $F$. Because $\Theta_m$ is defined without choices, it commutes with the identifications $\psi_{E,m}$ and $\psi_{F,m}$ of the fibres with the model spaces, and in the induced trivialisations it becomes the constant map $\operatorname{id}_U \times \Theta_0$. Whenever a fibrewise construction is natural in this sense — the same formula in every fibre, commuting with all linear isomorphisms — the smoothness check reduces to the observation that a constant linear map is smooth. This pattern recurs for every natural isomorphism of derived bundles: $(E \otimes F)^* \cong E^* \otimes F^*$, $\Lambda^p(E^*) \cong (\Lambda^p E)^*$, $\operatorname{End}(E) \cong E^* \otimes E$, and the identification $\Omega^p(M; E) = \Gamma(\Lambda^p T^*M \otimes E)$ used throughout [[Def - Bundle-Valued Differential Forms]].

**Coefficient matrices are the working currency of local bundle computations, and their transformation law is the fingerprint of the bundle.** Once frames $e$ and $f$ are fixed over $U$, a section of $E^* \otimes F$ and a section of $\operatorname{Hom}(E,F)$ are both nothing more than a smooth $l \times k$ matrix function $c : U \to \operatorname{Mat}_{l \times k}(\mathbb{R})$, by [[Thm - Local Frames Span Sections]]. The exercise shows that the two bundles agree not only in this local description but in how the description changes under frame change: $c \mapsto h c g^{-1}$ for $e = e' g$, $f = f' h$. The transformation law is what distinguishes bundles that are locally indistinguishable; two derived bundles whose coefficient matrices transform identically under all frame changes are isomorphic, via the map that is the identity on coefficients. The trigger for using this diagnostic is any claim that two bundles built from $E$ and $F$ "are the same": compute the transformation law of coefficients on each side, and if they agree the identity on coefficients is the isomorphism. The same diagnostic, run in reverse, is what shows that the connection matrix $A$ of [[Def - Connection Matrix and Local Form of a Connection]] is *not* the coefficient matrix of a section of $\operatorname{End} E$: its transformation law $A' = g^{-1} A g + g^{-1} dg$ carries the inhomogeneous term $g^{-1} dg$ that no tensorial object has.

**The exercise is what makes $\Omega^1(M; \operatorname{End} E)$ and $\operatorname{Hom}$-valued forms usable in the rest of the chapter.** The identification $\operatorname{Hom}(E, F) \cong E^* \otimes F$ is invoked silently every time one writes a $\operatorname{Hom}(E,F)$-valued form as $\sum \omega_{ai} \otimes f_a \varepsilon^i$, contracts an $\operatorname{End} E$-valued form against an $E$-valued form, or regards the difference of two connections — a $C^\infty(M)$-linear map $\Gamma(E) \to \Omega^1(M; E)$ — as an element $a \in \Omega^1(M; \operatorname{End} E)$ by [[Thm - Tensoriality Lemma for C-Infinity-Linear Maps]]. The tensoriality lemma produces, from a $C^\infty(M)$-linear operator, a section of $\Lambda^p T^*M \otimes \operatorname{Hom}(E, F)$; that this is the same thing as a section of $\Lambda^p T^*M \otimes E^* \otimes F$, and hence that the contraction $\operatorname{End}(E) \otimes E \to E$ can be applied to it, is exactly the content proved here. The reader who returns to this page after months should remember the single sentence that reconstructs it: *the map is the identity on coefficient matrices in every frame pair, and both sides' coefficients transform as $c \mapsto h c g^{-1}$.*

A companion exercise is [[Ex - Local Triviality of Dual, Tensor, and Exterior Power Bundles]], which verifies that the induced trivialisations used here really do satisfy the cocycle condition and make $E^*$, $E \otimes F$ and $\operatorname{Hom}(E,F)$ into smooth bundles via the construction lemma; and [[Ex - Local Frames Correspond to Local Trivialisations]] supplies the frame–trivialisation dictionary used in Steps 3 and 4.
