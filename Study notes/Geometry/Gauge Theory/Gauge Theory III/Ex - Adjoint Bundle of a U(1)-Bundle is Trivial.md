---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Adjoint Bundle"
  - "Def - Adjoint Representation"
  - "Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection"
tags: [geometry, gauge-theory, electromagnetism, abelian, adjoint-bundle]
---

# Problem Statement

Let $P \to M$ be any principal $U(1)$-bundle over a manifold $M$ (not necessarily trivial — e.g., the Hopf bundle $S^3 \to S^2$, or any non-trivial $U(1)$-bundle).

**Show that the adjoint bundle $\mathrm{Ad}\,P = P \times_{\mathrm{Ad}} \mathfrak{u}(1)$ is canonically isomorphic to the trivial line bundle $M \times \mathfrak{u}(1) = M \times i\mathbb{R}$**, as a vector bundle over $M$.

**Equivalently:** show that any $\mathfrak{u}(1)$-valued $r$-form section of $\Omega^r(M; \mathrm{Ad}\,P)$ is just an ordinary $\mathfrak{u}(1)$-valued (i.e., real-valued) $r$-form on $M$. In particular, the **electromagnetic field strength** $F$ — a 2-form section of $\mathrm{Ad}\,P$ for the electromagnetic $U(1)$-connection — is a *globally defined* ordinary 2-form on $M$.

**Compare with the non-abelian case** ($G = SU(2)$, say): the adjoint bundle $\mathrm{Ad}\,P$ is generically *non-trivial*, and the field strength $F$ is a section of a *non-trivial* bundle, not an ordinary 2-form on $M$.

**Recall:**

The adjoint bundle: ![[Def - Adjoint Bundle#The Definition]]

The adjoint representation: $\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g})$, $\mathrm{Ad}_g(\xi) = g\xi g^{-1}$ (matrix-group case). For abelian $G$, $\mathrm{Ad}_g(\xi) = \xi$ (conjugation is trivial in abelian groups).

The Lie algebra $\mathfrak{u}(1) = i\mathbb{R}$ (the tangent space to $U(1) = \{e^{i\theta}\}$ at the identity).

---

# Convergent Strategy

**Problem class:** This is a *triviality-of-an-associated-bundle* problem. The general pattern: identify when an associated bundle is trivial, by analysing the cocycle (transition functions) and the representation. The exercise illustrates the dramatic simplification of abelian gauge theory: many "non-trivial" bundle constructions become trivial when the structure group is abelian.

**Assumption pattern:** $G = U(1)$ — abelian, so the adjoint representation is trivial. This single fact — $\mathrm{Ad}_g = \mathrm{id}$ for $g \in U(1)$ — kills the non-triviality of the adjoint bundle.

**Theorem routing:** The adjoint bundle is constructed via the cocycle $\mathrm{Ad}(c_{\alpha\beta}) : \mathfrak{g} \to \mathfrak{g}$ where $c_{\alpha\beta}$ are the transition functions of $P$. For abelian $G$, $\mathrm{Ad}(c_{\alpha\beta}) = \mathrm{id}$ — the cocycle is *constant*, identical to that of the trivial bundle. Hence $\mathrm{Ad}\,P \cong M \times \mathfrak{g}$.

**Key decision point:** The recognition that "abelian $G$" implies "trivial adjoint action" requires only the definition of the adjoint representation and the abelian-ness of $U(1)$. The conclusion "trivial bundle" is then immediate from the cocycle construction of associated bundles.

---

# Legal Operations Used

10. **Operation 10 (specialise to the abelian case).** $G = U(1)$ abelian → $\mathrm{Ad}_g = \mathrm{id}$ → trivial adjoint bundle. This is the entire argument.

7. **Operation 7 (use induced connection on associated bundle).** For the *trivial* adjoint bundle, the induced connection is just $d$ (since there is no twisting to account for). The field strength $F$ as a section of $\mathrm{Ad}\,P = M \times i\mathbb{R}$ is just an ordinary 2-form.

---

# Hints

> [!note]- Hint 1
> The adjoint bundle is constructed from $P$ by replacing the structure-group action on the fibre $\mathfrak{g}$ with the adjoint action $\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g})$. For abelian $G$, the conjugation $g\xi g^{-1} = \xi$ for all $g, \xi$, so $\mathrm{Ad}_g = \mathrm{id}$ — the adjoint action is trivial.

