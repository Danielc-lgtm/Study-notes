---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Spin Groups in Dimensions Three and Four via Quaternions"
  - "Thm - Low-Dimensional Clifford Algebras and the Quaternionic Spinor Modules"
  - "Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions"
  - "Thm - Complex Representations of U(1) and SU(2)"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, the [[Def - Quaternions|quaternions]] are $\mathbb{H} = \mathbb{R}\oplus\mathbb{R}i\oplus\mathbb{R}j\oplus\mathbb{R}k$ with $i^2 = j^2 = k^2 = ijk = -1$, conjugation $\overline{a+bi+cj+dk} = a-bi-cj-dk$, norm $|q|^2 = q\bar q = \bar q q$, and imaginary part $\operatorname{Im}\mathbb{H} = \mathbb{R}i\oplus\mathbb{R}j\oplus\mathbb{R}k$; for $x\in\operatorname{Im}\mathbb{H}$ one has $\bar x = -x$ and $x^2 = -|x|^2$. The group of unit quaternions is $Sp(1) = \{q\in\mathbb{H} : |q| = 1\}$, so $\bar q = q^{-1}$ for $q\in Sp(1)$. For $q\in\mathbb{H}$ we write $L_q$ for left multiplication $v\mapsto qv$ on $\mathbb{H}$.

We use the [[Def - Clifford Algebra and Clifford Multiplication|Clifford algebra]] convention of this series, $u\cdot u = -|u|^2$, polarised to $u\cdot v + v\cdot u = -2\langle u,v\rangle$. As on [[Thm - Low-Dimensional Clifford Algebras and the Quaternionic Spinor Modules|the low-dimensional Clifford page]] we identify $\mathbb{R}^4$ with $\mathbb{H}$ by $e_1\mapsto 1$, $e_2\mapsto i$, $e_3\mapsto j$, $e_4\mapsto k$, and $\mathbb{R}^3$ with $\operatorname{Im}\mathbb{H}$ by $e_1\mapsto i$, $e_2\mapsto j$, $e_3\mapsto k$; the orientation of $\mathbb{R}^n$ is the one making $(e_1,\dots,e_n)$ positive. The **spinor modules** are those of that page:

- In dimension three, $\slashed{S} := \mathbb{H}$, with Clifford multiplication $\operatorname{Im}\mathbb{H}\otimes\slashed{S}\to\slashed{S}$, $x\otimes v\mapsto x\cdot v = xv$ (left quaternion multiplication).
- In dimension four, $\slashed{S} := \slashed{S}^{+}\oplus\slashed{S}^{-}$ with $\slashed{S}^{\pm} = \mathbb{H}$, and Clifford multiplication $\mathbb{H}\otimes\slashed{S}\to\slashed{S}$,
$$h\cdot(v_1,v_2) = (h v_2,\,-\bar h v_1) = \begin{pmatrix}0 & h\\ -\bar h & 0\end{pmatrix}\begin{pmatrix}v_1\\ v_2\end{pmatrix} \qquad (v_1\in\slashed{S}^{+},\ v_2\in\slashed{S}^{-}). \tag{112}$$

Each summand $\slashed{S}^{\pm} = \mathbb{H}$ is a **complex** two-dimensional space through the complex structure given by right multiplication by $\bar\imath = -i$ (so the complex scalar $z\in\mathbb{C}$ acts by $v\mapsto v\bar z$, which commutes with every left multiplication $L_q$ by associativity), with the positive-definite Hermitian inner product $\langle v,w\rangle := \pi(\bar v w)$, where $\pi:\mathbb{H}\to\mathbb{C} = \mathbb{R}\oplus\mathbb{R}i$ is the projection along $\mathbb{R}j\oplus\mathbb{R}k$; that this is Hermitian and that Clifford multiplication by a unit vector is unitary are proved on [[Thm - Low-Dimensional Clifford Algebras and the Quaternionic Spinor Modules|the low-dimensional page]]. For a finite-dimensional complex inner-product space $W$ we write $\operatorname{End}_{\mathbb{C}}(W)$ for its complex-linear endomorphisms, $\operatorname{End}_0(W) = \mathfrak{sl}(W)$ for the traceless ones, $\mathfrak{u}(W)$ for the skew-Hermitian ones ($T^{*} = -T$), and $\mathfrak{su}(W) = \operatorname{End}_0(W)\cap\mathfrak{u}(W)$ for the traceless skew-Hermitian ones; here $T^{*}$ is the Hermitian adjoint with respect to $\langle\cdot,\cdot\rangle$. For a real vector space $V$, $V\otimes_{\mathbb{R}}\mathbb{C}$ is its complexification and $\operatorname{Hom}_{\mathbb{C}}(A,B)$ the complex-linear maps between complex spaces $A,B$.

The rotation groups are realised through the double covers of [[Thm - Spin Groups in Dimensions Three and Four via Quaternions|the quaternionic spin page]]: $\alpha:Sp(1)\to SO(3)$, $\alpha(q)x = qx\bar q$ on $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$, realises $Spin(3)\cong Sp(1)$ with $\xi = \alpha$; and $\beta:Sp_+(1)\times Sp_-(1)\to SO(4)$, $\beta(q_+,q_-)h = q_+ h\bar q_-$ on $\mathbb{H}\cong\mathbb{R}^4$, realises $Spin(4)\cong Sp(1)\times Sp(1)$ with $\xi = \beta$. Under these identifications $Sp(1)$ acts on the dimension-three module $\slashed{S}$ by left multiplication, $\slashed{S}^{+}$ is the fundamental representation of $Sp_+(1)$ (left multiplication by $q_+$), and $\slashed{S}^{-}$ that of $Sp_-(1)$ (left multiplication by $q_-$). The self-dual decomposition $\Lambda^2\mathbb{R}^4 = \Lambda^2_+\oplus\Lambda^2_-$ and its orthonormal bases are those of [[Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions|the self-dual decomposition page]]; we use $\Lambda^2\mathbb{R}^4$ and $\Lambda^2(\mathbb{R}^4)^{*}$ interchangeably through the metric identification $e_i\wedge e_j\leftrightarrow e_i^{*}\wedge e_j^{*}$.

> [!warning] Convention: which complex structure and which spinor sign
> The two arbitrary-looking choices — the complex structure is *right* multiplication by $\bar\imath$, and Clifford multiplication in dimension four is $(112)$ rather than its transpose — are fixed once and for all on [[Thm - Low-Dimensional Clifford Algebras and the Quaternionic Spinor Modules|the low-dimensional page]] and are used here without alteration. Replacing $\bar\imath$ by $i$ conjugates the complex structure and changes nothing in any statement below; reversing the orientation of $\mathbb{R}^4$ exchanges $\Lambda^2_+\leftrightarrow\Lambda^2_-$ and $\slashed{S}^{+}\leftrightarrow\slashed{S}^{-}$ simultaneously, so the pairing "$\Lambda^2_\pm$ acts on $\slashed{S}^{\pm}$" is orientation-independent.

---

# Statement

