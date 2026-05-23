---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - The Maurer-Cartan Form"
  - "Def - Bracket of g-Valued Forms"
  - "Def - The Lie Algebra of a Lie Group"
tags: [geometry, gauge-theory, lie-groups, differential-forms]
---

# Notation

$G$ is a Lie group with Lie algebra $\mathfrak{g} = T_e G$. $\theta_G \in \Omega^1(G; \mathfrak{g})$ is the [[Def - The Maurer-Cartan Form|left-invariant Maurer-Cartan form]]. $\{E_R\}$ is a basis of $\mathfrak{g}$ with structure constants $[E_R, E_S] = C^T_{RS}\,E_T$; $\{X^R\}$ the corresponding left-invariant vector fields; $\{\sigma^R\}$ the dual left-invariant 1-forms. The bracket $[\,\cdot\,,\,\cdot\,]$ on $\mathfrak{g}$-valued forms is the [[Def - Bracket of g-Valued Forms|graded bracket]].

---

# Statement

> **Theorem (Maurer-Cartan equation).** Let $G$ be a Lie group and $\theta_G \in \Omega^1(G; \mathfrak{g})$ the left-invariant Maurer-Cartan form. Then
> $$
> d\theta_G + \tfrac{1}{2}[\theta_G, \theta_G] = 0
> $$
> identically on $G$. Equivalently, in a basis of left-invariant 1-forms $\sigma^R$ dual to left-invariant vector fields $X^R$,
> $$
> d\sigma^R + \tfrac{1}{2} C^R{}_{ST}\,\sigma^S \wedge \sigma^T = 0.
> $$

The two formulations are equivalent: applying the basis form to $\theta_G = E_R \otimes \sigma^R$ and using $[E_S, E_T] = C^R{}_{ST}\,E_R$.

A direct corollary: for matrix groups, $\tfrac{1}{2}[\theta_G, \theta_G] = \theta_G \wedge \theta_G$, so the equation reads
$$
d(g^{-1}dg) + (g^{-1}dg) \wedge (g^{-1}dg) = 0.
$$

---

# Motivation

The Maurer-Cartan equation is the universal structural identity satisfied by the canonical 1-form on a Lie group, and it is the *template* against which all curvature in gauge theory is measured.

To see why, recall the setup. A Lie group $G$ carries a canonical $\mathfrak{g}$-valued 1-form $\theta_G$ (the left-translation back-to-identity operator). The combination $d\theta_G + \tfrac{1}{2}[\theta_G, \theta_G]$ — the **Cartan structural combination** — has a natural meaning: it is the "curvature" of $\theta_G$ viewed as the canonical flat connection on the trivial principal bundle $G \to \{*\}$. Since this connection *is* flat (a fact one can read off the construction), the curvature must vanish. The vanishing is exactly the Maurer-Cartan equation.

More importantly, the Maurer-Cartan equation is the **template** for every gauge-theoretic structural equation:

- For a general connection $\omega$ on a general principal bundle, the analogous combination $d\omega + \tfrac{1}{2}[\omega, \omega]$ does *not* vanish in general — what it equals is the [[Def - Curvature 2-Form on a Principal Bundle|curvature 2-form]] $\Omega$. This is the [[Thm - Cartan Structural Equation for Principal Connections|Cartan structural equation]].
- For a Cartan geometry modelled on $G/H$ (a generalisation in which the connection lives on a principal $H$-bundle but takes values in $\mathfrak{g}$), the same combination measures the curvature of the Cartan geometry — and vanishes in the **flat** (Klein-geometric) case, where the Cartan geometry locally looks like $G/H$.

The Maurer-Cartan equation also encodes the **Lie algebra structure of $\mathfrak{g}$ entirely**: the basis-form $d\sigma^R + \tfrac{1}{2}C^R{}_{ST}\sigma^S \wedge \sigma^T = 0$ contains the structure constants $C^R{}_{ST}$ as coefficients, and they determine $\mathfrak{g}$ up to isomorphism. So computing $d\theta_G$ at the identity (or anywhere, by left-invariance) recovers the Lie bracket structure of $\mathfrak{g}$.