> [!note]- Hint 2
> With trivial $\mathrm{Ad}$, the transition functions of $\mathrm{Ad}\,P$ are $\mathrm{Ad}(c_{\alpha\beta}) = \mathrm{id}$ for all $\alpha, \beta$ — the cocycle is constant (the identity map on $\mathfrak{g}$). A vector bundle with constant transition functions is, by definition, trivial.

> [!note]- Hint 3
> Equivalently: a section $\psi$ of $\mathrm{Ad}\,P$ is locally a $\mathfrak{g}$-valued function $\psi_\alpha$ on each $U_\alpha$, with cocycle $\psi_\beta = \mathrm{Ad}_{c_{\alpha\beta}^{-1}}\psi_\alpha = \psi_\alpha$ — that is, $\psi_\alpha = \psi_\beta$ on overlaps. So $\psi$ is a globally well-defined $\mathfrak{g}$-valued function on $M$, identifying $\Gamma(\mathrm{Ad}\,P) \cong C^\infty(M; \mathfrak{g})$.

> [!note]- Hint 4
> For the field strength $F$: in the abelian case, $F = dA$ (no $[A, A]$ term). The local gauge potentials $A_\alpha$ are related by $A_\beta = A_\alpha + c_{\alpha\beta}^{-1}dc_{\alpha\beta}$. The difference $A_\beta - A_\alpha = c_{\alpha\beta}^{-1}dc_{\alpha\beta} = -i\,d(\arg c_{\alpha\beta})$ (using $c_{\alpha\beta} = e^{i\theta_{\alpha\beta}}$) is a *closed* 1-form (its $d$ is zero). Hence $dA_\beta = dA_\alpha$, so $F_\beta = F_\alpha$ on overlaps — the field strength is a globally well-defined 2-form on $M$.

> [!note]- Hint 5
> Compare with the non-abelian case ($G = SU(2)$): the adjoint action $\mathrm{Ad}_g\xi = g\xi g^{-1}$ is *non-trivial* (in fact, equivalent to the rotation $SO(3)$-action on $\mathfrak{su}(2) \cong \mathbb{R}^3$). For a non-trivial $SU(2)$-bundle, the adjoint bundle $\mathrm{Ad}\,P$ is a non-trivial rank-3 real vector bundle, and the field strength $F \in \Omega^2(M; \mathrm{Ad}\,P)$ is a section of this non-trivial bundle — *not* an ordinary 2-form. The simplification "abelian → trivial adjoint" is genuinely special to abelian gauge theory.

---

# Solution

**Plan:** Apply the definition of the adjoint bundle, observe that $\mathrm{Ad}_g = \mathrm{id}$ for abelian $G = U(1)$, conclude that the cocycle is trivial and hence the bundle is trivial. Identify the field strength $F$ as a globally defined ordinary 2-form.

**Step 1: Adjoint action on $\mathfrak{u}(1)$ is trivial.**

> [!note]- Derivation
> For $g \in U(1) = \{e^{i\theta} : \theta \in \mathbb{R}/2\pi\mathbb{Z}\}$ and $\xi \in \mathfrak{u}(1) = i\mathbb{R}$:
> $$
> \mathrm{Ad}_g(\xi) = g \cdot \xi \cdot g^{-1} = e^{i\theta} \cdot ix \cdot e^{-i\theta} = ix
> $$
> for $\xi = ix$ with $x \in \mathbb{R}$, since complex multiplication is commutative ($e^{i\theta}$ and $ix$ are both complex numbers, and they commute).
> 
> So $\mathrm{Ad}_g = \mathrm{id}_{\mathfrak{u}(1)}$ for all $g \in U(1)$. ✓

**Step 2: Cocycle of $\mathrm{Ad}\,P$ is trivial.**

