---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Spinor Map and SL(2,C)"
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
  - "Def - Lie Algebra sl(2,C) and the Exponential Map"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus. $SU(2) = \{A \in SL(2,\mathbb{C}) : A^\dagger = A^{-1}\}$ is the special unitary group; $\mathscr{S}$ is the [[Def - The Spinor Map and SL(2,C)|spinor map]] restricted to it. $\boldsymbol\sigma = (\sigma_1,\sigma_2,\sigma_3)$ are the [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|Pauli matrices]]; $\mathbf n = (n^1,n^2,n^3)$ is a Euclidean unit vector and $\mathbf n\cdot\boldsymbol\sigma = n^i\sigma_i$. $S^3 = \{x \in \mathbb{R}^4 : |x| = 1\}$ is the unit three-sphere; $e_0$ is the time direction in spacetime; $\mathbb{H}$ are the quaternions. Full registry on [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].

---

# Statement

> **Theorem (the spinor map SU(2) → SO(3)).** As a real manifold the special unitary group is the three-sphere, $SU(2) \cong S^3$. The spinor map restricts to a surjective two-to-one homomorphism
> $$ \mathscr{S} : SU(2) \longrightarrow SO(3), $$
> whose image is exactly the spatial rotations (a unitary $A$ fixes the time direction $e_0$). Explicitly, parametrising
> $$ A = \cos\tfrac\theta2\, I - \sin\tfrac\theta2\,(n^j i\sigma_j) = \exp\!\Big(-\tfrac{i\theta}{2}\,\mathbf n\cdot\boldsymbol\sigma\Big), \qquad \theta \in [0,2\pi],\ |\mathbf n| = 1, $$
> the image $\mathscr{S}(A)$ is the rotation of angle $\theta$ about the axis $\mathbf n$ (Rodrigues' formula). The kernel is $\{\pm I\}$, so $SO(3) \cong SU(2)/\{\pm I\}$, with $\theta = 0$ giving $A = I$ and $\theta = 2\pi$ giving $A = -I$, both mapping to the identity rotation.

> **Corollary (quaternion realisation).** Setting $\mathbf 1 = I$, $\mathbf i = -i\sigma_1$, $\mathbf j = -i\sigma_2$, $\mathbf k = -i\sigma_3$ realises the [[Def - Quaternions|quaternion]] algebra inside $\mathrm{Mat}(2,\mathbb{C})$ with $\mathbf i^2 = \mathbf j^2 = \mathbf k^2 = \mathbf i\mathbf j\mathbf k = -\mathbf 1$, and $SU(2)$ is exactly the unit quaternions $\{q \in \mathbb{H} : \|q\| = 1\}$.

---

# Motivation

This is the compact heart of the spinor map — the part that lives entirely inside rotations and so connects directly to ordinary three-dimensional geometry and to quantum spin. It answers two questions at once: *which* $SL(2,\mathbb{C})$ matrices give spatial rotations (the unitary ones), and *what is the shape* of the group of those matrices (the three-sphere).

The theorem matters because it is the bridge by which the abstract double cover becomes the concrete fact every physicist meets first: that a spin-½ system is described by $SU(2)$ and needs a $720^\circ$ rotation to return. The half-angle $\theta/2$ in the parametrisation is the visible cause, and tracing it to the two factors of $A$ in the congruence $A\underline X A^\dagger$ is the explanation that the bare statement "spin is half-integer" never provides.

It also supplies the workhorse computation for the surjectivity half of the [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|full double-cover theorem]]: that theorem needs explicit preimages of rotations, and this theorem provides them, together with the proof that they reproduce Rodrigues' rotation matrix. Finally, the quaternion corollary is the reason $SU(2)$ is not just a piece of relativity but the standard tool for composing rotations in graphics and robotics.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "$A$ is unitary in $SL(2,\mathbb{C})$," and the skill is recognising the many guises of that condition.