> **Theorem (spinor representations in dimensions three and four).** With the conventions above:
>
> **(i) Dimension three — Haydys equation (111).** The map
> $$\Phi:\operatorname{Im}\mathbb{H}\longrightarrow\operatorname{End}_{\mathbb{C}}(\slashed{S}), \qquad \Phi(x)(v) = x\cdot v = xv,$$
> is an $\mathbb{R}$-linear isomorphism onto $\mathfrak{su}(\slashed{S})$, the traceless skew-Hermitian endomorphisms. Its complexification is an isomorphism of $Sp(1)$-representations
> $$\operatorname{Im}\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\;\xrightarrow{\ \sim\ }\;\operatorname{End}_0(\slashed{S}),$$
> where $Sp(1)$ acts on the left through $\alpha$ (that is, by conjugation of $\operatorname{Im}\mathbb{H}$ and by conjugation of endomorphisms). Equivalently, $\operatorname{Im}\mathbb{H}$ is carried onto the traceless *self-adjoint* (Hermitian) endomorphisms by $x\mapsto -i\,\Phi(x)$.
>
> **(ii) Dimension four — Haydys equation (185).** The map
> $$\gamma:\mathbb{R}^4 = \mathbb{H}\longrightarrow\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{+},\slashed{S}^{-}), \qquad \gamma(v)(\psi) = v\cdot\psi,$$
> is an $\mathbb{R}$-linear injection whose complexification is an isomorphism of $Spin(4)$-representations
> $$\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\;\xrightarrow{\ \sim\ }\;\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{+},\slashed{S}^{-}),$$
> $Spin(4) = Sp_+(1)\times Sp_-(1)$ acting on $\mathbb{R}^4$ through $\beta$. The same holds for $\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{-},\slashed{S}^{+})$, proved by exchanging the two chiral halves in the argument. For every fixed $\psi_0\in\slashed{S}^{+}\setminus\{0\}$ the map $\mathbb{R}^4\to\slashed{S}^{-}$, $v\mapsto v\cdot\psi_0$, is an $\mathbb{R}$-linear isomorphism (and likewise with the chiralities exchanged).
>
> **(iii) Clifford action of two-forms — Haydys equations (186)–(187).** The Clifford action of two-forms
> $$c:\Lambda^2\mathbb{R}^4\longrightarrow\operatorname{End}_{\mathbb{C}}(\slashed{S}^{\pm}), \qquad c(e_i\wedge e_j) = e_i\cdot e_j\cdot\quad(i<j),$$
> extended $\mathbb{R}$-linearly, has kernel exactly $\Lambda^2_\mp\mathbb{R}^4$ on $\slashed{S}^{\pm}$ and takes values in the skew-Hermitian endomorphisms. It induces $Spin(4)$-equivariant isomorphisms
> $$\Lambda^2_+\mathbb{R}^4\;\xrightarrow{\ \sim\ }\;\mathfrak{su}(\slashed{S}^{+}), \qquad \Lambda^2_-\mathbb{R}^4\;\xrightarrow{\ \sim\ }\;\mathfrak{su}(\slashed{S}^{-}),$$
> and, on complexifying the first, $\Lambda^2_+\mathbb{R}^4\otimes_{\mathbb{R}}\mathbb{C}\xrightarrow{\sim}\operatorname{End}_0(\slashed{S}^{+})$ (compare (111)). Consequently $\Lambda^2_+\otimes\mathbb{C}$ and $\Lambda^2_-\otimes\mathbb{C}$ act on $\slashed{S}^{+}$, respectively $\slashed{S}^{-}$, through $\mathfrak{sl}(\slashed{S}^{\pm})$; in particular **every anti-self-dual two-form acts as zero on $\slashed{S}^{+}$**, and every self-dual two-form acts as zero on $\slashed{S}^{-}$.
>
> **(iv) The spin$^{c}$ statements.** All of (ii) and (iii) hold verbatim for $Spin^{c}(4)$ acting through the homomorphisms $\rho_\pm:Spin^{c}(4)\to U(\slashed{S}^{\pm})$ of §8.3: the isomorphism (185) is $Spin^{c}(4)$-equivariant with the central circle $U(1)\subset Spin^{c}(4)$ acting trivially on $\mathbb{H}\otimes\mathbb{C}$, and the isomorphism (187) is $Spin^{c}(4)$-equivariant with $U(1)$ acting trivially on $\mathfrak{su}(\slashed{S}^{+})$.

These identifications are stated by Haydys as equations (111) and (185)–(187) and dismissed as "an elementary exercise in the representation theory"; the proofs below are supplied in full, since the four-manifold gauge theory of chapters IX–XIII rests on them.

---

# Motivation

The Seiberg–Witten equations, and the linear algebra that makes them tractable, live entirely on the two spinor half-representations $\slashed{S}^{+}$ and $\slashed{S}^{-}$ of a four-manifold. Three separate objects have to be transported onto these two-dimensional complex spaces before a single estimate can be written down: a *vector* (so that Clifford multiplication, hence the Dirac operator, has meaning), a *self-dual two-form* (so that the curvature term $F_A^{+}$ of the equations can sit on the same footing as a spinor endomorphism), and the *Lie algebra of the structure group* (so that gauge transformations and the deformation complex can be computed). This theorem is the dictionary that does all three transports at once, and does them concretely: a vector becomes an off-diagonal quaternion matrix, a self-dual two-form becomes left multiplication by an imaginary quaternion, and the Lie algebra $\mathfrak{su}(2)$ becomes exactly the self-dual forms.

The single most consequential line of the theorem is the last one of part (iii): an anti-self-dual two-form annihilates $\slashed{S}^{+}$. Without it, the curvature equation $F_A^{+} = \mu(\psi)$ of Seiberg–Witten theory would be an equation between objects living in different spaces; with it, both sides are sections of $i\Lambda^2_+ \cong i\,\mathfrak{su}(\slashed{S}^{+})$, and the whole apparatus of chiral Weitzenböck formulas, $C^0$ bounds, and the deformation complex becomes available. The reason this vanishing is not a coincidence is the mechanism the theorem exhibits:

> $\mathfrak{so}(4) = \Lambda^2\mathbb{R}^4 = \Lambda^2_+\oplus\Lambda^2_-$, and each summand is the Lie algebra of one of the two $Sp(1)$-factors of $Spin(4)$, acting on its own spinor half and trivially on the other.

Everything on the page is a coordinate proof of that sentence. The reader is assumed to know the quaternions, the Pauli matrices, the definition of a Clifford module, and the self-dual splitting of two-forms in dimension four; the double covers $\alpha,\beta$ and the module $(112)$ are recalled at the point of use.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypotheses fix the dimension, so the operative question is which problems secretly hand one of these three transports.

The first disguised source is **any first-order chiral operator built from a connection on a four-manifold**. A Dirac-type operator $\slashed{D}^{+}_A:\Gamma(\slashed{S}^{+})\to\Gamma(\slashed{S}^{-})$ is, at the level of symbols, Clifford multiplication by the cotangent covector; part (ii) says its symbol at $\xi\ne 0$ is the isomorphism $v\mapsto v\cdot$ restricted to a single spinor, hence an isomorphism $\slashed{S}^{+}_x\to\slashed{S}^{-}_x$. The non-obvious bridge is that ellipticity of $\slashed{D}^{+}_A$ — the statement that its symbol is invertible — is *nothing but* the last clause of part (ii), that $v\mapsto v\cdot\psi_0$ is a bijection for $v$ ranging over $\mathbb{R}^4$ with $\psi_0$ fixed. *Example problem:* show that the twisted Dirac operator on a spin$^{c}$ four-manifold is elliptic by identifying its principal symbol with $\gamma$ of part (iv).

The second disguised source is **a curvature two-form that one wishes to feed to a spinor**. Whenever a computation produces $R\in\Lambda^2 T^{*}M\otimes\operatorname{End}(E)$ and one wants its Clifford image on $\slashed{S}^{+}$ — as in the Weitzenböck and Lichnerowicz formulas — part (iii) says only the self-dual part survives, because the anti-self-dual part lies in the kernel $\Lambda^2_-$. The non-obvious step is that one may replace $R$ by $R^{+}$ *before* Clifford-multiplying, with no error. *Example problem:* derive the chiral Weitzenböck identity $\slashed{D}^{-}_A\slashed{D}^{+}_A = \nabla_A^{*}\nabla_A + \tfrac14 s_g + \tfrac12 F_A^{+}\cdot$ from the full Weitzenböck formula by discarding $F_A^{-}$ on the strength of part (iii).

The third disguised source is **a computation that has produced a traceless Hermitian or skew-Hermitian endomorphism of a two-dimensional complex space**. Any such object is, by parts (i) and (iii), a self-dual form (or an imaginary quaternion), and can be handled with quaternion arithmetic. The non-obvious bridge is that the quadratic map $\mu(\psi) = \psi\psi^{*} - \tfrac12|\psi|^2$, which is manifestly a traceless Hermitian endomorphism, is *therefore* an imaginary self-dual two-form, and can be equated with $F_A^{+}$. *Example problem:* verify that $\mu(\psi)$ lands in $i\Lambda^2_+$ by checking that it is traceless and Hermitian, and reading off the corresponding two-form through (187).

**Targets (Output Amplification).** Combined with other results the theorem does much more than translate.

Combine part (iii) with **the full [[Thm - Weitzenbock Formula for the Dirac Operator|Weitzenböck formula]]** $D^2 = \nabla^{*}\nabla + \mathcal{R}$. Restricting to $\slashed{S}^{+}$ and using that the anti-self-dual part of the curvature acts as zero, the curvature endomorphism collapses to $\tfrac14 s_g + \tfrac12 F_A^{+}\cdot$; the payoff is the chiral Lichnerowicz identity, whose integrated form gives the $C^0$ bound $|\psi|^2\le -\!\min s_g$ on Seiberg–Witten solutions and the vanishing theorem on manifolds of positive scalar curvature. The extra ingredient is the pointwise scalar-curvature computation; the amplification is a global obstruction to solutions.

Combine part (i) with **the classification of [[Thm - Complex Representations of U(1) and SU(2)|complex $SU(2)$-representations]]**. Both $\operatorname{Im}\mathbb{H}\otimes\mathbb{C}$ and $\operatorname{End}_0(\slashed{S})$ are three-dimensional complex $Sp(1)$-representations; the classification says the three-dimensional irreducible representation $\varrho_2\cong(\operatorname{Ad}_{SU(2)})_{\mathbb{C}}$ is unique, so an $Sp(1)$-equivariant injection between them is automatically an isomorphism. The extra ingredient is irreducibility; the payoff is a proof of (111) that needs no dimension count at all, and the identification of the self-dual forms with the complexified adjoint representation used throughout Donaldson and Seiberg–Witten theory.

