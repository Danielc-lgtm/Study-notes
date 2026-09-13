---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Complex Vector Bundle and Hermitian Structure"
  - "Thm - Existence of Smooth Partitions of Unity"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M$ be a smooth manifold and let $E \to M$ be a **complex vector bundle**: a smooth real vector bundle of rank $2k$ equipped with a bundle endomorphism $I \in \Gamma(\operatorname{End} E)$ satisfying $I^2 = -\operatorname{id}$, so that each fibre $E_m$ becomes a complex vector space of complex dimension $k$ under $i \cdot v := I_m v$. Prove:

$$E \text{ admits a Hermitian structure.}$$

Concretely: construct a smooth family $h = (h_m)_{m \in M}$ of Hermitian inner products on the fibres — for each $m$ a map $h_m : E_m \times E_m \to \mathbb{C}$ that is complex-linear in its first slot, conjugate-linear in its second, satisfies $h_m(u, v) = \overline{h_m(v, u)}$, and is positive definite ($h_m(v, v) > 0$ for $v \neq 0$) — such that for all smooth sections $s, t \in \Gamma(E)$ the function $m \mapsto h_m(s(m), t(m))$ is smooth.

This is part (i) of Haydys Exercise 29 (item A-X2.2.4(i) in the source inventory).

**Recall:**

The objects in play are a complex vector bundle and its fibrewise complex structure $I$, a Hermitian inner product on a single complex vector space, and the existence of smooth partitions of unity subordinate to a cover.

