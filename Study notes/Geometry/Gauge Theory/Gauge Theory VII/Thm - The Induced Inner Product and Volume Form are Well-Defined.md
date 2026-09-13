---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms"
  - "Thm - Determinant is Multiplicative"
  - "Thm - Sylvester's Law of Inertia"
  - "Def - Alternating Tensor and Lambda k V Dual"
  - "Def - Orientation of a Vector Space"
  - "Def - Determinant"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $(V, \langle\cdot,\cdot\rangle)$ is a real vector space of finite dimension $n$ equipped with a non-degenerate symmetric bilinear form $\langle\cdot,\cdot\rangle$, not assumed to be positive definite. Following Bär (Wernli's lecture notes, §3.1), we call such a form an *inner product*, keeping in mind that it may be indefinite; the Lorentzian metric on a tangent space $T_xM$ of spacetime is the case we most want to allow. All the ingredients this page proves well-defined are collected on the companion definition page.

> [!note]- Recall — generalized orthonormal basis, index, induced inner product, volume form
> ![[Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms#The Definition]]

We fix the following symbols, each used with one meaning on the whole page.

- A **generalized orthonormal basis** (generalized ONB) of $V$ is an ordered basis $e_1, \dots, e_n$ with $\langle e_i, e_j\rangle = 0$ for $i \neq j$ and $\langle e_j, e_j\rangle = \epsilon_j \in \{+1, -1\}$. We write $\epsilon = \operatorname{diag}(\epsilon_1, \dots, \epsilon_n)$ for the diagonal matrix of these signs.
- The **index** $p$ of $\langle\cdot,\cdot\rangle$ is the number of indices $j$ with $\epsilon_j = -1$. That this count is the same for every generalized ONB is [[Thm - Sylvester's Law of Inertia|Sylvester's law of inertia]]; the definition page records it, and we invoke it below by name.
- $e^*_1, \dots, e^*_n$ is the **dual basis** of $V^*$, characterised by $e^*_i(e_j) = \delta_{ij}$ (the Kronecker delta, equal to $1$ if $i = j$ and $0$ otherwise).
- For a strictly increasing multi-index $I = (i_1 < \dots < i_k)$ with entries in $\{1, \dots, n\}$ we abbreviate $e^*_I := e^*_{i_1} \wedge \dots \wedge e^*_{i_k} \in \Lambda^k V^*$, and $\epsilon_I := \epsilon_{i_1}\cdots\epsilon_{i_k} \in \{+1,-1\}$.
- The **induced inner product** on $\Lambda^k V^*$ is the bilinear form
$$\langle\omega, \eta\rangle \;:=\; \sum_{i_1 < \dots < i_k} \epsilon_{i_1}\cdots\epsilon_{i_k}\; \omega(e_{i_1}, \dots, e_{i_k})\;\eta(e_{i_1}, \dots, e_{i_k}), \qquad \omega, \eta \in \Lambda^k V^*,$$
written by the same symbol $\langle\cdot,\cdot\rangle$. Its definition names a generalized ONB $e_1, \dots, e_n$; part (i) below is exactly the statement that the number it produces does not remember which one.
- When $V$ carries a chosen orientation, a generalized ONB is **positively oriented** if the ordered basis $e_1, \dots, e_n$ represents that orientation, and the **volume form** is $\mathrm{vol} := e^*_1 \wedge \dots \wedge e^*_n \in \Lambda^n V^*$.

We use throughout the vault's evaluation convention for wedge products of covectors, namely the determinant convention $(\omega^1 \wedge \dots \wedge \omega^k)(v_1, \dots, v_k) = \det\big(\omega^a(v_b)\big)_{a,b=1}^k$ from [[Def - Alternating Tensor and Lambda k V Dual|the exterior power of a dual space]] (no factor of $1/k!$). In this convention a $k$-form $\omega$ is determined by its values $\omega(e_{i_1}, \dots, e_{i_k})$ on increasing tuples of basis vectors, and it is alternating and $k$-linear in its arguments; both facts are used below.

If $e_1, \dots, e_n$ and $f_1, \dots, f_n$ are two generalized ONBs, the **change-of-basis matrix** $A = (A^k_i)$ is defined by $f_i = \sum_{k=1}^n A^k_i\, e_k$; here $A^k_i$ is the entry in row $k$, column $i$, so the $i$-th column of $A$ holds the coordinates of $f_i$ in the basis $e$. We write $A^t$ for the transpose, $(A^t)_{ik} = A^k_i$, and $\epsilon' = \operatorname{diag}(\epsilon'_1, \dots, \epsilon'_n)$ for the sign matrix of the basis $f$, so $\langle f_i, f_j\rangle = \delta_{ij}\epsilon'_j$.

> [!warning] Convention: source transcription
> Bär's printed proof (Lemma 3.1.1) writes the change-of-basis relation as $\epsilon' = A\,\epsilon\, A^{*}$, using $A^{*}$ for the transpose, and mixes the index placements $A^j_i$ and $A^i_l$ within a single computation (a defect flagged in the content map). The correct, index-consistent relation for $f_i = \sum_k A^k_i e_k$ is $A^t \epsilon A = \epsilon'$, and we use that form throughout; the two differ only by which factor is transposed, and produce the same contraction identity once the indices are tracked carefully.

---

# Statement

> **Theorem (well-definedness of the induced inner product and the volume form).** Let $(V, \langle\cdot,\cdot\rangle)$ be an $n$-dimensional real vector space with a non-degenerate symmetric bilinear form, and let $0 \le k \le n$.
>
> **(i) Basis-independence of the induced inner product.** The bilinear form $\langle\cdot,\cdot\rangle$ on $\Lambda^k V^*$ defined by
> $$\langle\omega, \eta\rangle = \sum_{i_1 < \dots < i_k} \epsilon_{i_1}\cdots\epsilon_{i_k}\, \omega(e_{i_1}, \dots, e_{i_k})\,\eta(e_{i_1}, \dots, e_{i_k})$$
> takes the same value for every generalized orthonormal basis $e_1, \dots, e_n$ of $V$.
>
> **(ii) The wedge monomials form a generalized ONB.** For any generalized orthonormal basis $e_1, \dots, e_n$, the family $\{e^*_{i_1} \wedge \dots \wedge e^*_{i_k}\}_{i_1 < \dots < i_k}$ is a generalized orthonormal basis of $\Lambda^k V^*$ for the induced inner product: distinct monomials are orthogonal, and
> $$\langle e^*_{i_1} \wedge \dots \wedge e^*_{i_k},\; e^*_{i_1} \wedge \dots \wedge e^*_{i_k}\rangle = \epsilon_{i_1}\cdots\epsilon_{i_k} \in \{+1, -1\}.$$
> In particular the induced inner product on $\Lambda^k V^*$ is non-degenerate.
>
> **(iii) The volume form.** The space $\Lambda^n V^*$ is one-dimensional, and
> $$\langle e^*_1 \wedge \dots \wedge e^*_n,\; e^*_1 \wedge \dots \wedge e^*_n\rangle = \epsilon_1 \cdots \epsilon_n = (-1)^p,$$
> where $p$ is the index of $\langle\cdot,\cdot\rangle$. Consequently $e^*_1 \wedge \dots \wedge e^*_n$ is determined up to sign independently of the generalized orthonormal basis, and if $V$ is oriented then the top form $\mathrm{vol} = e^*_1 \wedge \dots \wedge e^*_n$ is the same for all positively oriented generalized orthonormal bases; reversing the orientation replaces $\mathrm{vol}$ by $-\mathrm{vol}$.

The three parts are the three constructions the [[Def - Hodge Star in Arbitrary Signature|Hodge star]] rests on. Part (i) says the pairing $\langle\star\omega, \eta\rangle$ that defines the star is meaningful; part (ii) supplies the non-degeneracy that lets the star be recovered from that pairing; part (iii) fixes the single scalar $\mathrm{vol}$ against which the pairing is measured.

---

# Motivation

The Hodge star is defined by a single equation, $\omega \wedge \eta = \langle\star\omega, \eta\rangle\,\mathrm{vol}$, which is asked to hold for all $\eta$. That one equation carries three separate pieces of hidden machinery, and each has to be shown to be a genuine object before the equation can be read as a definition at all. The inner product $\langle\cdot,\cdot\rangle$ on forms has to *be* an inner product — a well-defined bilinear form — rather than a number that depends on a basis nobody canonically chose. It has to be *non-degenerate*, because the whole point of the defining equation is to run it backwards: given the linear functional $\eta \mapsto \omega\wedge\eta$, non-degeneracy is what allows us to represent it by a unique vector $\star\omega$. And $\mathrm{vol}$ has to be a *single* top form determined by the geometry, because the star's output is calibrated against it. This page discharges all three obligations at once.

The subtlety is entirely in the words "generalized orthonormal". In the positive-definite case one may quietly identify all orthonormal bases because the orthogonal group acts transitively on them, and the change-of-basis matrix is a genuine rotation or reflection with determinant $\pm 1$. In indefinite signature — Minkowski space is the case we care about — the relevant symmetry group is the *pseudo*-orthogonal group $O(n-p, p)$, whose matrices satisfy $A^t \epsilon A = \epsilon$ rather than $A^t A = 1$. Two generalized ONBs need not be related by anything as tame as a rotation. What survives, and what makes all three parts true, is the single algebraic fact that a matrix intertwining two diagonal sign patterns still has determinant $\pm 1$ and still contracts correctly against the sign weights $\epsilon_j$. Everything below is an unfolding of that fact.

There is a reason the source only proves part of this. Bär proves part (i) (Lemma 3.1.1) with a computation whose index bookkeeping is inconsistent as printed, states part (ii) as a remark without proof (Remark 3.1.2), and proves part (iii) briefly (Remark 3.1.4) leaning on the sign count $\epsilon_1\cdots\epsilon_n = (-1)^p$. Because the definition page and the existence-and-uniqueness of the star both quote part (ii) — the non-degeneracy of the induced form — a note that omits it would leave the Hodge star resting on an unproved claim. We supply the omitted arguments in full and repair the index placement in part (i).

---

# Sources and Targets

**Sources (Input Broadening).**

The literal hypothesis is mild: any finite-dimensional real space with a non-degenerate symmetric bilinear form. The skill is recognising when a problem hands you such data in disguise.

The first disguised source is **a Riemannian or semi-Riemannian metric evaluated at a point.** A metric $g$ on a smooth manifold is exactly a smoothly varying non-degenerate symmetric bilinear form on each tangent space $T_xM$; a Lorentzian metric is the indefinite case with index $p = 1$ (in the convention $(-,+,+,+)$). So the pointwise version of this theorem is what makes the Hodge star, the codifferential, and the $L^2$ inner product on forms well-defined on every oriented (semi-)Riemannian manifold, not merely on a fixed model space. The non-obvious bridge is that "a metric" is not a single inner product but a field of them, and the theorem must be applied fibrewise with the sign matrix $\epsilon$ allowed to be the Lorentzian one; the index is constant on a connected manifold precisely because it is a discrete invariant that varies continuously. *Example problem:* show that the electromagnetic action $\int_M F \wedge \star F$ on a four-dimensional Lorentzian spacetime is a well-defined real number.

The second disguised source is **a symmetric non-degenerate matrix, presented as a Gram matrix or a quadratic form.** Whenever one is given a symmetric invertible matrix $G$ and told to build an inner product $\langle u, v\rangle = u^t G v$, [[Thm - Diagonalization of a Symmetric Bilinear Form|diagonalisation]] produces a generalized ONB, and this theorem then guarantees that all the exterior-power constructions attached to $G$ are independent of the diagonalising basis chosen. The non-obvious step is that the *induced* form on $\Lambda^k$ depends on $G$ only through the intrinsic pairing, not through the arbitrary orthogonalisation used to compute it. *Example problem:* given the Killing form on a semisimple Lie algebra $\mathfrak{g}$, show that the induced pairing on $\Lambda^k \mathfrak{g}^*$ used to define invariant polynomials does not depend on the basis of $\mathfrak{g}$.

The third disguised source is **any perfect pairing of a space with itself.** A non-degenerate symmetric bilinear form is the same data as an isomorphism $V \xrightarrow{\sim} V^*$ that is its own transpose; problems that begin from such an isomorphism (a symplectic-free "self-dual" structure, a real structure on a complex space, a polarisation) supply the hypothesis without ever saying "inner product". The bridge is that the diagonalisation into $\pm 1$ eigenvalues is available for any such symmetric isomorphism over $\mathbb{R}$. *Example problem:* on the middle cohomology $H^2(X; \mathbb{R})$ of a closed oriented four-manifold, the intersection form is symmetric and non-degenerate (Poincaré duality), so it induces well-defined pairings on its exterior powers, the algebraic shadow of the geometry in chapter XIII.

**Targets (Output Amplification).**

The bare conclusion is that three constructions are well-posed. Combined with further ingredients it does much more.

Combine part (ii) with **a linear functional built from the wedge product.** Non-degeneracy of the induced form on $\Lambda^{n-k}V^*$ is exactly the hypothesis needed to represent the functional $\eta \mapsto (\omega\wedge\eta)/\mathrm{vol}$ by a unique element $\star\omega$; the payoff is the [[Thm - Existence and Uniqueness of the Hodge Star|existence and uniqueness of the Hodge star]], whose proof invokes part (ii) as a named hypothesis. The extra ingredient is the perfectness of the wedge pairing $\Lambda^k \times \Lambda^{n-k} \to \Lambda^n \cong \mathbb{R}$.

Combine part (ii) with **the identity permutation count on a complementary index set.** Once one knows $\langle e^*_I, e^*_I\rangle = \epsilon_I$, the value $\star e^*_I = \epsilon_J\,\operatorname{sign}(IJ)\,e^*_J$ (complementary $J$) follows by a one-line evaluation of the defining relation, and from it the whole table of [[Thm - Properties of the Hodge Star in Arbitrary Signature|properties of the star]] — the double-star sign $\star\star = (-1)^{k(n-k)+p}$, the isometry-up-to-sign $\langle\star\omega,\star\eta\rangle = (-1)^p\langle\omega,\eta\rangle$, the symmetry $\omega\wedge\star\eta = \eta\wedge\star\omega$. The extra ingredient is the shuffle-sign combinatorics.

Combine part (iii) with **an orientation of the manifold and Stokes' theorem.** The sign fact $\langle\mathrm{vol}, \mathrm{vol}\rangle = (-1)^p$ and the basis-independence of $\mathrm{vol}$ are what let one integrate $n$-forms unambiguously; together with an inner product on forms this produces the $L^2$ pairing $(\omega, \eta) \mapsto \int_M \langle\omega,\eta\rangle\,\mathrm{vol}$ underlying the variational formulation of electrodynamics and Yang–Mills theory. The extra ingredient is [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]], which turns the fibrewise algebra of this page into a global functional.

---

# Why Is It True

Strip away the exterior algebra and look at what a change of generalized ONB is. If $e_1, \dots, e_n$ and $f_1, \dots, f_n$ are two of them, the matrix $A$ with $f_i = \sum_k A^k_i e_k$ does not preserve the form $\langle\cdot,\cdot\rangle$ in the ordinary sense; it preserves it *up to relabelling the signs*. Writing the two sign patterns as diagonal matrices $\epsilon$ and $\epsilon'$, the requirement that both bases be generalized orthonormal is precisely the matrix equation $A^t \epsilon A = \epsilon'$. This is the definition of a pseudo-orthogonal matrix, and it is the single seed from which all three parts grow.

> **The one mechanism: the change-of-basis matrix between two generalized orthonormal bases is pseudo-orthogonal, $A^t \epsilon A = \epsilon'$, and pseudo-orthogonal matrices both contract correctly against the sign weights and have determinant $\pm 1$.**

Two consequences drop out of $A^t\epsilon A = \epsilon'$. First, inverting and transposing gives the "dual" relation $A\,\epsilon'\,A^t = \epsilon$, which in components reads $\sum_l A^i_l A^j_l\,\epsilon'_l = \delta_{ij}\epsilon_i$. This is exactly the contraction that appears when you expand the induced-product formula computed in the $f$-basis back into the $e$-basis: each of the $k$ index slots contracts through this identity, the primed signs $\epsilon'$ turn into unprimed signs $\epsilon$, and the sum in the $f$-basis becomes the sum in the $e$-basis. That is part (i): the formula was secretly basis-independent because the sign weights transform exactly as they must to cancel the change of basis.

Second, taking determinants of $A^t\epsilon A = \epsilon'$ gives $(\det A)^2 (-1)^p = (-1)^p$ (the two indices agree by Sylvester's law), so $\det A = \pm 1$. On the top exterior power $\Lambda^n V^*$, which is one-dimensional, the change of basis multiplies the top form by $\det A$; since $\det A = \pm 1$ the top form only changes sign, and an orientation — a rule that $\det A > 0$ for allowed changes — pins the sign. That is part (iii).

Part (ii) needs no pseudo-orthogonality at all: it is a direct evaluation. In the determinant convention a wedge monomial $e^*_I$ takes the value $1$ on the tuple $(e_{i_1}, \dots, e_{i_k})$ and $0$ on every other increasing tuple of basis vectors, so plugging two monomials into the defining sum leaves at most one surviving term, weighted by $\epsilon_I$. Distinct monomials never survive together, so they are orthogonal, and each has self-pairing $\pm 1$. A diagonal $\pm 1$ Gram matrix is invertible, which is non-degeneracy. The intuition is that the induced product was engineered to make the wedge monomials orthonormal-with-signs; part (ii) simply checks that the engineering worked.

---

# What Makes This Hard

The one genuinely error-prone step is the index bookkeeping in part (i): the change-of-basis relation $A^t\epsilon A = \epsilon'$ must be inverted to the contraction identity $\sum_l A^i_l A^j_l\epsilon'_l = \delta_{ij}\epsilon_i$ *with the transposes and the primed-versus-unprimed signs in the right places*, and it is the primed signs that get summed and the unprimed ones that survive, not the reverse. The printed source proof mixes $A^j_i$ and $A^i_l$ and writes $A^{*}$ for the transpose, so it cannot be copied; one has to re-derive the identity carefully, which is why we isolate it as its own lemma. The second common slip is forgetting that the defining sum ranges over *increasing* multi-indices, so that passing to a sum over all ordered tuples introduces a factor $1/k!$ and requires the summand to be permutation-symmetric and to vanish on repeated indices — both true here, but both needing a sentence. The third is treating "orthonormal" as "norm one" in part (iii): in indefinite signature the volume form has $\langle\mathrm{vol}, \mathrm{vol}\rangle = (-1)^p$, which is $-1$ in Lorentzian signature, so $\mathrm{vol}$ is a unit vector only up to the sign of the index.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce everything to the pseudo-orthogonality of the change-of-basis matrix, $A^t\epsilon A = \epsilon'$. From it, derive one contraction identity and one determinant fact. The contraction identity proves part (i) by expanding the induced product computed in one basis into the other. Part (ii) is an independent direct evaluation of the defining sum on wedge monomials. The determinant fact plus one-dimensionality of $\Lambda^n$ proves part (iii).

**Subgoal decomposition:**

1. **Pseudo-orthogonality and its dual.** From $\langle f_i, f_j\rangle = \delta_{ij}\epsilon'_j$ and $f_i = \sum_k A^k_i e_k$, derive $A^t\epsilon A = \epsilon'$, and from it the contraction identity $\sum_l A^i_l A^j_l\epsilon'_l = \delta_{ij}\epsilon_i$.
   - *Hint:* Expand $\langle f_i, f_j\rangle$ bilinearly; then invert $A^t\epsilon A = \epsilon'$ using $\epsilon^2 = \epsilon'^2 = 1$ to get $A\epsilon' A^t = \epsilon$, and read off components.
   - *Why needed:* This identity is the engine of part (i) and the determinant fact of part (iii).

2. **Determinant $\pm 1$.** Show $\det A = \pm 1$ for any change of generalized ONB.
   - *Hint:* Take determinants of $A^t\epsilon A = \epsilon'$ using multiplicativity and $\det A^t = \det A$; use Sylvester's law to equate the two indices, so $\det\epsilon = \det\epsilon'$.
   - *Why needed:* Controls how the top form changes, giving the sign statement in part (iii).

3. **Symmetrisation of the defining sum.** Show $\sum_{i_1 < \dots < i_k} T(i_1, \dots, i_k) = \tfrac{1}{k!}\sum_{i_1, \dots, i_k} T(i_1, \dots, i_k)$ for the induced-product summand $T$.
   - *Hint:* $T$ is symmetric under permuting its indices (two sign flips cancel) and vanishes when two coincide ($\omega$ is alternating).
   - *Why needed:* Lets the change-of-basis contraction act slot by slot in part (i).

4. **Monomial evaluation.** Show $e^*_I(e_{m_1}, \dots, e_{m_k}) = \delta_{IM}$ for increasing multi-indices $I, M$ (equal to $1$ if $I = M$, else $0$).
   - *Hint:* Determinant convention: $e^*_I(e_M) = \det(e^*_{i_a}(e_{m_b})) = \det(\delta_{i_a m_b})$; a repeated or missing index makes a zero row or column.
   - *Why needed:* Collapses the defining sum to one term in part (ii).

5. **Assemble.** Part (i) from subgoals 1, 3; part (ii) from subgoal 4; part (iii) from subgoal 2, one-dimensionality of $\Lambda^n$, and part (ii) at $k = n$.

---

# Lemma Decomposition

> [!note]- Lemma 1: pseudo-orthogonality of the change of basis and the contraction identity
> **Statement:** Let $e_1, \dots, e_n$ and $f_1, \dots, f_n$ be generalized orthonormal bases with sign matrices $\epsilon = \operatorname{diag}(\epsilon_j)$ and $\epsilon' = \operatorname{diag}(\epsilon'_j)$, and let $A = (A^k_i)$ satisfy $f_i = \sum_k A^k_i e_k$. Then $A^t \epsilon A = \epsilon'$, and consequently $A\,\epsilon'\,A^t = \epsilon$, i.e. in components
> $$\sum_{l=1}^n A^i_l\, A^j_l\, \epsilon'_l = \delta_{ij}\,\epsilon_i \qquad \text{for all } i, j.$$
>
> **Hint:** Expand $\langle f_i, f_j\rangle$ by bilinearity to get the first identity; invert using $\epsilon^2 = \epsilon'^2 = 1$.
>
> **Why needed:** The component identity is contracted through every index slot in the proof of part (i), and the matrix identity is where the determinant fact of part (iii) comes from.
>
> > [!note]- Full proof
> > **Deriving $A^t\epsilon A = \epsilon'$.** Fix $i, j$. Since $f$ is a generalized ONB, $\langle f_i, f_j\rangle = \delta_{ij}\epsilon'_j$. Expanding $f_i = \sum_k A^k_i e_k$ and $f_j = \sum_l A^l_j e_l$ and using bilinearity of $\langle\cdot,\cdot\rangle$,
> > $$\langle f_i, f_j\rangle = \sum_{k=1}^n\sum_{l=1}^n A^k_i\, A^l_j\, \langle e_k, e_l\rangle \qquad \text{(bilinearity in both slots).}$$
> > Because $e$ is a generalized ONB, $\langle e_k, e_l\rangle = \delta_{kl}\epsilon_k$, so only the terms with $l = k$ survive:
> > $$\langle f_i, f_j\rangle = \sum_{k=1}^n A^k_i\, A^k_j\, \epsilon_k \qquad \text{(since } \langle e_k, e_l\rangle = \delta_{kl}\epsilon_k\text{).}$$
> > The right-hand side is $\sum_k (A^t)_{ik}\,\epsilon_k\, A^k_j = (A^t\epsilon A)_{ij}$ (definition of matrix product, with $(A^t)_{ik} = A^k_i$ and $\epsilon$ diagonal). Equating with $\langle f_i, f_j\rangle = \delta_{ij}\epsilon'_j = (\epsilon')_{ij}$ gives $(A^t\epsilon A)_{ij} = (\epsilon')_{ij}$ for all $i, j$, that is,
> > $$A^t\epsilon A = \epsilon'. \tag{$\ast$}$$
> >
> > **Inverting to $A\epsilon' A^t = \epsilon$.** Both $\epsilon$ and $\epsilon'$ are diagonal with entries $\pm 1$, so $\epsilon^2 = 1_n$ and $\epsilon'^2 = 1_n$ (the identity matrix). From $(\ast)$, multiply on the left by $(A^t)^{-1}$ (the matrix $A$ is invertible, being a change of basis, so $A^t$ is too):
> > $$\epsilon A = (A^t)^{-1}\epsilon' \qquad \text{(left-multiply } (\ast) \text{ by } (A^t)^{-1}\text{).}$$
> > Multiply on the left by $\epsilon$ and use $\epsilon^2 = 1_n$:
> > $$A = \epsilon\,(A^t)^{-1}\,\epsilon' \qquad \text{(left-multiply by } \epsilon\text{, } \epsilon^2 = 1_n\text{).}$$
> > Now compute $A\epsilon' A^t$, using $\epsilon'^2 = 1_n$ and $(A^t)^{-1}A^t = 1_n$:
> > $$A\epsilon' A^t = \epsilon\,(A^t)^{-1}\,\epsilon'\,\epsilon'\,A^t = \epsilon\,(A^t)^{-1}A^t = \epsilon \qquad \text{(since } \epsilon'\epsilon' = 1_n \text{ and } (A^t)^{-1}A^t = 1_n\text{).}$$
> > **Reading off components.** The $(i,j)$ entry of $A\epsilon' A^t$ is $\sum_l A_{il}\,\epsilon'_l\,(A^t)_{lj} = \sum_l A^i_l\,\epsilon'_l\,A^j_l$ (since $A_{il} = A^i_l$, $(A^t)_{lj} = A^j_l$, and $\epsilon'$ is diagonal). The $(i,j)$ entry of $\epsilon$ is $\delta_{ij}\epsilon_i$. Hence
> > $$\sum_{l=1}^n A^i_l\, A^j_l\, \epsilon'_l = \delta_{ij}\,\epsilon_i. \qquad \blacksquare$$

