---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)"
  - "Def - Weyl Spinors (Left and Right Handed)"
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
tags: [physics, special-relativity]
---

# Problem Statement

A null direction on an observer's [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|celestial sphere]] is encoded by a spinor $\xi \in \mathbb{C}^2$ with $\underline X = \xi\xi^\dagger$, and its stereographic coordinate is $\omega = \xi_1/\xi_2 \in \mathbb{C}\cup\{\infty\}$.

1. Show that under a Lorentz transformation $A = \begin{pmatrix}a&b\\c&d\end{pmatrix} \in SL(2,\mathbb{C})$, the four-vector transformation $\underline X \mapsto A\underline X A^\dagger$ is equivalent to the spinor transformation $\xi \mapsto A\xi$, and deduce the Möbius action $\omega \mapsto \omega' = (a\omega + b)/(c\omega + d)$.
2. Verify that the composition of two Lorentz transformations corresponds to the composition of their Möbius maps, and that $A$ and $-A$ give the same Möbius map, so the faithful group is $PSL(2,\mathbb{C}) = SL(2,\mathbb{C})/\{\pm I\}$.
3. Show that a rotation about the line of sight (the $z$-axis) acts on the sky by $\omega \mapsto e^{-i\theta}\omega$ (a rigid rotation of the Riemann sphere), and identify its two fixed points with the forward and backward poles.

**Recall:**

![[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)#Statement]]

A [[Def - Weyl Spinors (Left and Right Handed)|left Weyl spinor]] transforms by $\xi \mapsto A\xi$. A **Möbius transformation** is a map $\omega \mapsto (a\omega+b)/(c\omega+d)$ with $ad - bc \neq 0$; these are the holomorphic automorphisms of the Riemann sphere $\mathbb{C}\cup\{\infty\}$. The [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|correspondence]] sends a null $X$ to a rank-one $\underline X = \xi\xi^\dagger$.

---

# Convergent Strategy

**Problem class.** A *push-down computation*: showing that the linear $SL(2,\mathbb{C})$ action on spinors descends to the Möbius (fractional-linear) action on their ratio. The [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map#Problem-Solving Strategy|topic strategy]] says that for questions about what an observer sees, you parametrise a null direction by a spinor and read the Lorentz action as a Möbius map; this exercise establishes that reading.

**Assumption pattern.** The key input is that the four-vector is *null*, so $\underline X = \xi\xi^\dagger$ factors and the four-vector law $A\underline X A^\dagger = (A\xi)(A\xi)^\dagger$ collapses to the single-factor spinor law $\xi \mapsto A\xi$. The signpost is "null direction": only for null vectors does the rank-one factorisation exist, making the Möbius structure available.

**Theorem routing.** This is the computational core of [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)]] (its Lemma 3), drawing on the [[Def - Weyl Spinors (Left and Right Handed)|Weyl-spinor]] transformation law and the [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|double cover]] for the $PSL(2,\mathbb{C})$ identification.

**Key decision point.** The crux is dividing through by $\xi_2$: the ratio $\omega = \xi_1/\xi_2$ transforms because the *new* components $(a\xi_1 + b\xi_2, c\xi_1 + d\xi_2)$ have a ratio that, upon dividing numerator and denominator by $\xi_2$, becomes $(a\omega + b)/(c\omega + d)$. Recognising that the ratio of two linear combinations of the components is automatically a fractional-linear function of the ratio is the single insight; everything else is the consequence.

---

# Legal Operations Used

1. **Parametrise a null direction by a spinor and project stereographically** (operation 7 from the topic page): the exercise factors $\underline X = \xi\xi^\dagger$ and forms $\omega = \xi_1/\xi_2$.

2. **Read $\xi \mapsto A\xi$ as the spinor law** (operation 7 / warning 3 from the topic page): part 1 deduces the single-factor spinor law from the two-factor four-vector law via the rank-one factorisation.

3. **Lift to the two preimages $\pm A$** (operation 6 from the topic page): part 2 shows $A$ and $-A$ give the same Möbius map, so the action factors through $PSL(2,\mathbb{C})$.

---

# Hints

> [!note]- Hint 1
> Since $\underline X = \xi\xi^\dagger$, $A\underline X A^\dagger = A\xi\xi^\dagger A^\dagger = (A\xi)(A\xi)^\dagger$. So the transformed null vector is $\xi' = A\xi$ — the spinor transforms by a *single* factor of $A$.

> [!note]- Hint 2
> With $\xi' = A\xi$, the components are $\xi_1' = a\xi_1 + b\xi_2$, $\xi_2' = c\xi_1 + d\xi_2$. Form $\omega' = \xi_1'/\xi_2'$ and divide top and bottom by $\xi_2$ to express it in terms of $\omega = \xi_1/\xi_2$.

