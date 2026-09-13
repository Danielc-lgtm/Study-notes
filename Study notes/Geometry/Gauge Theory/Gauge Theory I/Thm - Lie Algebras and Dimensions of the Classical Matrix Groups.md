---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Classical Matrix Groups"
  - "Def - The Lie Algebra of a Lie Group"
  - "Thm - Regular Value Theorem on Manifolds"
  - "Thm - Left-Invariant Vector Fields Form a Lie Algebra"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\mathbb{K}$ denotes either $\mathbb{R}$ or $\mathbb{C}$, and $\operatorname{Mat}(n \times n; \mathbb{K})$ is the space of $n \times n$ matrices with entries in $\mathbb{K}$, a real vector space of dimension $n^2$ when $\mathbb{K} = \mathbb{R}$ and $2n^2$ when $\mathbb{K} = \mathbb{C}$. We write $1_n$ for the identity matrix, $A^t$ for the transpose of $A$, $\bar{A}$ for the entrywise complex conjugate, and $A^* := \bar{A}^t = \overline{A^t}$ for the conjugate transpose (adjoint). The trace is $\operatorname{tr} A = \sum_{i=1}^n a_{ii}$ and the determinant is $\det A$. The **commutator** of two matrices is $[A, B] := AB - BA$.

The classical matrix groups are as fixed on the definition page [[Def - Classical Matrix Groups]]: the general linear group $GL(n; \mathbb{K}) = \{A : \det A \neq 0\}$; the orthogonal group $O(n) = \{A \in GL(n; \mathbb{R}) : A^t A = 1_n\}$ and its identity component the special orthogonal group $SO(n) = O(n) \cap \{\det A = 1\}$; the special linear group $SL(n; \mathbb{K}) = \{A : \det A = 1\}$; the unitary group $U(n) = \{A \in GL(n; \mathbb{C}) : A^* A = 1_n\}$ and the special unitary group $SU(n) = U(n) \cap SL(n; \mathbb{C})$; and the group $Sp(1) = \{q \in \mathbb{H} : |q| = 1\}$ of unit [[Def - Quaternions|quaternions]]. Here $\mathbb{H} = \{a + b\mathrm{i} + c\mathrm{j} + d\mathrm{k} : a,b,c,d \in \mathbb{R}\}$ is the quaternion algebra, with conjugate $\bar{q} = a - b\mathrm{i} - c\mathrm{j} - d\mathrm{k}$, norm $|q|^2 = q\bar{q} = a^2 + b^2 + c^2 + d^2$, real part $\operatorname{Re} q = a$, and imaginary part $\operatorname{Im} q = b\mathrm{i} + c\mathrm{j} + d\mathrm{k}$; the space of purely imaginary quaternions is $\operatorname{Im}\mathbb{H} = \{q : \operatorname{Re} q = 0\}$, a real vector space of dimension $3$.

We use two spaces of structured matrices: the symmetric matrices $\operatorname{Sym}(n) = \{S \in \operatorname{Mat}(n \times n; \mathbb{R}) : S^t = S\}$, a real vector space of dimension $n(n+1)/2$, and the Hermitian matrices $\operatorname{Herm}(n) = \{H \in \operatorname{Mat}(n \times n; \mathbb{C}) : H^* = H\}$, a real vector space of dimension $n^2$.

The Lie algebra of a Lie group follows the series convention. For a Lie group $G$ with identity $e$, the **Lie algebra** $\mathfrak{g} = \operatorname{Lie}(G)$ is the space of left-invariant vector fields on $G$, with the Lie bracket of vector fields; the evaluation map $X \mapsto X_e$ is a linear isomorphism $\mathfrak{g} \cong T_e G$ (proved on [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]]), and we transport the bracket to $T_e G$ along it. For a matrix group $G \subseteq GL(n; \mathbb{K})$ the identity is $e = 1_n$, the tangent space $T_{1_n} G$ is a linear subspace of $T_{1_n}\!\operatorname{Mat}(n \times n; \mathbb{K}) \cong \operatorname{Mat}(n \times n; \mathbb{K})$, and under this identification the transported bracket is the matrix commutator (proved on [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]]). We write $\mathfrak{gl}(n;\mathbb{K}), \mathfrak{o}(n), \mathfrak{so}(n), \mathfrak{sl}(n;\mathbb{K}), \mathfrak{u}(n), \mathfrak{su}(n), \mathfrak{sp}(1)$ for the Lie algebras of the corresponding groups. For a smooth map $\Phi$ between vector spaces (or manifolds) and a point $A$ of the domain, $d\Phi_A$ is the differential (total derivative) of $\Phi$ at $A$, a linear map between the tangent spaces.

> [!warning] Convention: identity element and completion of the dimension count
> The source (Bär, *Gauge Theory*, Ex. 1.2.7, pp. 12–13) writes $1_n$ for the group identity, which we keep for matrix groups; the standing series notation for a general Lie group identity is $e$, and the two coincide here. Bär establishes each identity $\mathfrak{g} = \{\text{constraint}\}$ by differentiating the defining equation along a curve — which yields only the *inclusion* $\mathfrak{g} \subseteq \{\text{constraint}\}$ — and then closes the argument by asserting a dimension count "$\dim \mathfrak{g} = \dim G = n(n-1)/2 = \dim\{A^t + A = 0\}$", with $\dim O(n)$ and the formula $\frac{d}{ds}\det c(s)\big|_0 = \operatorname{tr}\dot c(0)$ taken as known. We supply both missing pieces here: the determinant derivative is Lemma 1, and each dimension is *derived*, not assumed, by exhibiting the group as a regular level set (Lemma 2) so that the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] delivers the dimension and the tangent space in one stroke.

> [!warning] Convention: adjoint notation
> $A^* = \bar{A}^t$ is the conjugate transpose; over $\mathbb{R}$ it reduces to $A^t$. Bär writes $A^*$ for this throughout. The group $Sp(1)$ of unit quaternions is not in Bär's §1.2 enumeration; it is carried here from [[Def - Classical Matrix Groups]] because chapters III–VI need $\mathfrak{sp}(1)$ and the isomorphism $Sp(1) \cong SU(2)$.

---

# Statement