The first disguised source is **"$A$ fixes the time direction."** A Lorentz transformation that leaves $e_0$ invariant is a spatial rotation, and on the matrix side this is exactly unitarity: $A\sigma_0 A^\dagger = \sigma_0$ means $AA^\dagger = I$. The bridge is that $\sigma_0 = I$ corresponds to $e_0$, so fixing the time axis is fixing the identity matrix under congruence. *Example problem:* show that any $A$ with $AA^\dagger = I$ produces a Lorentz transformation that cannot mix time with space.

The second disguised source is **"$A$ preserves the spinor inner product."** A matrix preserving the Hermitian form $\langle\xi,\eta\rangle = \xi^\dagger\eta$ on $\mathbb{C}^2$ is by definition unitary, hence in $SU(2)$ if also $\det A = 1$. The bridge is the equivalence of "preserves $\xi^\dagger\eta$" and "$A^\dagger A = I$." *Example problem:* show that the normalisation $\xi^\dagger\xi = 1$ of a spin state is preserved exactly by $SU(2)$ rotations.

The third disguised source is **"$A$ lies on the unit three-sphere."** Writing $A = \begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix}$ with $|\alpha|^2 + |\beta|^2 = 1$, membership in $SU(2)$ is the equation of $S^3$ in the four real coordinates $(\mathrm{Re}\,\alpha, \mathrm{Im}\,\alpha, \mathrm{Re}\,\beta, \mathrm{Im}\,\beta)$. The bridge is this explicit parametrisation. *Example problem:* identify the $SU(2)$ element nearest the identity on $S^3$ with a small rotation.

**Targets (Output Amplification)**

The conclusion is "$\mathscr{S}: SU(2) \to SO(3)$ is a two-to-one cover with the Rodrigues parametrisation."

Combine the conclusion with **the homomorphism property** to compose rotations by multiplying quaternions. Since $\mathscr{S}$ is a homomorphism and every rotation has a quaternion preimage, the product of two rotations is the rotation of the quaternion product. The further result is the quaternion calculus of rotations used in graphics and aerospace; the combination is useful because $2\times 2$ (or quaternion) multiplication is cheaper and more numerically stable than $3\times 3$ matrix multiplication and avoids gimbal lock. *Example:* composing two rotations about different axes via $q_1 q_2$.

Combine the conclusion with **the half-angle** to predict the $4\pi$ periodicity of spinors. Since $A(\theta = 2\pi) = -I$ and $A(\theta = 4\pi) = I$, a spin state rotated by $2\pi$ acquires a sign and needs $4\pi$ to return. The further result is the experimental signature in neutron interferometry and the spin–statistics connection. The combination is nonobvious because the *rotation* is periodic with period $2\pi$ while its *spinor representative* has period $4\pi$. *Example:* the sign flip of an electron's wavefunction under a full rotation.

Combine the conclusion with **the kernel $\{\pm I\}$** to compute $\pi_1(SO(3))$. Since $S^3$ is simply connected and the cover is two-fold, $\pi_1(SO(3)) = \mathbb{Z}/2$, the topological fact behind the belt trick. The combination converts a homotopy question into a kernel count. *Example:* proving the rotation loop $\theta \in [0,2\pi]$ is noncontractible.

---

# Why Is It True

A unitary matrix fixes the identity under congruence — $AIA^\dagger = AA^\dagger = I$ — and the identity matrix is the time direction $e_0$. So a unitary $A$ produces a Lorentz transformation that does not move the time axis, and a Lorentz transformation fixing the time axis is precisely a spatial rotation: it must preserve the orthogonal complement of $e_0$, which is Euclidean three-space with its ordinary metric. This is the whole reason $SU(2)$ maps to $SO(3)$ rather than to boosts — *unitary fixes time*.