> [!note]- Lemma 2: a change of generalized orthonormal basis has determinant $\pm 1$
> **Statement:** With the notation of Lemma 1, $\det A = \pm 1$. If moreover $V$ is oriented and both bases are positively oriented, then $\det A = +1$.
>
> **Hint:** Take determinants in $A^t\epsilon A = \epsilon'$; use $\det A^t = \det A$, multiplicativity, and Sylvester's law to see $\det\epsilon = \det\epsilon'$.
>
> **Why needed:** It is exactly the statement that the top form changes only by a sign, which the orientation then fixes; this is part (iii).
>
> > [!note]- Full proof
> > **Transpose invariance of the determinant.** We first record that $\det A^t = \det A$ for any square real matrix. By the Leibniz formula (proved on [[Def - Determinant|the determinant page]]), $\det A = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\prod_{i=1}^n A_{\sigma(i),\,i}$. Applying it to $A^t$ and using $(A^t)_{\sigma(i),i} = A_{i,\sigma(i)}$,
> > $$\det A^t = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\prod_{i=1}^n A_{i,\,\sigma(i)} \qquad \text{(Leibniz formula for } A^t\text{).}$$
> > In each term substitute $j = \sigma(i)$, so the product $\prod_i A_{i,\sigma(i)} = \prod_j A_{\sigma^{-1}(j),\,j}$ (reindexing the factors), and replace the summation variable $\sigma$ by $\tau = \sigma^{-1}$, which ranges over all of $S_n$ as $\sigma$ does; since $\operatorname{sgn}(\sigma) = \operatorname{sgn}(\sigma^{-1}) = \operatorname{sgn}(\tau)$,
> > $$\det A^t = \sum_{\tau \in S_n} \operatorname{sgn}(\tau)\prod_{j=1}^n A_{\tau(j),\,j} = \det A \qquad \text{(reindexing } j = \sigma(i)\text{, } \tau = \sigma^{-1}\text{, } \operatorname{sgn}(\tau) = \operatorname{sgn}(\sigma)\text{).}$$
> >
> > **Determinant of the pseudo-orthogonality relation.** By Lemma 1, $A^t\epsilon A = \epsilon'$. Taking determinants and using that [[Thm - Determinant is Multiplicative|the determinant is multiplicative]] — for square matrices $M, N$ of the same size, $\det(MN) = (\det M)(\det N)$ — twice,
> > $$\det(A^t)\,\det(\epsilon)\,\det(A) = \det(\epsilon') \qquad \text{(multiplicativity of the determinant on } A^t\epsilon A\text{).}$$
> > Using $\det A^t = \det A$ from the previous step, the left side is $(\det A)^2\,\det\epsilon$, so
> > $$(\det A)^2\,\det\epsilon = \det\epsilon'. \tag{$\dagger$}$$
> >
> > **Equating the two determinants of signs.** The matrix $\epsilon = \operatorname{diag}(\epsilon_1, \dots, \epsilon_n)$ is diagonal, so $\det\epsilon = \epsilon_1\cdots\epsilon_n = (-1)^p$, where $p$ is the number of $\epsilon_j$ equal to $-1$, i.e. the index of $\langle\cdot,\cdot\rangle$ read off from the basis $e$. Likewise $\det\epsilon' = (-1)^{p'}$, with $p'$ the index read off from the basis $f$. By [[Thm - Sylvester's Law of Inertia|Sylvester's law of inertia]] — the number of negative diagonal entries in any diagonalisation of a real symmetric bilinear form is an invariant of the form — we have $p' = p$, hence $\det\epsilon' = (-1)^p = \det\epsilon$. Both are nonzero, so $(\dagger)$ gives $(\det A)^2 = 1$, that is,
> > $$\det A = \pm 1.$$
> >
> > **The oriented case.** Two ordered bases of $V$ determine the same orientation if and only if the change-of-basis matrix carrying one to the other has positive determinant; this is the definition of [[Def - Orientation of a Vector Space|orientation of a vector space]]. If $e$ and $f$ are both positively oriented, then $A$ (carrying $e$ to $f$) has $\det A > 0$, and combined with $\det A = \pm 1$ this forces $\det A = +1$. $\blacksquare$