Historically, the equation was discovered by **Élie Cartan** in his foundational work on the theory of moving frames (and later perfected by him into the theory of "Cartan geometries"); it has been the central identity of Lie group theory ever since.

---

# Sources and Targets

**Sources (input broadening).**

*Source 1: The form is "left-invariant and $\mathfrak{g}$-valued".* If you have a $\mathfrak{g}$-valued 1-form on $G$ that is left-invariant and reduces to the identity on $\mathfrak{g} = T_e G$ — i.e., it is the Maurer-Cartan form — then the equation applies. The bridge $B \to A$ is "left-invariance + $\mathfrak{g}$-valued + identity-at-identity → Maurer-Cartan form". Example: a constructive definition like "let $\theta_G$ be the unique $\mathfrak{g}$-valued left-invariant 1-form on $G$ with $\theta_G(\xi^L_g) = \xi$" automatically satisfies the Maurer-Cartan equation, by this theorem.

*Source 2: The form is "$g^{-1}dg$ for a matrix Lie group".* For matrix Lie groups $G \subseteq \mathrm{GL}(n)$, $g^{-1}dg$ is *by definition* the Maurer-Cartan form, and it satisfies $d(g^{-1}dg) + (g^{-1}dg)\wedge(g^{-1}dg) = 0$. The bridge is "matrix-group plus the universal symbol $g^{-1}dg$ → Maurer-Cartan equation". Example: computing the Maurer-Cartan equation for $G = \mathrm{GL}(n)$ uses only matrix algebra and ordinary calculus — no abstract Lie-algebra machinery.

*Source 3: The "flat connection on the trivial bundle $G \to *$".* If you encounter the canonical connection on a trivial principal bundle and want to verify it is flat, the Maurer-Cartan equation is the statement of flatness. The bridge: "canonical connection on $G$-bundle over a point → curvature equals Maurer-Cartan combination → zero". Example: in a Cartan geometry calculation, verifying that the model space $G/H$ is "flat" comes down to the Maurer-Cartan equation on $G$.

**Targets (output amplification).**

*Target 1: Structure constants of $\mathfrak{g}$.* Combined with explicit basis 1-forms $\sigma^R$, the equation $d\sigma^R + \tfrac{1}{2}C^R{}_{ST}\sigma^S \wedge \sigma^T = 0$ extracts the structure constants $C^R{}_{ST}$ of $\mathfrak{g}$ as the coefficients in $d\sigma^R$. Useful when you have $G$ in a concrete parametrisation and need to read off $\mathfrak{g}$.

*Target 2: Cartan structural equation by analogy.* The Maurer-Cartan equation is the *template* for the Cartan structural equation $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$. Combined with the principal-connection axioms, it gives the curvature formula for any connection.

*Target 3: BCH (Baker-Campbell-Hausdorff) formula.* The Maurer-Cartan equation is the differential identity underlying the BCH formula $\log(\exp X \exp Y) = X + Y + \tfrac{1}{2}[X, Y] + \cdots$. Combined with the exponential map, it determines the local structure of $G$ as a Lie group.

*Target 4: Chevalley-Eilenberg complex.* Combined with the dual structure constants, the Maurer-Cartan equation defines the **Chevalley-Eilenberg differential** on $\Lambda^\bullet \mathfrak{g}^*$, the complex computing the cohomology of $\mathfrak{g}$ with trivial coefficients. The de Rham cohomology of a compact Lie group equals the cohomology of left-invariant forms, which is computed by this complex.

---

# Why Is It True

**The bolded one-liner:** *The Maurer-Cartan equation says that the canonical connection $\theta_G$ on the trivial bundle $G \to \{*\}$ is flat — and "flat" is forced by the construction, since "no base" means "no room for curvature".*