> **Theorem (Lie algebras and dimensions of the classical matrix groups).** For each classical matrix group $G$, identify its Lie algebra $\mathfrak{g}$ with $T_{1_n} G \subseteq \operatorname{Mat}(n \times n; \mathbb{K})$ via the evaluation isomorphism $\mathfrak{g} \cong T_{1_n} G$, and equip it with the matrix commutator $[A, B] = AB - BA$. Then:
>
> 1. $\mathfrak{gl}(n; \mathbb{R}) = \operatorname{Mat}(n \times n; \mathbb{R})$, with $\dim \mathfrak{gl}(n; \mathbb{R}) = n^2$.
> 2. $\mathfrak{o}(n) = \mathfrak{so}(n) = \{A \in \operatorname{Mat}(n \times n; \mathbb{R}) : A^t + A = 0\}$ (the antisymmetric matrices), with $\dim \mathfrak{o}(n) = \dfrac{n(n-1)}{2}$.
> 3. $\mathfrak{sl}(n; \mathbb{R}) = \{A \in \operatorname{Mat}(n \times n; \mathbb{R}) : \operatorname{tr} A = 0\}$ (the traceless real matrices), with $\dim \mathfrak{sl}(n; \mathbb{R}) = n^2 - 1$.
> 4. $\mathfrak{u}(n) = \{A \in \operatorname{Mat}(n \times n; \mathbb{C}) : A^* = -A\}$ (the anti-Hermitian matrices), with $\dim_{\mathbb{R}} \mathfrak{u}(n) = n^2$.
> 5. $\mathfrak{sl}(n; \mathbb{C}) = \{A \in \operatorname{Mat}(n \times n; \mathbb{C}) : \operatorname{tr} A = 0\}$ (the traceless complex matrices), with $\dim_{\mathbb{R}} \mathfrak{sl}(n; \mathbb{C}) = 2n^2 - 2$.
> 6. $\mathfrak{su}(n) = \{A \in \operatorname{Mat}(n \times n; \mathbb{C}) : A^* = -A,\ \operatorname{tr} A = 0\}$ (the traceless anti-Hermitian matrices), with $\dim_{\mathbb{R}} \mathfrak{su}(n) = n^2 - 1$.
> 7. $\mathfrak{sp}(1) = \operatorname{Im}\mathbb{H} = \{b\mathrm{i} + c\mathrm{j} + d\mathrm{k} : b,c,d \in \mathbb{R}\}$ (the purely imaginary quaternions), with $\dim \mathfrak{sp}(1) = 3$ and bracket the quaternion commutator, which on $\operatorname{Im}\mathbb{H} \cong \mathbb{R}^3$ equals twice the cross product.
>
> In each case the listed subspace is closed under the commutator, so it is genuinely a Lie subalgebra of $\mathfrak{gl}(n; \mathbb{K})$, and $\dim_{\mathbb{R}} \mathfrak{g} = \dim G$.

---

# Motivation

A Lie group is a curved object — a manifold — but its Lie algebra is a flat one — a vector space with a bilinear bracket. Nearly everything one wants to compute about a Lie group is first linearised into a statement about its Lie algebra, where the tools of linear algebra apply, and only afterward exponentiated back. The connections, curvatures, and characteristic classes of gauge theory all take their values in a Lie algebra; the very phrase "an $SU(2)$-connection" means a one-form valued in $\mathfrak{su}(2)$. So before any of that machinery can run, one must know, concretely and correctly, *what the Lie algebra of each structure group is* — which matrices it consists of, and how many real parameters that is.

This theorem answers exactly that for the seven groups that recur throughout the series. It is not a single clever fact but a uniform method applied seven times: realise the group as the solution set of a matrix equation, differentiate the equation at the identity to see which infinitesimal matrices are allowed, and count. The reason the method is worth isolating as a theorem — rather than redone ad hoc for each group — is that the naïve execution has a genuine trap (the codomain of the defining map must be chosen correctly, or the differential is never surjective and the whole argument collapses), and because the dimension counts it produces, $\dim SU(2) = 3$, $\dim U(1) = 1$, $\dim SO(3) = 3$, are load-bearing constants in every later chapter. When chapter VI computes the second Chern number of an $SU(2)$-bundle, or chapter VII normalises the Yang–Mills functional with the inner product $-\operatorname{tr}(XY)$ on $\mathfrak{su}(n)$, or chapter IV writes a $\mathfrak{u}(1) = \mathrm{i}\mathbb{R}$-valued connection for electromagnetism, it is drawing on the identifications proved here.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem is a special case of a single principle: *a subgroup of $GL(n; \mathbb{K})$ that is cut out by a smooth equation whose differential is surjective at the identity is a Lie group, and its Lie algebra is the kernel of that differential.* The seven groups treated here are the instances Bär needs, but the same machine identifies the Lie algebra of any group presented in one of the following disguised forms.

The first disguised source is **the isometry group of a bilinear, sesquilinear, or quaternionic-Hermitian form**. If $J$ is a fixed nondegenerate matrix and $G = \{A : A^\dagger J A = J\}$ — where $\dagger$ is transpose, conjugate transpose, or quaternionic conjugate transpose — then $G$ is the level set at $J$ of $\Phi(A) = A^\dagger J A$, whose image lies in the matrices of a definite $\pm$-symmetry type. Differentiating gives $d\Phi_{1_n}(X) = X^\dagger J + J X$, so the Lie algebra is $\{X : X^\dagger J + J X = 0\}$. The bridge $B \Rightarrow A$ is the observation that $O(n), U(n)$, the symplectic group $Sp(2m; \mathbb{R})$ (with $J = \left(\begin{smallmatrix} 0 & 1_m \\ -1_m & 0 \end{smallmatrix}\right)$), the indefinite orthogonal groups $O(p,q)$, and the compact symplectic group $Sp(m)$ are all of this shape; recognising a group as a form-isometry group instantly hands over both its Lie algebra and its dimension. *Example problem:* show that the Lie algebra of $Sp(2m; \mathbb{R})$ is $\{X : X^t J + J X = 0\}$, of real dimension $m(2m+1)$, by verifying that $d\Phi_A(X) = X^t J A + A^t J X$ is surjective onto the antisymmetric matrices for every $A \in Sp(2m; \mathbb{R})$.

The second disguised source is **the kernel of a Lie group character or determinant-type constraint**. If $\chi : G \to \mathbb{K}^\times$ is a smooth homomorphism (a character) and one forms the "special" subgroup $S = \ker \chi = \{g : \chi(g) = 1\}$, then $S$ is the level set at $1$ of $\chi$ and its Lie algebra is $\ker d\chi_{1_n}$. The bridge is that $SL(n; \mathbb{K}) = \ker(\det)$ and $SU(n) = \ker(\det|_{U(n)})$ are exactly of this form; the differential of $\det$ at the identity is the trace (Lemma 1), so the special condition on the group ($\det = 1$) becomes the linear condition on the algebra ($\operatorname{tr} = 0$). *Example problem:* identify the Lie algebra of the group $\{A \in GL(n; \mathbb{C}) : |\det A| = 1\}$ as $\{X : \operatorname{Re}\operatorname{tr} X = 0\}$ by taking $\chi(A) = |\det A|$ and differentiating.

The third disguised source is **a stabiliser subgroup of a smooth group action with a regular orbit**. If a Lie group $H$ acts smoothly on a manifold $M$ and $v \in M$ has orbit map $\ell_v : H \to M$, $h \mapsto h \cdot v$, that is a submersion onto the orbit, then the stabiliser $\operatorname{Stab}(v) = \ell_v^{-1}(v)$ is a submanifold whose Lie algebra is the kernel of the infinitesimal action $\mathfrak{h} \to T_v M$, $X \mapsto \frac{d}{ds}\big|_0 \exp(sX)\cdot v$. The bridge is that $SO(n-1) \hookrightarrow SO(n)$ arises as the stabiliser of a unit vector under the defining action on $S^{n-1}$, and the orbit-stabiliser identification of $S^{n-1} = SO(n)/SO(n-1)$ then reads off $\dim SO(n) = \dim SO(n-1) + (n-1)$ inductively. *Example problem:* recover $\dim SO(n) = n(n-1)/2$ from $\dim SO(2) = 1$ and the recursion $\dim SO(n) = \dim SO(n-1) + (n-1)$ produced by the stabiliser presentation.

**Targets (Output Amplification)**

The bare output is a list of seven subspaces and their dimensions. Combined with one further ingredient each, these become the working facts of the later chapters.