> [!note]- Hint 3
> Composition: if $\xi \mapsto A\xi \mapsto B(A\xi) = (BA)\xi$, the Möbius map of $BA$ is the composition of those of $B$ and $A$ — fractional-linear maps compose like matrix multiplication. For $A = -I$: $(-I)\xi = -\xi$, and $\omega = (-\xi_1)/(-\xi_2) = \xi_1/\xi_2 = \omega$, unchanged.

> [!note]- Hint 4
> A $z$-rotation is $A = \mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2})$, so $\omega' = (e^{-i\theta/2}\xi_1)/(e^{i\theta/2}\xi_2) = e^{-i\theta}\omega$. The fixed points are $\omega = 0$ and $\omega = \infty$ (the south and north poles, $\theta_{\text{polar}} = \pi$ and $0$).

---

# Solution

The exercise establishes that the Lorentz action on the sky is Möbius. The plan: factor the null Hermitian matrix to extract the single-factor spinor law; divide the ratio to get the fractional-linear map; check composition and the $\pm I$ redundancy; and run the rotation example to see a rigid sphere rotation as a special Möbius map.

**Step 1: $\underline X \mapsto A\underline X A^\dagger$ becomes $\xi \mapsto A\xi$, hence $\omega \mapsto (a\omega+b)/(c\omega+d)$.**

> [!note]- Derivation
> A null direction has $\underline X = \xi\xi^\dagger$ (rank one, from [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|Lemma 1]]). Under the spinor map,
> $$A\underline X A^\dagger = A(\xi\xi^\dagger)A^\dagger = (A\xi)(\xi^\dagger A^\dagger) = (A\xi)(A\xi)^\dagger,$$
> using $(A\xi)^\dagger = \xi^\dagger A^\dagger$. So the transformed null vector is $\underline X' = (A\xi)(A\xi)^\dagger$, i.e. the spinor transforms by $\xi' = A\xi$ — a **single** factor of $A$, the [[Def - Weyl Spinors (Left and Right Handed)|left Weyl spinor]] law. (The phase ambiguity $\xi \sim e^{i\beta}\xi$ is preserved, since $A(e^{i\beta}\xi) = e^{i\beta}(A\xi)$.)
>
> The components are $\xi_1' = a\xi_1 + b\xi_2$, $\xi_2' = c\xi_1 + d\xi_2$, so the stereographic coordinate transforms as
> $$\omega' = \frac{\xi_1'}{\xi_2'} = \frac{a\xi_1 + b\xi_2}{c\xi_1 + d\xi_2} = \frac{a(\xi_1/\xi_2) + b}{c(\xi_1/\xi_2) + d} = \frac{a\omega + b}{c\omega + d},$$
> dividing numerator and denominator by $\xi_2$. This is the **Möbius transformation** with matrix $A$. So the Lorentz transformation acts on the celestial sphere by the Möbius map of its $SL(2,\mathbb{C})$ matrix.

**Step 2: Composition and the $PSL(2,\mathbb{C})$ identification.**

> [!note]- Derivation
> *Composition.* Applying $A$ then $B$ to the spinor: $\xi \mapsto A\xi \mapsto B(A\xi) = (BA)\xi$. The Möbius map of the composite is therefore the Möbius map of $BA$, and one checks directly that this equals the composition of the Möbius maps of $B$ and $A$:
> $$\omega \xmapsto{A} \frac{a\omega+b}{c\omega+d} \xmapsto{B} \frac{a'\frac{a\omega+b}{c\omega+d}+b'}{c'\frac{a\omega+b}{c\omega+d}+d'} = \frac{(a'a + b'c)\omega + (a'b + b'd)}{(c'a + d'c)\omega + (c'b + d'd)},$$
> whose matrix $\begin{pmatrix}a'a+b'c & a'b+b'd \\ c'a+d'c & c'b+d'd\end{pmatrix} = BA$ — the maps compose exactly as the matrices multiply. So $A \mapsto (\text{Möbius map of } A)$ is a homomorphism.
>
> *Redundancy.* For $A = -I$: $\xi \mapsto -\xi$, so $\omega = (-\xi_1)/(-\xi_2) = \xi_1/\xi_2 = \omega$ — the identity Möbius map. More generally, $A$ and $-A$ give the same Möbius map, since $(-a\omega - b)/(-c\omega - d) = (a\omega+b)/(c\omega+d)$. So the kernel of the Möbius action is $\{\pm I\}$, and the faithful group of sky transformations is
> $$PSL(2,\mathbb{C}) = SL(2,\mathbb{C})/\{\pm I\} \cong SO^+(1,3)$$
> by the [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|double cover]]. The restricted Lorentz group *is* the Möbius (conformal) group of the celestial sphere.

**Step 3: A $z$-rotation is the rigid sphere rotation $\omega \mapsto e^{-i\theta}\omega$.**

