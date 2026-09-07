---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Classical Matrix Groups"
  - "Def - Lie Group Homomorphism"
  - "Def - Lie Group"
  - "Def - Embedded Submanifold"
  - "Thm - The Closed Subgroup Theorem"
  - "Thm - The Rank Theorem"
  - "Def - Complex Exponential and Trigonometric Functions"
tags: [geometry, gauge-theory, lie-groups]
---

# Notation

This page depends on the following standing conventions of the series. Manifolds are smooth, Hausdorff and second countable, and "smooth" means $C^\infty$. Lie groups are [[Def - Lie Group|Lie groups]] in the sense of the vault: a smooth manifold $G$ that is also a group, with multiplication $G \times G \to G$ and inversion $G \to G$ smooth. Representations and group actions on manifolds are on the left; nothing on this page depends on the side.

Throughout, $\operatorname{Mat}(n \times n; \mathbb{K})$ denotes the vector space of $n \times n$ matrices with entries in the field $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$, identified with $\mathbb{R}^{n^2}$ (when $\mathbb{K} = \mathbb{R}$) or $\mathbb{R}^{2n^2}$ (when $\mathbb{K} = \mathbb{C}$) by listing entries; $1_n$ is the identity matrix, $A^t$ the transpose, $\bar A$ the entrywise complex conjugate, and $A^* := (\bar A)^t$. The [[Def - Classical Matrix Groups|classical matrix groups]] that occur are
$$GL(n;\mathbb{K}) = \{A \in \operatorname{Mat}(n \times n;\mathbb{K}) : \det A \neq 0\}, \qquad O(n) = \{A \in GL(n;\mathbb{R}) : A^t A = 1_n\},$$
$$SO(n) = \{A \in O(n) : \det A = 1\}, \qquad U(n) = \{A \in \operatorname{Mat}(n \times n;\mathbb{C}) : A^* A = 1_n\}.$$
For $n = 1$ a matrix is a single entry, and we write $z$ rather than $(z)$; thus $GL(1;\mathbb{C}) = \mathbb{C}^\times := \mathbb{C} \setminus \{0\}$ and $U(1) = \{z \in \mathbb{C} : \bar z z = 1\} = \{z \in \mathbb{C} : |z| = 1\}$, where $|z| := \sqrt{\bar z z}$ is the modulus. Each of $GL(n;\mathbb{K})$, $O(n)$, $SO(n)$, $U(n)$ is a Lie group: $GL(n;\mathbb{K})$ is an open subset of $\operatorname{Mat}(n \times n;\mathbb{K})$ with polynomial multiplication and rational inversion, and the others are closed subgroups of it, hence embedded Lie subgroups by the [[Thm - The Closed Subgroup Theorem|closed subgroup theorem]]; both facts are recorded on [[Def - Classical Matrix Groups]] and are restated where they are used below (Lemma 6).

The circle is
$$S^1 := \{z \in \mathbb{C} : |z| = 1\} = \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 = 1\},$$
the two descriptions being identified through $\mathbb{C} = \mathbb{R}^2$, $x + iy \leftrightarrow (x, y)$. As a set, $S^1$ is literally $U(1)$; the content of the phrase "$U(1)$ is diffeomorphic to $S^1$" is that the Lie group structure on $U(1)$ coming from the closed subgroup theorem is the standard smooth structure on the circle, which we take to be the [[Def - Embedded Submanifold|embedded submanifold]] structure of $S^1 \subseteq \mathbb{R}^2$ (Lemma 6 identifies the two).

For $\varphi \in \mathbb{R}$ we write
$$R(\varphi) := \begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix} \in \operatorname{Mat}(2 \times 2;\mathbb{R})$$
for the rotation matrix through the angle $\varphi$. The functions $\exp$, $\cos$, $\sin$ are those of [[Def - Complex Exponential and Trigonometric Functions]]: $\exp(z) = e^z := \sum_{n \geq 0} z^n/n!$ for $z \in \mathbb{C}$, and
$$\cos z := \frac{e^{iz} + e^{-iz}}{2}, \qquad \sin z := \frac{e^{iz} - e^{-iz}}{2i}.$$
Every property of these functions that the page uses — the functional equation $e^{z+w} = e^z e^w$, Euler's formula $e^{i\varphi} = \cos\varphi + i\sin\varphi$, the identity $\cos^2\varphi + \sin^2\varphi = 1$, the addition theorems, and the fact that $\varphi \mapsto e^{i\varphi}$ maps $\mathbb{R}$ onto $S^1$ with fibres the cosets of $2\pi\mathbb{Z}$ — is proved on this page (Lemmas 1–3), because the vault page that states them, [[Thm - Properties of the Complex Exponential]], does not carry a complete proof and may not be cited as one. The number $\pi$ is defined in Lemma 3 as twice the smallest positive zero of $\cos$. The only results from real analysis invoked without proof on this page are the intermediate value theorem and the mean value theorem for real functions of one real variable, the binomial theorem, and the fact that a real-valued function that is differentiable on an interval with a positive derivative is strictly increasing there (a consequence of the mean value theorem); these are at the undergraduate floor of the vault.

A **Lie group homomorphism** $\Phi : G \to H$ is a smooth map that is a group homomorphism; a **Lie group isomorphism** is a Lie group homomorphism that is bijective and whose inverse is again a Lie group homomorphism ([[Def - Lie Group Homomorphism]]; this is also Bär's Definition 1.1.7). We prove the smoothness of the inverse directly rather than through the constant-rank argument recorded on that page. The symbol $\cong$ between Lie groups means "isomorphic as Lie groups". The map at the centre of the page is
$$\Phi : SO(2) \longrightarrow U(1), \qquad \Phi(A) := A_{11} + i A_{21},$$
which reads the first column of $A$ as a complex number; we show that it coincides with Bär's prescription $R(\varphi) \mapsto e^{i\varphi}$ and that it is a Lie group isomorphism. Its inverse is $\Psi : U(1) \to SO(2)$, $\Psi(x + iy) = \begin{pmatrix} x & -y \\ y & x \end{pmatrix}$.

> [!warning] Convention: matrix layout in the source
> Bär (Example 1.1.8) writes a general element of $SO(2)$ as $A = \begin{pmatrix} a & c \\ b & d \end{pmatrix}$, so that $a, b$ are the entries of the *first column* and $c, d$ those of the second. We keep this layout in Lemma 4 so that the equations (1.1)–(1.4) match the source line by line. In every other place the entries are written $A_{jk}$ (row $j$, column $k$), so $a = A_{11}$, $b = A_{21}$, $c = A_{12}$, $d = A_{22}$.

---

# Statement

> **Theorem ($SO(2) \cong U(1) \cong S^1$; Bär Example 1.1.8).** Let $SO(2)$ and $U(1)$ carry the Lie group structures of embedded Lie subgroups of $GL(2;\mathbb{R})$ and $GL(1;\mathbb{C})$ respectively. Then:
>
> **(a) Description of $SO(2)$.** Every $A \in SO(2)$ has the form $A = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $a^2 + b^2 = 1$, and every such matrix lies in $SO(2)$. Consequently
> $$SO(2) = \left\{ R(\varphi) = \begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix} : \varphi \in \mathbb{R} \right\},$$
> and $R(\varphi) = R(\psi)$ if and only if $\varphi - \psi \in 2\pi\mathbb{Z}$.
>
> **(b) Description of $U(1)$.** $U(1) = \{z \in \mathbb{C} : |z| = 1\} = \{e^{i\varphi} : \varphi \in \mathbb{R}\}$, and $e^{i\varphi} = e^{i\psi}$ if and only if $\varphi - \psi \in 2\pi\mathbb{Z}$.
>
> **(c) The isomorphism.** The map $\Phi : SO(2) \to U(1)$, $\Phi(A) = A_{11} + iA_{21}$, is an isomorphism of Lie groups, with inverse $\Psi(x + iy) = \begin{pmatrix} x & -y \\ y & x \end{pmatrix}$. In the angle description it reads
> $$\Phi\big(R(\varphi)\big) = e^{i\varphi} \qquad (\varphi \in \mathbb{R}),$$
> so the prescription $R(\varphi) \mapsto e^{i\varphi}$ of the source is well defined (independent of the choice of $\varphi$ representing a given rotation) and is this isomorphism. Hence $SO(2) \cong U(1)$.
>
> **(d) Both are circles.** $U(1)$ is equal to $S^1$ as a smooth manifold, and $\Phi$ is a diffeomorphism; hence $SO(2)$ and $U(1)$ are both diffeomorphic to the unit circle $S^1$. In particular both are compact, connected, abelian Lie groups of dimension one.