The intuition is geometric. The trivial bundle $G \to \{*\}$ has a one-point base, so any connection on it has trivially zero curvature *as a 2-form on the base* — the base has no 2-forms. The Cartan structural equation $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$ tells us that the curvature 2-form on the total space $G$ is the Maurer-Cartan combination $d\theta_G + \tfrac{1}{2}[\theta_G, \theta_G]$. Since this curvature has to descend to zero on the base (= point), it must be the case that the Maurer-Cartan combination *is* zero — that is, the Maurer-Cartan equation holds.

A second, more algebraic intuition: the Maurer-Cartan equation is the dual statement of the **Jacobi identity** for $\mathfrak{g}$. The structure constants $C^R{}_{ST}$ satisfy the Jacobi identity $C^P{}_{RS}C^R{}_{TU} + C^P{}_{RT}C^R{}_{US} + C^P{}_{RU}C^R{}_{ST} = 0$ (cyclic in $S, T, U$). Taking the exterior derivative of $\sigma^R$ and using $d^2 = 0$ on the right-hand side $-\tfrac{1}{2}C^R{}_{ST}\sigma^S\wedge\sigma^T$ produces an expression involving structure-constant combinations that must vanish — and that vanishing is precisely the Jacobi identity. So Maurer-Cartan and Jacobi are *equivalent* identities, one in form language and one in bracket language.

A third intuition: the Maurer-Cartan form $\theta_G = g^{-1}dg$ has the property that its left-translation by any $h \in G$ gives back $\theta_G$ (it is left-invariant). Combined with the chain rule, $d(g^{-1}dg) = d(g^{-1})\wedge dg = -g^{-1}(dg)g^{-1}\wedge dg = -(g^{-1}dg)\wedge(g^{-1}dg)$, which gives $d\theta_G + \theta_G \wedge \theta_G = 0$ directly. The matrix-group identity $\theta_G\wedge\theta_G = \tfrac{1}{2}[\theta_G, \theta_G]$ then gives the Maurer-Cartan equation.

---

# What Makes This Hard

The conceptual difficulty is recognising that the Maurer-Cartan equation is *both* an algebraic identity on $\mathfrak{g}$ (the Jacobi identity in form language) and a geometric statement about flatness (the connection $\theta_G$ is flat). Most people learn it as one or the other; seeing both is the key. The computational difficulty is the bracket of $\mathfrak{g}$-valued 1-forms — for matrix groups, $\tfrac{1}{2}[\theta_G, \theta_G] = \theta_G \wedge \theta_G$, but the right-hand side is the matrix wedge of a 1-form with itself, which is *nonzero* even though the wedge of a scalar 1-form with itself is zero. Getting comfortable with "$\alpha \wedge \alpha \neq 0$ for matrix-valued forms" is the technical step most people stumble on.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Work in the basis form $d\sigma^R + \tfrac{1}{2}C^R{}_{ST}\sigma^S \wedge \sigma^T = 0$. Compute $d\sigma^R$ at the identity using the duality $\sigma^R(X^S) = \delta^R_S$ and the formula $d\alpha(X, Y) = X\alpha(Y) - Y\alpha(X) - \alpha([X, Y])$ for 1-forms and the Lie bracket of vector fields. Combine with $[X^S, X^T] = C^R{}_{ST} X^R$ (structure constants of $\mathfrak{g}$ via left-invariant vector fields). Conclude by left-invariance that the equation holds everywhere on $G$.

**Subgoal decomposition:**

1. **Subgoal 1:** Evaluate $d\sigma^R(X^S, X^T)$ at the identity $e \in G$.
   - *Hint:* Use the invariant formula $d\alpha(X, Y) = X\alpha(Y) - Y\alpha(X) - \alpha([X, Y])$.
   - *Why needed:* This connects the exterior derivative of $\sigma^R$ to the Lie bracket of $X$'s and hence to structure constants.

2. **Subgoal 2:** Evaluate $\tfrac{1}{2} C^R{}_{ST}\,\sigma^S \wedge \sigma^T (X^P, X^Q)$.
   - *Hint:* Use $\sigma^R(X^S) = \delta^R_S$ and the antisymmetry of the wedge.
   - *Why needed:* The second term of the Maurer-Cartan equation, which must cancel the first.