> [!note]- Derivation
> A rotation by $\theta$ about the line of sight ($z$-axis) is $A = \exp(-\tfrac{i\theta}{2}\sigma_3) = \mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2})$, so $a = e^{-i\theta/2}$, $d = e^{i\theta/2}$, $b = c = 0$. The Möbius map is
> $$\omega' = \frac{a\omega + b}{c\omega + d} = \frac{e^{-i\theta/2}\omega}{e^{i\theta/2}} = e^{-i\theta}\omega.$$
> This is a *rotation* of the Riemann sphere about its polar axis: in terms of the sky angles $\omega = e^{i\phi}\cot(\theta_{\text{polar}}/2)$, it sends $\phi \mapsto \phi - \theta$ at fixed polar angle — exactly a rigid rotation of the celestial sphere by $\theta$ about the line of sight, as it must be. The **fixed points** are $\omega = 0$ ($\theta_{\text{polar}} = \pi$, the backward pole, directly behind) and $\omega = \infty$ ($\theta_{\text{polar}} = 0$, the forward pole, directly ahead) — the two points on the line of sight, which a rotation about that line leaves fixed. (These are the two invariant null directions of the rotation, the images of [[Thm - Existence of Null Eigenvectors of a Restricted Lorentz Transformation|the null eigenvectors]] on the sphere.)

> [!note]- Complete formal solution
> Since a null direction has $\underline X = \xi\xi^\dagger$, the four-vector law $A\underline X A^\dagger = (A\xi)(A\xi)^\dagger$ reduces to the spinor law $\xi \mapsto A\xi$; the ratio $\omega = \xi_1/\xi_2$ then transforms by $\omega \mapsto (a\omega+b)/(c\omega+d)$ (divide by $\xi_2$). Composition $\xi \mapsto (BA)\xi$ makes the Möbius maps compose as the matrices multiply, and $A, -A$ give the same map, so the faithful group is $PSL(2,\mathbb{C}) \cong SO^+(1,3)$. A $z$-rotation $A = \mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2})$ gives $\omega \mapsto e^{-i\theta}\omega$, a rigid rotation of the Riemann sphere about its poles $\omega = 0, \infty$ (the forward and backward line-of-sight directions), which are its fixed points. $\blacksquare$

---

# Key Takeaways

**A null vector is the only kind that becomes a single spinor, and that is why the sky is Möbius.** The factorisation $\underline X = \xi\xi^\dagger$ exists precisely for null (rank-one) Hermitian matrices, and it is what converts the two-factor four-vector law into the one-factor spinor law $\xi \mapsto A\xi$. A timelike or spacelike vector has full-rank $\underline X$ and admits no such factorisation, so its transformation stays genuinely two-factor and is *not* fractional-linear. The lesson is that the elegant Möbius structure of the celestial sphere is a special feature of *null* directions — of light — and not of spacetime points in general; the sphere of light rays is $\mathbb{C}\mathrm{P}^1$ exactly because a light ray is a spinor up to scale. Whenever a problem restricts attention to null directions or light rays, expect the spinor/Möbius machinery to apply; whenever it concerns general four-vectors, it does not.

**The ratio of two linear combinations is automatically fractional-linear — this is the whole reason Lorentz acts by Möbius.** The single computational fact behind the entire celestial-sphere story is that if $\xi$ transforms linearly, $\xi' = A\xi$, then the ratio $\omega = \xi_1/\xi_2$ transforms fractional-linearly, because the ratio of $a\xi_1 + b\xi_2$ to $c\xi_1 + d\xi_2$ is $(a\omega + b)/(c\omega + d)$ after dividing by $\xi_2$. This is a general principle: *projectivising a linear action always produces a fractional-linear (projective) action*, and the group $GL$ acting linearly on $\mathbb{C}^2$ becomes $PGL$ acting on $\mathbb{C}\mathrm{P}^1$ by Möbius maps. Recognising this lets you predict the Möbius action without computation — it is forced by the projective structure — and it is the same principle by which projective transformations act on projective space throughout algebraic geometry. The reusable trigger: a linear action on a vector space induces a fractional-linear action on the lines through the origin.

**The restricted Lorentz group is the conformal group of the two-sphere — relativistic kinematics and 2D conformal geometry are one subject.** The endpoint of this exercise is the identification $PSL(2,\mathbb{C}) \cong SO^+(1,3)$, which says the group of Lorentz transformations acting on the sky is *exactly* the group of conformal (angle-preserving) automorphisms of $S^2 = \mathbb{C}\mathrm{P}^1$. This is not an analogy but an isomorphism, and it is a low-dimensional coincidence: the conformal group of $S^n$ is $SO^+(1, n+1)$, and at $n = 2$ this is the Lorentz group of four-dimensional spacetime. The consequence is that any fact about Möbius transformations — that they preserve circles, that they have one or two fixed points, that they form the holomorphic automorphisms of the Riemann sphere — is simultaneously a fact about how observers see the universe. This is what makes aberration conformal (the [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|circle theorem]]), and it is the kinematic backbone of the modern celestial-holography programme, where the conformal symmetry of the sky becomes the conformal symmetry of a putative dual field theory. The transferable insight is that whenever a physical symmetry group coincides with a geometric automorphism group, the two theories become translations of each other, and results flow freely in both directions.
