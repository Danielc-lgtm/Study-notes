---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Classification of Principal U(1)-Bundles by the First Chern Class"
  - "Thm - Clutching Construction for Bundles over a Closed Manifold"
  - "Thm - Winding Number of a Map from the Circle to U(1)"
  - "Thm - Principal Bundles are Classified by Cocycles"
  - "Def - Transition Functions and the Cocycle Condition"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\Sigma$ be a closed connected oriented surface — a two-dimensional manifold, compact and without boundary. On $\Sigma$ the principal $U(1)$-bundles (equivalently the complex line bundles) are classified up to isomorphism by a single integer, the degree, $\deg\colon \operatorname{Pic}(\Sigma) \xrightarrow{\ \sim\ } \mathbb{Z}$. This exercise realises every value of the degree by an explicit construction.

For each integer $d \in \mathbb{Z}$, let $z \mapsto z^d$ denote the map $S^1 \to U(1)$, $S^1 = \{z \in \mathbb{C} : |z| = 1\}$, and let $P_{z^d} \to \Sigma$ be the principal $U(1)$-bundle obtained by clutching a coordinate disc $D \subset \Sigma$ to its complement with clutching function $z^d$. Prove:

$$\text{(i) } P_{z^d} \text{ has degree } d; \qquad \text{(ii) } P_{z^d} \cong P_z^{\otimes d} \text{ for every } d \in \mathbb{Z}.$$

Carry out the construction of $P_{z^d}$ **explicitly** on two surfaces: the two-sphere $S^2$ and the torus $T^2 = \mathbb{R}^2 / \mathbb{Z}^2$. Conclude that for every $d \in \mathbb{Z}$ there is a principal $U(1)$-bundle over $\Sigma$ of degree $d$ — the existence (surjectivity) half of Haydys' classification of line bundles on oriented surfaces (source item A-E2.4.1, Example 72, p. 24) and of Bär's degree $\deg L = d$ (the degree recorded in source item A-D2.4.4).

> [!warning] Convention: source labelling
> The manifest cites this content as "B-D2.4.4". In Bär's notes D2.4.4 is a curvature form, unrelated to line bundles; the degree of a line bundle on an oriented surface is Haydys' item D2.4.4 (his Example 72, p. 24). We follow the corrected reading — the degree $d$ of a complex line bundle over an oriented closed surface — and flag the mislabel here. Throughout, $\operatorname{Pic}(\Sigma)$ denotes the group of isomorphism classes of principal $U(1)$-bundles (equivalently Hermitian line bundles) under tensor product, in the series' convention that avoids singular cohomology.

**Recall:**

The objects in play are the clutching construction of a bundle from a disc and its complement, the winding number of a circle map, the degree classification of $U(1)$-bundles on a surface, and the cocycle description of transition functions and of tensor products.