> **Companion form (the complex numbers as $2 \times 2$ real matrices).** The map $\Psi$ extends to the $\mathbb{R}$-linear map $M : \mathbb{C} \to \operatorname{Mat}(2 \times 2;\mathbb{R})$, $M(x + iy) = \begin{pmatrix} x & -y \\ y & x \end{pmatrix}$, and $M$ is an injective ring homomorphism: $M(zw) = M(z)M(w)$, $M(z + w) = M(z) + M(w)$, $M(1) = 1_2$. The isomorphism $\Phi$ is the inverse of the restriction of $M$ to the unit circle.

The companion form explains the theorem: $SO(2)$ is the unit circle inside the copy $M(\mathbb{C})$ of the complex numbers sitting inside the $2 \times 2$ real matrices, and $\Phi$ is nothing but the identification of that copy with $\mathbb{C}$ itself. Parts (a) and (b) are the two set-theoretic descriptions, (c) is the algebraic and smooth identification, and (d) is the topological conclusion.

---

# Motivation

The theorem is the first example in the series of two Lie groups, defined by unrelated-looking equations in different matrix spaces, being the *same* Lie group. $SO(2)$ is cut out of the four-dimensional space $\operatorname{Mat}(2 \times 2;\mathbb{R})$ by the orthogonality condition $A^t A = 1_2$ and the determinant condition $\det A = 1$; $U(1)$ is cut out of the two-dimensional space $\mathbb{C}$ by $\bar z z = 1$. That these two subsets are isomorphic as groups is the statement that rotating the plane through an angle is the same operation as multiplying by a unit complex number; that they are isomorphic as *Lie groups* is the further statement that the identification is smooth in both directions, so that every piece of differential-geometric structure — the Lie algebra, the exponential map, the invariant forms, the connections on bundles with this structure group — can be transported without loss.

Why does the series need this particular isomorphism, rather than merely noting it in passing? The structure group $U(1)$ is the structure group of electrodynamics (chapter VII) and of every Hermitian line bundle (chapters III and VI); $SO(2)$ is the structure group of an oriented real plane bundle. The theorem says these are the same theory: an oriented rank-two real vector bundle is the same thing as a complex line bundle, and the Euler class of the former is the first Chern class of the latter. Every time a later chapter passes between "a $U(1)$-connection" and "a metric connection on an oriented plane bundle", it is using the identification $\Phi$ and its smoothness.

The theorem also settles, in the smallest case, a question that the [[Def - Classical Matrix Groups|definition of the classical groups]] leaves open: what do these groups *look like* as manifolds? The definition presents each as a closed subset of a matrix space; the closed subgroup theorem promises a manifold structure but describes it only implicitly. Here we see explicitly that two real equations on four real entries leave exactly one free parameter, the angle, and that the resulting manifold is the circle. The same pattern — count the equations, find the free parameters, recognise the manifold — is the way one first understands $SU(2) \cong S^3$ ([[Ex - SU(2) is Diffeomorphic to S^3]]) and, later, the spheres and projective spaces that appear as homogeneous spaces.

Finally, the theorem is the one-dimensional case of a structural fact used repeatedly in chapter IV: an abelian Lie group has trivial adjoint representation. Since $U(1)$ is abelian, $\operatorname{Ad}_g = \operatorname{id}$ for every $g$, so a $U(1)$-connection's local forms transform by the addition of an exact form alone, $A_{s'} = A_s + g^{-1}dg$, with no conjugation term. The commutativity of $SO(2)$, which the theorem makes visible through $\Phi$ (multiplication of complex numbers is commutative), is the reason electrodynamics is a linear theory.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis of the theorem is simply "$A$ is a real $2 \times 2$ matrix with $A^t A = 1_2$ and $\det A = 1$", but that hypothesis arrives in several disguises.

The first disguised source is **a linear map of the plane that preserves lengths and orientation**. If $T : \mathbb{R}^2 \to \mathbb{R}^2$ is linear and satisfies $|Tv| = |v|$ for all $v$, then the polarisation identity $\langle v, w \rangle = \tfrac12(|v + w|^2 - |v|^2 - |w|^2)$ shows that $T$ preserves the inner product, so $\langle T^t T v, w \rangle = \langle v, w \rangle$ for all $v, w$ and $T^t T = 1_2$; if $T$ in addition preserves orientation, that is, $\det T > 0$, then since $(\det T)^2 = \det(T^t T) = 1$ we get $\det T = 1$. So a length- and orientation-preserving linear map of the plane is an element of $SO(2)$, and by the theorem it is a rotation $R(\varphi)$. *Example problem:* show that every isometry of the Euclidean plane fixing the origin and preserving orientation is a rotation about the origin.

The second disguised source is **a matrix that commutes with $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ and has unit determinant**. A real $2 \times 2$ matrix $A$ satisfies $AJ = JA$ if and only if it has the form $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ (compare the entries of $AJ$ and $JA$), that is, if and only if $A = M(a + ib)$ in the notation of the companion form; then $\det A = a^2 + b^2$, so $\det A = 1$ forces $A \in SO(2)$ by part (a). The bridge is non-obvious because "commutes with $J$" is a *complex-linearity* condition — $J$ is multiplication by $i$ on $\mathbb{R}^2 = \mathbb{C}$ — and the theorem says that complex-linear maps of $\mathbb{C}$ of modulus one are exactly the rotations. *Example problem:* show that the $\mathbb{C}$-linear isometries of $\mathbb{C}$ are the maps $z \mapsto e^{i\varphi} z$.

The third disguised source is **a one-parameter family of matrices solving $\dot A = JA$, $A(0) = 1_2$**. The unique solution of this linear system is $A(t) = R(t)$ (differentiate $R(t)$ using $\cos' = -\sin$, $\sin' = \cos$, which are established in Lemma 3 below, and use uniqueness of solutions of linear ordinary differential equations), and the theorem identifies its image with all of $SO(2)$; in the language of chapter I §1.4 this says $\exp(tJ) = R(t)$ and that the exponential map of $\mathfrak{so}(2) = \mathbb{R} J$ is surjective onto $SO(2)$ (the exercise `Ex - The Exponential Map of so(2) is Surjective but Not Injective` of the manifest). *Example problem:* compute the matrix exponential of $\theta J$ and identify its image.

**Targets (Output Amplification)**