That the image is *all* of $SO(3)$, and that the parametrisation gives Rodrigues' formula, is a computation, but its shape is forced. The matrix $A = \cos\tfrac\theta2 I - i\sin\tfrac\theta2\,\mathbf n\cdot\boldsymbol\sigma$ acts on the *traceless* Hermitian matrices (which correspond to the spatial part of a four-vector, since $x^0 = \tfrac12\mathrm{tr}\,\underline X = 0$ for them) by conjugation $\underline{\mathbf x} \mapsto A\underline{\mathbf x}A^\dagger$, and using the Pauli multiplication law this conjugation rotates the vector $\mathbf x$ by $\theta$ about $\mathbf n$ — the double-angle identities $\cos\theta = 1 - 2\sin^2\tfrac\theta2$ and $\sin\theta = 2\sin\tfrac\theta2\cos\tfrac\theta2$ are exactly what turn the half-angles in $A$ into the full angle in the rotation. The half-angle is therefore not a quirk; it is dictated by the two factors of $A$ in the congruence, each carrying $\theta/2$, which combine via the double-angle formulas into $\theta$.

The shape $S^3$ is immediate from the explicit form: the condition $A^\dagger = A^{-1}$ together with $\det A = 1$ forces $A = \begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix}$ with $|\alpha|^2 + |\beta|^2 = 1$, which is the unit sphere in $\mathbb{R}^4 = \mathbb{C}^2$.

**The whole theorem in one sentence: a unitary matrix fixes the identity (= the time axis), so it acts as a rotation of the three spatial directions, and the two factors of $A$ in the congruence turn the half-angle in $A$ into the full angle in the rotation via the double-angle formulas.**

The kernel being $\{\pm I\}$ is the same Schur's-lemma argument as in the full theorem: only scalars commute with all Pauli matrices, and unit determinant leaves $\pm I$.

---

# What Makes This Hard

The conceptual leap is recognising that the *spatial* part of a four-vector is the *traceless* Hermitian part, so that a unitary congruence acts on traceless Hermitian matrices as a rotation of $\mathbb{R}^3$. The computational subtlety is the double-angle bookkeeping: it is easy to lose track of whether $A$ carries $\theta$ or $\theta/2$, and the only reliable check is that a $2\pi$ rotation must send $A$ to $-I$ (not back to $I$), forcing the half-angle. The most common error is to conclude the kernel is trivial — to find $A = I$ and stop — missing $A = -I$, which is precisely the element that makes the cover double rather than trivial.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Show unitary $\Rightarrow$ fixes $\sigma_0 = e_0 \Rightarrow$ rotation; parametrise $A = \exp(-\tfrac{i\theta}{2}\mathbf n\cdot\boldsymbol\sigma)$ and compute its conjugation action on traceless Hermitian matrices, recovering Rodrigues' formula via double-angle identities; identify the manifold as $S^3$ from $|\alpha|^2 + |\beta|^2 = 1$; compute the kernel $\{\pm I\}$ by Schur.

**Subgoal decomposition:**

1. **Unitary fixes the time axis.** Show $A \in SU(2) \Rightarrow A\sigma_0 A^\dagger = \sigma_0$, so $\Lambda_A(e_0) = e_0$.
   - *Hint:* $\sigma_0 = I$ and $AA^\dagger = I$.
   - *Why needed:* Identifies the image as rotations, not boosts.

2. **Conjugation rotates the spatial part.** Show $A(\mathbf x\cdot\boldsymbol\sigma)A^\dagger = (R\mathbf x)\cdot\boldsymbol\sigma$ with $R$ the rotation by $\theta$ about $\mathbf n$.
   - *Hint:* Expand using $\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$; the half-angles combine by double-angle formulas.
   - *Why needed:* Proves surjectivity onto $SO(3)$ and pins the Rodrigues parametrisation.

3. **Manifold is $S^3$.** Show $A^\dagger = A^{-1}$, $\det A = 1 \Rightarrow A = \begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix}$, $|\alpha|^2 + |\beta|^2 = 1$.
   - *Hint:* $A^{-1} = \begin{pmatrix}\delta&-\beta\\-\gamma&\alpha\end{pmatrix}$ for $\det A = 1$; equate to $A^\dagger$.
   - *Why needed:* Gives simple connectedness, hence the universal-cover/$\pi_1$ conclusion.