![[Thm - Clutching Construction for Bundles over a Closed Manifold#Statement]]

The parts we use: for a closed connected surface $\Sigma$, a closed coordinate disc $D \subset \Sigma$ with boundary $S = \partial D \cong S^1$, and any smooth $g\colon S \to U(1)$, part (a) supplies a principal $U(1)$-bundle $P_g \to \Sigma$ that is trivial over $\Sigma \setminus D^\circ$ and over $D$, with transition function $g$ across a collar of $S$; part (c) says $P_g \cong P_{g'}$ if and only if $g' = (a|_S)\,g\,(b|_S)$ for smooth $a\colon \Sigma \setminus D^\circ \to U(1)$, $b\colon D \to U(1)$; and part (d) says $P_g$ is trivial exactly when $g$ has this form with $g' = e$.

![[Thm - Winding Number of a Map from the Circle to U(1)#Statement]]

The parts we use: for smooth $g\colon S^1 \to U(1)$, the winding number $w(g) = \tfrac{1}{2\pi i}\int_{S^1} g^{-1}\,dg$ is an integer; it is additive under pointwise products, $w(g_1 g_2) = w(g_1) + w(g_2)$ and $w(g^{-1}) = -w(g)$ (part (b)); and $w(z \mapsto z^k) = k$ (part (e)).

![[Thm - Classification of Principal U(1)-Bundles by the First Chern Class#Statement]]

The part we use is (C): for a closed connected oriented surface $\Sigma$, the degree $\deg\colon \operatorname{Pic}(\Sigma) \to \mathbb{Z}$, defined by $\deg(P_g) := w(g)$ for a clutching function $g$ of $P$, is a group isomorphism; in particular $\deg(P_1 \otimes P_2) = \deg P_1 + \deg P_2$, and $\deg$ is well defined (independent of the clutching data used to present $P$).

![[Thm - Principal Bundles are Classified by Cocycles#Statement]]

The parts we use: part (a), that a cocycle $\{g_{\alpha\beta}\}$ on a cover reconstructs a principal bundle glued from the trivial pieces $U_\alpha \times G$ by $(x,h) \sim (x, g_{\alpha\beta}(x)h)$; part (c), that two cocycles on the same cover give isomorphic bundles if and only if they are cohomologous; and part (d), that the associated vector bundle $P \times_\rho V$ has transition functions $\rho \circ g_{\alpha\beta}$.

---

# Convergent Strategy

**Problem class.** This is a *realisation* problem: an invariant (the degree) is known to take values in $\mathbb{Z}$, and we must exhibit, for each value, an object achieving it — and moreover organise the objects so that they are visibly all built from one generator. Realisation problems are solved by finding the most economical construction whose invariant we can read off directly; here that construction is clutching, because the degree *is by definition* the winding number of the clutching function, so the invariant is transparent from the start.

**Assumption pattern.** Two features of a closed oriented surface make the construction go through. First, a surface is *locally a disc*: it contains a coordinate disc $D$, and the clutching construction cares only about the disc, its boundary circle, and the complement, never about the global shape — this is why the very same recipe produces bundles of every degree on the sphere and on the torus (and on any genus), the genus never entering. Second, $U(1)$ is *abelian and one-dimensional*, so its self-maps on the boundary circle carry a single integer invariant (the winding number), and multiplication of clutching functions corresponds to tensor product of bundles — turning "power of a generator" into "power of a clutching function".

**Theorem routing.** The route is: build $P_{z^d}$ by **[[Thm - Clutching Construction for Bundles over a Closed Manifold|clutching]]** with $g = z^d$ (part (a)); read its degree as $\deg P_{z^d} = w(z^d) = d$ using the **[[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|degree classification]]** (C) and the **[[Thm - Winding Number of a Map from the Circle to U(1)|winding number]]** (e); prove that tensor product multiplies clutching functions using the **[[Thm - Principal Bundles are Classified by Cocycles|cocycle theorem]]** (c),(d); and deduce $P_z^{\otimes d} \cong P_{z^d}$ by induction, handling $d < 0$ through the dual bundle with clutching function $z^{-1}$.

**Key decision point.** The one genuinely non-obvious link is that *tensor product of $U(1)$-bundles multiplies their clutching functions*. Everything else is a direct specialisation of theorems already in hand, but this fact is what makes the answer structured rather than a mere list: it says $P_{z^d}$ is not just *some* degree-$d$ bundle but precisely the $d$-th tensor power of the degree-$1$ generator $P_z$, so a single generator organises all of $\operatorname{Pic}(\Sigma)$. Recognising that the clutching function of a tensor product is the product of the clutching functions — because a local frame of $L \otimes L'$ is the tensor of local frames of $L$ and $L'$, and a frame change multiplies — is the crux, and it is where the abelian, rank-one nature of $U(1)$ is used decisively.

---

# Legal Operations Used

This solution deploys the following operations (named descriptively; they correspond to the operations catalogued on the [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles|chapter topic page]]'s Legal Operations, whose numbering the topic page fixes):

1. **Clutch a bundle from a disc and its complement.** Choose a coordinate disc $D \subset \Sigma$; for a prescribed smooth $g\colon \partial D \to U(1)$ form the bundle $P_g$ trivial over $\Sigma \setminus D^\circ$ and over $D$, glued across a collar of $\partial D$ by $g$.

2. **Read the degree off the clutching function.** Because $\deg(P_g) = w(g)$, the winding number of the clutching function is the degree; specialise to $g = z^d$ and use $w(z^d) = d$.

3. **Realise the construction in explicit coordinates on a chosen surface.** Fix an explicit disc and boundary parametrisation on $S^2$ and on $T^2$ and write down the quotient total space of $P_{z^d}$.

4. **Compute the transition functions of an associated line bundle.** Pass from the principal $U(1)$-bundle $P_g$ to its associated line bundle $L_g = P_g \times_{U(1)} \mathbb{C}$; its transition function is $\varrho_1 \circ g = g$.

5. **Multiply transition functions to tensor line bundles.** A local frame of $L \otimes L'$ is the tensor of local frames of $L$ and $L'$; a frame change acts by the product, so the transition function of $L \otimes L'$ is the product of those of $L$ and $L'$.

6. **Invert transition functions to dualise, and iterate by induction.** The dual line bundle inverts transition functions ($z \mapsto z^{-1}$); combine with operation 5 to reach every integer power, positive, zero, and negative.

---

# Hints

> [!note]- Hint 1
> The degree of a $U(1)$-bundle over a surface is, by definition, the winding number of a clutching function that presents it. So do not try to compute anything analytic: just *build* a bundle whose clutching function you choose, and read the degree off. What clutching function $g\colon S^1 \to U(1)$ has winding number exactly $d$?

> [!note]- Hint 2
> Take $g(z) = z^d$. The clutching construction needs only a coordinate disc $D$ and its boundary circle, nothing about the rest of the surface — that is why the same recipe works on $S^2$ and on $T^2$. On $S^2$ let $D$ be the southern cap and $\Sigma \setminus D^\circ$ the northern cap, meeting along the equator; on $T^2 = \mathbb{R}^2/\mathbb{Z}^2$ let $D$ be a small round disc in a chart. Write the total space as two trivial pieces glued over the collar of the boundary circle by $(x,u) \sim (x, z(x)^d u)$.

> [!note]- Hint 3
> For part (ii) you must relate $P_{z^d}$ to the tensor power $P_z^{\otimes d}$. Tensor product of line bundles corresponds to *multiplying* transition functions: if $L$ and $L'$ are trivialised over the same two sets with transition functions $g$ and $g'$, take the tensor of the two local frames and see what frame change results across the overlap. What is the transition function of $L \otimes L'$?

> [!note]- Hint 4
> The transition function of $L \otimes L'$ is $g g'$ (pointwise product in $U(1)$). Hence the associated $U(1)$-bundle of $L_z \otimes L_z$ is $P_{z \cdot z} = P_{z^2}$, and by induction $P_z^{\otimes d} \cong P_{z^d}$ for $d \geq 1$. For $d = 0$, the empty tensor power is the trivial bundle, which is $P_{z^0} = P_1$. For $d < 0$, the dual $P_z^\vee$ has clutching function $z^{-1}$ (dualising inverts transition functions); tensor $|d|$ copies of it.

---

# Solution

The construction is a single application of the clutching theorem with the clutching function chosen to be $z^d$, whose winding number is $d$ by inspection; the degree is then $d$ with no computation, because the degree of a clutched bundle *is* the winding number of its clutching function. The identification $P_{z^d} \cong P_z^{\otimes d}$ rests on the one structural fact that tensoring line bundles multiplies transition functions, so that the clutching function of $P_z^{\otimes d}$ is $z^d$; the abelian group $U(1)$ makes both the winding number and this multiplication behave additively in the exponent.

**Step 1: The clutching data, and the definition of $P_{z^d}$ on a closed oriented surface.**

Fix a coordinate disc $D \subset \Sigma$, identify a collar of its boundary circle $S = \partial D$ with the unit circle, and define $P_{z^d}$ by clutching with $g = z^d$.

> [!note]- Derivation
> Let $\Sigma$ be a closed connected oriented surface. Choose a smooth chart $\varphi\colon W \to \mathbb{R}^2$ onto an open set, with $W \subset \Sigma$ open, and let
> $$D := \varphi^{-1}\big(\{y \in \mathbb{R}^2 : |y| \leq 1\}\big)$$
> be the closed coordinate disc that is the preimage of the closed unit ball; its boundary is the circle $S := \partial D = \varphi^{-1}(\{|y| = 1\})$, and $D$ carries the orientation induced from $\Sigma$. The boundary circle is identified with the standard unit circle by
> $$z\colon S \to S^1 = \{z \in \mathbb{C} : |z| = 1\}, \qquad z\big(\varphi^{-1}(\cos\theta, \sin\theta)\big) = e^{i\theta},$$
> where the orientation of $S = \partial D$ as the boundary of $D$ fixes the sense of increasing $\theta$. For an integer $d$, define the clutching function
> $$g_d\colon S \to U(1), \qquad g_d = (z \mapsto z^d), \quad\text{i.e.}\quad g_d\big(\varphi^{-1}(\cos\theta,\sin\theta)\big) = e^{i d\theta}.$$
> By part (a) of **[[Thm - Clutching Construction for Bundles over a Closed Manifold|the clutching theorem]]** — *for every smooth $g\colon S \to U(1)$ there is a principal $U(1)$-bundle $P_g \to \Sigma$, trivial over $\Sigma \setminus D^\circ$ and over $D$, with transition function the collar extension of $g$* — there is a principal $U(1)$-bundle
> $$P_{z^d} := P_{g_d} \longrightarrow \Sigma.$$
> Explicitly, choosing a collar $c\colon S \times (-\varepsilon, \varepsilon) \hookrightarrow \Sigma$ of $S$ with $c(\cdot, 0) = \mathrm{id}_S$, $c(S \times (0,\varepsilon)) \subset \Sigma \setminus D$ and $c(S \times (-\varepsilon, 0)) \subset D^\circ$, set the open cover
> $$U_0 := (\Sigma \setminus D) \cup c\big(S \times (-\varepsilon,\varepsilon)\big), \qquad U_1 := D^\circ \cup c\big(S \times (-\varepsilon,\varepsilon)\big),$$
> so $U_0 \cup U_1 = \Sigma$ and $U_0 \cap U_1 = c(S \times (-\varepsilon,\varepsilon))$ retracts onto $S$ by $c(s,\tau) \mapsto s$. The single transition function $g_{01}\colon U_0 \cap U_1 \to U(1)$ is $g_{01}(c(s,\tau)) := z(s)^d$ (the collar extension of $g_d$, constant in $\tau$), together with $g_{10} = g_{01}^{-1}$ and $g_{00} = g_{11} = e$. These satisfy the cocycle conditions: on a two-set cover the only nontrivial triple overlap lies within $U_0 \cap U_1$, where $g_{00}g_{01}g_{10} = e \cdot g_{01} \cdot g_{01}^{-1} = e$, and $g_{00} = g_{11} = e$, $g_{01} = g_{10}^{-1}$ by construction; so by part (a) of **[[Thm - Principal Bundles are Classified by Cocycles|the cocycle theorem]]**,
> $$P_{z^d} = \big(U_0 \times U(1) \ \sqcup\ U_1 \times U(1)\big)\big/\!\sim, \qquad (x, u)_0 \sim (x, g_{01}(x)\,u)_1 \ \text{ for } x \in U_0 \cap U_1.$$
> This is the total space; $\Sigma \setminus D^\circ$ carries the section $s_0(x) = [x, e]_0$ and $D$ carries $s_1(x) = [x, e]_1$, with $s_1 = s_0 \cdot g_{01}$ on the collar.

**Step 2: The degree of $P_{z^d}$ is $d$.**

The degree of a clutched bundle is the winding number of its clutching function, and $w(z^d) = d$.

> [!note]- Derivation
> By part (C) of **[[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|the degree classification]]** — *on a closed connected oriented surface the degree of a bundle presented by a clutching function $g$ is $\deg(P_g) = w(g)$, and this is well defined independently of the presentation* — the bundle $P_{z^d} = P_{g_d}$ has
> $$\deg P_{z^d} = w(g_d) = w(z \mapsto z^d).$$
> By part (e) of **[[Thm - Winding Number of a Map from the Circle to U(1)|the winding number theorem]]** — *$w(z \mapsto z^k) = k$* —
> $$w(z \mapsto z^d) = d.$$
> (For completeness, this is the direct computation $w(z^d) = \tfrac{1}{2\pi i}\int_{S^1} (z^d)^{-1}\,d(z^d) = \tfrac{1}{2\pi i}\int_{S^1} z^{-d}\cdot d z^{d-1}\,dz = \tfrac{d}{2\pi i}\int_{S^1} z^{-1}\,dz = \tfrac{d}{2\pi i}\cdot 2\pi i = d$, using $\int_{S^1} z^{-1}\,dz = 2\pi i$.) Therefore
> $$\deg P_{z^d} = d.$$

**Step 3: The explicit construction on $S^2$.**

On the sphere, take $D$ to be the southern cap and $\Sigma \setminus D^\circ$ the northern cap, meeting along the equator, and glue two trivial cylinders over the equator by $z^d$.

> [!note]- Derivation
> Realise $S^2 = \{(x_1, x_2, x_3) \in \mathbb{R}^3 : x_1^2 + x_2^2 + x_3^2 = 1\}$ with the orientation induced by the outward normal. Let
> $$D := \{(x_1,x_2,x_3) \in S^2 : x_3 \leq 0\} \quad\text{(closed southern cap)}, \qquad \Sigma \setminus D^\circ = \{x_3 \geq 0\} \quad\text{(closed northern cap)},$$
> both closed discs, meeting in the equator $S = \{x_3 = 0\} \cong S^1$. Parametrise the equator by $z(\cos\theta, \sin\theta, 0) = e^{i\theta}$, with $\theta$ increasing in the sense that orients $S = \partial D$ as the boundary of the southern cap. Take the two open sets $U_1 = \{x_3 < \tfrac{1}{2}\} \supset D$ and $U_0 = \{x_3 > -\tfrac{1}{2}\} \supset (\Sigma \setminus D^\circ)$, whose intersection is the equatorial band $\{|x_3| < \tfrac{1}{2}\}$, which deformation-retracts onto the equator by scaling the $(x_1,x_2)$ part to the unit circle. Define $g_{01}\colon U_0 \cap U_1 \to U(1)$ to be $z^d$ composed with this retraction. Then, by Steps 1–2,
> $$P_{z^d}^{S^2} = \big(U_0 \times U(1) \ \sqcup\ U_1 \times U(1)\big)\big/\!\big((x,u)_0 \sim (x, z(x)^d u)_1\big), \qquad \deg P_{z^d}^{S^2} = w(z^d) = d.$$
> For $d = 1$ this is (up to the sign fixed by the orientation, computed in [[Ex - The Tautological Bundle over CP^1 has Degree Minus One]]) the Hopf bundle $S^3 \to S^2 = \mathbb{CP}^1$: its transition function across the equator is $z/|z|$, of winding number one, exactly as recorded on [[Def - The Hopf Bundle]].

**Step 4: The explicit construction on $T^2$.**

On the torus, take $D$ to be a small round disc in a fundamental-domain chart and glue as before; the genus-one complement plays no role beyond providing the trivial piece.

> [!note]- Derivation
> Realise the torus as $T^2 = \mathbb{R}^2 / \mathbb{Z}^2$ with the orientation of $\mathbb{R}^2$, and let $q\colon \mathbb{R}^2 \to T^2$ be the quotient map. Fix a centre $c \in \mathbb{R}^2$ and a radius $r < \tfrac{1}{2}$, so that $q$ restricts to a diffeomorphism of the closed ball $\overline{B}(c,r) = \{y : |y - c| \leq r\}$ onto its image; set
> $$D := q\big(\overline{B}(c,r)\big) \subset T^2, \qquad S = \partial D = q\big(\{|y - c| = r\}\big) \cong S^1,$$
> a coordinate disc with boundary circle parametrised by $z\big(q(c + r(\cos\theta, \sin\theta))\big) = e^{i\theta}$, oriented as $\partial D$. The complement $T^2 \setminus D^\circ$ is a compact genus-one surface with the one boundary circle $S$. Take open sets $U_1 = q(B(c, r + \delta))$ (a slightly larger disc, $r + \delta < \tfrac{1}{2}$) and $U_0 = T^2 \setminus \overline{D'}$ thickened across the collar, where $D' = q(\overline{B}(c, r - \delta))$, so that $U_0 \cup U_1 = T^2$ and $U_0 \cap U_1$ is an annular collar of $S$ retracting onto $S$. With $g_{01} = z^d$ across this collar, Steps 1–2 give
> $$P_{z^d}^{T^2} = \big(U_0 \times U(1) \ \sqcup\ U_1 \times U(1)\big)\big/\!\big((x,u)_0 \sim (x, z(x)^d u)_1\big), \qquad \deg P_{z^d}^{T^2} = w(z^d) = d.$$
> The construction is word-for-word the sphere construction with the northern cap replaced by the genus-one surface $T^2 \setminus D^\circ$: only the local disc, its boundary circle, and the clutching function enter, so the genus is irrelevant to the degree. This is the concrete reason the classification "$\deg\colon \operatorname{Pic}(\Sigma) \to \mathbb{Z}$ is onto" holds identically for every closed oriented surface.

**Step 5: Tensor product multiplies clutching functions.**

If $P_g$ and $P_{g'}$ are clutched over the same disc $D$ with clutching functions $g, g'$, then $P_g \otimes P_{g'} \cong P_{g g'}$.

> [!note]- Derivation
> The tensor product of two principal $U(1)$-bundles is defined through their associated line bundles: with $L_g := P_g \times_{U(1)} \mathbb{C}$ and $L_{g'} := P_{g'} \times_{U(1)} \mathbb{C}$ (the standard representation $\varrho_1(\lambda)w = \lambda w$), one sets $P_g \otimes P_{g'} :=$ the unitary frame bundle of $L_g \otimes L_{g'}$, a principal $U(1)$-bundle. We compute its transition function.
>
> Work over the two-set cover $\{U_0, U_1\}$ of Step 1. By part (d) of **[[Thm - Principal Bundles are Classified by Cocycles|the cocycle theorem]]** — *the associated bundle $P \times_\rho V$ has transition functions $\rho \circ g_{\alpha\beta}$* — the line bundle $L_g$ has transition function $\varrho_1 \circ g = g$ (since $\varrho_1 = \mathrm{id}$ on $U(1) \subset \mathbb{C}^\times$), and likewise $L_{g'}$ has transition function $g'$. Concretely, $L_g$ has a nowhere-zero local frame $e_0$ over $U_0$ and $e_1$ over $U_1$, related on the collar by
> $$e_1 = g\, e_0,$$
> and $L_{g'}$ has frames $e_0', e_1'$ with $e_1' = g'\, e_0'$. The tensor product $L_g \otimes L_{g'}$ then has the local frames $e_0 \otimes e_0'$ over $U_0$ and $e_1 \otimes e_1'$ over $U_1$, and on the collar
> $$e_1 \otimes e_1' = (g\, e_0) \otimes (g'\, e_0') = (g g')\,(e_0 \otimes e_0') \qquad \text{(bilinearity of } \otimes \text{ pulls the scalars } g, g' \in U(1) \subset \mathbb{C} \text{ out).}$$
> Hence the transition function of $L_g \otimes L_{g'}$ across the collar is the pointwise product $g g'\colon U_0 \cap U_1 \to U(1)$ — well defined and $U(1)$-valued because $U(1)$ is an abelian group. The same product cocycle $\{g g'\}$ presents the clutched bundle $P_{g g'}$ (Step 1). By part (c) of the cocycle theorem — *two cocycles on the same cover give isomorphic bundles if and only if they are cohomologous* — the bundles with the identical cocycle $g g'$ are isomorphic:
> $$P_g \otimes P_{g'} \ \cong\ P_{g g'}.$$
> (As a consistency check with Step 2, $\deg(P_g \otimes P_{g'}) = w(g g') = w(g) + w(g') = \deg P_g + \deg P_{g'}$ by the additivity of the winding number, part (b) of the winding number theorem — exactly the additivity of degree recorded in the classification (C).)

**Step 6: $P_{z^d} \cong P_z^{\otimes d}$ for every $d \in \mathbb{Z}$, and every degree is realised.**

Induction on $|d|$ using Step 5, with the dual bundle for negative $d$, gives $P_z^{\otimes d} \cong P_{z^d}$; combined with Step 2 this realises every integer degree.

> [!note]- Derivation
> Write $P_z := P_{z^1}$, the clutching bundle of $g_1 = (z \mapsto z)$, of degree $1$ by Step 2. We treat the three cases $d > 0$, $d = 0$, $d < 0$, which are exhaustive.
>
> **Case $d > 0$ (induction).** For $d = 1$, $P_z^{\otimes 1} = P_z = P_{z^1}$ by definition. Assume $P_z^{\otimes (d-1)} \cong P_{z^{d-1}}$ for some $d \geq 2$. Then
> $$P_z^{\otimes d} = P_z^{\otimes(d-1)} \otimes P_z \ \cong\ P_{z^{d-1}} \otimes P_{z^1} \ \cong\ P_{z^{d-1} \cdot z} = P_{z^d} \qquad \text{(inductive hypothesis, then Step 5 with } g = z^{d-1},\, g' = z\text{).}$$
> By induction $P_z^{\otimes d} \cong P_{z^d}$ for all $d \geq 1$.
>
> **Case $d = 0$.** The empty tensor power $P_z^{\otimes 0}$ is by convention the identity of $\operatorname{Pic}(\Sigma)$, the trivial bundle $\underline{U(1)} = \Sigma \times U(1)$. The clutching bundle $P_{z^0} = P_1$ has constant clutching function $g_0 \equiv e$; by part (d) of the clutching theorem — *$P_g$ is trivial iff $g = (a|_S)(b|_S)$, in particular when $g \equiv e$* — $P_1$ is trivial. Hence $P_z^{\otimes 0} = \underline{U(1)} \cong P_1 = P_{z^0}$.
>
> **Case $d < 0$.** Write $d = -k$ with $k > 0$. The negative tensor powers are defined through the dual (equivalently conjugate) bundle: $P_z^{\otimes(-k)} = (P_z^\vee)^{\otimes k}$, where $P_z^\vee$ is the unitary frame bundle of the dual line bundle $L_z^\vee = \operatorname{Hom}(L_z, \mathbb{C})$. Dualising inverts transition functions: if $e_1 = z\, e_0$ are frames of $L_z$, the dual frames $e_0^*, e_1^*$ (defined by $e_i^*(e_i) = 1$) satisfy $e_1^* = z^{-1} e_0^*$, so $L_z^\vee$ has clutching function $z^{-1}$ and $P_z^\vee \cong P_{z^{-1}}$. Applying the $d > 0$ result to the generator $P_{z^{-1}}$ (whose clutching function is $z^{-1}$, so that $(P_{z^{-1}})^{\otimes k} \cong P_{(z^{-1})^k} = P_{z^{-k}}$ by the same induction via Step 5),
> $$P_z^{\otimes(-k)} = (P_z^\vee)^{\otimes k} \cong (P_{z^{-1}})^{\otimes k} \cong P_{z^{-k}} = P_{z^d}.$$
>
> In all three cases $P_z^{\otimes d} \cong P_{z^d}$. Together with Step 2, for every $d \in \mathbb{Z}$ the bundle $P_{z^d} = P_z^{\otimes d}$ is a principal $U(1)$-bundle over $\Sigma$ of degree exactly $d$. Since $d$ was arbitrary, the degree map $\deg\colon \operatorname{Pic}(\Sigma) \to \mathbb{Z}$ is surjective, and every isomorphism class is the $d$-th tensor power of the single generator $P_z$.

> [!note]- Complete formal solution
> **Claim.** Let $\Sigma$ be a closed connected oriented surface. For each $d \in \mathbb{Z}$ there is a principal $U(1)$-bundle $P_{z^d} \to \Sigma$ of degree $d$, constructed explicitly by clutching on $S^2$ and on $T^2$, and $P_{z^d} \cong P_z^{\otimes d}$.
>
> *Construction.* Fix a closed coordinate disc $D \subset \Sigma$ with boundary $S = \partial D$, parametrised by $z\colon S \to S^1$ compatibly with the boundary orientation. For $d \in \mathbb{Z}$ let $g_d = (z \mapsto z^d)\colon S \to U(1)$, and let $P_{z^d} := P_{g_d}$ be the clutching bundle of the clutching theorem, part (a): trivial over $U_0 \supset \Sigma \setminus D^\circ$ and $U_1 \supset D$, with total space $(U_0 \times U(1) \sqcup U_1 \times U(1))/((x,u)_0 \sim (x, z(x)^d u)_1)$ across the collar $U_0 \cap U_1$. On $S^2$ take $D$ the southern cap, $\Sigma \setminus D^\circ$ the northern cap, $S$ the equator; on $T^2 = \mathbb{R}^2/\mathbb{Z}^2$ take $D$ a round disc of radius $r < \tfrac12$ in a fundamental-domain chart. The recipe is identical because only $D$, $S$, and $g_d$ enter.
>
> *Degree.* By the degree classification, part (C), $\deg P_{z^d} = w(g_d)$, and by the winding number theorem, part (e), $w(z \mapsto z^d) = d$. So $\deg P_{z^d} = d$.
>
> *Tensor product multiplies clutching functions.* Over the two-set cover, the associated line bundle $L_g = P_g \times_{\varrho_1} \mathbb{C}$ has transition function $g$ (cocycle theorem, part (d), with $\varrho_1 = \mathrm{id}$), i.e. frames $e_0, e_1$ with $e_1 = g e_0$. For $L_g, L_{g'}$ the tensor $L_g \otimes L_{g'}$ has frames $e_0 \otimes e_0'$ and $e_1 \otimes e_1' = (g e_0)\otimes(g' e_0') = g g'\,(e_0 \otimes e_0')$, so its transition function is $g g'$. By the cocycle theorem, part (c), $P_g \otimes P_{g'} \cong P_{g g'}$.
>
> *Powers.* With $P_z := P_{z^1}$: for $d \geq 1$, induction gives $P_z^{\otimes d} = P_z^{\otimes(d-1)} \otimes P_z \cong P_{z^{d-1}} \otimes P_z \cong P_{z^d}$; for $d = 0$, $P_z^{\otimes 0} = \underline{U(1)} \cong P_1 = P_{z^0}$ (clutching theorem, part (d)); for $d = -k < 0$, $P_z^\vee \cong P_{z^{-1}}$ (dualising inverts transition functions) and $P_z^{\otimes(-k)} = (P_z^\vee)^{\otimes k} \cong P_{z^{-k}}$. Hence $P_z^{\otimes d} \cong P_{z^d}$ for all $d \in \mathbb{Z}$.
>
> *Conclusion.* For every $d \in \mathbb{Z}$, $P_{z^d} = P_z^{\otimes d}$ has degree $d$; the degree map is surjective and every class is a tensor power of $P_z$. $\blacksquare$

> [!warning] Illegal but tempting route: presenting all bundles on the same cover without justification
> The tensor-product computation in Step 5 silently assumes $P_g$ and $P_{g'}$ are trivialised over the *same* two sets $\{U_0, U_1\}$ with clutching over the same collar, so that their transition functions can be multiplied pointwise. This is legitimate here only because both bundles were *constructed* by clutching over one fixed disc $D$; for two bundles handed to us with unrelated trivialising covers, one may not simply multiply transition functions — one must first pass to a common refinement of the two covers (a standard but non-vacuous step) and rewrite both cocycles there. The multiplication of clutching functions is the *special case* of the common-refinement construction in which the common cover is already the two-set clutching cover. The condition that makes the shortcut legal is precisely that both bundles are given by clutching over the *same* $D$; when that fails, refine first.
>
> A second tempting shortcut is to declare $P_{z^d}$ "obviously" nontrivial for $d \neq 0$ because its clutching function $z^d$ is nonconstant. This is false as stated: triviality is not "constant clutching function" but "clutching function of the form $(a|_S)(b|_S)$" (clutching theorem, part (d)); a nonconstant $g$ with winding number zero, such as $z \mapsto e^{i(\cos\theta - 1)}$, still gives a trivial bundle. The correct invariant is the *winding number*, not constancy — which is exactly why the degree, and not mere nonconstancy, is the classifying integer.

---

# Key Takeaways

**Clutching turns a topological classification problem into an arithmetic one: build the bundle whose gluing datum you control, and read the invariant off the gluing datum.** The reusable principle is that on a space assembled from a disc and its complement — a surface, a sphere $S^n$, any closed manifold with a distinguished coordinate ball — a bundle is completely encoded by its clutching function on the boundary sphere, and the classifying invariant is a homotopy invariant of that function. On a surface the boundary is a circle and the invariant is the winding number $w(g) \in \mathbb{Z}$; on $S^4$ (chapter's $SU(2)$ story) the boundary is $S^3$ and the invariant is the degree $\deg(g\colon S^3 \to SU(2)) \in \mathbb{Z}$. The trigger to reach for clutching is a base space that is *trivial off a disc* (any $U(1)$- or $SU(2)$-bundle over a surface or a simply connected $4$-manifold is, by the generic-section argument of the classification theorems); the diagnostic is then "what is the homotopy invariant of maps from the boundary sphere into the structure group?" This same move recurs whenever one needs to *realise* a value of an invariant: rather than searching among all bundles, construct the clutching function achieving the value directly, as we did with $z^d$.

**Tensor product of line bundles is addition of degrees because it is multiplication of transition functions, and the abelian rank-one structure of $U(1)$ makes both visible in the exponent.** The core computation — a local frame of $L \otimes L'$ is the tensor of local frames, and a frame change multiplies, so transition functions multiply — is the concrete mechanism behind the group law on $\operatorname{Pic}$. It is worth carrying as a self-contained fact: $\operatorname{Pic}(\Sigma)$ is a group under tensor product with the dual as inverse, the trivial bundle as identity, and the degree is a *homomorphism* to $\mathbb{Z}$ because winding number is additive under products of circle maps. Recognising this reduces the whole classification to identifying one generator ($P_z$, of degree one) and observing that every other bundle is a tensor power of it — the structural statement "$\operatorname{Pic}(\Sigma)$ is infinite cyclic, generated by the degree-one bundle". The transferable diagnostic: whenever an invariant is additive and the objects form a group under a product operation, look for a single generator and express everything as its powers, converting a classification into a statement about one element.

**The genus never enters: a local construction sees only the disc, so results proved on the simplest surface transfer verbatim.** The sphere and the torus received *identical* constructions, differing only in what the complementary trivial piece happened to be — a disc for $S^2$, a genus-one surface for $T^2$ — and that difference was invisible to the degree because the clutching construction reads only the disc, its boundary circle, and the clutching function. This is a general lesson about local-to-global invariants: an invariant defined through data supported near a point or a disc is insensitive to the global topology away from that region, so one may compute it on whichever model is most convenient. The same insensitivity is why the second Chern number of an $SU(2)$-bundle over a closed oriented $4$-manifold, defined by clutching over a coordinate ball, does not depend on the manifold's global topology and is computed on $S^4$ (see the $SU(2)$ classification and its Chern–Weil identification in chapter VI). The companion exercise [[Ex - The First Chern Class does not Depend on the Hermitian Structure]] makes the dual point — that the invariant ignores the *auxiliary* choices — while this one shows it ignores the *global* shape; together they isolate exactly what the degree does depend on: the single integer winding the boundary circle around $U(1)$.