3. **Subgoal 3:** Combine to show $d\sigma^R + \tfrac{1}{2}C^R{}_{ST}\sigma^S \wedge \sigma^T = 0$ at the identity.
   - *Hint:* The first two computations give terms that are negatives of each other.
   - *Why needed:* Establishes the equation at one point.

4. **Subgoal 4:** Extend the equation to all of $G$ by left-invariance.
   - *Hint:* All terms in the equation are left-invariant ($\sigma^R$ is left-invariant, $d$ commutes with pullback by $L_g$, the bracket of left-invariant forms is left-invariant).
   - *Why needed:* The equation holds globally on $G$, not just at $e$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Cartan's formula for $d\alpha$ on 1-forms
> **Statement:** For any smooth 1-form $\alpha$ and smooth vector fields $X, Y$ on a manifold $G$,
> $$
> d\alpha(X, Y) = X\alpha(Y) - Y\alpha(X) - \alpha([X, Y]),
> $$
> where $X\alpha(Y)$ denotes the directional derivative of the function $\alpha(Y) : G \to \mathbb{R}$ in the direction $X$.
> 
> **Hint:** This is the standard invariant formula for the exterior derivative of a 1-form, derivable from $d\alpha$'s antisymmetric bilinearity over $\mathbb{R}$ and the Leibniz-with-$d$ rule.
> 
> **Why needed:** Lets us compute $d\sigma^R$ on the basis of left-invariant vector fields.
> 
> > [!note]- Full proof
> > By the universal property of $d$ on 1-forms, both sides agree on simple tensors $\alpha = f\,dg$: $d\alpha = df\wedge dg$, so $d\alpha(X, Y) = (Xf)(Yg) - (Yf)(Xg)$. The right-hand side of the lemma is $X(f \cdot Yg) - Y(f \cdot Xg) - f \cdot [X,Y]g = (Xf)(Yg) + f \cdot XYg - (Yf)(Xg) - f \cdot YXg - f \cdot [X, Y]g = (Xf)(Yg) - (Yf)(Xg) + f(XY - YX - [X, Y])g = (Xf)(Yg) - (Yf)(Xg)$, using the definition $[X, Y] = XY - YX$ of the Lie bracket on vector fields acting on functions. So both sides agree on $\alpha = f\,dg$; by linearity, on all 1-forms.

> [!note]- Lemma 2: $d\sigma^R(X^S, X^T) = -C^R{}_{ST}$ at every point of $G$
> **Statement:** For the left-invariant basis $X^S$ of $\mathfrak{g}$ with $[X^S, X^T] = C^R{}_{ST}\,X^R$, and dual left-invariant 1-forms $\sigma^R$,
> $$
> d\sigma^R(X^S, X^T) = -C^R{}_{ST}
> $$
> at every point of $G$.
> 
> **Hint:** Apply Lemma 1 with $\alpha = \sigma^R$, $X = X^S$, $Y = X^T$, and use that $\sigma^R(X^T) = \delta^R_T$ is *constant* on $G$ (because $\sigma^R$ and $X^T$ are both left-invariant, and their pairing is a left-invariant scalar function on $G$ which by smoothness must be constant if it has any value).
> 
> **Why needed:** This is the computation of the first term in the Maurer-Cartan equation.
> 
> > [!note]- Full proof
> > By Lemma 1, $d\sigma^R(X^S, X^T) = X^S\sigma^R(X^T) - X^T\sigma^R(X^S) - \sigma^R([X^S, X^T])$. The first two terms vanish: $\sigma^R(X^T) = \delta^R_T$ is constant on $G$, so $X^S\sigma^R(X^T) = 0$. The third term: $\sigma^R([X^S, X^T]) = \sigma^R(C^P{}_{ST} X^P) = C^P{}_{ST}\delta^R_P = C^R{}_{ST}$. So $d\sigma^R(X^S, X^T) = -C^R{}_{ST}$.