Combine the conclusion with **the definition of the adjoint representation**. Since $\Phi$ is an isomorphism onto the abelian group $U(1)$, $SO(2)$ is abelian, so for every $g \in SO(2)$ the conjugation $C_g(h) = ghg^{-1}$ is the identity map and $\operatorname{Ad}_g = d(C_g)_e = \operatorname{id}$ ([[Def - Adjoint Representation]]). The payoff, used in chapter IV for $U(1)$-connections, is that the transformation law of local connection forms, $A_{s'} = \operatorname{Ad}_{g^{-1}} A_s + g^* \theta$, collapses to $A_{s'} = A_s + g^{-1}dg$, and the curvature $F = dA$ is gauge invariant rather than merely gauge covariant. The extra ingredient is the general transformation law; the theorem contributes the vanishing of the conjugation term.

Combine the conclusion with **the classification of complex representations of $U(1)$** (`Thm - Complex Representations of U(1) and SU(2)` in this chapter). Every representation of $SO(2)$ is, through $\Phi$, a representation of $U(1)$, and the irreducible complex ones are the characters $z \mapsto z^n$, $n \in \mathbb{Z}$; pulled back along $\Phi$ they become $R(\varphi) \mapsto e^{in\varphi}$. The payoff is the Fourier decomposition of any finite-dimensional representation of the rotation group of the plane into integer "frequencies", which is the algebraic origin of angular momentum quantisation in two dimensions. The extra ingredient is the classification; the theorem supplies the transport of representations across the isomorphism.

Combine the conclusion with **the classification of principal bundles by cocycles** (chapter III). Since $\Phi$ is a Lie group isomorphism, a principal $SO(2)$-bundle and a principal $U(1)$-bundle over the same base are the same object up to the relabelling of transition functions $g_{\alpha\beta} \mapsto \Phi \circ g_{\alpha\beta}$, and the associated bundles $P \times_{SO(2)} \mathbb{R}^2$ and $P \times_{U(1)} \mathbb{C}$ agree. The payoff is that oriented real plane bundles and complex line bundles are classified by the same data, so that the Euler class of the former is the first Chern class of the latter (chapter VI); the extra ingredient is the cocycle classification and the smoothness of $\Phi$, which is what makes the relabelled cocycle smooth.

---

# Why Is It True

Picture the set $SO(2)$ inside the four-dimensional space of $2 \times 2$ real matrices. The orthogonality condition $A^t A = 1_2$ is a *symmetric* matrix equation, so it imposes only three independent real conditions — the two diagonal ones, $a^2 + b^2 = 1$ and $c^2 + d^2 = 1$, and the single off-diagonal one, $ac + bd = 0$ — on the four entries. Three conditions on four unknowns leave, generically, a one-parameter family. The determinant condition $\det A = 1$ is not a further independent constraint but a *sign choice*: orthogonality already forces $(\det A)^2 = 1$, and $\det A = 1$ selects one of the two components of $O(2)$. So $SO(2)$ is a one-dimensional object, and the only compact connected one-dimensional manifold is a circle.

**The mechanism is that the orthogonality relations force the second column of $A$ to be the first column rotated by a quarter turn, so that a single unit vector — one angle — determines the whole matrix.** Concretely, the conditions say that the two columns $(a, b)$ and $(c, d)$ are unit vectors that are orthogonal to each other. In the plane, the unit vectors orthogonal to $(a, b)$ are exactly $\pm(-b, a)$, and the determinant condition $ad - bc = 1$ picks the sign $+$: with $(c, d) = (-b, a)$ we get $ad - bc = a^2 + b^2 = 1$, and with $(c, d) = (b, -a)$ we get $-a^2 - b^2 = -1$. Hence $A$ is determined by the unit vector $(a, b)$, that is, by a point of the circle, that is, by an angle $\varphi$ with $(a, b) = (\cos\varphi, \sin\varphi)$.

Once $A = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ has been recognised, the isomorphism with $U(1)$ is a statement about the *complex numbers*, not about the circle: the matrices of this shape are precisely the matrices $a \cdot 1_2 + b \cdot J$, with $J^2 = -1_2$, and these multiply exactly as the complex numbers $a + ib$ do. The map $\Phi$ is the restriction to unit vectors of a ring isomorphism from $\{a 1_2 + bJ\}$ onto $\mathbb{C}$. That is why $\Phi$ is a group homomorphism (multiplication is preserved by a ring isomorphism), why it is smooth (it is the restriction of a *linear* map), and why the inverse is smooth (it too is the restriction of a linear map). The angle parametrisation is not needed for any of this; it is needed only to name the elements. The addition theorems for sine and cosine, which the source uses to prove the homomorphism property, are in this picture the statement that $(\cos\varphi + i\sin\varphi)(\cos\psi + i\sin\psi) = \cos(\varphi + \psi) + i\sin(\varphi + \psi)$, that is, the functional equation of the exponential read through Euler's formula.

The failure mechanism the hypotheses rule out is worth naming. Without the determinant condition, the set $O(2)$ contains also the reflections $\begin{pmatrix} a & b \\ b & -a \end{pmatrix}$, and $O(2)$ is two disjoint circles, not one; it is not abelian (a reflection conjugates a rotation to its inverse), so no isomorphism with $U(1)$ exists. Without orthogonality, $SL(2;\mathbb{R})$ is three-dimensional and non-compact. The two conditions together, and only together, leave exactly the circle.

---

# What Makes This Hard

The algebra is elementary; the difficulties are in saying precisely what is being claimed. First, the source's map is defined by a formula in $\varphi$, but $\varphi$ is not a function of the matrix — it is determined only modulo $2\pi$ — so "$R(\varphi) \mapsto e^{i\varphi}$" is not a definition until one has checked that different choices of $\varphi$ for the same matrix give the same value. The clean way out is to define the map by a formula in the matrix entries ($\Phi(A) = A_{11} + iA_{21}$) and then show it agrees with the angle formula; the common error is to define it by the angle and never check independence. Second, "isomorphism of Lie groups" requires smoothness of $\Phi$ and of $\Phi^{-1}$ *with respect to the manifold structures on $SO(2)$ and $U(1)$*, which are not given by explicit charts but by the closed subgroup theorem; one must therefore know how to recognise a smooth map into or out of an embedded submanifold, and the common error is to differentiate the formula in the ambient matrix space and declare victory without saying why that suffices. Third, the elementary facts about $\cos$, $\sin$ and $e^{i\varphi}$ — that they parametrise the circle, that the parametrisation has period exactly $2\pi$ — are usually taken from calculus without proof; the vault's standard requires them to be proved, and the definition of $\pi$ must be located somewhere.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Solve the four scalar equations $A^t A = 1_2$, $\det A = 1$ for a real $2 \times 2$ matrix to find $A = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $a^2 + b^2 = 1$; observe that such matrices are the complex numbers $a + ib$ written as real matrices, so that reading off the first column is a multiplicative bijection onto the unit circle. Prove smoothness in both directions by noting that both the map and its inverse are restrictions of linear maps between the ambient vector spaces, and that a smooth map into an ambient manifold whose image lies in an embedded submanifold is smooth into the submanifold. Obtain the angle descriptions from the polar parametrisation of the circle, which is proved from the power series of the exponential.

**Subgoal decomposition:**