Combine the identification $\mathfrak{u}(1) = \mathrm{i}\mathbb{R}$ and $\dim SU(2) = 3$ **with the Chern–Weil construction**. The extra ingredient is the invariant polynomial machinery of chapter VI. For a $U(1)$-bundle the curvature is an $\mathrm{i}\mathbb{R}$-valued two-form, so $\frac{\mathrm{i}}{2\pi} F$ is a real two-form and $c_1 = [\frac{\mathrm{i}}{2\pi} F]$ makes sense; the identification $\mathfrak{u}(1) = \mathrm{i}\mathbb{R}$ is what turns the abstract curvature into an ordinary real class. For an $SU(2)$-bundle the three-dimensionality of the fibre $\mathfrak{su}(2)$ is what makes the instanton number $\frac{1}{8\pi^2}\int \operatorname{tr}(F \wedge F)$ an integer detecting $\pi_3(SU(2)) = \mathbb{Z}$. The payoff is that every characteristic-class computation in the series is grounded in these two facts.

Combine $\mathfrak{su}(n) = \{A^* = -A,\ \operatorname{tr} A = 0\}$ **with the search for an $\operatorname{Ad}$-invariant inner product**. The extra ingredient is positive-definiteness. On anti-Hermitian matrices the form $\langle X, Y \rangle = -\operatorname{tr}(XY)$ satisfies $-\operatorname{tr}(X^2) = \operatorname{tr}(X^* X) = \sum_{i,j}|x_{ij}|^2 \geq 0$, so it is a genuine inner product, and it is $\operatorname{Ad}$-invariant because trace is conjugation-invariant. The payoff is the norm $|F|^2$ in the Yang–Mills functional $\mathcal{YM}(A) = \frac12 \int |F|^2$ of chapter VII; without the explicit anti-Hermitian description one could not check the sign that makes the functional bounded below.

Combine $\mathfrak{sp}(1) = \operatorname{Im}\mathbb{H}$ with bracket $2\times$ **with the classification of low-dimensional Lie algebras**. The extra ingredient is the abstract isomorphism $(\mathbb{R}^3, \times) \cong \mathfrak{so}(3) \cong \mathfrak{su}(2)$. Since $\mathfrak{sp}(1)$, $\mathfrak{su}(2)$, and $\mathfrak{so}(3)$ are all three-dimensional with the same structure constants, the three groups $Sp(1)$, $SU(2)$, $SO(3)$ share a Lie algebra, and $Sp(1) \cong SU(2)$ is the simply connected double cover of $SO(3)$. The payoff is the spin double cover used throughout chapters VIII and XI, and the identification $Sp(1) \cong SU(2)$ recorded in [[Def - Classical Matrix Groups]].

---

# Why Is It True

The picture is this. A matrix group $G$ sits inside the vector space $\operatorname{Mat}(n \times n; \mathbb{K})$ as the solution set of one or more polynomial equations — $A^t A = 1_n$, or $\det A = 1$. Its Lie algebra is the set of velocity vectors of curves that stay inside $G$ and pass through the identity at time zero. To find those velocities, take any curve $c(s)$ with $c(0) = 1_n$ that satisfies the defining equation identically in $s$, and differentiate the equation at $s = 0$. Differentiation converts a *multiplicative* constraint on the group into a *linear* constraint on the velocity $\dot c(0)$: the product rule turns $c(s)^t c(s) = 1_n$ into $\dot c(0)^t + \dot c(0) = 0$, and $\det c(s) = 1$ into $\operatorname{tr}\dot c(0) = 0$. That is the entire mechanism.

> **The Lie algebra of a matrix group is the linearisation of its defining equation: differentiate the constraint that holds on the group, and the tangent constraint that survives at the identity is exactly the equation cutting out $\mathfrak{g}$.**

But differentiating a curve only shows that every element of $\mathfrak{g}$ *satisfies* the linear constraint — it gives an inclusion $\mathfrak{g} \subseteq \{\text{constraint}\}$, not an equality. Something must rule out the possibility that $\mathfrak{g}$ is a proper subspace of the solutions of the linear constraint. That something is a dimension count, and the cleanest way to get an honest dimension count is to promote the naïve curve argument into an application of the regular value theorem. If the defining map $\Phi$ (say $\Phi(A) = A^t A$) has surjective differential at every point of $G$, then $G$ is a submanifold of codimension exactly $\dim(\text{target of }\Phi)$, its tangent space at the identity is precisely $\ker d\Phi_{1_n}$ — the full solution space of the linear constraint, not a proper subspace — and its dimension is forced. The surjectivity of $d\Phi$ is what upgrades the inclusion to an equality; it is the one nontrivial input, and it is where the correct choice of target space earns its keep.

---

# What Makes This Hard

The single subtle step is **choosing the codomain of the defining map correctly so that its differential is surjective**. The map $\Phi(A) = A^t A$ always produces a symmetric matrix, so if one regards $\Phi$ as taking values in all of $\operatorname{Mat}(n \times n; \mathbb{R})$, its differential can never be onto — its image is trapped inside the symmetric matrices — and $1_n$ is not a regular value, so the regular value theorem does not apply and one computes the wrong codimension ($n^2$ instead of $n(n+1)/2$, giving a negative dimension for $O(n)$). The fix is to declare the codomain to be $\operatorname{Sym}(n)$ from the start; then surjectivity holds and the count is right. The parallel trap for $U(n)$ is to forget that $A \mapsto A^* A$ lands in the *Hermitian* matrices, a real space of dimension $n^2$, not the complex space of dimension $2n^2$. The second, quieter difficulty is the case of $SU(n)$: its two constraints ($A^* A = 1_n$ and $\det A = 1$) are not independent in the naïve sense, and one must observe that on anti-Hermitian matrices the trace is automatically purely imaginary, so "$\operatorname{tr} = 0$" is a single real condition, not two — which is why $\dim \mathfrak{su}(n) = n^2 - 1$ and not $n^2 - 2$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For each group, write down the smooth map $\Phi$ whose level set at $1_n$ is the group, chosen with the *correct* codomain (symmetric, Hermitian, $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{R}$ again). Show $d\Phi_A$ is surjective for every $A$ in the group by exhibiting a preimage of an arbitrary target vector. The regular value theorem then gives the dimension (ambient dimension minus target dimension) and identifies the Lie algebra with $\ker d\Phi_{1_n}$. Read off that kernel by solving the linear equation. The bracket is the commutator because $T_{1_n} G$ is a Lie subalgebra of $\mathfrak{gl}(n)$, whose bracket is the commutator.

**Subgoal decomposition:**

1. **Determinant derivative.** Show $\frac{d}{ds}\big|_{0}\det(1_n + sX) = \operatorname{tr} X$, and more generally $d(\det)_A(X) = \det(A)\,\operatorname{tr}(A^{-1}X)$ for invertible $A$.
   - *Hint:* Expand $\det(1_n + sX)$ by the permutation formula and collect the coefficient of $s^1$; only the identity permutation contributes.
   - *Why needed:* It is the differential of the defining map for $SL(n;\mathbb{R})$, $SL(n;\mathbb{C})$, and $SU(n)$, and it is the dimension-count input Bär leaves unproved.

2. **Regular-level-set bridge.** Show that if a matrix group $G = \Phi^{-1}(y_0)$ with $d\Phi_A$ surjective on $G$, then $\dim G = \dim(\text{domain}) - \dim(\text{codomain})$ and $\mathfrak{g} \cong T_{1_n} G = \ker d\Phi_{1_n}$.
   - *Hint:* Apply the regular value theorem, then the evaluation isomorphism $\mathfrak{g} \cong T_{1_n} G$.
   - *Why needed:* It converts each surjectivity computation into a dimension and a Lie algebra simultaneously, closing the gap the curve argument leaves open.