4. **Kernel is $\{\pm I\}$.** As in the full theorem.
   - *Hint:* Only scalars commute with all $\sigma_i$; $\det = 1$ gives $\pm I$.
   - *Why needed:* Makes the cover two-to-one.

---

# Lemma Decomposition

> [!note]- Lemma 1: A unitary A fixes the time direction
> **Statement:** If $A \in SU(2)$ then $A\sigma_0 A^\dagger = \sigma_0$, so the Lorentz transformation $\Lambda_A$ satisfies $\Lambda_A(e_0) = e_0$ and is a spatial rotation.
>
> **Hint:** $\sigma_0 = I$ and unitarity is $AA^\dagger = I$.
>
> **Why needed:** This is the reason $SU(2)$ maps into $SO(3)$ rather than into the boosts.
>
> > [!note]- Full proof
> > For $A \in SU(2)$, $A\sigma_0 A^\dagger = A I A^\dagger = AA^\dagger = I = \sigma_0$, since unitarity means $A^\dagger = A^{-1}$, so $AA^\dagger = I$. Under the [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|correspondence]] $\sigma_0$ is the time direction $e_0$, so $\Lambda_A(e_0) = e_0$. A Lorentz transformation fixing the timelike vector $e_0$ preserves its orthogonal complement $e_0^\perp$, which carries the negative-definite (i.e. Euclidean up to sign) metric, and an interval-preserving map of $e_0^\perp$ is an orthogonal transformation of $\mathbb{R}^3$; being in the identity component it is a rotation, $\Lambda_A \in SO(3)$. $\blacksquare$

> [!note]- Lemma 2: Conjugation by A = exp(−iθ/2 n·σ) is the rotation by θ about n
> **Statement:** For $A = \cos\tfrac\theta2 I - i\sin\tfrac\theta2\,\mathbf n\cdot\boldsymbol\sigma$ and any vector $\mathbf x$, $A(\mathbf x\cdot\boldsymbol\sigma)A^\dagger = (R(\theta,\mathbf n)\mathbf x)\cdot\boldsymbol\sigma$, where $R(\theta,\mathbf n)$ is Rodrigues' rotation.
>
> **Hint:** Use $A^\dagger = \cos\tfrac\theta2 I + i\sin\tfrac\theta2\,\mathbf n\cdot\boldsymbol\sigma$ and the Pauli identity $\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$; collect terms and apply double-angle formulas.
>
> **Why needed:** Establishes surjectivity onto $SO(3)$ and that the half-angle parametrisation gives the correct rotation angle.
>
> > [!note]- Full proof
> > Write $A = cI - is\,(\mathbf n\cdot\boldsymbol\sigma)$ with $c = \cos\tfrac\theta2$, $s = \sin\tfrac\theta2$, so $A^\dagger = cI + is\,(\mathbf n\cdot\boldsymbol\sigma)$. Then
> > $$A(\mathbf x\cdot\boldsymbol\sigma)A^\dagger = (cI - is\,\mathbf n\cdot\boldsymbol\sigma)(\mathbf x\cdot\boldsymbol\sigma)(cI + is\,\mathbf n\cdot\boldsymbol\sigma).$$
> > Expanding and using $(\mathbf n\cdot\boldsymbol\sigma)(\mathbf x\cdot\boldsymbol\sigma) = (\mathbf n\cdot\mathbf x)I + i(\mathbf n\times\mathbf x)\cdot\boldsymbol\sigma$ (the vector form of the Pauli law), the result is, after collecting,
> > $$\Big[c^2\,\mathbf x + 2cs\,(\mathbf n\times\mathbf x) + s^2\big(2(\mathbf n\cdot\mathbf x)\mathbf n - \mathbf x\big)\Big]\cdot\boldsymbol\sigma.$$
> > Using $2cs = \sin\theta$, $c^2 - s^2 = \cos\theta$, and $2s^2 = 1 - \cos\theta$, the bracket is
> > $$\cos\theta\,\mathbf x + \sin\theta\,(\mathbf n\times\mathbf x) + (1-\cos\theta)(\mathbf n\cdot\mathbf x)\mathbf n,$$
> > which is exactly **Rodrigues' formula** for the rotation of $\mathbf x$ by angle $\theta$ about $\mathbf n$. Hence $A(\mathbf x\cdot\boldsymbol\sigma)A^\dagger = (R\mathbf x)\cdot\boldsymbol\sigma$. Since every rotation is of this form, $\mathscr{S}|_{SU(2)}$ is onto $SO(3)$. $\blacksquare$