1. **Exponential functional equation and Euler's formula.** Prove $e^{z + w} = e^z e^w$ by the Cauchy product of absolutely convergent series and the binomial theorem; deduce that for real $\varphi$, $\cos\varphi$ and $\sin\varphi$ are real, $e^{i\varphi} = \cos\varphi + i\sin\varphi$, $\cos^2\varphi + \sin^2\varphi = 1$, and the addition theorems.
   - *Hint:* $\overline{e^{z}} = e^{\bar z}$ by conjugating the partial sums; $|e^{i\varphi}|^2 = e^{i\varphi} e^{-i\varphi} = e^0 = 1$.
   - *Why needed:* These identities are what make $R(\varphi)$ lie in $SO(2)$ and what turn the homomorphism property into the addition theorems.

2. **Polar parametrisation of the circle.** Prove that $\varphi \mapsto e^{i\varphi}$ maps $\mathbb{R}$ onto $S^1$ and that $e^{i\varphi} = 1$ if and only if $\varphi \in 2\pi\mathbb{Z}$, where $\pi$ is defined as twice the first positive zero of $\cos$.
   - *Hint:* $\cos 0 = 1$ and $\cos 2 < 0$ by an alternating-series estimate, so $\cos$ has a first positive zero $\pi/2$ by the intermediate value theorem; $\sin' = \cos > 0$ on $[0, \pi/2)$ makes $\sin$ increase to $\sin(\pi/2) = 1$; then $e^{i\pi/2} = i$, and every point of the first quadrant of the circle is hit by continuity of $\cos$ on $[0, \pi/2]$; other quadrants are reached by multiplying by powers of $i$. For the kernel, write $t \in (0, 2\pi)$ as $4 \cdot (t/4)$ and show $(x + iy)^4 \neq 1$ when $x, y > 0$.
   - *Why needed:* This is the "$\subseteq$" half of the descriptions $SO(2) = \{R(\varphi)\}$ and $U(1) = \{e^{i\varphi}\}$ and the precise statement of the ambiguity in $\varphi$.

3. **Shape of an element of $SO(2)$.** From $A^t A = 1_2$ and $\det A = 1$ derive $c = -b$ and $d = a$ by multiplying the determinant equation by $c$ and by $d$ and substituting the orthogonality relations.
   - *Hint:* $c = c(ad - bc) = (ac)d - bc^2 = -(bd)d - bc^2 = -b(c^2 + d^2) = -b$.
   - *Why needed:* It reduces $SO(2)$ to the unit circle in the two-dimensional space $\{a 1_2 + bJ\}$, which is where the isomorphism lives.

4. **The matrix model of $\mathbb{C}$.** Show that $M(x + iy) = \begin{pmatrix} x & -y \\ y & x \end{pmatrix}$ is an injective $\mathbb{R}$-linear ring homomorphism $\mathbb{C} \to \operatorname{Mat}(2 \times 2;\mathbb{R})$ with $\det M(z) = |z|^2$ and $M(z)^t = M(\bar z)$.
   - *Hint:* Multiply two matrices of the given shape and compare with $(x + iy)(u + iv) = (xu - yv) + i(xv + yu)$.
   - *Why needed:* It gives the homomorphism property of $\Phi = M^{-1}$ and the bijection $M : S^1 \to SO(2)$ at once.

5. **Smooth maps into embedded submanifolds.** Show that if $S \subseteq N$ is an embedded submanifold and $F : P \to N$ is smooth with $F(P) \subseteq S$, then $F : P \to S$ is smooth.
   - *Hint:* Use the immersion form of the rank theorem for the inclusion $\iota : S \hookrightarrow N$ and the subspace topology to write the coordinate representation of $F$ into $S$ as a projection of the coordinate representation of $F$ into $N$.
   - *Why needed:* $\Phi$ and $\Psi$ are restrictions of linear maps; this lemma converts that into smoothness as maps between $SO(2)$ and $U(1)$.

6. **The manifold structures.** Record that $SO(2)$ is an embedded submanifold of $\operatorname{Mat}(2 \times 2;\mathbb{R})$ and $U(1)$ an embedded submanifold of $\mathbb{C}$ (closed subgroups of open subsets), and that $U(1) = S^1$ as manifolds (uniqueness of embedded submanifold structures).
   - *Hint:* An embedded submanifold of an open subset $V \subseteq \mathbb{R}^k$ is an embedded submanifold of $\mathbb{R}^k$, because $V \hookrightarrow \mathbb{R}^k$ is a smooth embedding and the subspace topology is transitive.
   - *Why needed:* Without it, "smooth" in the statement has no meaning and part (d) is not even formulated.

7. **Assembly.** Define $\Phi$ by entries, check $\Phi \circ \Psi = \operatorname{id}$ and $\Psi \circ \Phi = \operatorname{id}$ using subgoal 3, the homomorphism property using subgoal 4, smoothness both ways using subgoals 5 and 6, and the angle formula using subgoal 1; conclude (a)–(d).
   - *Hint:* $\Phi(R(\varphi)) = \cos\varphi + i\sin\varphi = e^{i\varphi}$ is Euler's formula; well-definedness of the angle prescription is then automatic because $\Phi$ was defined on matrices.
   - *Why needed:* This is the theorem.

---

# Lemma Decomposition

The first three lemmas are the analytic input: they establish, from the power-series definition of $\exp$, every property of $e^{i\varphi}$, $\cos\varphi$ and $\sin\varphi$ that the theorem uses. Lemmas 4 and 5 are the algebra of $SO(2)$ and of the matrix model of $\mathbb{C}$. Lemmas 6 and 7 are the differential-geometric input on smooth maps into embedded submanifolds and on the manifold structures of $SO(2)$, $U(1)$ and $S^1$.