3. **Bracket is the commutator.** Show the transported bracket on $T_{1_n} G$ is the restriction of the matrix commutator.
   - *Hint:* $T_{1_n} G$ is a Lie subalgebra of $\mathfrak{gl}(n) = \operatorname{Mat}(n \times n)$, whose bracket is $[A,B] = AB - BA$.
   - *Why needed:* Without it the seven subspaces are only vector spaces, not Lie algebras.

4. **Seven applications.** Run the machine on $GL, O = SO, SL(\cdot;\mathbb{R}), U, SL(\cdot;\mathbb{C}), SU, Sp(1)$, computing $\Phi$, its surjective differential, the kernel, and the dimension in each.
   - *Hint:* For each defining equation, guess the preimage of a target vector by scaling the target with $A$ (e.g. $X = \frac12 A S$ hits the symmetric $S$).
   - *Why needed:* These are the seven conclusions of the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: The differential of the determinant at the identity is the trace
> **Statement:** For $X \in \operatorname{Mat}(n \times n; \mathbb{K})$, $\det(1_n + sX) = 1 + s\,\operatorname{tr} X + O(s^2)$ as $s \to 0$, so $d(\det)_{1_n}(X) = \operatorname{tr} X$. More generally, for invertible $A$ and any $X$, $d(\det)_A(X) = \det(A)\,\operatorname{tr}(A^{-1}X)$.
>
> **Hint:** Expand the Leibniz permutation formula for $\det(1_n + sX)$ and isolate the coefficient of $s$; then factor $A + sX = A(1_n + sA^{-1}X)$ for the general point.
>
> **Why needed:** It differentiates the constraint $\det = 1$ into $\operatorname{tr} = 0$, and it is precisely the step the source uses without proof.
>
> > [!note]- Full proof
> > **Expansion at the identity.** By the Leibniz formula for the determinant,
> > $$\det(1_n + sX) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{i=1}^n \big(\delta_{i\,\sigma(i)} + s\,x_{i\,\sigma(i)}\big) \qquad \text{(Leibniz formula, with } (1_n + sX)_{ij} = \delta_{ij} + s x_{ij}\text{)},$$
> > where $\delta_{ij}$ is the Kronecker delta and $S_n$ the symmetric group on $n$ letters.
> >
> > **Constant term.** The term with no factor of $s$ takes $\delta_{i\,\sigma(i)}$ from every factor. This vanishes unless $\sigma(i) = i$ for all $i$, i.e. $\sigma = \operatorname{id}$, which contributes $\operatorname{sgn}(\operatorname{id})\prod_i \delta_{ii} = 1$. So the $s^0$ coefficient is $1$.
> >
> > **Linear term.** A term of order $s^1$ chooses the factor $s\,x_{i\,\sigma(i)}$ from exactly one index $i$ and $\delta_{j\,\sigma(j)}$ from the remaining $n-1$ indices $j \neq i$. For a nonzero contribution we need $\sigma(j) = j$ for all $j \neq i$ (from the $\delta$ factors); since $\sigma$ is a bijection, this forces $\sigma(i) = i$ as well, so $\sigma = \operatorname{id}$ (whence $\operatorname{sgn}(\sigma) = 1$) and the chosen factor is $s\,x_{ii}$. Summing over the index $i$ that supplied the $s$-factor,
> > $$[s^1]\det(1_n + sX) = \sum_{i=1}^n x_{ii} = \operatorname{tr} X \qquad \text{(only } \sigma = \operatorname{id} \text{ survives, one summand per diagonal entry)}.$$
> > All remaining terms carry at least two factors of $s$ and lie in $O(s^2)$. Hence $\det(1_n + sX) = 1 + s\,\operatorname{tr} X + O(s^2)$, and differentiating at $s = 0$ gives $\frac{d}{ds}\big|_0 \det(1_n + sX) = \operatorname{tr} X$. Since $s \mapsto 1_n + sX$ is the line through $1_n$ with velocity $X$, this says $d(\det)_{1_n}(X) = \operatorname{tr} X$.
> >
> > **General invertible point.** For invertible $A$ write $A + sX = A(1_n + sA^{-1}X)$, so by multiplicativity of the determinant
> > $$\det(A + sX) = \det(A)\,\det(1_n + sA^{-1}X) = \det(A)\big(1 + s\,\operatorname{tr}(A^{-1}X) + O(s^2)\big) \qquad \text{(the identity-point expansion applied to } A^{-1}X\text{)}.$$
> > Differentiating at $s = 0$, $d(\det)_A(X) = \det(A)\,\operatorname{tr}(A^{-1}X)$. This completes the proof. $\blacksquare$

> [!note]- Lemma 2: A matrix group cut out by a submersion has Lie algebra the kernel of its differential
> **Statement:** Let $G \subseteq GL(n; \mathbb{K})$ be a matrix Lie group. Let $M$ be a smooth manifold containing $G$ — either an open subset of the real vector space $V = \operatorname{Mat}(n \times n; \mathbb{K})$, or a smooth submanifold of $\operatorname{Mat}(n \times n; \mathbb{K})$ that is itself a matrix Lie group (as $U(n)$ is when we cut out $SU(n)$) — let $N$ be a smooth manifold, and let $\Phi : M \to N$ be smooth with $G = \Phi^{-1}(y_0)$ for some $y_0 \in N$. If the differential $d\Phi_A : T_A M \to T_{y_0} N$ is surjective for every $A \in G$, then $G$ is a smooth submanifold with $\dim G = \dim M - \dim N$, and, under the evaluation isomorphism $\mathfrak{g} \cong T_{1_n} G$, the Lie algebra is $\mathfrak{g} = \ker d\Phi_{1_n} \subseteq T_{1_n} M$, of dimension $\dim M - \dim N$. In the special case where $M$ is an open subset of $V = \operatorname{Mat}(n \times n; \mathbb{K})$ one has $T_A M = V$ for every $A$ and $\dim M = \dim_{\mathbb{R}} V$, so $\dim G = \dim_{\mathbb{R}} V - \dim N$.
>
> **Hint:** This is the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] followed by the identification $\mathfrak{g} \cong T_{1_n} G$ from [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]].
>
> **Why needed:** It is the bridge that turns each surjectivity computation into a dimension *and* an identification of $\mathfrak{g}$, closing the gap the curve argument leaves.
>
> > [!note]- Full proof
> > **Invoke the regular value theorem.** We use the following, proved in full on [[Thm - Regular Value Theorem on Manifolds]]: *if $\Phi : M \to N$ is smooth and $c \in N$ is a regular value (that is, $d\Phi_p$ is surjective for every $p \in \Phi^{-1}(c)$), then the nonempty level set $\Phi^{-1}(c)$ is a properly embedded submanifold of codimension $\dim N$, and $T_p\big(\Phi^{-1}(c)\big) = \ker d\Phi_p$ for every $p$ in it.* This is the general manifold-to-manifold statement; the domain $M$ (an open subset of $\operatorname{Mat}(n \times n; \mathbb{K})$, or a matrix Lie group embedded in it) and the codomain $N$ are both smooth manifolds, of dimensions $\dim M$ and $\dim N$ respectively.
> >
> > **Apply it to $\Phi$ at $y_0$.** By hypothesis $d\Phi_A$ is surjective for every $A \in G = \Phi^{-1}(y_0)$, so $y_0$ is a regular value of $\Phi$. The regular value theorem gives that $G$ is a submanifold of codimension $\dim N$, hence
> > $$\dim G = \dim M - \dim N \qquad \text{(codimension } = \dim N\text{)},$$
> > and, taking $p = 1_n \in G$,
> > $$T_{1_n} G = \ker d\Phi_{1_n} = \{X \in T_{1_n} M : d\Phi_{1_n}(X) = 0\} \qquad \text{(tangent space of a regular level set)}.$$
> >
> > **Identify the Lie algebra.** By [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]] — restated: *for a Lie group $G$ the evaluation map $\varepsilon : \mathfrak{g} \to T_{e} G$, $X \mapsto X_e$, is a linear isomorphism, so $\dim_{\mathbb{R}} \mathfrak{g} = \dim G$* — the Lie algebra $\mathfrak{g}$ is linearly isomorphic to $T_{1_n} G$ (with $e = 1_n$). Under this isomorphism $\mathfrak{g} = T_{1_n} G = \ker d\Phi_{1_n}$, of real dimension $\dim M - \dim N$. Since the kernel of the surjective linear map $d\Phi_{1_n} : T_{1_n} M \to T_{y_0} N$ has dimension $\dim T_{1_n} M - \dim T_{y_0} N = \dim M - \dim N$ by rank–nullity, the two dimension computations agree, as they must. $\blacksquare$

