---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Connection 1-Form on a Principal Bundle"
  - "Def - Local Connection 1-Form (Gauge Potential)"
  - "Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection"
tags: [geometry, gauge-theory, electromagnetism, principal-bundles]
---

# Problem Statement

Consider a principal $U(1)$-bundle $P \to M$ over a manifold $M$ (for concreteness, take $M =$ Minkowski space $\mathbb{R}^{1,3}$ and assume $P = M \times U(1)$ is trivial).

**(a)** Write down a global connection 1-form $\omega$ on the total space $P$ in a local trivialisation using the fibre coordinate $e^{i\theta}$. Verify the two axioms of a principal connection.

**(b)** Choose a section $s : M \to P$ (canonical: $s(x) = (x, e^{i \cdot 0}) = (x, 1)$). Compute the pullback $A := s^*\omega$ and identify it with the electromagnetic 4-potential $A_\mu dx^\mu$ of [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection|Gauge Theory I]].

**(c)** Verify the gauge transformation law: under $g(x) = e^{i\chi(x)}$ (a smooth $U(1)$-valued function), the new section $s'(x) = s(x) \cdot e^{i\chi(x)}$ has gauge potential $A' = A + i d\chi$ (the abelian special case of $A' = g^{-1}Ag + g^{-1}dg$).

**Recall:**

A principal $U(1)$-bundle is a principal $G$-bundle with structure group $G = U(1) = \{e^{i\theta}\}$. The Lie algebra is $\mathfrak{u}(1) = i\mathbb{R}$. The right action on the trivial bundle $M \times U(1)$ is $(x, e^{i\theta}) \cdot e^{i\alpha} = (x, e^{i(\theta + \alpha)})$.

A connection 1-form on $P$: ![[Def - Connection 1-Form on a Principal Bundle#The Definition]]

The local gauge potential: ![[Def - Local Connection 1-Form (Gauge Potential)#The Definition]]

The electromagnetic 4-potential is a $\mathfrak{u}(1)$-valued (often written real-valued with an implicit $i$) 1-form $A = A_\mu dx^\mu$ on Minkowski space, with field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ encoding the electric and magnetic fields.

---

# Convergent Strategy

**Problem class:** This is a *concrete-construction-of-a-principal-connection* problem. The general pattern: given an explicit principal bundle (here: trivial $U(1)$-bundle), construct an explicit connection 1-form, then derive the local gauge potential by pullback. The exercise illustrates how the abstract principal-bundle formalism specialises to the familiar electromagnetic-vector-potential setup of physics.

**Assumption pattern:** $U(1)$ is abelian — the adjoint action $\mathrm{Ad}_g\xi = g\xi g^{-1} = \xi$ is trivial (since $U(1)$ is abelian, conjugation in $\mathfrak{u}(1)$ is the identity). The bracket on $\mathfrak{u}(1)$ vanishes. So all the non-abelian structure (Maurer-Cartan inhomogeneous term, adjoint conjugation, bracket of forms) collapses to the abelian: $A' = A + g^{-1}dg = A + id\chi$, $F = dA$, no $[A, A]$ self-coupling.

**Theorem routing:** [[Def - Connection 1-Form on a Principal Bundle|connection axioms]] for the construction of $\omega$. [[Def - Local Connection 1-Form (Gauge Potential)|gauge potential]] for the pullback definition. [[Thm - Gauge Transformation Law for Local Connection 1-Forms|gauge transformation law]] for the abelian special case.

**Key decision point:** The choice of $\omega$ is essentially forced once we choose a base coupling $A_\mu$: $\omega = i d\theta + i A_\mu dx^\mu$ (or its abelian version with the $i$'s arranged according to convention). The non-trivial check is that the canonical section's pullback gives the standard 4-potential, and that the gauge transformation law reproduces the standard $A \mapsto A + d\chi$.

---

# Legal Operations Used

1. **Operation 1 (pull back along a section).** $A = s^*\omega$ — directly applied to compute the gauge potential in the canonical gauge.

2. **Operation 2 (gauge transformation law).** Apply $A' = g^{-1}Ag + g^{-1}dg$ for $g = e^{i\chi}$, simplify in the abelian case to $A' = A + id\chi$.

10. **Operation 10 (specialise the abelian case).** $G = U(1)$: $[\,\cdot\,,\,\cdot\,]_{\mathfrak{u}(1)} = 0$, $\mathrm{Ad}_g\xi = \xi$, $F = dA$, no self-coupling. Use this to simplify all formulas.

---

# Hints

> [!note]- Hint 1
> In a local trivialisation $P = U \times U(1)$ with fibre coordinate $\theta$ (so $g = e^{i\theta}$, $\theta \in \mathbb{R}/2\pi\mathbb{Z}$), the **vertical direction** is $\partial_\theta$, and the fundamental vector field of $i \in \mathfrak{u}(1) = i\mathbb{R}$ is $\partial_\theta$ (with normalisation $i^*_{(x, e^{i\theta})} = \partial_\theta$).

> [!note]- Hint 2
> The connection 1-form should: (i) satisfy $\omega(\partial_\theta) = i$ (verticality with $i \in \mathfrak{u}(1)$); (ii) couple to a base 1-form $A_\mu dx^\mu$. A natural choice is $\omega = i\,d\theta + i\,A_\mu(x)\,dx^\mu$. Verify this satisfies the axioms.

> [!note]- Hint 3
> Equivariance for $U(1)$ is automatic in the abelian case: $\mathrm{Ad}_g\xi = \xi$ for all $g \in U(1)$, so $R_g^*\omega = \omega$ — the connection is right-invariant, not just equivariant. (The non-trivial equivariance content is only for non-abelian groups.)

> [!note]- Hint 4
> For the pullback in the canonical gauge $s(x) = (x, e^{i \cdot 0})$: $s^*(i\,d\theta) = i\,s^*(d\theta) = 0$ (since $\theta \circ s = 0$ is constant), and $s^*(i\,A_\mu dx^\mu) = i\,A_\mu dx^\mu$ (on $M$, the $x^\mu$ are coordinates). So $A := s^*\omega = i A_\mu dx^\mu$ — the standard electromagnetic 4-potential, with the $i$ absorbed into the convention of $\mathfrak{u}(1) = i\mathbb{R}$.

> [!note]- Hint 5
> For the gauge transformation: under $g(x) = e^{i\chi(x)}$, the new section is $s'(x) = (x, e^{i\chi(x)})$. Compute $A' = (s')^*\omega = (s')^*(id\theta + iA_\mu dx^\mu) = i(d\theta \circ s')(\cdot) + iA_\mu dx^\mu$. The pullback $d\theta \circ s' = d\chi$ (since $\theta \circ s' = \chi$). So $A' = i\,d\chi + iA_\mu dx^\mu = A + i\,d\chi$. ✓

---

# Solution

**Plan:** Construct $\omega = i\,d\theta + i A_\mu dx^\mu$ on the trivial $U(1)$-bundle, verify the two axioms (verticality and equivariance), pullback along the canonical section to get $A = iA_\mu dx^\mu$, then perform a gauge transformation $g = e^{i\chi}$ and verify $A' = A + i d\chi$.

**Step 1: The connection 1-form $\omega$.**

On the trivial bundle $P = M \times U(1)$ with fibre coordinate $\theta \in \mathbb{R}/2\pi\mathbb{Z}$, define
$$
\omega := i\,d\theta + i\,A_\mu(x)\,dx^\mu \in \Omega^1(P; \mathfrak{u}(1)),
$$
where $A_\mu(x)$ are smooth real-valued functions on the base $M$ — to be identified with the electromagnetic 4-potential.

> [!note]- Derivation
> A general $\mathfrak{u}(1)$-valued 1-form on $P = M \times U(1)$ decomposes as
> $$
> \omega = f(x, \theta)\,d\theta + g_\mu(x, \theta)\,dx^\mu
> $$
> with $f, g_\mu$ smooth $\mathfrak{u}(1) = i\mathbb{R}$-valued functions.
> 
> **Verticality** requires $\omega(i^*) = i$, where $i^* = \partial_\theta$ (the fundamental vector field of $i \in \mathfrak{u}(1)$ on the trivial bundle). Apply: $\omega(\partial_\theta) = f(x, \theta)$. So $f = i$ — the constant $\mathfrak{u}(1)$-value $i$.
> 
> **Equivariance** requires $R_g^*\omega = \mathrm{Ad}_{g^{-1}}\omega = \omega$ (since $U(1)$ abelian). Under right action $(x, e^{i\theta}) \cdot e^{i\alpha} = (x, e^{i(\theta + \alpha)})$, the form $d\theta$ pulls back to $d\theta$ (translation-invariant), and $dx^\mu$ pulls back to $dx^\mu$. So $R_{e^{i\alpha}}^*\omega = i\,d\theta + i\,g_\mu(x, \theta + \alpha)\,dx^\mu$. For equivariance, $g_\mu(x, \theta + \alpha) = g_\mu(x, \theta)$ for all $\alpha$, i.e., $g_\mu$ is $\theta$-independent. So $g_\mu = g_\mu(x)$ — a function on the base only.
> 
> Renaming $g_\mu(x) = i A_\mu(x)$ (so $A_\mu$ is the real-valued component), we get $\omega = i\,d\theta + i\,A_\mu(x)\,dx^\mu$. ✓

**Step 2: The local gauge potential in the canonical gauge.**

The canonical section is $s : M \to P$, $s(x) = (x, e^{i \cdot 0}) = (x, 1)$ (the identity element of $U(1)$ at every point). The pullback is

> [!note]- Derivation
> $$
> A := s^*\omega = s^*(i\,d\theta + i\,A_\mu(x)\,dx^\mu).
> $$
> The function $\theta \circ s = 0$ is constant, so $s^*(d\theta) = d(\theta \circ s) = d(0) = 0$. The pullback $s^*(dx^\mu) = dx^\mu$ (on $M$, the $x^\mu$ are coordinates already). So
> $$
> A = i\,A_\mu(x)\,dx^\mu = i A_\mu dx^\mu \in \Omega^1(M; \mathfrak{u}(1)).
> $$
> The factor of $i$ is just the embedding $\mathfrak{u}(1) = i\mathbb{R}$; physicists often absorb it and write $A = A_\mu dx^\mu$ with $A_\mu$ understood as real-valued (multiplying by the unit of $\mathfrak{u}(1)$ implicitly). Either way, this is the **electromagnetic 4-potential** of [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection|Gauge Theory I]].

**Step 3: Gauge transformation.**

Apply a gauge transformation $g(x) = e^{i\chi(x)}$ for a smooth $\chi : M \to \mathbb{R}$. The new section is

> [!note]- Derivation
> $s'(x) = s(x) \cdot e^{i\chi(x)} = (x, e^{i\chi(x)})$. Pullback:
> $$
> A' := (s')^*\omega = (s')^*(i\,d\theta + i\,A_\mu(x)\,dx^\mu).
> $$
> The function $\theta \circ s' = \chi(x)$ is now non-constant. So $(s')^*(d\theta) = d(\theta \circ s') = d\chi$. The other term is unchanged: $(s')^*(i A_\mu dx^\mu) = i A_\mu dx^\mu$.
> 
> So $A' = i\,d\chi + i A_\mu dx^\mu = A + i\,d\chi$ — the standard electromagnetic gauge transformation $A \mapsto A + d\chi$ (with the $i$ explicit).
> 
> **Match to the general formula:** the gauge transformation law for a non-abelian connection is $A' = g^{-1}Ag + g^{-1}dg$. For abelian $G = U(1)$, $g^{-1}Ag = A$ (conjugation in an abelian group is trivial) and $g^{-1}dg = e^{-i\chi}\,d(e^{i\chi}) = e^{-i\chi}\,i e^{i\chi}\,d\chi = i\,d\chi$. So $A' = A + i\,d\chi$ — matches. ✓

> [!note]- Complete formal solution
> **The connection 1-form.** On $P = M \times U(1)$ with fibre coordinate $\theta$, define
> $$
> \omega := i\,d\theta + i\,A_\mu(x)\,dx^\mu \in \Omega^1(P; \mathfrak{u}(1)).
> $$
> 
> **Axioms.**
> - *Verticality:* the fundamental vector field of $i \in \mathfrak{u}(1)$ at $(x, e^{i\theta})$ is $\partial_\theta$, and $\omega(\partial_\theta) = i + 0 = i$. ✓
> - *Equivariance:* $U(1)$ abelian, $R_g^*\omega = \omega$ (translation-invariance of $d\theta$ + $\theta$-independence of $A_\mu$). $\mathrm{Ad}_{g^{-1}}\omega = \omega$ (trivial adjoint action). ✓
> 
> **Local gauge potential.** Canonical section $s(x) = (x, 1)$ gives $\theta \circ s = 0$, so
> $$
> A = s^*\omega = 0 + i A_\mu dx^\mu = i A_\mu dx^\mu.
> $$
> This is the electromagnetic 4-potential ($\mathfrak{u}(1)$-valued, equivalent to a real-valued 1-form via the embedding $\mathfrak{u}(1) = i\mathbb{R}$).
> 
> **Gauge transformation.** For $g(x) = e^{i\chi(x)}$, new section $s'(x) = (x, e^{i\chi(x)})$ gives
> $$
> A' = (s')^*\omega = i\,d\chi + i A_\mu dx^\mu = A + i\,d\chi.
> $$
> This matches the general gauge transformation law $A' = g^{-1}Ag + g^{-1}dg$ in the abelian special case where $g^{-1}Ag = A$ and $g^{-1}dg = i\,d\chi$. ∎

---

# Key Takeaways

**Electromagnetism is the abelian special case of principal-bundle gauge theory.** Everything in the principal-bundle formalism — connection 1-form on $P$, gauge potential as pullback, gauge transformation law, curvature as Cartan structural equation, Bianchi identity — specialises cleanly to electromagnetism when $G = U(1)$. The connection $\omega = i\,d\theta + i A_\mu dx^\mu$ on the trivial bundle, the gauge potential $A = iA_\mu dx^\mu$ in the canonical gauge, the gauge transformation $A \mapsto A + i\,d\chi$, the field strength $F = dA$, the Bianchi identity $dF = 0$ (Maxwell's geometric half) — all are the abelian shadows of the general non-abelian theory. Recognising this lets one see electromagnetism as a *geometric* theory, not just a vector-calculus theory.

**The gauge potential is a pullback, not a global object on $M$.** The local gauge potential $A_\mu dx^\mu$ is the pullback of the global connection 1-form $\omega$ on $P$ along a section. Different sections give different pullbacks, and the gauge transformation law is the cocycle that records the dependence. For a *trivial* bundle (like $M \times U(1)$ on a contractible $M$), a global section exists and the gauge potential is "globally defined modulo gauge". For *non-trivial* bundles (like the Hopf bundle $S^3 \to S^2$ that hosts the Dirac monopole), no global section exists, and the gauge potential must be specified by local potentials on charts plus transition functions.

**The abelian gauge transformation $A \mapsto A + d\chi$ is just the Maurer-Cartan form of the gauge.** In the general formula $g^{-1}dg$, with $g = e^{i\chi}$, $g^{-1}dg = i d\chi$ — exactly the Maurer-Cartan form of the $U(1)$-valued function $\chi$. So the electromagnetic gauge freedom is literally "adding the Maurer-Cartan form of an arbitrary gauge transformation", a direct application of the general principle. This explains why the gauge potential is *not* a tensor: the Maurer-Cartan form is intrinsically non-tensorial (it has the $g^{-1}dg$ chain-rule term that destroys tensorial transformation).

**Trigger-reaction pattern: "$U(1)$ on a trivial bundle" → "the connection is $i d\theta + iA$, the gauge potential is $iA_\mu dx^\mu$".** This recipe applies whenever you have a $U(1)$-bundle (charged scalar fields, electromagnetism, Berry phase, geometric phases in molecular physics). The explicit formula gives you the gauge potential in any chosen gauge; the gauge transformation law tells you how to change gauge. For non-trivial bundles (Dirac monopole, anomalous Hall effect), the same recipe works *locally on each chart*, with the transition functions on overlaps governed by the cocycle data.