![[Def - Complex Vector Bundle and Hermitian Structure#The Definition]]

A [[Def - Complex Vector Bundle and Hermitian Structure|Hermitian structure]] on $(E, I)$ is a smooth section $h$ of the real vector bundle $\mathcal{H}(E) \to M$ whose fibre $\mathcal{H}(E)_m$ is the real vector space of **Hermitian forms** on the complex vector space $(E_m, I_m)$ — the $\mathbb{R}$-bilinear maps $b : E_m \times E_m \to \mathbb{C}$ with $b(I_m u, v) = i\, b(u, v)$, $b(u, I_m v) = -i\, b(u, v)$, and $b(u, v) = \overline{b(v, u)}$ — such that $h_m$ is positive definite for every $m$. The Hermitian forms sit inside $(E \otimes_{\mathbb{R}} E)^*$ as a smooth sub-bundle, so "smooth section" and "gluing by a partition of unity" have their usual meaning; the positive-definite Hermitian forms make up an open convex cone $\mathcal{H}^+(E)_m \subseteq \mathcal{H}(E)_m$ in each fibre.

![[Thm - Existence of Smooth Partitions of Unity#Statement]]

We also use the standing fact, part of the definition of a complex vector bundle (its equivalent description as a locally trivial family of complex vector spaces, Haydys X2.2.3(i)), that $(E, I)$ admits an open cover $\{U_\alpha\}_{\alpha \in A}$ together with **complex-linear local trivialisations** $\psi_\alpha : E|_{U_\alpha} \xrightarrow{\ \cong\ } U_\alpha \times \mathbb{C}^k$, meaning each restriction $\psi_{\alpha, m} : E_m \to \mathbb{C}^k$ is a complex-linear isomorphism (it intertwines $I_m$ with multiplication by $i$).

---

# Convergent Strategy

**Problem class.** This is an *existence-of-a-global-geometric-structure* problem, and it belongs to the single most reused template in differential geometry: *build the structure locally where the bundle is trivial, then average the local pieces into one global piece with a partition of unity.* It is the exact analogue, in the complex-sesquilinear category, of the standard proof that every smooth vector bundle admits a Euclidean (Riemannian) metric; the only new wrinkle is that the fibrewise object is a Hermitian form rather than a real inner product, and one must check that Hermitian symmetry and $I$-compatibility survive the averaging.

**Assumption pattern.** Two hypotheses do all the work, each used once. The complex-bundle hypothesis is used *only* to obtain complex-linear local trivialisations, which give a model Hermitian form to pull back on each $U_\alpha$. Smoothness of $M$ (paracompactness) is used *only* to obtain a partition of unity subordinate to the trivialising cover. Recognising this split — "local triviality gives me local structures, paracompactness lets me glue" — is the whole diagnostic; whenever a desired structure is *pointwise convex* and *locally available*, this pair of hypotheses manufactures it globally.

**Theorem routing.** The route is: invoke the complex-linear trivialisations $\psi_\alpha$ to define $h_\alpha := \psi_\alpha^* \langle \cdot, \cdot \rangle_{\mathrm{std}}$ on each $U_\alpha$; invoke [[Thm - Existence of Smooth Partitions of Unity|the partition-of-unity theorem]] to obtain $\{\rho_\alpha\}$ subordinate to $\{U_\alpha\}$; set $h := \sum_\alpha \rho_\alpha h_\alpha$ (each summand extended by zero off $\operatorname{supp}\rho_\alpha$); then verify sesquilinearity, Hermitian symmetry, smoothness, and — the one substantive step — positive definiteness, which rests on the convexity of the cone of positive-definite Hermitian forms.

**Key decision point.** The only non-mechanical move is realising *why the average of Hermitian inner products is again a Hermitian inner product, and in particular still positive definite.* Positive definiteness is not a linear condition, so it is not automatically preserved by taking $\mathbb{R}$-linear combinations; what saves the argument is that the coefficients $\rho_\alpha(m)$ are non-negative and sum to $1$, and at each point at least one is strictly positive. A convex combination of non-negative-plus-one-strictly-positive terms is strictly positive. This is the precise reason the construction uses a *partition of unity* (non-negative, summing to one) rather than any old smooth gluing.

---

# Legal Operations Used

The Gauge Theory III topic page's Legal Operations are the reference numbering; until that page is assembled the operations are named descriptively here and the orchestrator will reconcile the numbers.

1. **Trivialise locally and pull back the model structure.** On each set $U_\alpha$ of a trivialising cover, transport the standard Hermitian product of the model fibre $\mathbb{C}^k$ back to $E|_{U_\alpha}$ through the complex-linear trivialisation $\psi_\alpha$. This produces a local Hermitian structure $h_\alpha$ on $E|_{U_\alpha}$ at essentially no cost, because the model $\mathbb{C}^k$ already carries a canonical Hermitian product.

2. **Glue local structures with a subordinate partition of unity.** Choose a smooth partition of unity $\{\rho_\alpha\}$ subordinate to the trivialising cover $\{U_\alpha\}$ and form the weighted sum $\sum_\alpha \rho_\alpha h_\alpha$. This is the standard mechanism for turning locally defined tensor fields into a single global tensor field.

3. **Extend a locally defined tensor by zero using support control.** Each $h_\alpha$ is defined only on $U_\alpha$, but $\rho_\alpha h_\alpha$ has support inside $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$ and extends by zero to a globally defined smooth section of $\mathcal{H}(E)$; local finiteness of the supports makes the sum smooth.

4. **Preserve positivity by averaging inside a convex cone.** The positive-definite Hermitian forms in each fibre make up a convex cone; a convex combination of them (non-negative weights summing to one, at least one weight positive) stays inside the cone. This is the operation that lets a linear averaging construction respect a non-linear (positivity) constraint.

---

# Hints

> [!note]- Hint 1
> You want a global object, and the bundle is *locally trivial*. What is the canonical Hermitian object on the model fibre $\mathbb{C}^k$? Once you have a Hermitian structure over each trivialising open set, what standard device lets you assemble local objects into a global one on a smooth manifold?

> [!note]- Hint 2
> Over a set $U_\alpha$ with a complex-linear trivialisation $\psi_\alpha : E|_{U_\alpha} \to U_\alpha \times \mathbb{C}^k$, define $h_\alpha(u, v) := \langle \psi_\alpha(u), \psi_\alpha(v) \rangle_{\mathrm{std}}$ where $\langle z, w \rangle_{\mathrm{std}} = \sum_{j=1}^k z_j \overline{w_j}$. Check this is a Hermitian inner product on each fibre of $E|_{U_\alpha}$. Then take a partition of unity $\{\rho_\alpha\}$ subordinate to $\{U_\alpha\}$ and consider $h = \sum_\alpha \rho_\alpha h_\alpha$.

> [!note]- Hint 3
> Sesquilinearity and Hermitian symmetry of $h = \sum_\alpha \rho_\alpha h_\alpha$ are immediate because the $\rho_\alpha(m)$ are *real* scalars and a real-linear combination of sesquilinear (respectively Hermitian-symmetric) forms is again sesquilinear (respectively Hermitian-symmetric). The one thing that is *not* automatic is positive definiteness. Write out $h_m(v, v)$ for $v \neq 0$ as $\sum_\alpha \rho_\alpha(m) h_{\alpha, m}(v, v)$ and use the two defining properties of a partition of unity: the weights are non-negative and they sum to $1$.

> [!note]- Hint 4
> For $v \neq 0$: every term $\rho_\alpha(m) h_{\alpha, m}(v, v)$ is $\geq 0$ (non-negative weight times a positive number, where $h_{\alpha, m}$ is defined). Because $\sum_\alpha \rho_\alpha(m) = 1$, at least one index $\alpha_0$ has $\rho_{\alpha_0}(m) > 0$, and there $h_{\alpha_0, m}(v, v) > 0$ since $h_{\alpha_0}$ is a genuine inner product and $m \in \operatorname{supp}\rho_{\alpha_0} \subseteq U_{\alpha_0}$. Hence the total sum is strictly positive.

---

# Solution

The construction is the sesquilinear version of "every smooth vector bundle carries a Riemannian metric": pull back the standard Hermitian product of $\mathbb{C}^k$ on each trivialising open set to get local Hermitian structures, then blend them with a partition of unity. The only genuinely load-bearing verification is that positive definiteness survives the blend, and it survives precisely because the partition-of-unity weights are non-negative and sum to one, so the average is a *convex* combination of positive-definite forms.

**Step 1: Manufacture a local Hermitian structure on each trivialising set.**

Over each $U_\alpha$ the complex-linear trivialisation $\psi_\alpha$ pulls the standard Hermitian product of $\mathbb{C}^k$ back to a Hermitian inner product $h_\alpha$ on the fibres of $E|_{U_\alpha}$, varying smoothly.

> [!note]- Derivation
> Because $(E, I)$ is a complex vector bundle, it admits an open cover $\{U_\alpha\}_{\alpha \in A}$ with complex-linear local trivialisations $\psi_\alpha : E|_{U_\alpha} \to U_\alpha \times \mathbb{C}^k$, each fibre map $\psi_{\alpha, m} : E_m \to \mathbb{C}^k$ being a $\mathbb{C}$-linear isomorphism (it intertwines $I_m$ with multiplication by $i$). Let
> $$\langle z, w \rangle_{\mathrm{std}} := \sum_{j=1}^k z_j\, \overline{w_j}, \qquad z = (z_1,\dots,z_k),\ w = (w_1,\dots,w_k) \in \mathbb{C}^k,$$
> denote the standard Hermitian inner product on $\mathbb{C}^k$: complex-linear in $z$, conjugate-linear in $w$, with $\langle w, z\rangle_{\mathrm{std}} = \overline{\langle z, w\rangle_{\mathrm{std}}}$ and $\langle z, z\rangle_{\mathrm{std}} = \sum_j |z_j|^2 > 0$ for $z \neq 0$. For $m \in U_\alpha$ and $u, v \in E_m$ define
> $$h_{\alpha, m}(u, v) := \big\langle \psi_{\alpha, m}(u),\, \psi_{\alpha, m}(v) \big\rangle_{\mathrm{std}}. \qquad \text{(pull-back of the model product)}$$
> This is a Hermitian inner product on $(E_m, I_m)$, checked clause by clause:
> - *Complex-linear in the first slot.* $h_{\alpha,m}(I_m u, v) = \langle \psi_{\alpha,m}(I_m u), \psi_{\alpha,m}(v)\rangle_{\mathrm{std}} = \langle i\, \psi_{\alpha,m}(u), \psi_{\alpha,m}(v)\rangle_{\mathrm{std}} = i\, h_{\alpha,m}(u,v)$ (since $\psi_{\alpha,m}$ is $\mathbb{C}$-linear, then $\langle\cdot,\cdot\rangle_{\mathrm{std}}$ is complex-linear in its first slot), and additivity is inherited from $\psi_{\alpha,m}$ and $\langle\cdot,\cdot\rangle_{\mathrm{std}}$.
> - *Conjugate-linear in the second slot.* $h_{\alpha,m}(u, I_m v) = \langle \psi_{\alpha,m}(u), i\,\psi_{\alpha,m}(v)\rangle_{\mathrm{std}} = -i\, h_{\alpha,m}(u,v)$ (conjugate-linearity of $\langle\cdot,\cdot\rangle_{\mathrm{std}}$ in its second slot).
> - *Hermitian symmetry.* $h_{\alpha,m}(v, u) = \langle \psi_{\alpha,m}(v), \psi_{\alpha,m}(u)\rangle_{\mathrm{std}} = \overline{\langle \psi_{\alpha,m}(u), \psi_{\alpha,m}(v)\rangle_{\mathrm{std}}} = \overline{h_{\alpha,m}(u, v)}$ (Hermitian symmetry of the model).
> - *Positive definiteness.* For $v \neq 0$, $\psi_{\alpha,m}(v) \neq 0$ (as $\psi_{\alpha,m}$ is an isomorphism), so $h_{\alpha,m}(v, v) = \langle \psi_{\alpha,m}(v), \psi_{\alpha,m}(v)\rangle_{\mathrm{std}} > 0$.
>
> Smoothness: for smooth sections $s, t$ of $E$ over $U_\alpha$, the components of $\psi_\alpha \circ s$ and $\psi_\alpha \circ t$ are smooth $\mathbb{C}$-valued functions, and $h_\alpha(s, t) = \sum_j (\psi_\alpha s)_j\, \overline{(\psi_\alpha t)_j}$ is a finite sum of products of smooth functions, hence smooth. Thus $h_\alpha$ is a smooth section of $\mathcal{H}^+(E)$ over $U_\alpha$.

**Step 2: Choose a partition of unity subordinate to the trivialising cover.**

Since $M$ is a smooth manifold and $\{U_\alpha\}$ is an open cover, there is a smooth partition of unity subordinate to it.

> [!note]- Derivation
> By [[Thm - Existence of Smooth Partitions of Unity|the existence of smooth partitions of unity]] — for any open cover $\{U_\alpha\}_{\alpha \in A}$ of a smooth manifold $M$ there exist smooth functions $\rho_\alpha : M \to [0, 1]$ with (1) $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$ for each $\alpha$, (2) the family $\{\operatorname{supp}\rho_\alpha\}_{\alpha \in A}$ locally finite, and (3) $\sum_{\alpha} \rho_\alpha(m) = 1$ for every $m \in M$ (a finite sum at each point) — apply this to the trivialising cover $\{U_\alpha\}$ of Step 1 to obtain such a family $\{\rho_\alpha\}_{\alpha \in A}$.

**Step 3: Assemble the global candidate and verify it is a smooth section.**

Define $h := \sum_\alpha \rho_\alpha h_\alpha$, each summand extended by zero off $\operatorname{supp}\rho_\alpha$; local finiteness makes $h$ a well-defined smooth section of $\mathcal{H}(E)$.

> [!note]- Derivation
> For each $\alpha$, the product $\rho_\alpha h_\alpha$ is a priori defined on $U_\alpha$, but $\rho_\alpha$ vanishes on the open set $U_\alpha \setminus \operatorname{supp}\rho_\alpha$, so $\rho_\alpha h_\alpha$ extends by zero to a smooth section of $\mathcal{H}(E)$ over all of $M$ (it is smooth on $U_\alpha$, identically zero on the open set $M \setminus \operatorname{supp}\rho_\alpha$, and these two open sets cover $M$; on their overlap both descriptions give the same values, so the two agree and the glued section is smooth). Define
> $$h := \sum_{\alpha \in A} \rho_\alpha h_\alpha.$$
> By local finiteness of $\{\operatorname{supp}\rho_\alpha\}$, every point $m$ has a neighbourhood on which all but finitely many summands vanish identically, so the sum is a *finite* sum of smooth sections near each point, hence a smooth section of $\mathcal{H}(E)$.

**Step 4: $h$ is fibrewise sesquilinear and Hermitian-symmetric.**

Because the weights are real scalars, the pointwise fibre form $h_m$ inherits complex-linearity in the first slot, conjugate-linearity in the second, and Hermitian symmetry from the $h_{\alpha, m}$.

> [!note]- Derivation
> Fix $m \in M$ and let $A_m := \{\alpha : \rho_\alpha(m) > 0\}$, a finite non-empty set; note $m \in \operatorname{supp}\rho_\alpha \subseteq U_\alpha$ for each $\alpha \in A_m$, so $h_{\alpha, m}$ is defined there. Then $h_m = \sum_{\alpha \in A_m} \rho_\alpha(m)\, h_{\alpha, m}$ with each $\rho_\alpha(m) \in \mathbb{R}_{>0}$.
> - *Additivity and complex-linearity in the first slot.* For $u, u', v \in E_m$ and $\lambda \in \mathbb{C}$,
> $$h_m(\lambda u + u', v) = \sum_{\alpha \in A_m} \rho_\alpha(m)\, h_{\alpha, m}(\lambda u + u', v) = \sum_{\alpha \in A_m} \rho_\alpha(m)\big(\lambda\, h_{\alpha, m}(u, v) + h_{\alpha, m}(u', v)\big) = \lambda\, h_m(u, v) + h_m(u', v),$$
> using complex-linearity of each $h_{\alpha, m}$ in its first slot (Step 1) and that $\lambda$ commutes past the *real* scalars $\rho_\alpha(m)$.
> - *Conjugate-linearity in the second slot.* Identically, with $h_{\alpha, m}(u, \lambda v + v') = \overline{\lambda}\, h_{\alpha, m}(u, v) + h_{\alpha, m}(u, v')$, one gets $h_m(u, \lambda v + v') = \overline{\lambda}\, h_m(u, v) + h_m(u, v')$.
> - *Hermitian symmetry.* Since each $\rho_\alpha(m)$ is real, $\overline{\rho_\alpha(m)} = \rho_\alpha(m)$, so
> $$\overline{h_m(u, v)} = \sum_{\alpha \in A_m} \rho_\alpha(m)\, \overline{h_{\alpha, m}(u, v)} = \sum_{\alpha \in A_m} \rho_\alpha(m)\, h_{\alpha, m}(v, u) = h_m(v, u) \qquad \text{(conjugate through the real weights; Hermitian symmetry of each } h_{\alpha,m}\text{).}$$
> Hence $h_m$ is a Hermitian form on $(E_m, I_m)$; equivalently, $h$ is a section of the sub-bundle $\mathcal{H}(E)$.

**Step 5: $h$ is positive definite.**

At every point, $h_m$ is a convex combination of positive-definite Hermitian forms with at least one strictly positive weight, hence positive definite.

> [!note]- Derivation
> Fix $m \in M$ and $v \in E_m$ with $v \neq 0$. With $A_m$ as in Step 4,
> $$h_m(v, v) = \sum_{\alpha \in A_m} \rho_\alpha(m)\, h_{\alpha, m}(v, v).$$
> For each $\alpha \in A_m$ we have $\rho_\alpha(m) > 0$ and, by Step 1 (positive definiteness of $h_\alpha$ and $v \neq 0$), $h_{\alpha, m}(v, v) > 0$; hence every term is strictly positive. The index set $A_m$ is non-empty: if it were empty then $\sum_{\alpha} \rho_\alpha(m) = 0$, contradicting property (3) of the partition of unity, $\sum_\alpha \rho_\alpha(m) = 1$. A sum of strictly positive terms over a non-empty finite set is strictly positive, so
> $$h_m(v, v) > 0.$$
> By Hermitian symmetry (Step 4), $h_m(v, v) = \overline{h_m(v, v)}$ is real, so this inequality is meaningful. Therefore $h_m$ is positive definite for every $m$, and $h$ is a section of the open cone $\mathcal{H}^+(E)$.

> [!note]- Complete formal solution
> **Claim.** Every complex vector bundle $(E, I) \to M$ over a smooth manifold admits a Hermitian structure.
>
> Because $(E, I)$ is a complex vector bundle, choose an open cover $\{U_\alpha\}_{\alpha \in A}$ of $M$ with complex-linear local trivialisations $\psi_\alpha : E|_{U_\alpha} \to U_\alpha \times \mathbb{C}^k$. Writing $\langle z, w\rangle_{\mathrm{std}} = \sum_{j=1}^k z_j \overline{w_j}$ for the standard Hermitian product on $\mathbb{C}^k$, define on $E|_{U_\alpha}$
> $$h_{\alpha, m}(u, v) := \langle \psi_{\alpha, m}(u), \psi_{\alpha, m}(v)\rangle_{\mathrm{std}} \qquad (m \in U_\alpha,\ u, v \in E_m).$$
> As $\psi_{\alpha, m}$ is a complex-linear isomorphism and $\langle\cdot,\cdot\rangle_{\mathrm{std}}$ is a Hermitian inner product, $h_{\alpha, m}$ is complex-linear in its first slot, conjugate-linear in its second, Hermitian-symmetric, and positive definite; and $h_\alpha$ depends smoothly on $m$ because in a smooth local frame it is a finite sum of products of smooth functions.
>
> By [[Thm - Existence of Smooth Partitions of Unity|the existence of smooth partitions of unity]] there are smooth $\rho_\alpha : M \to [0, 1]$ with $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$, the supports locally finite, and $\sum_\alpha \rho_\alpha \equiv 1$. Each $\rho_\alpha h_\alpha$ extends by zero to a smooth section of $\mathcal{H}(E)$ over $M$, and by local finiteness
> $$h := \sum_{\alpha \in A} \rho_\alpha h_\alpha$$
> is a well-defined smooth section of $\mathcal{H}(E)$.
>
> Fix $m$ and set $A_m = \{\alpha : \rho_\alpha(m) > 0\}$ (finite, non-empty because $\sum_\alpha \rho_\alpha(m) = 1$). Since the weights $\rho_\alpha(m)$ are real, $h_m = \sum_{\alpha \in A_m} \rho_\alpha(m) h_{\alpha, m}$ is complex-linear in its first slot, conjugate-linear in its second, and Hermitian-symmetric (real weights commute with scalars and with complex conjugation). For $v \neq 0$, each term $\rho_\alpha(m) h_{\alpha, m}(v, v)$ is strictly positive, so $h_m(v, v) > 0$; thus $h_m$ is positive definite.
>
> Therefore $h$ is a smooth positive-definite Hermitian form on the fibres of $E$: a Hermitian structure. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> One is tempted to skip the partition of unity and instead pick a *single* global smooth section $s_0 \in \Gamma(E)$ and set $h(u, v) := (\text{something built from } s_0)$, or to average with arbitrary smooth weights $c_\alpha$ that merely sum to $1$ without being non-negative. Both fail. A single section cannot see the whole fibre. And if the weights are allowed to be negative, the fibre form $\sum_\alpha c_\alpha(m) h_{\alpha, m}$ need not be positive definite: for instance $2 h_1 - 1 \cdot h_2$ has determinant that can be negative even though $h_1, h_2$ are inner products (take $h_2$ much larger than $h_1$ in some direction). Positivity is a *convex*, not a linear, condition; only *non-negative* weights summing to one — a genuine partition of unity — preserve it. The extra condition that rescues a general weighted sum is exactly non-negativity of the weights together with at least one being positive at each point.

> [!note]- Independent sanity check: the line-bundle case
> Take $E = L$ a complex line bundle ($k = 1$). A Hermitian structure is a smooth choice of squared-norm $\|\cdot\|^2 : L \to \mathbb{R}_{\geq 0}$, positive off the zero section. Over each $U_\alpha$ pick a nowhere-zero smooth section $\sigma_\alpha$ (a local frame) and declare $\|\sigma_\alpha\|_\alpha \equiv 1$, i.e. $h_\alpha(z \sigma_\alpha, w\sigma_\alpha) = z\overline{w}$. On overlaps $\sigma_\beta = g_{\beta\alpha}\sigma_\alpha$ with $g_{\beta\alpha} : U_\alpha \cap U_\beta \to \mathbb{C}^\times$ nowhere zero, so $h_\alpha$ and $h_\beta$ differ by the positive factor $|g_{\beta\alpha}|^2$. The blended metric $h = \sum_\alpha \rho_\alpha h_\alpha$ gives $\|\sigma_\alpha(m)\|^2 = \sum_\beta \rho_\beta(m)|g_{\alpha\beta}(m)|^2 > 0$, a smooth positive function — exactly a Hermitian metric on $L$. This matches the general construction and shows concretely why non-negativity of the $\rho_\beta$ is what keeps the norm positive.

---

# Key Takeaways

**The universal recipe for a globally defined, pointwise-convex geometric structure is: pull back the model on each trivialising set, then blend with a partition of unity.** The reusable principle is that any fibrewise structure whose admissible values form a *convex* set — Riemannian metrics, Hermitian metrics, fibrewise volume forms up to sign, torsion-free connections, compatible almost-complex-with-metric data — exists globally on any smooth (hence paracompact) manifold as soon as it exists locally, because local triviality supplies the local pieces and a subordinate partition of unity averages them without leaving the convex set. The trigger condition to recognise is the conjunction "the structure I want is locally available *and* its admissible values are closed under convex combination." When both hold, no obstruction theory is needed; the answer is immediate. The transferable diagnostic when a gluing construction *fails* is to ask whether the admissible values are actually convex — if they are not (for instance, the set of *flat* metrics, or *integrable* complex structures, or nowhere-vanishing sections), the partition-of-unity blend can leave the admissible set and existence becomes a genuine topological question.

**Non-negativity of the weights, not merely their summing to one, is what preserves positivity.** It is worth isolating why the construction demands a partition of *unity* with values in $[0, 1]$ rather than any smooth resolution $\sum_\alpha c_\alpha = 1$. Positive definiteness is preserved by convex combinations because a convex combination of positive numbers, with at least one positive coefficient, is positive; it is *not* preserved by arbitrary affine combinations. The same remark explains why this technique produces metrics (a convex condition) but cannot produce, say, a global *flat* connection or a global nowhere-zero section by the same move: those live in non-convex or topologically obstructed sets. Whenever you see a partition of unity used to build a metric or inner product, the mental note to store is "the weights are non-negative precisely so that positivity travels through the average."

**The result is the existence half of the reduction $GL_k(\mathbb{C}) \rightsquigarrow U(k)$, and its convexity gives uniqueness up to homotopy — the fact chapter VI relies on.** Choosing a Hermitian structure on $(E, I)$ is the same as reducing the structure group of $E$ from $GL_k(\mathbb{C})$ to the unitary group $U(k)$ (this is proved on [[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group|the reductions theorem]], where Hermitian structures are put in bijection with $U(k)$-structures inside the complex frame bundle); the present exercise supplies the *existence* of such a reduction, so that unitary frames, and hence unitary connections, are always available. Moreover the *set* of Hermitian structures on a fixed $(E, I)$ is itself convex: if $h_0, h_1$ are two Hermitian structures, then $h_t := (1 - t) h_0 + t\, h_1$ is a Hermitian structure for every $t \in [0, 1]$, by the very convexity argument of Step 5 applied with the two weights $1 - t, t$. Hence the space of Hermitian structures is non-empty and convex, therefore contractible, and any two are joined by a canonical smooth path $h_t$. This is exactly the input chapter VI uses to prove that the Chern classes of a complex bundle do not depend on the chosen Hermitian structure: the two unitary frame bundles are joined by a bundle over $M \times [0, 1]$, and the homotopy invariance of characteristic classes finishes the argument. The companion exercise [[Ex - Complex Structures Correspond to GL(k,C)-Structures|complex structures as $GL_k(\mathbb{C})$-structures]] establishes the parallel reduction for the complex structure itself.