> [!note]- Lemma 1: The exponential series converges absolutely and satisfies $e^{z+w} = e^z e^w$
> **Statement:** For every $z \in \mathbb{C}$ the series $\sum_{n \geq 0} z^n/n!$ converges absolutely, so $e^z := \sum_{n \geq 0} z^n/n!$ is a well-defined complex number, and $e^0 = 1$. For all $z, w \in \mathbb{C}$,
> $$e^{z+w} = e^z e^w.$$
> In particular $e^z e^{-z} = 1$, so $e^z \neq 0$ for every $z$, and $(e^z)^n = e^{nz}$ for every integer $n \geq 0$.
>
> **Hint:** Compare the tail of the series with a geometric series to get absolute convergence; multiply the two series by the Cauchy product, which for absolutely convergent series converges to the product of the sums, and recognise $\sum_{k=0}^n \frac{z^k w^{n-k}}{k!(n-k)!} = \frac{(z+w)^n}{n!}$ by the binomial theorem.
>
> **Why needed:** The functional equation is the source of every identity on this page: Euler's formula turns it into the addition theorems for $\sin$ and $\cos$, it gives $|e^{i\varphi}| = 1$, and it gives the periodicity and the kernel $2\pi\mathbb{Z}$ in Lemma 3.
>
> > [!note]- Full proof
> > We are given $z, w \in \mathbb{C}$ and must show, first, that the exponential series converges absolutely, and second, that $e^{z+w} = e^z e^w$; the remaining assertions are then short consequences.
> >
> > **Step 1 — absolute convergence.** Fix $z \in \mathbb{C}$ and put $u_n := |z|^n/n! \geq 0$. Choose an integer $N \geq 2|z|$. For $n \geq N$,
> > $$\frac{u_{n+1}}{u_n} = \frac{|z|}{n+1} \leq \frac{|z|}{N} \leq \frac12 \qquad \text{(since } n + 1 > N \geq 2|z| \text{)},$$
> > so by induction on $m \geq 0$, $u_{N+m} \leq u_N 2^{-m}$. Hence
> > $$\sum_{n \geq N} u_n \leq u_N \sum_{m \geq 0} 2^{-m} = 2u_N < \infty \qquad \text{(comparison with the geometric series of ratio } \tfrac12\text{)},$$
> > and the finitely many terms $u_0, \dots, u_{N-1}$ do not affect convergence. Therefore $\sum_n |z^n/n!| < \infty$, and since absolutely convergent series of complex numbers converge (the partial sums form a Cauchy sequence, because $|\sum_{n=p}^q z^n/n!| \leq \sum_{n=p}^q u_n$, and $\mathbb{C}$ is complete), $e^z$ is a well-defined complex number. For $z = 0$ every term with $n \geq 1$ vanishes and the $n = 0$ term is $0^0/0! = 1$, so $e^0 = 1$.
> >
> > **Step 2 — the Cauchy product of two absolutely convergent series.** Let $(a_n)_{n \geq 0}$ and $(b_n)_{n \geq 0}$ be complex sequences with $\alpha := \sum_n |a_n| < \infty$ and $\beta := \sum_n |b_n| < \infty$, and put $A := \sum_n a_n$, $B := \sum_n b_n$, $c_n := \sum_{k=0}^n a_k b_{n-k}$. We claim $\sum_n c_n$ converges and equals $AB$. Write $A_N := \sum_{n \leq N} a_n$, $B_N := \sum_{n \leq N} b_n$, $C_N := \sum_{n \leq N} c_n$. Regrouping the finite sum,
> > $$C_N = \sum_{n=0}^N \sum_{k=0}^n a_k b_{n-k} = \sum_{\substack{k, l \geq 0 \\ k + l \leq N}} a_k b_l \qquad \text{(substituting } l = n - k \text{; this is a finite rearrangement)},$$
> > while $A_N B_N = \sum_{0 \leq k, l \leq N} a_k b_l$. Subtracting,
> > $$A_N B_N - C_N = \sum_{\substack{0 \leq k, l \leq N \\ k + l > N}} a_k b_l .$$
> > In every index pair of this last sum, $k + l > N$ forces $k > N/2$ or $l > N/2$ (if both were $\leq N/2$ their sum would be $\leq N$). Hence, splitting the index set into the pairs with $k > N/2$ and the remaining pairs (which have $l > N/2$),
> > $$|A_N B_N - C_N| \leq \sum_{k > N/2} |a_k| \sum_{l \geq 0} |b_l| + \sum_{k \geq 0} |a_k| \sum_{l > N/2} |b_l| = \beta \sum_{k > N/2} |a_k| + \alpha \sum_{l > N/2} |b_l| \qquad \text{(triangle inequality, then enlarging the index sets)}.$$
> > Both tails on the right tend to $0$ as $N \to \infty$, because $\sum |a_k|$ and $\sum |b_l|$ converge. Therefore $A_N B_N - C_N \to 0$. Since $A_N \to A$ and $B_N \to B$, we have $A_N B_N \to AB$ (product of convergent sequences), and so $C_N = A_N B_N - (A_N B_N - C_N) \to AB - 0 = AB$. This proves the claim.
> >
> > **Step 3 — apply the Cauchy product to the exponential series.** Take $a_k := z^k/k!$ and $b_l := w^l/l!$; both series are absolutely convergent by Step 1. Then
> > $$c_n = \sum_{k=0}^n \frac{z^k}{k!} \frac{w^{n-k}}{(n-k)!} = \frac{1}{n!} \sum_{k=0}^n \binom{n}{k} z^k w^{n-k} = \frac{(z + w)^n}{n!} \qquad \text{(since } \tfrac{1}{k!(n-k)!} = \tfrac{1}{n!}\binom{n}{k} \text{; then the binomial theorem)}.$$
> > By Step 2, $\sum_n c_n = (\sum_k a_k)(\sum_l b_l)$, that is,
> > $$e^{z + w} = \sum_{n \geq 0} \frac{(z+w)^n}{n!} = e^z e^w \qquad \text{(Step 2 with the identification of } c_n \text{ just made)}.$$
> >
> > **Step 4 — consequences.** Putting $w = -z$ gives $e^z e^{-z} = e^0 = 1$ (Step 3, then Step 1), so $e^z \neq 0$. For the power identity, induct on $n$: $(e^z)^0 = 1 = e^0$, and if $(e^z)^n = e^{nz}$ then $(e^z)^{n+1} = e^{nz} e^z = e^{(n+1)z}$ by Step 3.
> >
> > Therefore the exponential series converges absolutely for every complex argument and the exponential satisfies the functional equation $e^{z+w} = e^z e^w$, with the stated consequences. $\blacksquare$

