# Pass 1 Content Map — "Mathematical Gauge Theory" lecture notes

**Source file:** `scratchpad/wernli.txt` (plain-text extraction, 155 PDF pages).

**Identity of the source (important).** The extracted text is **not** by Konstantin Wernli. Title page (PDF p. 1): *Christian Bär, "Gauge Theory", Summer Term 2009, Version of July 26, 2011, Geometrie in Potsdam*; the Preface (PDF p. 5) is signed "Potsdam, February 2011, Christian Bär" and credits Christian Becker with the first draft and the figures. The chapter/section numbering coincides exactly with the structure requested in the task (Preface; 1.1–1.5; 2.1–2.7; 3.1–3.3; 4.1–4.3; 5.1–5.3), so the inventory below follows it. Item numbers in the source are Bär's (e.g. "Definition 2.3.1"); inventory item numbers are ours (D/T/E/X/R/I + section).

**Page convention.** All page references below are **PDF page numbers** (PDF page $=$ printed page $+ 6$; e.g. printed p. 1 is PDF p. 7, printed p. 138 is PDF p. 144).

**Global notation established in the source (used throughout).**
- $\mathbb K \in \{\mathbb R, \mathbb C\}$; $\mathrm{Mat}(n\times n;\mathbb K)$; $1_n$ the identity matrix; $A^t$ transpose, $\bar A$ entrywise conjugate, $A^* := (\bar A)^t$.
- $\mathfrak X(M)$ smooth vector fields on $M$; $\Omega^k(M;V)$ $V$-valued $k$-forms.
- Lie group actions on a **principal bundle are right actions**; Lie algebra $\mathfrak g$ is **left-invariant** vector fields $\cong T_eG$.
- Exterior derivative convention (no $\tfrac{1}{k+1}$ factors): $d\omega(X,Y) = \partial_X\omega(Y) - \partial_Y\omega(X) - \omega([X,Y])$ for 1-forms, and $d\eta(X_1,X_2,X_3) = \partial_{X_1}\eta(X_2,X_3) - \partial_{X_2}\eta(X_1,X_3) + \partial_{X_3}\eta(X_1,X_2) - \eta([X_1,X_2],X_3) + \eta([X_1,X_3],X_2) - \eta([X_2,X_3],X_1)$ for 2-forms (PDF pp. 55, 57).
- Bracket of $\mathfrak g$-valued 1-forms: $[\eta,\varphi](X,Y) := [\eta(X),\varphi(Y)] - [\eta(Y),\varphi(X)]$, so $[\omega,\omega](X,Y) = 2[\omega(X),\omega(Y)]$.
- **Curvature:** $\Omega = d\omega + \tfrac12[\omega,\omega]$ (Prop. 2.4.2). For matrix groups this equals $d\omega + \omega\wedge\omega$.
- **Hodge star** defined by $\omega\wedge\eta = \langle *\omega,\eta\rangle\,\mathrm{vol}$ for $\omega\in\Lambda^kV^*$, $\eta\in\Lambda^{n-k}V^*$ (Lemma 3.1.5); index $p$ := number of $-1$'s among the $\epsilon_j$; $**=(-1)^{k(n-k)+p}$.
- **Lorentzian signature** in §3.2 is $(-,+,+,+)$: $\langle\partial_t,\partial_t\rangle<0$, spatial directions positive; units $c=1$, test particle of mass 1 and charge 1.
- **Intersection form** $Q_X([S_1],[S_2]) := S_1\cdot S_2 = \sum_{p\in S_1\cap S_2}\varepsilon(p)$, $\varepsilon(p)=+1$ iff the orientation of $T_pS_1\oplus T_pS_2$ agrees with that of $T_pX$; **unimodular** means $\det(Q(e_i,e_j)) = \pm1$; $\overline{X}$ denotes $X$ with reversed orientation and $Q_{\overline X} = -Q_X$.

**Equation-number index (source numbering → content).** (1.1)–(1.4) $SO(2)$ constraints; (1.5) $dF([X,Y]) = [dF(X),dF(Y)]$; (1.6) $\gamma_X(t)=\exp(tX)$; (1.7) $e^X=\sum X^k/k!$; (2.1) coboundary $g_{\alpha\beta} = h_\alpha\tilde g_{\alpha\beta}h_\beta^{-1}$; (2.2)/(2.3) transformation of local connection forms; (2.4) structure equation; (2.5) $R_g^*\Omega = \mathrm{Ad}_{g^{-1}}\Omega$; (2.6) $d\Omega=0$ (abelian); (2.7) local structure equation; (2.8) naturality of $c_\lambda$; (2.9) horizontal-lift ODE; (2.10) $\dot v=-Av$; (2.11)/(2.12) Dyson series and product formula; (2.13)/(2.14) path-ordered exponential; (2.15) holonomy expansion; (3.1) defining relation of $*$; (3.2)–(3.6) properties of $*$; (3.7) Gauss; (3.8) Faraday; (3.9) Coulomb; (3.10) Ampère; (3.11) continuity; (3.12) equation of motion; (3.13) Lorentz force; (3.14) total action; (3.15) Einstein equations; (3.16) divergence of $T$; (3.17) Poynting's theorem; (3.18) Yang–Mills bound; (4.1) long exact homotopy sequence; (4.2) $H_*(\mathbb{CP}^n)$; (5.1) unimodularity; (5.2) additivity of signature; (5.3) $E_8$ matrix.

---

## Preface

`PDF pages: 5` (Contents on PDF p. 3; title page PDF p. 1.)

**Content.** Lecture notes of an introductory course on gauge theory at Potsdam University, 2009. Aim: develop the mathematical underpinnings of gauge theory (bundle theory, characteristic classes) and give applications in physics (electrodynamics, Yang–Mills fields) and mathematics (theory of 4-manifolds). Introductory chapters on Lie groups and algebraic topology keep prerequisites minimal; basic differential-geometric notions (manifolds) are assumed known. Christian Becker wrote the first draft and produced most of the pstricks figures. Signed Potsdam, February 2011, Christian Bär.