> [!note]- Lemma 3: passing from an increasing sum to an unrestricted sum
> **Statement:** For fixed $\omega, \eta \in \Lambda^k V^*$ and a generalized ONB $e_1, \dots, e_n$, write $T(i_1, \dots, i_k) := \epsilon_{i_1}\cdots\epsilon_{i_k}\,\omega(e_{i_1}, \dots, e_{i_k})\,\eta(e_{i_1}, \dots, e_{i_k})$. Then
> $$\sum_{i_1 < \dots < i_k} T(i_1, \dots, i_k) = \frac{1}{k!}\sum_{i_1, \dots, i_k = 1}^n T(i_1, \dots, i_k),$$
> where the right-hand sum ranges over all ordered $k$-tuples.
>
> **Hint:** $T$ is invariant under permuting its arguments and vanishes when two of them coincide.
>
> **Why needed:** The change-of-basis substitution in part (i) is done on the unrestricted sum, where each index runs independently; this lemma converts between the two forms of the sum at the start and the end.
>
> > [!note]- Full proof
> > **Permutation symmetry.** Let $\pi \in S_k$ be a permutation of the $k$ argument slots. Since $\omega$ is alternating, $\omega(e_{i_{\pi(1)}}, \dots, e_{i_{\pi(k)}}) = \operatorname{sgn}(\pi)\,\omega(e_{i_1}, \dots, e_{i_k})$, and identically for $\eta$. Their product therefore picks up $\operatorname{sgn}(\pi)^2 = 1$. The sign factor $\epsilon_{i_1}\cdots\epsilon_{i_k}$ is a product over the same set of indices and so is unchanged by $\pi$. Hence $T(i_{\pi(1)}, \dots, i_{\pi(k)}) = T(i_1, \dots, i_k)$: the summand $T$ is symmetric in its $k$ arguments.
> >
> > **Vanishing on repeats.** If two arguments coincide, say $i_a = i_b$ with $a \neq b$, then $\omega(e_{i_1}, \dots, e_{i_k}) = 0$ because $\omega$ is alternating (an alternating form vanishes on a tuple with a repeated entry), so $T(i_1, \dots, i_k) = 0$.
> >
> > **Counting.** In the unrestricted sum $\sum_{i_1, \dots, i_k}$, the tuples with a repeated index contribute $0$ by the previous paragraph. Each tuple with $k$ distinct entries is a permutation of a unique strictly increasing tuple $(i_1 < \dots < i_k)$, and there are exactly $k!$ such permutations, each contributing the same value of $T$ by permutation symmetry. Therefore
> > $$\sum_{i_1, \dots, i_k = 1}^n T(i_1, \dots, i_k) = \sum_{i_1 < \dots < i_k} k!\, T(i_1, \dots, i_k) = k! \sum_{i_1 < \dots < i_k} T(i_1, \dots, i_k),$$
> > and dividing by $k!$ gives the claim. $\blacksquare$

