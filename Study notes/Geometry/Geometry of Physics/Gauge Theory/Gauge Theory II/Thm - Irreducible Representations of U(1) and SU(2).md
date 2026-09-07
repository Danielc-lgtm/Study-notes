---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Representation of a Lie Group"
  - "Ex - SU(2) is Diffeomorphic to S^3"
tags: [gauge-theory, representation-theory, u1, su2]
---

# Prerequisite Concepts

- [[Def - Representation of a Lie Group]]
- [[Ex - SU(2) is Diffeomorphic to S^3]]

# Statement

> [!theorem] Compact rank-one representation classification
> Every finite-dimensional complex representation of $U(1)$ is a direct sum of the characters $\rho_k(z)=z^k$, $k\in\mathbb Z$. Every finite-dimensional complex representation of $SU(2)$ is a direct sum of
> $$V_m=\operatorname{Sym}^m(\mathbb C^2),\qquad m\in\mathbb Z_{\ge0},$$
> and the $V_m$ are pairwise inequivalent irreducibles of dimension $m+1$.

# Why Is It True

Compactness makes representations unitary and therefore completely reducible. For $U(1)$, simultaneous diagonalization reduces everything to characters. For $SU(2)$, differentiation reduces the problem to the highest-weight classification of finite-dimensional $\mathfrak{sl}_2(\mathbb C)$-modules.

# Lemma Decomposition

> [!note]- Lemma 1 — Compact representations are completely reducible
> Average a Hermitian inner product over normalized Haar measure. If $W$ is invariant, its orthogonal complement is invariant because every $\rho(g)$ is unitary. Induction on dimension gives an orthogonal sum of irreducibles.

> [!note]- Lemma 2 — Finite-dimensional irreducible $\mathfrak{sl}_2$-modules are highest-weight modules
> For generators $H,E,F$ with $[H,E]=2E$, $[H,F]=-2F$, $[E,F]=H$, an irreducible module has a vector $v_0$ with $Ev_0=0$ and $Hv_0=mv_0$ for a unique $m\in\mathbb Z_{\ge0}$. The vectors $v_j=F^jv_0$, $0\le j\le m$, form a basis and
> $$Hv_j=(m-2j)v_j,\quad Fv_j=v_{j+1},\quad Ev_j=j(m-j+1)v_{j-1}.$$

# Formal Proof

> [!proof]- Formal Proof
> By Lemma 1 it suffices to classify irreducibles.
>
> For $U(1)$, a unitary representation is a commuting family of normal matrices, hence admits a common orthonormal eigenbasis. On an eigenline it is a continuous character $\chi:U(1)\to U(1)$. Lift $\chi(e^{it})$ through $\mathbb R\to U(1)$ with value $0$ at $t=0$. The homomorphism law and uniqueness of lifts make the lift additive, hence $t\mapsto kt$ for some real $k$. Periodicity at $2\pi$ forces $k\in\mathbb Z$, so $\chi(z)=z^k$.
>
> For $SU(2)$, differentiate a unitary representation and complexify to obtain a representation of $\mathfrak{sl}_2(\mathbb C)$. The standard Cartan generator $H$ is a scalar multiple of a skew-Hermitian infinitesimal generator, so it is diagonalizable. Choose an $H$-eigenvalue maximal in the ordering obtained by repeatedly adding $2$. Applying $E$ raises the $H$-weight by $2$, so maximality yields a nonzero $v_0$ with $Ev_0=0$ and $Hv_0=mv_0$. The commutator relations give by induction
> $$E F^jv_0=j(m-j+1)F^{j-1}v_0.$$
> Finite dimensionality gives a least $r>0$ with $F^rv_0=0$. Applying $E$ shows $r(m-r+1)F^{r-1}v_0=0$, hence $m=r-1\in\mathbb Z_{\ge0}$. Distinct $H$-weights make $v_0,Fv_0,\ldots,F^mv_0$ linearly independent, and their span is stable under $E,F,H$; irreducibility makes it the whole module. This proves Lemma 2 and uniqueness by $m$.
>
> On homogeneous polynomials of degree $m$ in two variables, the differentiated standard action has exactly these formulas, so the module is $\operatorname{Sym}^m(\mathbb C^2)$. Finally, $SU(2)$ is connected and simply connected, so a finite-dimensional Lie-algebra representation integrates uniquely to a group representation; two group representations with the same differential agree. Thus the $V_m$ exhaust the irreducible $SU(2)$ representations. Complete reducibility finishes the proof.

# Rederivation Scaffold

Compactness gives orthogonal complements. Rank one gives a single weight direction. For $SU(2)$, start at the top weight and repeatedly apply the lowering operator until finite dimensionality forces an integer endpoint.

# Unlocked by This

Weight $k$ line bundles explain abelian charge. The modules $V_m$ distinguish integer from half-integer spin and generate the associated spinor and matter bundles used later.
