---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - First Chern Class via the Classifying Map"
  - "Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles"
  - "Def - Complex Vector Bundle and Hermitian Structure"
  - "Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group"
  - "Def - Principal G-Bundle"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M$ be a compact smooth manifold and $L \to M$ a complex line bundle. The topological first Chern class of $L$ is defined by first choosing a Hermitian scalar product $h$ on $L$ — equivalently a reduction of the frame bundle $\operatorname{Fr}(L)$ to the subgroup $U(1) \subset GL_1(\mathbb{C})$, giving a principal $U(1)$-bundle $P_h \subset \operatorname{Fr}(L)$ — and then setting $c_1^{\mathrm{top}}(L) := c_1^{\mathrm{top}}(P_h)$, where $c_1^{\mathrm{top}}(P_h) \in H^2_{\mathrm{dR}}(M)$ is the Chern class of the principal $U(1)$-bundle $P_h$ obtained from its classifying map.

$$\text{Show that } c_1^{\mathrm{top}}(L) \text{ is independent of the chosen Hermitian scalar product } h.$$

Concretely: given two Hermitian scalar products $h_0$ and $h_1$ on $L$, with associated $U(1)$-reductions $P_{h_0}$ and $P_{h_1}$, prove that $P_{h_0} \cong P_{h_1}$ as principal $U(1)$-bundles over $M$, and deduce $c_1^{\mathrm{top}}(P_{h_0}) = c_1^{\mathrm{top}}(P_{h_1})$.

The intended route: the Hermitian scalar products on $L$ form a convex set, so $h_t := (1-t)h_0 + t\,h_1$ is again a Hermitian scalar product for every $t \in [0,1]$. This one-parameter family assembles into a single Hermitian scalar product $H$ on the pulled-back bundle $\operatorname{pr}^*L$ over $M \times [0,1]$, where $\operatorname{pr}\colon M \times [0,1] \to M$ is the projection. The $U(1)$-reduction $P_H$ of $\operatorname{pr}^*L$ is a principal $U(1)$-bundle over $M \times [0,1]$ whose restriction to $M \times \{s\}$ is exactly $P_{h_s}$. Because a principal bundle over $M \times [0,1]$ restricts isomorphically to its two ends, $P_{h_0} \cong P_{h_1}$; and since $c_1^{\mathrm{top}}$ is defined on isomorphism classes, the two Chern classes coincide.

This is the exercise Haydys records as Exercise 76 (source item A-X2.4.1, p. 25), immediately after his Definition 75 of the first Chern class.

**Recall:**

The objects in play are a complex line bundle with a Hermitian scalar product, the principal $U(1)$-bundle it reduces to, the first Chern class of a $U(1)$-bundle, and the theorem that a bundle over a cylinder $M \times [0,1]$ has isomorphic ends.