> [!note]- Lemma 2: Euler's formula, the Pythagorean identity, and the addition theorems
> **Statement:** For every real $\varphi$, the numbers $\cos\varphi$ and $\sin\varphi$ are real, and
> $$e^{i\varphi} = \cos\varphi + i\sin\varphi, \qquad \cos^2\varphi + \sin^2\varphi = 1, \qquad |e^{i\varphi}| = 1.$$
> Moreover $\cos 0 = 1$, $\sin 0 = 0$, $\cos(-\varphi) = \cos\varphi$, $\sin(-\varphi) = -\sin\varphi$, and for all real $\varphi, \psi$ the addition theorems hold:
> $$\cos(\varphi + \psi) = \cos\varphi\cos\psi - \sin\varphi\sin\psi, \qquad \sin(\varphi + \psi) = \sin\varphi\cos\psi + \cos\varphi\sin\psi .$$
> Consequently $R(\varphi) \in SO(2)$ for every real $\varphi$, and $R(\varphi) R(\psi) = R(\varphi + \psi)$.
>
> **Hint:** Conjugation commutes with the exponential series, so $\overline{e^{i\varphi}} = e^{-i\varphi}$; Euler's formula is the sum of the defining expressions of $\cos$ and $i\sin$; the addition theorems are the real and imaginary parts of $e^{i(\varphi+\psi)} = e^{i\varphi}e^{i\psi}$.
>
> **Why needed:** It is what puts $R(\varphi)$ inside $SO(2)$ (the "$\supseteq$" half of part (a)), it identifies $\Phi(R(\varphi))$ with $e^{i\varphi}$, and it is the source's route to the homomorphism property.
>
> > [!note]- Full proof
> > Let $\varphi, \psi \in \mathbb{R}$. We must show the realness of $\cos\varphi$, $\sin\varphi$, the three displayed identities, the values at $0$, the parity relations, the addition theorems, and the two matrix consequences.
> >
> > **Conjugation commutes with $\exp$.** For $z \in \mathbb{C}$ and $N \geq 0$, $\overline{\sum_{n \leq N} z^n/n!} = \sum_{n \leq N} \bar z^n/n!$, because complex conjugation is a ring automorphism of $\mathbb{C}$ fixing the real numbers $1/n!$. Conjugation is continuous ($|\bar u - \bar v| = |u - v|$), so letting $N \to \infty$ on both sides (Lemma 1 guarantees both limits exist) gives $\overline{e^z} = e^{\bar z}$. For $z = i\varphi$ with $\varphi$ real, $\bar z = -i\varphi$, so
> > $$\overline{e^{i\varphi}} = e^{-i\varphi} . \tag{2.1}$$
> >
> > **Realness of $\cos\varphi$ and $\sin\varphi$.** By the definitions and (2.1),
> > $$\overline{\cos\varphi} = \overline{\left(\frac{e^{i\varphi} + e^{-i\varphi}}{2}\right)} = \frac{e^{-i\varphi} + e^{i\varphi}}{2} = \cos\varphi, \qquad \overline{\sin\varphi} = \overline{\left(\frac{e^{i\varphi} - e^{-i\varphi}}{2i}\right)} = \frac{e^{-i\varphi} - e^{i\varphi}}{-2i} = \sin\varphi \qquad \text{(by (2.1) and } \bar i = -i\text{)},$$
> > so both are fixed by conjugation, hence real.
> >
> > **Euler's formula.** Directly from the definitions,
> > $$\cos\varphi + i\sin\varphi = \frac{e^{i\varphi} + e^{-i\varphi}}{2} + i \cdot \frac{e^{i\varphi} - e^{-i\varphi}}{2i} = \frac{e^{i\varphi} + e^{-i\varphi} + e^{i\varphi} - e^{-i\varphi}}{2} = e^{i\varphi} \qquad \text{(since } i \cdot \tfrac{1}{2i} = \tfrac12\text{)}.$$
> > Since $\cos\varphi$ and $\sin\varphi$ are real, this says $\operatorname{Re} e^{i\varphi} = \cos\varphi$ and $\operatorname{Im} e^{i\varphi} = \sin\varphi$.
> >
> > **Modulus one and the Pythagorean identity.** By the definition of the modulus, (2.1), and Lemma 1,
> > $$|e^{i\varphi}|^2 = e^{i\varphi}\,\overline{e^{i\varphi}} = e^{i\varphi} e^{-i\varphi} = e^{0} = 1 \qquad \text{(by (2.1); then the functional equation of Lemma 1; then } e^0 = 1\text{)},$$
> > so $|e^{i\varphi}| = 1$. On the other hand, for a complex number with real part $x$ and imaginary part $y$ one has $|x + iy|^2 = x^2 + y^2$, so Euler's formula gives $|e^{i\varphi}|^2 = \cos^2\varphi + \sin^2\varphi$. Combining the two expressions for $|e^{i\varphi}|^2$, $\cos^2\varphi + \sin^2\varphi = 1$.
> >
> > **Values at $0$ and parity.** From $e^0 = 1$ (Lemma 1): $\cos 0 = (1 + 1)/2 = 1$ and $\sin 0 = (1 - 1)/(2i) = 0$. Replacing $\varphi$ by $-\varphi$ in the definitions exchanges $e^{i\varphi}$ and $e^{-i\varphi}$, which leaves $\cos$ unchanged and changes the sign of $\sin$: $\cos(-\varphi) = \cos\varphi$, $\sin(-\varphi) = -\sin\varphi$.
> >
> > **Addition theorems.** By Euler's formula applied to $\varphi + \psi$, then Lemma 1, then Euler's formula applied to $\varphi$ and to $\psi$,
> > $$\cos(\varphi+\psi) + i\sin(\varphi+\psi) = e^{i(\varphi+\psi)} = e^{i\varphi} e^{i\psi} = (\cos\varphi + i\sin\varphi)(\cos\psi + i\sin\psi)$$
> > $$= (\cos\varphi\cos\psi - \sin\varphi\sin\psi) + i(\sin\varphi\cos\psi + \cos\varphi\sin\psi) \qquad \text{(expanding, using } i^2 = -1\text{)}.$$
> > All of $\cos\varphi, \sin\varphi, \cos\psi, \sin\psi, \cos(\varphi+\psi), \sin(\varphi+\psi)$ are real, so the real parts of the two ends agree and the imaginary parts agree; these are exactly the two addition theorems.
> >
> > **$R(\varphi) \in SO(2)$.** Compute, with $c := \cos\varphi$, $s := \sin\varphi$,
> > $$R(\varphi)^t R(\varphi) = \begin{pmatrix} c & s \\ -s & c \end{pmatrix} \begin{pmatrix} c & -s \\ s & c \end{pmatrix} = \begin{pmatrix} c^2 + s^2 & -cs + sc \\ -sc + cs & s^2 + c^2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \qquad \text{(matrix multiplication; then } c^2 + s^2 = 1\text{)},$$
> > and $\det R(\varphi) = c \cdot c - (-s) \cdot s = c^2 + s^2 = 1$. Hence $R(\varphi) \in O(2)$ and $\det R(\varphi) = 1$, that is, $R(\varphi) \in SO(2)$.
> >
> > **$R(\varphi)R(\psi) = R(\varphi + \psi)$.** With $c, s$ as above and $c' := \cos\psi$, $s' := \sin\psi$,
> > $$R(\varphi) R(\psi) = \begin{pmatrix} c & -s \\ s & c \end{pmatrix} \begin{pmatrix} c' & -s' \\ s' & c' \end{pmatrix} = \begin{pmatrix} cc' - ss' & -(cs' + sc') \\ sc' + cs' & cc' - ss' \end{pmatrix} = \begin{pmatrix} \cos(\varphi+\psi) & -\sin(\varphi+\psi) \\ \sin(\varphi+\psi) & \cos(\varphi+\psi) \end{pmatrix} = R(\varphi + \psi) \qquad \text{(matrix multiplication; then the addition theorems)}.$$
> >
> > Therefore every stated identity holds; in particular $\varphi \mapsto R(\varphi)$ is a group homomorphism from $(\mathbb{R}, +)$ into $SO(2)$ and $\varphi \mapsto e^{i\varphi}$ is a group homomorphism from $(\mathbb{R}, +)$ into $U(1)$. $\blacksquare$