Combine part (ii) with **the affine structure of the space of connections**. Since $a\mapsto a\cdot$ realises $T^{*}M\otimes i\mathbb{R}$ inside $\operatorname{Hom}(\slashed{S}^{+},\slashed{S}^{-})$, the derivative of the Seiberg–Witten map in the connection direction is Clifford multiplication by the perturbing one-form; combined with the surjectivity clause $v\mapsto v\cdot\psi_0$ (an isomorphism for $\psi_0\ne 0$), this makes the linearised map surjective at irreducible configurations. The extra ingredient is a nonvanishing spinor; the payoff is that the origin is a regular value of the perturbed map, hence the moduli space is a manifold.

---

# Why Is It True

The whole page is powered by a single computation with the module $(112)$. A vector $h\in\mathbb{H} = \mathbb{R}^4$ acts on $\slashed{S} = \slashed{S}^{+}\oplus\slashed{S}^{-}$ by the off-diagonal matrix $\left(\begin{smallmatrix}0 & h\\ -\bar h & 0\end{smallmatrix}\right)$, so an *even* Clifford element — a product $ab$ of two vectors — acts by the diagonal matrix
$$\begin{pmatrix}0 & a\\ -\bar a & 0\end{pmatrix}\begin{pmatrix}0 & b\\ -\bar b & 0\end{pmatrix} = \begin{pmatrix}-a\bar b & 0\\ 0 & -\bar a b\end{pmatrix},$$
that is, left multiplication by $-a\bar b$ on $\slashed{S}^{+}$ and by $-\bar a b$ on $\slashed{S}^{-}$. Every statement on the page is read off this matrix.

**For a two-form,** take $a = e_i$, $b = e_j$: on $\slashed{S}^{+}$ the generator $e_i\wedge e_j$ acts by left multiplication by the imaginary quaternion $-e_i\bar e_j$. Running through the six basis two-forms one finds that the three *self-dual* ones act as $2L_i, 2L_j, 2L_k$ — a basis of the imaginary quaternions, hence of $\mathfrak{su}(2)$ — while the three *anti-self-dual* ones act as $0$, because on $\slashed{S}^{+}$ the two summands of an anti-self-dual form cancel and the two summands of a self-dual form reinforce. On $\slashed{S}^{-}$ the roles are exactly reversed. This is the promised mechanism: the self-dual forms are the imaginary quaternions acting on $\slashed{S}^{+}$ from the left, and imaginary quaternions acting from the left are precisely the Lie algebra of the $Sp_+(1)$-factor.

> **The one-sentence mechanism:** Clifford multiplying twice turns the off-diagonal vector action into a diagonal even action, and in dimension four the diagonal entry that a two-form contributes is $\pm$ its self-dual part on $\slashed{S}^{+}$ and $\mp$ its anti-self-dual part on $\slashed{S}^{-}$, so exactly half of $\Lambda^2 = \mathfrak{so}(4)$ is visible to each spinor half.

**That the images are skew-Hermitian** is because left multiplication by a unit quaternion preserves the Hermitian metric $\langle v,w\rangle = \pi(\bar v w)$ (it multiplies $\bar v w$ on the left and right by $\bar q$ and $q$ with $\bar q q = 1$), so $L_q$ is unitary; a unit imaginary quaternion has $L_x^2 = L_{-1} = -\operatorname{id}$, and a unitary map squaring to $-\operatorname{id}$ is skew-Hermitian. **That the maps are equivariant** is because Clifford multiplication intertwines the spinor action of $Spin(4)$ with the rotation action on $\mathbb{R}^4$ — conjugating a vector by a spin element rotates it — and this propagates to products of vectors, that is, to two-forms.

---

# What Makes This Hard

The genuine subtlety is bookkeeping of the two factors of two. The self-dual basis form $e_1\wedge e_2 + e_3\wedge e_4$ acts as $2L_i$, not $L_i$, so the isomorphism $\Lambda^2_+\cong\mathfrak{su}(\slashed{S}^{+})$ carries an unavoidable scale that must be tracked whenever the induced metrics on the two sides are compared (it is the origin of factors such as the $\tfrac12$ in $F_A^{+}\cdot\psi$). The common error is to conclude that the kernel of the two-form action is $\Lambda^2_-$ *on all of $\slashed{S}$*; it is not — on $\slashed{S}^{-}$ the kernel is $\Lambda^2_+$, and only the chirally-restricted statement is true. A second trap is the passage from a real-linear injection to an isomorphism of complexifications: real-linear injectivity does not by itself give injectivity after tensoring with $\mathbb{C}$, and one must check that $i$ times the real image meets the real image only in zero (equivalently, invoke the uniqueness of the relevant irreducible representation) before the dimension count is allowed to finish the argument.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Compute how an even Clifford element acts on each spinor half by applying $(112)$ twice; this reduces everything to left multiplication by a quaternion. Read off part (i) from left multiplication by imaginary quaternions on $\slashed{S}$ (dimension three); read off part (ii) from the off-diagonal action of vectors and a check that the real image and $i$ times it are independent; read off part (iii) from the six-entry table of self-dual and anti-self-dual basis forms; obtain part (iv) by noting that the central circle acts by scalars and so is invisible to every conjugation and every Hom-space.

**Subgoal decomposition:**

1. **Left multiplication by imaginary quaternions is $\mathfrak{su}(\slashed{S})$.** Show $\Phi(x) = L_x$ is complex-linear, traceless, skew-Hermitian, and that $x\mapsto L_x$ is a real-linear bijection onto $\mathfrak{su}(\slashed{S})$.
   - *Hint:* Complex-linearity is associativity; skew-Hermiticity is "unitary with square $-\operatorname{id}$"; tracelessness is that the two eigenvalues $\pm i|x|$ sum to zero.
   - *Why needed:* It is part (i), and it is the target of the two-form map in part (iii).

2. **Complexify to (111).** Show $\operatorname{End}_0(\slashed{S}) = \mathfrak{su}(\slashed{S})\oplus i\,\mathfrak{su}(\slashed{S})$, so that the complexification of the isomorphism $\operatorname{Im}\mathbb{H}\xrightarrow{\sim}\mathfrak{su}(\slashed{S})$ is an isomorphism onto $\operatorname{End}_0(\slashed{S})$.
   - *Hint:* Any traceless complex matrix $M$ is $\tfrac12(M - M^{*}) + i\cdot\tfrac1{2i}(M + M^{*})$, a sum of a skew-Hermitian and $i$ times a skew-Hermitian, both traceless.
   - *Why needed:* It upgrades the real isomorphism to the stated complex one.

3. **Even elements act diagonally.** Prove that $ab$ acts on $\slashed{S}^{+}$ by $L_{-a\bar b}$ and on $\slashed{S}^{-}$ by $L_{-\bar a b}$.
   - *Hint:* Multiply the two off-diagonal matrices of $(112)$.
   - *Why needed:* It is the engine of parts (ii) and (iii).

4. **The vector map and its complexification.** Show $\gamma(v) = v\cdot$ is a real-linear injection $\mathbb{R}^4\to\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{+},\slashed{S}^{-})$, that its real image $R$ satisfies $R\cap iR = 0$, and conclude the complexification is an isomorphism; deduce the isomorphism $\mathbb{R}^4\to\slashed{S}^{-}$ for fixed $\psi_0\ne 0$.
   - *Hint:* $\gamma(v)$ is left multiplication by $-\bar v$; $R$ is all left multiplications, and $J\circ L_w$ is a left multiplication only when $w = 0$.
   - *Why needed:* It is part (ii).

5. **The six-form table.** Evaluate $c(e_i\wedge e_j)$ on $\slashed{S}^{+}$ for the six pairs, combine them into the self-dual and anti-self-dual bases, and read off the kernel $\Lambda^2_-$ and image $\mathfrak{su}(\slashed{S}^{+})$; do the same on $\slashed{S}^{-}$.
   - *Hint:* Use Subgoal 3 and the bases $e_1\wedge e_2\pm e_3\wedge e_4$, $e_1\wedge e_3\mp e_2\wedge e_4$, $e_1\wedge e_4\pm e_2\wedge e_3$.
   - *Why needed:* It is the computational heart of part (iii).