> [!note]- Derivation
> By the [[Def - Adjoint Bundle|definition]] of the adjoint bundle: $\mathrm{Ad}\,P = (P \times \mathfrak{g})/G$ with diagonal action $(p, \xi) \cdot g = (p \cdot g, \mathrm{Ad}_{g^{-1}}\xi)$. Locally, a section is a $\mathfrak{g}$-valued function $\psi_\alpha$ on each trivialising patch $U_\alpha$, transforming on overlaps as
> $$
> \psi_\beta(x) = \mathrm{Ad}_{c_{\alpha\beta}^{-1}(x)}\,\psi_\alpha(x),
> $$
> where $c_{\alpha\beta} : U_\alpha \cap U_\beta \to G$ are the transition functions of $P$.
> 
> For $G = U(1)$, $\mathrm{Ad}_{c_{\alpha\beta}^{-1}} = \mathrm{id}_{\mathfrak{u}(1)}$ (by Step 1). So the cocycle simplifies:
> $$
> \psi_\beta(x) = \psi_\alpha(x) \text{ on } U_\alpha \cap U_\beta.
> $$
> 
> A "section" of $\mathrm{Ad}\,P$ is therefore a collection of $\mathfrak{u}(1)$-valued functions on each chart that *agree on overlaps* — that is, a globally defined smooth $\mathfrak{u}(1)$-valued function on $M$.

**Step 3: $\mathrm{Ad}\,P$ is the trivial line bundle.**

> [!note]- Derivation
> A vector bundle is *trivial* iff it has constant transition functions (the identity in the structure group). The transition functions of $\mathrm{Ad}\,P$ are $\mathrm{Ad}(c_{\alpha\beta}) = \mathrm{id}$, which is the trivial cocycle. So
> $$
> \mathrm{Ad}\,P \cong M \times \mathfrak{u}(1) = M \times i\mathbb{R}
> $$
> as a vector bundle over $M$, canonically. This is the *trivial real line bundle of rank 1* over $M$ (with the $i$ absorbed into the fibre).

**Step 4: Electromagnetic field strength is globally defined.**

> [!note]- Derivation
> The electromagnetic $U(1)$-connection has local gauge potentials $A_\alpha \in \Omega^1(U_\alpha; \mathfrak{u}(1))$, related on overlaps by the abelian gauge transformation law
> $$
> A_\beta = A_\alpha + c_{\alpha\beta}^{-1}\,dc_{\alpha\beta}
> $$
> (since $\mathrm{Ad}_{c_{\alpha\beta}^{-1}}A_\alpha = A_\alpha$ in the abelian case).
> 
> The local field strength is $F_\alpha = dA_\alpha$. On overlaps:
> $$
> F_\beta = dA_\beta = d(A_\alpha + c_{\alpha\beta}^{-1}\,dc_{\alpha\beta}) = dA_\alpha + d(c_{\alpha\beta}^{-1}\,dc_{\alpha\beta}).
> $$
> But $d(c_{\alpha\beta}^{-1}\,dc_{\alpha\beta}) = -(c_{\alpha\beta}^{-2})(dc_{\alpha\beta})\wedge dc_{\alpha\beta} + c_{\alpha\beta}^{-1}d^2c_{\alpha\beta} = 0$ (the first term vanishes because $dc_{\alpha\beta} \wedge dc_{\alpha\beta} = 0$ for any scalar function $c_{\alpha\beta}$; the second because $d^2 = 0$). So $F_\beta = F_\alpha$ on overlaps.
> 
> Hence the local field strengths $\{F_\alpha\}$ agree on overlaps, defining a *global* ordinary 2-form on $M$:
> $$
> F \in \Omega^2(M; \mathbb{R}) \quad \text{(or equivalently } \Omega^2(M; \mathfrak{u}(1)) = \Omega^2(M; i\mathbb{R}) \text{)}.
> $$
> The electromagnetic field strength is a *globally defined* 2-form on spacetime, independent of the gauge choice. This is why physicists routinely write "$F_{\mu\nu}(x)$" as a function of position alone, without worrying about gauge.