> [!note]- Lemma 3: The transported bracket on $T_{1_n} G$ is the matrix commutator
> **Statement:** For a matrix Lie group $G \subseteq GL(n; \mathbb{K})$, the Lie bracket transported from left-invariant vector fields to $T_{1_n} G$ under the evaluation isomorphism is the restriction of the matrix commutator: $[A, B] = AB - BA$ for $A, B \in T_{1_n} G \subseteq \operatorname{Mat}(n \times n; \mathbb{K})$. Consequently each of the subspaces named in the theorem is closed under the commutator.
>
> **Hint:** For $G = GL(n; \mathbb{K})$ this is proved on [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]]; for a subgroup, restrict.
>
> **Why needed:** Without it the seven subspaces would be identified as sets only, not as Lie algebras.
>
> > [!note]- Full proof
> > **The ambient case.** We use the result of [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]], restated: *for $G = GL(n; \mathbb{K})$, whose Lie algebra is $T_{1_n} GL(n; \mathbb{K}) = \operatorname{Mat}(n \times n; \mathbb{K})$, the left-invariant vector field with value $A$ at $1_n$ is $A^L\big|_g = gA$, and evaluating the Lie bracket of vector fields $[A^L, B^L]$ at $1_n$ gives the matrix commutator $AB - BA$.* Concretely, on the linear coordinates $x_{ij}$ of $\operatorname{Mat}(n\times n;\mathbb{K})$ one computes $[A^L, B^L]\big|_{1_n} = AB - BA$ from $A^L|_g = gA$, $B^L|_g = gB$ and the coordinate formula for the bracket of vector fields. Thus the transported bracket on $\mathfrak{gl}(n; \mathbb{K}) = T_{1_n} GL(n; \mathbb{K})$ is the commutator.
> >
> > **Restriction to a subgroup.** Let $G \subseteq GL(n; \mathbb{K})$ be a matrix Lie group. Its left-invariant vector fields are the restrictions to $G$ of the left-invariant fields of $GL(n; \mathbb{K})$ whose values at $1_n$ lie in $T_{1_n} G$, and the Lie bracket of vector fields is local, so the transported bracket on $T_{1_n} G$ is the restriction of the transported bracket on $T_{1_n} GL(n; \mathbb{K})$; that is, the commutator. (By [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]] the left-invariant fields of $G$ form a Lie subalgebra, so the bracket of two elements of $T_{1_n} G$ again lies in $T_{1_n} G$.)
> >
> > **Closure of the seven subspaces (verification).** Consistency requires each listed subspace to be closed under the commutator; we check the three defining conditions clause by clause. For antisymmetric $A, B$ ($A^t = -A$, $B^t = -B$): $[A,B]^t = (AB - BA)^t = B^t A^t - A^t B^t = (-B)(-A) - (-A)(-B) = BA - AB = -[A,B]$ (using $(XY)^t = Y^t X^t$), so $[A,B]$ is antisymmetric. For anti-Hermitian $A, B$ ($A^* = -A$, $B^* = -B$): $[A,B]^* = (AB - BA)^* = B^* A^* - A^* B^* = BA - AB = -[A,B]$ (using $(XY)^* = Y^* X^*$), so $[A,B]$ is anti-Hermitian. For any $A, B$: $\operatorname{tr}[A,B] = \operatorname{tr}(AB) - \operatorname{tr}(BA) = 0$ (using $\operatorname{tr}(AB) = \operatorname{tr}(BA)$), so the commutator is always traceless. Combining, each of $\mathfrak{o}(n), \mathfrak{u}(n), \mathfrak{sl}, \mathfrak{su}(n)$ is closed under the commutator, confirming they are Lie subalgebras. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the seven identifications in turn. Throughout, the strategy is Lemma 2: present the group as a regular level set of a smooth map $\Phi$ with the correct codomain, verify $d\Phi_A$ is surjective on the group, and read off $\dim G$ and $\mathfrak{g} = \ker d\Phi_{1_n}$; the bracket is the commutator by Lemma 3.
>
> **Step 0 — the identification of $\mathfrak{g}$ with $T_{1_n} G$.** For every matrix group $G$ below, we use the evaluation isomorphism $\mathfrak{g} \cong T_{1_n} G$ of [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]] — restated: *the map $X \mapsto X_{1_n}$ from left-invariant vector fields to $T_{1_n} G$ is a linear isomorphism, and $\dim_{\mathbb{R}} \mathfrak{g} = \dim G$.* We therefore compute $T_{1_n} G$ and transport the bracket, which is the commutator by Lemma 3.
>
> **Part 1 — $\mathfrak{gl}(n; \mathbb{R})$.** The general linear group $GL(n; \mathbb{R}) = \{A : \det A \neq 0\}$ is the preimage of the open set $\mathbb{R} \setminus \{0\}$ under the continuous map $\det$, hence an open subset of $\operatorname{Mat}(n \times n; \mathbb{R})$. An open subset of a vector space has tangent space at every point equal to the whole space, so
> $$T_{1_n} GL(n; \mathbb{R}) = \operatorname{Mat}(n \times n; \mathbb{R}) \qquad \text{(tangent space of an open subset of } \operatorname{Mat}(n\times n;\mathbb{R})\text{)}.$$
> Thus $\mathfrak{gl}(n; \mathbb{R}) = \operatorname{Mat}(n \times n; \mathbb{R})$, of dimension $n^2$, with bracket the commutator by Lemma 3.
>
> **Part 2 — $\mathfrak{o}(n)$ and $\mathfrak{so}(n)$.** Define $\Phi : \operatorname{Mat}(n \times n; \mathbb{R}) \to \operatorname{Sym}(n)$ by $\Phi(A) = A^t A$; this lands in $\operatorname{Sym}(n)$ because $(A^t A)^t = A^t A$. Then $O(n) = \Phi^{-1}(1_n)$. The differential at $A$ is, by the product rule,
> $$d\Phi_A(X) = X^t A + A^t X \qquad \text{(product rule applied to } A \mapsto A^t A\text{)}.$$
> **Surjectivity.** Fix $A \in O(n)$ and an arbitrary $S \in \operatorname{Sym}(n)$; put $X = \tfrac12 A S$. Then
> $$d\Phi_A\big(\tfrac12 A S\big) = \tfrac12 (AS)^t A + \tfrac12 A^t (A S) = \tfrac12 S^t A^t A + \tfrac12 (A^t A) S = \tfrac12 S^t + \tfrac12 S = S \qquad \text{(since } A^t A = 1_n \text{ as } A \in O(n)\text{, and } S^t = S\text{)}.$$
> So $d\Phi_A$ is surjective onto $\operatorname{Sym}(n)$ for every $A \in O(n)$, and $1_n$ is a regular value. By Lemma 2, $O(n)$ is a submanifold with
> $$\dim O(n) = \dim \operatorname{Mat}(n \times n; \mathbb{R}) - \dim \operatorname{Sym}(n) = n^2 - \tfrac{n(n+1)}{2} = \tfrac{n(n-1)}{2} \qquad \text{(Lemma 2, then } \dim\operatorname{Mat} = n^2,\ \dim\operatorname{Sym}(n) = \tfrac{n(n+1)}{2}\text{)},$$
> and
> $$\mathfrak{o}(n) = T_{1_n} O(n) = \ker d\Phi_{1_n} = \{X : X^t \cdot 1_n + 1_n \cdot X = 0\} = \{X : X^t + X = 0\} \qquad \text{(evaluating } d\Phi \text{ at } A = 1_n\text{)}.$$
> The antisymmetric matrices have zero diagonal and free strictly-upper entries, so their dimension is $n(n-1)/2$, matching $\dim O(n)$ as required. For $SO(n)$: the restriction $\det : O(n) \to \{\pm 1\}$ is continuous with discrete codomain, so $SO(n) = \det^{-1}(1)$ is open and closed in $O(n)$; an open subset shares tangent spaces, hence
> $$\mathfrak{so}(n) = T_{1_n} SO(n) = T_{1_n} O(n) = \mathfrak{o}(n) \qquad \text{(} SO(n) \text{ open in } O(n)\text{)}.$$
> Equivalently $\mathfrak{so}(n) = \mathfrak{o}(n) \cap \mathfrak{sl}(n; \mathbb{R}) = \mathfrak{o}(n)$, since every antisymmetric matrix is traceless (its diagonal vanishes). The bracket is the commutator by Lemma 3, and $\mathfrak{o}(n)$ is commutator-closed by the antisymmetric case of Lemma 3.
>
> **Part 3 — $\mathfrak{sl}(n; \mathbb{R})$.** Define $\Phi = \det : \operatorname{Mat}(n \times n; \mathbb{R}) \to \mathbb{R}$, so $SL(n; \mathbb{R}) = \det^{-1}(1)$. By Lemma 1, for $A \in SL(n; \mathbb{R})$ (so $\det A = 1$),
> $$d(\det)_A(X) = \det(A)\,\operatorname{tr}(A^{-1}X) = \operatorname{tr}(A^{-1} X) \qquad \text{(Lemma 1, general-point form, with } \det A = 1\text{)}.$$
> **Surjectivity.** Given a target $t \in \mathbb{R}$, put $X = \tfrac{t}{n} A$; then $d(\det)_A(X) = \operatorname{tr}(A^{-1}\cdot \tfrac{t}{n} A) = \tfrac{t}{n}\operatorname{tr}(1_n) = \tfrac{t}{n}\cdot n = t$. So $d(\det)_A$ is surjective onto $\mathbb{R}$ for every $A \in SL(n; \mathbb{R})$, and $1$ is a regular value. By Lemma 2,
> $$\dim SL(n; \mathbb{R}) = n^2 - 1, \qquad \mathfrak{sl}(n; \mathbb{R}) = \ker d(\det)_{1_n} = \{X : \operatorname{tr} X = 0\} \qquad \text{(Lemma 1 at } A = 1_n \text{ gives } d(\det)_{1_n} = \operatorname{tr}\text{)}.$$
> The traceless matrices are the kernel of the surjective linear functional $\operatorname{tr}$, of dimension $n^2 - 1$, matching. The bracket is the commutator (Lemma 3), and the trace of any commutator is zero, so $\mathfrak{sl}(n; \mathbb{R})$ is closed under it.
>
> **Part 4 — $\mathfrak{u}(n)$.** Define $\Phi : \operatorname{Mat}(n \times n; \mathbb{C}) \to \operatorname{Herm}(n)$ by $\Phi(A) = A^* A$; this lands in $\operatorname{Herm}(n)$ because $(A^* A)^* = A^* A$. Here we regard $\operatorname{Mat}(n \times n; \mathbb{C})$ as the real vector space $\mathbb{R}^{2n^2}$ and $\operatorname{Herm}(n)$ as the real vector space of dimension $n^2$. Then $U(n) = \Phi^{-1}(1_n)$, and the (real) differential at $A$ is
> $$d\Phi_A(X) = X^* A + A^* X \qquad \text{(product rule; this is } \mathbb{R}\text{-linear in } X \text{ but not } \mathbb{C}\text{-linear, because of } X^*\text{)}.$$
> **Surjectivity.** Fix $A \in U(n)$ and an arbitrary $H \in \operatorname{Herm}(n)$; put $X = \tfrac12 A H$. Then
> $$d\Phi_A\big(\tfrac12 A H\big) = \tfrac12 (AH)^* A + \tfrac12 A^* (A H) = \tfrac12 H^* A^* A + \tfrac12 (A^* A) H = \tfrac12 H^* + \tfrac12 H = H \qquad \text{(since } A^* A = 1_n \text{ as } A \in U(n)\text{, and } H^* = H\text{)}.$$
> So $d\Phi_A$ is surjective onto $\operatorname{Herm}(n)$ for every $A \in U(n)$, and $1_n$ is a regular value. By Lemma 2,
> $$\dim U(n) = \dim_{\mathbb{R}}\operatorname{Mat}(n \times n; \mathbb{C}) - \dim_{\mathbb{R}}\operatorname{Herm}(n) = 2n^2 - n^2 = n^2 \qquad \text{(Lemma 2, then } \dim_{\mathbb{R}}\operatorname{Mat}(n\times n;\mathbb{C}) = 2n^2,\ \dim_{\mathbb{R}}\operatorname{Herm}(n) = n^2\text{)},$$
> and
> $$\mathfrak{u}(n) = T_{1_n} U(n) = \ker d\Phi_{1_n} = \{X : X^* + X = 0\} \qquad \text{(evaluating } d\Phi \text{ at } A = 1_n\text{)},$$
> the anti-Hermitian matrices. Their real dimension is $n^2$: the $n$ diagonal entries are purely imaginary ($n$ real parameters) and the $n(n-1)/2$ strictly-upper entries are free complex numbers determining the lower ones by $x_{ji} = -\bar{x}_{ij}$ ($n(n-1)$ real parameters), totalling $n + n(n-1) = n^2$, matching $\dim U(n)$. The bracket is the commutator (Lemma 3), and $\mathfrak{u}(n)$ is commutator-closed by the anti-Hermitian case of Lemma 3.
>
> **Part 5 — $\mathfrak{sl}(n; \mathbb{C})$.** Define $\Phi = \det : \operatorname{Mat}(n \times n; \mathbb{C}) \to \mathbb{C}$, a $\mathbb{C}$-linear-differentiable (holomorphic) map which we regard as a smooth map of real vector spaces $\mathbb{R}^{2n^2} \to \mathbb{R}^2$. Then $SL(n; \mathbb{C}) = \det^{-1}(1)$, and by Lemma 1 (whose expansion is valid over $\mathbb{C}$),
> $$d(\det)_A(X) = \det(A)\,\operatorname{tr}(A^{-1} X) = \operatorname{tr}(A^{-1} X) \qquad \text{for } A \in SL(n; \mathbb{C}) \text{ (so } \det A = 1\text{)}.$$
> **Surjectivity.** This map is $\mathbb{C}$-linear in $X$ and nonzero (it sends $X = A$ to $\operatorname{tr}(1_n) = n \neq 0$), so as a $\mathbb{C}$-linear map to $\mathbb{C}$ it is surjective; concretely, for target $z \in \mathbb{C}$ put $X = \tfrac{z}{n} A$, giving $\operatorname{tr}(A^{-1}\cdot\tfrac{z}{n} A) = z$. Regarded over $\mathbb{R}$, its image is all of $\mathbb{C} = \mathbb{R}^2$. So $1$ is a regular value. By Lemma 2,
> $$\dim_{\mathbb{R}} SL(n; \mathbb{C}) = 2n^2 - 2, \qquad \mathfrak{sl}(n; \mathbb{C}) = \ker d(\det)_{1_n} = \{X \in \operatorname{Mat}(n \times n; \mathbb{C}) : \operatorname{tr} X = 0\} \qquad \text{(Lemma 2 with } \dim_{\mathbb{R}}\operatorname{Mat} = 2n^2,\ \dim_{\mathbb{R}}\mathbb{C} = 2\text{; Lemma 1 at } A = 1_n \text{ gives } d(\det)_{1_n} = \operatorname{tr}\text{)}.$$
> The complex-traceless matrices form a complex subspace of complex codimension $1$, hence complex dimension $n^2 - 1$ and real dimension $2n^2 - 2$, matching. The bracket is the commutator (Lemma 3), and the trace of a commutator vanishes.
>
> **Part 6 — $\mathfrak{su}(n)$.** We have $SU(n) = U(n) \cap SL(n; \mathbb{C}) = \{A \in U(n) : \det A = 1\}$. On the manifold $U(n)$ the determinant takes values in the unit circle $U(1) = \{z \in \mathbb{C} : |z| = 1\}$, since $|\det A|^2 = \det A \, \overline{\det A} = \det A \, \det(A^*) = \det(A^* A) = \det(1_n) = 1$ for $A \in U(n)$ (using $\det(A^*) = \overline{\det A}$ and multiplicativity). So the restriction $\psi := \det|_{U(n)} : U(n) \to U(1)$ is a smooth map between manifolds, and $SU(n) = \psi^{-1}(1)$. **The differential of $\psi$ at $1_n$** is the restriction of $d(\det)_{1_n} = \operatorname{tr}$ (Lemma 1) to $T_{1_n} U(n) = \mathfrak{u}(n)$:
> $$d\psi_{1_n} : \mathfrak{u}(n) \to T_1 U(1) = \mathrm{i}\mathbb{R}, \qquad d\psi_{1_n}(X) = \operatorname{tr} X.$$
> This is well-targeted: for anti-Hermitian $X$ ($X^* = -X$) each diagonal entry satisfies $x_{ii} = -\bar{x}_{ii}$, hence is purely imaginary, so $\operatorname{tr} X = \sum_i x_{ii} \in \mathrm{i}\mathbb{R} = T_1 U(1)$. **Surjectivity.** Given $\mathrm{i}t \in \mathrm{i}\mathbb{R}$, put $X = \tfrac{\mathrm{i}t}{n} 1_n$, which is anti-Hermitian ($X^* = -\tfrac{\mathrm{i}t}{n} 1_n = -X$), and $\operatorname{tr} X = \tfrac{\mathrm{i}t}{n}\cdot n = \mathrm{i}t$. So $d\psi_{1_n}$ is surjective onto $T_1 U(1) = \mathrm{i}\mathbb{R}$. By left-translation $\psi$ is a submersion at every point of $SU(n)$ (it is a homomorphism, so $d\psi_A = d\psi_{1_n} \circ (dL_{A^{-1}})_A$ up to the identification $T_1 U(1) \cong T_{\psi(A)} U(1)$, and $L_{A^{-1}}$ is a diffeomorphism), so $1$ is a regular value of $\psi$. Applying the regular value theorem to $\psi : U(n) \to U(1)$ (Lemma 2 with domain the manifold $U(n)$ and codomain $U(1)$),
> $$\dim SU(n) = \dim U(n) - \dim U(1) = n^2 - 1 \qquad \text{(Lemma 2 with } \dim U(n) = n^2 \text{ from Part 4 and } \dim U(1) = 1\text{)},$$
> and
> $$\mathfrak{su}(n) = T_{1_n} SU(n) = \ker d\psi_{1_n} = \{X \in \mathfrak{u}(n) : \operatorname{tr} X = 0\} = \{X : X^* = -X,\ \operatorname{tr} X = 0\}.$$
> Note that "$\operatorname{tr} X = 0$" is a *single* real condition on $\mathfrak{u}(n)$, because $\operatorname{tr} X$ is already purely imaginary there; this is why the codimension drops by $1$, not $2$, and $\dim \mathfrak{su}(n) = n^2 - 1$. The bracket is the commutator (Lemma 3), under which $\mathfrak{su}(n)$ is closed since the commutator preserves both anti-Hermiticity and tracelessness (Lemma 3). In particular $\dim \mathfrak{su}(2) = 3$.
>
> **Part 7 — $\mathfrak{sp}(1)$.** The unit quaternions are $Sp(1) = \{q \in \mathbb{H} : |q|^2 = 1\}$, the level set at $1$ of the norm map $N : \mathbb{H} \to \mathbb{R}$, $N(q) = q\bar{q} = a^2 + b^2 + c^2 + d^2$, where $q = a + b\mathrm{i} + c\mathrm{j} + d\mathrm{k}$ and we identify $\mathbb{H} = \mathbb{R}^4$. The map $N$ is the standard quadratic form, with differential $dN_q(v) = 2\langle q, v\rangle$ (Euclidean inner product); for $q \neq 0$ this is a surjective functional $\mathbb{R}^4 \to \mathbb{R}$ (it sends $v = q$ to $2|q|^2 \neq 0$), so every nonzero value, in particular $1$, is a regular value. By Lemma 2,
> $$\dim Sp(1) = 4 - 1 = 3, \qquad \mathfrak{sp}(1) = T_1 Sp(1) = \ker dN_1.$$
> Computing the kernel at $q = 1$ (i.e. $a = 1$, $b = c = d = 0$): for a curve $c(s) \in Sp(1)$ with $c(0) = 1$, differentiating $c(s)\overline{c(s)} = 1$ gives
> $$0 = \dot{c}(0)\,\overline{c(0)} + c(0)\,\dot{\overline{c}}(0) = \dot{c}(0) + \overline{\dot{c}(0)} = 2\operatorname{Re}\dot{c}(0) \qquad \text{(} c(0) = \overline{c(0)} = 1\text{, and } \dot{\overline{c}}(0) = \overline{\dot{c}(0)}\text{)},$$
> so $\mathfrak{sp}(1) = \{X \in \mathbb{H} : \operatorname{Re} X = 0\} = \operatorname{Im}\mathbb{H} = \operatorname{span}_{\mathbb{R}}\{\mathrm{i}, \mathrm{j}, \mathrm{k}\}$, of dimension $3$. **The bracket.** Realise $\mathbb{H}$ as a real subalgebra of $\operatorname{Mat}(2 \times 2; \mathbb{C})$ by $a + b\mathrm{i} + c\mathrm{j} + d\mathrm{k} \mapsto \left(\begin{smallmatrix} a + b\mathrm{i} & -c - d\mathrm{i} \\ c - d\mathrm{i} & a - b\mathrm{i}\end{smallmatrix}\right)$, under which $Sp(1)$ becomes a matrix group (indeed $Sp(1) \cong SU(2)$, since a unit quaternion maps to a matrix $\left(\begin{smallmatrix} z & -\bar{w} \\ w & \bar{z}\end{smallmatrix}\right)$ with $|z|^2 + |w|^2 = 1$, which is the general element of $SU(2)$); then $\mathfrak{sp}(1)$ becomes a matrix Lie algebra and its bracket is the commutator by Lemma 3. Computed intrinsically, for purely imaginary quaternions $u, v \in \operatorname{Im}\mathbb{H} \cong \mathbb{R}^3$ the quaternion product is $uv = -\langle u, v\rangle + u \times v$ (real part $-\langle u,v\rangle$, imaginary part the cross product), so
> $$[u, v] = uv - vu = (u \times v) - (v \times u) = 2\,(u \times v) \qquad \text{(the real parts } -\langle u,v\rangle \text{ cancel; } v \times u = -u \times v\text{)}.$$
> Thus $\mathfrak{sp}(1) = (\operatorname{Im}\mathbb{H}, [\cdot,\cdot]) \cong (\mathbb{R}^3, 2\times)$, which is isomorphic as a Lie algebra to $\mathfrak{su}(2)$ and to $\mathfrak{so}(3)$.
>
> **Conclusion.** All seven Lie algebras have been identified as the stated matrix subspaces, each with its dimension derived from the regular value theorem (Lemma 2, fed by Lemma 1) and its bracket shown to be the commutator (Lemma 3); the closure of each subspace under the commutator was verified in Lemma 3, so each is a genuine Lie subalgebra, and in every case $\dim_{\mathbb{R}} \mathfrak{g} = \dim G$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The symplectic group in Hamiltonian mechanics.** The linear symplectic group $Sp(2m; \mathbb{R}) = \{A : A^t J A = J\}$, with $J = \left(\begin{smallmatrix} 0 & 1_m \\ -1_m & 0 \end{smallmatrix}\right)$, is the group of linear changes of coordinates preserving the canonical symplectic form on phase space. The theorem's method applies verbatim: $\Phi(A) = A^t J A$ lands in the antisymmetric matrices, its differential is $X^t J A + A^t J X$, and verifying surjectivity of that differential (for a target antisymmetric $B$, the matrix $X = \tfrac12 A J^{-1} B$ maps to $B$) yields $\mathfrak{sp}(2m; \mathbb{R}) = \{X : X^t J + J X = 0\}$ of dimension $m(2m+1)$. This is non-obvious because the constraint mixes transpose and a fixed antisymmetric $J$, so the correct codomain is the antisymmetric — not symmetric — matrices; getting the $\pm$-symmetry type right is exactly the lesson of "What Makes This Hard".