![[Def - Complex Vector Bundle and Hermitian Structure#The Definition]]

A **Hermitian scalar product** (or Hermitian structure) on a complex vector bundle $L \to M$ is a smooth choice, fibrewise, of a Hermitian inner product $h_m$ on $L_m$: a map $h_m\colon L_m \times L_m \to \mathbb{C}$ that is complex-linear in the second argument, satisfies $h_m(v,w) = \overline{h_m(w,v)}$ (conjugate symmetry), and is positive definite, $h_m(v,v) > 0$ for every nonzero $v \in L_m$; smoothness means that $m \mapsto h_m(s(m), t(m))$ is a smooth function for all smooth sections $s, t$.

![[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group#Statement]]

For a complex vector bundle $L$ of complex rank $m$, the theorem above provides a natural bijection between Hermitian structures on $L$ and reductions of the structure group of $\operatorname{Fr}(L)$ from $GL_m(\mathbb{C})$ to the unitary group $U(m)$. For a **line** bundle ($m = 1$) this is a reduction from $GL_1(\mathbb{C}) = \mathbb{C}^\times$ to $U(1)$: the principal $U(1)$-bundle $P_h \subset \operatorname{Fr}(L)$ is the bundle of $h$-unitary frames, whose fibre over $m$ is the set of $h_m$-unit vectors $\{v \in L_m : h_m(v,v) = 1\}$, a circle, with $U(1) = \{\lambda \in \mathbb{C} : |\lambda| = 1\}$ acting by scalar multiplication.

![[Def - First Chern Class via the Classifying Map#The Definition]]

For a principal $U(1)$-bundle $P \to M$ over a compact manifold, the **first Chern class** is $c_1^{\mathrm{top}}(P) := -f^*[\omega_N] \in H^2_{\mathrm{dR}}(M)$, where $f\colon M \to \mathbb{CP}^N$ is any classifying map (so that $P \cong f^*(S^{2N+1} \to \mathbb{CP}^N)$) and $[\omega_N] \in H^2_{\mathrm{dR}}(\mathbb{CP}^N)$ is the standard generator. This class is well defined precisely because it is an invariant of the isomorphism class of $P$: isomorphic principal $U(1)$-bundles have classifying maps that are homotopic, and homotopic maps induce the same map on de Rham cohomology, so $-f^*[\omega_N]$ does not change.

![[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles#Statement]]

The single fact from that theorem we use is part (a): **if $P \to M \times [0,1]$ is a principal $G$-bundle over a manifold $M$, then $P \cong \operatorname{pr}^*\!\big(P|_{M \times \{0\}}\big)$; in particular its restrictions to the two ends $M \times \{0\}$ and $M \times \{1\}$ are isomorphic principal $G$-bundles over $M$.** Here $\operatorname{pr}\colon M \times [0,1] \to M$ is the projection.

---

# Convergent Strategy

**Problem class.** This is a *well-definedness* problem: a construction ($L \mapsto c_1^{\mathrm{top}}(L)$) is made by way of an auxiliary choice (the Hermitian structure $h$), and we must show the output does not depend on the choice. Such problems are always solved by connecting any two choices and showing the output is constant along the connection. The characteristic feature here is that the space of choices is not merely connected but *convex*, which makes the connecting path immediate and canonical.

**Assumption pattern.** Two structural facts are being used, and recognising which fact each hypothesis feeds is the whole game. First, the space of Hermitian scalar products on a fixed complex vector bundle is a *convex subset* of the vector space of Hermitian forms — a positive-definite form stays positive definite under convex combination. This turns "connect $h_0$ to $h_1$" into the one-line formula $h_t = (1-t)h_0 + t\,h_1$. Second, the invariant $c_1^{\mathrm{top}}$ was constructed as a function of the *isomorphism class* of the underlying $U(1)$-bundle; so once we produce an isomorphism $P_{h_0} \cong P_{h_1}$, equality of Chern classes is automatic and needs no further computation.

**Theorem routing.** The route has three links. The convex path $h_t$ is repackaged as a *single* Hermitian structure $H$ on the pulled-back line bundle $\operatorname{pr}^*L$ over the cylinder $M \times [0,1]$. Its $U(1)$-reduction, produced by **[[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group|the reduction theorem]]**, is a principal $U(1)$-bundle $P_H$ over $M \times [0,1]$ that restricts to $P_{h_s}$ at each level $M \times \{s\}$. Then **[[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|the cylinder theorem]]**, part (a), says a principal bundle over $M \times [0,1]$ has isomorphic ends, delivering $P_{h_0} \cong P_{h_1}$. Finally **[[Def - First Chern Class via the Classifying Map|the definition of $c_1^{\mathrm{top}}$]]**, being an isomorphism invariant, converts that bundle isomorphism into the desired equality of classes.

**Key decision point.** The one non-obvious move is to *stop thinking of a one-parameter family of bundles over $M$ and instead assemble a single bundle over $M \times [0,1]$*. A family $\{P_{h_t}\}_{t}$ of bundles over $M$ is exactly the same data as one bundle $P_H$ over $M \times [0,1]$, and only in the second form is the powerful cylinder theorem available. This is the recurring idiom "a homotopy of geometric objects is a single object over a cylinder", and identifying it is what reduces a potential curvature computation to a purely topological triviality. Everything else — convexity, the ends being $P_{h_0}$ and $P_{h_1}$ — is bookkeeping once this reframing is made.

---

# Legal Operations Used

This solution deploys the following operations (named descriptively; they correspond to the operations catalogued on the [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles|chapter topic page]]'s Legal Operations, whose numbering the topic page fixes):

1. **Connect two auxiliary choices by a convex path.** Given two Hermitian structures $h_0, h_1$ on the same bundle, form the affine segment $h_t = (1-t)h_0 + t\,h_1$; verify it stays inside the space of Hermitian structures by checking positive definiteness clause by clause.

2. **Repackage a one-parameter family as a single object over a cylinder.** A smooth family of Hermitian structures $\{h_t\}_{t \in [0,1]}$ on $L \to M$ is the same datum as a single Hermitian structure $H$ on $\operatorname{pr}^*L \to M \times [0,1]$; make the identification explicit fibre by fibre.

3. **Pass from a Hermitian structure to its $U(1)$-reduction.** Apply the reduction theorem to $H$ to obtain a principal $U(1)$-bundle $P_H \subset \operatorname{Fr}(\operatorname{pr}^*L)$ over $M \times [0,1]$.

4. **Restrict a bundle to a submanifold and identify the restriction.** Restrict $P_H$ to $M \times \{s\}$ and recognise it, through the canonical identification $\operatorname{pr}^*L|_{M \times \{s\}} \cong L$, as the reduction $P_{h_s}$.

5. **Invoke the cylinder theorem to identify the two ends.** A principal $G$-bundle over $M \times [0,1]$ has isomorphic restrictions to $M \times \{0\}$ and $M \times \{1\}$.

6. **Transport a bundle isomorphism through an isomorphism-invariant.** Because $c_1^{\mathrm{top}}$ is a function of the isomorphism class of the $U(1)$-bundle, an isomorphism $P_{h_0} \cong P_{h_1}$ yields the equality $c_1^{\mathrm{top}}(P_{h_0}) = c_1^{\mathrm{top}}(P_{h_1})$.

---

# Hints

> [!note]- Hint 1
> You are asked to show a construction that starts from a *choice* (the Hermitian structure $h$) does not actually depend on that choice. The universal method: take any two choices $h_0, h_1$ and connect them by a path. What is the simplest possible path between two positive-definite Hermitian forms, and why does it stay positive definite?

> [!note]- Hint 2
> Set $h_t = (1-t)h_0 + t\,h_1$. Now resist the temptation to compute anything about $c_1^{\mathrm{top}}(P_{h_t})$ directly (that would drag in curvature or classifying maps at every $t$). Instead, notice that the whole family $\{h_t\}$ is a *single* Hermitian structure on one bundle sitting over $M \times [0,1]$. Which bundle, and which theorem about bundles over a product with an interval is now available?

> [!note]- Hint 3
> Let $\operatorname{pr}\colon M \times [0,1] \to M$ be the projection and put $H_{(m,t)} := h_t$ acting on the fibre $(\operatorname{pr}^*L)_{(m,t)} = L_m$. This is a Hermitian structure on $\operatorname{pr}^*L$, so it has a $U(1)$-reduction $P_H$, a principal $U(1)$-bundle over $M \times [0,1]$. Check that restricting $P_H$ to $M \times \{0\}$ gives $P_{h_0}$ and to $M \times \{1\}$ gives $P_{h_1}$.

> [!note]- Hint 4
> By part (a) of the theorem that a bundle over $M \times [0,1]$ is the pullback of its restriction to $M \times \{0\}$, the two ends $P_H|_{M \times \{0\}} = P_{h_0}$ and $P_H|_{M \times \{1\}} = P_{h_1}$ are isomorphic principal $U(1)$-bundles. The first Chern class was *defined* on isomorphism classes of $U(1)$-bundles — so what is the final line?

---

# Solution

The argument never computes a Chern class. It converts the choice-dependence question into a statement about a bundle over the cylinder $M \times [0,1]$, where the only fact needed is that such a bundle has isomorphic ends. Convexity of the space of Hermitian structures supplies the interpolating family for free; assembling that family over the cylinder makes the cylinder theorem applicable; and the isomorphism invariance built into the definition of $c_1^{\mathrm{top}}$ finishes the job.

**Step 1: The Hermitian scalar products on $L$ form a convex set, so $h_t = (1-t)h_0 + t\,h_1$ is a Hermitian scalar product for every $t \in [0,1]$.**

Two Hermitian structures $h_0, h_1$ interpolate through the affine segment $h_t$, which stays positive definite because a nonnegative combination of positive quantities, with positive total weight, is positive.

> [!note]- Derivation
> Fix a point $m \in M$; the fibre $L_m$ is a one-dimensional complex vector space and $h_{0,m}, h_{1,m}$ are Hermitian inner products on it. For $t \in [0,1]$ define
> $$h_{t,m}(v,w) := (1-t)\,h_{0,m}(v,w) + t\,h_{1,m}(v,w), \qquad v, w \in L_m.$$
> We verify clause by clause that $h_{t,m}$ is a Hermitian inner product.
> - **Sesquilinearity.** For fixed $v$, the map $w \mapsto h_{t,m}(v,w) = (1-t)h_{0,m}(v,w) + t\,h_{1,m}(v,w)$ is a real-coefficient linear combination of the complex-linear maps $w \mapsto h_{0,m}(v,w)$ and $w \mapsto h_{1,m}(v,w)$, hence complex-linear (a linear combination of complex-linear maps is complex-linear). For fixed $w$, the map $v \mapsto h_{t,m}(v,w) = (1-t)h_{0,m}(v,w) + t\,h_{1,m}(v,w)$ is a real-coefficient linear combination of the conjugate-linear maps $v \mapsto h_{0,m}(v,w)$ and $v \mapsto h_{1,m}(v,w)$, hence conjugate-linear (a linear combination of conjugate-linear maps is conjugate-linear).
> - **Conjugate symmetry.** Using $h_{0,m}(v,w) = \overline{h_{0,m}(w,v)}$ and $h_{1,m}(v,w) = \overline{h_{1,m}(w,v)}$, and that $(1-t), t$ are real,
> $$h_{t,m}(v,w) = (1-t)\overline{h_{0,m}(w,v)} + t\,\overline{h_{1,m}(w,v)} = \overline{(1-t)h_{0,m}(w,v) + t\,h_{1,m}(w,v)} = \overline{h_{t,m}(w,v)} \qquad \text{(real scalars pass through the conjugation).}$$
> - **Positive definiteness.** Let $v \in L_m$ with $v \neq 0$. Then $h_{0,m}(v,v) > 0$ and $h_{1,m}(v,v) > 0$ (positive definiteness of $h_0, h_1$). Since $1 - t \geq 0$, $t \geq 0$, and $(1-t) + t = 1 > 0$, at least one coefficient is strictly positive, so
> $$h_{t,m}(v,v) = (1-t)\,h_{0,m}(v,v) + t\,h_{1,m}(v,v) > 0 \qquad \text{(a nonnegative combination, with positive total weight, of two strictly positive numbers).}$$
> Thus $h_{t,m}$ is a Hermitian inner product on $L_m$ for each $t$. It depends smoothly on $(m,t)$: for smooth sections $s, t'$ of $L$ the function $(m,t) \mapsto h_{t,m}(s(m), t'(m)) = (1-t)\,h_{0,m}(s(m),t'(m)) + t\,h_{1,m}(s(m),t'(m))$ is smooth, being affine in $t$ with smooth-in-$m$ coefficients (smoothness of $h_0, h_1$). Hence $h_t$ is a Hermitian scalar product on $L$ for every $t \in [0,1]$.

**Step 2: The family $\{h_t\}$ is a single Hermitian scalar product $H$ on the pulled-back line bundle $\operatorname{pr}^*L$ over $M \times [0,1]$.**

Let $\operatorname{pr}\colon M \times [0,1] \to M$ be the projection. The pullback $\operatorname{pr}^*L$ has fibre $L_m$ over $(m,t)$, and putting $H$ equal to $h_t$ on that fibre defines a Hermitian scalar product on $\operatorname{pr}^*L$.

> [!note]- Derivation
> The pulled-back complex line bundle $\operatorname{pr}^*L \to M \times [0,1]$ has, by the construction of the [[Def - Operations on Vector Bundles and Pull-Back Bundles|pull-back bundle]], total space
> $$\operatorname{pr}^*L = \{\, ((m,t), \ell) \in (M \times [0,1]) \times L : \ell \in L_{\operatorname{pr}(m,t)} = L_m \,\},$$
> so its fibre over $(m,t)$ is canonically identified with $L_m$, and the bundle projection sends $((m,t),\ell)$ to $(m,t)$. Define, for $\ell, \ell' \in (\operatorname{pr}^*L)_{(m,t)} = L_m$,
> $$H_{(m,t)}(\ell, \ell') := h_{t,m}(\ell, \ell').$$
> By Step 1, $h_{t,m}$ is a Hermitian inner product on $L_m$ for each $(m,t)$, so $H_{(m,t)}$ is a Hermitian inner product on the fibre $(\operatorname{pr}^*L)_{(m,t)}$. Smoothness of $H$ on $M \times [0,1]$ follows from the smoothness statement in Step 1 together with the smoothness of the pullback: a local frame of $\operatorname{pr}^*L$ near $(m_0,t_0)$ is $\operatorname{pr}^*e$ for a local frame $e$ of $L$ near $m_0$, and $H(\operatorname{pr}^*e, \operatorname{pr}^*e)(m,t) = h_{t,m}(e(m),e(m))$ is smooth in $(m,t)$ by Step 1. Hence $H$ is a Hermitian scalar product on $\operatorname{pr}^*L$.

**Step 3: The $U(1)$-reduction $P_H$ of $\operatorname{pr}^*L$ restricts to $P_{h_0}$ over $M \times \{0\}$ and to $P_{h_1}$ over $M \times \{1\}$.**

By the reduction theorem, $H$ determines a principal $U(1)$-bundle $P_H \subset \operatorname{Fr}(\operatorname{pr}^*L)$ over $M \times [0,1]$; its restriction to the level $M \times \{s\}$ is the reduction $P_{h_s}$ of $L$.

> [!note]- Derivation
> By **[[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group|the reduction theorem]]** — *for a complex vector bundle, Hermitian structures correspond bijectively to $U(m)$-reductions of the frame bundle* — the Hermitian structure $H$ on the complex line bundle $\operatorname{pr}^*L$ gives a $U(1)$-reduction
> $$P_H := \{\, \varphi \in \operatorname{Fr}(\operatorname{pr}^*L) : \varphi \text{ is an } H\text{-unitary frame} \,\} \subset \operatorname{Fr}(\operatorname{pr}^*L),$$
> a principal $U(1)$-bundle over $M \times [0,1]$. Concretely, for a line bundle a frame at $(m,t)$ is a nonzero vector of the fibre, and $P_H$ is the circle bundle of $H$-unit vectors,
> $$\big(P_H\big)_{(m,t)} = \{\, \ell \in (\operatorname{pr}^*L)_{(m,t)} = L_m : H_{(m,t)}(\ell,\ell) = 1 \,\}.$$
> Now restrict to a level $s \in \{0,1\}$. The inclusion $\iota_s\colon M \to M \times [0,1]$, $\iota_s(m) = (m,s)$, satisfies $\operatorname{pr} \circ \iota_s = \operatorname{id}_M$, so $\iota_s^*(\operatorname{pr}^*L) = (\operatorname{pr}\circ\iota_s)^*L = L$ canonically, with the fibre of $\operatorname{pr}^*L$ over $(m,s)$ identified with $L_m$ as in Step 2. Under this identification $H_{(m,s)} = h_{s,m}$ (by the definition of $H$ in Step 2). Therefore the fibre of $P_H$ over $(m,s)$ is
> $$\{\, \ell \in L_m : H_{(m,s)}(\ell,\ell) = 1 \,\} = \{\, \ell \in L_m : h_{s,m}(\ell,\ell) = 1 \,\} = \big(P_{h_s}\big)_m,$$
> the $h_s$-unit circle in $L_m$, which is precisely the fibre of the reduction $P_{h_s}$ of $L$. Since this identification is the restriction of the $U(1)$-equivariant identification of frame bundles, it is an isomorphism of principal $U(1)$-bundles:
> $$P_H\big|_{M \times \{0\}} \cong P_{h_0}, \qquad P_H\big|_{M \times \{1\}} \cong P_{h_1}.$$

**Step 4: The two ends are isomorphic, so the Chern classes agree.**

The cylinder theorem gives $P_{h_0} \cong P_{h_1}$; isomorphism invariance of $c_1^{\mathrm{top}}$ then yields $c_1^{\mathrm{top}}(P_{h_0}) = c_1^{\mathrm{top}}(P_{h_1})$.

> [!note]- Derivation
> Apply part (a) of **[[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|the cylinder theorem]]** to the principal $U(1)$-bundle $P_H \to M \times [0,1]$: *a principal $G$-bundle over $M \times [0,1]$ has isomorphic restrictions to $M \times \{0\}$ and $M \times \{1\}$*. With $G = U(1)$ this gives
> $$P_H\big|_{M \times \{0\}} \cong P_H\big|_{M \times \{1\}}.$$
> Combining with the two identifications of Step 3,
> $$P_{h_0} \cong P_H\big|_{M \times \{0\}} \cong P_H\big|_{M \times \{1\}} \cong P_{h_1} \qquad \text{(Step 3, cylinder theorem, Step 3).}$$
> Finally, $c_1^{\mathrm{top}}$ was defined on isomorphism classes of principal $U(1)$-bundles: by **[[Def - First Chern Class via the Classifying Map|the definition of the first Chern class]]**, $c_1^{\mathrm{top}}(P) = -f_P^*[\omega_N]$ for a classifying map $f_P$, and isomorphic bundles have homotopic classifying maps, which induce equal maps on $H^2_{\mathrm{dR}}$. Hence from $P_{h_0} \cong P_{h_1}$,
> $$c_1^{\mathrm{top}}(L) \overset{h_0}{=} c_1^{\mathrm{top}}(P_{h_0}) = c_1^{\mathrm{top}}(P_{h_1}) \overset{h_1}{=} c_1^{\mathrm{top}}(L).$$
> Since $h_0, h_1$ were arbitrary Hermitian scalar products on $L$, the class $c_1^{\mathrm{top}}(L)$ is the same whichever Hermitian structure is used to compute it.

> [!note]- Complete formal solution
> **Claim.** Let $M$ be a compact manifold and $L \to M$ a complex line bundle. The first Chern class $c_1^{\mathrm{top}}(L) := c_1^{\mathrm{top}}(P_h)$, defined by choosing a Hermitian scalar product $h$ on $L$ and passing to its $U(1)$-reduction $P_h$, is independent of $h$.
>
> Let $h_0, h_1$ be two Hermitian scalar products on $L$. For $t \in [0,1]$ set $h_t := (1-t)h_0 + t\,h_1$. Fibrewise and pointwise this is sesquilinear and conjugate-symmetric (real linear combination of such forms), and positive definite: for $v \neq 0$, $h_t(v,v) = (1-t)h_0(v,v) + t\,h_1(v,v) > 0$ since $h_0(v,v), h_1(v,v) > 0$ and the nonnegative weights $1-t, t$ sum to $1$. Smoothness in $(m,t)$ is inherited from $h_0, h_1$, being affine in $t$. So each $h_t$ is a Hermitian scalar product on $L$.
>
> Let $\operatorname{pr}\colon M \times [0,1] \to M$ be the projection and $\operatorname{pr}^*L \to M \times [0,1]$ the pulled-back line bundle, whose fibre over $(m,t)$ is $L_m$. Define a Hermitian scalar product $H$ on $\operatorname{pr}^*L$ by $H_{(m,t)} := h_{t,m}$ on the fibre $L_m$; it is smooth by the previous paragraph. By the reduction theorem, $H$ determines a principal $U(1)$-bundle $P_H \subset \operatorname{Fr}(\operatorname{pr}^*L)$ over $M \times [0,1]$, the circle bundle of $H$-unit vectors. For $s \in \{0,1\}$, the inclusion $\iota_s(m) = (m,s)$ satisfies $\operatorname{pr}\circ\iota_s = \operatorname{id}_M$, so $\iota_s^*(\operatorname{pr}^*L) = L$ and $H|_{M \times \{s\}} = h_s$; hence the fibre of $P_H$ over $(m,s)$ is the $h_s$-unit circle in $L_m$, giving $P_H|_{M \times \{s\}} \cong P_{h_s}$.
>
> By part (a) of the cylinder theorem, the principal $U(1)$-bundle $P_H$ over $M \times [0,1]$ has isomorphic ends: $P_H|_{M \times \{0\}} \cong P_H|_{M \times \{1\}}$. Composing the identifications, $P_{h_0} \cong P_{h_1}$.
>
> The first Chern class of a principal $U(1)$-bundle is an invariant of its isomorphism class (isomorphic bundles have homotopic classifying maps, and homotopic maps induce equal maps on $H^2_{\mathrm{dR}}$). Therefore $c_1^{\mathrm{top}}(P_{h_0}) = c_1^{\mathrm{top}}(P_{h_1})$, that is, the value $c_1^{\mathrm{top}}(L)$ does not depend on the chosen Hermitian scalar product. $\blacksquare$

> [!warning] Illegal but tempting route: "any two Hermitian structures are equal after a scaling, so nothing to prove"
> It is true that on a **line** bundle any two Hermitian scalar products satisfy $h_1 = \rho\, h_0$ for a smooth positive function $\rho\colon M \to \mathbb{R}_{>0}$ (both are determined fibrewise by a single positive real number). One might try to conclude directly that $P_{h_0} = P_{h_1}$. This is false: the unit circles $\{h_0(v,v) = 1\}$ and $\{h_1(v,v) = 1\} = \{h_0(v,v) = \rho^{-1}\}$ are *different* subsets of $L_m$, so $P_{h_0}$ and $P_{h_1}$ are genuinely different subbundles of $\operatorname{Fr}(L)$; they are only *isomorphic*, via the fibrewise rescaling $v \mapsto \rho^{1/2} v$. The scaling observation does give a second, direct proof — the bundle map $v \mapsto \sqrt{\rho(m)}\, v$ restricts to a $U(1)$-equivariant diffeomorphism $P_{h_1} \to P_{h_0}$ — but it is special to line bundles, whereas the cylinder argument above works verbatim for Hermitian structures on a complex bundle of any rank (where "$h_1 = \rho h_0$" is false and the positive automorphism relating them is $h_0$-self-adjoint and no longer scalar). The lesson is to prove *isomorphism*, not *equality*, of the reductions.

---

# Key Takeaways

**A construction that depends on a choice is choice-independent as soon as the space of choices is connected and the output is a homotopy invariant; convexity is the strongest possible form of connectedness and makes the connecting path free.** The reusable principle is a two-part test. First, identify the *space of auxiliary choices* — here the Hermitian scalar products on $L$ — and show it is path-connected; when that space is a convex subset of a vector space (positive-definite forms, Riemannian metrics, connections, compatible almost-complex structures tamed by a fixed symplectic form), the straight-line homotopy $x_t = (1-t)x_0 + t\,x_1$ does the connecting with no effort, and one only checks the defining inequality is preserved. Second, confirm the *output* is invariant under the deformation the path induces. The trigger to reach for this pattern is any definition phrased as "choose a $\dots$, then set $\dots$"; the diagnostic question is "along a path of choices, does the output live in a discrete set?" If yes, a connected space of choices forces the output constant. This is exactly why characteristic classes, being homotopy invariants valued in a cohomology group, are insensitive to the metrics, connections, and Hermitian structures used to compute them — a theme that returns in Chern–Weil theory, where $c_1$ is computed from the curvature of *any* connection and the answer is independent of the connection for the very same reason.

**"A one-parameter family of bundles over $M$" and "a single bundle over $M \times [0,1]$" are the same datum, and the second form unlocks the cylinder theorem.** The decisive step was refusing to track $c_1^{\mathrm{top}}(P_{h_t})$ as a function of $t$ — which would require differentiating classifying data — and instead assembling the whole family into one bundle $P_H$ over the cylinder, where the purely topological fact "a bundle over $M \times [0,1]$ has isomorphic ends" is available. This translation is the engine behind homotopy invariance throughout gauge theory and topology: a homotopy of maps $f_t\colon M' \to M$ is a single map $M' \times [0,1] \to M$, and pulling a bundle back along it produces a bundle over the cylinder whose ends are $f_0^*P$ and $f_1^*P$ — which is exactly how [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|the cylinder theorem]] proves that homotopic maps pull back isomorphic bundles. Whenever a problem presents a continuous family of geometric structures, the strategic move is to look for the single object over the product with the parameter interval and ask what standard theorem about such objects applies. The parameter interval need not be $[0,1]$; the same idiom over $M \times \mathbb{R}$ or over higher-dimensional parameter spaces underlies deformation invariance of Seiberg–Witten and Donaldson invariants in the later chapters.

**Prove isomorphism, not equality, and let the invariant do the last step.** The final line of the proof is essentially free: because $c_1^{\mathrm{top}}$ was defined on *isomorphism classes* of $U(1)$-bundles, the moment we have $P_{h_0} \cong P_{h_1}$ there is nothing left to compute. This is the payoff of building invariants correctly — as functions of isomorphism classes rather than of specific models — and it is worth internalising as a habit: when an invariant is known to factor through isomorphism (or homotopy, or cobordism, or diffeomorphism) classes, one never verifies equality of invariants by computing both sides, only by exhibiting an isomorphism (respectively homotopy, cobordism, diffeomorphism) between the underlying objects. The temptation, warned against above, is to try to prove the two reductions $P_{h_0}$ and $P_{h_1}$ are literally *equal*; they are not, and chasing equality both fails and obscures the point. Companion exercises pursuing the same "invariant factors through iso-classes" reflex are [[Ex - Line Bundles of Every Degree on a Closed Oriented Surface]], where the degree is shown to be a complete isomorphism invariant on surfaces, and [[Ex - The Tautological Bundle over CP^1 has Degree Minus One]], where a specific bundle's class is pinned down by identifying its isomorphism type.