> [!note]- Complete formal solution
> **Step 1.** For abelian $G = U(1)$ and $\xi \in \mathfrak{u}(1) = i\mathbb{R}$, the adjoint action $\mathrm{Ad}_g\xi = g\xi g^{-1} = \xi$ (complex multiplication is commutative). So $\mathrm{Ad}_g = \mathrm{id}_{\mathfrak{u}(1)}$ for all $g \in U(1)$.
> 
> **Step 2.** The cocycle of the adjoint bundle is $\mathrm{Ad}(c_{\alpha\beta}) = \mathrm{id}$ — trivial. A section $\psi$ of $\mathrm{Ad}\,P$ is locally a $\mathfrak{u}(1)$-valued function $\psi_\alpha$ on $U_\alpha$, with $\psi_\beta = \psi_\alpha$ on overlaps (no twisting). Equivalently, sections of $\mathrm{Ad}\,P$ are globally defined smooth $\mathfrak{u}(1)$-valued functions on $M$.
> 
> **Step 3.** Therefore
> $$
> \mathrm{Ad}\,P \cong M \times \mathfrak{u}(1) = M \times i\mathbb{R}
> $$
> as a vector bundle over $M$, canonically.
> 
> **Step 4.** The electromagnetic field strength $F$, viewed as a 2-form section of $\mathrm{Ad}\,P$ (which is the general formulation), is a 2-form section of the trivial bundle $M \times \mathfrak{u}(1)$ — i.e., an ordinary $\mathfrak{u}(1)$-valued 2-form on $M$. Verification: local field strengths $F_\alpha = dA_\alpha$ agree on overlaps ($F_\beta = F_\alpha$, using abelian gauge transformation + $d^2 = 0$), defining a global $F \in \Omega^2(M; \mathfrak{u}(1))$. ∎
> 
> **Contrast with non-abelian case.** For $G = SU(2)$: $\mathrm{Ad}_g \neq \mathrm{id}$ in general (the adjoint rep of $SU(2)$ is the rotation rep of $SO(3)$ on $\mathfrak{su}(2) \cong \mathbb{R}^3$). For a non-trivial $SU(2)$-bundle, $\mathrm{Ad}\,P$ is a non-trivial rank-3 vector bundle, and the field strength $F \in \Omega^2(M; \mathrm{Ad}\,P)$ is a section of this non-trivial bundle — *not* an ordinary 2-form. The simplification "abelian → trivial adjoint bundle" is genuinely special to abelian gauge theory.

---

# Key Takeaways

**Abelian gauge theory is simpler precisely because the adjoint bundle is trivial.** All the complications of non-abelian gauge theory — the field strength being a section of a non-trivial bundle, the need to choose local trivialisations, the cocycle gluing data — disappear when the structure group is abelian. For $G = U(1)$, the field strength $F$ is a globally defined ordinary 2-form on $M$, and one can work in a *single global gauge* (modulo the freedom of $A \mapsto A + d\chi$). The dramatic simplification of electromagnetism compared to QCD reflects exactly this geometric fact.

**The triviality of $\mathrm{Ad}\,P$ for abelian $G$ has nothing to do with the triviality of $P$ itself.** Even if $P$ is a *non-trivial* $U(1)$-bundle (Hopf bundle, Dirac monopole bundle, any bundle with non-zero first Chern class), the adjoint bundle $\mathrm{Ad}\,P$ is *always* trivial — the non-triviality is in the gauge transition data $c_{\alpha\beta}$, not in the adjoint twisting. This is why the Dirac monopole has a *globally defined* field strength $F$ — even on the non-trivial Hopf bundle, $F$ is a 2-form on $S^2$, not a section of some twisted bundle.

**Trigger-reaction pattern: "adjoint bundle of abelian group" → "trivial line bundle, field strength is global 2-form".** Whenever you encounter the adjoint bundle of an abelian gauge group, immediately conclude triviality. This applies to electromagnetism ($U(1)$), to the gauge bundle of weak hypercharge in the electroweak theory ($U(1)$ component), to any Berry-phase calculation ($U(1)$). The corresponding field strengths are all ordinary 2-forms on the base — globally defined, gauge-invariant in the strong sense that they do not require a trivialisation.

**The non-abelian case is genuinely different: $\mathrm{Ad}\,P$ is non-trivial and the field strength is a bundle section, not a function.** For QCD ($SU(3)$), the colour field strength $G^a_{\mu\nu}$ — for $a = 1, \ldots, 8$ — is *not* a globally defined eight-tuple of ordinary 2-forms; it is a 2-form section of the non-trivial rank-8 adjoint bundle $\mathrm{Ad}\,P_{SU(3)}$, whose global structure depends on the topology of the bundle. The "$F^a$" notation works *only* in a fixed gauge; under change of gauge, the indices $a$ rotate by the adjoint action of the structure group. This is the technical source of difficulty in non-abelian gauge theory and why physicists need formal machinery (BRST, Faddeev-Popov, etc.) to handle non-abelian gauge fixing.