**Chapter list (Contents, PDF p. 3):** 1 Lie groups and Lie algebras (1.1 Lie groups, 1.2 Lie algebras, 1.3 Representations, 1.4 The exponential map, 1.5 Group actions); 2 Bundle theory (2.1 Fiber bundles, 2.2 Principal bundles, 2.3 Connections, 2.4 Curvature, 2.5 Characteristic classes, 2.6 Parallel transport, 2.7 Gauge transformations); 3 Applications to Physics (3.1 The Hodge-star operator, 3.2 Electrodynamics, 3.3 Yang–Mills fields); 4 Algebraic Topology (4.1 Homotopy theory, 4.2 Homology theory, 4.3 Orientations and the fundamental class); 5 4-dimensional Manifolds (5.1 The intersection form, 5.2 Classification results, 5.3 Donaldson's theorem). Index on PDF pp. 151–155.

---

# Chapter 1 — Lie groups and Lie algebras

## 1.1 Lie groups

`PDF pages: 7–9`

### Standing conventions and notation
- $G\times G\to G$, $(g_1,g_2)\mapsto g_1\cdot g_2$ and $G\to G$, $g\mapsto g^{-1}$ are the structure maps.
- $GL(n;\mathbb R)$ is regarded as an open subset of $\mathrm{Mat}(n\times n;\mathbb R) = \mathbb R^{n^2}$; $GL(n;\mathbb C)\subset\mathbb C^{n^2} = \mathbb R^{2n^2}$ (source writes $\mathbb R^{(2n)^2}$, a typo).
- $A^* := (\bar A)^t$.

### Definitions
- **D1.1.1 — Def - Lie Group** (Def. 1.1.1, p. 7). A differentiable manifold $G$ which is at the same time a group is a *Lie group* iff the maps $G\times G\to G$, $(g_1,g_2)\mapsto g_1\cdot g_2$ and $G\to G$, $g\mapsto g^{-1}$ are smooth.
- **D1.1.2 — Def - Classical Matrix Groups** (Ex. 1.1.2, 1.1.4, pp. 7–8). $GL(n;\mathbb R) := \{A\in\mathrm{Mat}(n\times n;\mathbb R)\mid \det A\neq0\}$; $GL(n;\mathbb C)$ likewise. $O(n) := \{A\in GL(n;\mathbb R)\mid A^tA = 1_n\}$ (orthogonal group); $SL(n;\mathbb R) := \{A\in\mathrm{Mat}(n\times n;\mathbb R)\mid\det A = 1\}$ (special linear group); $SO(n) := O(n)\cap SL(n;\mathbb R)$ (special orthogonal group); $U(n) := \{A\in\mathrm{Mat}(n\times n;\mathbb C)\mid A^*A = 1\}$ (unitary group); $SL(n;\mathbb C) := \{A\in\mathrm{Mat}(n\times n;\mathbb C)\mid\det A = 1\}$ (source item 5 misprints this as $SL(n;\mathbb R)$); $SU(n) := U(n)\cap SL(n;\mathbb C)$ (special unitary group).
- **D1.1.3 — Def - Product Lie Group** (Ex. 1.1.5, p. 8). For Lie groups $G,G'$, $G\times G'$ is a Lie group with $(g_1,g_1')\cdot(g_2,g_2') := (g_1g_2, g_1'g_2')$ and $(g,g')^{-1} := (g^{-1},g'^{-1})$.
- **D1.1.4 — Def - Lie Group Homomorphism** (Def. 1.1.7, p. 8). A smooth group homomorphism $\varphi: G\to H$ between Lie groups is a *homomorphism of Lie groups*; it is an *isomorphism of Lie groups* if invertible with inverse again a Lie group homomorphism; then $G,H$ are *isomorphic as Lie groups*.

### Theorems
- **T1.1.1 — Thm - Closed Subgroup Theorem** (Thm. 1.1.3, p. 7). Let $G$ be a Lie group and $H\subset G$ an (algebraic) subgroup which is closed as a subset. Then $H\subset G$ is a submanifold and a Lie group in its own right. `Proof in source: omitted/cited (no reference given; stated without proof).`
- **T1.1.2 — Thm - SO(2) Is Isomorphic to U(1)** (Ex. 1.1.8, p. 9). $SO(2) = \left\{\begin{pmatrix}\cos\varphi & -\sin\varphi\\ \sin\varphi & \cos\varphi\end{pmatrix}\ \middle|\ \varphi\in\mathbb R\right\}$, $U(1) = \{e^{i\varphi}\mid\varphi\in\mathbb R\}$, and $\begin{pmatrix}\cos\varphi & -\sin\varphi\\ \sin\varphi & \cos\varphi\end{pmatrix}\mapsto e^{i\varphi}$ is an isomorphism of Lie groups; both are diffeomorphic to $S^1$. `Proof in source: full.` Strategy: write $A = \begin{pmatrix}a&c\\b&d\end{pmatrix}$ (source's layout); $A^tA = 1$ gives $a^2+b^2=1$ (1.1), $c^2+d^2=1$ (1.2), $ac+bd=0$ (1.3); $\det A = ad-bc = 1$ (1.4). Multiply (1.4) by $c$ and $d$ and use (1.3),(1.2) to get $c=-b$, $d=a$; so $A = \begin{pmatrix}a&-b\\b&a\end{pmatrix}$ with $a^2+b^2=1$, i.e. $(a,b) = (\cos\varphi,\sin\varphi)$. Group homomorphism property: addition theorems for $\sin,\cos$; bijectivity: Euler's formula.

### Examples
- **E1.1.1** (Ex. 1.1.2.1, p. 7) $G = \mathbb R^n$ with addition.
- **E1.1.2** (Ex. 1.1.2.2, p. 7) $GL(n;\mathbb R)$: open in $\mathbb R^{n^2}$ since $\det$ is continuous; multiplication smooth since entries of $AB$ are polynomials in entries of $A,B$; inversion smooth since entries of $A^{-1}$ are rational functions of entries of $A$.
- **E1.1.3** (Ex. 1.1.2.3, p. 7) $GL(n;\mathbb C)$.
- **E1.1.4** (Ex. 1.1.4.1, pp. 7–8) $O(n)$ is a closed subgroup: $(AB)^t(AB) = B^tA^tAB = B^tB = 1_n$; $A^{-1} = A^t$ so $1_n = (A^{-1})^tA^{-1}$; closedness since $A\mapsto A^tA$ is continuous.
- **E1.1.5** (Ex. 1.1.4.2–6, p. 8) $SL(n;\mathbb R)$, $SO(n)$, $U(n)$, $SL(n;\mathbb C)$, $SU(n)$ as closed subgroups (no verification written).
- **E1.1.6** (Ex. 1.1.5, p. 8) Product of Lie groups.
- **E1.1.7** (Ex. 1.1.8, p. 9) $SO(2)\cong U(1)\cong S^1$ — see T1.1.2.

### Exercises
- None stated in this section.

### Remarks / load-bearing paragraphs
- **R1.1.1** (Rem. 1.1.6, p. 8) Hilbert's 5th problem (ICM Paris 1900): can "smooth" be replaced by "continuous" in the definition of a Lie group? Answer (1950s): yes, nothing changes. (Gleason–Montgomery–Zippin, not named in the source.)

### External results imported without proof
- **I1.1.1** Closed subgroup theorem (T1.1.1) — used to make $O(n), SL, SO, U, SU$ Lie groups.
- **I1.1.2** Solution of Hilbert's 5th problem (R1.1.1) — mentioned only.

---

## 1.2 Lie algebras

`PDF pages: 10–13`

### Standing conventions and notation
- Lie bracket $[\cdot,\cdot]$; antisymmetry is misprinted as "$[v,w] = -[v,w]$" (intended: $[v,w] = -[w,v]$).
- For fixed $g\in G$: **left translation** $L_g(h) := g\cdot h$, **right translation** $R_g(h) := h\cdot g$, **conjugation** $\alpha_g := L_g\circ R_{g^{-1}}$, $\alpha_g(h) = ghg^{-1}$ (p. 11). Conjugation is a Lie group isomorphism; $L_g, R_g$ are diffeomorphisms but not homomorphisms.
- **Push-forward of a vector field** by a diffeomorphism $F: M\to M$: $dF(X)(p) := d_{F^{-1}(p)}F\big(X(F^{-1}(p))\big)$ (Rem. 1.2.4, p. 11), so that $dF\circ X = dF(X)\circ F$.
- $\mathfrak g := \{X\in\mathfrak X(G)\mid X \text{ left-invariant}\}$; identification $T_eG\cong\mathfrak g$ via $X(g) := d_eL_g(X_0)$.
- Lie algebra of $G$ computed as $T_{1_n}G = \{\dot c(0)\mid c:(-\epsilon,\epsilon)\to G \text{ smooth}, c(0) = 1_n\}$ for matrix groups.

### Definitions
- **D1.2.1 — Def - Lie Algebra** (Def. 1.2.1, p. 10). A vector space $V$ with a map $[\cdot,\cdot]: V\times V\to V$ is a *Lie algebra* iff (i) $[\cdot,\cdot]$ is bilinear; (ii) antisymmetric: $\forall v,w$: $[v,w] = -[w,v]$; (iii) Jacobi identity: $\forall u,v,w\in V$: $[[u,v],w] + [[v,w],u] + [[w,u],v] = 0$. $[\cdot,\cdot]$ is the *Lie bracket*.
- **D1.2.2 — Def - Abelian Lie Algebra** (Ex. 1.2.2.1, p. 10). A Lie algebra with $[\cdot,\cdot]\equiv0$ is *abelian*.
- **D1.2.3 — Def - Lie Subalgebra** (Def. 1.2.3, p. 11). A vector subspace $W\subset V$ with $[\cdot,\cdot]|_{W\times W}$ is a *Lie subalgebra* iff $\forall w,w'\in W$: $[w,w']\in W$. (Then $W$ is a Lie algebra.)
- **D1.2.4 — Def - Left and Right Translation and Conjugation** (p. 11). $L_g, R_g, \alpha_g$ as above.
- **D1.2.5 — Def - Push-Forward of a Vector Field** (Rem. 1.2.4, p. 11). As above; $dF(X)$ is again a smooth vector field.
- **D1.2.6 — Def - Left-Invariant Vector Field** (Def. 1.2.5, p. 11). $X\in\mathfrak X(G)$ is *left-invariant* iff $\forall g\in G$: $dL_g(X) = X$.
- **D1.2.7 — Def - Lie Algebra of a Lie Group** (Def. 1.2.6, p. 12). $\mathfrak g :=$ the Lie subalgebra of left-invariant vector fields of $\mathfrak X(G)$ is the *Lie algebra of $G$*. Linear isomorphism $T_eG\to\mathfrak g$, $X_0\mapsto (g\mapsto d_eL_g(X_0))$; $\dim\mathfrak g = \dim G$.
- **D1.2.8 — Def - Classical Matrix Lie Algebras** (Ex. 1.2.7, pp. 12–13). $\mathfrak{gl}(n;\mathbb R) = \mathrm{Mat}(n\times n;\mathbb R)$ with commutator; $\mathfrak o(n) = \{A\mid A^t + A = 0\}$; $\mathfrak{sl}(n;\mathbb R) = \{A\mid \mathrm{tr}A = 0\}$; $\mathfrak{so}(n) = \mathfrak o(n)\cap\mathfrak{sl}(n;\mathbb R) = \mathfrak o(n)$; $\mathfrak u(n) = \{A\in\mathrm{Mat}(n\times n;\mathbb C)\mid A^* = -A\}$; $\mathfrak{sl}(n;\mathbb C) = \{A\in\mathrm{Mat}(n\times n;\mathbb C)\mid\mathrm{tr}A = 0\}$; $\mathfrak{su}(n) = \{A\in\mathrm{Mat}(n\times n;\mathbb C)\mid A^* = -A, \mathrm{tr}A = 0\}$.

### Theorems
- **T1.2.1 — Thm - Push-Forward Preserves the Lie Bracket** (eq. (1.5), Rem. 1.2.4, p. 11). For a diffeomorphism $F: M\to M$ and $X,Y\in\mathfrak X(M)$: $dF([X,Y]) = [dF(X),dF(Y)]$. `Proof in source: omitted/cited (stated as a standard fact).`
- **T1.2.2 — Thm - Left-Invariant Vector Fields Form a Lie Subalgebra** (pp. 11–12). If $X,Y$ are left-invariant then $dL_g([X,Y]) = [dL_g X, dL_g Y] = [X,Y]$, so $\mathfrak g\subset\mathfrak X(G)$ is a Lie subalgebra. `Proof in source: full` (one line from (1.5)).
- **T1.2.3 — Thm - Lie Algebra Is Isomorphic to the Tangent Space at the Identity** (p. 12). For $X\in\mathfrak g$: $X(g) = d_eL_g(X(e))$; conversely $X_0\in T_eG$ gives the left-invariant $X(g) := d_eL_g(X_0)$; hence $T_eG\cong\mathfrak g$ linearly and $\dim_{\mathbb R}\mathfrak g = \dim G$. `Proof in source: full.` Strategy: $X(g) = dL_g(X)(g) = d_{L_{g^{-1}}(g)}L_g(X(L_{g^{-1}}g)) = d_eL_g(X(e))$.
- **T1.2.4 — Thm - Lie Algebras of the Classical Groups** (Ex. 1.2.7, pp. 12–13). The identifications in D1.2.8. `Proof in source: full modulo a dimension count.` Strategy for $\mathfrak o(n)$: for a curve $c(s)\in O(n)$ with $c(0) = 1_n$, differentiate $c(s)^tc(s) = 1_n$ at $s=0$ to get $\dot c(0)^t + \dot c(0) = 0$, so $\mathfrak o(n)\subset\{A^t+A = 0\}$; then $\dim\mathfrak o(n) = \dim O(n) = n(n-1)/2 = \dim\{A^t+A=0\}$ gives equality. For $\mathfrak{sl}$: differentiate $\det c(s) = 1$ to get $\mathrm{tr}\dot c(0) = 0$, dimension count. For $\mathfrak u(n)$: differentiate $c^*c = 1_n$. Gaps: $\dim O(n) = n(n-1)/2$ and the other dimension counts are asserted, not derived; the formula $\frac{d}{ds}\det c(s)|_0 = \mathrm{tr}\,\dot c(0)$ is used without proof.

### Examples
- **E1.2.1** (Ex. 1.2.2.1, p. 10) Any vector space with zero bracket (abelian).
- **E1.2.2** (Ex. 1.2.2.2, p. 10) $\mathrm{Mat}(n\times n;\mathbb K)$ with $[A,B] := AB - BA$; the Jacobi identity is verified by expanding $[[A,B],C] + [[B,C],A] + [[C,A],B] = 0$ and is a consequence of associativity.
- **E1.2.3** (Ex. 1.2.2.3, p. 10) $\mathbb R^3$ with the cross product $[\cdot,\cdot] = (\cdot)\times(\cdot)$.
- **E1.2.4** (Ex. 1.2.2.4, p. 10) $\mathfrak X(M)$ with the Lie bracket of vector fields — an infinite-dimensional Lie algebra.
- **E1.2.5–E1.2.11** (Ex. 1.2.7.1–7, pp. 12–13) $\mathfrak{gl}(n;\mathbb R)$, $\mathfrak o(n)$, $\mathfrak{sl}(n;\mathbb R)$, $\mathfrak{so}(n)$, $\mathfrak u(n)$, $\mathfrak{sl}(n;\mathbb C)$, $\mathfrak{su}(n)$ — see D1.2.8/T1.2.4.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R1.2.1** (p. 10) "In general, the Jacobi identity can be thought of as a replacement for associativity."
- **R1.2.2** (p. 11) Conjugation $\alpha_g$ is a Lie group isomorphism; $L_g$ and $R_g$ are diffeomorphisms but not group homomorphisms.
- **R1.2.3** (p. 12) The construction $X(g) := d_eL_g(X_0)$ shows every tangent vector at $e$ extends uniquely to a left-invariant field.

### External results imported without proof
- **I1.2.1** Naturality of the Lie bracket under diffeomorphisms (1.5).
- **I1.2.2** $\dim O(n) = n(n-1)/2$, $\dim SL(n;\mathbb R) = n^2-1$, etc.

---

## 1.3 Representations

`PDF pages: 13–21`

### Standing conventions and notation
- $\varrho: G\to\mathrm{Aut}(V)$, $V$ finite-dimensional $\mathbb K$-vector space; choosing a basis, $\mathrm{Aut}(V)\cong GL(n;\mathbb K)$ (Rem. 1.3.2).
- Adjoint representation $\mathrm{Ad}_g := d_e\alpha_g: \mathfrak g\to\mathfrak g$; for matrix groups $\mathrm{Ad}_g(X) = gXg^{-1}$.
- Dual representation uses the inverse: $\varrho^*(g) := \varrho(g^{-1})^*$, where $\varrho(g)^*(\lambda) := \lambda\circ\varrho(g)$.
- Basis of $\mathfrak{su}(2)$: $-i\sigma_1 = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$, $-i\sigma_2 = \begin{pmatrix}0&i\\i&0\end{pmatrix}$, $-i\sigma_3 = \begin{pmatrix}i&0\\0&-i\end{pmatrix}$ ("$-i$ times the Pauli matrices"; note with the standard Pauli matrices $-i\sigma_2 = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$ and $-i\sigma_1 = \begin{pmatrix}0&-i\\-i&0\end{pmatrix}$, so the source's labelling of $\sigma_1,\sigma_2$ is nonstandard; the three matrices listed do form a basis of $\mathfrak{su}(2)$).
- $\varrho_*:= d_e\varrho$ for the induced Lie algebra representation.

### Definitions
- **D1.3.1 — Def - Representation of a Lie Group** (Def. 1.3.1, p. 13). A *representation* of a Lie group $G$ is a Lie group homomorphism $\varrho: G\to\mathrm{Aut}(V)$ for some finite-dimensional $\mathbb K$-vector space $V$; *real* if $\mathbb K = \mathbb R$, *complex* if $\mathbb K = \mathbb C$.
- **D1.3.2 — Def - Faithful Representation** (Def. 1.3.3, p. 14). $\varrho$ is *faithful* iff injective.
- **D1.3.3 — Def - Trivial Representation** (Ex. 1.3.4.1, p. 14). $\varrho(g) := \mathrm{id}_V$ for all $g$; faithful only for $G = \{e\}$.
- **D1.3.4 — Def - Adjoint Representation of a Lie Group** (Ex. 1.3.4.2, p. 14). $\mathrm{Ad}: G\to\mathrm{Aut}(\mathfrak g)$, $\mathrm{Ad}_g := d_e\alpha_g: \mathfrak g\cong T_eG\to T_eG\cong\mathfrak g$ (well-defined since $\alpha_g(e) = e$).
- **D1.3.5 — Def - Standard Representation** (Ex. 1.3.10, p. 16). For $G = GL(n;\mathbb K)$: $\varrho_{st} := \mathrm{id}: G\to GL(n;\mathbb K) = \mathrm{Aut}(\mathbb K^n)$; for $O(n), SL(n;\mathbb R), SO(n)$: the inclusion into $GL(n;\mathbb R)$; for $U(n), SL(n;\mathbb C), SU(n)$: the inclusion into $GL(n;\mathbb C)$.
- **D1.3.6 — Def - Direct Sum Representation** (Def. 1.3.11.1, p. 16). $(\varrho_1\oplus\varrho_2)(g)(v_1\oplus v_2) := \varrho_1(g)v_1\oplus\varrho_2(g)v_2$; block-diagonal $\begin{pmatrix}\varrho_1(g)&0\\0&\varrho_2(g)\end{pmatrix}$.
- **D1.3.7 — Def - Tensor Product Representation** (Def. 1.3.11.2, p. 16). $(\varrho_1\otimes\varrho_2)(g)(v_1\otimes v_2) := \varrho_1(g)v_1\otimes\varrho_2(g)v_2$, extended linearly.
- **D1.3.8 — Def - Antisymmetric Tensor Product Representation** (Def. 1.3.11.3, p. 16). $\Lambda^k\varrho: G\to\mathrm{Aut}(\Lambda^kV)$, $(\Lambda^k\varrho)(g)(v_1\wedge\dots\wedge v_k) := \varrho(g)v_1\wedge\dots\wedge\varrho(g)v_k$ (also "wedge product representation").
- **D1.3.9 — Def - Symmetric Tensor Product Representation** (Def. 1.3.11.4, p. 17). $\odot^k\varrho: G\to\mathrm{Aut}(\odot^kV)$, $(\odot^k\varrho)(g)(v_1\odot\dots\odot v_k) := \varrho(g)v_1\odot\dots\odot\varrho(g)v_k$.
- **D1.3.10 — Def - Dual Representation** (Def. 1.3.11.5, p. 17). $\varrho^*: G\to\mathrm{Aut}(V^*)$, $\varrho^*(g) := \varrho(g^{-1})^*$, i.e. $\varrho^*(g)(\lambda) = \lambda\circ\varrho(g^{-1})$.
- **D1.3.11 — Def - Complexification of a Representation** (Def. 1.3.11.6, p. 17). For real $\varrho$, $V_{\mathbb C} := V\otimes_{\mathbb R}\mathbb C$ and $\varrho_{\mathbb C} := \varrho\otimes\mathrm{id}_{\mathbb C}: G\to\mathrm{Aut}(V_{\mathbb C})$; in matrices: regard the real matrices as complex.
- **D1.3.12 — Def - Equivalent Representations** (Def. 1.3.12, p. 18). $\varrho: G\to\mathrm{Aut}(V)$ and $\tilde\varrho: G\to\mathrm{Aut}(\tilde V)$ are *equivalent* iff there is an isomorphism $T: V\to\tilde V$ with $T\circ\varrho(g) = \tilde\varrho(g)\circ T$ for all $g$.
- **D1.3.13 — Def - Representation of a Lie Algebra** (Def. 1.3.16, p. 20). A *representation* of a Lie algebra $\mathfrak g$ is a Lie algebra homomorphism $\lambda: \mathfrak g\to\mathrm{End}(V)$, $V$ finite-dimensional over $\mathbb K$ (real/complex accordingly). An *equivalence* of $\lambda$ and $\tilde\lambda: \tilde{\mathfrak g}\to\mathrm{End}(\tilde V)$ (source writes $\tilde{\mathfrak g}$, presumably $\mathfrak g$) is a linear isomorphism $T: V\to\tilde V$ with $T\circ\lambda(X) = \tilde\lambda(X)\circ T$ for all $X\in\mathfrak g$.
- **D1.3.14 — Def - Adjoint Representation of a Lie Algebra** (Ex. 1.3.18.2, p. 20). $\mathrm{ad}: \mathfrak g\to\mathrm{End}(\mathfrak g)$, $\mathrm{ad}(X)(Y) := [X,Y]$.
- **D1.3.15 — Def - Representations rho_k of U(1)** (Ex. 1.3.14, p. 18). $\varrho_k: U(1)\to GL(1;\mathbb C)$, $z\mapsto z^k$, $k\in\mathbb Z$; $\varrho_0$ trivial, $\varrho_1 = \varrho_{st}$.
- **D1.3.16 — Def - Representations rho_k of SU(2)** (Ex. 1.3.15, p. 19). $\varrho_0$ trivial, $\varrho_1 := \varrho_{st}: SU(2)\to GL(2;\mathbb C)$, $\varrho_k := \odot^k\varrho_1$ for $k\ge2$; $\dim_{\mathbb C}\odot^k\mathbb C^2 = k+1$.

### Theorems
- **T1.3.1 — Thm - Ad Is a Smooth Representation** (Ex. 1.3.4.2, p. 14). $\mathrm{Ad}: G\to\mathrm{Aut}(\mathfrak g)$ is a Lie group homomorphism: $\mathrm{Ad}_{g_1g_2} = \mathrm{Ad}_{g_1}\circ\mathrm{Ad}_{g_2}$, $\mathrm{Ad}_e = \mathrm{id}$, $(\mathrm{Ad}_g)^{-1} = \mathrm{Ad}_{g^{-1}}$, and $\mathrm{Ad}$ is smooth. `Proof in source: full (smoothness asserted).` Strategy: take a curve $c$ with $c(0)=e$, $\dot c(0) = X$; $\mathrm{Ad}_{g_1g_2}(X) = \frac{d}{ds}|_0\alpha_{g_1g_2}(c(s)) = \frac{d}{ds}|_0(\alpha_{g_1}\circ\alpha_{g_2})(c(s)) = d_e\alpha_{g_1}(d_e\alpha_{g_2}X)$ using $\alpha_{g_1g_2} = \alpha_{g_1}\circ\alpha_{g_2}$. Gaps: smoothness of $g\mapsto\mathrm{Ad}_g$ is asserted from smoothness of $(g,h)\mapsto\alpha_g(h)$.
- **T1.3.2 — Thm - Adjoint Representation of Matrix Groups Is Conjugation** (Rem. 1.3.7, p. 15). For $G$ any matrix group of Ex. 1.1.4 and $X\in\mathfrak g$: $\mathrm{Ad}_g(X) = \frac{d}{ds}|_0\, g\,c(s)\,g^{-1} = gXg^{-1}$. `Proof in source: full.`
- **T1.3.3 — Thm - Dual Representation Is a Homomorphism** (p. 17). The naive $g\mapsto\varrho(g)^*$ is an anti-homomorphism ($\varrho(g_1g_2)^* = \varrho(g_2)^*\varrho(g_1)^*$); with $\varrho^*(g) := \varrho(g^{-1})^*$ one gets $\varrho^*(g_1g_2) = \varrho^*(g_1)\varrho^*(g_2)$. `Proof in source: full.`
- **T1.3.4 — Thm - Tensor Products and Duals of U(1) Representations** (Ex. 1.3.14, p. 18). Under $\mathbb C\otimes\mathbb C\cong\mathbb C$, $u\otimes w\mapsto uw$: $\varrho_k\otimes\varrho_l\cong\varrho_{k+l}$; and $\varrho_k^*\cong\varrho_{-k}$ (since $\varrho_k^*(z)(\lambda) = \lambda\circ z^{-k} = z^{-k}\lambda$). `Proof in source: full.`
- **T1.3.5 — Thm - Complete Reducibility for U(1)** (Ex. 1.3.14, p. 18). Every complex representation of $U(1)$ is equivalent to a direct sum of the 1-dimensional $\varrho_k$. `Proof in source: omitted/cited ("It turns out").`
- **T1.3.6 — Thm - rho_2 of SU(2) Is the Complexified Adjoint Representation** (Ex. 1.3.15, p. 19). For $g = \mathrm{diag}(e^{i\varphi},e^{-i\varphi})$, in the basis $e_1\odot e_1, e_2\odot e_2, e_2\odot e_1$: $\varrho_2(g) = \mathrm{diag}(e^{2i\varphi},e^{-2i\varphi},1)$; with $T = \begin{pmatrix}-i&1&0\\1&-i&0\\0&0&1\end{pmatrix}$, $T^{-1} = \begin{pmatrix}i/2&1/2&0\\1/2&i/2&0\\0&0&1\end{pmatrix}$ one has $T\,\mathrm{Ad}_g\,T^{-1} = \varrho_2(g)$; this holds for all $g\in SU(2)$, so $T$ is an equivalence between $\varrho_2$ and $(\mathrm{Ad}_{SU(2)})_{\mathbb C}$. `Proof in source: sketch.` Gaps: verified only for diagonal $g$; "It can be checked" for general $g$.
- **T1.3.7 — Thm - Complete Reducibility for SU(2)** (p. 19). Every complex representation of $SU(2)$ is equivalent to a direct sum of the $\varrho_k$. `Proof in source: omitted/cited.`
- **T1.3.8 — Thm - ad Is a Lie Algebra Representation** (Ex. 1.3.18.2, p. 20). $\mathrm{ad}(X)\in\mathrm{End}(\mathfrak g)$, $X\mapsto\mathrm{ad}(X)$ is linear, and $\mathrm{ad}([X,Y]) = [\mathrm{ad}(X),\mathrm{ad}(Y)]$. `Proof in source: full.` Strategy: $\mathrm{ad}([X,Y])(Z) = [[X,Y],Z] = -[[Y,Z],X] - [[Z,X],Y] = [X,[Y,Z]] - [Y,[X,Z]] = (\mathrm{ad}X\,\mathrm{ad}Y - \mathrm{ad}Y\,\mathrm{ad}X)(Z)$ by Jacobi and antisymmetry.
- **T1.3.9 — Thm - Differential of a Group Representation Is an Algebra Representation** (Rem. 1.3.19, pp. 20–21). If $\varrho: G\to\mathrm{Aut}(V)$ is a Lie group representation then $\varrho_* := d_e\varrho: \mathfrak g\cong T_eG\to T_{\mathrm{id}}\mathrm{Aut}(V)\cong\mathrm{End}(V)$ is a Lie algebra representation. `Proof in source: deferred to Cor. 1.4.10.`

### Examples
- **E1.3.1** (Rem. 1.3.5, Ex. 1.3.6, p. 14) If $G$ abelian then $\alpha_g = \mathrm{id}$ and $\mathrm{Ad}_g = \mathrm{id}_{\mathfrak g}$; e.g. $G = U(1)$.
- **E1.3.2** (Ex. 1.3.8, p. 15) Adjoint representation of $SU(2)$: $\mathfrak{su}(2) = \left\{\begin{pmatrix}it&z\\-\bar z&-it\end{pmatrix}\mid z\in\mathbb C, t\in\mathbb R\right\}$; for $g = \mathrm{diag}(e^{i\varphi},e^{-i\varphi})$: $\mathrm{Ad}_g(-i\sigma_1) = \cos(2\varphi)(-i\sigma_1) + \sin(2\varphi)(-i\sigma_2)$, $\mathrm{Ad}_g(-i\sigma_2) = \cos(2\varphi)(-i\sigma_2) - \sin(2\varphi)(-i\sigma_1)$, $\mathrm{Ad}_g(-i\sigma_3) = -i\sigma_3$; matrix $\mathrm{Ad}_g = \begin{pmatrix}\cos2\varphi&-\sin2\varphi&0\\ \sin2\varphi&\cos2\varphi&0\\0&0&1\end{pmatrix}$ in the basis $-i\sigma_1,-i\sigma_2,-i\sigma_3$.
- **E1.3.3** (Rem. 1.3.9, p. 15) $\mathrm{Ad}_{SU(2)}$ is not faithful: $\mathrm{Ad}_{-1_2} = 1$.
- **E1.3.4** (Ex. 1.3.10, p. 16) Standard representations.
- **E1.3.5** (Ex. 1.3.13, p. 18) Two bases of $V$ give $F_1,F_2: V\to\mathbb K^n$ and representations $\varrho_1,\varrho_2$ into $GL(n;\mathbb K)$; $T := F_2\circ F_1^{-1}$ is an equivalence.
- **E1.3.6** (Ex. 1.3.14, p. 18) $U(1)$ representations $\varrho_k$.
- **E1.3.7** (Ex. 1.3.15, p. 19) $SU(2)$ representations $\varrho_k = \odot^k\varrho_1$; $\varrho_2\cong(\mathrm{Ad})_{\mathbb C}$; basis of $\odot^k\mathbb C^2$ is $e_1^{\odot k}, e_2\odot e_1^{\odot(k-1)},\dots,e_2^{\odot k}$.
- **E1.3.8** (Ex. 1.3.18.1, p. 20) Trivial Lie algebra representation $\lambda(X) := 0$.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R1.3.1** (Rem. 1.3.2, p. 13) Basis choice gives $V\cong\mathbb K^n$, $\mathrm{Aut}(V)\cong GL(n;\mathbb K)$.
- **R1.3.2** (Rem. 1.3.17, p. 20) Up to equivalence a Lie algebra representation is a homomorphism $\mathfrak g\to\mathrm{Mat}(n\times n;\mathbb K)$.
- **R1.3.3** (p. 17) Why the dual representation needs $g^{-1}$: $(\varrho(g_1)\varrho(g_2))^* = \varrho(g_2)^*\varrho(g_1)^*$ reverses order.
- **R1.3.4** (p. 19) Since $\mathrm{Ad}_{SU(2)}$ is real 3-dimensional, $\varrho_2$ is the only candidate among the $\varrho_k$ to be equivalent to its complexification.

### External results imported without proof
- **I1.3.1** Complete reducibility of complex representations of $U(1)$ (T1.3.5).
- **I1.3.2** Complete reducibility of complex representations of $SU(2)$ into the $\varrho_k$ (T1.3.7).
- **I1.3.3** $T_{\mathrm{id}}\mathrm{Aut}(V)\cong\mathrm{End}(V)$ (used in Rem. 1.3.19).

---

## 1.4 The exponential map

`PDF pages: 21–27`

### Standing conventions and notation
- $\gamma_X: \mathbb R\to G$ the integral curve of $X\in\mathfrak g$ with $\gamma_X(0) = e$ (defined on all of $\mathbb R$ by Exercise 1.4.1).
- $\exp(X) := \gamma_X(1)$; $\gamma_X(t) = \exp(tX)$ (1.6).
- Matrix exponential $e^X := \sum_{k=0}^\infty X^k/k!$ (1.7).
- $\mathrm{inv}: G\to G$, $g\mapsto g^{-1}$; $\varphi_* := d_e\varphi$; $\mathrm{Ad}_* = \mathrm{ad}$.
- Footnote (p. 25): for a Lie group homomorphism $\varphi$, $\varphi(\alpha_g(g')) = \alpha_{\varphi(g)}(\varphi(g'))$.

### Definitions
- **D1.4.1 — Def - Integral Curve of a Left-Invariant Field** (p. 21). For $X\in\mathfrak g$, $\gamma_X:\mathbb R\to G$ is the integral curve of $X$ with $\gamma_X(0) = e$.
- **D1.4.2 — Def - Exponential Map** (Def. 1.4.3, p. 21). $\exp: \mathfrak g\to G$, $\exp(X) := \gamma_X(1)$. Smooth by ODE theory.
- **D1.4.3 — Def - Matrix Exponential** (eq. (1.7), p. 26). $e^X := \sum_{k=0}^\infty\frac{X^k}{k!}$ for $X\in\mathrm{Mat}(n\times n;\mathbb K)$; the series converges absolutely; $e^0 = 1_n$; $\frac{d}{dt}|_0 e^{tX} = X$.
- **D1.4.4 — Def - Induced Lie Algebra Homomorphism** (Lemma 1.4.9, p. 24). $\varphi_* := d_e\varphi: \mathfrak g\to\mathfrak h$ for a Lie group homomorphism $\varphi: G\to H$.

### Theorems
- **T1.4.1 — Thm - One-Parameter Subgroups Are Integral Curves** (Lemma 1.4.2, p. 21). Let $\gamma:\mathbb R\to G$ be smooth with $\gamma(0) = e$. Then $\gamma$ is a group homomorphism ($\gamma(s+t) = \gamma(s)\gamma(t)$ for all $s,t$) iff $\gamma$ is an integral curve of a left-invariant vector field. `Proof in source: "⇒" full; "⇐" omitted ("slightly more involved").` Strategy for ⇒: $\dot\gamma(t) = \frac{d}{ds}|_0\gamma(t)\gamma(s) = dL_{\gamma(t)}\dot\gamma(0) = X(\gamma(t))$ with $X$ the left-invariant field with $X(e) = \dot\gamma(0)$.
- **T1.4.2 — Thm - Exponential Map Gives One-Parameter Subgroups** (eq. (1.6), p. 22). $\gamma_X(t) = \exp(tX)$; hence $\exp((s+t)X) = \exp(sX)\exp(tX)$, $\exp(0) = e$, $\exp(-X) = \exp(X)^{-1}$. `Proof in source: full.` Strategy: $\tilde\gamma(t) := \gamma_X(\alpha t)$ is a homomorphism $\mathbb R\to G$ hence an integral curve of a left-invariant field; $\dot{\tilde\gamma} = \alpha X(\tilde\gamma)$ and $\tilde\gamma(0) = e$ so $\tilde\gamma = \gamma_{\alpha X}$; evaluate at 1. Gap: uses the "⇐" direction of Lemma 1.4.2, which was not proved.
- **T1.4.3 — Thm - Differential of exp at Zero** (Lemma 1.4.4, p. 22). $d_0\exp = \mathrm{id}_{\mathfrak g}$. `Proof in source: full`: $d_0\exp(X) = \frac{d}{ds}|_0\exp(sX) = X$.
- **T1.4.4 — Thm - exp Is a Local Diffeomorphism** (Cor. 1.4.5, p. 23). There are neighbourhoods $U\subset\mathfrak g$ of $0$ and $V\subset G$ of $e$ such that $\exp|_U: U\to V$ is a diffeomorphism. `Proof in source: full` (inverse function theorem).
- **T1.4.5 — Thm - Differential of Inversion** (Cor. 1.4.6, p. 23). $d_e\mathrm{inv} = -\mathrm{id}_{\mathfrak g}$. `Proof in source: full.` Strategy: the diagram $U\xrightarrow{-\mathrm{id}}U$, $V\xrightarrow{\mathrm{inv}}V$ with vertical $\exp$ commutes (since $\exp(-X) = \exp(X)^{-1}$); differentiate at 0 using $d_0\exp = \mathrm{id}$.
- **T1.4.6 — Thm - Naturality of exp** (Cor. 1.4.7, p. 24). For any Lie group homomorphism $\varphi: G\to H$: $\varphi\circ\exp = \exp\circ d_e\varphi$. `Proof in source: full.` Strategy: $t\mapsto\varphi(\exp(tX))$ is a homomorphism $\mathbb R\to H$ with derivative $d_e\varphi(X)$ at 0, hence (Lemma 1.4.2) the integral curve of the left-invariant field of $d_e\varphi(X)$; evaluate at $t=1$.
- **T1.4.7 — Thm - Differential of Ad Is ad** (Rem. 1.4.8, p. 24). $\mathrm{Ad}_* = \mathrm{ad}$. `Proof in source: full for matrix groups only.` Strategy: $\mathrm{Ad}_*(X)(Y) = \frac{d}{dt}|_0\exp(tX)Y\exp(-tX) = XY - YX = [X,Y]$. Gap: general Lie groups asserted ("easily checked").
- **T1.4.8 — Thm - Homomorphisms Induce Lie Algebra Homomorphisms** (Lemma 1.4.9, pp. 24–25). If $\varphi: G\to H$ is a Lie group homomorphism then $\varphi_* = d_e\varphi: \mathfrak g\to\mathfrak h$ is a Lie algebra homomorphism. `Proof in source: full.` Strategy: $\varphi_*([X,Y]) = \varphi_*(\mathrm{Ad}_*(X)Y) = \frac{d}{dt}|_0\varphi_*(\mathrm{Ad}_{\exp tX}Y) = \partial_t\partial_s|_0\varphi(\alpha_{\exp tX}(\exp sY)) = \partial_t\partial_s|_0\alpha_{\varphi(\exp tX)}(\varphi(\exp sY)) = \partial_t\partial_s|_0\alpha_{\exp(t\varphi_*X)}(\exp(s\varphi_*Y))$ (by 1.4.7) $= \mathrm{Ad}_*(\varphi_*X)(\varphi_*Y) = [\varphi_*X,\varphi_*Y]$. Gaps: relies on $\mathrm{Ad}_* = \mathrm{ad}$ for general $G$ (only shown for matrix groups).
- **T1.4.9 — Thm - Differential of a Representation Is a Representation** (Cor. 1.4.10, p. 25). If $\varphi: G\to\mathrm{Aut}(V)$ is a Lie group representation, then $\varphi_*: \mathfrak g\to\mathrm{End}(V)$ is a Lie algebra representation. `Proof in source: full` (immediate from Lemma 1.4.9).
- **T1.4.10 — Thm - Lie Algebra of an Abelian Group Is Abelian** (Rem. 1.4.11, pp. 25–26). If $G$ abelian then $\mathrm{inv}$ is a homomorphism, $\mathrm{inv}_* = -\mathrm{id}_{\mathfrak g}$ is a Lie algebra homomorphism, so $-[X,Y] = [-X,-Y] = [X,Y]$, hence $[\cdot,\cdot]\equiv0$. `Proof in source: full.`
- **T1.4.11 — Thm - exp Equals the Matrix Exponential for Matrix Groups** (p. 26). For $G\subset GL(n;\mathbb K)$: $e^{(s+t)X} = e^{sX}e^{tX}$ (Cauchy product with $m = k-l$), so $t\mapsto e^{tX}$ is a homomorphism $\mathbb R\to G$, hence by Lemma 1.4.2 the integral curve of $X$; thus $e^{tX} = \exp(tX)$, $e^X = \exp(X)$. `Proof in source: full.` Gap: that $e^{tX}$ lies in $G$ (not just $GL$) is not discussed.
- **T1.4.12 — Thm - exp Surjective for Compact Connected Groups** (Rem. 1.4.13, p. 27). If $G$ is compact and connected then $\exp: \mathfrak g\to G$ is surjective. `Proof in source: omitted/cited.`

### Examples
- **E1.4.1** (Ex. 1.4.12, pp. 26–27) $\mathfrak{so}(2) = \left\{\begin{pmatrix}0&-\theta\\\theta&0\end{pmatrix}\right\}$; for $A = \begin{pmatrix}0&-\theta\\\theta&0\end{pmatrix}$: $A^{2k} = (-1)^k\theta^{2k}1_2$, $A^{2k+1} = (-1)^k\theta^{2k+1}\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, so $e^A = \begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$; $\exp: \mathfrak{so}(2)\to SO(2)$ is surjective but not injective.

### Exercises
- **X1.4.1** (Exercise 1.4.1, p. 21). Show that the maximal integral curves of left-invariant vector fields on Lie groups are defined on all of $\mathbb R$.

### Remarks / load-bearing paragraphs
- **R1.4.1** (p. 22) Smoothness of $\exp$ from the general theory of ODEs (smooth dependence on initial data); figure of $\exp$ mapping $\mathfrak g$ to $G$.
- **R1.4.2** (p. 26) Cauchy-product computation $e^{(s+t)X} = e^{sX}e^{tX}$ (substitution $m = k-l$).

### External results imported without proof
- **I1.4.1** Existence/uniqueness/smooth dependence for ODE flows (used for $\exp$ smooth, uniqueness of $\gamma_X$).
- **I1.4.2** Inverse function theorem (Cor. 1.4.5).
- **I1.4.3** Surjectivity of $\exp$ for compact connected $G$ (Rem. 1.4.13).
- **I1.4.4** "⇐" of Lemma 1.4.2.

---

## 1.5 Group actions

`PDF pages: 27–36`

### Standing conventions and notation
- **Left action** $G\times M\to M$, $(g,x)\mapsto g\cdot x$; $L_g: M\to M$, $L_g(x) := g\cdot x$ (same letter as left translation).
- **Right action** $M\times G\to M$, $(x,g)\mapsto x\cdot g$ (Def. 1.5.26). Conversion: a left action gives a right action by $p*g := g^{-1}\cdot p$ and vice versa $g*p := p\cdot g^{-1}$ (Rem. 1.5.27).
- Orbit $G\cdot x$; orbit space $G\backslash M$ (left action; written $G\backslash M$ throughout, also for right actions on $P$ in §2.2 where it should be $P/G$).
- $R_p: G\to M$, $R_p(g) := g\cdot p$; fundamental vector field $\bar X(p) := d_eR_p(X)$.
- $\mathbb{CP}^{n-1} := U(1)\backslash S^{2n-1}$; $\hat{\mathbb C} := \mathbb C\cup\{\infty\}$; stereographic projection $u\mapsto\frac{1}{4+|u|^2}(4u, 4-|u|^2)$ (from the plane at height... normalised so that $S^2\subset\mathbb C\times\mathbb R$ has the south pole $(0,-1)$).
- Hopf map $\mathrm{Hopf}: S^3\to S^2$, $w = (w_1,w_2)\mapsto\frac{1}{4|w_2|^2+|w_1|^2}\big(4w_1\bar w_2,\ 4|w_2|^2 - |w_1|^2\big)$.
- $Z(G) := \{g\mid\forall h: gh = hg\}$ the center.

### Definitions
- **D1.5.1 — Def - Left Action** (Def. 1.5.1, p. 27). A smooth map $G\times M\to M$, $(g,x)\mapsto g\cdot x$ is a *(left) action* iff (i) $(g\cdot h)\cdot x = g\cdot(h\cdot x)$ for all $x, g, h$; (ii) $e\cdot x = x$.
- **D1.5.2 — Def - Trivial Action** (Ex. 1.5.3.1, p. 27). $g\cdot x := x$.
- **D1.5.3 — Def - Action Induced by a Representation** (Ex. 1.5.3.2, p. 27). $g\cdot v := \varrho(g)(v)$.
- **D1.5.4 — Def - Natural Actions of a Group on Itself** (Ex. 1.5.3.3, pp. 27–28). By multiplication $g*h := gh$ ((i) = associativity, (ii) = neutral element) and by conjugation $g*h := \alpha_g(h)$.
- **D1.5.5 — Def - Effective Free and Transitive Actions** (Def. 1.5.4, p. 28). *Effective*: $\forall g$: $(\forall x: g\cdot x = x)\Rightarrow g = e$, equivalently $L_g = \mathrm{id}_M\Rightarrow g = e$, equivalently $G\to\mathrm{Diff}(M)$ injective. *Free*: $\forall g$: $(\exists x: g\cdot x = x)\Rightarrow g = e$. *Transitive*: $\forall x,y\ \exists g: g\cdot x = y$.
- **D1.5.6 — Def - Center of a Group** (Ex. 1.5.6.3, p. 28). $Z(G) := \{g\in G\mid\forall h\in G: gh = hg\}$.
- **D1.5.7 — Def - Orbit and Orbit Space** (Def. 1.5.8, p. 29). $G\cdot x := \{g\cdot x\mid g\in G\}$; $G$ transitive iff $G\cdot x = M$; orbit space $G\backslash M := \{G\cdot x\mid x\in M\}$.
- **D1.5.8 — Def - Hopf Map** (Ex. 1.5.10, p. 30). As in conventions; smooth; fibres $\mathrm{Hopf}^{-1}(p)$ are the $U(1)$-orbits on $S^3$.
- **D1.5.9 — Def - Complex Projective Space** (Def. 1.5.13, Ex. 1.5.12, pp. 31–32). $\mathbb{CP}^{n-1} := U(1)\backslash S^{2n-1}\cong\{1\text{-dimensional complex subspaces of }\mathbb C^n\}$, the $(n-1)$-dimensional complex projective space.
- **D1.5.10 — Def - Fundamental Vector Field** (Def. 1.5.16, p. 33). For an action of $G$ on $M$, $p\in M$, $R_p: G\to M$, $R_p(g) := g\cdot p$; for $X\in\mathfrak g$ set $\bar X(p) := d_eR_p(X)\in T_pM$; $\bar X\in\mathfrak X(M)$ is the *fundamental vector field* of $X$.
- **D1.5.11 — Def - Discrete Group** (Def. 1.5.20, p. 34). A zero-dimensional Lie group.
- **D1.5.12 — Def - Properly Discontinuous Action** (Def. 1.5.22, pp. 34–35). An action of a discrete group $G$ on $M$ is *properly discontinuous* iff (i) $\forall p\in M$ there is a neighbourhood $U$ of $p$ with $g\cdot U\cap U\neq\emptyset\Rightarrow g = e$; (ii) $\forall p,q$ with $G\cdot p\neq G\cdot q$ there are neighbourhoods $U\ni p$, $V\ni q$ with $g\cdot U\cap V = \emptyset$ for all $g\in G$.
- **D1.5.13 — Def - Right Action** (Def. 1.5.26, p. 36). A smooth map $M\times G\to M$, $(x,g)\mapsto x\cdot g$ with (i) $x\cdot(g\cdot h) = (x\cdot g)\cdot h$; (ii) $x\cdot e = x$.

### Theorems
- **T1.5.1 — Thm - Action Gives a Homomorphism into Diff(M)** (Rem. 1.5.2, p. 27). For any action, $L_g$ is a diffeomorphism with inverse $L_{g^{-1}}$ and $g\mapsto L_g$ is a group homomorphism $G\to\mathrm{Diff}(M)$. `Proof in source: full.`
- **T1.5.2 — Thm - Free Implies Effective** (Rem. 1.5.5, p. 28). Every free action is effective (unless $M = \emptyset$). `Proof in source: full (immediate).`
- **T1.5.3 — Thm - Quotient by a Free Compact Group Action** (Thm. 1.5.11, p. 31). Let $G$ be a compact Lie group acting freely on $M$. Then $G\backslash M$ carries a smooth manifold structure such that (i) $M\to G\backslash M$, $x\mapsto G\cdot x$, is smooth with differential of maximal rank at every point; (ii) $\dim(G\backslash M) = \dim M - \dim G$; (iii) universal property: for every manifold $N$ and smooth $f: M\to N$ constant on orbits there is a unique smooth $\tilde f: G\backslash M\to N$ with $\tilde f\circ\pi = f$. `Proof in source: sketch ("Idea of proof").` Strategy: for $x\in M$ choose a small embedded disc $D$ of dimension $\dim M - \dim G$ transverse to $G\cdot x$ at $x$; after shrinking, $G\times D\to M$, $(g,y)\mapsto g\cdot y$, is a diffeomorphism onto its image; this yields a chart of the orbit space. Compactness of $G$ ensures points of a small disc correspond 1:1 to orbits and the quotient is Hausdorff. Gaps: all details.
- **T1.5.4 — Thm - CP^1 Is Diffeomorphic to S^2** (Rem. 1.5.14, p. 32). $\dim_{\mathbb R}\mathbb{CP}^{n-1} = 2(n-1)$; $\mathbb{CP}^{n-1}$ is compact and connected (image of $S^{2n-1}$); for $n = 2$ the Hopf map factors as $S^3\to\mathbb{CP}^1\xrightarrow{\widetilde{\mathrm{Hopf}}}S^2$ with $\widetilde{\mathrm{Hopf}}$ smooth, bijective, of maximal rank everywhere, hence a diffeomorphism. `Proof in source: sketch ("By explicit computation").`
- **T1.5.5 — Thm - Cell Decomposition of Complex Projective Space** (Rem. 1.5.15, pp. 32–33). $\mathbb C\subset\mathbb C^2\subset\dots$ gives $S^1\subset S^3\subset\dots$ and $\{*\}\subset\mathbb{CP}^1\subset\mathbb{CP}^2\subset\dots$. Lines in $\mathbb C^{n+1} = \mathbb C^n\oplus\mathbb C$ are either contained in the hyperplane $\mathbb C^n$ (forming $\mathbb{CP}^{n-1}$) or meet the affine hyperplane $\mathbb C^n + e_{n+1}$ in exactly one point; hence $\mathbb{CP}^n = \mathbb{CP}^{n-1}\sqcup\mathbb C^n$. `Proof in source: full (elementary).`
- **T1.5.6 — Thm - Fundamental Vector Fields Give a Lie Algebra Homomorphism** (Rem. 1.5.17, p. 33). $\mathfrak g\ni X\mapsto\bar X\in\mathfrak X(M)$ is the Lie algebra homomorphism corresponding to $G\to\mathrm{Diff}(M)$. `Proof in source: omitted (stated).` Note: for a *left* action this map is in fact an anti-homomorphism with the usual bracket conventions; the source does not address this.
- **T1.5.7 — Thm - Flow of a Fundamental Vector Field** (Rem. 1.5.19, p. 34). $\frac{d}{dt}|_{t_0}\exp(tX)\cdot p = \bar X(\exp(t_0X)\cdot p)$, so $L_{\exp(tX)}$ is the flow of $\bar X$; in particular $\bar X(p) = 0\Rightarrow\exp(tX)\cdot p = p$ for all $t$. Consequently: if $G$ with $\dim G\ge1$ acts freely on $M$ then $M$ has a nowhere-vanishing vector field, so $\chi(M) = 0$; e.g. $M\not\cong S^{2n}$. `Proof in source: full for the flow statement; the obstruction uses Poincaré–Hopf / hairy ball without proof.` Strategy: $\frac{d}{dt}|_{t_0}\exp(tX)p = \frac{d}{ds}|_0\exp(sX)\exp(t_0X)p = d_eR_{\exp(t_0X)p}(X)$.
- **T1.5.8 — Thm - Quotient by a Properly Discontinuous Action** (Thm. 1.5.23, p. 35). If a discrete group $G$ acts properly discontinuously on $M$ then $G\backslash M$ carries a unique differentiable structure such that $M\to G\backslash M$ is smooth and a covering map (hence a local diffeomorphism), and the universal property (as in T1.5.3(iii)) holds. `Proof in source: sketch.` Strategy: neighbourhoods $U$ as in (i) serve as charts; (ii) gives Hausdorff.
- **T1.5.9 — Thm - Left and Right Actions Correspond** (Rem. 1.5.27, p. 36). If $g\cdot p$ is a left action then $p*g := g^{-1}\cdot p$ is a right action; if $p\cdot g$ is a right action then $g*p := p\cdot g^{-1}$ is a left action. `Proof in source: full` (with $g*p := p\cdot g$, (i) reads $(gh)*p = h*(g*p)$).

### Examples
- **E1.5.1** (Ex. 1.5.3, pp. 27–28) Trivial action; action from a representation; multiplication and conjugation actions of $G$ on itself.
- **E1.5.2** (Ex. 1.5.6, p. 28) Trivial action effective ⇔ $G = \{e\}$ ⇔ free. Representation action never transitive ($\varrho(g)0 = 0$) unless $V = 0$. Left multiplication is free and transitive ($g = yx^{-1}$). Conjugation: $gxg^{-1} = x\ \forall x$ ⇔ $g\in Z(G)$; not effective iff $Z(G)\neq\{e\}$; not transitive unless one conjugacy class.
- **E1.5.3** (Ex. 1.5.7.1, p. 29) $SO(2)$ on $S^2$ by rotation about the $z$-axis, $g\cdot x := \begin{pmatrix}g&0\\0&1\end{pmatrix}x$: effective, not free (poles fixed), not transitive (latitude circles invariant).
- **E1.5.4** (Ex. 1.5.7.2, p. 29) $U(1)$ on $S^{2n-1}\subset\mathbb C^n$ by scalar multiplication: free ($zw = w$, $w\neq0$ ⇒ $z = 1$); transitive iff $n = 1$ ($zx = y$ forces linear dependence).
- **E1.5.5** (Ex. 1.5.9, p. 29) Orbits of the rotation action on $S^2$ are latitude circles and poles; orbit space $\cong[-1,1]$ via the $z$-coordinate. (Source says $G = U(1)$ here.)
- **E1.5.6** (Ex. 1.5.10, pp. 30–31) $U(1)$ on $S^3\subset\mathbb C^2$: $w,w'$ in the same orbit iff $w_1/w_2 = w_1'/w_2'\in\hat{\mathbb C}$; orbit space $=$ Riemann sphere; via stereographic projection with $u = w_1/w_2$, $\frac{1}{4+|u|^2}(4u,4-|u|^2) = \frac{1}{4|w_2|^2+|w_1|^2}(4w_1\bar w_2, 4|w_2|^2-|w_1|^2)$ — the Hopf map. Hopf circles in $\mathbb R^3$ after stereographic projection of $S^3$: $\mathbb R^3$ is a disjoint union of circles and one line; any two Hopf circles are linked (Hopf link). Figures on pp. 30–31.
- **E1.5.7** (Ex. 1.5.12, p. 31) $U(1)\backslash S^{2n-1}$ is a manifold (free action, compact group) and equals $\mathbb{CP}^{n-1}$.
- **E1.5.8** (Ex. 1.5.18, p. 33) Fundamental vector fields of $SO(2)$ on $S^2$ are tangent to latitude circles.
- **E1.5.9** (Ex. 1.5.24, pp. 35–36) $\mathbb Z$ on $\mathbb R$ by $(k,t)\mapsto k+t$ is properly discontinuous: (i) $U := (t-\tfrac12,t+\tfrac12)$; (ii) for $t-s\notin\mathbb Z$ set $\epsilon := \min_k|t-(s+k)|$, $U := (s-\epsilon/2,s+\epsilon/2)$, $V := (t-\epsilon/2,t+\epsilon/2)$. $\mathbb Z\backslash\mathbb R\cong S^1$ via $f(t) := (\cos2\pi t,\sin2\pi t)$ and the universal property; $\tilde f$ bijective with $d\tilde f\neq0$, hence a diffeomorphism.
- **E1.5.10** (Ex. 1.5.25, p. 36) $(\mathbb Q,+)$ with the discrete topology acting on $\mathbb R$ by translation is not properly discontinuous (orbits are dense); $\mathbb Q\backslash\mathbb R$ is not Hausdorff.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R1.5.1** (Rem. 1.5.21, p. 34) A discrete group is compact iff finite; the quotient theorem for compact groups motivates the search for a criterion for discrete groups.
- **R1.5.2** (Rem. 1.5.19, p. 34) Obstruction to free actions via $\chi(M) = 0$ — see T1.5.7.
- **R1.5.3** (p. 30) Visualisation of the Hopf fibration via stereographic projection of $S^3$ minus a point.

### External results imported without proof
- **I1.5.1** Slice theorem / quotient manifold theorem for free compact actions (Thm. 1.5.11).
- **I1.5.2** Quotient by properly discontinuous actions is a manifold and a covering (Thm. 1.5.23).
- **I1.5.3** Poincaré–Hopf / hairy ball theorem: a nowhere-vanishing vector field forces $\chi(M) = 0$; $\chi(S^{2n})\neq0$ (Rem. 1.5.19).
- **I1.5.4** Maximal rank of the Hopf map (Rem. 1.5.14).

---

# Chapter 2 — Bundle theory

## 2.1 Fiber bundles

`PDF pages: 37–40`

### Standing conventions and notation
- A fiber bundle is a triple $(E,\pi,B)$ with typical fiber $F$; $\pi$ surjective smooth; local trivialization $\psi_U: \pi^{-1}(U)\to U\times F$ with $\mathrm{pr}_1\circ\psi_U = \pi$.
- Fibers $E_x := \pi^{-1}(x)$; $E|_U := \pi^{-1}(U)$.
- **Convention (p. 39):** from now on sections are assumed smooth unless specified otherwise.
- Pull-back $\lambda^*E := \{(b',p)\in B'\times E\mid\lambda(b') = \pi(p)\}$, $\pi' := \mathrm{pr}_1$; $\mathrm{pr}_2$ identifies $(\lambda^*E)_{b_0'}\cong E_{\lambda(b_0')}$.

### Definitions
- **D2.1.1 — Def - Fiber Bundle** (Def. 2.1.1, p. 37). Let $E,B,F$ be differentiable manifolds and $\pi: E\to B$ a surjective smooth map. $(E,\pi,B)$ is a *fiber bundle with typical fiber $F$* iff each $x\in B$ has an open neighbourhood $U$ with a diffeomorphism $\psi_U: \pi^{-1}(U)\to U\times F$ such that $\mathrm{pr}_1\circ\psi_U = \pi|_{\pi^{-1}(U)}$. $B$ is the *base*, $E$ the *total space*, $\psi_U$ a *local trivialization over $U$*.
- **D2.1.2 — Def - Fiber of a Bundle** (Rem. 2.1.2, p. 37). $E_x := \pi^{-1}(x)$; $\psi_U|_{\pi^{-1}(x)}: \pi^{-1}(x)\to\{x\}\times F\cong F$ is a diffeomorphism, so all fibers are diffeomorphic to $F$.
- **D2.1.3 — Def - Trivial Fiber Bundle** (Ex. 2.1.3.1, p. 37). $(B\times F,\mathrm{pr}_1,B)$.
- **D2.1.4 — Def - Unit Sphere Bundle** (Ex. 2.1.3.2, p. 37). For a Riemannian $n$-manifold $(B,g)$: $E := \{X\in TB\mid\|X\|_g = 1\}$ with the foot-point projection; fiber $S^{n-1}$; trivializations from those of $TB$.
- **D2.1.5 — Def - Mapping Torus Bundle over the Circle** (Rem. 2.1.4, pp. 37–38). For a diffeomorphism $\phi: F\to F$, $\mathbb Z$ acts properly discontinuously on $\mathbb R\times F$ by $(k,(t,f))\mapsto(t+k,\phi^k(f))$; $E := \mathbb Z\backslash(\mathbb R\times F)$, $\pi: E\to\mathbb Z\backslash\mathbb R\cong S^1$ induced by $\mathrm{pr}_1$; $(E,\pi,S^1)$ is a fiber bundle with typical fiber $F$, obtained from $[0,1]\times F$ by gluing the fibers over $0$ and $1$ via $\phi$.
- **D2.1.6 — Def - Moebius Strip** (Ex. 2.1.5, p. 38). $F = (-1,1)$, $\phi(x) := -x$ in D2.1.5.
- **D2.1.7 — Def - Isomorphic Fiber Bundles and Trivial Bundle** (Def. 2.1.6, p. 38). $(E,\pi,B)$, $(E',\pi',B')$ are *isomorphic* iff there is a diffeomorphism $\psi: E\to E'$ with $\pi'\circ\psi = \pi$ (source's diagram has a single base $B$). A bundle is *trivial* iff isomorphic to $B\times F\to B$, equivalently iff it admits a global trivialization ($U = B$).
- **D2.1.8 — Def - Vector Bundle** (Def. 2.1.7, p. 38). A fiber bundle with typical fiber $\mathbb K^n$ is a *(real or complex) vector bundle of rank $n$* iff each fiber $E_x$ carries a $\mathbb K$-vector space structure and the local trivializations can be chosen with $\psi_U|_{\pi^{-1}(x)}: E_x\to\{x\}\times\mathbb K^n\cong\mathbb K^n$ a linear isomorphism.
- **D2.1.9 — Def - Section of a Fiber Bundle** (Def. 2.1.9, p. 39). A *section* is a map $s: B\to E$ with $\pi\circ s = \mathrm{id}_B$.
- **D2.1.10 — Def - Zero Section** (Rem. 2.1.10, p. 39). $s(x) := 0_x\in V_x$ for a vector bundle $V$.
- **D2.1.11 — Def - Pull-Back Bundle** (Def. 2.1.11, p. 40). For $\lambda: B'\to B$ smooth and $(E,\pi,B)$ a fiber bundle with fiber $F$: $E' := \{(b',p)\in B'\times E\mid\lambda(b') = \pi(p)\}$, $\pi' := \mathrm{pr}_1|_{E'}$; $\lambda^*(E,\pi,B) := (E',\pi',B')$ is the *pull-back of $(E,\pi,B)$ along $\lambda$*. The square with $\mathrm{pr}_2: \lambda^*E\to E$ commutes.

### Theorems
- **T2.1.1 — Thm - Mapping Torus Is a Fiber Bundle** (Rem. 2.1.4, pp. 37–38). `Proof in source: sketch` — use global triviality of $\mathbb R\times F\to\mathbb R$ plus proper discontinuity.
- **T2.1.2 — Thm - Pull-Back Is a Fiber Bundle** (pp. 39–40). $E'\subset B'\times E$ is a smooth submanifold, $(E',\pi',B')$ is a fiber bundle with fiber $F$, and $\mathrm{pr}_2: E'_{b_0'}\to E_{\lambda(b_0')}$ is a bijection. `Proof in source: full.` Strategy: for $b_0'$ choose $U\ni\lambda(b_0')$ with trivialization $\psi_U$, set $U' := \lambda^{-1}(U)$; then $\pi'^{-1}(U') = \{(b',p)\in U'\times E\mid\lambda(b') = \pi(p)\}\cong\{(b',u,f)\in U'\times U\times F\mid\lambda(b') = u\}\cong U'\times F$. Fiber: $E'_{b_0'} = \{b_0'\}\times E_{\lambda(b_0')}$. Gaps: submanifold property asserted from the local identification.

### Examples
- **E2.1.1** (Ex. 2.1.3.1) Trivial bundle. **E2.1.2** (Ex. 2.1.3.2) Unit sphere bundle. **E2.1.3** (Ex. 2.1.5) Möbius strip.
- **E2.1.4** (Ex. 2.1.8, p. 38) $TB$ and all bundles built fiberwise by linear algebra: $T^*B$, $\Lambda^kT^*B$, $\odot^kT^*B$, etc., are vector bundles.
- **E2.1.5** (table, p. 39) Sections: $TB$ ↔ vector fields; $T^*B$ ↔ 1-forms; $\Lambda^kT^*M$ ↔ $k$-forms; $\bigotimes^kTB\otimes\bigotimes^lT^*B$ ↔ $(k,l)$-tensor fields.
- **E2.1.6** (Ex. 2.1.12, p. 40) $E = TB$, $\lambda: (-\epsilon,\epsilon)\to B$ a curve: sections of $\lambda^*TB$ are vector fields along $\lambda$; the velocity field $\dot\lambda$ is one; variational fields/Jacobi fields are others.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R2.1.1** (Rem. 2.1.10, p. 39) Every vector bundle has smooth sections (zero section); general fiber bundles may have no continuous sections at all.

### External results imported without proof
- None beyond basic manifold theory.

---

## 2.2 Principal bundles

`PDF pages: 41–50`

### Standing conventions and notation
- $G$ acts on $P$ **from the right**; $p\cdot G = P_{\pi(p)}$; $L_p: G\to P_{\pi(p)}$, $L_p(g) := p\cdot g$ (source reuses $L$).
- Equivariance of trivializations (Def. 2.2.1(iii)): $\psi_U(p\cdot g) = (\pi(p), \psi_U^{G}(p)\cdot g)$, i.e. the diagram $\pi^{-1}(U)\times G\to\pi^{-1}(U)$ (action) vs. $U\times G\times G\xrightarrow{\mathrm{id}\times\mu_G}U\times G$ commutes.
- Associated bundle actions: $G$ acts on $P\times H$ by $(p,h)\cdot g := (p\cdot g,\ \varphi(g^{-1})\cdot h)$ and on $P\times V$ by $(p,v)\cdot g := (p\cdot g,\ \rho(g^{-1})v)$; classes $[p,h]$, $[p,v]$; $H$ acts on $P\times_\varphi H$ by $[p,h]\cdot h' := [p,hh']$.
- Local section from trivialization: $s(x) := \psi_U^{-1}(x,e)$; then $\psi_U^{-1}(x,g) = s(x)\cdot g$. Conversely $\psi_U(p) := (\pi(p), g(p))$ with $p = s(\pi(p))\cdot g(p)$.
- **Transition functions:** $s_\beta(x) = s_\alpha(x)\cdot g_{\alpha\beta}(x)$ on $U_{\alpha\beta} := U_\alpha\cap U_\beta$. **Cocycle conditions:** $g_{\alpha\alpha} = e$, $g_{\alpha\beta} = g_{\beta\alpha}^{-1}$, $g_{\alpha\beta}g_{\beta\gamma}g_{\gamma\alpha} = e$. **Coboundary condition (2.1):** if $\tilde s_\alpha = s_\alpha h_\alpha$ then $g_{\alpha\beta} = h_\alpha\tilde g_{\alpha\beta}h_\beta^{-1}$.
- **Bundle from cocycle:** $P := \bigsqcup_\alpha U_\alpha\times G/\sim$ with $(x,g)\in U_\alpha\times G\sim(x',g')\in U_\beta\times G$ iff $x = x'$ and $g = g_{\alpha\beta}(x)g'$.
- Table of structure groups for bundles of bases (p. 42): any $\mathbb K$-bundle → all bases → $GL(n;\mathbb K)$; real Riemannian → orthonormal → $O(n)$; complex Hermitian → orthonormal → $U(n)$; real oriented → positively oriented → $GL^+(n;\mathbb R) := \{\det>0\}$; real Riemannian oriented → oriented orthonormal → $SO(n)$.

### Definitions
- **D2.2.1 — Def - Principal Bundle** (Def. 2.2.1, p. 41). A fiber bundle $(P,\pi,B)$ with a right action of a Lie group $G$ on $P$ is a *$G$-principal bundle* iff (i) the action is free; (ii) transitive on fibers: $p\cdot G = P_{\pi(p)}$ for all $p$; (iii) local trivializations $\psi_U: \pi^{-1}(U)\to U\times G$ can be chosen equivariant: $\psi_U(p\cdot g) = (\mathrm{id}_U\times\mu_G)(\psi_U(p),g)$. $G$ is the *structure group*.
- **D2.2.2 — Def - Frame Bundle and Orthonormal Frame Bundle** (Def. 2.2.7, p. 42). For an $n$-manifold $B$, the $GL(n;\mathbb K)$-principal bundle of ordered bases of $TB$ (Ex. 2.2.5) is the *frame bundle*; for Riemannian $(B,g)$ the $O(n)$-bundle of orthonormal bases of $TB$ is the *orthonormal frame bundle*.
- **D2.2.3 — Def - Pull-Back of a Principal Bundle** (Rem. 2.2.8, p. 43). $\lambda^*P := \{(b',p)\in B'\times P\mid\lambda(b') = \pi(p)\}$ with $(b',p)\cdot g := (b',p\cdot g)$ is a $G$-principal bundle over $B'$.
- **D2.2.4 — Def - Associated Principal Bundle** (Def. 2.2.10, p. 44). For $\varphi: G\to H$ a Lie group homomorphism, $P\times_\varphi H := (P\times H)/G$ with the action above and $\pi'[p,h] := \pi(p)$ is the *$H$-principal bundle associated to $P$ with respect to $\varphi$*. If $\varphi$ is an embedding of a subgroup, $P\times_\varphi H$ is obtained by *extension of the structure group*; conversely a $G$-bundle $P$ whose extension is isomorphic to a given $H$-bundle $Q$ is a *reduction of $Q$ to the structure group $G$*.
- **D2.2.5 — Def - Associated Vector Bundle** (Def. 2.2.12, p. 44). For a representation $\rho: G\to\mathrm{Aut}(V)$: $P\times_\rho V := (P\times V)/G$ with $(p,v)\cdot g = (p\cdot g,\rho(g^{-1})v)$ is a vector bundle over $B$, the *associated vector bundle*.
- **D2.2.6 — Def - Transition Functions** (pp. 46–47). For local sections $s_\alpha$ over a cover $\{U_\alpha\}$: the unique smooth $g_{\alpha\beta}: U_{\alpha\beta}\to G$ with $s_\beta = s_\alpha\cdot g_{\alpha\beta}$; they satisfy the cocycle conditions.
- **D2.2.7 — Def - Coboundary Condition** (eq. (2.1), p. 47). Two systems $\{g_{\alpha\beta}\}$, $\{\tilde g_{\alpha\beta}\}$ are related by $\{h_\alpha: U_\alpha\to G\}$ iff $g_{\alpha\beta} = h_\alpha\tilde g_{\alpha\beta}h_\beta^{-1}$.
- **D2.2.8 — Def - Principal Bundle Reconstructed from a Cocycle** (pp. 47–48). $P := \bigsqcup_\alpha U_\alpha\times G/\sim$ as in conventions; motivated by $s_\beta(x)g_{\beta\alpha}(x)g = s_\alpha(x)g \overset{!}{=} s_\beta(x)g'$.
- **D2.2.9 — Def - Local Gauge** (Rem. 2.2.19, p. 50). Local sections (equivalently local trivializations) are *local gauges*; e.g. for $G = \mathbb R$ a local section identifies fiber points with real numbers — a choice of units.

### Theorems
- **T2.2.1 — Thm - Fibers of a Principal Bundle Are Diffeomorphic to G** (Rem. 2.2.2, p. 41). $L_p: G\to P_{\pi(p)}$, $g\mapsto p\cdot g$, is a diffeomorphism; the typical fiber is $G$; fibers carry no natural group structure. `Proof in source: full.` Strategy: injective by (i), surjective by (ii); $d_eL_p: X\mapsto\bar X(p)$ is injective for a free action (Rem. 1.5.19); $L_p = L_{p\cdot g}\circ L_{g^{-1}}$ gives $d_gL_p = d_eL_{pg}\circ d_gL_{g^{-1}}$, injective ∘ bijective.
- **T2.2.2 — Thm - Free Compact Action Gives a Principal Bundle** (Rem. 2.2.3, p. 41). If a compact group $G$ acts freely from the right on $P$, then $(P,\pi,G\backslash P)$ with $\pi(p) := p\cdot G$ is a $G$-principal bundle. `Proof in source: sketch` — (i),(ii) obvious, (iii) from the proof idea of Thm. 1.5.11.
- **T2.2.3 — Thm - Bundle of Bases Is a Principal Bundle** (Ex. 2.2.5, p. 42). For a rank-$n$ $\mathbb K$-vector bundle $V\to B$, $P_b := \{$ordered bases of $V_b\}$, $(b_1,\dots,b_n)\cdot A := (\sum_iA_{i1}b_i,\dots,\sum_iA_{in}b_i)$ is a free transitive right $GL(n;\mathbb K)$-action, and $P := \bigsqcup_bP_b\to B$ is a $GL(n;\mathbb K)$-principal bundle. `Proof in source: sketch (local triviality not written).`
- **T2.2.4 — Thm - Associated Principal Bundle Is a Principal Bundle** (Conclusion 2.2.9, pp. 43–44). $(P\times_\varphi H,\pi',B)$ is an $H$-principal bundle. `Proof in source: full for $G$ compact; general case asserted.` Strategy: the $G$-action on $P\times H$ is free (since it is free on $P$); for compact $G$ the quotient is a manifold (Rem. 2.2.3); $\pi\circ\mathrm{pr}_1$ is $G$-invariant so descends to $\pi'$; $H$ acts on $P\times H$ by $(p,h)\cdot h' = (p,hh')$, commutes with the $G$-action, descends; freeness: $[p,hh'] = [p,h]$ ⇒ $\exists g$: $(p,hh') = (pg,\varphi(g^{-1})h)$ ⇒ $g = e$ ⇒ $h' = e$. Gaps: non-compact $G$ ("also holds"); transitivity on fibers and local triviality not written; source misprints $P\times_\varphi G$ for $P\times_\varphi H$.
- **T2.2.5 — Thm - Reduction to the Trivial Group** (Ex. 2.2.11, p. 44). An $H$-principal bundle can be reduced to $G = \{e\}$ iff it is trivial. `Proof in source: omitted (stated).`
- **T2.2.6 — Thm - Vector Bundle Is Associated to Its Frame Bundle** (Ex. 2.2.13, pp. 44–45). For $E$ a $\mathbb K$-vector bundle with frame bundle $P$ and $\rho_{std}$ the standard representation: $P\times_{\rho_{std}}\mathbb K^n\cong E$, $[(b_1,\dots,b_n),(x_1,\dots,x_n)]\mapsto\sum_jx_jb_j$. `Proof in source: full (well-definedness):` $[b,x] = [b',x']$ ⇒ $(b',x') = (bg, g^{-1}x)$ ⇒ $b'x' = bgg^{-1}x = bx$.
- **T2.2.7 — Thm - Tensor Constructions Are Associated Bundles** (Rem. 2.2.14, p. 45). $P\times_{\Lambda^k\rho_{std}}\Lambda^k\mathbb K^n\cong\Lambda^kE$; likewise for tensor products, direct sums, duals. `Proof in source: omitted (stated).`
- **T2.2.8 — Thm - Local Trivializations Correspond to Local Sections** (Conclusion 2.2.15, pp. 45–46). There is a 1–1 correspondence {local trivializations over $U$} ↔ {local sections over $U$}; in particular a principal bundle has a global section iff it is trivial. `Proof in source: full.` Strategy: $\psi_U\mapsto s := \psi_U^{-1}(\cdot,e)$, with $\psi_U^{-1}(u,g) = s(u)\cdot g$ by equivariance; conversely, freeness and transitivity give a unique $g(p)$ with $p = s(\pi(p))\cdot g(p)$ and $\psi_U(p) := (\pi(p),g(p))$.
- **T2.2.9 — Thm - Hopf Bundle Has No Global Section** (Ex. 2.2.16, p. 46). The Hopf bundle $S^3\to S^2$ ($G = U(1)$) has no global section: otherwise $S^3\cong S^2\times S^1$ and $\{e\}\cong\pi_1(S^3)\cong\pi_1(S^2)\times\pi_1(S^1)\cong\mathbb Z$, contradiction. `Proof in source: full modulo $\pi_1$ facts.`
- **T2.2.10 — Thm - Cocycle Conditions** (p. 47). $g_{\alpha\alpha} = e$; $g_{\alpha\beta} = g_{\beta\alpha}^{-1}$ (from $s_\beta = s_\alpha g_{\alpha\beta} = s_\beta g_{\beta\alpha}g_{\alpha\beta}$ and freeness); $g_{\alpha\beta}g_{\beta\gamma}g_{\gamma\alpha} = e$ (from $s_\alpha = s_\beta g_{\beta\alpha} = s_\gamma g_{\gamma\beta}g_{\beta\alpha} = s_\alpha g_{\alpha\gamma}g_{\gamma\beta}g_{\beta\alpha}$). `Proof in source: full.`
- **T2.2.11 — Thm - Change of Local Sections Gives a Coboundary** (eq. (2.1), p. 47). If $\tilde s_\alpha = s_\alpha h_\alpha$ then $h_\beta = g_{\beta\alpha}h_\alpha\tilde g_{\alpha\beta}$, i.e. $g_{\alpha\beta} = h_\alpha\tilde g_{\alpha\beta}h_\beta^{-1}$. `Proof in source: full.`
- **T2.2.12 — Thm - Reconstruction from Transition Functions** (pp. 47–48). A cocycle $\{g_{\alpha\beta}\}$ defines a $G$-principal bundle $P = \bigsqcup U_\alpha\times G/\sim$; this reconstructs a given bundle up to isomorphism; the cocycle conditions make $\sim$ an equivalence relation; cohomologous cocycles (2.1) give isomorphic bundles via $[x,g]\mapsto[x,h_\alpha^{-1}(x)g]$. `Proof in source: well-definedness of the isomorphism full; the rest asserted.` Strategy for well-definedness: $g = g_{\alpha\beta}g' = h_\alpha\tilde g_{\alpha\beta}h_\beta^{-1}g'$ gives $\tilde g := h_\alpha^{-1}g$ and $\tilde g' := h_\beta^{-1}g'$ related by $\tilde g = \tilde g_{\alpha\beta}\tilde g'$.
- **T2.2.13 — Thm - Transition Function of the Hopf Bundle** (Ex. 2.2.17, pp. 48–49). With $\mathrm{Hopf}(w_1,w_2) = \frac{(4w_1\bar w_2,\,4|w_2|^2-|w_1|^2)}{4|w_2|^2+|w_1|^2}$ and, for $(z,t)\in S^2\subset\mathbb C\times\mathbb R$, the sections $s_1(z,t) := \left(\frac{4|z|^2}{(1+t)^2}+1\right)^{-1/2}\left(\frac{2z}{1+t},1\right)$ on $U_1 := S^2\setminus\{(0,-1)\}$ and $s_2(z,t) := \left(1+\frac{|z|^2/4}{(1-t)^2}\right)^{-1/2}\left(1,\frac{z/2}{1-t}\right)$ on $U_2 := S^2\setminus\{(0,1)\}$, one has $s_1\cdot\frac{z}{|z|} = s_2$, so $g_{12}: U_{12} = S^2\setminus\{(0,\pm1)\}\to U(1)$, $g_{12}(z,t) = z/|z|$. `Proof in source: full computation` using $(1-t)(1+t) = |z|^2$ and $(1+t)^2 = |z|^4/(1-t)^2$. Note: source additionally writes "$= |z|/z$", which contradicts $z/|z|$; the computed value is $z/|z|$.
- **T2.2.14 — Thm - Transition Functions of an Associated Bundle** (Rem. 2.2.18, p. 49). With $s'_\alpha(u) := [s_\alpha(u),e]$ as sections of $P' = P\times_\varphi H$: $g'_{\alpha\beta} = \varphi\circ g_{\alpha\beta}$. `Proof in source: full:` $s'_\beta = [s_\beta,e] = [s_\alpha g_{\alpha\beta},e] = [s_\alpha g_{\alpha\beta}g_{\beta\alpha},\varphi(g_{\beta\alpha}^{-1})e] = [s_\alpha,\varphi(g_{\alpha\beta})]$ vs. $s'_\beta = s'_\alpha g'_{\alpha\beta} = [s_\alpha,g'_{\alpha\beta}]$.

### Examples
- **E2.2.1** (Ex. 2.2.4, p. 42) Hopf fibration $S^{2n-1}\to\mathbb{CP}^{n-1}$ (source writes $\mathbb{CP}^n$) is a $U(1)$-principal bundle.
- **E2.2.2** (Ex. 2.2.5, p. 42) Bundle of bases of a vector bundle — $GL(n;\mathbb K)$.
- **E2.2.3** (Ex. 2.2.6, p. 42) Orthonormal bases for Riemannian/Hermitian bundles — $O(n)$/$U(n)$.
- **E2.2.4** (table, p. 42) Structure groups for bases respecting extra structure — see conventions.
- **E2.2.5** (Ex. 2.2.11, p. 44) Reduction to $\{e\}$ iff trivial.
- **E2.2.6** (Ex. 2.2.13, p. 44) $P\times_{\rho_{std}}\mathbb K^n\cong E$.
- **E2.2.7** (Ex. 2.2.16, p. 46) Hopf bundle non-trivial via $\pi_1$.
- **E2.2.8** (Ex. 2.2.17, pp. 48–49) Explicit sections and transition function $z/|z|$ of the Hopf bundle.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R2.2.1** (p. 41 fn.) The equivariance diagram in Def. 2.2.1(iii).
- **R2.2.2** (pp. 45–46) Derivation of $\psi_U^{-1}(u,g) = s(u)\cdot g$ from equivariance.
- **R2.2.3** (Rem. 2.2.19, p. 50) Physical reading of local sections as gauges/units.

### External results imported without proof
- **I2.2.1** $\pi_1(S^3) = 0$, $\pi_1(S^2) = 0$, $\pi_1(S^1) = \mathbb Z$, $\pi_1(X\times Y) = \pi_1X\times\pi_1Y$ (Ex. 2.2.16).
- **I2.2.2** Quotients $(P\times H)/G$ are manifolds also for non-compact $G$ (p. 43).
- **I2.2.3** Smoothness of $\pi'$ "by the general theory of group actions".

---

## 2.3 Connections

`PDF pages: 50–54`

### Standing conventions and notation
- $\omega\in\Omega^1(P;\mathfrak g)$ = section of $T^*P\otimes\mathfrak g$.
- **Connection conditions:** (1) $R_g^*\omega = \mathrm{Ad}_{g^{-1}}\circ\omega$ for all $g\in G$ (i.e. $\omega_{p\cdot g}(dR_gX) = \mathrm{Ad}_{g^{-1}}(\omega_p(X))$; source misprints "$R_g^* = \mathrm{Ad}_{g^{-1}}\circ\omega$"); (2) $\omega(\bar X(p)) = X$ for all $X\in\mathfrak g$, where $\bar X$ is the fundamental vector field of the right action ($\bar X(p) = \frac{d}{dt}|_0\,p\cdot\exp(tX) = dL_p(X)$).
- Horizontal subspace $H_p := \ker\omega_p$; $T_pP = H_p\oplus T_pP_{\pi(p)}$; $dR_g(H_p) = H_{pg}$; $\pi_H$ horizontal projection.
- Local connection forms $\omega_\alpha := s_\alpha^*\omega\in\Omega^1(U_\alpha;\mathfrak g)$, $s^*\omega(Y) = \omega(ds(Y))$.
- **Transformation law (2.2)/(2.3):** $\omega_\beta|_{u_0} = \mathrm{Ad}_{g_{\alpha\beta}(u_0)^{-1}}\circ\omega_\alpha|_{u_0} + d\big(g_{\alpha\beta}(u_0)^{-1}\cdot g_{\alpha\beta}\big)|_{u_0}$ (for matrix groups: $\omega_\beta = g_{\alpha\beta}^{-1}\omega_\alpha g_{\alpha\beta} + g_{\alpha\beta}^{-1}dg_{\alpha\beta}$).
- Christoffel symbols: $\Gamma^j_{ik} := (s^*\omega(\partial/\partial x^k))^j_i$ for $s = (\partial_1,\dots,\partial_n)$.
- Frame-bundle connection from a covariant derivative: $\frac{\nabla}{dt}|_0p_j(t) =: \sum_i\Gamma^i_j(X)p_i(0) =: (p(0)\cdot\omega(X))_j$.
- $\mathcal C(P) := \{$connection 1-forms on $P\}$, an affine space over $\Omega^1(B;P\times_{\mathrm{Ad}}\mathfrak g)$.
- Induced covariant derivative on $E = P\times_\varrho V$: $\nabla_X[p(u),v(u)] := [p(u_0),\ \partial_Xv + \varrho_*(p^*\omega(X))\,v(u_0)]$ for $X\in T_{u_0}B$.

### Definitions
- **D2.3.1 — Def - Connection 1-Form** (Def. 2.3.1, p. 50). A 1-form $\omega\in\Omega^1(P;\mathfrak g)$ on a $G$-principal bundle $P\to B$ is a *connection 1-form* iff (1) $R_g^*\omega = \mathrm{Ad}_{g^{-1}}\circ\omega$ for all $g\in G$; (2) $\omega(\bar X(p)) = X$ for all $X\in\mathfrak g$, $p\in P$. (Condition 2 fixes $\omega$ on vertical vectors, all of which are of the form $\bar X(p)$.)
- **D2.3.2 — Def - Horizontal Subspace** (p. 52). $H_p := \ker\omega_p\subset T_pP$; $H_p\oplus T_pP_{\pi(p)} = T_pP$, $\dim H_p = \dim B$.
- **D2.3.3 — Def - Local Connection Forms** (p. 53). $\omega_\alpha := s_\alpha^*\omega\in\Omega^1(U_\alpha;\mathfrak g)$ for local sections $s_\alpha$.
- **D2.3.4 — Def - Space of Connections** (Rem. 2.3.8, p. 54). $\mathcal C(P) := \{$connection 1-forms on $P\to B\}$; not a vector space ($0\notin\mathcal C(P)$); an infinite-dimensional affine space over $\Omega^1(B;P\times_{\mathrm{Ad}}\mathfrak g)$.
- **D2.3.5 — Def - Covariant Derivative Induced on an Associated Bundle** (Rem. 2.3.9, p. 54). For $\varrho: G\to\mathrm{Aut}(V)$, $E := P\times_\varrho V$, $X\in T_{u_0}B$, a local section $p$ of $P$ and $v: U\to V$: $\nabla_X[p(u),v(u)] := [p(u_0),\partial_Xv + \varrho_*(p^*\omega(X))v(u_0)]$.

### Theorems
- **T2.3.1 — Thm - Consistency of the Two Connection Conditions** (Rem. 2.3.2, pp. 50–51). Conditions (1) and (2) are compatible: $dR_g(\bar X(p)) = \overline{\mathrm{Ad}_{g^{-1}}X}(pg)$, so $\omega(dR_g\bar X(p)) = \mathrm{Ad}_{g^{-1}}X$ agrees with (1); replacing $\mathrm{Ad}_{g^{-1}}$ by $\mathrm{Ad}_g$ would be inconsistent. `Proof in source: full:` $dR_g(dL_p X) = \frac{d}{dt}|_0\,p\exp(tX)g = \frac{d}{dt}|_0\,pg\,g^{-1}\exp(tX)g = dL_{pg}(\mathrm{Ad}_{g^{-1}}X)$.
- **T2.3.2 — Thm - Covariant Derivative Gives a Connection on the Frame Bundle** (Ex. 2.3.3 "Fundamental example", p. 51). Let $\nabla$ be a covariant derivative on $V\to B$, $P$ the frame bundle ($G = GL(n;\mathbb K)$, $\mathfrak g = \mathrm{Mat}(n\times n;\mathbb K)$). For $X\in T_pP$ choose a curve $p(t) = (p_1(t),\dots,p_n(t))$ with $p(0) = p$, $\dot p(0) = X$, $c := \pi\circ p$; define $\omega(X)\in\mathfrak g$ by $\frac{\nabla}{dt}|_0p_j = (p(0)\cdot\omega(X))_j$. Then $\omega$ is well-defined and a connection 1-form. `Proof in source: full.` Strategy: independence of the curve since $\frac{\nabla}{dt}|_0p_j$ depends only on $X$; property (2): $p(t) := p\exp(tX)$ lies in a fiber so $\frac\nabla{dt} = \frac d{dt}$, giving $\omega(\bar X(p)) = X$; property (1): $\frac{\nabla}{dt}|_0(p(t)g) = (\frac\nabla{dt}|_0p(t))g$ gives $g\,\omega(dR_gX) = \omega(X)g$.
- **T2.3.3 — Thm - Christoffel Symbols Are the Local Connection Form** (Rem. 2.3.4, p. 52). For $s = (\partial_1,\dots,\partial_n)$ a local section of the frame bundle of $TB$: $\Gamma^j_{ik} = \Gamma^j_i(ds(\partial_k)) = (s^*\omega(\partial_k))^j_i$. `Proof in source: full (definition unwinding).`
- **T2.3.4 — Thm - Horizontal Distribution** (p. 52). $\omega_p|_{T_pP_{\pi(p)}}: T_pP_{\pi(p)}\to\mathfrak g$ is an isomorphism; $T_pP = H_p\oplus T_pP_{\pi(p)}$; $\dim H_p = \dim B$; $dR_g(H_p) = H_{pg}$. `Proof in source: full:` for $X\in H_p$, $\omega_{pg}(dR_gX) = \mathrm{Ad}_{g^{-1}}\omega(X) = 0$ so $dR_gH_p\subset H_{pg}$; equality by dimension.
- **T2.3.5 — Thm - Standard Connection on the Hopf Bundle** (Ex. 2.3.5, p. 53). On $S^3\subset\mathbb C^2\cong\mathbb R^4$ with $G = U(1)$, $\mathfrak g = i\mathbb R$, fundamental field of $X = i$: $\bar X(p) = p\cdot i$. Define $\omega_p(Y) := i\langle Y,p\cdot i\rangle$ (real scalar product on $\mathbb R^4$). Then $\omega$ is a connection 1-form with $H_p = (p\cdot i)^\perp$. `Proof in source: full:` $R_z^*\omega(Y) = i\langle zY,pzi\rangle = i\langle Y,pi\rangle$ since $z$ acts as an isometry, and $\mathrm{Ad}$ is trivial; $\omega(\bar X) = i\langle pi,pi\rangle = i$. (Source labels the two checks in swapped order.)
- **T2.3.6 — Thm - Transformation Law for Local Connection Forms** (eq. (2.2)/(2.3), p. 53). $\omega_\beta|_{u_0} = \mathrm{Ad}_{g_{\alpha\beta}(u_0)^{-1}}\circ\omega_\alpha|_{u_0} + d(g_{\alpha\beta}(u_0)^{-1}g_{\alpha\beta})|_{u_0}$. `Proof in source: full.` Strategy: write $s_\beta(u) = s_\alpha(u)g_{\alpha\beta}(u_0)\cdot g_{\alpha\beta}(u_0)^{-1}g_{\alpha\beta}(u)$, differentiate: $ds_\beta = dR_{g_{\alpha\beta}(u_0)}\circ ds_\alpha + dL_{s_\alpha(u_0)g_{\alpha\beta}(u_0)}\circ d(g_{\alpha\beta}(u_0)^{-1}g_{\alpha\beta})$; apply $\omega$ and use (1) on the first term and (2) on the second (which is a fundamental vector).
- **T2.3.7 — Thm - Connection Determined by Local Forms** (Ex. 2.3.6, p. 54). $\omega$ is uniquely determined by $(\omega_\alpha)_{\alpha}$ (condition 2 fixes $\omega$ at $s_\alpha(u)$, condition 1 along the fiber); conversely a family $\omega_\alpha\in\Omega^1(U_\alpha;\mathfrak g)$ satisfying (2.2) defines a unique connection. `Proof in source: sketch.`
- **T2.3.8 — Thm - Existence of Connections and Their Differences** (Ex. 2.3.7, p. 54). Every principal bundle has connection 1-forms (partition of unity). For $\omega,\tilde\omega\in\mathcal C(P)$: $\omega_\beta-\tilde\omega_\beta = \mathrm{Ad}_{g_{\alpha\beta}^{-1}}(\omega_\alpha - \tilde\omega_\alpha)$, so $[s_\alpha,(\omega_\alpha-\tilde\omega_\alpha)(X)]$ glue to a global section of $P\times_{\mathrm{Ad}}\mathfrak g$; differences of connections correspond to elements of $\Omega^1(B;P\times_{\mathrm{Ad}}\mathfrak g)$. `Proof in source: existence sketch; difference statement full.`
- **T2.3.9 — Thm - Connections Form an Affine Space** (Rem. 2.3.8, p. 54). $\mathcal C(P)$ is an affine space over $\Omega^1(B;P\times_{\mathrm{Ad}}\mathfrak g)$. `Proof in source: full (from T2.3.8).`
- **T2.3.10 — Thm - Induced Covariant Derivative Is Well-Defined** (Rem. 2.3.9, p. 54). The formula in D2.3.5 is independent of the representative $[p(u),v(u)] = [p(u)g(u),\varrho(g(u)^{-1})v(u)]$. `Proof in source: sketch ("A simple computation shows"); the displayed verification breaks off at the end of the page.` Gaps: the computation with $(pg)^*\omega = \mathrm{Ad}_{g^{-1}}p^*\omega + g^{-1}dg$ is not completed.

### Examples
- **E2.3.1** (Ex. 2.3.3, p. 51) Frame-bundle connection from $\nabla$.
- **E2.3.2** (Rem. 2.3.4, p. 52) Christoffel symbols.
- **E2.3.3** (Ex. 2.3.5, p. 53) Hopf bundle connection $\omega_p(Y) = i\langle Y,pi\rangle$.
- **E2.3.4** (Ex. 2.3.6, 2.3.7, p. 54) — see T2.3.7, T2.3.8 (source labels these "Examples").

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R2.3.1** (p. 50, figure) Vertical vectors are exactly the $\bar X(p)$; condition (2) fixes $\omega$ vertically.
- **R2.3.2** ("Local description of connections", p. 53) The derivation of (2.3).

### External results imported without proof
- **I2.3.1** Partition of unity argument for existence of connections.

---

## 2.4 Curvature

`PDF pages: 55–59`

### Standing conventions and notation
- $\Omega(X,Y) := d\omega(\pi_HX,\pi_HY)$.
- $[\eta,\varphi](X,Y) := [\eta(X),\varphi(Y)] - [\eta(Y),\varphi(X)]$ for $\eta,\varphi\in\Omega^1(P;\mathfrak g)$; hence $[\omega,\omega](X,Y) = 2[\omega(X),\omega(Y)]$.
- **Structure equation (2.4):** $\Omega = d\omega + \tfrac12[\omega,\omega]$.
- **Equivariance (2.5):** $R_g^*\Omega = \mathrm{Ad}_{g^{-1}}\circ\Omega$.
- Abelian case (2.6): $\Omega = d\omega$, $d\Omega = 0$.
- Local curvature forms $\Omega_\alpha := s_\alpha^*\Omega$; **local structure equation (2.7):** $\Omega_\alpha = d\omega_\alpha + \tfrac12[\omega_\alpha,\omega_\alpha]$; transformation $\Omega_\beta = \mathrm{Ad}_{g_{\alpha\beta}^{-1}}\circ\Omega_\alpha$ (no inhomogeneous term).
- Global curvature $\bar\Omega\in\Omega^2(B;P\times_{\mathrm{Ad}}\mathfrak g)$, $\bar\Omega|_{U_\alpha} := [s_\alpha,\Omega_\alpha]$, i.e. $\bar\Omega(X,Y) = [s_\alpha,\Omega_\alpha(X,Y)]$; if $G$ abelian, $\bar\Omega\in\Omega^2(B;\mathfrak g)$ with $\bar\Omega|_{U_\alpha} = \Omega_\alpha$.

### Definitions
- **D2.4.1 — Def - Curvature Form** (Def. 2.4.1, p. 55). For a connection $\omega$ on $P\to B$ with horizontal projection $\pi_H: T_pP\to H_p$, the 2-form $\Omega\in\Omega^2(P;\mathfrak g)$, $\Omega(X,Y) := d\omega(\pi_H(X),\pi_H(Y))$, is the *curvature form of $\omega$*.
- **D2.4.2 — Def - Bracket of Lie-Algebra-Valued 1-Forms** (Notation, p. 55). $[\eta,\varphi](X,Y) := [\eta(X),\varphi(Y)] - [\eta(Y),\varphi(X)]$.
- **D2.4.3 — Def - Local Curvature Forms** (p. 58). $\Omega_\alpha := s_\alpha^*\Omega\in\Omega^2(U_\alpha;\mathfrak g)$.
- **D2.4.4 — Def - Curvature 2-Form on the Base** (p. 58). $\bar\Omega\in\Omega^2(B;P\times_{\mathrm{Ad}}\mathfrak g)$ (a section of $\Lambda^2T^*B\otimes(P\times_{\mathrm{Ad}}\mathfrak g)$) defined by $\bar\Omega|_{U_\alpha}(X,Y) := [s_\alpha,\Omega_\alpha(X,Y)]$; well-defined by $\Omega_\beta = \mathrm{Ad}_{g_{\alpha\beta}^{-1}}\Omega_\alpha$.

### Theorems
- **T2.4.1 — Thm - Structure Equation** (Prop. 2.4.2, pp. 55–56). $\Omega = d\omega + \tfrac12[\omega,\omega]$. `Proof in source: full (three cases).` Strategy: (i) $X = \bar X',Y = \bar Y'$ vertical: $\Omega(X,Y) = 0$; $[\omega,\omega](X,Y) = 2[X',Y']$; $d\omega(X,Y) = \partial_XY' - \partial_YX' - \omega([\bar X',\bar Y']) = -[X',Y']$ using $[\bar X',\bar Y'] = \overline{[X',Y']}$ and constancy of $X',Y'$. (ii) both horizontal: $[\omega,\omega](X,Y) = 0$ and $\Omega(X,Y) = d\omega(X,Y)$. (iii) $X = \bar X'$ vertical, $Y$ horizontal: $[\omega,\omega](X,Y) = 0$; $d\omega(X,Y) = \partial_X(\omega Y) - \partial_Y(\omega X) - \omega([X,Y]) = 0 - 0 - 0$ since $[X,Y]$ is horizontal (Lemma 2.4.3); $\Omega(X,Y) = 0$. Gaps: in (i) the identity $\omega([\bar X',\bar Y']) = [X',Y']$ (i.e. $X\mapsto\bar X$ is a bracket homomorphism for the right action) is used silently.
- **T2.4.2 — Thm - Bracket of Fundamental and Horizontal Fields Is Horizontal** (Lemma 2.4.3, p. 56). For $X\in\mathfrak g$ and $Y$ a horizontal vector field, $[\bar X,Y]$ is horizontal. `Proof in source: full:` flow of $\bar X$ is $R_{\exp(tX)}$; $\omega([\bar X,Y]) = \omega(\mathcal L_{\bar X}Y) = \mathcal L_{\bar X}(\omega(Y)) - (\mathcal L_{\bar X}\omega)(Y) = 0 - \frac{d}{dt}|_0R^*_{\exp tX}\omega(Y) = -\frac d{dt}|_0\mathrm{Ad}_{\exp(-tX)}\omega(Y) = 0$.
- **T2.4.3 — Thm - Equivariance of the Curvature Form** (Lemma 2.4.4, pp. 56–57). $R_g^*\Omega = \mathrm{Ad}_{g^{-1}}\circ\Omega$. `Proof in source: full:` $dR_g$ preserves the splitting so $\pi_H\circ dR_g = dR_g\circ\pi_H$; then $(R_g^*\Omega)(X,Y) = (R_g^*d\omega)(\pi_HX,\pi_HY) = d(\mathrm{Ad}_{g^{-1}}\omega)(\pi_HX,\pi_HY) = \mathrm{Ad}_{g^{-1}}\Omega(X,Y)$.
- **T2.4.4 — Thm - Bianchi Identity** (Prop. 2.4.5, p. 57). $d\Omega$ vanishes on $H\times H\times H$. `Proof in source: full:` $d\Omega = \tfrac12d[\omega,\omega]$; $\eta := [\omega,\omega]$ vanishes if any argument is horizontal; for horizontal $X_1,X_2,X_3$ every term of $d\eta(X_1,X_2,X_3)$ (six-term formula) vanishes.
- **T2.4.5 — Thm - Abelian Curvature Is Closed** (Rem. 2.4.6, p. 57). If $G$ is abelian, $\Omega = d\omega$ and $d\Omega = 0$ (2.6). `Proof in source: full (immediate).`
- **T2.4.6 — Thm - Local Structure Equation and Gluing of Curvature** (pp. 57–58). (a) $\Omega_\alpha = d\omega_\alpha + \tfrac12[\omega_\alpha,\omega_\alpha]$ (2.7) — pull back (2.4) by $s_\alpha$. (b) $\Omega_\beta = \mathrm{Ad}_{g_{\alpha\beta}(u_0)^{-1}}\circ\Omega_\alpha$ at $u_0$ — differentiate $s_\beta = s_\alpha g_{\alpha\beta}$ as in (2.3); the second (vertical) term is killed by $\Omega$; the first gives $R^*_{g_{\alpha\beta}}\Omega\circ ds_\alpha = \mathrm{Ad}_{g_{\alpha\beta}^{-1}}\Omega_\alpha$. (c) Hence $[s_\beta,\Omega_\beta(X,Y)] = [s_\alpha g_{\alpha\beta},\mathrm{Ad}_{g_{\alpha\beta}^{-1}}\Omega_\alpha(X,Y)] = [s_\alpha,\Omega_\alpha(X,Y)]$, so the $[s_\alpha,\Omega_\alpha]$ are restrictions of a global $\bar\Omega\in\Omega^2(B;P\times_{\mathrm{Ad}}\mathfrak g)$; if $G$ abelian, $\Omega_\beta = \Omega_\alpha$ and $\bar\Omega\in\Omega^2(B;\mathfrak g)$. `Proof in source: full.`
- **T2.4.7 — Thm - Curvature of the Hopf Connection** (Ex. 2.4.7, p. 59). For $\omega_p(Y) = i\langle ip,Y\rangle$ on $S^3$: $\Omega_p(X,Y) = d\omega_p(X,Y) = 2i\langle iX,Y\rangle$; it vanishes on vertical $X = ip$ since $\Omega_p(ip,Y) = 2i\langle-p,Y\rangle = 0$ for $Y\in T_pS^3 = p^\perp$. `Proof in source: full:` $d\omega(X,Y) = \partial_X\omega(Y) - \partial_Y\omega(X) - \omega([X,Y]) = i\langle ip,\partial_XY\rangle + i\langle iX,Y\rangle - i\langle ip,\partial_YX\rangle - i\langle iY,X\rangle - i\langle ip,[X,Y]\rangle = i(\langle iX,Y\rangle - \langle iY,X\rangle) = 2i\langle iX,Y\rangle$ (using $\langle iY,X\rangle = \langle i^2Y,iX\rangle = -\langle iX,Y\rangle$... source: $\langle iY,X\rangle = \langle X,iY\rangle$, $\langle iX,Y\rangle - \langle iX,i^2Y\rangle$ with $i$ an isometry).

### Examples
- **E2.4.1** (Ex. 2.4.7, p. 59) Curvature of the Hopf connection.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R2.4.1** (p. 58) In the abelian case (2.7) is linear in $\omega_\alpha$; in general it is a semilinear first-order PDE for $\omega_\alpha$.
- **R2.4.2** (pp. 57–58) The full computation of the transformation of $\Omega_\alpha$ and the gluing to $\bar\Omega$ (T2.4.6).

### External results imported without proof
- **I2.4.1** Cartan formula $\mathcal L_X = d\iota_X + \iota_Xd$ / Leibniz rule for $\mathcal L_{\bar X}$ on $\omega(Y)$ (Lemma 2.4.3).
- **I2.4.2** Flow of $\bar X$ is $R_{\exp(tX)}$ (from Rem. 1.5.19, right-action version).

---

## 2.5 Characteristic classes

`PDF pages: 59–65`

### Standing conventions and notation
- $\lambda: \mathfrak g\times\dots\times\mathfrak g\to\mathbb K$ ($k$ factors) multilinear, symmetric, **invariant**: $\lambda(\mathrm{Ad}_gX_1,\dots,\mathrm{Ad}_gX_k) = \lambda(X_1,\dots,X_k)$.
- $\lambda$ descends fiberwise to $P\times_{\mathrm{Ad}}\mathfrak g$: $([p,X_1],\dots,[p,X_k])\mapsto\lambda(X_1,\dots,X_k)$.
- **$\lambda\circ\bar\Omega\in\Omega^{2k}(B;\mathbb K)$:** $(\lambda\circ\bar\Omega)(X_1,\dots,X_{2k}) := \frac1{k!}\sum_{\sigma\in S_{2k}}\mathrm{sign}(\sigma)\,\lambda\big(\bar\Omega(X_{\sigma(1)},X_{\sigma(2)}),\dots,\bar\Omega(X_{\sigma(2k-1)},X_{\sigma(2k)})\big)$; in a basis $Y_1,\dots,Y_N$ of $\mathfrak g$ with $\Omega_\alpha = \sum_j\Omega_\alpha^jY_j$: $\lambda(\bar\Omega)|_{U_\alpha} = \sum_{j_1,\dots,j_k}\Omega^{j_1}_\alpha\wedge\dots\wedge\Omega^{j_k}_\alpha\cdot\lambda(Y_{j_1},\dots,Y_{j_k})$.
- de Rham cohomology $H^k_{dR}(M;\mathbb K)$; Betti numbers $b_k$.
- $c_\lambda(P) := [\lambda\circ\bar\Omega]\in H^{2k}(B;\mathbb K)$.
- **Chern classes:** $c_1$ from $\lambda(A) = \frac{1}{2\pi i}\mathrm{tr}A$; $c_n$ from $\lambda(A_1,\dots,A_n) = \frac1{(2\pi i)^n}A_1\wedge\dots\wedge A_n\in\mathrm{End}(\Lambda^n\mathbb C^n)\cong\mathbb C$ (for $G = GL(n;\mathbb C)$ or $U(n)$; $\mathbb K = \mathbb C$ resp. $\mathbb R$).
- **Euler class:** $G = SO(2m)$, $\mathfrak{so}(2m)\cong\Lambda^2\mathbb R^{2m}$, $\lambda(\sigma_1,\dots,\sigma_m) := \sigma_1\wedge\dots\wedge\sigma_m\in\Lambda^{2m}\mathbb R^{2m}\cong\mathbb R$, Pfaffian $\mathrm{Pf}(\sigma) := \lambda(\sigma,\dots,\sigma)$, $e(P) := \left[\frac{\mathrm{Pf}(\bar\Omega)}{(2\pi)^m\,m!}\right]\in H^{2m}(B;\mathbb R)$.
- Maurer–Cartan form on $G$: $\phi_g := dL_{g^{-1}}: T_gG\to\mathfrak g$, satisfying $d\phi + \tfrac12[\phi,\phi] = 0$.

### Definitions
- **D2.5.1 — Def - Invariant Multilinear Function** (Def. 2.5.1, p. 59). A multilinear symmetric $\lambda: \mathfrak g^k\to\mathbb K$ is *invariant* iff $\lambda(\mathrm{Ad}_gX_1,\dots,\mathrm{Ad}_gX_k) = \lambda(X_1,\dots,X_k)$ for all $g\in G$, $X_i\in\mathfrak g$.
- **D2.5.2 — Def - Characteristic Form lambda of Omega** (p. 59). $\lambda\circ\bar\Omega\in\Omega^{2k}(B;\mathbb K)$ as in conventions.
- **D2.5.3 — Def - de Rham Cohomology and Betti Numbers** (Def. 2.5.4, p. 61). $H^k_{dR}(M;\mathbb K) := \ker(d:\Omega^k\to\Omega^{k+1})/\mathrm{im}(d:\Omega^{k-1}\to\Omega^k)$; $b_k(M) := \dim_{\mathbb R}H^k(M;\mathbb R)$; well-defined since $d\circ d = 0$.
- **D2.5.4 — Def - Characteristic Class** (Def. 2.5.5, p. 61). $c_\lambda(P) := [\lambda\circ\bar\Omega]\in H^{2k}(B;\mathbb K)$, the *characteristic class of $P\to B$ associated with $\lambda$*.
- **D2.5.5 — Def - First Chern Class** (Ex. 2.5.11, p. 64). For $G = GL(n;\mathbb C)$ or $U(n)$, $\lambda(A) := \frac1{2\pi i}\mathrm{tr}(A)$: $c_1(P) := c_\lambda(P)$.
- **D2.5.6 — Def - n-th Chern Class** (Ex. 2.5.13, p. 65). $\lambda(A_1,\dots,A_n) := \frac1{(2\pi i)^n}A_1\wedge\dots\wedge A_n\in\mathrm{End}(\Lambda^n\mathbb C^n)\cong\mathbb C$: $c_n(P) := c_\lambda(P)$.
- **D2.5.7 — Def - Pfaffian and Euler Class** (Ex. 2.5.14, p. 65). As in conventions; $e(P)\in H^{2m}(B;\mathbb R)$ for an $SO(2m)$-bundle.

### Theorems
- **T2.5.1 — Thm - Invariant Functions Descend to the Adjoint Bundle** (p. 59). The fiberwise map $([p,X_1],\dots,[p,X_k])\mapsto\lambda(X_1,\dots,X_k)$ on $P\times_{\mathrm{Ad}}\mathfrak g$ is well-defined. `Proof in source: full` (representatives $[pg,\mathrm{Ad}_{g^{-1}}X_i]$ give the same value by invariance).
- **T2.5.2 — Thm - Characteristic Forms Are Closed** (Lemma 2.5.2, pp. 60–61). $d(\lambda\circ\bar\Omega) = 0$. `Proof in source: full.` Strategy: at $b\in U_\alpha$ choose the local section $s_\alpha$ with $ds_\alpha(T_bB) = H_{s_\alpha(b)}$; then $d\Omega_\alpha(X,Y,Z) = (d\Omega)(ds_\alpha X,ds_\alpha Y,ds_\alpha Z) = 0$ at $b$ by Bianchi (2.4.5); expand $\lambda(\bar\Omega) = \sum\Omega^{j_1}_\alpha\wedge\dots\wedge\Omega^{j_k}_\alpha\lambda(Y_{j_1},\dots,Y_{j_k})$ and apply Leibniz: each term contains some $d\Omega^{j}_\alpha$, which vanishes at $b$; $b$ arbitrary. Gaps: existence of a local section horizontal at a given point is asserted.
- **T2.5.3 — Thm - Characteristic Class Independent of Connection** (Lemma 2.5.3, p. 61). If $\omega'$ is another connection with curvature $\bar\Omega'$, then $\lambda\circ\bar\Omega - \lambda\circ\bar\Omega'$ is exact. `Proof in source: omitted.`
- **T2.5.4 — Thm - Naturality of Characteristic Classes** (Rem. 2.5.7, pp. 62–63, eq. (2.8)). For $f: M\to B$ smooth: $c_\lambda(f^*P) = f^*c_\lambda(P)\in H^{2k}(M;\mathbb K)$. `Proof in source: full.` Strategy: $\mathrm{pr}_2^*\omega$ is a connection on $f^*P$ ($R_g^*\mathrm{pr}_2^*\omega = \mathrm{pr}_2^*R_g^*\omega = \mathrm{Ad}_{g^{-1}}\mathrm{pr}_2^*\omega$ since $\mathrm{pr}_2\circ R_g = R_g\circ\mathrm{pr}_2$; $(\mathrm{pr}_2^*\omega)(\bar X) = \omega(\bar X) = X$); its curvature is $\Omega' = \mathrm{pr}_2^*\Omega$; with $V_\alpha := f^{-1}(U_\alpha)$, $s'_\alpha := \mathrm{pr}_2^{-1}\circ s_\alpha\circ f$: $\Omega'_\alpha = f^*\Omega_\alpha$; hence $f^*\lambda(\bar\Omega) = \lambda(\bar\Omega')$.
- **T2.5.5 — Thm - Isomorphic Bundles Have Equal Characteristic Classes** (Rem. 2.5.8, p. 63). If $\phi: P\to P'$ is an isomorphism of $G$-bundles, $c_\lambda(P) = c_\lambda(P')$. `Proof in source: full:` $\omega' := \phi_*\omega$ (source writes $\phi^*\omega$) is a connection on $P'$ with $\Omega' = \phi_*\Omega$; sections $s'_\alpha := \phi\circ s_\alpha$ (source: $\phi^{-1}\circ s_\alpha$) give $\Omega'_\alpha = \Omega_\alpha$.
- **T2.5.6 — Thm - Trivial Bundles Have Vanishing Characteristic Classes** (Rem. 2.5.9, pp. 63–64). For $k\ge1$ and $P$ trivial, $c_\lambda(P) = 0$. `Proof in source: full.` Strategy: reduce to $P = B\times G$; $\omega := \mathrm{pr}_2^*\phi$ with $\phi_g := dL_{g^{-1}}$ is a connection (property 1: $R_g^*\phi_{g'} = dL_{g'^{-1}}\circ dR_g = \mathrm{Ad}_{g^{-1}}\circ dL_{(g'g)^{-1}}$... source's chain: $\mathrm{pr}_2^*(dL_{(g')^{-1}}\circ dR_g) = \mathrm{Ad}_{g^{-1}}\circ\mathrm{pr}_2^*\phi_{g'g^{-1}}$; property 2: $\phi(\bar X) = X$); curvature $\Omega = \mathrm{pr}_2^*(d\phi + \tfrac12[\phi,\phi])$; for left-invariant $X,Y$: $d\phi(X,Y) = -[X,Y](e)$... source: $d\phi(X,Y) = \partial_X(Y(e)) - \partial_Y(X(e)) - [X,Y](e) = [X,Y](e)$ (sign as printed; intended $-[X,Y]$) and $[\phi,\phi](X,Y) = 2[X,Y]$, so $d\phi + \tfrac12[\phi,\phi] = 0$ and $\Omega = 0$. Gaps: sign slip in the printed $d\phi(X,Y)$; the labelling of $g'g^{-1}$ vs $g'g$ in the equivariance check is garbled.
- **T2.5.7 — Thm - Non-Vanishing Characteristic Class Obstructs Triviality** (Cor. 2.5.10, p. 64). If $c_\lambda(P)\neq0\in H^{2k}(B;\mathbb K)$, $k\ge1$, then $P$ is not trivial. `Proof in source: full (from T2.5.6).`
- **T2.5.8 — Thm - Integral of the Curvature Detects Non-Triviality of a Circle Bundle** (Ex. 2.5.12, p. 64). For a $U(1)$-bundle $P$ over a closed surface $B$: $c_1(P) = [\frac1{2\pi i}\bar\Omega]\in H^2_{dR}(B;\mathbb R)$; if $c_1(P) = 0$ then $\bar\Omega = d\eta$ for some $\eta\in\Omega^1(B;i\mathbb R)$ and $\int_B\bar\Omega = \int_{\partial B}\eta = 0$ by Stokes; hence $\int_B\bar\Omega\neq0$ ⇒ $P$ non-trivial. `Proof in source: full.`
- **T2.5.9 — Thm - Euler Class Equals First Chern Class for Circle Bundles** (Ex. 2.5.15, p. 65). For $G = SO(2) = U(1)$: $\mathfrak{so}(2)\cong\mathbb R$, $\mathfrak u(1)\cong i\mathbb R$, $\mathrm{Pf}(\sigma) = \sigma$, $\mathrm{tr}(A) = A$, so $e(P) = [\mathrm{Pf}(\bar\Omega)/(2\pi)] = [\mathrm{tr}(\bar\Omega)/(2\pi i)] = c_1(P)$. `Proof in source: full.`

### Examples
- **E2.5.1** (Ex. 2.5.11, p. 64) First Chern class.
- **E2.5.2** (Ex. 2.5.12, p. 64) $U(1)$-bundles over closed surfaces: $\int_B\bar\Omega\neq0$ ⇒ non-trivial.
- **E2.5.3** (Ex. 2.5.13, p. 65) $n$-th Chern class.
- **E2.5.4** (Ex. 2.5.14, p. 65) Euler class of an $SO(2m)$-bundle via the Pfaffian.
- **E2.5.5** (Ex. 2.5.15, p. 65) $e = c_1$ for $SO(2) = U(1)$.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R2.5.1** (Rem. 2.5.6, p. 62) Lemma 2.5.2 says $\lambda\circ\bar\Omega$ represents a de Rham class; Lemma 2.5.3 says the class is independent of the connection.
- **R2.5.2** (Rem. 2.5.7, pp. 62–63) Pull-back connections and the naturality computation (T2.5.4).
- **R2.5.3** (Rem. 2.5.9, pp. 63–64) Maurer–Cartan form on $B\times G$ is flat — the mechanism behind T2.5.6.

### External results imported without proof
- **I2.5.1** Lemma 2.5.3 (transgression / independence of connection).
- **I2.5.2** $\mathfrak{so}(2m)\cong\Lambda^2\mathbb R^{2m}$ and the Pfaffian as an invariant polynomial (Ex. 2.5.14).
- **I2.5.3** Stokes' theorem on a closed surface (Ex. 2.5.12).

---

## 2.6 Parallel transport

`PDF pages: 65–75`

### Standing conventions and notation
- $P\to B$ with a fixed connection $\omega$ throughout; $I$ an interval; curves piecewise smooth.
- Horizontal lift $\tilde c$ of $c$: (i) $\pi\circ\tilde c = c$ (source misprints "$c = \tilde c\circ\pi$"); (ii) $\dot{\tilde c}(t)\in H_{\tilde c(t)}$; (iii) $\tilde c(t_0) = p$.
- Ansatz $\tilde c(t) = s_\alpha(c(t))\cdot h_\alpha(t)$, $\dot s_\alpha(t_1) := \frac d{dt}|_{t_1}s_\alpha(c(t))$; **lift ODE (2.9):** $\dot h_\alpha(t_1) = -dR_{h_\alpha(t_1)}\big(\omega(\dot s_\alpha(t_1))\big)$; matrix case $\dot h_\alpha = -\omega(\dot s_\alpha)\,h_\alpha$ (linear).
- **Linear ODE (2.10):** $\dot v(t) = -A(t)v(t)$, $v(0) = v_0$, $A: [0,L]\to\mathrm{Mat}(n\times n;\mathbb K)$ continuous.
- **Path-ordered exponential (2.13)/(2.14):** $\mathcal P\exp\big(-\int_0^tA(\tau)d\tau\big) := \sum_{j=0}^\infty(-1)^j\int_0^td\tau_j\int_0^{\tau_j}d\tau_{j-1}\cdots\int_0^{\tau_2}d\tau_1\,A(\tau_j)A(\tau_{j-1})\cdots A(\tau_1) = \lim_{N\to\infty}\big(1_n - \tfrac tNA(\tfrac{N-1}Nt)\big)\cdots\big(1_n - \tfrac tNA(\tfrac1Nt)\big)\big(1_n - \tfrac tNA(0)\big)$.
- $\Gamma(c): P_{c(t_0)}\to P_{c(t_1)}$ parallel transport; $c_2*c_1$ concatenation.
- Abelian holonomy: $\Gamma(c) = \exp(-\int_c\omega_\alpha) = \exp(-\int_S\Omega_\alpha)$ for $c = \partial S$, $S\subset U_\alpha$.
- Small-loop expansion (2.15) and result: $\Gamma(c_L) = 1_n - \int_{S_L}\Omega_\alpha + O(L^3)$ as $L\searrow0$, for loops $c_L$ of length $O(L)$ bounding $S_L$ of area $O(L^2)$ inside a ball of radius $CL$, parametrised proportionally to arc length; $I_s, I_a$ the symmetric/antisymmetric parts of the second-order term; coordinates $x^1,\dots,x^n$ centred at $b_0$, $\omega_\alpha = \omega_jdx^j$.

### Definitions
- **D2.6.1 — Def - Horizontal Lift** (Lemma 2.6.1, p. 65). For $c: I\to B$, $t_0\in I$, $p\in P_{c(t_0)}$: the unique curve $\tilde c: I\to P$ with $\pi\circ\tilde c = c$, $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ for all $t$, and $\tilde c(t_0) = p$ is the *horizontal lift of $c$ with initial condition $\tilde c(t_0) = p$*.
- **D2.6.2 — Def - Parallel Section Along a Curve** (Rem. 2.6.3, p. 67). For $\mathcal V := P\times_\varrho V$ and a horizontal lift $\tilde c$, $t\mapsto[\tilde c(t),v]$ ($v\in V$ fixed) is a *parallel section of $\mathcal V$ along $c$*: $\frac\nabla{dt}[\tilde c(t),v] = [\tilde c(t),\frac{dv}{dt} + \varrho_*(\omega_{\tilde c(t)}(\dot{\tilde c}))\,v]$... (source writes $\omega_{\tilde c(t)}(\dot s_\alpha(t))$) $= 0$.
- **D2.6.3 — Def - Parallel Transport** (Def. 2.6.4, p. 67). For $c: [t_0,t_1]\to B$: $\Gamma(c): P_{c(t_0)}\to P_{c(t_1)}$, $\Gamma(c)(p) := \tilde c(t_1)$ where $\tilde c$ is the horizontal lift with $\tilde c(t_0) = p$.
- **D2.6.4 — Def - Path-Ordered Exponential** (Def. 2.6.8, p. 72). The solution operator of (2.10), $\mathcal P\exp(-\int_0^tA(\tau)d\tau)$, given by (2.13) = (2.14); $v(t) = \mathcal P\exp(-\int_0^tA)\,v_0$.

### Theorems
- **T2.6.1 — Thm - Existence and Uniqueness of Horizontal Lifts** (Lemma 2.6.1, pp. 65–66). For any (piecewise) smooth $c: I\to B$, $t_0\in I$, $p\in P_{c(t_0)}$ there is a unique (piecewise) smooth horizontal lift $\tilde c$ with $\tilde c(t_0) = p$. `Proof in source: full (reduction to ODE); global existence in Rem. 2.6.2.` Strategy: w.l.o.g. $c$ smooth with $c(I)\subset U_\alpha$; (i) ⇔ $\tilde c(t) = s_\alpha(c(t))h_\alpha(t)$; (iii) fixes $h_\alpha(t_0)$; (ii) ⇔ $0 = \omega(\dot{\tilde c}(t_1)) = \omega\big(dL_{s_\alpha(c(t_1))h_\alpha(t_1)}\frac d{dt}|_{t_1}(h_\alpha(t_1)^{-1}h_\alpha(t)) + dR_{h_\alpha(t_1)}\dot s_\alpha(t_1)\big) = dL_{h_\alpha(t_1)^{-1}}\dot h_\alpha(t_1) + \mathrm{Ad}_{h_\alpha(t_1)^{-1}}\omega(\dot s_\alpha(t_1))$; apply $dL_{h_\alpha(t_1)}$ to get (2.9), a first-order ODE with unique solution on all of $I$.
- **T2.6.2 — Thm - Global Existence of the Lift ODE** (Rem. 2.6.2, p. 67). The solution of (2.9) exists on all of $I$. `Proof in source: full.` Strategy: matrix groups: (2.9) is linear, $\dot h_\alpha = -\omega(\dot s_\alpha)h_\alpha$. General: if the maximal solution stops at $t_1<\sup I$, take a horizontal lift $\hat c$ near $t_1$, pick $\tau<t_1$ and $g$ with $\tilde c(\tau) = \hat c(\tau)g$; $\bar c := \hat c\cdot g$ is a horizontal lift (Rem. 2.6.5.5) agreeing with $\tilde c$ at $\tau$, hence everywhere both are defined, extending $\tilde c$ beyond $t_1$ — contradiction.
- **T2.6.3 — Thm - Horizontal Lifts Give Parallel Sections** (Rem. 2.6.3, p. 67). $t\mapsto[\tilde c(t),v]$ is parallel; for $P$ the frame bundle of $E$ and $\varrho$ standard, $\tilde c(t) = (b_1(t),\dots,b_n(t))$ is horizontal iff the $b_i$ are parallel. `Proof in source: full (one-line computation via D2.3.5).`
- **T2.6.4 — Thm - Properties of Parallel Transport** (Rem. 2.6.5, p. 68). (1) $c$ constant ⇒ $\Gamma(c) = \mathrm{id}$. (2) $c' = c\circ\phi$, $\phi$ orientation-preserving reparametrisation ⇒ $\Gamma(c') = \Gamma(c)$. (3) $\phi$ orientation-reversing ⇒ $\Gamma(c') = \Gamma(c)^{-1}$; hence $\Gamma(c)$ is a diffeomorphism. (4) $\Gamma(c_2*c_1) = \Gamma(c_2)\circ\Gamma(c_1)$. (5) If $\tilde c$ is the lift with $\tilde c(t_0) = p$ then $\tilde c\cdot g$ is the lift with $\tilde c(t_0) = pg$; hence $R_g\circ\Gamma(c) = \Gamma(c)\circ R_g$. `Proof in source: full (brief).`
- **T2.6.5 — Thm - Solution of a Commuting Linear ODE** (pp. 68–69). If all $A(t)$ commute (values in an abelian subalgebra), the solution of (2.10) is $v(t) = \exp(-\int_0^tA(\tau)d\tau)v_0$. `Proof in source: full` — differentiate the series termwise, using commutativity to move $A(t)$ to the front: $\dot v = \sum_{j\ge1}\frac{(-1)^j}{j!}jA(t)(\int_0^tA)^{j-1}v_0 = -A(t)v(t)$; in general there is an ordering problem.
- **T2.6.6 — Thm - Path-Ordered Exponential Solves the Linear ODE** (Lemma 2.6.7, pp. 69–71). For continuous $A: [0,L]\to\mathrm{Mat}(n\times n;\mathbb K)$, the solution of (2.10) is $v(t) = \sum_{j\ge0}(-1)^j\int_0^td\tau_j\int_0^{\tau_j}d\tau_{j-1}\cdots\int_0^{\tau_2}d\tau_1A(\tau_j)\cdots A(\tau_1)v_0$ (2.11) $= \lim_{N\to\infty}\prod_{k=N-1}^{0}(1_n - \tfrac tNA(\tfrac kNt))v_0$ (2.12). `Proof in source: full (four steps).` (a) Euler scheme: $v(s+\epsilon) = (1_n-\epsilon A(s))v(s) + O(\epsilon^2)$; iterate with $\epsilon = t/N$ to get (2.12) with error $N\cdot O(t^2/N^2) = O(1/N)$. (b) Induction: $\int_0^td\tau_j\cdots\int_0^{\tau_2}d\tau_1 = t^j/j!$. (c) Operator-norm bound $\|j\text{-th term}\|_{C^0}\le\frac{L^j}{j!}\|A\|^j_{C^0}$ and $\|\frac d{dt}(j\text{-th term})\|_{C^0}\le\frac{L^{j-1}}{(j-1)!}\|A\|^j_{C^0}$, so the series converges absolutely in $C^1(I;\mathrm{Mat})$ and may be differentiated termwise. (d) Termwise differentiation gives $\dot v = -A(t)v(t)$. Gaps: the $O(\epsilon^2)$ uniformity in (a) is not justified (needs $A$ differentiable or a Lipschitz-type argument); the source's (a) proves (2.12) only heuristically.
- **T2.6.7 — Thm - Holonomy of an Abelian Connection** (Rem. 2.6.9, p. 72). $G$ abelian, $c$ a closed curve in $U_\alpha$ bounding $S\subset U_\alpha$: $\Gamma(c) = \exp(-\int_I\omega_\alpha(\dot c)dt) = \exp(-\int_c\omega_\alpha) = \exp(-\int_Sd\omega_\alpha) = \exp(-\int_S\Omega_\alpha)$; so $\Gamma(c)\neq\mathrm{id}$ in general if $\Omega\neq0$. `Proof in source: full (Stokes + T2.6.5).`
- **T2.6.8 — Thm - Small-Loop Holonomy Expansion** (pp. 72–75, eq. (2.15)). For a matrix group $G$ and loops $c_L$ at $b_0$ as in conventions: $\Gamma(c_L) = 1_n - \int_{S_L}\Omega_\alpha + O(L^3)$ as $L\searrow0$. `Proof in source: full (long computation).` Strategy: (1) Dyson expansion (2.15): $\Gamma(c) = 1_n - \int_0^1\omega_\alpha(\dot c) + \int_0^1d\tau_2\int_0^{\tau_2}d\tau_1\,\omega_\alpha(\dot c(\tau_2))\omega_\alpha(\dot c(\tau_1)) + O(L^3)$. (2) First-order term $= \int_c\omega_\alpha = \int_Sd\omega_\alpha = O(L^2)$ by Stokes. (3) Split the second-order term into symmetric $I_s$ and antisymmetric $I_a$ parts; $2I_s = (\int_0^1\omega_\alpha(\dot c))^2 = O(L^4)$. (4) In coordinates $\omega_\alpha = \omega_jdx^j$, freeze coefficients at $b_0 = 0$ with error $O(L^3)$: $2I_a = \omega_j(0)\omega_k(0)\int_0^1d\tau_2\int_0^{\tau_2}d\tau_1(\dot c^j(\tau_2)\dot c^k(\tau_1) - \dot c^j(\tau_1)\dot c^k(\tau_2)) + O(L^3) = \omega_j(0)\omega_k(0)\int_c(x^kdx^j - x^jdx^k) + O(L^3) = -[\omega_j(0),\omega_k(0)]\int_Sdx^j\wedge dx^k + O(L^3) = -\int_S[\omega_\alpha,\omega_\alpha] + O(L^3)$. (5) Hence $\Gamma(c) = 1_n - \int_Sd\omega_\alpha - \tfrac12\int_S[\omega_\alpha,\omega_\alpha] + O(L^3) = 1_n - \int_S\Omega_\alpha + O(L^3)$. Gaps: the error bookkeeping ($\|\dot c\| = O(L)$, area $O(L^2)$) is stated, not proved; the factor bookkeeping between $I_a$ and $\tfrac12[\omega_\alpha,\omega_\alpha]$ relies on $[\omega_\alpha,\omega_\alpha] = 2\sum_{j<k}[\omega_j,\omega_k]dx^j\wedge dx^k$.

### Examples
- **E2.6.1** (Rem. 2.6.3, p. 67) Frame bundle: horizontal lift = parallel frame.
- **E2.6.2** (pp. 68–69) Commuting case of the linear ODE — exponential of the integral.
- **E2.6.3** (Rem. 2.6.9, p. 72) Abelian holonomy around a loop.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R2.6.1** (Rem. 2.6.6, p. 68) $\Gamma(c)$ is independent of parametrisation but depends on $c$; for closed $c$, $\Gamma(c)\neq\mathrm{id}$ in general — related to curvature.
- **R2.6.2** (p. 69) Ordering problem for non-commuting $A(t)$ motivates the path-ordered exponential.
- **R2.6.3** (pp. 72–75) The holonomy expansion (T2.6.8) — establishes that curvature is the infinitesimal holonomy.

### External results imported without proof
- **I2.6.1** Picard–Lindelöf and global existence for linear ODEs (Rem. 2.6.2).
- **I2.6.2** Stokes' theorem (Rem. 2.6.9, T2.6.8).
- **I2.6.3** Completeness of $C^0(I;\mathrm{Mat})$ and $C^1(I;\mathrm{Mat})$ (Lemma 2.6.7(c)).

---

## 2.7 Gauge transformations

`PDF pages: 75–78`

### Standing conventions and notation
- $\mathrm{Aut}(P) := \{f\in\mathrm{Diff}(P)\mid f(p\cdot g) = f(p)\cdot g\ \forall p,g\}$; induced $\bar f\in\mathrm{Diff}(B)$ with $\pi\circ f = \bar f\circ\pi$.
- $\mathrm{Aut}(P)$ acts on $\mathcal C(P)$ **from the right by pull-back**: $(f\circ g)^*\omega = g^*(f^*\omega)$.
- Gauge group $\mathcal G(P) := \{f\in\mathrm{Aut}(P)\mid\bar f = \mathrm{id}_B\} = \ker(f\mapsto\bar f)$.
- Group bundle $P\times_\alpha G := P\times G/\sim$, $[p,g]\sim[ph,h^{-1}gh]$; multiplication $[p,g]\cdot[p,g'] := [p,gg']$.
- Correspondence $\mathcal G(P)\cong\{C^\infty\text{-sections of }P\times_\alpha G\}$: $f(p) = p\cdot g(p)$ with $g(ph) = h^{-1}g(p)h$.
- Reduced gauge group $\mathcal G_b(P) := \{f\in\mathcal G(P)\mid f|_{P_b} = \mathrm{id}_{P_b}\}$; $H^\omega_q$ horizontal spaces of $\omega$.
- Diagram of groups (p. 77): $\mathcal G_b(P)\hookrightarrow\mathcal G(P)\hookrightarrow\mathrm{Aut}(P)\hookrightarrow\mathrm{Diff}(P)$, with $\mathcal G(P)\to\mathrm{Diff}(P_b)$ (restriction) and $\mathrm{Aut}(P)\to\mathrm{Diff}(B)$ ($f\mapsto\bar f$).

### Definitions
- **D2.7.1 — Def - Automorphism of a Principal Bundle** (Def. 2.7.1, p. 75). A diffeomorphism $f: P\to P$ with $f(p\cdot g) = f(p)\cdot g$ for all $g\in G$, $p\in P$; $\mathrm{Aut}(P)$ the *automorphism group*.
- **D2.7.2 — Def - Induced Diffeomorphism of the Base** (Rem. 2.7.2.2, p. 75). The unique smooth $\bar f: B\to B$ with $\pi\circ f = \bar f\circ\pi$.
- **D2.7.3 — Def - Gauge Transformation and Gauge Group** (Def. 2.7.3, p. 76). $f\in\mathrm{Aut}(P)$ with $\bar f = \mathrm{id}_B$ is a *gauge transformation*; $\mathcal G(P) := \{$gauge transformations$\}$ is the *gauge group*.
- **D2.7.4 — Def - Group Bundle of a Principal Bundle** (Rem. 2.7.7, p. 76). $P\times_\alpha G := P\times G/\sim$ with $\alpha$ the conjugation action, $[p,g]\sim[ph,h^{-1}gh]$; fibers are groups via $[p,g]\cdot[p,g'] := [p,gg']$, isomorphic to $G$; it is a group bundle with typical fiber $G$ but not a $G$-principal bundle; it always has global sections, e.g. $\pi(p)\mapsto[p,e]$.
- **D2.7.5 — Def - Reduced Gauge Group** (Def. 2.7.8, p. 77). For $b\in B$: $\mathcal G_b(P) := \{f\in\mathcal G(P)\mid f|_{P_b} = \mathrm{id}_{P_b}\} = \ker(\mathcal G(P)\to\mathrm{Diff}(P_b))$.

### Theorems
- **T2.7.1 — Thm - Automorphisms Cover Diffeomorphisms and Act on Connections** (Rem. 2.7.2, pp. 75–76). (1) $\mathrm{Aut}(P)\subset\mathrm{Diff}(P)$ is a subgroup. (2) Every $f\in\mathrm{Aut}(P)$ maps fibers to fibers and induces a unique smooth $\bar f: B\to B$. (3) For $\omega\in\mathcal C(P)$, $f\in\mathrm{Aut}(P)$: $f^*\omega\in\mathcal C(P)$, and pull-back is a right action of $\mathrm{Aut}(P)$ on $\mathcal C(P)$. `Proof in source: full.` Strategy for (3): $R_g^*f^*\omega = (f\circ R_g)^*\omega = (R_g\circ f)^*\omega = f^*\mathrm{Ad}_{g^{-1}}\omega = \mathrm{Ad}_{g^{-1}}f^*\omega$; $(f^*\omega)(\bar X(p)) = \omega(df\circ dL_p(X)) = \omega(dL_{f(p)}X) = \omega(\bar X(f(p))) = X$ using $f\circ L_p = L_{f(p)}$; $(f\circ g)^* = g^*f^*$. Gap: smoothness of $\bar f$ asserted.
- **T2.7.2 — Thm - Gauge Group Is the Kernel of the Base Map** (Rem. 2.7.4, p. 76). $f\mapsto\bar f$ is a group homomorphism $\mathrm{Aut}(P)\to\mathrm{Diff}(B)$; $\mathcal G(P) = \ker\subset\mathrm{Aut}(P)$ is a subgroup. `Proof in source: full (immediate).`
- **T2.7.3 — Thm - Gauge Transformations of Abelian Bundles** (Ex. 2.7.5, Rem. 2.7.6, p. 76). If $G$ is abelian, every smooth $g: B\to G$ gives a gauge transformation $f(p) := p\cdot g(\pi(p))$ ($f(pg') = pg'g(\pi p) = pg(\pi p)g' = f(p)g'$), and all gauge transformations are of this form. If $G$ is non-abelian this works only for $g: B\to Z(G)$. `Proof in source: full for the construction; "all are of this form" via Rem. 2.7.7.`
- **T2.7.4 — Thm - Gauge Group Equals Sections of the Group Bundle** (Rem. 2.7.7, pp. 76–77). $\{C^\infty\text{-sections of }P\times_\alpha G\}\cong\mathcal G(P)$ as groups. `Proof in source: full.` Strategy: given a section $b\mapsto[p(b),g(b)]$, define $f(p(b)h) := p(b)h\cdot h^{-1}g(b)h$; uniqueness from equivariance. Conversely, for $f\in\mathcal G(P)$ define $g(p)$ by $f(p) = p\cdot g(p)$; then $g(ph) = h^{-1}g(p)h$, so $\pi(p)\mapsto[p,g(p)]$ is a well-defined smooth section.
- **T2.7.5 — Thm - Reduced Gauge Group Acts Freely on Connections** (Prop. 2.7.9, p. 78). If $B$ is connected, the action of $\mathcal G_b(P)$ on $\mathcal C(P)$ is free. `Proof in source: full.` Strategy: let $f\in\mathcal G_b(P)$ with $f^*\omega = \omega$; fix $p$, choose $c: [0,1]\to B$ from $b$ to $\pi(p)$, let $\tilde c$ be the $\omega$-horizontal lift with $\tilde c(1) = p$ and $\hat c := f\circ\tilde c$; $\hat c$ lifts $c$; $df(H^\omega_q) = H^\omega_{f(q)}$ (since $\omega(dfX) = f^*\omega(X) = \omega(X) = 0$ and dimensions agree), so $\hat c$ is horizontal; $\hat c(0) = f(\tilde c(0)) = \tilde c(0)$ as $\tilde c(0)\in P_b$; uniqueness of lifts gives $\hat c = \tilde c$, so $f(p) = \hat c(1) = \tilde c(1) = p$.

### Examples
- **E2.7.1** (Ex. 2.7.5, p. 76) Abelian gauge transformations from maps $B\to G$.
- **E2.7.2** (Rem. 2.7.7, p. 77) The identity gauge transformation corresponds to the section $\pi(p)\mapsto[p,e]$.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R2.7.1** (Rem. 2.7.6, p. 76) Non-abelian obstruction: $p\cdot g(\pi(p))$ is a gauge transformation only if $g$ takes values in the center.
- **R2.7.2** (p. 78) "At least one reason to define the reduced gauge group is the following nice property" — motivation for $\mathcal G_b(P)$ is freeness of its action (Prop. 2.7.9).

### External results imported without proof
- None.

---

# Chapter 3 — Applications to Physics

## 3.1 The Hodge-star operator

`PDF pages: 79–84`

### Standing conventions and notation
- $V$ an $n$-dimensional real vector space with a **non-degenerate, not necessarily definite** inner product $\langle\cdot,\cdot\rangle$.
- **Generalized orthonormal basis:** $e_1,\dots,e_n$ with $\langle e_i,e_j\rangle = 0$ for $i\neq j$ and $\langle e_j,e_j\rangle = \epsilon_j = \pm1$. Dual basis $e_i^*$ with $e_i^*(e_j) = \delta_{ij}$.
- **Index** $p$ of $\langle\cdot,\cdot\rangle$ := number of $j$ with $\epsilon_j = -1$ (Prop. 3.1.8; "ind" in Rem. 3.1.4).
- **Inner product on $\Lambda^kV^*$:** $\langle\omega,\eta\rangle := \sum_{i_1<\dots<i_k}\epsilon_{i_1}\cdots\epsilon_{i_k}\,\omega(e_{i_1},\dots,e_{i_k})\,\eta(e_{i_1},\dots,e_{i_k})$; $\{e^*_{i_1}\wedge\dots\wedge e^*_{i_k}\}_{i_1<\dots<i_k}$ is a generalized ONB with $\langle e^*_{i_1}\wedge\dots\wedge e^*_{i_k},\text{same}\rangle = \epsilon_{i_1}\cdots\epsilon_{i_k}$.
- **Volume form:** $\mathrm{vol} := e_1^*\wedge\dots\wedge e_n^*$ for a *positively oriented* generalized ONB; $\langle\mathrm{vol},\mathrm{vol}\rangle = (-1)^p$; orientation reversal gives $-\mathrm{vol}$.
- **Hodge star, defining relation (3.1):** $\omega\wedge\eta = \langle*\omega,\eta\rangle\cdot\mathrm{vol}$ for all $\omega\in\Lambda^kV^*$, $\eta\in\Lambda^{n-k}V^*$. **Warning:** this is $*$ *on the left* inside the pairing; it agrees with the common convention $\omega\wedge*\eta = \langle\omega,\eta\rangle\mathrm{vol}$ only up to the sign $(-1)^p$ (see (3.5)), so in Lorentzian signature the two conventions differ by a sign.
- **Properties (Prop. 3.1.8):** (3.2) $*(e^*_{i_1}\wedge\dots\wedge e^*_{i_k}) = \epsilon_{j_1}\cdots\epsilon_{j_{n-k}}\,\mathrm{sign}(IJ)\,e^*_{j_1}\wedge\dots\wedge e^*_{j_{n-k}}$ where $(IJ) = (i_1,\dots,i_k,j_1,\dots,j_{n-k})$ is a permutation of $(1,\dots,n)$; (3.3) $**\omega = (-1)^{k(n-k)+p}\omega$; (3.4) $\langle*\omega,*\eta\rangle = (-1)^p\langle\omega,\eta\rangle$; (3.5) $\omega\wedge*\eta = \eta\wedge*\omega = (-1)^p\langle\omega,\eta\rangle\mathrm{vol}$; (3.6) $\omega\wedge\eta = (-1)^{k(n-k)}\langle\omega,*\eta\rangle\mathrm{vol}$.
- **Four-dimensional Euclidean case** ($n=4$, $k=2$, $p=0$): $**=1$, $*$ an isometry, $\Lambda^2V^* = \Lambda^2_+V^*\oplus\Lambda^2_-V^*$, $\Lambda^2_\pm := \{*\omega = \pm\omega\}$, $\dim\Lambda^2_\pm = 3$; $*(e_1^*\wedge e_2^*) = e_3^*\wedge e_4^*$, $*(e_1^*\wedge e_3^*) = -e_2^*\wedge e_4^*$, $*(e_1^*\wedge e_4^*) = e_2^*\wedge e_3^*$; bases $e_1^*\wedge e_2^*\pm e_3^*\wedge e_4^*$, $e_1^*\wedge e_3^*\mp e_2^*\wedge e_4^*$, $e_1^*\wedge e_4^*\pm e_2^*\wedge e_3^*$ of $\Lambda^2_\pm$.
- $W$-valued forms: $\langle v\otimes w,v'\otimes w'\rangle := \langle v,v'\rangle\langle w,w'\rangle$; $*(\omega\otimes w) := (*\omega)\otimes w$.

### Definitions
- **D3.1.1 — Def - Generalized Orthonormal Basis and Index** (pp. 79, 82). As in conventions.
- **D3.1.2 — Def - Induced Inner Product on Exterior Powers** (p. 79). $\langle\omega,\eta\rangle := \sum_{i_1<\dots<i_k}\epsilon_{i_1}\cdots\epsilon_{i_k}\omega(e_{i_1},\dots,e_{i_k})\eta(e_{i_1},\dots,e_{i_k})$ on $\Lambda^kV^*$.
- **D3.1.3 — Def - Volume Form** (Def. 3.1.3, p. 80). For oriented $V$ and a positively oriented generalized ONB: $\mathrm{vol} := e_1^*\wedge\dots\wedge e_n^*\in\Lambda^nV^*$.
- **D3.1.4 — Def - Hodge-Star Operator** (Def. 3.1.6, Lemma 3.1.5, p. 81). The unique linear map $*: \Lambda^kV^*\to\Lambda^{n-k}V^*$ with $\omega\wedge\eta = \langle*\omega,\eta\rangle\mathrm{vol}$ for all $\omega\in\Lambda^kV^*$, $\eta\in\Lambda^{n-k}V^*$; it depends on the inner product (Rem. 3.1.7).
- **D3.1.5 — Def - Self-Dual and Anti-Self-Dual 2-Forms** (Rem. 3.1.9, p. 83). For $n = 4$, $p = 0$: $\Lambda^2_\pm V^* := \{\omega\in\Lambda^2V^*\mid*\omega = \pm\omega\}$; *self-dual* ($+$), *anti-self-dual* ($-$).
- **D3.1.6 — Def - Hodge Star on Vector-Valued Forms** (Rem. 3.1.11, p. 84). $*: \Lambda^kV^*\otimes W\to\Lambda^{n-k}V^*\otimes W$, $*(\omega\otimes w) := (*\omega)\otimes w$, with the product inner product on $V\otimes W$.

### Theorems
- **T3.1.1 — Thm - Induced Inner Product Is Basis-Independent** (Lemma 3.1.1, pp. 79–80). The definition of $\langle\cdot,\cdot\rangle$ on $\Lambda^kV^*$ does not depend on the generalized ONB. `Proof in source: full.` Strategy: for another gen. ONB $f_i = Ae_i = \sum_jA^j_ie_j$, $\delta_{ij}\epsilon'_j = \sum_kA^k_iA^k_j\epsilon_k$, i.e. $\epsilon' = A\epsilon A^*$ hence $A^*\epsilon'A = \epsilon$, i.e. $\delta_{ij}\epsilon_i = \sum_lA^i_lA^j_l\epsilon'_l$; expand $\frac1{k!}\sum_{i_1..i_k}\epsilon'_{i_1}\cdots\omega(f_{i_1},\dots)\eta(f_{i_1},\dots)$ in the $e$'s and contract using this identity. Gaps: index placement in the printed computation is inconsistent (mixes $A^j_i$ and $A^i_l$); the matrix identity manipulation "$\epsilon' = A\epsilon A^*$" uses $A^*$ for transpose.
- **T3.1.2 — Thm - Wedge Basis Is a Generalized Orthonormal Basis** (Rem. 3.1.2, p. 80). `Proof in source: omitted (stated).`
- **T3.1.3 — Thm - Volume Form Is Well-Defined** (Rem. 3.1.4, p. 81). $\Lambda^nV^*$ is 1-dimensional and $\langle e_1^*\wedge\dots\wedge e_n^*,\text{same}\rangle = \epsilon_1\cdots\epsilon_n = (-1)^{\mathrm{ind}}$, so $e_1^*\wedge\dots\wedge e_n^*$ is determined up to sign; the orientation fixes the sign. `Proof in source: full.`
- **T3.1.4 — Thm - Existence and Uniqueness of the Hodge Star** (Lemma 3.1.5, p. 81). `Proof in source: full.` Strategy: for fixed $\omega$, $\eta\mapsto\frac{\omega\wedge\eta}{\mathrm{vol}}$ is a linear functional on $\Lambda^{n-k}V^*$; non-degeneracy of $\langle\cdot,\cdot\rangle$ gives a unique $*\omega$ representing it; linearity in $\omega$ is clear. Gaps: non-degeneracy of the induced inner product on $\Lambda^{n-k}V^*$ is used without comment (it follows from Rem. 3.1.2).
- **T3.1.5 — Thm - Properties of the Hodge Star** (Prop. 3.1.8, pp. 82–83). Properties (3.2)–(3.6) as in conventions, for $V$ oriented $n$-dimensional with inner product of index $p$. `Proof in source: (1) full; (2),(3),(4) left as exercise; (5) full.` Strategy (1): if $\{i\}\cup\{j\}\neq\{1..n\}$ the wedge vanishes so $*(e^*_I)$ is a multiple $c\,e^*_J$ of the complementary basis form; $\mathrm{sign}(IJ)\mathrm{vol} = e^*_I\wedge e^*_J = \langle*e^*_I,e^*_J\rangle\mathrm{vol} = c\,\epsilon_{j_1}\cdots\epsilon_{j_{n-k}}\mathrm{vol}$. (5): $\omega\wedge\eta = \langle*\omega,\eta\rangle\mathrm{vol} = (-1)^p\langle**\omega,*\eta\rangle\mathrm{vol} = (-1)^{k(n-k)+2p}\langle\omega,*\eta\rangle\mathrm{vol}$.
- **T3.1.6 — Thm - Self-Dual Decomposition in Four Dimensions** (Rem. 3.1.9, p. 83). For $n=4$, $k=2$, $p=0$: $*\circ* = 1$, $*$ is an isometry, so $\Lambda^2V^* = \Lambda^2_+\oplus\Lambda^2_-$ with $\dim\Lambda^2_\pm = 3$ and the explicit bases above. `Proof in source: full` (the six listed elements are pairwise orthogonal hence independent; $\dim\Lambda^2 = 6$).
- **T3.1.7 — Thm - Orientation Reversal Swaps Self-Dual and Anti-Self-Dual Forms** (Rem. 3.1.10, p. 83). Reversing orientation negates $\mathrm{vol}$ and hence $*$; $\Lambda^2_\pm$ are interchanged. `Proof in source: full (immediate from (3.1)).`

### Examples
- **E3.1.1** (Rem. 3.1.9, p. 83) Explicit $*$ on 2-forms in 4-dimensional Euclidean space and the bases of $\Lambda^2_\pm$.

### Exercises
- **X3.1.1** (Prop. 3.1.8(2), p. 82) Prove $**\omega = (-1)^{k(n-k)+p}\omega$ for all $\omega\in\Lambda^kV^*$ (3.3).
- **X3.1.2** (Prop. 3.1.8(3), p. 82) Prove $\langle*\omega,*\eta\rangle = (-1)^p\langle\omega,\eta\rangle$ for $\omega,\eta\in\Lambda^kV^*$ (3.4).
- **X3.1.3** (Prop. 3.1.8(4), p. 83) Prove $\omega\wedge*\eta = \eta\wedge*\omega = (-1)^p\langle\omega,\eta\rangle\mathrm{vol}$ for $\omega,\eta\in\Lambda^kV^*$ (3.5).

### Remarks / load-bearing paragraphs
- **R3.1.1** (Rem. 3.1.7, p. 81) $*$ depends on the inner product (relevant for varying the metric in §3.2).
- **R3.1.2** (Rem. 3.1.11, p. 84) Extension of $*$ to $W$-valued forms (used for $\mathfrak g$-valued curvature in §3.3).

### External results imported without proof
- None (all linear algebra).

---

## 3.2 Electrodynamics

`PDF pages: 84–96` (sub-subsections: **Conformal invariance** pp. 92–93; **Diffeomorphism invariance** pp. 93–96; **Gauge invariance** p. 96)

### Standing conventions and notation
- $M$ an oriented **Lorentzian 4-manifold** (spacetime); Minkowski space for special relativity. Coordinates $(t,x,y,z)$ with $\langle\partial_t,\partial_t\rangle<0$ and $\langle\partial_x,\partial_x\rangle,\langle\partial_y,\partial_y\rangle,\langle\partial_z,\partial_z\rangle>0$ — **signature $(-,+,+,+)$, index $p = 1$**. Index $0$ is used for $t$ in tensor formulas ($x^0 = t$, $g_{00} = -1$ on Minkowski space); $\mathrm{vol} = dt\wedge dx\wedge dy\wedge dz$ (implicit in the star table).
- $P\to M$ a $U(1)$-principal bundle; for $\omega\in\mathcal C(P)$, $s^*\Omega$ is independent of $s$ (abelian), giving $\bar\Omega\in\Omega^2(M;i\mathbb R)$; write $\bar\Omega = iF$, $F\in\Omega^2(M;\mathbb R)$. Bianchi (2.6): $dF = 0$.
- **Field strength decomposition:** $F = E_x\,dx\wedge dt + E_y\,dy\wedge dt + E_z\,dz\wedge dt + B_x\,dy\wedge dz + B_y\,dz\wedge dx + B_z\,dx\wedge dy$; $\vec E := (E_x,E_y,E_z)$ electric field, $\vec B := (B_x,B_y,B_z)$ magnetic field (coordinate-dependent). Note $E_i\,dx^i\wedge dt$ means $F_{i0} = E_i$, $F_{0i} = -E_i$.
- **Current 3-form:** $J = \varrho\,dx\wedge dy\wedge dz - j_x\,dt\wedge dy\wedge dz - j_y\,dt\wedge dz\wedge dx - j_z\,dt\wedge dx\wedge dy$; $\varrho$ charge density, $\vec j = (j_x,j_y,j_z)$ current density.
- **Background connection** $\omega_0\in\mathcal C(P)$; $iA := s^*(\omega-\omega_0)\in\Omega^1(M;i\mathbb R)$ independent of $s$; $dA = F - F_0$.
- **Lagrangian:** $L: \mathcal C(P)\to\Omega^4(M;i\mathbb R)$ (sic; it is real-valued), $L(\omega) := \tfrac12F\wedge*F + A\wedge J$; $L_1 := \tfrac12F\wedge*F$, $L_2 := A\wedge J$. **Critical:** $\forall$ open $U\Subset M$, $\forall\eta\in\Omega^1(M;\mathbb R)$ with $\mathrm{supp}\,\eta\subset U$: $\frac d{dt}|_0\int_{\bar U}L(\omega_{t,\eta}) = 0$, where $A(\omega_{t,\eta},\omega_0) = A(\omega,\omega_0) + t\eta$, so $F(\omega_{t,\eta}) = F + t\,d\eta$.
- **Minkowski Hodge star on 2-forms:** $*(dt\wedge dx) = dy\wedge dz$, $*(dy\wedge dz) = -dt\wedge dx$, $*(dt\wedge dy) = dz\wedge dx$, $*(dz\wedge dx) = -dt\wedge dy$, $*(dt\wedge dz) = dx\wedge dy$, $*(dx\wedge dy) = -dt\wedge dz$. Hence $*F = -E_x\,dy\wedge dz - E_y\,dz\wedge dx - E_z\,dx\wedge dy + B_x\,dx\wedge dt + B_y\,dy\wedge dt + B_z\,dz\wedge dt$ (source prints "$-B_z\,dz\wedge dt$", a sign typo).
- **Musical isomorphism:** for $\eta\in T_x^*M$, $\eta^\sharp\in T_xM$ with $\eta(Y) = \langle\eta^\sharp,Y\rangle$ (fn. 1, p. 88).
- **Test particle:** mass 1, charge 1; worldline = timelike curve $c$, $\langle c',c'\rangle<0$; $c(\tau) = (t(\tau),\vec c(\tau))$; observed velocity $\vec v = d\vec c/dt = \vec c'/t'$, $|\vec v|<1$; **equation of motion (3.12):** $\frac\nabla{d\tau}c' + F(c',\cdot)^\sharp = 0$; eigentime normalisation $\langle c',c'\rangle = -1$, $t'>0$; relativistic mass $m = m_0/\sqrt{1-|\vec v|^2} = m_0t'$.
- **Metric variation:** $g(t)$ with $g(0) = g$, $\dot g(0) = h\in\odot^2T^*M$; footnote formulas $\frac{d}{dt}\det A = \det A\cdot\mathrm{tr}(A^{-1}\dot A)$ and $\dot g^{il} = -g^{ij}\dot g_{jk}g^{kl}$; $\frac d{dt}|_0\mathrm{vol}_{g(t)} = \tfrac12\mathrm{tr}_g(h)\mathrm{vol}_g$; $\frac d{dt}|_0\langle F,F\rangle_{g(t)} = F^{\delta i}F^j{}_\delta h_{ij}$.
- **Energy–momentum tensor:** $T^{ij} := -F^{\delta i}F^j{}_\delta - \tfrac12\langle F,F\rangle_g\,g^{ij}$; $\frac d{dt}|_0L_1(\omega,g(t)) = -\tfrac12T^{ij}h_{ij}\mathrm{vol}_g$; $T = T_{ij}dx^i\otimes dx^j$ the $(0,2)$-version.
- **Einstein–Hilbert (geometric) Lagrangian:** $L_{geom}(g) := -\tfrac12\mathrm{scal}_g\mathrm{vol}_g$; $\frac d{dt}|_0\mathrm{scal}_{g(t)} = -\mathrm{ric}^{ij}_gh_{ij} + \mathrm{div}(X)$.
- **Einstein field equations (3.15):** $\mathrm{ric}_g - \tfrac12\mathrm{scal}_g\,g = T$.
- Minkowski: $\langle F,F\rangle = -|\vec E|^2 + |\vec B|^2$; $T^{00} = \tfrac12(|\vec E|^2+|\vec B|^2)$ energy density; $(T^{01},T^{02},T^{03}) = \vec E\times\vec B =: \vec S$ Poynting vector; $T^{ij} = -\sigma^{ij}$ with **Maxwell stress tensor** $\sigma := \vec E\otimes\vec E + \vec B\otimes\vec B - \tfrac12(|\vec B|^2+|\vec E|^2)g$ ($g$ = inverse metric on the right).
- **Conformal rescaling:** $g' = \lambda^2g$ ⇒ $\langle\cdot,\cdot\rangle'_{\Lambda^k} = \lambda^{-2k}\langle\cdot,\cdot\rangle$, $\mathrm{vol}_{g'} = \lambda^n\mathrm{vol}_g$, $*' = \lambda^{2k-n}*$; for $2k = n$, $*' = *$. (Source writes "$g' = \lambda\cdot g$" on p. 93; the computation uses $\lambda^2$.)
- **Symmetrized covariant derivative:** $(\mathcal L_Xg)(Y,Z) = g(\nabla_YX,Z) + g(Y,\nabla_ZX) =: 2(\nabla^{sym}X)(Y,Z)$.
- **Divergence of a $(2,0)$-tensor:** $\mathrm{div}(T) := \sum_{i=1}^n(\nabla_{e_i}T)(e_i^*,\cdot)\in\mathfrak X(M)$ for a generalized ONB (basis-independent); $\int_MT\cdot\nabla^{sym}X\,\mathrm{vol}_g = -\int_M\langle\mathrm{div}T,X\rangle\mathrm{vol}_g$.
- **Cartan's magic formula** (fn. 4, p. 94): $\mathcal L_X\alpha = d(\iota_X\alpha) + \iota_X(d\alpha)$, $\iota_X\beta = \beta(X,\dots)$.
- Pull-back of bundles under $\phi\in\mathrm{Diff}(M)$: $\Phi: \phi^*P\to P$ covering $\phi$; local sections $s_{\alpha,t} := \Phi_t^{-1}\circ s_\alpha\circ\phi_t$.

### Definitions
- **D3.2.1 — Def - Electromagnetic Field Strength and Electric and Magnetic Fields** (p. 84). $\bar\Omega = iF$; the coefficient functions $\vec E,\vec B$ of $F$ in coordinates $(t,x,y,z)$ as above.
- **D3.2.2 — Def - Charge Density and Current Density** (pp. 85–86). $J\in\Omega^3(M;\mathbb R)$ with coefficients $\varrho$, $\vec j$ as above.
- **D3.2.3 — Def - Potential Relative to a Background Connection** (p. 85). $iA(\omega,\omega_0) := s^*(\omega-\omega_0)$; $dA = F-F_0$.
- **D3.2.4 — Def - Electrodynamics Lagrangian and Critical Connection** (p. 85). $L(\omega) := \tfrac12F\wedge*F + A\wedge J$; criticality as in conventions.
- **D3.2.5 — Def - Worldline and Observed Velocity** (pp. 87–88). Timelike smooth curve $c$; $\vec v := \vec c'/t'$.
- **D3.2.6 — Def - Equation of Motion of a Charged Test Particle** (eq. (3.12), p. 88). $\frac\nabla{d\tau}c' + F(c',\cdot)^\sharp = 0$ ("Newton's law", force given by $F$).
- **D3.2.7 — Def - Eigentime Parametrization and Relativistic Mass** (p. 88). $\langle c',c'\rangle = -1$, $t'>0$; $m = m_0/\sqrt{1-|\vec v|^2} = m_0t'$.
- **D3.2.8 — Def - Energy Momentum Tensor** (p. 90). $T^{ij} := -F^{\delta i}F^j{}_\delta - \tfrac12\langle F,F\rangle_gg^{ij}$, $T := T^{ij}\partial_i\otimes\partial_j$ (of $\omega$ or of $F$).
- **D3.2.9 — Def - Einstein-Hilbert Action** (p. 90). $L_{geom}(g) := -\tfrac12\mathrm{scal}_g\,\mathrm{vol}_g$ ("geometric Lagrangian").
- **D3.2.10 — Def - Energy Density Poynting Vector and Maxwell Stress Tensor** (pp. 91–92). $T^{00} = \tfrac12(|\vec E|^2+|\vec B|^2)$; $\vec S := \vec E\times\vec B$; $\sigma := \vec E\otimes\vec E + \vec B\otimes\vec B - \tfrac12(|\vec B|^2+|\vec E|^2)g$.
- **D3.2.11 — Def - Conformal Invariance of the Lagrangian** (p. 93). $L(\omega,g') = L(\omega,g)$ for $g' = \lambda^2g$, $\lambda\in C^\infty(M)$, $\lambda>0$.
- **D3.2.12 — Def - Symmetrized Covariant Derivative** (p. 94). $2(\nabla^{sym}X)(Y,Z) := g(\nabla_YX,Z) + g(Y,\nabla_ZX)$.
- **D3.2.13 — Def - Divergence of a 2-Tensor** (p. 95). $\mathrm{div}(T) := \sum_i(\nabla_{e_i}T)(e_i^*,\cdot)$.

### Theorems
- **T3.2.1 — Thm - Solutions of the Equation of Motion Have Constant Speed** (Rem. 3.2.1, p. 88). For any timelike $c$ solving (3.12): $\frac d{dt}\langle c',c'\rangle = 2\langle\frac\nabla{d\tau}c',c'\rangle = -2F(c',c') = 0$, so $c$ is parametrised proportionally to eigentime. `Proof in source: full.`
- **T3.2.2 — Thm - Existence and Uniqueness for the Equation of Motion** (Rem. 3.2.2, p. 88). For $p\in M$, $X\in T_pM$ there is a unique maximal solution $c$ of (3.12) with $c(t_0) = p$, $c'(t_0) = X$. `Proof in source: omitted ("since (3.12) is a linear ODE of second order")`. Gap: (3.12) is not linear in general (it is a second-order ODE with smooth coefficients); existence/uniqueness follows from Picard–Lindelöf regardless.

### Examples
- **E3.2.1** (pp. 86–87) Minkowski space with standard coordinates: explicit $*F$, $d*F$, and Maxwell's equations.
- **E3.2.2** (p. 87) Charge conservation for a compact $B\subset\mathbb R^3$: $0 = \int_{[t_0,t_1]\times B}dJ = \int_B\varrho(t_1) - \int_B\varrho(t_0) + \int_{t_0}^{t_1}\int_{\partial B}\langle\vec j,\nu\rangle$.
- **E3.2.3** (p. 96) Energy conservation for $\vec j = 0$: $0 = \tfrac12\int_B(|\vec E|^2+|\vec B|^2)(t_1) - \tfrac12\int_B(\dots)(t_0) - \int_{t_0}^{t_1}\int_{\partial B}\langle\vec S,\nu\rangle$ (source prints a minus before the flux term).

### Exercises
- None stated.

### Remarks / load-bearing paragraphs (the section is mostly derivations)
- **R3.2.1 — Curvature of a U(1)-connection is a global real 2-form; Bianchi gives $dF = 0$** (p. 84). Since $\mathrm{Ad}$ is trivial, $s^*\Omega$ is section-independent; $\bar\Omega = iF$; (2.6) gives $dF = 0$.
- **R3.2.2 — Derivation of the homogeneous Maxwell equations** (p. 84, eqs. (3.7),(3.8)). Compute $dF$ in coordinates: $dF = (\partial_xB_x+\partial_yB_y+\partial_zB_z)dx\wedge dy\wedge dz + (\dots)dt\wedge dy\wedge dz + \dots$; hence $dF = 0$ ⇔ $\mathrm{div}\vec B = 0$ (Gauss's law) and $\partial_t\vec B + \mathrm{rot}\vec E = 0$ (Faraday's law). (The printed $dt\wedge dy\wedge dz$ coefficient "$-\partial_yE_z+\partial_yE_z+\partial_tB_x$" is a typo for $\partial_yE_z - \partial_zE_y + \partial_tB_x$.)
- **R3.2.3 — Euler–Lagrange equation of the electrodynamics Lagrangian** (pp. 85–86). $\frac d{dt}|_0L_1(\omega_{t,\eta}) = \tfrac12(d\eta\wedge*F + F\wedge*d\eta) = d\eta\wedge*F$ by (3.5); $\int_{\bar U}d\eta\wedge*F = \int_{\bar U}d(\eta\wedge*F) + \eta\wedge d*F = \int_M\eta\wedge d*F$ (Stokes, $\mathrm{supp}\,\eta\subset U$); $\frac d{dt}|_0\int_{\bar U}L_2 = \int_M\eta\wedge J$. Hence **$\omega$ critical ⇔ $d*F + J = 0$**.
- **R3.2.4 — Independence of the background connection** (p. 86). Replacing $\omega_0$ by $\tilde\omega_0$ changes $L$ by $A(\tilde\omega_0,\omega_0)\wedge J$, a constant after integration, so the Euler–Lagrange equation is unchanged.
- **R3.2.5 — Derivation of the inhomogeneous Maxwell equations** (pp. 86–87, eqs. (3.9),(3.10)). On Minkowski space, $d(*F) = (-\mathrm{div}\vec E)dx\wedge dy\wedge dz + (\mathrm{rot}\vec B - \partial_t\vec E)_x\,dt\wedge dy\wedge dz + (\dots)_y\,dt\wedge dz\wedge dx + (\dots)_z\,dt\wedge dx\wedge dy$; so $d*F + J = 0$ ⇔ $\mathrm{div}\vec E = \varrho$ (Coulomb's law) and $\mathrm{rot}\vec B - \partial_t\vec E = \vec j$ (Ampère's law).
- **R3.2.6 — Continuity equation and conservation of charge** (p. 87, eq. (3.11)). $0 = d(d*F + J) = dJ = (\partial_t\varrho + \partial_xj_x + \partial_yj_y + \partial_zj_z)dt\wedge dx\wedge dy\wedge dz$ ⇔ $\partial_t\varrho + \mathrm{div}\vec j = 0$; Stokes on $[t_0,t_1]\times B$ gives charge conservation (E3.2.2).
- **R3.2.7 — Derivation of the Lorentz force law** (pp. 88–89, eq. (3.13)). LHS of (3.12) in coordinates: $\frac d{dt}(m\vec v) = m_0\vec c''/t'$. RHS: $F(c',\cdot)^\sharp = -\langle\vec c',\vec E\rangle\partial_t + (-t'\vec E + \vec B\times\vec c')$ (computed componentwise with $dt^\sharp = -\partial_t$, $dx^\sharp = \partial_x$, etc.). So (3.12) ⇔ $t'' + \langle\vec c',\vec E\rangle = 0$ and $\vec c'' - t'\vec E + \vec B\times\vec c' = 0$; the first follows from the second via $\langle c',c'\rangle = $ const ($t't'' = \langle\vec c',\vec c''\rangle$); dividing by $t'$: $\frac d{dt}(m\vec v) = \vec E + \vec v\times\vec B$ (Lorentz force law). (Source prints "$\vec v''$" for $\vec c''$ and "$\frac d{dt}\langle c',c'\rangle$" in places.)
- **R3.2.8 — Variation of the Lagrangian with respect to the metric; energy–momentum tensor** (pp. 89–90). $L_1(\omega,g) = \tfrac12\langle F,F\rangle_g\mathrm{vol}_g$. (a) $\frac d{dt}|_0\mathrm{vol}_{g(t)} = \frac d{dt}\sqrt{-\det g_{ij}}\,dx^0\wedge\dots\wedge dx^3 = \tfrac12g^{ij}h_{ji}\mathrm{vol}_g = \tfrac12\mathrm{tr}_g(h)\mathrm{vol}_g$ (Jacobi's formula). (b) $\langle F,F\rangle = \tfrac14F_{\alpha\beta}F_{\gamma\delta}(g^{\alpha\gamma}g^{\beta\delta} - g^{\alpha\delta}g^{\beta\gamma})$; differentiate with $\dot g^{il} = -g^{ij}h_{jk}g^{kl}$ to get $\frac d{dt}|_0\langle F,F\rangle = F^{\delta i}F^j{}_\delta h_{ij}$. (c) $\frac d{dt}|_0L_1 = \tfrac12(F^{\delta i}F^j{}_\delta h_{ij} + \tfrac12\langle F,F\rangle\mathrm{tr}_gh)\mathrm{vol}_g = -\tfrac12T^{ij}h_{ij}\mathrm{vol}_g$ with $T^{ij} = -F^{\delta i}F^j{}_\delta - \tfrac12\langle F,F\rangle g^{ij}$. Gap: the intermediate sign/index bookkeeping in (b) is compressed ("$-F^{i\delta}F^{j}{}_\delta - F^{\gamma i}F_{\gamma}{}^{j} + \dots$").
- **R3.2.9 — Einstein field equations from the coupled action** (pp. 90–91, eqs. (3.14),(3.15)). Using $\frac d{dt}|_0\mathrm{scal}_{g(t)} = -\mathrm{ric}^{ij}h_{ij} + \mathrm{div}X$ (imported) and (a): $\frac d{dt}|_0\int L_{geom} = \tfrac12\int(\mathrm{ric}^{ij} - \tfrac12g^{ij}\mathrm{scal})h_{ij}\mathrm{vol}_g$ for compactly supported $h$. Hence $g$ critical for $L_{geom}(g) + L_1(\omega,g) + L_2(\omega)$ ⇔ $\int(\mathrm{ric}^{ij} - \tfrac12g^{ij}\mathrm{scal} - T^{ij})h_{ij}\mathrm{vol} = 0\ \forall h$ ⇔ $\mathrm{ric}_g - \tfrac12\mathrm{scal}_g\,g = T$.
- **R3.2.10 — Energy–momentum tensor in terms of E and B** (pp. 91–92). $\langle F,F\rangle = -\sum_kF_{0k}F_{0k} + \sum_{i<k}F_{ik}F_{ik} = -|\vec E|^2 + |\vec B|^2$; $T^{00} = F^{0k}F^{0}{}_k - \tfrac12(|\vec B|^2-|\vec E|^2)g^{00} = \tfrac12(|\vec E|^2+|\vec B|^2)$; $T^{01} = E_2B_3 - E_3B_2 = (\vec E\times\vec B)_1$, similarly $T^{02},T^{03}$; for $1\le i,j\le3$: $T^{ij} = -E_iE_j - B_iB_j + \tfrac12(|\vec B|^2+|\vec E|^2)g^{ij} = -\sigma^{ij}$.
- **R3.2.11 — Conformal invariance and tracelessness of T** (pp. 92–93). Rescaling $g' = \lambda^2g$: gen. ONB $e_i' = \lambda^{-1}e_i$, dual $(e_i^*)' = \lambda e_i^*$, $\langle\cdot,\cdot\rangle' = \lambda^{-2k}\langle\cdot,\cdot\rangle$ on $\Lambda^k$, $\mathrm{vol}_{g'} = \lambda^n\mathrm{vol}_g$; from (3.1): $\langle\omega,*\eta\rangle\mathrm{vol}_g = \omega\wedge\eta = \lambda^{n-2k}\langle\omega,*'\eta\rangle\mathrm{vol}_g$, so $*' = \lambda^{2k-n}*$; for $n=4,k=2$: $*' = *$, so $L$ is conformally invariant. Take $g(t) := (1+t)g$, $\dot g(0) = g$: $0 = \frac d{dt}|_0L_1 = -\tfrac12T\cdot g\,\mathrm{vol}_g = -\tfrac12\mathrm{tr}_g(T)\mathrm{vol}_g$, so **$\mathrm{tr}_gT = 0$**.
- **R3.2.12 — Diffeomorphism invariance of the action** (pp. 93–94). For $\phi\in\mathrm{Diff}(M)$ with $\mathrm{supp}\,\phi\subset U\Subset M$ and induced $\Phi: \phi^*P\to P$: $\int_UL_1(\Phi^*\omega,\phi^*g) = \tfrac12\int_U\langle\phi^*F,\phi^*F\rangle_{\phi^*g}\phi^*\mathrm{vol}_g = \tfrac12\int_U(\langle F,F\rangle_g\circ\phi)\phi^*\mathrm{vol}_g = \tfrac12\int_U\langle F,F\rangle_g\mathrm{vol}_g$. This is an invariance of the action, not pointwise of the density.
- **R3.2.13 — Divergence identity for T; Poynting's theorem** (pp. 94–96, eqs. (3.16),(3.17)). Let $X$ be compactly supported with flow $\phi_t$, $g_t := \phi_t^*g$, $h = \mathcal L_Xg = 2\nabla^{sym}X$ (proved via $\mathcal L_Xg(Y,Z) = \partial_Xg(Y,Z) - g([X,Y],Z) - g(Y,[X,Z])$ and torsion-freeness). Then $0 = \frac d{dt}|_0\int_UL_1(\Phi_t^*\omega,\phi_t^*g) = \int_U\eta\wedge d*F - \tfrac12\int_UT\cdot h\,\mathrm{vol}_g$, where $i\eta := \frac d{dt}|_0s^*_{\alpha,t}\Phi_t^*\omega = \mathcal L_X(s_\alpha^*\omega) = i(\iota_XF + df)$, $f := s_\alpha^*\omega(X)/i$ (Cartan). Hence $\int_MT\cdot\nabla^{sym}X\,\mathrm{vol}_g = \int_M(\iota_XF + df)\wedge d*F = \int_M\langle\iota_XF,*d*F\rangle\mathrm{vol}_g$ (Stokes kills $d(f\,d*F)$), i.e. (3.16): $-\langle\mathrm{div}T,X\rangle = \langle\iota_XF,*d*F\rangle$ for all $X\in TM$. If $\omega$ is critical ($d*F = J$; sign as printed, cf. R3.2.3 which has $d*F = -J$) then $-\langle\mathrm{div}T,X\rangle = \langle\iota_XF,*J\rangle$. For $X = \partial_t$ on Minkowski space: LHS $= -\partial_tT^{00} - \sum_i\partial_iT^{i0} = -\tfrac12\partial_t(|\vec E|^2+|\vec B|^2) - \mathrm{div}\vec S$; RHS $= \langle\sum_i-E_idx^i,\ \varrho\,dt - \sum_ij_idx^i\rangle = \langle\vec E,\vec j\rangle$. Result (3.17): **$\tfrac12\partial_t(|\vec E|^2+|\vec B|^2) + \mathrm{div}\vec S = -\langle\vec E,\vec j\rangle$** (Poynting's theorem); for $\vec j = 0$, Stokes gives energy conservation with $\vec S$ the energy current density (E3.2.3). Gaps: the identification of $\Phi_t^*\omega$ across different bundles via $s_{\alpha,t}$ is only described; the formula $\int T\cdot\nabla^{sym}X = -\int\langle\mathrm{div}T,X\rangle$ is asserted "by Stokes"; the sign of $J$ in "$d*F = J$" is inconsistent with R3.2.3.
- **R3.2.14 — Gauge invariance** (p. 96). For $\phi\in\mathcal G(P)$, $\omega' := \phi^*\omega$: since $U(1)$ is abelian, $\bar\Omega' = \bar\Omega$, $F' = F$, so $L_1(\phi^*\omega,g) = L_1(\omega,g)$.

### External results imported without proof
- **I3.2.1** Stokes' theorem (used repeatedly).
- **I3.2.2** Jacobi's formula $\frac d{dt}\det A = \det A\,\mathrm{tr}(A^{-1}\dot A)$ (fn. 2, p. 90).
- **I3.2.3** First variation of scalar curvature: $\frac d{dt}|_0\mathrm{scal}_{g(t)} = -\mathrm{ric}^{ij}_gh_{ij} + \mathrm{div}(X)$ (p. 90).
- **I3.2.4** Cartan's magic formula (fn. 4, p. 94).
- **I3.2.5** Existence of the bundle isomorphism $\Phi: \phi^*P\to P$ covering a diffeomorphism $\phi$ isotopic to the identity (p. 93) — asserted via a diagram.
- **I3.2.6** Newton's law as the physical input for (3.12); relativistic mass formula $m = m_0/\sqrt{1-|\vec v|^2}$ (p. 88).
- **I3.2.7** Picard–Lindelöf for (3.12).

---

## 3.3 Yang–Mills fields

`PDF pages: 97–105`

### Standing conventions and notation
- $E\to M$ a $\mathbb K$-vector bundle with covariant derivative $\nabla$; $\Omega^k(M;E) = \Gamma(\Lambda^kT^*M\otimes E)$.
- **Exterior covariant derivative:** $d^\nabla\eta(X_0,\dots,X_k) := \sum_i(-1)^i\nabla_{X_i}(\eta(X_0,\dots,\widehat{X_i},\dots,X_k)) + \sum_{i<j}(-1)^{i+j}\eta([X_i,X_j],X_0,\dots,\widehat{X_i},\dots,\widehat{X_j},\dots,X_k)$.
- Curvature tensor $R(X,Y)\sigma = \nabla_X\nabla_Y\sigma - \nabla_Y\nabla_X\sigma - \nabla_{[X,Y]}\sigma$.
- **Wedge of $E$-valued forms:** $\eta\wedge\mu := \sum\eta_{i_1..i_k}\otimes\mu_{j_1..j_l}\otimes dx^{i_1}\wedge\dots\wedge dx^{j_l}\in\Omega^{k+l}(M;E\otimes E)$; with a metric on $E$: $\langle\eta\wedge\mu\rangle := \sum\langle\eta_{i_1..i_k},\mu_{j_1..j_l}\rangle dx^{i_1}\wedge\dots\wedge dx^{j_l}$; Leibniz for metric $\nabla$: $d\langle\eta\wedge\mu\rangle = \langle d^\nabla\eta\wedge\mu\rangle + (-1)^k\langle\eta\wedge d^\nabla\mu\rangle$.
- **Setting:** $M$ a **Riemannian** 4-manifold, $P\to M$ an $SU(N)$-bundle, $N\ge2$; $\lambda(A,B) := -\mathrm{tr}(AB)$ on $\mathfrak{su}(N)$ — real, positive definite, symmetric, $\mathrm{Ad}$-invariant; induces a Riemannian metric $\lambda([p,A],[p,B]) := \lambda(A,B)$ on $P\times_{\mathrm{Ad}}\mathfrak g$.
- **Covariant derivative on the adjoint bundle:** $\nabla^\omega_X[s,A] := [s,\partial_XA + \mathrm{ad}(s^*\omega(X))A]$ (source writes $\partial_Xs$, a typo for $\partial_XA$); $\nabla^\omega$ is metric for $\lambda$; $d^\omega := d^{\nabla^\omega}$.
- **Bianchi identity in base terms:** $d^\omega\bar\Omega = 0$; locally $d\Omega_\alpha + [\omega_\alpha,\Omega_\alpha] = 0$ (nonlinear in $\omega$).
- **Yang–Mills Lagrangian:** $L_{YM}(\omega) := \tfrac12\lambda(\bar\Omega\wedge*\bar\Omega) = \tfrac12\langle\bar\Omega,\bar\Omega\rangle\mathrm{vol}$; $\int_ML_{YM} = \tfrac12\|\bar\Omega\|^2_{L^2}\ge0$; in the variation the source writes $-\tfrac12\mathrm{tr}(\bar\Omega_t\wedge*\bar\Omega_t)$.
- **Variation:** $\omega_t = \omega + t\eta$, $\eta\in\Omega^1_{\mathrm{Ad}}(P;\mathfrak{su}(N))$; $\Omega_t = \Omega + t(d\eta + [\omega,\eta]) + O(t^2)$, $\bar\Omega_t = \bar\Omega + t\,d^\omega\bar\eta + O(t^2)$ (fn. 5: $[\omega,\eta] = [\eta,\omega]$ for 1-forms).
- **Yang–Mills equation:** $d^\omega*\bar\Omega = 0$.
- **Instanton** := connection with self-dual curvature $*\bar\Omega = \bar\Omega$.
- **First Pontrjagin class:** $p_1(P) := \left[\frac1{8\pi^2}\big(\mathrm{tr}(\bar\Omega)\wedge\mathrm{tr}(\bar\Omega) - \mathrm{tr}(\bar\Omega\wedge\bar\Omega)\big)\right]\in H^4_{dR}(M)$ for a $GL(n;\mathbb R)$-bundle; $p_1(E) := p_1(\text{frame bundle of }E)$; on a compact oriented connected 4-manifold identified with $\int_M$ of a representative.
- **Killing form:** $(A,B)\mapsto\mathrm{tr}(\mathrm{ad}A\circ\mathrm{ad}B)$; $\lambda'(A,B) := -\mathrm{tr}(\mathrm{ad}A\circ\mathrm{ad}B)$; for $\mathfrak{su}(N)$: $\lambda' = 2N\lambda$.
- **Bound (3.18):** $\int_ML_{YM}(\omega)\ge\frac{2\pi^2}{N}|p_1(P\times_{\mathrm{Ad}}\mathfrak g)|$; equality iff $\bar\Omega = \pm*\bar\Omega$.

### Definitions
- **D3.3.1 — Def - Exterior Covariant Derivative** (Def. 3.3.1, p. 97). $d^\nabla: \Omega^k(M;E)\to\Omega^{k+1}(M;E)$ by the formula in conventions.
- **D3.3.2 — Def - Wedge Product and Metric Pairing of Bundle-Valued Forms** (Rem. 3.3.3, pp. 97–98). $\eta\wedge\mu\in\Omega^{k+l}(M;E\otimes E)$ and $\langle\eta\wedge\mu\rangle\in\Omega^{k+l}(M;\mathbb K)$ as above.
- **D3.3.3 — Def - Trace Inner Product on su(N) and on the Adjoint Bundle** (p. 98). $\lambda(A,B) := -\mathrm{tr}(A\cdot B)$; $\lambda([p,A],[p,B]) := \lambda(A,B)$.
- **D3.3.4 — Def - Covariant Derivative on the Adjoint Bundle** (p. 99). $\nabla^\omega_X[s,A] := [s,\partial_XA + \mathrm{ad}(s^*\omega(X))A]$; $d^\omega := d^{\nabla^\omega}$.
- **D3.3.5 — Def - Yang-Mills Lagrangian** (Def. 3.3.4, p. 100). $L_{YM}: \mathcal C(P)\to\Omega^4(M;\mathbb R)$, $\omega\mapsto\tfrac12\lambda(\bar\Omega\wedge*\bar\Omega)$.
- **D3.3.6 — Def - Yang-Mills Connection** (Def. 3.3.7, p. 100). $\omega\in\mathcal C(P)$ is a *Yang–Mills connection* iff critical for the action $\int L_{YM}$ (variations $\omega + t\eta$, $\bar\eta$ compactly supported).
- **D3.3.7 — Def - Instanton** (Def. 3.3.9, p. 102). A connection 1-form $\omega$ with self-dual curvature $\bar\Omega\in\Omega^2(M;P\times_{\mathrm{Ad}}\mathfrak g)$.
- **D3.3.8 — Def - First Pontrjagin Class** (Def. 3.3.10, p. 102). As in conventions, for $GL(n;\mathbb R)$-bundles and real vector bundles; $\mathrm{tr}(\bar\Omega\wedge\bar\Omega)$ in the sense of Rem. 3.3.3.
- **D3.3.9 — Def - Killing Form** (p. 104). $(A,B)\mapsto\mathrm{tr}(\mathrm{ad}(A)\circ\mathrm{ad}(B))$; negative definite iff $G$ semisimple (stated).

### Theorems
- **T3.3.1 — Thm - Square of the Exterior Covariant Derivative Is the Curvature** (Rem. 3.3.2, p. 97). On $\Omega^0(M;E) = \Gamma(E)$: $(d^\nabla d^\nabla\sigma)(X,Y) = \nabla_X\nabla_Y\sigma - \nabla_Y\nabla_X\sigma - \nabla_{[X,Y]}\sigma = R(X,Y)\sigma$; $d^\nabla\circ d^\nabla\equiv0$ iff $R\equiv0$. `Proof in source: full for 0-forms.`
- **T3.3.2 — Thm - Leibniz Rule for the Metric Pairing** (Rem. 3.3.3, p. 98). If $\nabla$ is metric: $d\langle\eta\wedge\mu\rangle = \langle d^\nabla\eta\wedge\mu\rangle + (-1)^k\langle\eta\wedge d^\nabla\mu\rangle$. `Proof in source: omitted (stated).`
- **T3.3.3 — Thm - Trace Form on su(N) Is an Ad-Invariant Inner Product** (p. 98). $\lambda(A,B) = -\mathrm{tr}(AB)$ is real ($\overline{-\mathrm{tr}(AB)} = -\mathrm{tr}(\bar A\bar B) = -\mathrm{tr}(B^*A^*) = -\mathrm{tr}(BA) = -\mathrm{tr}(AB)$), positive definite ($-\mathrm{tr}(AA) = \sum_{i,j}|A^i_j|^2$), and $\mathrm{Ad}$-invariant ($\mathrm{tr}(gAg^{-1}gBg^{-1}) = \mathrm{tr}(AB)$). `Proof in source: full.`
- **T3.3.4 — Thm - Induced Connection on the Adjoint Bundle Is Metric** (p. 99). $\partial_X\lambda([s,A],[s,B]) = \lambda(\nabla^\omega_X[s,A],[s,B]) + \lambda([s,A],\nabla^\omega_X[s,B])$, since $\mathrm{tr}([C,A]B + A[C,B]) = \mathrm{tr}([C,AB]) = 0$. `Proof in source: full.`
- **T3.3.5 — Thm - Bianchi Identity on the Base** (pp. 99–100). $d^\omega\bar\Omega = 0$; locally $d\Omega_\alpha + [\omega_\alpha,\Omega_\alpha] = 0$. `Proof in source: full.` Strategy: at $x$ take vector fields with $[X,Y]_x = [X,Z]_x = [Y,Z]_x = 0$ and a section $s$ with $ds_x(T_xM) = H_{s(x)}$; then $(d^\omega\bar\Omega)_x(X,Y,Z) = \nabla^\omega_X\bar\Omega(Y,Z) - \nabla^\omega_Y\bar\Omega(X,Z) + \nabla^\omega_Z\bar\Omega(X,Y) = [s,d(s^*\Omega)(X,Y,Z)] + [s,\mathrm{ad}(\omega(dsX))\cdots] - \dots$; the $\mathrm{ad}$ terms vanish since $\omega(ds\,X) = 0$ at $x$; $[s,d\Omega(dsX,dsY,dsZ)] = 0$ by Prop. 2.4.5. Gaps: existence of $s$ horizontal at $x$ and of commuting extensions asserted; the local formula $d\Omega_\alpha + [\omega_\alpha,\Omega_\alpha] = 0$ is stated without derivation.
- **T3.3.6 — Thm - Yang-Mills Action Is the Squared L2-Norm of the Curvature** (Rem. 3.3.5, p. 100). $\lambda(\bar\Omega\wedge*\bar\Omega) = \langle\bar\Omega,\bar\Omega\rangle\mathrm{vol}$ for the inner product on $\Lambda^2T^*M\otimes(P\times_{\mathrm{Ad}}\mathfrak g)$; $\int_ML_{YM}(\omega) = \tfrac12\|\bar\Omega\|^2_{L^2}\ge0$. `Proof in source: full (definition of $*$).`
- **T3.3.7 — Thm - Gauge Invariance of the Yang-Mills Lagrangian** (Rem. 3.3.6, p. 100). For $\phi\in\mathcal G(P)$: $L_{YM}(\phi^*\omega) = L_{YM}(\omega)$. `Proof in source: full:` with $\omega' = \phi^*\omega$, $s' := \phi\circ s$, and $g: P\to G$ the section with $\phi(p) = p\cdot g(p)$: $\bar\Omega'(X,Y) = [s,(\phi^*\Omega)(dsX,dsY)] = [\phi^{-1}\circ s',(s')^*\Omega(X,Y)] = [s',\mathrm{Ad}_{g^{-1}\circ s'}(s')^*\Omega(X,Y)]$, so $\bar\Omega' = \mathrm{Ad}_{g^{-1}}\bar\Omega$ and $\lambda$ is $\mathrm{Ad}$-invariant.
- **T3.3.8 — Thm - Yang-Mills Equation** (p. 101). $\omega$ is critical for $L_{YM}$ ⇔ $\forall\bar\eta\in\Omega^1(M;P\times_{\mathrm{Ad}}\mathfrak g)$ compactly supported: $\int_M\mathrm{tr}(\bar\eta\wedge d^\omega*\bar\Omega) = 0$ ⇔ **$d^\omega*\bar\Omega = 0$**. `Proof in source: full.` Strategy: $\Omega_t = d\omega_t + \tfrac12[\omega_t,\omega_t] = \Omega + t(d\eta + [\omega,\eta]) + O(t^2)$ (using symmetry of $[\cdot,\cdot]$ on 1-forms), so $\bar\Omega_t = \bar\Omega + t\,d^\omega\bar\eta + O(t^2)$; $\frac d{dt}|_0\int_{\bar U}L_{YM}(\omega_t) = -\tfrac12\int\mathrm{tr}(\bar\Omega\wedge*d^\omega\bar\eta + d^\omega\bar\eta\wedge*\bar\Omega) = -\int\mathrm{tr}(d^\omega\bar\eta\wedge*\bar\Omega) = -\int d(\mathrm{tr}(\bar\eta\wedge*\bar\Omega)) + \mathrm{tr}(\bar\eta\wedge d^\omega*\bar\Omega) = -\int\mathrm{tr}(\bar\eta\wedge d^\omega*\bar\Omega)$ ($\nabla^\omega$ metric, Stokes). Gaps: the identification $\overline{d\eta + [\omega,\eta]} = d^\omega\bar\eta$ is asserted; the sign convention in the Leibniz step ($(-1)^k$ with $k=1$) is absorbed silently.
- **T3.3.9 — Thm - Self-Dual Connections Are Yang-Mills** (Cor. 3.3.8, p. 102). If $\bar\Omega$ is (anti-)self-dual then $\omega$ is Yang–Mills: $d^\omega*\bar\Omega = \pm d^\omega\bar\Omega = 0$ by Bianchi. `Proof in source: full.`
- **T3.3.10 — Thm - Properties of the First Pontrjagin Class** (Rem. 3.3.11, p. 102). (1) $p_1(E)$ is independent of the connection on the frame bundle; (2) $E$ trivial ⇒ $p_1(E) = 0$; (3) $p_1(\phi^*E) = \phi^*p_1(E)$. `Proof in source: omitted (analogous to §2.5).`
- **T3.3.11 — Thm - Top de Rham Cohomology of a Closed Oriented 4-Manifold** (Rem. 3.3.12, p. 103). On an oriented connected compact 4-manifold, $H^4_{dR}(M)\xrightarrow{\cong}\mathbb R$, $[\omega]\mapsto\int_M\omega$. `Proof in source: omitted (stated).`
- **T3.3.12 — Thm - Yang-Mills Energy Bound and Instantons** (Thm. 3.3.13, pp. 103–105). Let $P\to M$ be an $SU(N)$-bundle over a compact oriented 4-manifold. For every $\omega\in\mathcal C(P)$: $\int_ML_{YM}(\omega)\ge\frac{2\pi^2}N|p_1(P\times_{\mathrm{Ad}}\mathfrak g)|$ (3.18). Moreover: (1) if $p_1<0$, $P$ has no self-dual connections, and $\int L_{YM}\ge-\frac{2\pi^2}Np_1$ with equality iff $\omega$ is anti-self-dual; (2) if $p_1 = 0$, $\omega$ is (anti-)self-dual iff $\bar\Omega\equiv0$ (flat); (3) if $p_1>0$, no anti-self-dual connections, and $\int L_{YM}\ge\frac{2\pi^2}Np_1$ with equality iff self-dual. `Proof in source: full modulo imports.` Strategy: (i) the connection $\phi$ on the frame bundle of $P\times_{\mathrm{Ad}}\mathfrak g$ induced by $\omega$ has curvature $\bar\Phi = \mathrm{ad}\circ\bar\Omega$. (ii) Differentiating $\lambda(\mathrm{Ad}_{\exp tX}A,\mathrm{Ad}_{\exp tX}B) = \lambda(A,B)$ gives $\lambda(\mathrm{ad}(X)A,B) + \lambda(A,\mathrm{ad}(X)B) = 0$: $\mathrm{ad}(X)$ is $\lambda$-skew, hence traceless, so $\mathrm{tr}\bar\Phi = 0$. (iii) $\lambda'(A,B) := -\mathrm{tr}(\mathrm{ad}A\circ\mathrm{ad}B)$ is another $\mathrm{Ad}$-invariant inner product; by "an elementary fact in representation theory" $\lambda' = 2N\lambda$ on $\mathfrak{su}(N)$. (iv) Hence $p_1(P\times_{\mathrm{Ad}}\mathfrak g) = -\frac1{8\pi^2}\int\mathrm{tr}(\mathrm{ad}\bar\Omega\wedge\mathrm{ad}\bar\Omega) = -\frac{2N}{8\pi^2}\int\mathrm{tr}(\bar\Omega\wedge\bar\Omega) = \frac{2N}{8\pi^2}\int\lambda(\bar\Omega,*\bar\Omega)\mathrm{vol}$. (v) $0\le\|\bar\Omega\mp*\bar\Omega\|^2_{L^2} = 2(\|\bar\Omega\|^2\mp\langle\bar\Omega,*\bar\Omega\rangle_{L^2}) = 2(2\int L_{YM}\mp\frac{8\pi^2}{2N}p_1)$, giving (3.18) with equality iff $\bar\Omega = \pm*\bar\Omega$. (vi) Cases: if $p_1<0$ a self-dual $\omega$ would give $\int L_{YM} = \frac{2\pi^2}Np_1<0$, impossible; symmetrically for $p_1>0$; if $p_1 = 0$ and $*\bar\Omega = \pm\bar\Omega$ then $2\int L_{YM} = \|\bar\Omega\|^2 = \pm\frac{8\pi^2}{2N}p_1 = 0$. Gaps: $\bar\Phi = \mathrm{ad}\circ\bar\Omega$ asserted; $\lambda' = 2N\lambda$ imported; the identity $\int\mathrm{tr}(\bar\Omega\wedge\bar\Omega) = -\int\lambda(\bar\Omega,*\bar\Omega)\mathrm{vol}$ uses (3.5) with $p = 0$ and Rem. 3.3.3 implicitly.

### Examples
- None labelled as examples.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R3.3.1** (p. 100) "Note that this is a nonlinear equation in $\omega$!" — the non-abelian Bianchi identity $d\Omega_\alpha + [\omega_\alpha,\Omega_\alpha] = 0$.
- **R3.3.2** (p. 101) Derivation of the Yang–Mills equation by variation (T3.3.8).
- **R3.3.3** (pp. 103–105) Chern–Weil computation of $p_1$ of the adjoint bundle in terms of $\mathrm{tr}(\bar\Omega\wedge\bar\Omega)$ and the $L^2$ argument (T3.3.12).
- **R3.3.4** (Rem. 3.3.12, p. 103) Convention: identify $H^4_{dR}(M)$ with $\mathbb R$ via integration; $p_1$ treated as a number.

### External results imported without proof
- **I3.3.1** Leibniz rule for $d^\nabla$ and the metric pairing (Rem. 3.3.3).
- **I3.3.2** Proportionality of $\mathrm{Ad}$-invariant inner products on a simple Lie algebra; $\lambda' = 2N\lambda$ for $\mathfrak{su}(N)$ ("elementary fact in representation theory", p. 104).
- **I3.3.3** Killing form negative definite iff $G$ semisimple (p. 104).
- **I3.3.4** Curvature of the induced connection on the frame bundle of the adjoint bundle is $\mathrm{ad}\circ\bar\Omega$ (p. 103).
- **I3.3.5** $H^4_{dR}(M)\cong\mathbb R$ via integration for closed connected oriented $M$ (Rem. 3.3.12).
- **I3.3.6** Properties (1)–(3) of $p_1$ (Rem. 3.3.11).

---

# Chapter 4 — Algebraic Topology

## 4.1 Homotopy theory

`PDF pages: 107–116`

### Standing conventions and notation
- $C(X,Y) := \{f: X\to Y\text{ continuous}\}$; $I := [0,1]$; $f_0\simeq f_1$ homotopic; $X\simeq Y$ homotopy equivalent; $f_0\simeq f_1$ rel. $A$.
- $NP\in S^n$ a fixed base point ("north pole"); $S^0 = \{NP,SP\}$.
- $\pi_n(X,x) := \{f\in C(S^n,X)\mid f(NP) = x\}/\simeq\text{rel.}\{NP\}$; cube model $I^n$ with $\psi: I^n\to S^n$, $\psi|_{\mathring I^n}$ a homeomorphism onto $S^n\setminus\{NP\}$, $\psi(\partial I^n) = \{NP\}$; $\pi_n(X,x)\leftrightarrow\{g\in C(I^n,X)\mid g(\partial I^n) = \{x\}\}/\simeq\text{rel.}\,\partial I^n$.
- **Concatenation** in the first coordinate: $(g_1*g_2)(t_1,\dots,t_n) := g_1(2t_1,t_2,\dots)$ for $t_1\le\tfrac12$, $g_2(2t_1-1,t_2,\dots)$ for $t_1\ge\tfrac12$; $[g_1]*[g_2] := [g_1*g_2]$; neutral element the constant map.
- Induced map $g_\sharp[f] := [g\circ f]$.
- Covering := fiber bundle with discrete fiber; lifts $\tilde f$ with $p\circ\tilde f = f$.
- $J^{n-1} := \partial I^n\setminus(I^{n-1}\times\{0\})$ (closure of the boundary minus the bottom face; used in constructing $\partial$); boundary homomorphism $\partial: \pi_n(B,b_0)\to\pi_{n-1}(F,e_0)$, $\partial[u] := [\tilde u|_{I^{n-1}\times\{0\}}]$.
- Long exact sequence (4.1).

### Definitions
- **D4.1.1 — Def - Homotopic Maps and Homotopy** (Def. 4.1.1, p. 107). $f_0,f_1\in C(X,Y)$ are *homotopic* iff there is $f\in C(X\times I,Y)$ with $f(\cdot,0) = f_0$, $f(\cdot,1) = f_1$; write $f_0\simeq f_1$; $f$ is a *homotopy*.
- **D4.1.2 — Def - Homotopy Equivalence** (Def. 4.1.5, p. 108). $X,Y$ are *homotopy equivalent* iff there are $f\in C(X,Y)$, $g\in C(Y,X)$ with $f\circ g\simeq\mathrm{id}_Y$ and $g\circ f\simeq\mathrm{id}_X$ (source misprints $\mathrm{id}_Y$ twice); $f,g$ are *homotopy equivalences* and *homotopy inverses*; write $X\simeq Y$.
- **D4.1.3 — Def - Contractible Space** (Def. 4.1.7, p. 108). $X\simeq\{*\}$.
- **D4.1.4 — Def - Homotopy Relative to a Subset** (Def. 4.1.11, p. 108). $f_0\simeq f_1$ rel. $A$ iff there is a homotopy $f$ from $f_0$ to $f_1$ with $f(a,t) = f_0(a)$ for all $a\in A$, $t\in I$.
- **D4.1.5 — Def - Homotopy Groups** (Def. 4.1.13, p. 109). $\pi_n(X,x) := \{f\in C(S^n,X)\mid f(NP) = x\}/\simeq\text{rel.}\{NP\}$, $n\in\mathbb N_0$, the *$n$-th homotopy group* of $(X,x)$.
- **D4.1.6 — Def - Group Structure on Homotopy Groups** (Rem. 4.1.15, pp. 109–110). Via the cube model and concatenation $g_1*g_2$; for $n\ge1$ this makes $\pi_n(X,x)$ a group with neutral element the constant map.
- **D4.1.7 — Def - Fundamental Group and Simply Connected** (Def. 4.1.18, p. 111). $\pi_1(X,x)$ is the *fundamental group*; a path-connected $X$ ($\pi_0(X,x) = \{x\}$) is *simply connected* iff $\pi_1(X,x) = \{e\}$ for any (hence all) $x$.
- **D4.1.8 — Def - Induced Homomorphism on Homotopy Groups** (Cor. 4.1.20, p. 111). $g_\sharp: \pi_n(X,x)\to\pi_n(Y,g(x))$, $[f]\mapsto[g\circ f]$.
- **D4.1.9 — Def - Covering** (Def. 4.1.27, p. 112). A fiber bundle with discrete fiber.
- **D4.1.10 — Def - Universal Covering** (Ex. 4.1.29, p. 113). For a connected differentiable manifold $X$: the covering $\bar X\to X$ with $\bar X$ simply connected, unique up to isomorphism.
- **D4.1.11 — Def - Lift Through a Covering** (Lemma 4.1.31, p. 113). For a covering $p: \tilde Y\to Y$, $\tilde y\in\tilde Y$, $y = p(\tilde y)$, $f: X\to Y$ with $f(x) = y$: a *lift of $f$ through $\tilde y$* is $\tilde f\in C(X,\tilde Y)$ with $\tilde f(x) = \tilde y$ and $p\circ\tilde f = f$.
- **D4.1.12 — Def - Exact Sequence of Groups** (Def. 4.1.34, p. 114). $\cdots\to G_{i+1}\xrightarrow{f_{i+1}}G_i\xrightarrow{f_i}G_{i-1}\to\cdots$ is *exact* iff $\ker f_i = \mathrm{im}f_{i+1}$ for all $i$.
- **D4.1.13 — Def - Boundary Homomorphism of a Fiber Bundle** (pp. 114–115). For $p: E\to B$, $e_0\in E$, $b_0 = p(e_0)$, $F = E_{b_0}$: given $u\in C(I^n,B)$ with $u(\partial I^n) = \{b_0\}$, lift the family of closed curves (lines in $I^n$ parametrised from $I^{n-1}\times\{1\}$) to curves in $E$ starting at $e_0$, continuously in the initial point, obtaining $\tilde u\in C(I^n,E)$ with $p\circ\tilde u = u$, $\tilde u(J^{n-1}) = \{e_0\}$; set $\partial[u] := [\tilde u|_{I^{n-1}\times\{0\}}]\in\pi_{n-1}(F,e_0)$.

### Theorems
- **T4.1.1 — Thm - Homotopy Is an Equivalence Relation** (Rem. 4.1.3, p. 107). `Proof in source: full:` reflexive (constant homotopy), symmetric ($\tilde f(x,t) := f(x,1-t)$), transitive (concatenate at $t = \tfrac12$).
- **T4.1.2 — Thm - Homotopy Equivalence Is an Equivalence Relation** (Rem. 4.1.6, p. 108). `Proof in source: omitted.`
- **T4.1.3 — Thm - Homeomorphisms Are Homotopy Equivalences** (Rem. 4.1.9, p. 108). Converse false ($\mathbb R^n\simeq\{0\}$). `Proof in source: omitted (obvious).`
- **T4.1.4 — Thm - Relative Homotopy Is an Equivalence Relation** (Rem. 4.1.12, p. 109). `Proof in source: omitted ("as above").`
- **T4.1.5 — Thm - Zeroth Homotopy Set Is the Set of Path Components** (Rem. 4.1.14, p. 109). $\{f\in C(S^0,X)\mid f(NP) = x\}\cong X$ via $x'\mapsto(NP\mapsto x,SP\mapsto x')$; $f\simeq f'$ rel. $NP$ iff $f(SP), f'(SP)$ are joined by a path; so $\pi_0(X,x)\leftrightarrow$ path components. No canonical group structure (Rem. 4.1.15). `Proof in source: full.`
- **T4.1.6 — Thm - Cube Model of Homotopy Groups** (Rem. 4.1.15, p. 109). The bijections $\{f\in C(S^n,X), f(NP) = x\}\leftrightarrow\{g\in C(I^n,X), g(\partial I^n) = \{x\}\}$ and $\simeq$ rel. $NP$ ↔ $\simeq$ rel. $\partial I^n$; concatenation induces a group structure for $n\ge1$. `Proof in source: sketch (bijection via $\psi$; group axioms asserted).`
- **T4.1.7 — Thm - Higher Homotopy Groups Are Abelian** (Prop. 4.1.16, p. 110). For $n\ge2$, $\pi_n(X,x)$ is abelian. `Proof in source: sketch (pictorial chain of six homotopies shrinking $g_1,g_2$ into sub-cubes and rotating them past each other using the second coordinate).`
- **T4.1.8 — Thm - Composition Respects Relative Homotopy** (Lemma 4.1.19, p. 111). $f_0,f_1\in C(X,Y)$, $g_0,g_1\in C(Y,Z)$, $A\subset X$, $B\subset Y$, $f_i(A)\subset B$; if $f_0\simeq f_1$ rel. $A$ and $g_0\simeq g_1$ rel. $B$ then $g_0\circ f_0\simeq g_1\circ f_1$ rel. $A$. `Proof in source: left as exercise.`
- **T4.1.9 — Thm - Continuous Maps Induce Homomorphisms of Homotopy Groups** (Cor. 4.1.20, p. 111). If $[f_0] = [f_1]\in\pi_n(X,x)$ and $g\in C(X,Y)$ then $[g\circ f_0] = [g\circ f_1]\in\pi_n(Y,g(x))$; $g_\sharp$ is a group homomorphism. `Proof in source: full from Lemma 4.1.19 (homomorphism property asserted).`
- **T4.1.10 — Thm - Homotopic Maps Induce the Same Homomorphism** (Cor. 4.1.21, p. 111). $g_0\simeq g_1$ rel. $\{x\}$ ⇒ $(g_0)_\sharp = (g_1)_\sharp$. `Proof in source: full (from Lemma 4.1.19).`
- **T4.1.11 — Thm - Functoriality** (Rem. 4.1.22, p. 112). $(g\circ f)_\sharp = g_\sharp\circ f_\sharp$, $(\mathrm{id}_X)_\sharp = \mathrm{id}$. `Proof in source: full (immediate).`
- **T4.1.12 — Thm - Homotopy Invariance of Homotopy Groups** (Rem. 4.1.23, p. 112). If $(X,x)\simeq(Y,y)$ (pointed homotopy equivalence rel. base points) then $f_\sharp,g_\sharp$ are mutually inverse isomorphisms; homotopy equivalent spaces have isomorphic homotopy groups; contractible spaces have trivial homotopy groups. `Proof in source: full.`
- **T4.1.13 — Thm - Fundamental Group of the Circle** (Ex. 4.1.24, p. 112). $\mathbb Z\to\pi_1(S^1,1)$, $k\mapsto[z\mapsto z^k]$ is an isomorphism; $S^1$ not simply connected; $\mathbb R^2\setminus\{0\}\simeq S^1$ not contractible. `Proof in source: omitted ("one can show").`
- **T4.1.14 — Thm - Spheres of Dimension at Least Two Are Simply Connected** (Ex. 4.1.25, p. 112). `Proof in source: omitted.`
- **T4.1.15 — Thm - Low Homotopy Groups of Spheres** (Rem. 4.1.26, p. 112). $\pi_i(S^n) = \{e\}$ for $i<n$, $\pi_n(S^n) = \mathbb Z$; $\pi_m(S^n)$ for $m>n$ not known in general. `Proof in source: omitted.`
- **T4.1.16 — Thm - Exponential Coverings of Circle and Torus** (Ex. 4.1.28, pp. 112–113). $\exp: \mathbb R\to S^1$, $t\mapsto e^{2\pi it}$ is a covering and a $\mathbb Z$-principal bundle ($(t,k)\mapsto t+k$); $\mathbb R^n\to T^n$ is a $\mathbb Z^n$-principal bundle. `Proof in source: omitted.`
- **T4.1.17 — Thm - Existence of Universal Coverings** (Ex. 4.1.29, p. 113). `Proof in source: omitted.`
- **T4.1.18 — Thm - Power Map Is a Cyclic Covering** (Ex. 4.1.30, p. 113). $S^1\to S^1$, $z\mapsto z^k$ is a $k$-fold covering, a $\mathbb Z_k$-principal bundle. `Proof in source: omitted.`
- **T4.1.19 — Thm - Lifting Lemma** (Lemma 4.1.31, p. 113). Let $p: \tilde Y\to Y$ be a covering, $\tilde y\in\tilde Y$, $y = p(\tilde y)$, $X$ path connected, $x\in X$, $f\in C(X,Y)$ with $f(x) = y$. A lift of $f$ through $\tilde y$ exists iff $f_\sharp(\pi_1(X,x))\subset p_\sharp(\pi_1(\tilde Y,\tilde y))$. `Proof in source: "⇒" full ($f_\sharp[c] = [p\circ\tilde f\circ c] = p_\sharp[\tilde f\circ c]$); "⇐" omitted ("slightly more involved").`
- **T4.1.20 — Thm - Maps from Simply Connected Spaces Lift** (Cor. 4.1.32, p. 114). If $X$ is simply connected, any $f\in C(X,Y)$ lifts to any covering $\tilde Y\to Y$. `Proof in source: full (immediate).`
- **T4.1.21 — Thm - Higher Homotopy Groups of the Circle Vanish** (Ex. 4.1.33, p. 114). $\pi_n(S^1,1) = \{1\}$ for $n\ge2$. `Proof in source: full:` lift $u: S^n\to S^1$ through $0\in\mathbb R$ ($S^n$ simply connected) to $\tilde u$; $[u] = \exp_\sharp[\tilde u] = 0$ since $\pi_n(\mathbb R,0) = 0$.
- **T4.1.22 — Thm - Long Exact Homotopy Sequence of a Fiber Bundle** (Thm. 4.1.35, p. 115, eq. (4.1)). For a fiber bundle $p: E\to B$, $e_0\in E$, $b_0 = p(e_0)$, $F = E_{b_0}$, $\iota: F\hookrightarrow E$: $\cdots\xrightarrow{\partial}\pi_n(F,e_0)\xrightarrow{\iota_\sharp}\pi_n(E,e_0)\xrightarrow{p_\sharp}\pi_n(B,b_0)\xrightarrow{\partial}\pi_{n-1}(F,e_0)\xrightarrow{\iota_\sharp}\cdots\xrightarrow{p_\sharp}\pi_1(B,b_0)$ is exact. `Proof in source: omitted; only $\mathrm{im}\,\iota_\sharp\subset\ker p_\sharp$ (from $p\circ\iota$ constant) and the construction of $\partial$ are given.` Gaps: continuity of the lifted family (homotopy lifting for fiber bundles) is asserted; exactness at every spot omitted.
- **T4.1.23 — Thm - Homotopy Groups of a Product** (Ex. 4.1.36, pp. 115–116). For $E = B\times F$: $\hat p\circ\iota = \mathrm{id}_F$ gives $\iota_\sharp$ injective, $\hat p_\sharp$ surjective, so $\partial = 0$ and (4.1) splits into short exact sequences $0\to\pi_n(F)\to\pi_n(E)\to\pi_n(B)\to0$; $p_\sharp\times\hat p_\sharp: \pi_n(B\times F,(b_0,e_0))\xrightarrow{\cong}\pi_n(B,b_0)\times\pi_n(F,e_0)$. `Proof in source: full` (injectivity: $p_\sharp x = 0$ ⇒ $x = \iota_\sharp y$; $0 = \hat p_\sharp\iota_\sharp y = y$).
- **T4.1.24 — Thm - Third Homotopy Group of the 2-Sphere** (Ex. 4.1.37, p. 116). From the Hopf bundle $S^1\to S^3\to S^2$: $\pi_3(S^1) = 0\to\pi_3(S^3)\xrightarrow{H_\sharp}\pi_3(S^2)\to\pi_2(S^1) = 0$, so $H_\sharp$ is an isomorphism and $\pi_3(S^2)\cong\pi_3(S^3)\cong\mathbb Z$, generated by $[H]$ (the Hopf map). `Proof in source: full given $\pi_3(S^3)\cong\mathbb Z$ generated by $[\mathrm{id}]$.`

### Examples
- **E4.1.1** (Ex. 4.1.2, p. 107) $\mathrm{id}_{\mathbb R^n}\simeq0$ via $f(x,t) := tx$.
- **E4.1.2** (Ex. 4.1.4, p. 107) Any two maps $\mathbb R^n\to\mathbb R^n$ are homotopic.
- **E4.1.3** (Ex. 4.1.8, p. 108) $\mathbb R^n$ is contractible.
- **E4.1.4** (Ex. 4.1.10, p. 108) $S^n\simeq\mathbb R^{n+1}\setminus\{0\}$ via inclusion and $y\mapsto y/\|y\|$, homotopy $G(y,t) := (1-t+\frac t{\|y\|})y$.
- **E4.1.5** (Ex. 4.1.24, p. 112) $\pi_1(S^1) = \mathbb Z$. **E4.1.6** (Ex. 4.1.25) $S^n$ simply connected for $n\ge2$.
- **E4.1.7** (Ex. 4.1.28, 4.1.29, 4.1.30, pp. 112–113) Coverings $\mathbb R\to S^1$, $\mathbb R^n\to T^n$, universal covering, $z\mapsto z^k$.
- **E4.1.8** (Ex. 4.1.33, p. 114) $\pi_n(S^1) = 0$ for $n\ge2$.
- **E4.1.9** (Ex. 4.1.36, p. 115) Trivial bundle. **E4.1.10** (Ex. 4.1.37, p. 116) $\pi_3(S^2)\cong\mathbb Z$.

### Exercises
- **X4.1.1** (Lemma 4.1.19, p. 111) Prove: if $f_0\simeq f_1$ rel. $A$ and $g_0\simeq g_1$ rel. $B$ with $f_i(A)\subset B$, then $g_0\circ f_0\simeq g_1\circ f_1$ rel. $A$.

### Remarks / load-bearing paragraphs
- **R4.1.1** (Rem. 4.1.17, p. 110) $\pi_1(X,x)$ is in general not abelian.
- **R4.1.2** (pp. 114–115) Construction of the boundary homomorphism $\partial$ via lifting a family of loops (with figure).
- **R4.1.3** (Rem. 4.1.26 figure, p. 112) Picture of a map $S^m\to S^n$.

### External results imported without proof
- **I4.1.1** $\pi_1(S^1)\cong\mathbb Z$; $\pi_i(S^n) = 0$ for $i<n$; $\pi_n(S^n)\cong\mathbb Z$ generated by $[\mathrm{id}]$.
- **I4.1.2** Existence and uniqueness of universal coverings for connected manifolds.
- **I4.1.3** "⇐" of the Lifting Lemma; path/homotopy lifting for coverings and fiber bundles.
- **I4.1.4** Exactness of the long exact homotopy sequence (Thm. 4.1.35).
- **I4.1.5** Group axioms for concatenation on $\pi_n$.

---

## 4.2 Homology theory

`PDF pages: 116–126`

### Standing conventions and notation
- Complex $(A_\bullet,f_\bullet)$ of abelian groups with $\mathrm{im}f_k\subset\ker f_{k-1}$; $H_k := \ker f_k/\mathrm{im}f_{k+1}$.
- **Standard simplex** $\Delta^n := \{(t_0,\dots,t_n)\in\mathbb R^{n+1}\mid t_i\ge0,\sum t_i = 1\}$; **$k$-th side** $\iota^n_k: \Delta^{n-1}\to\Delta^n$, $(t_0,\dots,t_{n-1})\mapsto(t_0,\dots,t_{k-1},0,t_k,\dots,t_{n-1})$.
- $R$ a commutative ring with unit ($\mathbb Z,\mathbb Z/k\mathbb Z,\mathbb Q,\mathbb R,\mathbb C$); $C_n(X;R)$ free $R$-module on $C(\Delta^n,X)$; **boundary** $\partial_n\sigma := \sum_{k=0}^n(-1)^k\sigma\circ\iota^n_k$; $\partial\circ\partial = 0$; $Z_n$, $B_n$, $H_n(X;R) := Z_n/B_n$.
- $f_*(\sum\alpha_j\sigma_j) := \sum\alpha_j(f\circ\sigma_j)$; $\partial f_* = f_*\partial$; $f_*[z] := [f_*z]$.
- **Mayer–Vietoris** for open $X_0\cup X_1 = X$, $j_\nu: X_\nu\hookrightarrow X$, $i_\nu: X_0\cap X_1\hookrightarrow X_\nu$: $\cdots\to H_n(X_0\cap X_1)\xrightarrow{(i^0_*,i^1_*)}H_n(X_0)\oplus H_n(X_1)\xrightarrow{(j^0_*,-j^1_*)}H_n(X)\xrightarrow{\partial}H_{n-1}(X_0\cap X_1)\to\cdots$ exact.
- Sphere decomposition: $S^m = D_+\cup D_-$ with $D_\pm\simeq\{p\}$, $D_+\cap D_-\simeq S^{m-1}$.
- $\dot M := M\setminus\{x\}$; connected sum $M\#N$; $[c]\in H_n(S^n;\mathbb Z)\cong\mathbb Z$ a fixed generator; Hurewicz $h[f] := f_*[c]$; $[G,G]$ commutator subgroup; $G^{abel} := G/[G,G]$; $\mathbb Z*\mathbb Z$ free group.

### Definitions
- **D4.2.1 — Def - Chain Complex of Abelian Groups** (Def. 4.2.1, p. 116). A sequence $\cdots\to A_{k+1}\xrightarrow{f_{k+1}}A_k\xrightarrow{f_k}A_{k-1}\to\cdots$ of homomorphisms of abelian groups with $\mathrm{im}f_k\subset\ker f_{k-1}$ for all $k$.
- **D4.2.2 — Def - Homology of a Complex** (Def. 4.2.2, p. 116). $H_k(A_\bullet,f_\bullet) := \ker(f_k: A_k\to A_{k-1})/\mathrm{im}(f_{k+1}: A_{k+1}\to A_k)$.
- **D4.2.3 — Def - Standard Simplex Singular Simplex and Sides** (Def. 4.2.4, p. 117). As in conventions; a *singular $n$-simplex* in $X$ is $\sigma\in C(\Delta^n,X)$.
- **D4.2.4 — Def - Singular Chains and Boundary Operator** (Def. 4.2.6, p. 118). $C_n(X;R) := \{\sum_k\alpha_k\sigma_k\mid\alpha_k\in R,\sigma_k\in C(\Delta^n,X)\}$; $\partial_n(\sigma) := \sum_{k=0}^n(-1)^k\sigma\circ\iota^n_k$, extended linearly.
- **D4.2.5 — Def - Cycles Boundaries and Singular Homology** (Def. 4.2.7, p. 118). $Z_n(X;R) := \ker\partial_n$ (*$n$-cycles*), $B_n(X;R) := \mathrm{im}\,\partial_{n+1}$ (*$n$-boundaries*), $H_n(X;R) := Z_n/B_n$ the *$n$-th singular homology with coefficients in $R$*.
- **D4.2.6 — Def - Induced Map on Homology** (p. 119). $f_*[z] := [f_*z]$ for $f\in C(X,Y)$.
- **D4.2.7 — Def - Connected Sum** (Ex. 4.2.15, p. 123). $M\#N$: remove a small ball from each of $M,N$ and glue the remainders along the boundary spheres (filling in a small neck).
- **D4.2.8 — Def - Hurewicz Homomorphism** (Def. 4.2.17, p. 124). Fix a generator $[c]\in H_n(S^n;\mathbb Z)\cong\mathbb Z$; for path-connected $X$, $x\in X$: $h: \pi_n(X,x)\to H_n(X;\mathbb Z)$, $h([f]) := f_*([c])$.
- **D4.2.9 — Def - Commutator Subgroup and Abelianization** (Rem. 4.2.19, p. 125). $[G,G]$ := normal subgroup generated by all $ghg^{-1}h^{-1}$; $G^{abel} := G/[G,G]$; $G$ abelian ⇒ $G^{abel} = G$.

### Theorems
- **T4.2.1 — Thm - Homology Measures Failure of Exactness** (Rem. 4.2.3, p. 116). $(A_\bullet,f_\bullet)$ exact iff $H_k = 0$ for all $k$. `Proof in source: full (immediate).`
- **T4.2.2 — Thm - Boundary Squared Is Zero** (p. 118). $\partial\circ\partial\equiv0$. `Proof in source: omitted (stated).`
- **T4.2.3 — Thm - Chain Maps Commute with the Boundary** (p. 119). $\partial\circ f_* = f_*\circ\partial$, so $f_*$ preserves cycles and boundaries and descends to homology. `Proof in source: omitted (stated).`
- **T4.2.4 — Thm - Eilenberg-Steenrod Properties of Singular Homology** (Rem. 4.2.8, pp. 119–120). (1) Functoriality: $(g\circ f)_* = g_*f_*$, $(\mathrm{id})_* = \mathrm{id}$. (2) Homotopy invariance: $f\simeq g$ ⇒ $f_* = g_*$. (3) Coefficients: $H_n(\{p\};R) = R$ for $n = 0$, $0$ for $n\ge1$. (4) Mayer–Vietoris exact sequence. `Proof in source: (1) full (from definitions); (3) full; (2),(4) omitted ("to be done in a lecture course on algebraic topology").` Strategy (3): only one $n$-simplex $\sigma_n$ in a point; $\partial\sigma_n = (\sum_k(-1)^k)\sigma_{n-1} = 0$ ($n$ odd) or $\sigma_{n-1}$ ($n$ even); complex $0\leftarrow R\xleftarrow0R\xleftarrow1R\xleftarrow0\cdots$; $H_{2n} = \ker1/\mathrm{im}0 = 0$, $H_{2n-1} = \ker0/\mathrm{im}1 = 0$, $H_0 = R/\mathrm{im}0 = R$.
- **T4.2.5 — Thm - Homotopy Invariance of Homology Groups** (Rem. 4.2.9, p. 120). $X\simeq Y$ ⇒ $H_n(X;R)\cong H_n(Y;R)$. `Proof in source: full (from (1),(2)).`
- **T4.2.6 — Thm - Homology of the Empty Set** (Rem. 4.2.10, p. 120). $C_n(\emptyset;R) = 0$, $H_n(\emptyset;R) = 0$. `Proof in source: full.`
- **T4.2.7 — Thm - Homology of a Disjoint Union** (Rem. 4.2.11, p. 120). $X = X_0\sqcup X_1$ ⇒ $H_n(X_0)\oplus H_n(X_1)\cong H_n(X)$. `Proof in source: full (Mayer–Vietoris with empty intersection).`
- **T4.2.8 — Thm - Zeroth Homology of a Path-Connected Space** (Rem. 4.2.12, p. 120). $H_0(X;R)\cong R$. `Proof in source: omitted.`
- **T4.2.9 — Thm - Homology of Spheres** (Ex. 4.2.13, pp. 120–121). $H_k(S^m;R) = R$ for $k\in\{0,m\}$ and $0$ otherwise ($m\ge1$); $H_k(S^0;R) = R^2$ for $k = 0$, $0$ otherwise. `Proof in source: full (induction via Mayer–Vietoris).` Strategy: (a) $S^0$ from T4.2.7. (b) $S^1 = D_+\cup D_-$: for $n\ge2$ the MV sequence $0\to H_n(S^1)\to H_{n-1}(S^0) = 0$; for $n = 1$: $0\to H_1(S^1)\to H_0(D_+\cap D_-)\cong R^2\xrightarrow{\begin{pmatrix}1&1\\1&1\end{pmatrix}}R^2$, so $H_1(S^1) = \ker = \{(x,-x)\}\cong R$. (c) $S^m$, $m\ge2$: for $k\ge2$, $H_k(S^m)\cong H_{k-1}(S^{m-1})$; $H_0 = R$; $H_1(S^m)\to H_0(S^{m-1}) = R\xrightarrow{(1,1)^t}R^2$ injective so $H_1(S^m) = 0$.
- **T4.2.10 — Thm - Homology of Complex Projective Space** (Ex. 4.2.14, pp. 122–123, eq. (4.2)). $H_k(\mathbb{CP}^n;R) = R$ for $k = 0,2,4,\dots,2n$ and $0$ otherwise. `Proof in source: full (induction via Mayer–Vietoris).` Strategy: $\mathbb{CP}^1 = S^2$; cover $\mathbb{CP}^n$ by $X_0 := \{\ell\mid\ell\cap B_2\neq\emptyset\}\cong B_2\simeq\{p\}$ and $X_1 := \{\ell\mid\ell\cap\bar B_1 = \emptyset\}\simeq\mathbb{CP}^{n-1}$ for concentric balls $B_1\subset B_2\subset\mathbb C^n + e_{n+1}$ (model of Rem. 1.5.15); $X_0\cap X_1\cong B_2\setminus\bar B_1\simeq S^{2n-1}$; MV gives $H_k(\mathbb{CP}^n)\cong H_k(\mathbb{CP}^{n-1})$ for $k\neq0,1,2n-1,2n$; $H_0 = R$; $H_1 = 0$ (the map $H_0(S^1)\to H_0(\{p\})\oplus H_0(\mathbb{CP}^{n-1})$ is injective; source writes $S^1$ for $S^{2n-1}$); $H_{2n-1} = 0$; $H_{2n}\cong H_{2n-1}(S^{2n-1}) = R$. Gaps: the homotopy equivalences $X_0\simeq\{p\}$, $X_1\simeq\mathbb{CP}^{n-1}$ asserted.
- **T4.2.11 — Thm - Homology of Punctured Manifolds and Connected Sums** (Ex. 4.2.15, pp. 123–124). For an $n$-manifold $M$, $\dot M = M\setminus\{x\}$: for $k\notin\{0,1,n-1,n\}$ the inclusion induces $H_k(\dot M;R)\cong H_k(M;R)$. For $M\#N$ with $X_0 = \dot M$, $X_1 = \dot N$, $X_0\cap X_1\cong S^{n-1}\times(0,1)\simeq S^{n-1}$: $H_k(M)\oplus H_k(N)\cong H_k(M\#N;R)$ for $k\notin\{0,1,n-1,n\}$; in particular for $n = 4$, $k = 2$. `Proof in source: full (MV).`
- **T4.2.12 — Thm - No Retraction of the Ball onto Its Boundary Sphere** (Ex. 4.2.16, p. 124). There is no continuous $f: \bar B^{n+1}\to S^n$ with $f|_{S^n} = \mathrm{id}$. `Proof in source: full:` otherwise $\mathrm{id} = (f\circ\iota)_* = f_*\iota_*$ on $H_n(S^n;\mathbb Z)\cong\mathbb Z$ would factor through $H_n(\bar B^{n+1};\mathbb Z) = 0$.
- **T4.2.13 — Thm - Hurewicz Homomorphism Is Well-Defined** (Rem. 4.2.18, p. 124). $h$ is well-defined by homotopy invariance; that it is a homomorphism is `omitted`.
- **T4.2.14 — Thm - Hurewicz Homomorphism Factors Through the Abelianization** (Rem. 4.2.21, p. 125). $h$ vanishes on $[\pi_n,\pi_n]$, giving $h: \pi_n(X,x)^{abel}\to H_n(X;\mathbb Z)$. `Proof in source: full (target abelian).`
- **T4.2.15 — Thm - Hurewicz Theorem** (Thm. 4.2.22, p. 125). Let $X$ be path connected, $x\in X$, $\pi_k(X,x) = 0$ for $k = 1,\dots,m-1$. Then $h: \pi_m(X,x)^{abel}\to H_m(X;\mathbb Z)$ is an isomorphism. (For $m\ge2$, $\pi_m$ is already abelian — Rem. 4.2.23.) `Proof in source: omitted.`
- **T4.2.16 — Thm - Homotopy Groups of Spheres Below the Dimension** (Ex. 4.2.24, p. 125). For $n\ge2$ and $m\le n$: $\pi_m(S^n,NP)\cong H_m(S^n;\mathbb Z) = \mathbb Z$ if $m = n$, $0$ if $1\le m<n$. `Proof in source: full (iterated Hurewicz using T4.2.9).` The hypothesis is necessary: $\pi_3(S^2)\cong\mathbb Z$ but $H_3(S^2;\mathbb Z) = 0$ (p. 126).
- **T4.2.17 — Thm - Connected Sum of Simply Connected Manifolds** (Rem. 4.2.25, p. 126). If $M,N$ are simply connected topological manifolds of dimension $\ge2$ then $M\#N$ is simply connected. `Proof in source: omitted.`
- **T4.2.18 — Thm - Abelianization of the Free Group on Two Generators** (Ex. 4.2.20, p. 125). $(\mathbb Z*\mathbb Z)^{abel} = \mathbb Z^2$. `Proof in source: omitted.`

### Examples
- **E4.2.1** (Ex. 4.2.5, p. 117) Pictures of $\Delta^0,\Delta^1,\Delta^2$ and the side maps $\iota^1_0,\iota^1_1,\iota^2_0,\iota^2_1,\iota^2_2$.
- **E4.2.2** (Ex. 4.2.13) Spheres. **E4.2.3** (Ex. 4.2.14) $\mathbb{CP}^n$. **E4.2.4** (Ex. 4.2.15) Punctured manifolds, connected sums. **E4.2.5** (Ex. 4.2.16) No retraction. **E4.2.6** (Ex. 4.2.20) $(\mathbb Z*\mathbb Z)^{abel}$. **E4.2.7** (Ex. 4.2.24) $\pi_m(S^n)$, $m\le n$.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R4.2.1** (p. 119) Naturality of chains: $f_*$ commutes with $\partial$.
- **R4.2.2** (p. 126) Failure of Hurewicz without the vanishing hypothesis ($\pi_3(S^2)$ vs $H_3(S^2)$).

### External results imported without proof
- **I4.2.1** $\partial\circ\partial = 0$ for singular chains.
- **I4.2.2** Homotopy invariance of singular homology (Rem. 4.2.8(2)).
- **I4.2.3** Mayer–Vietoris sequence (Rem. 4.2.8(4)).
- **I4.2.4** $H_0$ of a path-connected space is $R$.
- **I4.2.5** Hurewicz homomorphism is a homomorphism; Hurewicz theorem.
- **I4.2.6** Connected sums of simply connected manifolds are simply connected (Seifert–van Kampen).
- **I4.2.7** Standard mollifier/smoothing and the homotopy equivalences used in the $\mathbb{CP}^n$ cover.

---

## 4.3 Orientations and the fundamental class

`PDF pages: 126–130`

### Standing conventions and notation
- $R$ a ring with unit throughout.
- $\dot B(x,r) := B(x,r)\setminus\{x\}$; $F_{x,r}: S^{n-1}\to\dot B(x,r)$, $y\mapsto x + \tfrac r2y$, a homotopy equivalence; $(F_{x,r})_*: H_{n-1}(S^{n-1};R)\xrightarrow{\cong}H_{n-1}(\dot B(x,r);R)$; for $r_1<r_2$, $(F_{x,r_2})_* = (\iota_{r_1,r_2})_*\circ(F_{x,r_1})_*$.
- $\mathcal K_x$ := charts sending $x$ to $0$; $\tilde M_x := \mathcal K_x/\sim$; $\tilde M := \bigsqcup_x\tilde M_x$ the $R$-orientation covering.
- $[M]\in H_n(M;R)$ fundamental class; $\alpha\in H_k(X;R)$ represented by $f: M\to X$ iff $\alpha = f_*[M]$.
- $(S^2\times S^2)^\cdot := (S^2\times S^2)\setminus\{-(p_1,p_2)\}$; $f_1(x) := (x,p_2)$, $f_2(x) := (p_1,x)$.

### Definitions
- **D4.3.1 — Def - R-Orientation Preserving Homeomorphism** (Def. 4.3.1, p. 126). For open $U,V\subset\mathbb R^n$, a homeomorphism $\Phi: U\to V$ is *$R$-orientation preserving at $x\in U$* iff for every $\varrho>0$ with $B(\Phi(x),\varrho)\subset V$ and every $r>0$ with $\Phi(B(x,r))\subset B(\Phi(x),\varrho)$: $(\Phi|_{\dot B(x,r)})_*\circ(F_{x,r})_* = (F_{\Phi(x),\varrho})_*$ as maps $H_{n-1}(S^{n-1};R)\to H_{n-1}(\dot B(\Phi(x),\varrho);R)$. $\Phi$ is *$R$-orientation preserving* iff so at every $x\in U$.
- **D4.3.2 — Def - R-Oriented Atlas and R-Orientation** (Def. 4.3.5, pp. 127–128). An atlas $\mathcal A$ of a topological $n$-manifold $M$ is *$R$-oriented* iff all chart changes $\Phi\circ\Psi^{-1}$, $\Phi,\Psi\in\mathcal A$, are $R$-orientation preserving; a maximal $R$-oriented atlas is an *$R$-orientation*; $(M,\mathcal A)$ an *$R$-oriented manifold*; $M$ is *$R$-orientable* iff it admits an $R$-orientation.
- **D4.3.3 — Def - R-Orientation Covering** (Rem. 4.3.8, p. 128). On $\mathcal K_x$: $\Phi\sim\Psi$ iff $\Phi\circ\Psi^{-1}$ is $R$-orientation preserving at $0$; $\tilde M_x := \mathcal K_x/\sim$, $\tilde M := \bigsqcup_x\tilde M_x$ with an appropriate topology is a covering of $M$.
- **D4.3.4 — Def - Fundamental Class** (Def. 4.3.10, p. 129). For $M$ compact, connected, $R$-oriented topological $n$-manifold: $[M]\in H_n(M;R)$ is the class mapped to $1\in R$ under the distinguished isomorphism $H_n(M;R)\xrightarrow{\partial}H_{n-1}(\dot B;R)\xrightarrow{\cong}H_{n-1}(S^{n-1};R)\cong R$ (Rem. 4.3.9).
- **D4.3.5 — Def - Homology Class Represented by a Map** (Def. 4.3.12, p. 129). For $X$ a space and $M$ an $R$-oriented connected compact topological $k$-manifold, $\alpha\in H_k(X;R)$ is *represented by* $f: M\to X$ iff $\alpha = f_*([M])$.

### Theorems
- **T4.3.1 — Thm - Compatibility of Radial Homotopy Equivalences** (p. 126). $(F_{x,r_2})_* = (\iota_{r_1,r_2})_*(F_{x,r_1})_*$ for $r_1<r_2$ (diagram commutes up to homotopy). `Proof in source: full (stated with reason).`
- **T4.3.2 — Thm - Every Homeomorphism Is Z/2-Orientation Preserving** (Ex. 4.3.3, p. 127). For $R = \mathbb Z/2\mathbb Z$ the identity is the only automorphism of $R$, so the diagram always commutes. `Proof in source: full.`
- **T4.3.3 — Thm - One Pair of Radii Suffices** (Rem. 4.3.4, p. 127). To check $R$-orientation preservation at $x$ it suffices to check the diagram for one $r$ and one $\varrho$: the upper square in the two-radii diagram commutes for all radii, so the lower triangle commutes iff the whole diagram does. `Proof in source: full.`
- **T4.3.4 — Thm - Every Manifold Is Z/2-Orientable** (Rem. 4.3.6, p. 128). `Proof in source: full (from T4.3.2).`
- **T4.3.5 — Thm - Differentiable Orientability Equals Z-Orientability** (Rem. 4.3.7, p. 128). `Proof in source: omitted.`
- **T4.3.6 — Thm - Simply Connected Manifolds Are R-Orientable** (Rem. 4.3.8, p. 128). If $M$ is simply connected, $\mathrm{id}_M$ lifts (Lemma 4.1.31) to a continuous section $\widetilde{\mathrm{id}_M}: M\to\tilde M$ of the $R$-orientation covering; any such lift is an $R$-orientation. `Proof in source: sketch.` Gaps: topology of $\tilde M$ and that a section gives an oriented atlas asserted.
- **T4.3.7 — Thm - Top Homology of a Closed Oriented Manifold** (Rem. 4.3.9, p. 128). For $M$ compact connected $R$-oriented, $X_0 = \dot M$, $X_1 = B\ni x$ a ball: MV gives $0\to H_n(M;R)\xrightarrow{\partial}H_{n-1}(\dot B;R)\to0$ (both outer terms $H_n(\dot M)\oplus H_n(\{p\})$ and $H_{n-1}(\dot M)\oplus H_{n-1}(\{p\})$ are claimed $0$); $\partial$ is an isomorphism (Poincaré duality); the orientation gives $H_{n-1}(\dot B;R)\cong H_{n-1}(S^{n-1};R)\cong R$; hence a distinguished $H_n(M;R)\cong R$. `Proof in source: sketch; the isomorphism $\partial$ is imported.` Gaps: vanishing of $H_n(\dot M)$ and $H_{n-1}(\dot M)$ asserted (the latter is false in general, e.g. for $M = T^n$; the correct statement is only that $\partial$ is an isomorphism onto $H_{n-1}(\dot B)$ when $M$ is closed connected oriented).
- **T4.3.8 — Thm - Triangulations Represent the Fundamental Class** (Rem. 4.3.11, p. 129). If $M$ admits a triangulation $T$, the formal sum of its (suitably parametrised, oriented) simplices represents $[M]$. `Proof in source: omitted.`
- **T4.3.9 — Thm - Homology of the Product of Two 2-Spheres** (Ex. 4.3.13(4), pp. 129–130). $f_1,f_2: S^2\to S^2\times S^2$ represent the two generators of $H_2(S^2\times S^2;R)\cong R^2$; $H_k(S^2\times S^2;R) = R$ for $k = 0,4$, $R^2$ for $k = 2$, $0$ for $k = 1,3$. `Proof in source: full.` Strategy: $\iota: (S^2\times S^2)^\cdot\hookrightarrow S^2\times S^2$ induces an isomorphism on $H_2$ (Ex. 4.2.15); cover $(S^2\times S^2)^\cdot$ by $X_0 := S^2\times(S^2\setminus\{-p_2\})\simeq S^2\times\{p_2\}$ and $X_1 := (S^2\setminus\{-p_1\})\times S^2\simeq\{p_1\}\times S^2$ (source writes $-p_2$ twice) with $X_0\cap X_1\cong D^2\times D^2\simeq\{pt\}$; MV: $0\to H_2(S^2\times\{p_2\})\oplus H_2(\{p_1\}\times S^2)\xrightarrow{\cong}H_2((S^2\times S^2)^\cdot)\to0$; compose with $((f_1)_*,(f_2)_*)$.
- **T4.3.10 — Thm - Bounding Classes Vanish** (Rem. 4.3.14, p. 130). Let $\alpha\in H_k(X;R)$ be represented by $f: M\to X$, $W$ a compact connected $R$-oriented $(k+1)$-manifold with $\partial W = M$, and $F: W\to X$ continuous with $F|_{\partial W} = f$. Then $\alpha = 0$. `Proof in source: full given the imported fact that $\iota: M = \partial W\hookrightarrow W$ represents $0\in H_k(W;R)$ (Poincaré duality):` $\alpha = f_*[M] = (F\circ\iota)_*[M] = F_*(\iota_*[M]) = 0$.

### Examples
- **E4.3.1** (Ex. 4.3.2, p. 127) Picture of the definition for $n = 2$, $R = \mathbb Z$.
- **E4.3.2** (Ex. 4.3.3, p. 127) $R = \mathbb Z/2\mathbb Z$.
- **E4.3.3** (Ex. 4.3.13(1), p. 129) $\mathrm{id}_M$ represents $[M]$.
- **E4.3.4** (Ex. 4.3.13(2), p. 129) Any $f: \{p\}\to X$ represents a generator of $H_0(X;R)\cong R$ for path-connected $X$.
- **E4.3.5** (Ex. 4.3.13(3), p. 129) $\iota: \mathbb{CP}^{n-1}\hookrightarrow\mathbb{CP}^n$ represents a generator of $H_{2n-2}(\mathbb{CP}^n)$; $\iota: \mathbb{CP}^k\hookrightarrow\mathbb{CP}^n$ represents generators of $H_{2k}(\mathbb{CP}^n)$, $k = 1,\dots,n$ (from the MV computation of Ex. 4.2.14).
- **E4.3.6** (Ex. 4.3.13(4), pp. 129–130) $S^2\times S^2$ — see T4.3.9.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R4.3.1** (p. 126) Setup of $F_{x,r}$ and compatibility under change of radius.
- **R4.3.2** (Rem. 4.3.9) The MV argument identifying $H_n(M;R)\cong R$ (T4.3.7).
- **R4.3.3** (Rem. 4.3.14) The bounding argument (T4.3.10) — used in §5.1 Step 4 to show the handle-attaching modification does not change the homology class.

### External results imported without proof
- **I4.3.1** Poincaré duality in the form: for closed connected $R$-oriented $M$, $\partial: H_n(M;R)\to H_{n-1}(\dot B;R)$ is an isomorphism (Rem. 4.3.9).
- **I4.3.2** Poincaré duality in the form: the boundary inclusion $\partial W\hookrightarrow W$ represents $0$ in $H_k(W;R)$ (Rem. 4.3.14).
- **I4.3.3** Smooth orientability = $\mathbb Z$-orientability (Rem. 4.3.7).
- **I4.3.4** Topology on the orientation covering; triangulations represent $[M]$ (Rem. 4.3.8, 4.3.11).

---

# Chapter 5 — 4-dimensional Manifolds

## 5.1 The intersection form

`PDF pages: 131–138`

### Standing conventions and notation
- **Standing hypothesis (§5.1):** $X$ a compact, oriented, simply connected, **differentiable** 4-manifold. $H_2(X;\mathbb Z)\cong\mathbb Z^r$ (no torsion, Rem. 5.1.9).
- **Intersection number** of embedded compact oriented surfaces $S_1,S_2\subset X$ meeting transversally (or not at all): $S_1\cdot S_2 := \sum_{p\in S_1\cap S_2}\varepsilon(p)$, $\varepsilon(p) = +1$ iff the orientation of $T_pS_1\oplus T_pS_2 = T_pX$ induced from $S_1,S_2$ (in this order) agrees with that of $X$, else $-1$.
- **Intersection form** $Q_X: H_2(X;\mathbb Z)\times H_2(X;\mathbb Z)\to\mathbb Z$, $([S_1],[S_2])\mapsto S_1\cdot S_2$ (source misprints $S_2\cdot S_2$).
- $\overline X$: $X$ with reversed orientation; $Q_{\overline X} = -Q_X$. $\overline{\mathbb{CP}^2}$ := $\mathbb{CP}^2$ with reversed orientation.
- $k\mathbb{CP}^2\#l\overline{\mathbb{CP}^2}$ := connected sum of $k$ copies of $\mathbb{CP}^2$ and $l$ of $\overline{\mathbb{CP}^2}$; $Q = \mathrm{diag}(1,\dots,1,-1,\dots,-1)$ ($k$ ones, $l$ minus ones).
- **Unimodular:** $\det(Q(e_i,e_j))_{i,j} = \pm1$ for some (hence every) basis (5.1). **Rank** $\mathrm{rk}(Q) := \dim H$. **Signature** $\mathrm{sign}(Q) := \#\{\text{positive eigenvalues}\} - \#\{\text{negative eigenvalues}\}$ after diagonalising over $\mathbb R$ or $\mathbb Q$; $\mathrm{sign}(X) := \mathrm{sign}(Q_X)$. **Definite/indefinite; parity** even iff $Q(a,a)\in2\mathbb Z$ for all $a$, else odd.
- Direct sum: $Q_{X_1\#X_2} = Q_{X_1}\oplus Q_{X_2}$, $\mathrm{sign}(X_1\#X_2) = \mathrm{sign}X_1 + \mathrm{sign}X_2$ (5.2).
- **$E_8$ form** (5.3): the symmetric $8\times8$ matrix with $2$ on the diagonal, $1$ in positions $(1,2),(2,3),(3,4),(4,5),(5,6)$ ... as printed: row 1 $(2,1,0,0,0,0,0,0)$, row 2 $(1,2,1,0,0,0,0,0)$, row 3 $(0,1,2,1,0,0,0,0)$, row 4 $(0,0,1,2,1,0,0,0)$, row 5 $(0,0,0,1,2,0,0,1)$, row 6 $(0,0,0,0,0,2,1,0)$, row 7 $(0,0,0,0,0,1,2,0)$, row 8 $(0,0,0,0,1,0,0,2)$ — i.e. the Cartan matrix of $E_8$ in some vertex ordering (the printed matrix has a $1$ at $(5,8)$/$(8,5)$ and a chain $6-7$ disconnected from $1{-}2{-}3{-}4{-}5{-}8$; this appears to be a transcription defect in the source; the intended matrix is the $E_8$ Cartan matrix with $\det = 1$). Even, positive definite, $\mathrm{sign}(E_8) = 8$.
- **Homogeneous coordinates** $[z_0:\dots:z_n]$ on $\mathbb{CP}^n = U(1)\backslash S^{2n+1}$.
- **K3 surface:** $K3 := \{[z_0:z_1:z_2:z_3]\in\mathbb{CP}^3\mid z_0^4+z_1^4+z_2^4+z_3^4 = 0\}$; $Q_{K3} = (-E_8)\oplus(-E_8)\oplus3\begin{pmatrix}0&1\\1&0\end{pmatrix}$, even, indefinite, $\mathrm{sign}(K3) = -16$.
- Dirac operator $D = \begin{pmatrix}0&D^-\\D^+&0\end{pmatrix}$ on the spinor bundle; $\mathrm{ind}(D^+) := \dim\ker D^+ - \dim\ker D^-$; quaternionic structure $J$ ($\mathbb C$-antilinear, $J^2 = -\mathrm{id}$).

### Definitions
- **D5.1.1 — Def - Transversal Immersion with Double Points** (Step 3, p. 131). An immersion $f: S^2\to X$ with finitely many double points $x_i = f(p_i) = f(q_i)$, $p_i\neq q_i$, $x_i\neq x_j$, such that $df(T_{p_i}S^2)\oplus df(T_{q_i}S^2) = T_{x_i}X$ ("$f$ is transversal").
- **D5.1.2 — Def - Intersection Number and Intersection Form** (Def. 5.1.2, p. 133). As in conventions.
- **D5.1.3 — Def - Connected Sums of Projective Planes** (Ex. 5.1.8, p. 134). $k\mathbb{CP}^2\#l\overline{\mathbb{CP}^2}$.
- **D5.1.4 — Def - Unimodular Form** (Def. 5.1.10, p. 135). A symmetric bilinear form $Q$ on a free $\mathbb Z$-module $H\cong\mathbb Z^r$ is *unimodular* iff there is a basis $e_1,\dots,e_r$ with $\det(Q(e_i,e_j))_{i,j} = \pm1$.
- **D5.1.5 — Def - Rank Signature Definiteness and Parity** (Def. 5.1.13, p. 135). As in conventions; $\mathrm{sign}(X) := \mathrm{sign}(Q_X)$.
- **D5.1.6 — Def - E8 Form** (Ex. 5.1.17, p. 137). The form on $\mathbb Z^8$ given by matrix (5.3).
- **D5.1.7 — Def - Homogeneous Coordinates** (Ex. 5.1.18, p. 137). $[z_0:\dots:z_n]$ := class of $(z_0,\dots,z_n)\in S^{2n+1}$.
- **D5.1.8 — Def - K3 Surface** (Ex. 5.1.18, p. 137). The quartic $\{z_0^4+z_1^4+z_2^4+z_3^4 = 0\}\subset\mathbb{CP}^3$ (also "Kummer surface"); well-defined since the equation is homogeneous.

### Theorems
- **T5.1.1 — Thm - Every Class in H_2 Is Represented by an Embedded Surface** (Steps 1–4 and Rem. 5.1.1, pp. 131–133). Every $\alpha\in H_2(X;\mathbb Z)$ is represented by an embedding $f: S\to X$ of a compact connected oriented surface $S$. `Proof in source: sketch in four steps.` (1) Hurewicz: $X$ simply connected ⇒ $\pi_2(X,x)\cong H_2(X;\mathbb Z)$, so $\alpha = f_*[S^2]$ for a continuous $f$. (2) Smoothing by mollifiers: a homotopy $F$ with $F(\cdot,t)$ smooth for $t>0$. (3) Transversality (Thom): deform $f$ to a transversal immersion with finitely many double points. (4) Removal of double points: at $x_i$ choose a chart $\Phi: U(x_i)\to\mathbb R^4 = \mathbb C^2$ with $f(U(p_i)) = \mathbb R^2\times0$, $f(U(q_i)) = 0\times\mathbb R^2$; connect the two Hopf circles $S^1_1 = (\mathbb C\times0)\cap S^3$, $S^1_2 = (0\times\mathbb C)\cap S^3$ by a cylinder $Z$; remove $f^{-1}(\Phi^{-1}(B(0,1)))$ from $S^2$ and attach a handle, extending $f$ over the handle along the cylinder, giving $\tilde f: S^2\#T^2\to X$; repeating gives $\tilde f: \tilde S\to X$ with $N$ handles. To see $[\tilde f] = [f]$: fill $\tilde S$ to a handlebody $\tilde W$, remove a small ball to get $W$ with $\partial W = S^2\sqcup\overline{S^2}$... (source: $\partial W = S^2\sqcup S^2(\varrho)$ with reversed orientation), extend to $F: W\to X$ (constant along radial lines outside the modification; over the solid handle repeat the attaching for circles $S^3(r)$ so the nerve of the handle maps to $x_i$); then $F|_{\partial W} = f\sqcup\tilde f$ and Rem. 4.3.14 gives $[f] = [\tilde f]$. Gaps: everything is sketched with figures; the orientation bookkeeping of $\partial W$ is only indicated.
- **T5.1.2 — Thm - Intersection Form Is Well-Defined Bilinear and Symmetric** (Rem. 5.1.3, p. 133). `Proof in source: omitted (stated).`
- **T5.1.3 — Thm - Intersection Form of the Product of Two 2-Spheres** (Ex. 5.1.4, p. 133). With $S_1 := S^2\times\{p_2\}$, $S_2 := \{p_1\}\times S^2$: $S_1\cdot S_2 = 1$; $[S_1] = [S^2\times\{p_2'\}]$ since $S^2\times\{p_2\}\sqcup S^2\times\{p_2'\} = \partial(S^2\times c)$ for a path $c$; so $Q(S_1,S_1) = S_1\cdot S_1' = 0$, likewise for $S_2$; $Q_{S^2\times S^2} = \begin{pmatrix}0&1\\1&0\end{pmatrix}$. `Proof in source: full (modulo Rem. 4.3.14).`
- **T5.1.4 — Thm - Intersection Form of the Complex Projective Plane** (Ex. 5.1.5, pp. 133–134). $H_2(\mathbb{CP}^2;\mathbb Z)\cong\mathbb Z$ generated by $[\mathbb{CP}^1]$; two distinct complex-linear embeddings $j_1,j_2: \mathbb C^2\hookrightarrow\mathbb C^3$ induce homotopic embeddings $\iota_\nu: \mathbb{CP}^1\hookrightarrow\mathbb{CP}^2$ with $\mathbb{CP}^1_1\cap\mathbb{CP}^1_2 = \{\ell_0\}$, $\ell_0 = j_1(\mathbb C^2)\cap j_2(\mathbb C^2)$, and $\varepsilon(\ell_0) = +1$ for the complex orientations; $Q_{\mathbb{CP}^2} = (1)$. `Proof in source: full (the sign $\varepsilon = +1$ from complex orientations asserted).`
- **T5.1.5 — Thm - Orientation Reversal Negates the Intersection Form** (Rem. 5.1.6, p. 134). $Q_{\overline X} = -Q_X$. `Proof in source: omitted (immediate).`
- **T5.1.6 — Thm - Intersection Form of a Connected Sum** (Rem. 5.1.7, p. 134). $H_2(X_1;\mathbb Z)\oplus H_2(X_2;\mathbb Z)\cong H_2(\dot X_1)\oplus H_2(\dot X_2)\cong H_2(X_1\#X_2;\mathbb Z)$ and $Q_{X_1\#X_2} = Q_{X_1}\oplus Q_{X_2}$ (block diagonal), since representatives can be taken inside $\dot X_1$, $\dot X_2$ and intersections are independent. `Proof in source: sketch.`
- **T5.1.7 — Thm - Intersection Form of Connected Sums of Projective Planes** (Ex. 5.1.8, p. 134). $Q_{k\mathbb{CP}^2\#l\overline{\mathbb{CP}^2}} = \mathrm{diag}(1^{(k)},(-1)^{(l)})$. `Proof in source: full (from T5.1.4–T5.1.6).`
- **T5.1.8 — Thm - Torsion Is Killed by a Bilinear Form** (Rem. 5.1.9, p. 134). For $Q: H\times H\to\mathbb Z$ symmetric bilinear on a finitely generated $\mathbb Z$-module and $a$ torsion ($ka = 0$): $kQ(a,b) = Q(ka,b) = 0$ so $Q(a,b) = 0$; $Q$ descends to $H/\mathrm{Torsion}$. `Proof in source: full.`
- **T5.1.9 — Thm - Unimodularity Is Basis-Independent** (Rem. 5.1.11, p. 135). If (5.1) holds for one basis it holds for all: $(f_j) = (e_i)A$ with $A\in GL(r;\mathbb Z)$, $\det A = \pm1$, $(Q(e_i,e_j)) = A^t(Q(f_k,f_l))A$. `Proof in source: full.`
- **T5.1.10 — Thm - Intersection Form Is Unimodular** (Rem. 5.1.12, p. 135). For $X$ as above, $Q_X$ is unimodular (Poincaré duality). `Proof in source: omitted/cited (Poincaré duality).`
- **T5.1.11 — Thm - Even Parity Is Detected by Diagonal Entries** (Rem. 5.1.14, pp. 135–136). $Q$ has even parity iff for any (equivalently some) basis all diagonal entries $Q(e_i,e_i)$ are even: $Q(a,a) = \sum_{i,j}Q_{ij}a_ia_j = 2\sum_{i<j}Q_{ij}a_ia_j + \sum_iQ_{ii}a_i^2$. `Proof in source: full.`
- **T5.1.12 — Thm - Direct Sums of Forms** (Rem. 5.1.16, p. 136). (1) $Q_1\oplus Q_2$ unimodular iff both are; (2) $\mathrm{sign}(Q_1\oplus Q_2) = \mathrm{sign}Q_1 + \mathrm{sign}Q_2$, hence (5.2) $\mathrm{sign}(X_1\#X_2) = \mathrm{sign}X_1 + \mathrm{sign}X_2$; (3) $Q_1\oplus Q_2$ positive (negative) definite iff both are. `Proof in source: omitted (stated).`
- **T5.1.13 — Thm - K3 Is Simply Connected with the Stated Intersection Form** (Ex. 5.1.18, p. 137). By the Lefschetz hyperplane theorem, $\iota: K3\hookrightarrow\mathbb{CP}^3$ induces isomorphisms $\pi_k(K3)\to\pi_k(\mathbb{CP}^3) = 0$ for $k = 0,1$, so $K3$ is simply connected; $Q_{K3} = -2E_8\oplus3\begin{pmatrix}0&1\\1&0\end{pmatrix}$, even, indefinite, signature $-16$. `Proof in source: omitted/cited (Lefschetz; "One can show" for $Q_{K3}$).`
- **T5.1.14 — Thm - Even Intersection Form Is Equivalent to Spin** (Rem. 5.1.19, p. 137). For $X$ simply connected compact oriented differentiable: $Q_X$ even iff $X$ has a spin structure; then spinors and the Dirac operator are defined. `Proof in source: omitted.`
- **T5.1.15 — Thm - Rochlin's Theorem** (Thm. 5.1.20, pp. 137–138). Let $X$ be a simply connected, compact, oriented differentiable 4-manifold with $Q_X$ of even parity. Then $\mathrm{sign}(X)\in16\mathbb Z$. `Proof in source: sketch.` Strategy: Atiyah–Singer gives $\mathrm{ind}(D^+) = \tfrac18\mathrm{sign}(X)$, so $\mathrm{sign}(X)\in8\mathbb Z$; in dimension 4 the spinor bundle has a quaternionic structure $J$ commuting with $D$, so $\ker D^\pm$ are quaternionic vector spaces, hence even-dimensional (over $\mathbb C$), so $\mathrm{ind}(D^+)\in2\mathbb Z$ and $\mathrm{sign}(X) = 8\,\mathrm{ind}(D^+)\in16\mathbb Z$.

### Examples
- **E5.1.1** (Ex. 5.1.4) $Q_{S^2\times S^2} = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ ("hyperbolic form").
- **E5.1.2** (Ex. 5.1.5) $Q_{\mathbb{CP}^2} = (1)$.
- **E5.1.3** (Ex. 5.1.8) $k\mathbb{CP}^2\#l\overline{\mathbb{CP}^2}$.
- **E5.1.4** (Ex. 5.1.15, p. 136) $Q_{S^2\times S^2}$: even, indefinite, signature 0. $Q_{\mathbb{CP}^2}$: odd, positive definite, signature 1. $Q_{\mathbb{CP}^2\#\overline{\mathbb{CP}^2}} = \mathrm{diag}(1,-1)$: odd, indefinite, signature 0. Over $\mathbb Q$/$\mathbb R$ the matrices $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and $\mathrm{diag}(1,-1)$ are equivalent but over $\mathbb Z$ they are not (different parity).
- **E5.1.5** (Ex. 5.1.17) $E_8$.
- **E5.1.6** (Ex. 5.1.18) $K3$.
- **E5.1.7** (Ex. 5.1.21, p. 138) Table: $S^4$: sign 0, even; $S^2\times S^2$: 0, even; $\mathbb{CP}^2$: 1, odd; $k\mathbb{CP}^2\#l\overline{\mathbb{CP}^2}$: $k-l$, odd; $K3$: $-16$, even.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R5.1.1** (Steps 1–4, pp. 131–132) The representation of $H_2$ classes by embedded surfaces (T5.1.1) — with the handle-attachment and the cobordism $W$ argument.
- **R5.1.2** (Rem. 5.1.9) Why torsion can be ignored and how $Q$ descends to $H/\mathrm{Torsion}$ in general.
- **R5.1.3** (Ex. 5.1.15 last sentence) Parity distinguishes $\mathbb Z$-equivalence classes that are $\mathbb Q$-equivalent.

### External results imported without proof
- **I5.1.1** Hurewicz theorem for $\pi_2$ of a simply connected space (Step 1).
- **I5.1.2** Smoothing of continuous maps by mollifiers (Step 2).
- **I5.1.3** Thom transversality: deformation to a transversal immersion with finitely many double points (Step 3).
- **I5.1.4** Poincaré duality: $Q_X$ unimodular (Rem. 5.1.12); well-definedness of $Q_X$ (Rem. 5.1.3).
- **I5.1.5** Lefschetz hyperplane theorem (Ex. 5.1.18).
- **I5.1.6** $Q_{K3} = -2E_8\oplus3H$ (Ex. 5.1.18).
- **I5.1.7** Even intersection form ⇔ spin structure (Rem. 5.1.19).
- **I5.1.8** Atiyah–Singer index theorem in the form $\mathrm{ind}(D^+) = \tfrac18\mathrm{sign}(X)$ for the Dirac operator on a spin 4-manifold (Thm. 5.1.20).
- **I5.1.9** Quaternionic structure on 4-dimensional spinors commuting with $D$ (Thm. 5.1.20).
- **I5.1.10** Diagonalisability of symmetric forms over $\mathbb Q$/$\mathbb R$ and Sylvester's law (Def. 5.1.13).

---

## 5.2 Classification results

`PDF pages: 138–143`

### Standing conventions and notation
- **Standing hypothesis (§5.2):** $X$ a simply connected, compact, oriented **topological** 4-manifold; $Q$ a symmetric bilinear form on a $\mathbb Z$-module $H$ of finite rank.
- **Self-linking number** of an embedding $f: \bar D^2\times S^1\to S^3$: $\mathrm{lk}(f,f) := \mathrm{lk}(f(0,\cdot),f(1,\cdot))$ (linking number of the core with a parallel boundary curve); **linking number** of two such with disjoint images: $\mathrm{lk}(f_1,f_2) := \mathrm{lk}(f_1(0,\cdot),f_2(0,\cdot))$; **linking matrix** $(\mathrm{lk}(f_i,f_j))_{i,j}$.
- Handle gluing: $\bar B^4\cup_{f_i}\bigcup_i\bar D^2\times\bar D^2$ along $\bar D^2\times\partial\bar D^2$.
- $M_{E_8}$ := the simply connected compact topological 4-manifold with $Q = E_8$ (Freedman); $*\mathbb{CP}^2$ := fake $\mathbb{CP}^2$.
- **Serre normal forms:** odd: $A^{odd}_{k,l} := \mathrm{diag}(1^{(k)},(-1)^{(l)})$, $k,l\ge1$, $\mathrm{rk} = k+l$, $\mathrm{sign} = k-l$; even: $A^{even}_{\pm k,l} := \pm kE_8\oplus l\begin{pmatrix}0&1\\1&0\end{pmatrix}$.
- **Characteristic element** $w\in H$: $Q(x,x)\equiv Q(w,x)\pmod2$ for all $x$; $\bar H := H/2H$ (source: $H/2\mathbb Z$), $\bar Q$ the induced $\mathbb Z/2$-form.
- $\mathcal Q_{8k}$ := isomorphism classes of unimodular positive definite even forms of rank $8k$; Bernoulli numbers via $\frac{x}{e^x-1} = 1 - \frac x2 - \sum_{j\ge1}\frac{(-1)^jB_j}{(2j)!}x^{2j}$ (so $B_1 = \tfrac16$, $B_2 = \tfrac1{30},\dots$ in the source's convention).
- **Minkowski–Siegel mass formula:** $\sum_{Q\in\mathcal Q_{8k}}\frac1{\#\mathrm{Aut}(Q)} = 2^{1-8k}\frac{B_{2k}}{(4k)!}\prod_{j=1}^{4k-1}B_j =: a_{8k}$.

### Definitions
- **D5.2.1 — Def - Self-Linking Number Linking Number and Linking Matrix** (proof of Thm. 5.2.3(a), pp. 139–140). As in conventions.
- **D5.2.2 — Def - Fake Complex Projective Plane** (Ex. 5.2.4, p. 140). $*\mathbb{CP}^2$ := the topological 4-manifold obtained by Freedman's construction from the trefoil knot with self-linking number 1 (vs. $\mathbb{CP}^2$ from the unknot).
- **D5.2.3 — Def - The E8 Manifold** (Rem. 5.2.5, p. 140). $M_{E_8}$ := the simply connected compact topological 4-manifold with $Q_{M_{E_8}}\cong E_8$.
- **D5.2.4 — Def - Characteristic Element and Characteristic Surface** (Def. 5.2.9, p. 142). $w\in H$ with $Q(x,x)\equiv Q(w,x)\pmod 2$ for all $x\in H$; for $H = H_2(X;\mathbb Z)$, a surface $S\subset X$ representing a characteristic element is a *characteristic surface*.
- **D5.2.5 — Def - Bernoulli Numbers** (Rem. 5.2.12, p. 143). Via the generating function above.
- **D5.2.6 — Def - Isomorphism Classes of Even Definite Unimodular Forms** (Rem. 5.2.12, p. 143). $\mathcal Q_{8k}$.

### Theorems
- **T5.2.1 — Thm - Intersection Form Is a Homotopy Invariant of Topological 4-Manifolds** (Rem. 5.2.1, p. 138). $Q_X$ can be defined homologically without a differentiable structure (Poincaré duality), and $X_1\simeq X_2$ ⇒ $Q_{X_1}\cong Q_{X_2}$. `Proof in source: omitted.`
- **T5.2.2 — Thm - Whitehead's Theorem** (Thm. 5.2.2, p. 138). For simply connected compact oriented topological 4-manifolds $X_1,X_2$: $X_1\simeq X_2$ iff $Q_{X_1}\cong Q_{X_2}$. `Proof in source: omitted/cited (Whitehead).`
- **T5.2.3 — Thm - Freedman's Theorem** (Thm. 5.2.3, p. 139). For any unimodular symmetric bilinear form $Q$ on a finite-rank $\mathbb Z$-module there is a simply connected compact oriented topological 4-manifold $X$ with $Q_X\cong Q$. If $Q$ is even, $X$ is unique up to homeomorphism; if $Q$ is odd there are exactly two such $X$ up to homeomorphism. `Proof in source: sketch of existence only.` Strategy: (a) define linking numbers; (b) choose $f_1,\dots,f_r: \bar D^2\times S^1\to S^3$ with disjoint images and linking matrix $Q$; glue $r$ copies of $\bar D^2\times\bar D^2$ to $\bar B^4$ along $\bar D^2\times\partial\bar D^2$ via the $f_i$ to get a compact $X_1$ with boundary; (c) by a careful study of $\partial X_1$ find a contractible $X_2$ with $\partial X_2\cong\partial X_1$; $X := X_1\cup_\partial X_2$ is simply connected compact oriented with $Q_X\cong Q$ since $X_2$ is contractible. Gaps: (c) is the deep part (Freedman's contractible manifolds), entirely omitted; uniqueness omitted.
- **T5.2.4 — Thm - The E8 Manifold Is Not Smoothable** (Rem. 5.2.5, p. 140). $\mathrm{sign}(M_{E_8}) = 8$; if $M_{E_8}$ were differentiable this would contradict Rochlin (even form ⇒ signature in $16\mathbb Z$). `Proof in source: full (from Rochlin + Freedman).`
- **T5.2.5 — Thm - Low-Dimensional Manifolds Are Uniquely Smoothable** (Rem. 5.2.6, p. 140). For $k\le3$ any topological $k$-manifold carries a differentiable structure, unique up to diffeomorphism. `Proof in source: omitted/cited.`
- **T5.2.6 — Thm - Serre's Classification of Indefinite Unimodular Forms** (Thm. 5.2.7, p. 141). For indefinite unimodular symmetric bilinear forms $Q_1,Q_2$ on free $\mathbb Z$-modules of finite rank: $Q_1\cong Q_2$ iff $\mathrm{rk}Q_1 = \mathrm{rk}Q_2$, $\mathrm{sign}Q_1 = \mathrm{sign}Q_2$, and same parity. Odd forms are represented by $A^{odd}_{k,l}$ ($k,l\ge1$); even forms by $A^{even}_{\pm k,l} = \pm kE_8\oplus lH$. `Proof in source: omitted/cited (Serre).`
- **T5.2.7 — Thm - Existence of Characteristic Elements** (Lemma 5.2.8, pp. 141–142). For $Q$ unimodular on free $H$ of finite rank there is $w\in H$ with $Q(x,x)\equiv Q(w,x)\pmod2$ for all $x$. `Proof in source: full.` Strategy: unimodularity ⇒ every linear $f: H\to\mathbb Z$ is $Q(y,\cdot)$ for a unique $y$ (invert the matrix); the same holds for $\bar H = H/2H$ and $\bar Q$; $\bar f(\xi) := \bar Q(\xi,\xi)$ is linear over $\mathbb Z/2$ since $\bar Q(\xi+\eta,\xi+\eta) = \bar f(\xi) + \bar f(\eta) + 2\bar Q(\xi,\eta)$; take $w$ lifting $y_{\bar f}$.
- **T5.2.8 — Thm - Van der Blij's Lemma** (Lemma 5.2.10, p. 142). For $Q$ unimodular on free $H$ of finite rank and $w$ characteristic: $\mathrm{sign}(Q)\equiv Q(w,w)\pmod8$. `Proof in source: omitted/cited.`
- **T5.2.9 — Thm - Even Unimodular Forms Have Signature Divisible by 8** (Rem. 5.2.11, pp. 142–143). If $Q$ is even then $w = 0$ is characteristic, so $\mathrm{sign}Q\equiv0\pmod8$; weaker than Rochlin (8 not 16) but applies to topological manifolds. If $Q$ is positive definite and even, $\mathrm{rk}Q = \mathrm{sign}Q\in8\mathbb Z$. `Proof in source: full (from van der Blij).`
- **T5.2.10 — Thm - Lower Bound on the Number of Even Definite Forms** (Cor. 5.2.13, p. 143). $\#\mathcal Q_{8k}\ge a_{8k} := 2^{1-8k}\frac{B_{2k}}{(4k)!}\prod_{j=1}^{4k-1}B_j$ since $\#\mathrm{Aut}(Q)\ge1$. Table: $k=1$: $\#\mathcal Q_8 = 1$ ($E_8$), $a_8\approx1.43\cdot10^{-9}$; $k=2$: $2$ ($E_8\oplus E_8$, $\Gamma_{16}$), $a_{16}\approx2.48\cdot10^{-18}$; $k=3$: $24$ (Niemeier 1968; source: "Niemeyer"), $a_{24}\approx7.93\cdot10^{-15}$; $k=4$: unknown, $a_{32}\approx4.03\cdot10^7$; $k=5$: unknown, $a_{40}\approx4.39\cdot10^{51}$. `Proof in source: full (from the mass formula).`

### Examples
- **E5.2.1** (proof of 5.2.3(a), p. 139, figure) Three embeddings $f_1,f_2,f_3$ of a solid torus with $\mathrm{lk}(f_1,f_1) = 0$, $\mathrm{lk}(f_2,f_2) = 1$, $\mathrm{lk}(f_3,f_3) = 4$.
- **E5.2.2** (Ex. 5.2.4, p. 140) Realising $Q = (1)$: the unknot gives $\mathbb{CP}^2$, the trefoil gives the fake $*\mathbb{CP}^2$ — the two manifolds of Freedman's odd case.
- **E5.2.3** (Rem. 5.2.5) $M_{E_8}$ — a non-smoothable topological 4-manifold.
- **E5.2.4** (Cor. 5.2.13 table) Counts of even definite forms.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R5.2.1** (p. 141) "What about definite intersection forms? So far, the classification is unknown ... there are huge numbers of them!" — motivation for the mass formula and for Donaldson's theorem.
- **R5.2.2** (Rem. 5.2.12) The Minkowski–Siegel mass formula as a quantitative statement of the difficulty.

### External results imported without proof
- **I5.2.1** Homological definition and homotopy invariance of $Q_X$ (Rem. 5.2.1).
- **I5.2.2** Whitehead's theorem (Thm. 5.2.2).
- **I5.2.3** Freedman's theorem (Thm. 5.2.3), including existence of contractible 4-manifolds with prescribed homology-sphere boundary, and the uniqueness statements.
- **I5.2.4** Uniqueness of smooth structures in dimensions $\le3$ (Rem. 5.2.6; Moise).
- **I5.2.5** Serre's classification of indefinite unimodular forms (Thm. 5.2.7).
- **I5.2.6** Van der Blij's lemma (Lemma 5.2.10).
- **I5.2.7** Minkowski–Siegel mass formula; Niemeier's classification of rank-24 even unimodular lattices; the values in the table (Rem. 5.2.12, Cor. 5.2.13).

---

## 5.3 Donaldson's theorem

`PDF pages: 144–150`

### Standing conventions and notation
- $X$ a simply connected compact oriented differentiable 4-manifold with positive definite $Q_X$; $P\to X$ the $SU(2)$-principal bundle with $\int_Xc_2(P) = -1$ (fn. 1: $SU(2)$-bundles are classified by $p_1$ and $H^4_{dR}(X)\cong\mathbb R$, so $P$ is unique up to isomorphism).
- $\mathcal A(P) := \{\omega\in\mathcal C(P)\mid\bar\Omega\in\Omega^2_+(M;P\times_{\mathrm{Ad}}\mathfrak{su}(2))\}$ = $SU(2)$-instantons (self-dual); **moduli space** $\mathcal M := \mathcal A(P)/\mathcal G(P)$.
- Curvature decomposition $\bar\Omega = \bar\Omega^+ + \bar\Omega^-$; $\int_X|\bar\Omega_k|^2 = \int|\bar\Omega^+_k|^2 + |\bar\Omega^-_k|^2$; $-8\pi^2\int_Xc_2(P) = \int_X(|\bar\Omega^+|^2 - |\bar\Omega^-|^2)\mathrm{dvol}$; for self-dual $\omega_k$: $\int_X|\bar\Omega_k|^2\mathrm{dvol} = 8\pi^2$.
- $\mathcal M_c := \mathcal M\sqcup X$ compactified moduli space (Uhlenbeck), topologised so that a divergent sequence $[\omega_k]$ converges to the concentration point $x\in X$; $\mathcal M'$ := $\mathcal M_c$ with cone neighbourhoods of the singular points cut off; $\partial\mathcal M' = X\sqcup\bigsqcup^{n_+}\mathbb{CP}^2\sqcup\bigsqcup^{n_-}\overline{\mathbb{CP}^2}$, $n_++n_- = n$ (source writes $n_+-n_- = n$, a typo).
- **Integral de Rham cohomology:** $H^2_{dR}(X;\mathbb Z) := \{[\alpha]\in H^2_{dR}(X;\mathbb R)\mid\int_c\alpha\in\mathbb Z\ \forall c\in Z_{2,smooth}(X;\mathbb Z)\}$; $Q_X([\alpha],[\beta]) := \int_X\alpha\wedge\beta$ (fn. 2: smooth singular cycles compute the same homology).
- For $\alpha\in H^2_{dR}(X;\mathbb Z)$ with $Q_X(\alpha,\alpha) = 1$: $L\to X$ the $U(1)$-bundle with $c_1(L) = \alpha$ (fn. 3: $U(1)$-bundles classified by $c_1$); total Chern class $c(L\oplus L^*) = c(L)c(L^*) = (1+c_1(L))(1-c_1(L)) = 1 - c_1(L)^2 = 1 + c_2(P)$; splitting $P\cong L\oplus L^*$; **reducible** self-dual connections ↔ singular points; $H^2_{dR}(X;\mathbb Z)\cong\mathbb Z\alpha\oplus\alpha^\perp$, $\beta\mapsto Q_X(\beta,\alpha)\alpha\oplus(\beta - Q_X(\beta,\alpha)\alpha)$.
- $n(Q) := \tfrac12\#\{\alpha\in H^2_{dR}(X;\mathbb Z)\mid Q(\alpha,\alpha) = 1\}$ (number of singular points); $n(Q)\le\mathrm{rk}(Q)$ with equality iff $Q\cong\mathrm{diag}(1,\dots,1)$.
- Exotic $\mathbb R^4$ notation: $K3\approx2M_{E_8}\#3(S^2\times S^2)$; $\Sigma\subset K3$ topologically embedded 3-sphere; $X_1\cong2\overline{M_{E_8}}\setminus B^4$ (source: $2\overline{M}_{E_8} - B^4$), $X_2\cong3(S^2\times S^2)\setminus B^4$; $j: X_2\hookrightarrow3(S^2\times S^2)$ smooth; $A := B'\setminus\bar B^4$; $V := 3(S^2\times S^2)\setminus j(X_2\setminus A)$; $K := 3(S^2\times S^2)\setminus j(X_2)$ compact.
- $\tfrac{11}8$-conjecture: $b_2(X)\ge\tfrac{11}8\mathrm{sign}(X)$ for even $Q_X$ (presumably $|\mathrm{sign}|$); Furuta: $b_2(X)\ge\tfrac{10}8\mathrm{sign}(X) + 2$.

### Definitions
- **D5.3.1 — Def - Instanton Moduli Space** (proof of Thm. 5.3.1(a), p. 146). $\mathcal A(P)$ and $\mathcal M := \mathcal A(P)/\mathcal G(P)$ as above.
- **D5.3.2 — Def - Compactified Moduli Space** (proof (b), p. 147). $\mathcal M_c := \mathcal M\sqcup X$ with the Uhlenbeck topology; $\mathcal M'$ the truncation.
- **D5.3.3 — Def - Integral de Rham Cohomology and Smooth Singular Cycles** (proof (c) and fn. 2, p. 148). As above; $Z_{2,smooth}(X;\mathbb Z)$ spanned by $\sigma: \Delta^2\to X$ smooth in the interior with all derivatives extending continuously.
- **D5.3.4 — Def - Reducible Self-Dual Connection** (proof (d), p. 149). A self-dual connection on $P\cong L\oplus L^*$ induced from a self-dual connection on the $U(1)$-bundle $L$.
- **D5.3.5 — Def - Counting Function for Singular Points** (proof (d), p. 149). $n(Q) := \tfrac12\#\{\alpha\mid Q(\alpha,\alpha) = 1\}$.
- **D5.3.6 — Def - Exotic R4** (Ex. 5.3.3, p. 144). A differentiable manifold homeomorphic but not diffeomorphic to standard $\mathbb R^4$ ("fake $\mathbb R^4$").

### Theorems
- **T5.3.1 — Thm - Donaldson's Theorem** (Thm. 5.3.1, p. 144). Let $X$ be a simply connected compact oriented differentiable 4-manifold with positive definite intersection form $Q_X$. Then over $\mathbb Z$, $Q_X\cong\mathrm{diag}(1,\dots,1)$. `Proof in source: sketch (pp. 146–149).` Strategy: (a) Take the $SU(2)$-bundle $P$ with $\int c_2(P) = -1$ and the moduli space $\mathcal M$ of self-dual connections mod gauge. Facts: (a') $\mathcal M$ is a 5-manifold with finitely many singular points $p_1,\dots,p_n$; (b') each $p_i$ has a neighbourhood homeomorphic to a cone on $\mathbb{CP}^2$; (c') every divergent sequence $[\omega_k]$ has a subsequence whose curvature concentrates at a point $x\in X$: $\int_{X\setminus B_r(x)}|\bar\Omega_k|^2\to0$ for all $r>0$ (and $\int_X|\bar\Omega_k|^2 = 8\pi^2$ by self-duality and $c_2 = -1$). (b) Form $\mathcal M_c = \mathcal M\sqcup X$; cutting off cone neighbourhoods gives a compact 5-manifold $\mathcal M'$ with $\partial\mathcal M' = X\sqcup n_+\mathbb{CP}^2\sqcup n_-\overline{\mathbb{CP}^2}$; cobordism invariance of the signature: $0 = \mathrm{sign}(\partial\mathcal M') = \mathrm{sign}X + n_+ - n_-$, hence $\mathrm{sign}(X) = n_+ - n_-$ (sign as printed; with the source's orientation conventions). (c) Realise $Q_X$ on $H^2_{dR}(X;\mathbb Z)$ by $\int\alpha\wedge\beta$. (d) Each $\alpha$ with $Q_X(\alpha,\alpha) = 1$ gives a $U(1)$-bundle $L$ with $c_1(L) = \alpha$ and $c(L\oplus L^*) = 1 - \alpha^2 = 1 + c_2(P)$, hence a splitting $P\cong L\oplus L^*$ and reducible self-dual connections, which have extra symmetry and produce the singular points; this gives a bijection $\{$singular points$\}\leftrightarrow\{\pm\alpha\mid Q_X(\alpha,\alpha) = 1\}$. (d, second) Each such $\alpha$ splits $H^2_{dR}(X;\mathbb Z) = \mathbb Z\alpha\oplus\alpha^\perp$ with $\mathrm{rk}(Q|_{\alpha^\perp}) = \mathrm{rk}Q - 1$ and $n(Q) = n(Q|_{\alpha^\perp}) + 1$; induction on rank gives $n(Q)\le\mathrm{rk}(Q)$ with equality iff $Q\cong\mathrm{diag}(1,\dots,1)$. Then $\mathrm{rk}Q_X = \mathrm{sign}Q_X = n_+ - n_-\le n_+ + n_- = n(Q_X)\le\mathrm{rk}Q_X$, forcing $n_- = 0$ and $n(Q_X) = \mathrm{rk}Q_X$, so $Q_X\cong\mathrm{diag}(1,\dots,1)$. Gaps: all of (a')–(c') (Freed–Uhlenbeck/Taubes/Uhlenbeck), the cobordism invariance of signature, the classification of $SU(2)$- and $U(1)$-bundles, the Whitney sum formula, the correspondence singular points ↔ reducible connections, and the induction step $n(Q) = n(Q|_{\alpha^\perp}) + 1$ (which as stated ignores classes with $Q(\beta,\beta) = 1$ not in $\mathbb Z\alpha\cup\alpha^\perp$; positive definiteness makes it correct) are imported or asserted.
- **T5.3.2 — Thm - E8 Plus E8 Is Not Smoothable** (Cor. 5.3.2, p. 144). The topological 4-manifold $X$ with $Q_X\cong E_8\oplus E_8$ does not admit a differentiable structure. `Proof in source: full (from Donaldson: $E_8\oplus E_8$ is positive definite but not diagonal).`
- **T5.3.3 — Thm - Existence of an Exotic R4** (Ex. 5.3.3, pp. 144–146). There is a differentiable manifold homeomorphic but not diffeomorphic to $\mathbb R^4$. `Proof in source: sketch.` Strategy: $Q_{K3} = -2E_8\oplus3H$, so by Freedman $K3\approx2M_{E_8}\#3(S^2\times S^2)$ (orientation as printed); hence a topologically embedded $S^3 = \Sigma\subset K3$ splitting $K3 = X_1\cup_\Sigma X_2$ with $X_1\cong2\overline{M_{E_8}}\setminus B^4$, $X_2\cong3(S^2\times S^2)\setminus B^4$; give $X_2$ the smooth structure from $K3$. Casson facts: (1) there is a smooth embedding $j: X_2\hookrightarrow3(S^2\times S^2)$; set $V := 3(S^2\times S^2)\setminus j(X_2\setminus A)$ with $A = B'\setminus\bar B^4$ a collar; (2) $\pi_1(V) = 0$ (Seifert–van Kampen), $H_2(V;\mathbb Z) = 0$ (MV), $V$ has one end $\cong(0,\infty)\times S^3$, hence $V\approx B^4\approx\mathbb R^4$. $K := 3(S^2\times S^2)\setminus j(X_2)\subset V$ is compact. If a smoothly embedded 3-sphere $S\subset V$ surrounded $K$, then (transporting via $j^{-1}$ and the smooth embedding $X_2\hookrightarrow K3$) one gets a smoothly embedded 3-sphere $\Sigma'\subset K3$; cutting $K3$ along $\Sigma'$ and gluing in $\bar B^4$ yields a closed smooth simply connected 4-manifold $Z$ with $Q_Z\cong E_8\oplus E_8$, contradicting Cor. 5.3.2. In standard $\mathbb R^4$ every compact set is surrounded by a smooth 3-sphere (boundary of a large ball), so $V\not\cong_{\text{diffeo}}\mathbb R^4$. Gaps: Casson's embedding theorem and the "one end ⇒ $\mathbb R^4$" fact (Freedman) imported; the passage from $S$ to $\Sigma'$ and the identification of $Q_Z$ are only indicated; signs of $E_8$ vs $-E_8$ are handled loosely.
- **T5.3.4 — Thm - Homeomorphism Classification of Simply Connected Smooth 4-Manifolds** (p. 149). From Freedman, Serre and Donaldson: every simply connected compact orientable differentiable 4-manifold $X$ is homeomorphic to either $m\mathbb{CP}^2\#n\overline{\mathbb{CP}^2}$ or $\pm mM_{E_8}\#n(S^2\times S^2)$ for suitable $m,n\in\mathbb N$. Not all of these are smoothable ($1M_{E_8}\#0(S^2\times S^2)$ is not; $-2M_{E_8}\#3(S^2\times S^2) = K3$ is); which are is open. `Proof in source: sketch (one paragraph).` Gap: the case of definite $Q_X$ uses Donaldson; indefinite uses Serre; the passage from form to manifold uses Freedman's uniqueness (even case) and the fact that for odd forms the smooth manifold must be the non-fake one (not discussed).
- **T5.3.5 — Thm - Consequence of the 11/8-Conjecture** (p. 150). If Conj. 5.3.4 holds, then for $X = mM_{E_8}\#n(S^2\times S^2)$: $b_2 = 8m+2n$, $\mathrm{sign} = 8m$, so $8m+2n\ge11m$ ⇔ $2n\ge3m$; for $m = -2k$, $n\ge-3k$... (source: $n\ge3k$, $l := n-3k$) and $X = kK3\#l(S^2\times S^2)$. `Proof in source: full (arithmetic).` Gap: the sign of $m$ and the inequality direction are garbled in print ($m = -2k$ gives $\mathrm{sign}<0$; the intended statement is $|\mathrm{sign}|$).
- **T5.3.6 — Thm - Furuta's 10/8 Theorem** (Thm. 5.3.5, p. 150). If $X$ is a simply connected compact oriented differentiable 4-manifold with even $Q_X$, then $b_2(X)\ge\tfrac{10}8\mathrm{sign}(X) + 2$. `Proof in source: omitted/cited (Furuta, via Seiberg–Witten theory — a $U(1)$ gauge theory with $U(1)$ gauge fields coupled to $\mathrm{Spin}^{\mathbb C}$ spinor fields).`

### Examples
- **E5.3.1** (Ex. 5.3.3) Exotic $\mathbb R^4$ — see T5.3.3 (with figures pp. 144–146).
- **E5.3.2** (p. 149) $M_{E_8}$ not smoothable; $K3 = -2M_{E_8}\#3(S^2\times S^2)$ smoothable.

### Exercises
- None stated.

### Remarks / load-bearing paragraphs
- **R5.3.1** (fn. 1, p. 146) $SU(2)$-bundles over $X$ are classified by $p_1$ (equivalently $c_2$); $H^4_{dR}(X)\cong\mathbb R$; hence $P$ with $\int c_2 = -1$ is unique.
- **R5.3.2** (p. 147) Energy identity for self-dual connections: $\int_X|\bar\Omega_k|^2 = -8\pi^2\int_Xc_2(P) = 8\pi^2$; curvature concentration (bubbling) picture.
- **R5.3.3** (p. 148, step b) Signature of the boundary of $\mathcal M'$ vanishes ⇒ $\mathrm{sign}X = n_+ - n_-$.
- **R5.3.4** (p. 148, step c, fn. 2) Intersection form on integral de Rham classes via $\int\alpha\wedge\beta$; smooth singular chains compute homology.
- **R5.3.5** (pp. 148–149, step d) Whitney sum formula computation $c(L\oplus L^*) = 1 - c_1(L)^2$, splitting of $P$, reducible connections ↔ singular points.
- **R5.3.6** (p. 149) The counting argument $n(Q)\le\mathrm{rk}Q$ with equality iff diagonal.
- **R5.3.7** (p. 149) Homeomorphism classification list and the open question of which entries are smoothable.
- **R5.3.8** (Conj. 5.3.4 and following, p. 150) The $\tfrac{11}8$-conjecture and its consequence $kK3\#l(S^2\times S^2)$.

### External results imported without proof
- **I5.3.1** Classification of $SU(2)$-principal bundles over a 4-manifold by $p_1$ (or $c_2$); of $U(1)$-bundles by $c_1$ (fns. 1, 3).
- **I5.3.2** Structure of the instanton moduli space for $c_2 = -1$ on a positive definite 4-manifold: 5-dimensional manifold with finitely many cone-on-$\mathbb{CP}^2$ singularities (Freed–Uhlenbeck; Taubes' existence of instantons implicitly for non-emptiness; Uhlenbeck's removable singularities and compactness for (c')).
- **I5.3.3** Uhlenbeck compactness / curvature concentration: divergent sequences bubble at a point with energy $8\pi^2$ (step (c')).
- **I5.3.4** Cobordism invariance of the signature: $\mathrm{sign}(\partial\mathcal M') = 0$ (step (b)).
- **I5.3.5** Whitney sum formula for total Chern classes and $c_1(L^*) = -c_1(L)$ (step (d)).
- **I5.3.6** Reducible self-dual connections correspond to splittings $P = L\oplus L^*$ and to singular points of $\mathcal M$ (step (d)).
- **I5.3.7** Smooth singular chains compute singular homology; de Rham theorem identifying $\int\alpha\wedge\beta$ with $Q_X$ (fn. 2, step (c)).
- **I5.3.8** Freedman's theorem (used for $K3\approx2M_{E_8}\#3(S^2\times S^2)$ and for $V\approx\mathbb R^4$ from the one-end condition).
- **I5.3.9** Casson's theory: smooth embedding $j: X_2\hookrightarrow3(S^2\times S^2)$ (Ex. 5.3.3 fact 1).
- **I5.3.10** Seifert–van Kampen theorem; Mayer–Vietoris for $H_2(V) = 0$ (Ex. 5.3.3 fact 2).
- **I5.3.11** Serre's classification (for T5.3.4).
- **I5.3.12** Furuta's theorem and Seiberg–Witten theory (Thm. 5.3.5).

---

# Appendix A — Index of source-labelled items by number (for cross-reference)

Chapter 1: Def 1.1.1, Ex 1.1.2, Thm 1.1.3, Ex 1.1.4, Ex 1.1.5, Rem 1.1.6, Def 1.1.7, Ex 1.1.8; Def 1.2.1, Ex 1.2.2, Def 1.2.3, Rem 1.2.4, Def 1.2.5, Def 1.2.6, Ex 1.2.7; Def 1.3.1, Rem 1.3.2, Def 1.3.3, Ex 1.3.4, Rem 1.3.5, Ex 1.3.6, Rem 1.3.7, Ex 1.3.8, Rem 1.3.9, Ex 1.3.10, Def 1.3.11, Def 1.3.12, Ex 1.3.13, Ex 1.3.14, Ex 1.3.15, Def 1.3.16, Rem 1.3.17, Ex 1.3.18, Rem 1.3.19; Exercise 1.4.1, Lemma 1.4.2, Def 1.4.3, Lemma 1.4.4, Cor 1.4.5, Cor 1.4.6, Cor 1.4.7, Rem 1.4.8, Lemma 1.4.9, Cor 1.4.10, Rem 1.4.11, Ex 1.4.12, Rem 1.4.13; Def 1.5.1, Rem 1.5.2, Ex 1.5.3, Def 1.5.4, Rem 1.5.5, Ex 1.5.6, Ex 1.5.7, Def 1.5.8, Ex 1.5.9, Ex 1.5.10, Thm 1.5.11, Ex 1.5.12, Def 1.5.13, Rem 1.5.14, Rem 1.5.15, Def 1.5.16, Rem 1.5.17, Ex 1.5.18, Rem 1.5.19, Def 1.5.20, Rem 1.5.21, Def 1.5.22, Thm 1.5.23, Ex 1.5.24, Ex 1.5.25, Def 1.5.26, Rem 1.5.27.

Chapter 2: Def 2.1.1, Rem 2.1.2, Ex 2.1.3, Rem 2.1.4, Ex 2.1.5, Def 2.1.6, Def 2.1.7, Ex 2.1.8, Def 2.1.9, Rem 2.1.10, Def 2.1.11, Ex 2.1.12; Def 2.2.1, Rem 2.2.2, Rem 2.2.3, Ex 2.2.4, Ex 2.2.5, Ex 2.2.6, Def 2.2.7, Rem 2.2.8, Conclusion 2.2.9, Def 2.2.10, Ex 2.2.11, Def 2.2.12, Ex 2.2.13, Rem 2.2.14, Conclusion 2.2.15, Ex 2.2.16, Ex 2.2.17, Rem 2.2.18, Rem 2.2.19; Def 2.3.1, Rem 2.3.2, Ex 2.3.3, Rem 2.3.4, Ex 2.3.5, Ex 2.3.6, Ex 2.3.7, Rem 2.3.8, Rem 2.3.9; Def 2.4.1, Prop 2.4.2, Lemma 2.4.3, Lemma 2.4.4, Prop 2.4.5, Rem 2.4.6, Ex 2.4.7; Def 2.5.1, Lemma 2.5.2, Lemma 2.5.3, Def 2.5.4, Def 2.5.5, Rem 2.5.6, Rem 2.5.7, Rem 2.5.8, Rem 2.5.9, Cor 2.5.10, Ex 2.5.11, Ex 2.5.12, Ex 2.5.13, Ex 2.5.14, Ex 2.5.15; Lemma 2.6.1, Rem 2.6.2, Rem 2.6.3, Def 2.6.4, Rem 2.6.5, Rem 2.6.6, Lemma 2.6.7, Def 2.6.8, Rem 2.6.9; Def 2.7.1, Rem 2.7.2, Def 2.7.3, Rem 2.7.4, Ex 2.7.5, Rem 2.7.6, Rem 2.7.7, Def 2.7.8, Prop 2.7.9.

Chapter 3: Lemma 3.1.1, Rem 3.1.2, Def 3.1.3, Rem 3.1.4, Lemma 3.1.5, Def 3.1.6, Rem 3.1.7, Prop 3.1.8, Rem 3.1.9, Rem 3.1.10, Rem 3.1.11; Rem 3.2.1, Rem 3.2.2 (all other §3.2 content is unlabelled derivation); Def 3.3.1, Rem 3.3.2, Rem 3.3.3, Def 3.3.4, Rem 3.3.5, Rem 3.3.6, Def 3.3.7, Cor 3.3.8, Def 3.3.9, Def 3.3.10, Rem 3.3.11, Rem 3.3.12, Thm 3.3.13.

Chapter 4: Def 4.1.1, Ex 4.1.2, Rem 4.1.3, Ex 4.1.4, Def 4.1.5, Rem 4.1.6, Def 4.1.7, Ex 4.1.8, Rem 4.1.9, Ex 4.1.10, Def 4.1.11, Rem 4.1.12, Def 4.1.13, Rem 4.1.14, Rem 4.1.15, Prop 4.1.16, Rem 4.1.17, Def 4.1.18, Lemma 4.1.19, Cor 4.1.20, Cor 4.1.21, Rem 4.1.22, Rem 4.1.23, Ex 4.1.24, Ex 4.1.25, Rem 4.1.26, Def 4.1.27, Ex 4.1.28, Ex 4.1.29, Ex 4.1.30, Lemma 4.1.31, Cor 4.1.32, Ex 4.1.33, Def 4.1.34, Thm 4.1.35, Ex 4.1.36, Ex 4.1.37; Def 4.2.1, Def 4.2.2, Rem 4.2.3, Def 4.2.4, Ex 4.2.5, Def 4.2.6, Def 4.2.7, Rem 4.2.8, Rem 4.2.9, Rem 4.2.10, Rem 4.2.11, Rem 4.2.12, Ex 4.2.13, Ex 4.2.14, Ex 4.2.15, Ex 4.2.16, Def 4.2.17, Rem 4.2.18, Rem 4.2.19, Ex 4.2.20, Rem 4.2.21, Thm 4.2.22, Rem 4.2.23, Ex 4.2.24, Rem 4.2.25; Def 4.3.1, Ex 4.3.2, Ex 4.3.3, Rem 4.3.4, Def 4.3.5, Rem 4.3.6, Rem 4.3.7, Rem 4.3.8, Rem 4.3.9, Def 4.3.10, Rem 4.3.11, Def 4.3.12, Ex 4.3.13, Rem 4.3.14.

Chapter 5: Rem 5.1.1, Def 5.1.2, Rem 5.1.3, Ex 5.1.4, Ex 5.1.5, Rem 5.1.6, Rem 5.1.7, Ex 5.1.8, Rem 5.1.9, Def 5.1.10, Rem 5.1.11, Rem 5.1.12, Def 5.1.13, Rem 5.1.14, Ex 5.1.15, Rem 5.1.16, Ex 5.1.17, Ex 5.1.18, Rem 5.1.19, Thm 5.1.20, Ex 5.1.21; Rem 5.2.1, Thm 5.2.2, Thm 5.2.3, Ex 5.2.4, Rem 5.2.5, Rem 5.2.6, Thm 5.2.7, Lemma 5.2.8, Def 5.2.9, Lemma 5.2.10, Rem 5.2.11, Rem 5.2.12, Cor 5.2.13; Thm 5.3.1, Cor 5.3.2, Ex 5.3.3, Conj 5.3.4, Thm 5.3.5.

# Appendix B — Source typos and defects noticed during extraction (so writers do not propagate them)

1. p. 8, Ex. 1.1.4.5: "$SL(n;\mathbb R)$" should read $SL(n;\mathbb C)$.
2. p. 10, Def. 1.2.1(ii): "$[v,w] = -[v,w]$" should read $[v,w] = -[w,v]$.
3. p. 15: the matrices labelled $-i\sigma_1,-i\sigma_2$ do not match the standard Pauli labelling (they are a basis of $\mathfrak{su}(2)$ regardless).
4. p. 20, Def. 1.3.16: "$\tilde\lambda: \tilde{\mathfrak g}\to\mathrm{End}(\tilde V)$" — equivalence is meant for two representations of the same $\mathfrak g$.
5. p. 29, Ex. 1.5.9: "$G = U(1)$" for the rotation action of $SO(2)$ on $S^2$.
6. p. 42, Ex. 2.2.4: "$\mathbb{CP}^n$" should read $\mathbb{CP}^{n-1}$ for $S^{2n-1}$.
7. p. 43: "$P\times_\varphi G$" should read $P\times_\varphi H$.
8. p. 49, Ex. 2.2.17: "$g_{12}(z,t) = z/|z| = |z|/z$" — the two expressions differ; the computation gives $z/|z|$.
9. p. 50, Def. 2.3.1(1): "$R_g^* = \mathrm{Ad}_{g^{-1}}\circ\omega$" should read $R_g^*\omega = \mathrm{Ad}_{g^{-1}}\circ\omega$.
10. p. 53, Ex. 2.3.5: the labels "property 1"/"property 2" are swapped relative to Def. 2.3.1.
11. p. 63, Rem. 2.5.8: $\omega' := \phi^*\omega$ with $\phi: P\to P'$ is a form on $P$, not $P'$; intended $(\phi^{-1})^*\omega$ and $s'_\alpha := \phi\circ s_\alpha$.
12. p. 64, Rem. 2.5.9: printed $d\phi(X,Y) = [X,Y](e)$ should be $-[X,Y](e)$ for $d\phi + \tfrac12[\phi,\phi] = 0$ to hold with $[\phi,\phi](X,Y) = 2[X,Y]$.
13. p. 65, Lemma 2.6.1(i): "$c = \tilde c\circ\pi$" should read $c = \pi\circ\tilde c$.
14. p. 67, Rem. 2.6.3: "$\omega_{\tilde c(t)}(\dot s_\alpha(t))$" should be $\omega(\dot{\tilde c}(t))$.
15. p. 84: coefficient of $dt\wedge dy\wedge dz$ in $dF$ printed as "$-\partial_yE_z + \partial_yE_z + \partial_tB_x$"; should be $\partial_yE_z - \partial_zE_y + \partial_tB_x$.
16. p. 85: $L: \mathcal C(P)\to\Omega^4(M;i\mathbb R)$ — $L$ is real-valued.
17. p. 86: "$-B_z\,dz\wedge dt$" in $*F$ should be $+B_z\,dz\wedge dt$ by the star table.
18. p. 88, Rem. 3.2.2: (3.12) called "linear"; it is a second-order ODE, not linear.
19. p. 89: "$\vec v''$" should be $\vec c\,''$.
20. p. 93: "$g' = \lambda\cdot g$" vs. computation with $\lambda^2$.
21. p. 95: "$d*F = J$" vs. Euler–Lagrange equation $d*F + J = 0$ on p. 86.
22. p. 99: "$\partial_Xs$" in $\nabla^\omega_X[s,A]$ should be $\partial_XA$; "$s^*\omega(Y)$" should be $s^*\omega(X)$.
23. p. 108, Def. 4.1.5: "$g\circ f\simeq\mathrm{id}_Y$" should be $\mathrm{id}_X$.
24. p. 122: "$H_0(S^1;R)$" in the $k=1$ MV step should be $H_0(S^{2n-1};R)$.
25. p. 128, Rem. 4.3.9: the claim $H_{n-1}(\dot M)\oplus H_{n-1}(\{p\}) = 0$ is false in general; only $\partial$ being an isomorphism is needed (Poincaré duality).
26. p. 129, Ex. 4.3.13(4): $X_1$ should be $(S^2\setminus\{-p_1\})\times S^2$.
27. p. 133, Def. 5.1.2: "$S_2\cdot S_2$" should be $S_1\cdot S_2$.
28. p. 137, matrix (5.3): the printed $E_8$ matrix has its off-diagonal $1$'s in a pattern (rows 5–8) that does not obviously match the $E_8$ Dynkin diagram; verify against the standard Cartan matrix ($\det = 1$) before use.
29. p. 143: "Niemeyer" should be Niemeier; "Minkowski-Segal" should be Minkowski–Siegel.
30. p. 147: "$n_+ - n_- = n$" should be $n_+ + n_- = n$.
31. p. 150: the $\tfrac{11}8$-conjecture and Furuta's bound are stated with $\mathrm{sign}(X)$ where $|\mathrm{sign}(X)|$ is intended; the consequence "$m = -2k$ ... $n\ge-3k$" is sign-garbled.