6. **Equivariance and the spin$^{c}$ upgrade.** Show all maps intertwine the group actions, using $\xi(g)v = gvg^{-1}$; then observe the central $U(1)$ of $Spin^{c}(4)$ acts by scalars on each $\slashed{S}^{\pm}$, hence trivially on every Hom-space and every conjugation-representation.
   - *Hint:* $g(v\cdot\psi) = (\xi(g)v)\cdot(g\psi)$, and conjugation by $g$ sends $ab$ to $(\xi(g)a)(\xi(g)b)$.
   - *Why needed:* It makes the isomorphisms $Spin(4)$- and $Spin^{c}(4)$-equivariant, which is what the applications use.

---

# Lemma Decomposition

> [!note]- Lemma 1: Left multiplication by imaginary quaternions realises $\mathfrak{su}(\slashed{S})$
> **Statement:** For $x\in\operatorname{Im}\mathbb{H}$ the map $L_x:\slashed{S}\to\slashed{S}$, $v\mapsto xv$, is complex-linear (for the complex structure of right multiplication by $\bar\imath$), traceless, and skew-Hermitian for $\langle v,w\rangle = \pi(\bar v w)$. The assignment $x\mapsto L_x$ is a real-linear isomorphism $\operatorname{Im}\mathbb{H}\xrightarrow{\sim}\mathfrak{su}(\slashed{S})$.
>
> **Hint:** Complex-linearity is associativity of quaternion multiplication; unitarity is $\bar q q = 1$; tracelessness is the eigenvalue pair $\pm i|x|$.
>
> **Why needed:** It is part (i) in its real form and the image side of part (iii).
>
> > [!note]- Full proof
> > Fix $x\in\operatorname{Im}\mathbb{H}$, so $\bar x = -x$ and $x^2 = -|x|^2$.
> >
> > **Complex-linearity.** The complex structure is right multiplication by $\bar\imath$, so for $z\in\mathbb{C}$ the scalar action on $v$ is $v\mapsto v\bar z$. By associativity of quaternion multiplication, $L_x(v\bar z) = x(v\bar z) = (xv)\bar z = (L_x v)\bar z$ (associativity), so $L_x$ commutes with the complex scalar action and is complex-linear. Hence $L_x\in\operatorname{End}_{\mathbb{C}}(\slashed{S})$.
> >
> > **Skew-Hermiticity.** First, for $q\in Sp(1)$ and all $v,w\in\slashed{S}$,
> > $$\langle L_q v, L_q w\rangle = \pi(\overline{qv}\,qw) = \pi(\bar v\,\bar q q\,w) = \pi(\bar v w) = \langle v,w\rangle \qquad (\overline{qv} = \bar v\bar q;\ \bar q q = |q|^2 = 1),$$
> > so $L_q$ is unitary. Take $x\ne 0$ and set $q = x/|x|\in Sp(1)$, a unit imaginary quaternion; then $L_q$ is unitary and $L_q^2 = L_{q^2} = L_{-1} = -\operatorname{id}$ (since $q^2 = -|q|^2 = -1$). A unitary map $U$ with $U^2 = -\operatorname{id}$ satisfies $U^{*} = U^{-1} = -U$ (unitarity gives $U^{*} = U^{-1}$; $U^2 = -\operatorname{id}$ gives $U^{-1} = -U$), so $L_q^{*} = -L_q$; scaling, $L_x^{*} = |x| L_q^{*} = -|x| L_q = -L_x$ (real scaling commutes with the adjoint). For $x = 0$ the claim is trivial. Thus $L_x$ is skew-Hermitian.
> >
> > **Tracelessness.** Being skew-Hermitian, $L_x$ is diagonalisable with purely imaginary eigenvalues $\lambda_1,\lambda_2$ (spectral theorem, [[Thm - Complex Spectral Theorem|complex spectral theorem]]). From $L_x^2 = L_{x^2} = -|x|^2\operatorname{id}$ we get $\lambda_k^2 = -|x|^2$, so $\lambda_k = \pm i|x|$ (each root of $\lambda^2 + |x|^2 = 0$). If $\lambda_1 = \lambda_2$ then $L_x = \lambda_1\operatorname{id}$ is a complex scalar; but $L_x$ is not scalar for $x\ne 0$, since it fails to commute with another left multiplication — for $x = i$, $L_i L_j(1) = ij = k$ while $L_j L_i(1) = ji = -k$ (quaternion products), so $L_i L_j\ne L_j L_i$, whereas a scalar commutes with everything. Hence $\lambda_1 = -\lambda_2$ and $\operatorname{tr} L_x = \lambda_1 + \lambda_2 = 0$. Therefore $L_x\in\mathfrak{su}(\slashed{S})$.
> >
> > **Bijection.** The map $x\mapsto L_x$ is real-linear and injective: if $L_x = 0$ then $x = x\cdot 1 = L_x(1) = 0$ (evaluate at $v = 1\in\mathbb{H}$). Its domain $\operatorname{Im}\mathbb{H}$ has real dimension $3$, and its codomain $\mathfrak{su}(\slashed{S}) = \mathfrak{su}(2)$ also has real dimension $3$ (the traceless skew-Hermitian $2\times 2$ complex matrices form a three-real-dimensional space, spanned by $-i\sigma_1,-i\sigma_2,-i\sigma_3$). An injective real-linear map between real vector spaces of equal finite dimension is a bijection (rank–nullity). Hence $x\mapsto L_x$ is an isomorphism $\operatorname{Im}\mathbb{H}\xrightarrow{\sim}\mathfrak{su}(\slashed{S})$.

> [!note]- Lemma 2: The complexification of $\mathfrak{su}(W)$ is $\operatorname{End}_0(W)$
> **Statement:** For a finite-dimensional complex inner-product space $W$, every traceless endomorphism $M\in\operatorname{End}_0(W)$ is uniquely $M = P + iQ$ with $P,Q\in\mathfrak{su}(W)$; equivalently the real-linear map $\mathfrak{su}(W)\otimes_{\mathbb{R}}\mathbb{C}\to\operatorname{End}_0(W)$, $P\otimes z\mapsto zP$, is an isomorphism of complex vector spaces.
>
> **Hint:** Split $M$ into its skew-Hermitian and Hermitian parts; the Hermitian part is $i$ times a skew-Hermitian one.
>
> **Why needed:** It converts the real isomorphism of Lemma 1 (and of part (iii)) into the complex isomorphisms (111) and (187).
>
> > [!note]- Full proof
> > Let $M\in\operatorname{End}_0(W)$, so $\operatorname{tr} M = 0$. Write
> > $$M = \underbrace{\tfrac12\left(M - M^{*}\right)}_{=:P} + \underbrace{\tfrac12\left(M + M^{*}\right)}_{=:H},$$
> > where $M^{*}$ is the Hermitian adjoint. Then $P^{*} = \tfrac12(M^{*} - M) = -P$, so $P$ is skew-Hermitian, and $H^{*} = \tfrac12(M^{*} + M) = H$, so $H$ is Hermitian (both by taking adjoints termwise and using $(M^{*})^{*} = M$). Since the trace is conjugate-symmetric, $\operatorname{tr} M^{*} = \overline{\operatorname{tr} M} = 0$, so $\operatorname{tr} P = 0$ and $\operatorname{tr} H = 0$. Now $Q := -iH$ satisfies $Q^{*} = \overline{(-i)}H^{*} = iH = -Q$ (adjoint conjugates the scalar and fixes $H$), so $Q$ is skew-Hermitian and traceless, and $H = iQ$. Thus $M = P + iQ$ with $P,Q\in\mathfrak{su}(W)$.
> >
> > **Uniqueness.** If $P + iQ = P' + iQ'$ with all four in $\mathfrak{su}(W)$, then $P - P' = i(Q' - Q)$; the left side is skew-Hermitian and the right side is $i$ times skew-Hermitian, i.e. Hermitian. An endomorphism that is both skew-Hermitian and Hermitian satisfies $T = T^{*} = -T$, hence $2T = 0$ and $T = 0$; so $P = P'$ and $Q = Q'$. This is exactly the statement that the real-linear map $\mathfrak{su}(W)\otimes_{\mathbb{R}}\mathbb{C}\to\operatorname{End}_0(W)$ is bijective; it is complex-linear by construction. $\qquad$ (Over $W = \slashed{S}$ this gives $\dim_{\mathbb{C}}\operatorname{End}_0(\slashed{S}) = \dim_{\mathbb{R}}\mathfrak{su}(\slashed{S}) = 3$, as $\operatorname{End}_0$ of a two-dimensional space is $\mathfrak{sl}_2(\mathbb{C})$.)