> [!note]- Lemma 4: evaluation of wedge monomials on basis tuples
> **Statement:** For strictly increasing multi-indices $I = (i_1 < \dots < i_k)$ and $M = (m_1 < \dots < m_k)$ in $\{1, \dots, n\}$,
> $$e^*_I(e_{m_1}, \dots, e_{m_k}) = \delta_{IM} := \begin{cases} 1 & I = M, \\ 0 & I \neq M. \end{cases}$$
>
> **Hint:** In the determinant convention $e^*_I(e_M) = \det(\delta_{i_a m_b})$; a mismatched index leaves a zero row or column.
>
> **Why needed:** It collapses the defining sum to a single surviving term in part (ii).
>
> > [!note]- Full proof
> > By the determinant convention for the wedge product of covectors on [[Def - Alternating Tensor and Lambda k V Dual|the exterior power]], for any covectors $\omega^1, \dots, \omega^k$ and vectors $v_1, \dots, v_k$ one has $(\omega^1\wedge\dots\wedge\omega^k)(v_1, \dots, v_k) = \det\big(\omega^a(v_b)\big)_{a,b=1}^k$. Applying this with $\omega^a = e^*_{i_a}$ and $v_b = e_{m_b}$, and using $e^*_{i_a}(e_{m_b}) = \delta_{i_a m_b}$,
> > $$e^*_I(e_{m_1}, \dots, e_{m_k}) = \det\big(\delta_{i_a m_b}\big)_{a, b = 1}^k.$$
> > If $I = M$, then $\delta_{i_a m_b} = \delta_{ab}$ (because both are increasing, $i_a = m_a$ for each $a$, and $i_a = m_b \iff a = b$), so the matrix is the $k \times k$ identity and its determinant is $1$. If $I \neq M$, then, both being increasing, there is an index value that appears in one of $I, M$ but not the other; say $i_a \notin M$ for some $a$. Then the $a$-th row $(\delta_{i_a m_1}, \dots, \delta_{i_a m_k})$ is identically zero, since $i_a \neq m_b$ for every $b$, and a matrix with a zero row has determinant $0$. (Symmetrically, if some $m_b \notin I$ the $b$-th column is zero.) Hence $e^*_I(e_M) = \delta_{IM}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $(V, \langle\cdot,\cdot\rangle)$ be an $n$-dimensional real vector space with a non-degenerate symmetric bilinear form and fix $0 \le k \le n$. We prove the three parts in turn.
>
> **Part I — basis-independence of the induced inner product (part (i)).**
>
> **Step 0 — set-up.** Let $e_1, \dots, e_n$ and $f_1, \dots, f_n$ be two generalized orthonormal bases, with sign matrices $\epsilon = \operatorname{diag}(\epsilon_j)$ and $\epsilon' = \operatorname{diag}(\epsilon'_j)$ respectively, and let $A = (A^k_i)$ be the change-of-basis matrix, $f_i = \sum_k A^k_i e_k$. Fix $\omega, \eta \in \Lambda^k V^*$. Write $\langle\omega, \eta\rangle_e$ and $\langle\omega, \eta\rangle_f$ for the value of the defining sum computed in the basis $e$ and in the basis $f$ respectively; we must show $\langle\omega, \eta\rangle_f = \langle\omega, \eta\rangle_e$.
>
> **Step 1 — pass to the unrestricted sum.** By Lemma 3 applied to the summand $T'(i_1, \dots, i_k) = \epsilon'_{i_1}\cdots\epsilon'_{i_k}\,\omega(f_{i_1}, \dots, f_{i_k})\,\eta(f_{i_1}, \dots, f_{i_k})$ in the $f$-basis,
> $$\langle\omega, \eta\rangle_f = \sum_{i_1 < \dots < i_k} T'(i_1, \dots, i_k) = \frac{1}{k!}\sum_{i_1, \dots, i_k = 1}^n \epsilon'_{i_1}\cdots\epsilon'_{i_k}\,\omega(f_{i_1}, \dots, f_{i_k})\,\eta(f_{i_1}, \dots, f_{i_k}) \qquad \text{(by Lemma 3).}$$
>
> **Step 2 — expand each $f$ in the $e$-basis.** By multilinearity of the alternating $k$-forms $\omega$ and $\eta$, and $f_{i} = \sum_j A^j_{i}e_j$,
> $$\omega(f_{i_1}, \dots, f_{i_k}) = \sum_{j_1, \dots, j_k = 1}^n A^{j_1}_{i_1}\cdots A^{j_k}_{i_k}\,\omega(e_{j_1}, \dots, e_{j_k}) \qquad \text{(}k\text{-linearity of } \omega\text{),}$$
> $$\eta(f_{i_1}, \dots, f_{i_k}) = \sum_{l_1, \dots, l_k = 1}^n A^{l_1}_{i_1}\cdots A^{l_k}_{i_k}\,\eta(e_{l_1}, \dots, e_{l_k}) \qquad \text{(}k\text{-linearity of } \eta\text{).}$$
> Substituting both into the unrestricted sum of Step 1 and collecting all the factors that carry a given summation index $i_m$,
> $$\langle\omega, \eta\rangle_f = \frac{1}{k!}\sum_{\substack{j_1, \dots, j_k \\ l_1, \dots, l_k}} \left[\prod_{m=1}^k\Big(\sum_{i_m = 1}^n \epsilon'_{i_m}\,A^{j_m}_{i_m}\,A^{l_m}_{i_m}\Big)\right]\omega(e_{j_1}, \dots, e_{j_k})\,\eta(e_{l_1}, \dots, e_{l_k}),$$
> where we used that the $k$ inner summations over $i_1, \dots, i_k$ are independent, so the total sum factors into a product of $k$ separate sums, one per slot (distributivity).
>
> **Step 3 — contract each slot by Lemma 1.** By the contraction identity of Lemma 1, for each slot $m$,
> $$\sum_{i_m = 1}^n \epsilon'_{i_m}\,A^{j_m}_{i_m}\,A^{l_m}_{i_m} = \delta_{j_m l_m}\,\epsilon_{j_m} \qquad \text{(by Lemma 1, with } (i, j, l) = (j_m, l_m, i_m)\text{).}$$
> The product over $m$ is therefore $\prod_{m=1}^k \delta_{j_m l_m}\epsilon_{j_m}$, which vanishes unless $l_m = j_m$ for every $m$, and then equals $\epsilon_{j_1}\cdots\epsilon_{j_k}$. The sum over $l_1, \dots, l_k$ thus collapses to its terms with $l_m = j_m$:
> $$\langle\omega, \eta\rangle_f = \frac{1}{k!}\sum_{j_1, \dots, j_k = 1}^n \epsilon_{j_1}\cdots\epsilon_{j_k}\,\omega(e_{j_1}, \dots, e_{j_k})\,\eta(e_{j_1}, \dots, e_{j_k}) \qquad \text{(collapsing } l_m = j_m\text{).}$$
>
> **Step 4 — return to the increasing sum.** The right-hand side of Step 3 is $\tfrac{1}{k!}\sum_{j_1, \dots, j_k} T(j_1, \dots, j_k)$ with $T$ the $e$-basis summand of Lemma 3, so by Lemma 3 (read from right to left),
> $$\langle\omega, \eta\rangle_f = \sum_{j_1 < \dots < j_k} \epsilon_{j_1}\cdots\epsilon_{j_k}\,\omega(e_{j_1}, \dots, e_{j_k})\,\eta(e_{j_1}, \dots, e_{j_k}) = \langle\omega, \eta\rangle_e \qquad \text{(by Lemma 3).}$$
> Since $\omega, \eta$ were arbitrary, the induced inner product computed in the basis $f$ agrees with the one computed in the basis $e$. This proves part (i).
>
> **Part II — the wedge monomials form a generalized ONB (part (ii)).**
>
> **Step 0 — the family is a basis of $\Lambda^k V^*$.** For a fixed generalized ONB $e_1, \dots, e_n$ with dual basis $e^*_1, \dots, e^*_n$, the family $\{e^*_I\}_{I}$ over strictly increasing multi-indices $I = (i_1 < \dots < i_k)$ is the standard basis of $\Lambda^k V^*$, and there are $\binom{n}{k} = \dim\Lambda^k V^*$ of them; this is the basis statement on [[Def - Alternating Tensor and Lambda k V Dual|the exterior power page]]. It remains to compute the induced pairing on this basis.
>
> **Step 1 — evaluate the defining sum on two monomials.** Let $I = (i_1 < \dots < i_k)$ and $J = (j_1 < \dots < j_k)$ be increasing multi-indices. By the definition of the induced inner product (which is legitimate by part (i)),
> $$\langle e^*_I, e^*_J\rangle = \sum_{m_1 < \dots < m_k} \epsilon_{m_1}\cdots\epsilon_{m_k}\; e^*_I(e_{m_1}, \dots, e_{m_k})\; e^*_J(e_{m_1}, \dots, e_{m_k}).$$
> By Lemma 4, $e^*_I(e_{m_1}, \dots, e_{m_k}) = \delta_{IM}$ and $e^*_J(e_{m_1}, \dots, e_{m_k}) = \delta_{JM}$, where $M = (m_1 < \dots < m_k)$ is the summation multi-index. The product $\delta_{IM}\delta_{JM}$ is nonzero only when $M = I$ and $M = J$ simultaneously, which requires $I = J$; and then $M = I$ contributes the single term $\epsilon_{i_1}\cdots\epsilon_{i_k}$. Hence
> $$\langle e^*_I, e^*_J\rangle = \begin{cases} \epsilon_{i_1}\cdots\epsilon_{i_k} & I = J, \\ 0 & I \neq J \end{cases} \qquad \text{(by Lemma 4).}$$
>
> **Step 2 — conclude generalized orthonormality and non-degeneracy.** Distinct basis monomials are orthogonal, and each satisfies $\langle e^*_I, e^*_I\rangle = \epsilon_{i_1}\cdots\epsilon_{i_k} \in \{+1, -1\}$ because each $\epsilon_{i_a} = \pm 1$; so $\{e^*_I\}_I$ is a generalized orthonormal basis of $\Lambda^k V^*$. The Gram matrix of the induced inner product in this basis is diagonal with entries $\pm 1$, hence invertible (its determinant is $\pm 1 \neq 0$); a bilinear form with an invertible Gram matrix in some basis is non-degenerate. Therefore the induced inner product on $\Lambda^k V^*$ is non-degenerate. This proves part (ii).
>
> **Part III — the volume form (part (iii)).**
>
> **Step 0 — one-dimensionality.** Taking $k = n$, $\dim\Lambda^n V^* = \binom{n}{n} = 1$; this is the top-degree case of the dimension count on [[Def - Alternating Tensor and Lambda k V Dual|the exterior power page]]. The only increasing multi-index is $(1, 2, \dots, n)$, and $e^*_1 \wedge \dots \wedge e^*_n$ spans $\Lambda^n V^*$.
>
> **Step 1 — the self-pairing of the top monomial.** Applying part (ii) with $k = n$ and $I = (1, \dots, n)$,
> $$\langle e^*_1 \wedge \dots \wedge e^*_n,\; e^*_1 \wedge \dots \wedge e^*_n\rangle = \epsilon_1\cdots\epsilon_n = (-1)^p \qquad \text{(part (ii); } p \text{ of the } \epsilon_j \text{ equal } -1\text{),}$$
> where $p$ is the index of $\langle\cdot,\cdot\rangle$, well-defined by [[Thm - Sylvester's Law of Inertia|Sylvester's law]].
>
> **Step 2 — the top monomial is determined up to sign, independently of the basis.** Let $e_1, \dots, e_n$ and $f_1, \dots, f_n$ be two generalized orthonormal bases with change-of-basis matrix $A$, $f_i = \sum_k A^k_i e_k$. Write $\mathrm{vol}_e := e^*_1 \wedge \dots \wedge e^*_n$ and $\mathrm{vol}_f := f^*_1 \wedge \dots \wedge f^*_n$; both lie in the one-dimensional space $\Lambda^n V^*$, so $\mathrm{vol}_e = c\,\mathrm{vol}_f$ for a unique scalar $c \in \mathbb{R}$. To find $c$, evaluate both sides on the tuple $(f_1, \dots, f_n)$. On the right, by Lemma 4 with $k = n$ (applied in the $f$-basis), $\mathrm{vol}_f(f_1, \dots, f_n) = 1$, so the right side is $c$. On the left, by the determinant convention on [[Def - Alternating Tensor and Lambda k V Dual|the exterior power page]] together with $e^*_a(f_b) = e^*_a\big(\sum_r A^r_b e_r\big) = A^a_b$,
> $$\mathrm{vol}_e(f_1, \dots, f_n) = \det\big(e^*_a(f_b)\big)_{a, b = 1}^n = \det\big(A^a_b\big) = \det A \qquad \text{(determinant convention; } e^*_a(f_b) = A^a_b\text{).}$$
> Hence $c = \det A$, that is, $\mathrm{vol}_e = (\det A)\,\mathrm{vol}_f$. By Lemma 2, $\det A = \pm 1$, so $\mathrm{vol}_e = \pm\,\mathrm{vol}_f$: the top monomial is the same for the two bases up to sign, and this holds for every pair of generalized orthonormal bases. Therefore $e^*_1 \wedge \dots \wedge e^*_n$ is determined up to sign independently of the generalized orthonormal basis, as claimed.
>
> **Step 3 — the orientation fixes the sign.** Suppose now $V$ is oriented and both $e$ and $f$ are positively oriented generalized orthonormal bases. By the oriented case of Lemma 2, $\det A = +1$, so Step 2 gives $\mathrm{vol}_e = \mathrm{vol}_f$: the top form $\mathrm{vol} = e^*_1 \wedge \dots \wedge e^*_n$ is the same for all positively oriented generalized orthonormal bases, and is therefore a well-defined element of $\Lambda^n V^*$. If one replaces the orientation of $V$ by its opposite, a formerly positively oriented basis becomes negatively oriented; a positively oriented basis for the reversed orientation is obtained from a positively oriented basis for the original orientation by a change of basis $A$ with $\det A < 0$, hence $\det A = -1$ by Lemma 2, so by Step 2 the volume form is negated, $\mathrm{vol} \mapsto -\mathrm{vol}$. This proves part (iii).
>
> **Conclusion.** The induced inner product on $\Lambda^k V^*$ is independent of the generalized orthonormal basis (Part I), the wedge monomials form a generalized orthonormal basis for it so that it is non-degenerate (Part II), and the top form $e^*_1 \wedge \dots \wedge e^*_n$ has self-pairing $(-1)^p$ and is fixed by the orientation (Part III). All three ingredients of the Hodge star are therefore well-defined. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Special relativity: the invariance of the spacetime volume element.** On Minkowski space $\mathbb{R}^{1,3}$ with the metric of index $p = 1$, part (iii) says the four-form $\mathrm{vol} = dt \wedge dx \wedge dy \wedge dz$ is the same for every positively oriented generalized orthonormal frame, and in particular is unchanged under any proper orthochronous Lorentz transformation, since those are exactly the changes of frame with $\det A = +1$ preserving the time orientation. The theorem applies because a Lorentz frame *is* a generalized ONB with $\epsilon = \operatorname{diag}(-1, 1, 1, 1)$; the point that is non-obvious to a physicist meeting it first as "$d^4x$ is Lorentz invariant" is that the invariance is the special case $\det \Lambda = 1$ of Lemma 2, and that the self-pairing $\langle\mathrm{vol}, \mathrm{vol}\rangle = -1$ (not $+1$) is what forces the minus signs in the Lorentzian Hodge star.

**Lie theory: basis-independence of Chern–Weil integrands.** For a compact Lie group $G$ with Lie algebra $\mathfrak{g}$ carrying an $\operatorname{Ad}$-invariant non-degenerate form (for a semisimple group, the Killing form or its negative), the induced inner product on $\Lambda^k\mathfrak{g}^*$ underlies the pairing used to form $|F|^2$ and other invariant integrands in Yang–Mills theory. Part (i) applied fibrewise guarantees that these integrands do not depend on the frame chosen to trivialise the adjoint bundle. The theorem applies because the invariant form is non-degenerate and symmetric; the non-obvious content is that even when the form is indefinite (as it is for non-compact real forms), the construction still goes through, so the same machinery handles both the compact and split real forms.

**Algebraic topology: pairings on the exterior powers of the intersection form.** On $H^2(X; \mathbb{R})$ for a closed oriented four-manifold, the intersection form is symmetric and non-degenerate by Poincaré duality, and its index (the number of negative eigenvalues) is the invariant $b_2^-$. Part (ii) shows that a diagonalising basis produces an explicit generalized ONB of each $\Lambda^k$, and part (iii) that the top exterior power has self-pairing $(-1)^{b_2^-}$. This is a purely algebraic warm-up for chapter XIII; it is non-obvious because "orthonormal basis" over an indefinite form is not a basis of unit vectors but a basis of $\pm$-unit vectors, and the sign count is exactly the topological invariant that Donaldson's theorem constrains.

---

# Bridges

- **[[Thm - Existence and Uniqueness of the Hodge Star|Existence and uniqueness of the Hodge star]]** — the immediate consumer. That result fixes $\omega \in \Lambda^k V^*$, forms the linear functional $\eta \mapsto (\omega\wedge\eta)/\mathrm{vol}$ on $\Lambda^{n-k}V^*$, and represents it by a unique vector $\star\omega$ using non-degeneracy of the induced inner product on $\Lambda^{n-k}V^*$. That non-degeneracy is precisely part (ii) of this page, invoked there as a named hypothesis; the division by $\mathrm{vol}$ is meaningful because $\mathrm{vol}$ is the single well-defined generator of $\Lambda^n V^*$ from part (iii).

- **[[Def - Hodge Star in Arbitrary Signature|The Hodge star in arbitrary signature]]** — the definition this page makes well-posed. Its defining relation $\omega\wedge\eta = \langle\star\omega, \eta\rangle\,\mathrm{vol}$ names all three objects proved well-defined here; without this page the relation would depend on an arbitrary choice of generalized ONB and would not define anything.

- **[[Thm - Properties of the Hodge Star in Arbitrary Signature|Properties of the Hodge star]]** — the downstream calculus. Part (ii)'s value $\langle e^*_I, e^*_I\rangle = \epsilon_I$ is the input to the computation $\star e^*_I = \epsilon_J\,\operatorname{sign}(IJ)\,e^*_J$, from which the double-star sign, the isometry-up-to-index, and the pairing symmetry all follow. The mechanism there — a shuffle sign times a product of $\epsilon$'s over a complementary index set — reuses the sign counting of part (iii).

- **[[Thm - Sylvester's Law of Inertia|Sylvester's law of inertia]]** — the invariant that makes the index $p$ meaningful. It is what allows Lemma 2 to equate $\det\epsilon = \det\epsilon'$ across two bases, and what makes $(-1)^p$ in part (iii) an invariant of the form rather than of a basis. The construction runs: diagonalise the form (producing a generalized ONB), read off the number of negative signs, and invoke Sylvester to see this number is basis-independent.

- **The $L^2$ inner product on forms over a manifold** — the global bridge. Applying this page fibrewise on an oriented (semi-)Riemannian manifold $M$ makes $\langle\omega, \eta\rangle_x$ a well-defined function of $x$ and $\mathrm{vol}$ a well-defined top form, so that $(\omega, \eta) \mapsto \int_M \langle\omega, \eta\rangle\,\mathrm{vol}$ is unambiguous; this is the pairing in which the Hodge codifferential is the adjoint of $d$ and in which the electromagnetic and Yang–Mills actions are written. The construction is: take the pointwise induced product from this page, multiply by the pointwise volume form, and integrate.

---

# Unlocked by This

> [!tip] The Hodge star in indefinite signature *(from Semi-Riemannian Geometry)*
> With the induced inner product and volume form now well-defined for any non-degenerate symmetric form, the Hodge star $\star : \Lambda^k V^* \to \Lambda^{n-k} V^*$ exists on Lorentzian tangent spaces, and with it the Maxwell equations become the two coordinate-free statements $dF = 0$ and $d\star F = \star J$. See **Def - Hodge Star in Arbitrary Signature** and §7.2.

> [!tip] The self-dual/anti-self-dual splitting *(from Four-Dimensional Gauge Theory)*
> In dimension four with $p = 0$, part (ii) gives $\star$ as an isometry with $\star\star = 1$ on $\Lambda^2 V^*$, whose $\pm 1$ eigenspaces $\Lambda^2_\pm$ split the two-forms orthogonally into two three-dimensional pieces. This splitting is the algebraic basis of instantons and of the Seiberg–Witten equations. See **Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions**.