**Lorentz transformations in special relativity.** The Lorentz group $O(1,3) = \{A : A^t \eta A = \eta\}$ with $\eta = \operatorname{diag}(-1,1,1,1)$ is the isometry group of Minkowski spacetime. Its Lie algebra $\mathfrak{so}(1,3) = \{X : X^t \eta + \eta X = 0\}$ is six-dimensional (three boosts and three rotations), obtained by the same differentiation of $A^t \eta A = \eta$ at the identity. The application is non-obvious because the indefinite metric $\eta$ replaces the identity, yet the structure of the argument is identical; comparing $\mathfrak{so}(1,3)$ with the compact $\mathfrak{so}(4)$ shows how the signature of the form, not just the dimension, shapes the algebra.

**Density matrices and the trace constraint in quantum mechanics.** In quantum information the special unitary group $SU(n)$ is the group of quantum gates on an $n$-level system, and its Lie algebra $\mathfrak{su}(n)$ — the traceless anti-Hermitian matrices — is the space of Hamiltonians (up to the factor $\mathrm{i}$): a physical Hamiltonian $H$ is Hermitian, and $\mathrm{i}H$ generates the unitary evolution $e^{-\mathrm{i}Ht}$. The subtle point that "$\operatorname{tr} = 0$" is a single real condition on anti-Hermitian matrices is the statement that removing the global phase (the $U(1)$ factor with generator $\mathrm{i}1_n$) costs exactly one real dimension, so $\dim \mathfrak{su}(n) = n^2 - 1$ counts the physically distinct generators. This is where the delicate part of Part 6 has direct physical meaning.