> [!note]- Lemma 3: The polar parametrisation of the unit circle
> **Statement:** The functions $\cos, \sin : \mathbb{R} \to \mathbb{R}$ are differentiable, with $\cos' = -\sin$ and $\sin' = \cos$; consequently they are smooth. There is a unique real number $\pi > 0$ such that $\pi/2$ is the smallest positive zero of $\cos$; for it, $\cos > 0$ on $[0, \pi/2)$, $\sin$ is strictly increasing on $[0, \pi/2]$ with $\sin(\pi/2) = 1$, and $e^{i\pi/2} = i$, $e^{i\pi} = -1$, $e^{2\pi i} = 1$. The map $\varphi \mapsto e^{i\varphi}$ is a surjection of $\mathbb{R}$ onto $S^1 = \{z \in \mathbb{C} : |z| = 1\}$, and for real $\varphi, \psi$,
> $$e^{i\varphi} = e^{i\psi} \iff \varphi - \psi \in 2\pi\mathbb{Z}.$$
> Equivalently, $(\cos\varphi, \sin\varphi) = (\cos\psi, \sin\psi)$ if and only if $\varphi - \psi \in 2\pi\mathbb{Z}$, and every $(a, b) \in \mathbb{R}^2$ with $a^2 + b^2 = 1$ equals $(\cos\varphi, \sin\varphi)$ for some real $\varphi$.
>
> **Hint:** Get the derivatives from the addition theorems together with the series estimates $|\sin h - h| \leq e|h|^3$, $|\cos h - 1| \leq e h^2$ for $|h| \leq 1$. Show $\cos 2 < 0$ by bounding the alternating series and use the intermediate value theorem to find the first zero. Use $\sin' = \cos > 0$ to push $\sin$ up to $1$ at $\pi/2$; then $e^{i\pi/2} = i$ and the four quadrants are related by multiplication by $i$. For the kernel, show $(x + iy)^4 \neq 1$ whenever $x, y > 0$ and $x^2 + y^2 = 1$.
>
> **Why needed:** It supplies the "$\subseteq$" half of both angle descriptions in parts (a) and (b), and the precise ambiguity $\varphi \bmod 2\pi$ that makes the source's prescription need a well-definedness check.
>
> > [!note]- Full proof
> > We must establish, in order: the series expansions of $\cos$ and $\sin$ on the reals; the derivatives; the existence of $\pi$ and the sign information on $[0, \pi/2]$; the special values of $e^{i\varphi}$; the kernel of $\varphi \mapsto e^{i\varphi}$; and its surjectivity onto $S^1$. Throughout, $\varphi, \psi, h, s, t$ denote real numbers.
> >
> > **Step 1 — real series for $\cos$ and $\sin$.** By Lemma 2, $\cos\varphi = \operatorname{Re} e^{i\varphi}$ and $\sin\varphi = \operatorname{Im} e^{i\varphi}$. Since $\operatorname{Re}$ and $\operatorname{Im}$ are continuous and additive, the real part of a convergent series is the series of real parts (apply $\operatorname{Re}$ to the partial sums and pass to the limit). Now $i^n \varphi^n/n!$ has real part $(-1)^{n/2}\varphi^n/n!$ if $n$ is even and $0$ if $n$ is odd, and imaginary part $0$ if $n$ is even and $(-1)^{(n-1)/2}\varphi^n/n!$ if $n$ is odd (because $i^{2m} = (-1)^m$ and $i^{2m+1} = (-1)^m i$). Deleting the zero terms of a convergent series does not change its sum (the partial sums of the thinned series form a subsequence of the original partial sums). Hence
> > $$\cos\varphi = \sum_{m \geq 0} (-1)^m \frac{\varphi^{2m}}{(2m)!}, \qquad \sin\varphi = \sum_{m \geq 0} (-1)^m \frac{\varphi^{2m+1}}{(2m+1)!} \qquad \text{(real and imaginary parts of the series for } e^{i\varphi}\text{)},$$
> > both series being absolutely convergent since their terms are dominated in modulus by those of $\sum |\varphi|^n/n!$ (Lemma 1, Step 1).
> >
> > **Step 2 — two estimates near $0$.** For $|h| \leq 1$, using Step 1 and the triangle inequality,
> > $$|\sin h - h| = \Big| \sum_{m \geq 1} (-1)^m \frac{h^{2m+1}}{(2m+1)!} \Big| \leq \sum_{m \geq 1} \frac{|h|^{2m+1}}{(2m+1)!} \leq |h|^3 \sum_{m \geq 1} \frac{1}{(2m+1)!} \leq e\,|h|^3 \qquad \text{(since } |h|^{2m+1} \leq |h|^3 \text{ for } m \geq 1 \text{ and } |h| \leq 1 \text{; and } \textstyle\sum_{k \geq 0} 1/k! = e^1 =: e\text{)},$$
> > $$|\cos h - 1| = \Big| \sum_{m \geq 1} (-1)^m \frac{h^{2m}}{(2m)!} \Big| \leq h^2 \sum_{m \geq 1} \frac{1}{(2m)!} \leq e\,h^2 \qquad \text{(the same reasoning)}.$$
> > Consequently $\lim_{h \to 0} \frac{\sin h}{h} = 1$ (because $|\sin h/h - 1| \leq e h^2$) and $\lim_{h \to 0} \frac{\cos h - 1}{h} = 0$ (because $|(\cos h - 1)/h| \leq e|h|$).
> >
> > **Step 3 — derivatives.** For $h \neq 0$, by the addition theorems of Lemma 2,
> > $$\frac{\sin(\varphi + h) - \sin\varphi}{h} = \frac{\sin\varphi\cos h + \cos\varphi\sin h - \sin\varphi}{h} = \sin\varphi \cdot \frac{\cos h - 1}{h} + \cos\varphi \cdot \frac{\sin h}{h} \xrightarrow[h \to 0]{} \sin\varphi \cdot 0 + \cos\varphi \cdot 1 = \cos\varphi \qquad \text{(addition theorem for } \sin\text{; then Step 2)},$$
> > $$\frac{\cos(\varphi + h) - \cos\varphi}{h} = \cos\varphi \cdot \frac{\cos h - 1}{h} - \sin\varphi \cdot \frac{\sin h}{h} \xrightarrow[h \to 0]{} -\sin\varphi \qquad \text{(addition theorem for } \cos\text{; then Step 2)}.$$
> > So $\sin' = \cos$ and $\cos' = -\sin$ on $\mathbb{R}$. In particular both functions are differentiable, hence continuous; and by induction each is $n$ times differentiable for every $n$ with $n$-th derivative among $\pm\cos, \pm\sin$, so both are smooth. It follows that $\varphi \mapsto R(\varphi)$ and $\varphi \mapsto e^{i\varphi} = \cos\varphi + i\sin\varphi$ are smooth maps $\mathbb{R} \to \operatorname{Mat}(2 \times 2;\mathbb{R})$ and $\mathbb{R} \to \mathbb{C}$ (their component functions are smooth).
> >
> > **Step 4 — $\cos 2 < 0$ and the definition of $\pi$.** Put $t_m := 4^m/(2m)!$, so that $\cos 2 = \sum_{m \geq 0} (-1)^m t_m$ by Step 1. For $m \geq 1$,
> > $$\frac{t_{m+1}}{t_m} = \frac{4}{(2m+1)(2m+2)} \leq \frac{4}{3 \cdot 4} = \frac13 < 1 \qquad \text{(the denominator is smallest at } m = 1\text{)},$$
> > so $(t_m)_{m \geq 1}$ is strictly decreasing. For the tail $T := \sum_{m \geq 2} (-1)^m t_m$ (convergent, as a subseries of an absolutely convergent series) we claim $T \leq t_2$. Indeed, for every $N \geq 2$ the partial sum satisfies
> > $$\sum_{m=2}^N (-1)^m t_m = t_2 - (t_3 - t_4) - (t_5 - t_6) - \dots \leq t_2 \qquad \text{(grouping consecutive terms; each bracket is } \geq 0 \text{ because } (t_m) \text{ is decreasing; a final unpaired term } -t_N \text{ with } N \text{ odd is also } \leq 0\text{)},$$
> > and passing to the limit preserves the inequality. Therefore
> > $$\cos 2 = t_0 - t_1 + T \leq 1 - 2 + t_2 = -1 + \frac{16}{24} = -\frac13 < 0 \qquad \text{(with } t_0 = 1,\ t_1 = 4/2 = 2,\ t_2 = 16/24\text{)}.$$
> > Since $\cos 0 = 1 > 0$ (Lemma 2), $\cos 2 < 0$, and $\cos$ is continuous (Step 3), the intermediate value theorem gives a zero of $\cos$ in $(0, 2)$. Let $Z := \{x \in (0, 2] : \cos x = 0\}$, a nonempty set bounded below by $0$, and let $x_0 := \inf Z$. There is a sequence $x_n \in Z$ with $x_n \to x_0$, so $\cos x_0 = \lim \cos x_n = 0$ by continuity. Moreover $x_0 > 0$: since $\cos 0 = 1$ and $\cos$ is continuous, there is $\delta > 0$ with $\cos > 1/2$ on $[0, \delta]$, so $Z \cap (0, \delta] = \emptyset$ and $x_0 \geq \delta$. Thus $x_0$ is the smallest positive zero of $\cos$ (any positive zero $x < x_0$ would lie in $(0, 2]$, since $x < x_0 \leq 2$, and would contradict $x_0 = \inf Z$). We **define** $\pi := 2x_0$; this is the unique positive number with the stated property.
> >
> > **Step 5 — signs on $[0, \pi/2]$.** On $[0, \pi/2)$ the function $\cos$ has no zero (Step 4) and $\cos 0 = 1 > 0$; if $\cos$ took a negative value at some $x \in (0, \pi/2)$, the intermediate value theorem would give a zero in $(0, x)$, contradicting minimality. Hence $\cos > 0$ on $[0, \pi/2)$. Since $\sin' = \cos$ (Step 3) is positive on the open interval $(0, \pi/2)$ and $\sin$ is continuous on $[0, \pi/2]$, the mean value theorem shows $\sin$ is strictly increasing on $[0, \pi/2]$: for $0 \leq u < v \leq \pi/2$, $\sin v - \sin u = (v - u)\cos\xi$ for some $\xi \in (u, v)$, and $\cos\xi > 0$. As $\sin 0 = 0$, we get $\sin > 0$ on $(0, \pi/2]$. In the same way, $\cos' = -\sin < 0$ on $(0, \pi/2)$ makes $\cos$ strictly decreasing on $[0, \pi/2]$. Finally $\sin^2(\pi/2) = 1 - \cos^2(\pi/2) = 1 - 0 = 1$ (Lemma 2, Step 4) and $\sin(\pi/2) > 0$, so $\sin(\pi/2) = 1$.
> >
> > **Step 6 — special values.** By Euler's formula (Lemma 2) and Step 5, $e^{i\pi/2} = \cos(\pi/2) + i\sin(\pi/2) = 0 + i = i$. By Lemma 1, $e^{i\pi} = (e^{i\pi/2})^2 = i^2 = -1$ and $e^{2\pi i} = (e^{i\pi})^2 = 1$. Consequently, for every real $\varphi$ and integer $k$, $e^{i(\varphi + 2\pi k)} = e^{i\varphi}(e^{2\pi i})^k = e^{i\varphi}$ (Lemma 1; for negative $k$ use $e^{-2\pi i} = (e^{2\pi i})^{-1} = 1$). Taking real and imaginary parts, $\cos$ and $\sin$ are $2\pi$-periodic.
> >
> > **Step 7 — the kernel: $e^{it} \neq 1$ for $0 < t < 2\pi$.** Let $0 < t < 2\pi$ and put $s := t/4 \in (0, \pi/2)$, $x := \cos s$, $y := \sin s$. By Step 5, $x > 0$ and $y > 0$, and $x^2 + y^2 = 1$ by Lemma 2. By Lemma 1 and Euler's formula, $e^{it} = (e^{is})^4 = (x + iy)^4$. Expanding,
> > $$(x + iy)^2 = (x^2 - y^2) + 2ixy, \qquad (x + iy)^4 = \big((x^2 - y^2) + 2ixy\big)^2 = (x^2 - y^2)^2 - 4x^2y^2 + 4ixy(x^2 - y^2) \qquad \text{(squaring twice, } i^2 = -1\text{)}.$$
> > Suppose, for a contradiction, that $e^{it} = 1$. Then the imaginary part $4xy(x^2 - y^2)$ vanishes; as $x, y > 0$ this forces $x^2 = y^2$, and with $x^2 + y^2 = 1$ we get $x^2 = y^2 = 1/2$. But then the real part is $(x^2 - y^2)^2 - 4x^2y^2 = 0 - 4 \cdot \tfrac14 = -1 \neq 1$, contradicting $e^{it} = 1$. Hence $e^{it} \neq 1$ for all $t \in (0, 2\pi)$.
> >
> > **Step 8 — the fibres.** Let $\varphi, \psi$ be real. Multiplying by $e^{-i\psi}$ (which is invertible, Lemma 1), $e^{i\varphi} = e^{i\psi}$ if and only if $e^{i(\varphi - \psi)} = 1$. If $\varphi - \psi \in 2\pi\mathbb{Z}$, then $e^{i(\varphi-\psi)} = 1$ by Step 6. Conversely, suppose $e^{i(\varphi - \psi)} = 1$. Let $k := \lfloor (\varphi - \psi)/2\pi \rfloor \in \mathbb{Z}$ and $t := \varphi - \psi - 2\pi k \in [0, 2\pi)$. Then $1 = e^{i(\varphi-\psi)} = e^{2\pi i k} e^{it} = e^{it}$ (Lemma 1 and Step 6), so $t = 0$ by Step 7, that is, $\varphi - \psi = 2\pi k \in 2\pi\mathbb{Z}$. By Euler's formula and the realness of $\cos, \sin$, the condition $e^{i\varphi} = e^{i\psi}$ is the same as $(\cos\varphi, \sin\varphi) = (\cos\psi, \sin\psi)$, which gives the equivalent formulation.
> >
> > **Step 9 — surjectivity onto $S^1$.** Let $w = a + ib \in \mathbb{C}$ with $a, b$ real and $a^2 + b^2 = 1$. We distinguish three cases, which are exhaustive: either $b \geq 0$ and $a \geq 0$, or $b \geq 0$ and $a < 0$, or $b < 0$.
> >
> > *Case 1: $a \geq 0$ and $b \geq 0$.* Since $a^2 \leq 1$ we have $0 \leq a \leq 1$. The function $\cos$ is continuous on $[0, \pi/2]$ with $\cos 0 = 1 \geq a$ and $\cos(\pi/2) = 0 \leq a$, so by the intermediate value theorem there is $s \in [0, \pi/2]$ with $\cos s = a$. By Step 5 (and $\sin 0 = 0$), $\sin s \geq 0$, and $\sin^2 s = 1 - \cos^2 s = 1 - a^2 = b^2$, so $\sin s = |b| = b$ (Lemma 2 for the Pythagorean identity; $b \geq 0$). Hence $e^{is} = \cos s + i\sin s = a + ib = w$.
> >
> > *Case 2: $a < 0$ and $b \geq 0$.* The number $-iw = -ia + b = b + i(-a)$ has real part $b \geq 0$ and imaginary part $-a > 0$, and modulus $|{-i}||w| = 1$. By Case 1 there is $s$ with $e^{is} = -iw$. Then $w = i e^{is} = e^{i\pi/2} e^{is} = e^{i(s + \pi/2)}$ (Step 6, then Lemma 1).
> >
> > *Case 3: $b < 0$.* The number $-w = (-a) + i(-b)$ has imaginary part $-b > 0$ and modulus $1$, so by Case 1 or Case 2 there is $s$ with $e^{is} = -w$. Then $w = -e^{is} = e^{i\pi} e^{is} = e^{i(s + \pi)}$ (Step 6, then Lemma 1).
> >
> > In every case $w = e^{i\varphi}$ for some real $\varphi$. Since also $|e^{i\varphi}| = 1$ for every $\varphi$ (Lemma 2), the image of $\varphi \mapsto e^{i\varphi}$ is exactly $S^1$. Taking real and imaginary parts, every $(a, b)$ on the unit circle is $(\cos\varphi, \sin\varphi)$ for some $\varphi$.
> >
> > Therefore $\cos$ and $\sin$ are smooth with the stated derivatives, $\pi$ is well defined, and $\varphi \mapsto e^{i\varphi}$ is a surjection $\mathbb{R} \to S^1$ whose fibres are exactly the cosets of $2\pi\mathbb{Z}$. $\blacksquare$