> [!note]- Lemma 3: SU(2) is the three-sphere
> **Statement:** $A \in SU(2) \iff A = \begin{pmatrix}\alpha & \beta \\ -\bar\beta & \bar\alpha\end{pmatrix}$ with $|\alpha|^2 + |\beta|^2 = 1$; hence $SU(2) \cong S^3$.
>
> **Hint:** For $\det A = 1$, $A^{-1} = \begin{pmatrix}\delta & -\beta \\ -\gamma & \alpha\end{pmatrix}$; set this equal to $A^\dagger = \begin{pmatrix}\bar\alpha & \bar\gamma \\ \bar\beta & \bar\delta\end{pmatrix}$.
>
> **Why needed:** Simple connectedness of $S^3$ makes $SU(2)$ the universal cover of $SO(3)$, giving $\pi_1(SO(3)) = \mathbb{Z}/2$.
>
> > [!note]- Full proof
> > Let $A = \begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}$ with $\det A = \alpha\delta - \beta\gamma = 1$, so $A^{-1} = \begin{pmatrix}\delta&-\beta\\-\gamma&\alpha\end{pmatrix}$. Unitarity $A^\dagger = A^{-1}$ equates $\begin{pmatrix}\bar\alpha&\bar\gamma\\\bar\beta&\bar\delta\end{pmatrix} = \begin{pmatrix}\delta&-\beta\\-\gamma&\alpha\end{pmatrix}$, giving $\delta = \bar\alpha$ and $\gamma = -\bar\beta$. The determinant condition becomes $|\alpha|^2 + |\beta|^2 = 1$. Writing $\alpha = x_1 + ix_2$, $\beta = x_3 + ix_4$, this is $x_1^2 + x_2^2 + x_3^2 + x_4^2 = 1$, the equation of the unit three-sphere $S^3 \subset \mathbb{R}^4$. The correspondence $A \leftrightarrow (x_1,x_2,x_3,x_4)$ is a diffeomorphism $SU(2) \cong S^3$. $\blacksquare$