> [!note]- Lemma 3: Even Clifford elements act diagonally by left multiplication
> **Statement:** For vectors $a,b\in\mathbb{R}^4 = \mathbb{H}$, the product $a\cdot b$ acts on $\slashed{S} = \slashed{S}^{+}\oplus\slashed{S}^{-}$ preserving each summand, by
> $$(a\cdot b)\big|_{\slashed{S}^{+}} = L_{-a\bar b}, \qquad (a\cdot b)\big|_{\slashed{S}^{-}} = L_{-\bar a b}.$$
>
> **Hint:** Compose the two off-diagonal matrices of $(112)$.
>
> **Why needed:** It reduces the entire action of the even Clifford algebra — hence of two-forms — to left quaternion multiplication.
>
> > [!note]- Full proof
> > By the module structure $(112)$, a vector $h$ acts by $(v_1,v_2)\mapsto(hv_2,-\bar h v_1)$. Apply this with $h = b$ and then with $h = a$. On $\slashed{S}^{+}$, starting from $(v_1,0)$:
> > $$b\cdot(v_1,0) = (b\cdot 0,\,-\bar b v_1) = (0,\,-\bar b v_1) \qquad (\text{formula }(112)\text{ with }v_2 = 0),$$
> > $$a\cdot(0,\,-\bar b v_1) = \big(a(-\bar b v_1),\,-\bar a\cdot 0\big) = (-a\bar b\, v_1,\,0) \qquad (\text{formula }(112)\text{ with }v_1 = 0),$$
> > so $(a\cdot b)(v_1,0) = (-a\bar b\,v_1,0)$, i.e. left multiplication by $-a\bar b$ on $\slashed{S}^{+}$. On $\slashed{S}^{-}$, starting from $(0,v_2)$:
> > $$b\cdot(0,v_2) = (b v_2,\,0) \qquad (\text{formula }(112)\text{ with }v_1 = 0),$$
> > $$a\cdot(bv_2,\,0) = \big(a\cdot 0,\,-\bar a (b v_2)\big) = (0,\,-\bar a b\, v_2) \qquad (\text{formula }(112)\text{ with }v_2 = 0),$$
> > so $(a\cdot b)(0,v_2) = (0,-\bar a b\,v_2)$, i.e. left multiplication by $-\bar a b$ on $\slashed{S}^{-}$. In particular $a\cdot b$ preserves each summand, as an even element must. $\blacksquare$