> [!note]- Lemma 3: $\tfrac{1}{2} C^R{}_{ST}\,(\sigma^S \wedge \sigma^T)(X^P, X^Q) = C^R{}_{PQ}$
> **Statement:** $\tfrac{1}{2} C^R{}_{ST}\,(\sigma^S \wedge \sigma^T)(X^P, X^Q) = C^R{}_{PQ}$.
> 
> **Hint:** Use the wedge product formula $(\sigma^S \wedge \sigma^T)(X^P, X^Q) = \sigma^S(X^P)\sigma^T(X^Q) - \sigma^S(X^Q)\sigma^T(X^P) = \delta^S_P\delta^T_Q - \delta^S_Q\delta^T_P$, and the antisymmetry of $C^R{}_{ST}$ in $(S, T)$.
> 
> **Why needed:** This is the computation of the second term in the Maurer-Cartan equation, which (when summed with the first) gives zero.
> 
> > [!note]- Full proof
> > $\tfrac{1}{2} C^R{}_{ST}(\sigma^S \wedge \sigma^T)(X^P, X^Q) = \tfrac{1}{2}C^R{}_{ST}(\delta^S_P \delta^T_Q - \delta^S_Q\delta^T_P) = \tfrac{1}{2}(C^R{}_{PQ} - C^R{}_{QP}) = \tfrac{1}{2} \cdot 2 C^R{}_{PQ} = C^R{}_{PQ}$, using the antisymmetry $C^R{}_{ST} = -C^R{}_{TS}$ inherited from the Lie bracket.