---

# Bridges

- **The regular value theorem as the engine.** The whole theorem is seven applications of [[Thm - Regular Value Theorem on Manifolds]]. That theorem says a smooth map with a regular value has a submanifold as its level set, with tangent space the kernel of the differential; here the map is a matrix equation and the "kernel of the differential" *is* the Lie algebra. The construction of $O(n)$ and $SL(n;\mathbb{R})$ as regular level sets, worked in detail, appears on [[Ex - The Orthogonal Group as a Regular Level Set]] and [[Ex - The Special Linear Group is a Submanifold of GL(n)]]; this page reuses those constructions and reads off the tangent space at the identity.

- **From tangent space to Lie algebra.** The passage from "$T_{1_n} G$ is a linear subspace" to "$\mathfrak{g}$ is a Lie algebra" runs through [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]], which builds the evaluation isomorphism $\mathfrak{g} \cong T_e G$, and [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]], which computes the transported bracket as the matrix commutator. Together they let one work entirely with matrices and forget the vector-field origin of the bracket.

- **The exponential map runs the identification backward.** Where this page linearises a group into its algebra by differentiating, the matrix exponential $\exp(X) = \sum_{k \geq 0} X^k/k!$ integrates the algebra back into the group: for each classical group, $\exp$ maps the Lie algebra found here into the group (e.g. $\exp$ of an antisymmetric matrix is orthogonal, $\exp$ of an anti-Hermitian matrix is unitary). This is the content of the later page **Thm - The Exponential Map of a Matrix Group is the Matrix Exponential**, which closes the loop begun here.