> [!note]- Lemma 4: The vector map is injective and its complexification is bijective
> **Statement:** The real-linear map $\gamma:\mathbb{R}^4\to\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{+},\slashed{S}^{-})$, $\gamma(v)(\psi) = v\cdot\psi$, equals $v\mapsto L_{-\bar v}$; it is injective; its real image $R = \{L_w : w\in\mathbb{H}\}$ satisfies $R\cap iR = \{0\}$; and its complexification $\gamma_{\mathbb{C}}:\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\to\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{+},\slashed{S}^{-})$ is a complex-linear isomorphism. For fixed $\psi_0\ne 0$, $v\mapsto v\cdot\psi_0$ is an $\mathbb{R}$-linear isomorphism $\mathbb{R}^4\to\slashed{S}^{-}$.
>
> **Hint:** On $\slashed{S}^{+}$ a vector $v$ acts as the second component of $(112)$, namely $\psi\mapsto -\bar v\psi$; check that $J\circ L_w$ is never a left multiplication unless $w = 0$.
>
> **Why needed:** It is part (ii).
>
> > [!note]- Full proof
> > **Form of $\gamma$.** For $\psi\in\slashed{S}^{+}$, i.e. $(v_1,v_2) = (\psi,0)$, formula $(112)$ gives $v\cdot(\psi,0) = (v\cdot 0,-\bar v\psi) = (0,-\bar v\psi)$, so as a map $\slashed{S}^{+}\to\slashed{S}^{-}$ we have $\gamma(v) = L_{-\bar v}$: left multiplication by $-\bar v$. Each $L_w$ is complex-linear (Lemma 1's argument: left multiplication commutes with right multiplication by $\bar\imath$), so $\gamma(v)\in\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{+},\slashed{S}^{-})$.
> >
> > **Injectivity.** If $\gamma(v) = 0$ then $-\bar v = L_{-\bar v}(1) = 0$, so $v = 0$. (Equivalently, $v\cdot v\cdot\psi = -|v|^2\psi$ shows $\gamma(v)$ is invertible for $v\ne 0$.) The real image is $R = \{L_{-\bar v} : v\in\mathbb{H}\} = \{L_w : w\in\mathbb{H}\}$, since $v\mapsto -\bar v$ is a real-linear bijection of $\mathbb{H}$; thus $\dim_{\mathbb{R}} R = 4$.
> >
> > **The intersection $R\cap iR$.** The complex structure on the target is post-composition with $J$, right multiplication by $\bar\imath$ on $\slashed{S}^{-} = \mathbb{H}$: $(i\cdot T)(\psi) = J(T\psi) = (T\psi)\bar\imath$. Hence $iR = \{J\circ L_w : w\in\mathbb{H}\}$, where $(J\circ L_w)(\psi) = (w\psi)\bar\imath = w(\psi\bar\imath)$ (associativity). Suppose $L_{w'} = J\circ L_w$ for some $w,w'$, i.e. $w'\psi = w\psi\bar\imath$ for all $\psi\in\mathbb{H}$. Setting $\psi = 1$ gives $w' = w\bar\imath$; substituting back, $w\bar\imath\,\psi = w\psi\bar\imath$ for all $\psi$. If $w\ne 0$, cancel $w$ (left multiplication by a nonzero quaternion is injective) to get $\bar\imath\psi = \psi\bar\imath$ for all $\psi$; but $\psi = j$ gives $\bar\imath j = -ij = -k$ while $j\bar\imath = -ji = k$ (quaternion products), a contradiction. Hence $w = 0$, so $w' = 0$: $R\cap iR = \{0\}$.
> >
> > **Complexification is an isomorphism.** A general element of $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$ is $u\otimes 1 + u'\otimes i$ with $u,u'\in\mathbb{H}$, and $\gamma_{\mathbb{C}}(u\otimes 1 + u'\otimes i) = \gamma(u) + i\,\gamma(u') = L_{-\bar u} + J\circ L_{-\bar u'}$. If this is zero, then $L_{-\bar u} = -J\circ L_{-\bar u'}\in R\cap iR = \{0\}$ (the right side lies in $iR$, the left in $R$), so $L_{-\bar u} = 0$ and $J\circ L_{-\bar u'} = 0$; since $J$ is invertible, $L_{-\bar u'} = 0$ too, whence $u = u' = 0$. Thus $\gamma_{\mathbb{C}}$ is injective. Its domain has complex dimension $\dim_{\mathbb{R}}\mathbb{H} = 4$, and its codomain $\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{+},\slashed{S}^{-})\cong\operatorname{Hom}_{\mathbb{C}}(\mathbb{C}^2,\mathbb{C}^2)$ has complex dimension $4$; an injective complex-linear map between complex spaces of equal finite dimension is bijective. Hence $\gamma_{\mathbb{C}}$ is an isomorphism.
> >
> > **The map to $\slashed{S}^{-}$.** Fix $\psi_0\in\slashed{S}^{+}\setminus\{0\} = \mathbb{H}\setminus\{0\}$. The map $\mathbb{R}^4\to\slashed{S}^{-}$, $v\mapsto v\cdot\psi_0 = -\bar v\psi_0$, is real-linear; it is injective because $-\bar v\psi_0 = 0$ with $\psi_0\ne 0$ forces $\bar v = 0$ (left multiplication by $\psi_0$ is injective and quaternion multiplication has no zero divisors), so $v = 0$; and $\dim_{\mathbb{R}}\mathbb{R}^4 = 4 = \dim_{\mathbb{R}}\slashed{S}^{-}$, so it is a bijection. $\blacksquare$

> [!note]- Lemma 5: Clifford multiplication is $Spin(4)$-equivariant
> **Statement:** For $g\in Spin(4)\subset\mathrm{Cl}^0(\mathbb{R}^4)$, with $\rho(g)$ the spinor action (left Clifford multiplication by $g$) and $\xi(g) = \beta(q_+,q_-)$ the induced rotation, one has, for all $v\in\mathbb{R}^4$ and $\psi\in\slashed{S}$,
> $$\rho(g)\big(v\cdot\psi\big) = \big(\xi(g)v\big)\cdot\rho(g)\psi, \qquad\text{and}\qquad \rho(g)\,(a\cdot b)\,\rho(g)^{-1} = (\xi(g)a)\cdot(\xi(g)b)$$
> for vectors $a,b$. Consequently the maps $\gamma$ and $c$ of parts (ii), (iii) intertwine the $Spin(4)$-action on $\mathbb{R}^4$ (through $\xi = \beta$) and on $\Lambda^2\mathbb{R}^4$ with the conjugation/composition actions on the spinor Hom- and endomorphism-spaces.
>
> **Hint:** In the Clifford algebra $\xi(g)v = gvg^{-1}$, and $\rho$ is left multiplication, so the identity is $g(v\psi) = (gvg^{-1})(g\psi)$, pure associativity.
>
> **Why needed:** It makes the isomorphisms of (i)–(iii) equivariant, which is the form the applications need.
>
> > [!note]- Full proof
> > On [[Def - Spin Group and the Double Cover of SO(n)|the spin group page]] the double cover is realised by $\xi(g)v = g v g^{-1}$ for $g\in Spin(n)$ and $v\in\mathbb{R}^n\subset\mathrm{Cl}(\mathbb{R}^n)$ (for even $g$ the twisted and untwisted adjoints agree), and the spinor representation $\rho$ is the restriction to $Spin(n)$ of the Clifford module action, i.e. $\rho(g)\psi = g\cdot\psi = g\psi$. Then
> > $$\rho(g)(v\cdot\psi) = g(v\psi) = (gvg^{-1})(g\psi) = (\xi(g)v)\cdot(g\psi) = (\xi(g)v)\cdot\rho(g)\psi \qquad (\text{associativity; }g^{-1}g = 1),$$
> > which is the first identity. For the second, with vectors $a,b$,
> > $$\rho(g)(a\cdot b)\rho(g)^{-1} = g(ab)g^{-1} = (gag^{-1})(gbg^{-1}) = (\xi(g)a)\cdot(\xi(g)b) \qquad (\text{inserting }g^{-1}g = 1).$$
> > Since $\xi = \beta$ realises the $SO(4)$-action on $\mathbb{R}^4$, the induced action on the product $a\wedge b$ is the $SO(4)$-action on $\Lambda^2\mathbb{R}^4$; thus $c(g\cdot\omega) = \rho(g)\,c(\omega)\,\rho(g)^{-1}$ for all $\omega\in\Lambda^2\mathbb{R}^4$, and $\gamma(\xi(g)v) = \rho(g)\gamma(v)\rho(g)^{-1}$ as maps $\slashed{S}^{+}\to\slashed{S}^{-}$ (here $\rho(g)$ restricts to left multiplication by $q_\pm$ on $\slashed{S}^{\pm}$). The self-dual and anti-self-dual subspaces $\Lambda^2_\pm$ are the $\pm 1$-eigenspaces of the Hodge star $\star$, which commutes with orientation-preserving isometries ([[Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions|self-dual decomposition page]]), so they are $SO(4)$-invariant and the equivariance descends to each. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the four parts in turn, using Lemmas 1–5.
>
> ---
> **Part (i) — equation (111).** By **Lemma 1**, $\Phi(x) = L_x$ is a real-linear isomorphism $\operatorname{Im}\mathbb{H}\xrightarrow{\sim}\mathfrak{su}(\slashed{S})$ onto the traceless skew-Hermitian endomorphisms of the complex two-dimensional space $\slashed{S}$. Tensoring the source with $\mathbb{C}$ and using **Lemma 2** (with $W = \slashed{S}$), the complex-linear extension
> $$\Phi_{\mathbb{C}}:\operatorname{Im}\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\longrightarrow\operatorname{End}_0(\slashed{S}), \qquad \Phi_{\mathbb{C}}(x\otimes z) = z\,L_x,$$
> is the composite of the isomorphism $\operatorname{Im}\mathbb{H}\otimes\mathbb{C}\xrightarrow{\sim}\mathfrak{su}(\slashed{S})\otimes\mathbb{C}$ (Lemma 1, tensored with $\mathbb{C}$) with the isomorphism $\mathfrak{su}(\slashed{S})\otimes\mathbb{C}\xrightarrow{\sim}\operatorname{End}_0(\slashed{S})$ (Lemma 2), hence itself an isomorphism.
>
> **Equivariance.** $Sp(1)$ acts on $\operatorname{Im}\mathbb{H}$ through $\alpha$, $\alpha(q)x = qx\bar q = qxq^{-1}$ (as $\bar q = q^{-1}$), and on $\operatorname{End}_0(\slashed{S})$ by conjugation $T\mapsto\rho(q)T\rho(q)^{-1}$ with $\rho(q) = L_q$ the left-multiplication action. Then, for all $v\in\slashed{S}$,
> $$\Phi(\alpha(q)x)(v) = (qxq^{-1})v = q\big(x(q^{-1}v)\big) = L_q\,\Phi(x)\,L_q^{-1}(v) \qquad (\text{associativity}),$$
> so $\Phi(\alpha(q)x) = \rho(q)\Phi(x)\rho(q)^{-1}$; the same holds after tensoring with $\mathbb{C}$ (the action is $\mathbb{C}$-linear on both sides). Therefore $\Phi_{\mathbb{C}}$ is an isomorphism of $Sp(1)$-representations, which is (111). Finally $x\mapsto -i\,\Phi(x) = -iL_x$ carries $\operatorname{Im}\mathbb{H}$ bijectively onto the traceless *self-adjoint* endomorphisms: for $P = L_x\in\mathfrak{su}(\slashed{S})$ (so $P^{*} = -P$), the scalar-adjoint rule $(cT)^{*} = \bar c\,T^{*}$ gives $(-iP)^{*} = \overline{(-i)}\,P^{*} = (i)(-P) = -iP$, so $-iP$ is Hermitian; it is traceless since $\operatorname{tr}(-iP) = -i\operatorname{tr}P = 0$. As $x\mapsto L_x$ is a bijection onto $\mathfrak{su}(\slashed{S})$ (Lemma 1) and $P\mapsto -iP$ is a bijection from $\mathfrak{su}(\slashed{S})$ onto the traceless Hermitian endomorphisms (Lemma 2), the composite is the claimed bijection.
>
> ---
> **Part (ii) — equation (185).** By **Lemma 4**, $\gamma(v)(\psi) = v\cdot\psi$ is a real-linear injection $\mathbb{R}^4\to\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{+},\slashed{S}^{-})$ whose complexification $\gamma_{\mathbb{C}}:\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\to\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{+},\slashed{S}^{-})$ is a complex-linear isomorphism, and $v\mapsto v\cdot\psi_0$ is an $\mathbb{R}$-linear isomorphism $\mathbb{R}^4\to\slashed{S}^{-}$ for each $\psi_0\ne 0$. Interchanging the roles of the two chiral halves — the vector action $\slashed{S}^{-}\to\slashed{S}^{+}$ is $\psi\mapsto (v\cdot\psi)$ given by the first component of $(112)$, $L_v$ — the identical argument gives the isomorphism $\mathbb{H}\otimes\mathbb{C}\xrightarrow{\sim}\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{-},\slashed{S}^{+})$ and the isomorphism $\mathbb{R}^4\to\slashed{S}^{+}$, $v\mapsto v\cdot\psi_0$.
>
> **Equivariance.** By **Lemma 5**, $\gamma(\xi(g)v) = \rho(g)\gamma(v)\rho(g)^{-1}$ for $g\in Spin(4)$, where $Spin(4)$ acts on $\mathbb{R}^4$ through $\xi = \beta$ and on $\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{+},\slashed{S}^{-})$ by $T\mapsto\rho(g)_{-}\,T\,\rho(g)_{+}^{-1}$ (left multiplication by $q_-$ on the target $\slashed{S}^{-}$, precomposed with $q_+^{-1}$ on the source $\slashed{S}^{+}$). Extending $\mathbb{C}$-linearly, $\gamma_{\mathbb{C}}$ is an isomorphism of $Spin(4)$-representations, which is (185). Concretely, one may verify the equivariance by hand: $\gamma(\beta(q_+,q_-)v) = L_{-\overline{q_+ v\bar q_-}} = L_{-q_-\bar v\bar q_+}$ (since $\overline{q_+ v\bar q_-} = q_-\bar v\bar q_+$, using $\overline{abc} = \bar c\bar b\bar a$ and $\overline{\bar q_-} = q_-$), while $\rho(g)_{-}\gamma(v)\rho(g)_{+}^{-1}(\psi) = q_-\big(-\bar v(\bar q_+\psi)\big) = -q_-\bar v\bar q_+\psi = L_{-q_-\bar v\bar q_+}(\psi)$ (using $q_+^{-1} = \bar q_+$); the two agree.
>
> ---
> **Part (iii) — equations (186)–(187).** Fix the chirality $\slashed{S}^{+}$. By **Lemma 3**, $c(e_i\wedge e_j) = e_i\cdot e_j\cdot$ acts on $\slashed{S}^{+}$ as $L_{-e_i\bar e_j}$. With $e_1 = 1,e_2 = i,e_3 = j,e_4 = k$ (so $\bar e_1 = 1,\bar e_2 = -i,\bar e_3 = -j,\bar e_4 = -k$), the six increasing pairs give:
> $$
> \begin{aligned}
> c(e_1\wedge e_2) &= L_{-e_1\bar e_2} = L_{-(1)(-i)} = L_i, & c(e_3\wedge e_4) &= L_{-e_3\bar e_4} = L_{-(j)(-k)} = L_{jk} = L_i,\\
> c(e_1\wedge e_3) &= L_{-(1)(-j)} = L_j, & c(e_2\wedge e_4) &= L_{-(i)(-k)} = L_{ik} = L_{-j},\\
> c(e_1\wedge e_4) &= L_{-(1)(-k)} = L_k, & c(e_2\wedge e_3) &= L_{-(i)(-j)} = L_{ij} = L_k,
> \end{aligned}
> $$
> where $jk = i$, $ik = -j$, $ij = k$ are the quaternion products. Using the orthonormal bases of $\Lambda^2_\pm$ from [[Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions|the self-dual decomposition page]],
> $$\Lambda^2_+ = \operatorname{span}\{e_1\wedge e_2 + e_3\wedge e_4,\ e_1\wedge e_3 - e_2\wedge e_4,\ e_1\wedge e_4 + e_2\wedge e_3\},$$
> $$\Lambda^2_- = \operatorname{span}\{e_1\wedge e_2 - e_3\wedge e_4,\ e_1\wedge e_3 + e_2\wedge e_4,\ e_1\wedge e_4 - e_2\wedge e_3\},$$
> and the real-linearity of $c$, we combine the table entries:
> $$c(e_1\wedge e_2 + e_3\wedge e_4) = L_i + L_i = 2L_i, \quad c(e_1\wedge e_3 - e_2\wedge e_4) = L_j - L_{-j} = 2L_j, \quad c(e_1\wedge e_4 + e_2\wedge e_3) = L_k + L_k = 2L_k,$$
> $$c(e_1\wedge e_2 - e_3\wedge e_4) = L_i - L_i = 0, \quad c(e_1\wedge e_3 + e_2\wedge e_4) = L_j + L_{-j} = 0, \quad c(e_1\wedge e_4 - e_2\wedge e_3) = L_k - L_k = 0.$$
> **Kernel.** The three self-dual basis forms map to $2L_i,2L_j,2L_k$, which are linearly independent (they are twice the images of the linearly independent $i,j,k$ under the injective map $x\mapsto L_x$ of Lemma 1), and the three anti-self-dual basis forms map to $0$. Since $\{ \Lambda^2_+\text{-basis}\}\cup\{\Lambda^2_-\text{-basis}\}$ is a basis of $\Lambda^2\mathbb{R}^4$, the kernel of $c$ on $\slashed{S}^{+}$ is exactly $\Lambda^2_-$, and $c$ restricts to an injection on $\Lambda^2_+$.
> **Image and the isomorphism $\Lambda^2_+\cong\mathfrak{su}(\slashed{S}^{+})$.** The image of $c|_{\Lambda^2_+}$ is $\operatorname{span}\{2L_i,2L_j,2L_k\} = \operatorname{span}\{L_i,L_j,L_k\} = L_{\operatorname{Im}\mathbb{H}} = \mathfrak{su}(\slashed{S}^{+})$ (Lemma 1). Thus $c$ induces a real-linear isomorphism $\Lambda^2_+\xrightarrow{\sim}\mathfrak{su}(\slashed{S}^{+})$ (injective, equal three-dimensional real spaces); in particular the image is skew-Hermitian. Complexifying and applying **Lemma 2** gives $\Lambda^2_+\otimes_{\mathbb{R}}\mathbb{C}\xrightarrow{\sim}\mathfrak{su}(\slashed{S}^{+})\otimes\mathbb{C} = \operatorname{End}_0(\slashed{S}^{+})$, which is (187).
> **The other chirality.** By Lemma 3, $c(e_i\wedge e_j)$ acts on $\slashed{S}^{-}$ as $L_{-\bar e_i e_j}$; the same computation on this chirality gives
> $$c(e_1\wedge e_2) = L_{-i},\ c(e_3\wedge e_4) = L_{i},\quad c(e_1\wedge e_3) = L_{-j},\ c(e_2\wedge e_4) = L_{-j},\quad c(e_1\wedge e_4) = L_{-k},\ c(e_2\wedge e_3) = L_{k},$$
> (using $-\bar e_1 e_2 = -i$, $-\bar e_3 e_4 = jk = i$, $-\bar e_1 e_3 = -j$, $-\bar e_2 e_4 = ik = -j$, $-\bar e_1 e_4 = -k$, $-\bar e_2 e_3 = ij = k$), so on $\slashed{S}^{-}$ the *self-dual* basis forms map to $L_{-i}+L_i = 0$, $L_{-j}-L_{-j} = 0$, $L_{-k}+L_k = 0$, and the *anti-self-dual* ones to $-2L_i,-2L_j,-2L_k$. Hence the kernel on $\slashed{S}^{-}$ is $\Lambda^2_+$ and $c$ induces $\Lambda^2_-\xrightarrow{\sim}\mathfrak{su}(\slashed{S}^{-})$. This proves the "$\Lambda^2_\mp$ on $\slashed{S}^{\pm}$" kernel statement.
> **Equivariance and the consequences.** By **Lemma 5** the map $c$ intertwines the $SO(4)$-action on $\Lambda^2$ (through $\xi = \beta$) with conjugation on $\operatorname{End}(\slashed{S}^{\pm})$, and $\Lambda^2_\pm$ are invariant; so the isomorphisms $\Lambda^2_\pm\cong\mathfrak{su}(\slashed{S}^{\pm})$ are $Spin(4)$-equivariant. Since $\Lambda^2_-$ is the kernel on $\slashed{S}^{+}$, every anti-self-dual two-form acts as $0$ on $\slashed{S}^{+}$; by the symmetric statement every self-dual two-form acts as $0$ on $\slashed{S}^{-}$. Finally, $\Lambda^2_+\otimes\mathbb{C}$ acts on $\slashed{S}^{+}$ through $\operatorname{End}_0(\slashed{S}^{+}) = \mathfrak{sl}(\slashed{S}^{+})$ (its image is traceless, being $\mathfrak{su}(\slashed{S}^{+})\otimes\mathbb{C}$), and trivially on $\slashed{S}^{-}$ (its representatives $\Lambda^2_+$ lie in the kernel there), and dually for $\Lambda^2_-$.
>
> ---
> **Part (iv) — the spin$^{c}$ statements.** The group $Spin^{c}(4) = (Sp_+(1)\times Sp_-(1))\times U(1)/\{\pm 1\}$ acts on $\slashed{S}^{\pm}$ through $\rho_\pm([q_+,q_-,z]) = z\,L_{q_\pm}$ (the central circle $U(1)$ acting by the complex scalar $z$ on each summand); this is the action of §8.3, and it is well-defined because $\rho_\pm(-1,-1,-1) = (-1)L_{-1} = \operatorname{id}$. Two observations finish the proof.
>
> First, the central circle acts on $\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{+},\slashed{S}^{-})$ by $T\mapsto (zL_{\mathrm{id}})\,T\,(zL_{\mathrm{id}})^{-1} = z T z^{-1} = T$, because $z$ is a complex scalar and $T$ is complex-linear (a scalar on the source and its inverse on the target cancel). Hence $U(1)$ acts trivially on $\operatorname{Hom}_{\mathbb{C}}(\slashed{S}^{+},\slashed{S}^{-})$, matching the trivial $U(1)$-action on $\mathbb{H}\otimes\mathbb{C}$ ($U(1)$ maps to $SO(4)$ trivially under $\rho_0$, so it fixes every vector); the isomorphism $\gamma_{\mathbb{C}}$ of part (ii), already $Spin(4)$-equivariant, is therefore $Spin^{c}(4)$-equivariant. This is Haydys's assertion that (185) is valid as an isomorphism of $Spin^{c}(4)$-representations.
>
> Second, the central circle acts on $\operatorname{End}(\slashed{S}^{+})$ by $T\mapsto (zL_{\mathrm{id}})T(zL_{\mathrm{id}})^{-1} = T$ for the same reason, so $U(1)$ acts trivially on $\mathfrak{su}(\slashed{S}^{+})$ and on $\operatorname{End}_0(\slashed{S}^{+})$. The isomorphisms $\Lambda^2_+\cong\mathfrak{su}(\slashed{S}^{+})$ and $\Lambda^2_+\otimes\mathbb{C}\cong\operatorname{End}_0(\slashed{S}^{+})$ of part (iii), already $Spin(4)$-equivariant, are thus $Spin^{c}(4)$-equivariant with $U(1)$ acting trivially on the self-dual forms. All of parts (ii) and (iii), including the kernel statement and the vanishing of anti-self-dual forms on $\slashed{S}^{+}$, hold verbatim, since the underlying linear maps are unchanged — only the group acting has been enlarged. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Seiberg–Witten theory: the quadratic map as a self-dual form.** In chapter XI the quadratic map $\mu:\slashed{S}^{+}\to i\,\mathfrak{su}(\slashed{S}^{+})$, $\mu(\psi) = \psi\psi^{*} - \tfrac12|\psi|^2\operatorname{id}$, appears on the right of the curvature equation $F_A^{+} = \mu(\psi)$; see [[Def - The Quadratic Map on Positive Spinors|the quadratic map page]]. Part (iii) is exactly what gives this equation meaning: $\mu(\psi)$ is manifestly Hermitian ($(\psi\psi^{*})^{*} = \psi\psi^{*}$ and $\tfrac12|\psi|^2\operatorname{id}$ is real-scalar, so $\mu(\psi)^{*} = \mu(\psi)$) and traceless ($\operatorname{tr}(\psi\psi^{*}) = |\psi|^2$ and $\operatorname{tr}(\tfrac12|\psi|^2\operatorname{id}) = |\psi|^2$ on the two-dimensional $\slashed{S}^{+}$, so $\operatorname{tr}\mu(\psi) = 0$), hence lies in $i\,\mathfrak{su}(\slashed{S}^{+})$; through (187) it is therefore an *imaginary self-dual two-form*, the same kind of object as $F_A^{+}$. In the $\mathbb{C}^2$-model $\mu\binom{\psi_1}{\psi_2} = \tfrac12\left(\begin{smallmatrix}|\psi_1|^2-|\psi_2|^2 & 2\psi_1\bar\psi_2\\ 2\bar\psi_1\psi_2 & |\psi_2|^2-|\psi_1|^2\end{smallmatrix}\right)$, which is visibly traceless Hermitian. A good exercise is to verify these two clauses and to identify the self-dual two-form corresponding to $\mu(\psi)$ on the standard basis; it is non-obvious only because the target of $\mu$ looks like an endomorphism, not a form, until (187) is invoked.