> [!note]- Lemma 4: The quaternion realisation
> **Statement:** With $\mathbf 1 = I$, $\mathbf i = -i\sigma_1$, $\mathbf j = -i\sigma_2$, $\mathbf k = -i\sigma_3$, the Hamilton relations $\mathbf i^2 = \mathbf j^2 = \mathbf k^2 = \mathbf i\mathbf j\mathbf k = -\mathbf 1$ hold, and $SU(2)$ is the set of unit quaternions.
>
> **Hint:** $(-i\sigma_1)^2 = -\sigma_1^2 = -I$; $(-i\sigma_1)(-i\sigma_2) = -\sigma_1\sigma_2 = -i\sigma_3 = \mathbf k$.
>
> **Why needed:** Identifies $SU(2)$ with the unit quaternions, the form used to compose rotations in practice.
>
> > [!note]- Full proof
> > Compute $\mathbf i^2 = (-i\sigma_1)^2 = i^2\sigma_1^2 = (-1)(I) = -I = -\mathbf 1$, and likewise $\mathbf j^2 = \mathbf k^2 = -\mathbf 1$ since $\sigma_i^2 = I$. For the products, $\mathbf i\mathbf j = (-i\sigma_1)(-i\sigma_2) = -\sigma_1\sigma_2 = -i\sigma_3 = \mathbf k$ (using $\sigma_1\sigma_2 = i\sigma_3$), so $\mathbf i\mathbf j\mathbf k = \mathbf k\cdot\mathbf k = \mathbf k^2 = -\mathbf 1$, the full Hamilton relation. A general element $\mathbb{1}t + \mathbf i u + \mathbf j v + \mathbf k w = \begin{pmatrix} t - iw & -v - iu \\ v - iu & t + iw\end{pmatrix}$ has determinant $t^2 + u^2 + v^2 + w^2 = \|q\|^2$, so it lies in $SU(2)$ (determinant one, and one checks unitarity) exactly when $\|q\| = 1$; comparison with Lemma 3 (via $\alpha = t - iw$, $\beta = -v - iu$) confirms $SU(2) = \{q \in \mathbb{H} : \|q\| = 1\}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Manifold structure.** By Lemma 3, $SU(2)$ consists of matrices $\begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix}$ with $|\alpha|^2 + |\beta|^2 = 1$, diffeomorphic to $S^3 \subset \mathbb{R}^4$. In particular $SU(2)$ is connected and simply connected.
>
> **Image is $SO(3)$.** By Lemma 1, a unitary $A$ fixes $\sigma_0 = e_0$, so $\mathscr{S}(A)$ is a spatial rotation; thus $\mathscr{S}(SU(2)) \subseteq SO(3)$. By Lemma 2, the explicit family $A = \exp(-\tfrac{i\theta}{2}\mathbf n\cdot\boldsymbol\sigma)$ maps onto every rotation $R(\theta,\mathbf n)$ via Rodrigues' formula, so $\mathscr{S}(SU(2)) = SO(3)$: the map is onto.
>
> **Homomorphism.** As a restriction of the spinor map ([[Def - The Spinor Map and SL(2,C)]]), $\mathscr{S}|_{SU(2)}$ is a homomorphism, and $SU(2)$ is closed under multiplication (a subgroup of $SL(2,\mathbb{C})$), so the image $SO(3)$ is a subgroup.
>
> **Kernel.** The kernel of $\mathscr{S}|_{SU(2)}$ is the kernel of $\mathscr{S}$ intersected with $SU(2)$. By the argument of [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|Lemma 3 of the full theorem]], $\mathscr{S}(A) = \mathrm{Id} \Rightarrow A$ commutes with all Pauli matrices $\Rightarrow A = \lambda I$ with $\lambda^2 = 1 \Rightarrow A = \pm I$, both of which are unitary. Hence $\ker(\mathscr{S}|_{SU(2)}) = \{\pm I\}$.
>
> **Conclusion.** $\mathscr{S}: SU(2) \to SO(3)$ is a surjective homomorphism with kernel $\{\pm I\}$, hence two-to-one, and $SO(3) \cong SU(2)/\{\pm I\}$. Since $SU(2) = S^3$ is simply connected, it is the universal cover of $SO(3)$, and $\pi_1(SO(3)) \cong \{\pm I\} \cong \mathbb{Z}/2$. The endpoints $\theta = 0$ ($A = I$) and $\theta = 2\pi$ ($A = \cos\pi\,I = -I$) both map to the identity rotation, exhibiting the two-fold fibre. The quaternion realisation is Lemma 4. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Euler angles and the Cayley–Klein parameters (classical mechanics).** A rigid body's orientation is given by three Euler angles $(\hat\varphi, \hat\theta, \hat\psi)$, and the corresponding $SU(2)$ element has entries $\alpha = -\cos\tfrac{\hat\theta}2 e^{-i(\hat\varphi+\hat\psi)/2}$, $\beta = i\sin\tfrac{\hat\theta}2 e^{i(\hat\psi-\hat\varphi)/2}$ — the **Cayley–Klein parameters** of the rotation. The theorem is what guarantees these parametrise $SU(2)$ and project to the Euler-angle rotation; the application connects spinor methods to the classical theory of the spinning top, where Cayley and Klein introduced them.