- **The isomorphism $Sp(1) \cong SU(2)$.** Part 7 realises the unit quaternions inside $\operatorname{Mat}(2 \times 2; \mathbb{C})$ and identifies them with $SU(2)$; on Lie algebras this is the isomorphism $\mathfrak{sp}(1) \cong \mathfrak{su}(2)$, both three-dimensional with bracket the (doubled) cross product. This underlies the spin double cover $Sp(1) = SU(2) \to SO(3)$ and the drilling of $Sp(1) \cong SU(2)$ on [[Def - Classical Matrix Groups]].

---

# Unlocked by This

> [!tip] Ad-Invariant Inner Product on a Compact Lie Algebra *(from Chern–Weil theory)*
> On $\mathfrak{su}(n)$ the form $\langle X, Y\rangle = -\operatorname{tr}(XY)$ is a positive-definite $\operatorname{Ad}$-invariant inner product, because $-\operatorname{tr}(X^2) = \operatorname{tr}(X^* X) \geq 0$ for anti-Hermitian $X$. This is the inner product that normalises the Yang–Mills functional and the invariant polynomials of chapter VI. See **Def - Ad-Invariant Polynomial**.

> [!tip] The Dimension Constants of the Series *(from gauge theory)*
> The numbers proved here — $\dim U(1) = 1$, $\dim SU(2) = 3$, $\dim SO(3) = 3$, $\dim SU(n) = n^2 - 1$ — recur as the fibre dimensions of every structure group. In particular $\mathfrak{u}(1) = \mathrm{i}\mathbb{R}$ is the target of the electromagnetic connection and $\mathfrak{su}(2)$ the target of the instanton connections. See **Def - Connection on a Principal Bundle**.