> [!warning] Source typo (Haydys p. 61, Appendix B item 16)
> Haydys writes the polarised expansion as $\mu(\psi)(\phi) = \langle\phi,\psi\rangle\psi + \tfrac12|\psi|^2\phi$; the sign of the second term is inconsistent with tracelessness and with the matrix form above. The correct expansion is $\mu(\psi)(\phi) = \langle\phi,\psi\rangle\psi - \tfrac12|\psi|^2\phi$, and this is the form used in the series (the trace of the operator $\phi\mapsto\langle\phi,\psi\rangle\psi$ is $|\psi|^2$, cancelled by the $-\tfrac12|\psi|^2\cdot 2$ from the identity term).

**Ellipticity of Dirac-type operators.** On any spin$^{c}$ four-manifold the principal symbol of $\slashed{D}^{+}_A$ at a covector $\xi\ne 0$ is Clifford multiplication $\gamma(\xi):\slashed{S}^{+}_x\to\slashed{S}^{-}_x$; part (ii)'s last clause says this is an isomorphism, so $\slashed{D}^{+}_A$ is elliptic. The exercise is to write out the symbol sequence and check invertibility directly from $v\cdot v\cdot = -|v|^2$; the transfer to the *Atiyah complex* $0\to\Lambda^0\to\Lambda^1\to\Lambda^2_+\to 0$ is non-obvious because there the same fact is packaged as exactness of a three-term symbol sequence rather than invertibility of a single map.