> [!note]- Lemma 4: Combine Lemmas 2 and 3 to conclude
> **Statement:** $(d\sigma^R + \tfrac{1}{2}C^R{}_{ST}\sigma^S \wedge \sigma^T)(X^P, X^Q) = 0$ for all $P, Q$.
> 
> **Hint:** Lemma 2 gives $-C^R{}_{PQ}$ for the first term; Lemma 3 gives $+C^R{}_{PQ}$ for the second; sum is zero.
> 
> **Why needed:** The basis form of the Maurer-Cartan equation holds on the basis of $TG$.
> 
> > [!note]- Full proof
> > Direct addition: $d\sigma^R(X^P, X^Q) + \tfrac{1}{2}C^R{}_{ST}(\sigma^S \wedge \sigma^T)(X^P, X^Q) = -C^R{}_{PQ} + C^R{}_{PQ} = 0$. By the bilinearity of both sides in the vector fields, this equality holds for all pairs of left-invariant vector fields, hence for all pairs of vector fields (any vector field is a linear combination of $X^P$'s pointwise). The equation $d\sigma^R + \tfrac{1}{2}C^R{}_{ST}\sigma^S \wedge \sigma^T = 0$ holds as an identity of 2-forms.

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1 (Cartan's formula for $d\alpha$ on 1-forms), for any smooth 1-form $\alpha$ and smooth vector fields $X, Y$,
> $$
> d\alpha(X, Y) = X\alpha(Y) - Y\alpha(X) - \alpha([X, Y]).
> $$
> 
> Apply with $\alpha = \sigma^R$, $X = X^S$, $Y = X^T$ (left-invariant vector fields with $[X^S, X^T] = C^P{}_{ST}\,X^P$). Since $\sigma^R(X^T) = \delta^R_T$ is constant on $G$ (Lemma 2), the first two terms vanish, and we get
> $$
> d\sigma^R(X^S, X^T) = -C^R{}_{ST}.
> $$
> 
> By Lemma 3,
> $$
> \tfrac{1}{2}C^R{}_{PQ}\,(\sigma^P \wedge \sigma^Q)(X^S, X^T) = C^R{}_{ST}.
> $$
> 
> Adding,
> $$
> \big(d\sigma^R + \tfrac{1}{2}C^R{}_{PQ}\sigma^P \wedge \sigma^Q\big)(X^S, X^T) = 0.
> $$
> 
> Since the $X^R$'s are a basis of $TG$ at every point (left-invariant frame), this gives
> $$
> d\sigma^R + \tfrac{1}{2}C^R{}_{PQ}\sigma^P \wedge \sigma^Q = 0
> $$
> identically on $G$.
> 
> Recombining into the invariant form: $\theta_G = E_R \otimes \sigma^R$, so $d\theta_G = E_R \otimes d\sigma^R$ and $\tfrac{1}{2}[\theta_G, \theta_G] = \tfrac{1}{2}[E_P, E_Q]\otimes\sigma^P \wedge \sigma^Q = \tfrac{1}{2}C^R{}_{PQ}\,E_R \otimes \sigma^P \wedge \sigma^Q$. Adding,
> $$
> d\theta_G + \tfrac{1}{2}[\theta_G, \theta_G] = E_R \otimes (d\sigma^R + \tfrac{1}{2}C^R{}_{PQ}\sigma^P \wedge \sigma^Q) = 0.
> $$
> 
> This completes the proof.

---

# Cross-Field Exercise Suggestions

**Cartan geometry (Differential geometry / Cartan's program).** The Maurer-Cartan equation is the *flatness condition* of a Cartan geometry modelled on $G/H$: the curvature of the Cartan connection $\theta$ is $d\theta + \tfrac{1}{2}[\theta, \theta]$, which vanishes precisely for the flat (Klein-geometric) model. So computing the Maurer-Cartan equation for the model is the prototype of "geometric flatness". This shows up in conformal geometry ($G/H = SO(n+1,1)/SO(n)\times O(1,1)$), projective geometry ($SL(n+1)/$parabolic), and parabolic geometries generally.

**BCH formula and local Lie theory.** The Maurer-Cartan equation is the differential identity underlying the **Baker-Campbell-Hausdorff (BCH) formula** $\log(e^X e^Y) = X + Y + \tfrac{1}{2}[X, Y] + \tfrac{1}{12}[X, [X, Y]] - \tfrac{1}{12}[Y, [X, Y]] + \cdots$. Specifically, pulling back the Maurer-Cartan form under the group multiplication map $\mu : G \times G \to G$ and integrating gives the BCH series. This is the bridge from Lie group theory to formal power series in non-commutative variables.

**Chevalley-Eilenberg cohomology.** The dual structure-constant equation $d\sigma^R + \tfrac{1}{2}C^R{}_{ST}\sigma^S\wedge\sigma^T = 0$ is the **defining identity** of the Chevalley-Eilenberg complex $(\Lambda^\bullet\mathfrak{g}^*, d_{CE})$, which computes the cohomology of $\mathfrak{g}$ with trivial coefficients. For a compact Lie group $G$, the de Rham cohomology $H^\bullet(G; \mathbb{R})$ equals the cohomology of left-invariant forms, which equals the Chevalley-Eilenberg cohomology $H^\bullet_{CE}(\mathfrak{g}; \mathbb{R})$ — a purely algebraic computation. This is the bridge from differential geometry to homological algebra of Lie algebras.

**Spin structures and the Maurer-Cartan form on $SU(2)$.** On $SU(2) \cong S^3$ with its Maurer-Cartan form, the three left-invariant 1-forms $\sigma^a$ ($a = 1, 2, 3$) provide a global parallelisation of $S^3$. They satisfy the $\mathfrak{su}(2)$ Maurer-Cartan equation $d\sigma^a + \varepsilon^a{}_{bc}\sigma^b \wedge \sigma^c = 0$ (with the right normalisation). This is used in the construction of the **BPST instanton** on $S^4$, in **Berry phase** calculations, and in the analysis of the Hopf fibration.

---

# Bridges

- **[[Thm - Cartan Structural Equation for Principal Connections|Cartan structural equation]]** — the Maurer-Cartan equation is the *flat case* of the Cartan structural equation $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$. The structural equation reduces to the Maurer-Cartan equation when the connection is flat and the bundle is trivial: $\omega = \theta_G$ on $G \to *$ has $\Omega = 0$, which is the Maurer-Cartan equation. So the Maurer-Cartan equation is the *template* for every gauge-theoretic curvature formula — every curvature is a deformation of this identity.

- **Jacobi identity on $\mathfrak{g}$** — the Maurer-Cartan equation in basis form is *the dual statement of the Jacobi identity* on $\mathfrak{g}$. Differentiating $d\sigma^R + \tfrac{1}{2}C^R{}_{ST}\sigma^S \wedge \sigma^T = 0$ and using $d^2 = 0$ produces, after a calculation, the identity $C^P{}_{RS}C^R{}_{TU} + \text{cyclic} = 0$ — which is the Jacobi identity for the structure constants $C^R{}_{ST}$. So Maurer-Cartan and Jacobi are equivalent identities, one expressed in form language, one in bracket language.

- **[[Def - The Maurer-Cartan Form|Maurer-Cartan form]] as universal flat connection** — the Maurer-Cartan equation is the statement that $\theta_G$ is the canonical *flat* connection on the trivial bundle $G \to *$. Every flat connection on every principal bundle is *locally* pulled back from this universal model, so the Maurer-Cartan equation governs the entire theory of flat connections. This is the bridge to **monodromy / holonomy** of flat connections.

- **BCH formula and the multiplication of $G$** — the Maurer-Cartan equation, pulled back along the multiplication map $\mu : G \times G \to G$, gives the differential identity underlying the BCH series $\log(e^X e^Y) = X + Y + \tfrac{1}{2}[X, Y] + \cdots$. So the multiplication of $G$ near the identity is *encoded* in the Maurer-Cartan equation — recovering $G$'s Lie group structure from $\mathfrak{g}$ alone, via integration.

---

# Unlocked by This

> [!tip] Cartan Structural Equation *(from Gauge Theory III)*
> The Maurer-Cartan equation is the prototype of the [[Thm - Cartan Structural Equation for Principal Connections|Cartan structural equation]] $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$. Every curvature formula in gauge theory is a deformation of the Maurer-Cartan equation. The structural equation says "the curvature of a general connection is $d\omega + \tfrac{1}{2}[\omega, \omega]$"; the Maurer-Cartan equation says "for the canonical flat connection, this combination vanishes".

> [!tip] Chevalley-Eilenberg Cohomology *(from Homological Algebra)*
> The Maurer-Cartan equation in basis form defines the **Chevalley-Eilenberg differential** on $\Lambda^\bullet\mathfrak{g}^*$: $d_{CE}\sigma^R = -\tfrac{1}{2}C^R{}_{ST}\sigma^S \wedge \sigma^T$. The resulting cohomology $H^\bullet_{CE}(\mathfrak{g}; \mathbb{R})$ computes the de Rham cohomology of a compact Lie group $G$ as a purely algebraic invariant of $\mathfrak{g}$, by the **van Est theorem**. This is the foundational bridge between Lie algebra cohomology and the topology of Lie groups.

> [!tip] Cartan Geometries *(from Differential Geometry)*
> A **Cartan geometry** modelled on a homogeneous space $G/H$ is a principal $H$-bundle equipped with a $\mathfrak{g}$-valued 1-form pointwise reproducing $\theta_G$. The Maurer-Cartan equation holds in the flat (Klein-geometric) case; its failure for a general Cartan geometry is the **Cartan curvature**. This unifies Riemannian, conformal, projective, and parabolic geometries under a single rubric.

> [!tip] L-infinity Algebras and Deformation Theory *(from Higher Algebra)*
> Solutions of the **Maurer-Cartan equation in a DGLA** (differential graded Lie algebra) classify the (formal) deformations of a geometric structure: complex structures, Poisson structures, flat $G$-bundles. The fundamental insight of **derived deformation theory** (Kontsevich, Lurie) is that every deformation problem is governed by a Maurer-Cartan equation in some DGLA, and the solutions modulo gauge equivalence are the moduli space.