**The Bloch sphere (quantum information).** The state of a single qubit is a unit vector in $\mathbb{C}^2$ up to phase, i.e. a point on $S^2$ (the Bloch sphere), and the unitary gates acting on it are $SU(2)$. The theorem's map $SU(2) \to SO(3)$ is exactly the statement that a qubit gate rotates the Bloch sphere, with the half-angle meaning a $2\pi$ gate flips the qubit's phase. The application is foundational to quantum computing, where single-qubit operations *are* this $SU(2)$ action.

**The Hopf fibration (topology).** The map $S^3 = SU(2) \to S^2$ sending $A$ to the image of a fixed spin state is the **Hopf fibration**, a nontrivial $S^1$-bundle over $S^2$. The theorem provides the total space $S^3 = SU(2)$ and the structure; the fibration's nontriviality is the same fact as the double cover's. The application is a cornerstone of homotopy theory ($\pi_3(S^2) = \mathbb{Z}$), reachable directly from the spinor map, and it reappears on the [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|celestial sphere]] as the Hopf map $S^3/U(1) = S^2$.

---

# Bridges

- **[[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group]]** — this theorem is the compact ($SU(2) \subset SL(2,\mathbb{C})$) restriction. Adjoining the boosts (the Hermitian, non-unitary elements) extends $SU(2) = \mathrm{Spin}(3)$ to $SL(2,\mathbb{C}) = \mathrm{Spin}^+(1,3)$ and $SO(3)$ to $SO^+(1,3)$; the kernel $\{\pm I\}$ is unchanged, which is why both covers are two-fold.

- **[[Thm - SU(2) is the Double Cover of SO(3)]]** — the vault's Clifford-algebra statement of the same result. There $SU(2) = \mathrm{Spin}(3)$ arises as the even Clifford group of $\mathbb{R}^3$ acting on vectors by conjugation; here it arises as the unitary subgroup of the spinor map. The two constructions agree because the [[Ex - Pauli Matrices Generate Cl(R^3)|Pauli matrices generate \mathrm{Cl}(3)]], and the conjugation action is the same.

- **[[Def - Quaternions]]** — the corollary realises $SU(2)$ as the unit quaternions, and the spinor map becomes the classical "rotation by quaternion conjugation $\mathbf v \mapsto q\mathbf v q^{-1}$." This is the bridge to computer graphics and spacecraft attitude control, where quaternions compose rotations without gimbal lock; the double cover appears as the redundancy $q \leftrightarrow -q$.

- **[[Def - SU(2) Action on Spinors]]** — the vault's quantum-mechanical $SU(2)$ action on spin-½ states is exactly the restriction of the left Weyl representation to rotations, and the half-angle here is the half-angle that makes a spin-½ wavefunction double-valued. The spin operators $S_i = \tfrac12\sigma_i$ are the generators of this action.

---

# Unlocked by This

> [!tip] Spin-½ and the Stern–Gerlach Experiment *(from Quantum Mechanics)*
> A two-component object transforming by $\exp(-\tfrac{i\theta}{2}\mathbf n\cdot\boldsymbol\sigma)$ is a **spin-½** state, and the half-angle is observable: a magnetic field rotating the spin by $2\pi$ leaves a measurable sign on the wavefunction, and a Stern–Gerlach apparatus splits a spin-½ beam into exactly two — the two eigenstates of $S_z = \tfrac12\sigma_3$. The map $SU(2) \to SO(3)$ of this theorem is why "spin" rotates like an ordinary angular momentum in space while its state needs $720^\circ$ to return.

> [!tip] The Belt Trick and π₁(SO(3)) *(from Topology)*
> Because $SU(2) = S^3$ is simply connected and double-covers $SO(3)$, the fundamental group $\pi_1(SO(3)) = \mathbb{Z}/2$: a single $2\pi$ rotation traces a noncontractible loop, but a $4\pi$ rotation is contractible. This is **Dirac's belt trick** (or plate trick): a belt twisted by $2\pi$ cannot be untwisted with fixed ends, but a $4\pi$ twist can. The theorem turns this tactile demonstration into a precise statement about the topology of the rotation group and its cover.