**Representation theory of $SU(2)$.** Part (i) identifies two three-dimensional complex $Sp(1)$-representations, $\operatorname{Im}\mathbb{H}\otimes\mathbb{C}$ and $\operatorname{End}_0(\slashed{S})$. A clean exercise is to reprove (111) *without any explicit map*, purely from [[Thm - Complex Representations of U(1) and SU(2)|the classification of $SU(2)$-representations]]: both spaces are three-dimensional, both are irreducible (the adjoint representation and its avatar), and the three-dimensional irreducible $\varrho_2\cong(\operatorname{Ad}_{SU(2)})_{\mathbb{C}}$ is unique, so they are isomorphic. This makes visible that the explicit quaternion computation is one realisation of a representation-theoretic fact, and it is non-obvious because it replaces a basis computation by an appeal to uniqueness.

---

# Bridges

- **The two $Sp(1)$-factors and $\mathfrak{so}(4) = \mathfrak{so}(3)\oplus\mathfrak{so}(3)$.** Part (iii) exhibits $\Lambda^2_+ = \mathfrak{su}(\slashed{S}^{+})$ and $\Lambda^2_- = \mathfrak{su}(\slashed{S}^{-})$ as the Lie algebras of the two factors of $Spin(4) = Sp_+(1)\times Sp_-(1)$. Under the standard identification $\mathfrak{so}(4)\cong\Lambda^2\mathbb{R}^4$, $A\mapsto\tfrac12\sum_{i,j}\langle Ae_i,e_j\rangle e_i\wedge e_j$, this is exactly the Lie-algebra splitting $\mathfrak{so}(4) = \mathfrak{so}(3)\oplus\mathfrak{so}(3)$ that [[Thm - Spin Groups in Dimensions Three and Four via Quaternions|the quaternionic spin page]] uses to define $\beta$; the exercise [[Ex - so(4) Splits as so(3) plus so(3) via Self-Dual Forms|so(4) splits as so(3) ⊕ so(3)]] carries the identification out, and the present page supplies the spinor side of the dictionary. Each self-dual (respectively anti-self-dual) form is an infinitesimal rotation that acts nontrivially only on $\slashed{S}^{+}$ (respectively $\slashed{S}^{-}$).

- **The chiral Weitzenböck and Lichnerowicz formulas.** The full [[Thm - Weitzenbock Formula for the Dirac Operator|Weitzenböck formula]] $D^2 = \nabla^{*}\nabla + \mathcal{R}$ carries a curvature endomorphism $\mathcal{R} = \tfrac12\sum_{i,j}e_i\cdot e_j\cdot R_{e_i,e_j}$, which is Clifford multiplication by the curvature two-form. On $\slashed{S}^{+}$, part (iii) discards the anti-self-dual part of every curvature two-form, so the twisting curvature contributes only $\tfrac12 F_A^{+}\cdot$; this is the linear-algebra input to the chiral identity $\slashed{D}^{-}_A\slashed{D}^{+}_A = \nabla_A^{*}\nabla_A + \tfrac14 s_g + \tfrac12 F_A^{+}\cdot$ proved on the four-dimensional Weitzenböck page and used for the $C^0$ bound in chapter XI.

- **The Lorentzian analogue: Weyl spinors.** In four-dimensional Lorentzian signature the double cover is $SL(2,\mathbb{C})\to SO^{+}(3,1)$ rather than $Sp(1)\times Sp(1)\to SO(4)$, and the two chiral spinor representations $\slashed{S}^{\pm}$ become the two inequivalent two-dimensional complex representations of $SL(2,\mathbb{C})$ — the left- and right-handed **[[Def - Weyl Spinors (Left and Right Handed)|Weyl spinors]]** of special relativity — which are complex conjugates of each other rather than genuinely independent. The self-dual/anti-self-dual splitting of the electromagnetic field strength is the Lorentzian shadow of $\Lambda^2 = \Lambda^2_+\oplus\Lambda^2_-$; the present page is the compact, Riemannian version where the two halves are truly independent because $Spin(4)$ is a product.

---

# Unlocked by This

> [!tip] The Seiberg–Witten map is well-typed *(from Gauge Theory XI)*
> Because $\mu(\psi)$ lands in $i\Lambda^2_+$ by (187) and $\slashed{D}^{+}_A\psi$ lands in $\slashed{S}^{-}$ by (185), the Seiberg–Witten map $(\psi,A)\mapsto(\slashed{D}^{+}_A\psi,\ F_A^{+} - \mu(\psi))$ takes values in $\Gamma(\slashed{S}^{-})\oplus\Omega^2_+(M;i\mathbb{R})$; both target factors are named on this page. See **Def - Seiberg-Witten Equations**.

> [!tip] The Atiyah complex *(from Gauge Theory XI)*
> The vanishing of anti-self-dual forms on $\slashed{S}^{+}$ is what lets the linearised Seiberg–Witten and anti-self-duality equations be folded into the elliptic complex $0\to\Omega^0\to\Omega^1\to\Omega^2_+\oplus\Gamma(\slashed{S}^{-})\to 0$, whose index computes the dimension of the moduli space. See **Thm - The Origin is a Regular Value of the Perturbed Seiberg-Witten Map**.
