---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Normal Operator"
  - "Def - Adjoint of a Linear Map"
  - "Def - Inner Product Space"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional [[Def - Inner Product Space|inner product space]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$. An operator $T \in \mathcal{L}(V)$ is [[Def - Normal Operator|normal]] if $TT^* = T^*T$, with [[Def - Adjoint of a Linear Map|adjoint]] $T^*$ satisfying $\langle Tv, w \rangle = \langle v, T^* w \rangle$ for all $v, w \in V$. The norm of $v$ is $\|v\| = \sqrt{\langle v, v \rangle}$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

---

# Statement

> **Theorem (Equivalent characterisations of normality).** Let $T \in \mathcal{L}(V)$. The following are equivalent:
>
> 1. $T$ is normal: $T T^* = T^* T$.
> 2. $\|Tv\| = \|T^* v\|$ for all $v \in V$.
> 3. For every $\lambda \in \mathbb{F}$, $\operatorname{null}(T - \lambda I) = \operatorname{null}(T^* - \overline{\lambda} I)$ — that is, $Tv = \lambda v$ if and only if $T^* v = \overline{\lambda} v$.
> 4. Eigenvectors of $T$ for distinct eigenvalues are orthogonal.
>
> Over $\mathbb{C}$, this is further equivalent to:
>
> 5. $V$ has an orthonormal basis of eigenvectors of $T$ (the [[Thm - Complex Spectral Theorem|complex spectral theorem]]).

---

# Motivation

This theorem is the operational toolkit for normality. The condition $T T^* = T^* T$ — the *official* definition — is rarely the most convenient form to verify or use. Each of the equivalent characterisations is the right form for a different setting:

- **(1) for symbolic manipulation:** $TT^* = T^*T$ is the cleanest statement; once internalised, it gives normality of polynomial expressions in $T, T^*$ and lets you commute the two operators freely.
- **(2) for verification from a concrete description:** computing $\|Tv\|$ and $\|T^* v\|$ from a matrix or operator description is mechanical; checking $TT^*v = T^*Tv$ for all $v$ via matrix multiplication requires two separate computations.
- **(3) for eigenvector analysis:** the eigenvector-eigenvalue conjugation pairing is what makes the spectral theorem's induction work; without it, eigenspaces of $T$ would not be $T^*$-invariant.
- **(4) for proving orthogonality:** when you have several eigenvectors of a normal operator at hand, their pairwise orthogonality is read off this property directly.

The deeper content of the theorem is the equivalence chain (3) ⇔ (4) ⇔ (5) (the last over $\mathbb{C}$): eigenvalue conjugation pairing, orthogonality of distinct-eigenvalue eigenvectors, and orthonormal diagonalisability are all the same condition viewed three ways. Each implies the others, and each is the right form for a different style of argument.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$T$ is an operator on a finite-dimensional inner product space". Recognising any one of the characterisations is enough to invoke all the others.

The first disguised source is **the operator preserves the norm to within complex conjugation**. The relation $\|Tv\| = \|T^* v\|$ is what one verifies for a concrete operator; it amounts to checking that two functions on $V$ agree, which is computationally simple. *Example problem:* show that any normal $T$ with $Tv = 0$ for some $v$ also satisfies $T^* v = 0$ — this is the eigenvalue-$0$ case of characterisation (3), and it follows directly from (2).

The second disguised source is **$T$ commutes with $T^*$ on a specific basis**. If $T T^* e_j = T^* T e_j$ for a basis $\{e_j\}$, then by linearity $T T^* = T^* T$. So normality can be checked on a basis. *Example problem:* the matrix $\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$ — verify on standard basis that $TT^* = T^*T$ (both equal $2I$).

The third disguised source is **$T$ has a complete orthonormal eigenbasis** — characterisation (5). If you have presented an operator by its orthonormal eigendecomposition $T = \sum \lambda_j P_j$, normality is automatic. *Example problem:* prove that polynomial functional calculus $p(T)$ of a normal $T$ is also normal — write $p(T) = \sum p(\lambda_j) P_j$, which has the same orthonormal eigenbasis.

**Targets (Output Amplification)**

The conclusion is the full equivalence: any one characterisation gives all the others.

Combine characterisation (3) with **the spectral theorem proof**: the eigenvector-eigenvalue conjugation pairing is the mechanism that makes eigenspaces of $T$ also be eigenspaces of $T^*$, hence both-invariant, hence the orthogonal complement is also both-invariant, hence the induction can proceed. The further result $E$ is the [[Thm - Complex Spectral Theorem|complex spectral theorem]] itself.

Combine characterisation (4) with **the polarisation identity**: orthogonality of eigenvectors $v, w$ for distinct eigenvalues $\lambda, \mu$ means $\langle v, w \rangle = 0$. Combined with the eigenvalue conjugation pairing, eigenvectors of $T^*$ are eigenvectors of $T$, with conjugate eigenvalues, so they too are orthogonal. The further result $E$ is that the spectral decomposition is a true orthogonal direct sum.

Combine characterisation (2) with **the absolute value $|T| = \sqrt{T^* T}$**: for normal $T$, $\|Tv\|^2 = \langle T^*Tv, v \rangle = \langle |T|^2 v, v \rangle = \||T| v\|^2$, so $\|Tv\| = \||T| v\|$ — the absolute value preserves norms with $T$. Equivalently, $T = U|T|$ for a unitary $U$ when $T$ is normal — the polar decomposition's $U$ factor is unitary precisely when $T$ is normal.

---

# Why Is It True

The proof revolves around a single calculation: for any $S \in \mathcal{L}(V)$, $\|Sv\|^2 = \langle Sv, Sv \rangle = \langle S^* S v, v \rangle$. So $\|Sv\|^2 - \|S^* v\|^2 = \langle (S^* S - S S^*) v, v \rangle$. The right side is zero for all $v$ if and only if $S^* S - S S^* = 0$ (using that this difference is self-adjoint, hence determined by its diagonal numerical values via polarisation). That gives **(1) ⇔ (2)** in one step.

**The one-liner mechanism: $\|Tv\|^2 - \|T^*v\|^2 = \langle (T^* T - T T^*) v, v \rangle$, so $\|Tv\| = \|T^* v\|$ for all $v$ iff $T^* T - T T^* = 0$, iff $T$ is normal.**

For **(2) ⇒ (3)**, apply (2) to $T - \lambda I$ (which is normal whenever $T$ is — see Lemma 1 in [[Thm - Complex Spectral Theorem]]): $\|(T - \lambda I) v\| = \|(T - \lambda I)^* v\| = \|(T^* - \overline{\lambda} I) v\|$. So one side is zero iff the other is zero, giving $T v = \lambda v$ iff $T^* v = \overline{\lambda} v$.

For **(3) ⇒ (4)**, the standard eigenvector orthogonality calculation: if $Tv = \lambda v$ and $Tw = \mu w$ with $\lambda \neq \mu$, then by (3), $T^* w = \overline{\mu} w$, so $\lambda \langle v, w \rangle = \langle Tv, w \rangle = \langle v, T^* w \rangle = \langle v, \overline{\mu} w \rangle = \mu \langle v, w \rangle$, forcing $\langle v, w \rangle = 0$.

For **(4) ⇒ (5) ⇒ (1)** over $\mathbb{C}$, this is the content of the [[Thm - Complex Spectral Theorem|complex spectral theorem]] proof. (4) is the orthogonality input; (5) is the eigenbasis output; (5) implies (1) by direct calculation in the eigenbasis (diagonal matrices commute with their conjugate transposes).

So the equivalence is structured: (1) ⇔ (2) is a one-step calculation; (2) ⇒ (3) ⇒ (4) is a chain by applying (2) to shifted operators; (4) ⇒ (5) is the spectral theorem's inductive proof; (5) ⇒ (1) is a direct calculation. The circle is closed.

---

# What Makes This Hard

The most subtle step is **(1) ⇔ (2)**: turning the operator identity $TT^* = T^*T$ into the norm identity $\|Tv\| = \|T^* v\|$. The mechanism is the bilinear-form trick: the self-adjoint operator $T^*T - TT^*$ has zero diagonal numerical range ($\langle (T^*T - TT^*)v, v \rangle = 0$ for all $v$) if and only if it is zero (using polarisation over $\mathbb{C}$, or its real analogue over $\mathbb{R}$). Without this lemma, the equivalence reduces to "operator $= 0$ on every vector iff operator $= 0$", which is trivial — but the relationship to the norm-comparison form is the nontrivial conversion.

The second subtle step is **(2) ⇒ (3)**: that normality propagates from $T$ to $T - \lambda I$. The calculation $TT^* = T^*T$ implies $(T - \lambda I)(T - \lambda I)^* = (T - \lambda I)^*(T - \lambda I)$ requires expanding both sides — they each equal $TT^* - \lambda T^* - \overline{\lambda} T + |\lambda|^2 I$ when normality is used, but if normality is *not* assumed for $T$, the two expansions differ.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Show (1) ⇔ (2) by computing $\|Tv\|^2 - \|T^*v\|^2$ as a quadratic form, then $(2)$ ⇒ $(3)$ by applying to $T - \lambda I$, then $(3)$ ⇒ $(4)$ by the standard eigenvector orthogonality calculation, then $(4) \Rightarrow (5) \Rightarrow (1)$ via the complex spectral theorem.

**Subgoal decomposition:**

1. **(1) ⇔ (2).** Show $TT^* = T^*T$ iff $\|Tv\| = \|T^*v\|$ for all $v$.
   - *Hint:* Both sides equal $\|Tv\|^2 - \|T^*v\|^2 = \langle (T^*T - TT^*) v, v \rangle$, and a self-adjoint operator is zero iff its diagonal numerical range is zero.

2. **Normality propagates to shifted operators.** For normal $T$ and $\lambda \in \mathbb{F}$, $T - \lambda I$ is normal.
   - *Hint:* Direct expansion.
   - *Why needed:* Allows applying (2) to $T - \lambda I$.

3. **(2) ⇒ (3).** Apply (2) to $T - \lambda I$ (normal by subgoal 2): $\|(T - \lambda I) v\| = \|(T^* - \overline{\lambda} I) v\|$, so kernels coincide.

4. **(3) ⇒ (4).** Use the eigenvector orthogonality calculation: $\lambda \langle v, w \rangle = \langle Tv, w \rangle = \langle v, T^*w \rangle = \mu \langle v, w \rangle$, hence $\langle v, w \rangle = 0$ when $\lambda \neq \mu$.

5. **(4) ⇒ (5)** (over $\mathbb{C}$). This is the complex spectral theorem.

6. **(5) ⇒ (1).** In an orthonormal eigenbasis the matrices of $T$ and $T^*$ are diagonal, hence commute.

---

# Lemma Decomposition

> [!note]- Lemma 1: Self-adjoint operator with zero diagonal numerical range is zero
> **Statement:** Let $S \in \mathcal{L}(V)$ be self-adjoint. If $\langle Sv, v \rangle = 0$ for all $v \in V$, then $S = 0$.
>
> **Hint:** Over $\mathbb{C}$, use the polarisation identity $\langle Sv, w \rangle = \frac{1}{4} \sum_{k=0}^{3} i^k \langle S(v + i^k w), v + i^k w \rangle$. Over $\mathbb{R}$ with self-adjoint $S$, use $\langle Sv, w \rangle = \frac{1}{4} [\langle S(v+w), v+w \rangle - \langle S(v-w), v-w \rangle]$.
>
> **Why needed:** Lets us conclude $T^*T = TT^*$ from $\langle (T^*T - TT^*) v, v \rangle = 0$ for all $v$, since $T^*T - TT^*$ is self-adjoint.
>
> > [!note]- Full proof
> > Over $\mathbb{C}$: from polarisation, $\langle Sv, w \rangle$ is a linear combination of $\langle Sv', v' \rangle$ at four specific vectors $v' = v + i^k w$. If all such diagonal values vanish, so does $\langle Sv, w \rangle$ for all $v, w$, hence $Sv = 0$ for all $v$ (take $w = Sv$), hence $S = 0$.
> >
> > Over $\mathbb{R}$ with $S$ self-adjoint: from $\langle S(v+w), v+w \rangle = \langle Sv, v \rangle + \langle Sw, w \rangle + 2\langle Sv, w \rangle$ (using self-adjointness for the cross term), if all diagonal values vanish then $\langle Sv, w \rangle = 0$ for all $v, w$, hence $S = 0$.

> [!note]- Lemma 2: Normal operator's shifts are normal
> **Statement:** If $T$ is normal and $\lambda \in \mathbb{F}$, then $T - \lambda I$ is normal.
>
> **Hint:** Expand $(T - \lambda I)(T - \lambda I)^* - (T - \lambda I)^*(T - \lambda I)$ directly.
>
> **Why needed:** Lets us apply the $\|Sv\| = \|S^*v\|$ characterisation to $S = T - \lambda I$ and conclude that kernels match.
>
> > [!note]- Full proof
> > $(T - \lambda I)(T - \lambda I)^* = (T - \lambda I)(T^* - \overline{\lambda} I) = TT^* - \overline{\lambda} T - \lambda T^* + |\lambda|^2 I$.
> >
> > $(T - \lambda I)^*(T - \lambda I) = (T^* - \overline{\lambda} I)(T - \lambda I) = T^*T - \overline{\lambda} T - \lambda T^* + |\lambda|^2 I$.
> >
> > Subtract: the difference is $T T^* - T^* T = 0$ by normality of $T$. So $T - \lambda I$ commutes with $(T - \lambda I)^*$, i.e., $T - \lambda I$ is normal.

> [!note]- Lemma 3: Eigenvector orthogonality from conjugation pairing
> **Statement:** If $T$ is normal, $Tv = \lambda v$, $Tw = \mu w$, $\lambda \neq \mu$, then $\langle v, w \rangle = 0$.
>
> **Hint:** Compute $\lambda \langle v, w \rangle$ via $\langle Tv, w \rangle$, and recognise the result as $\mu \langle v, w \rangle$ via $T^* w = \overline{\mu} w$.
>
> **Why needed:** This is characterisation (4), produced from characterisation (3) — eigenvectors of distinct eigenvalues are orthogonal.
>
> > [!note]- Full proof
> > By (3) (equivalently, by Lemmas 1 and 2 applied to the shifted operator), $T^* w = \overline{\mu} w$. Then $\lambda \langle v, w \rangle = \langle \lambda v, w \rangle = \langle Tv, w \rangle = \langle v, T^* w \rangle = \langle v, \overline{\mu} w \rangle = \mu \langle v, w \rangle$. So $(\lambda - \mu) \langle v, w \rangle = 0$, and since $\lambda \neq \mu$, $\langle v, w \rangle = 0$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> **(1) ⇔ (2):** For any $v \in V$, $\|Tv\|^2 = \langle Tv, Tv \rangle = \langle T^* T v, v \rangle$ and $\|T^* v\|^2 = \langle T^*v, T^*v \rangle = \langle T T^* v, v \rangle$ (the latter using $(T^*)^* = T$). Subtracting: $\|Tv\|^2 - \|T^*v\|^2 = \langle (T^*T - T T^*) v, v \rangle$.
>
> If $TT^* = T^*T$, the right side vanishes for all $v$, so $\|Tv\| = \|T^*v\|$ for all $v$.
>
> Conversely, if $\|Tv\| = \|T^*v\|$ for all $v$, then $\langle (T^*T - T T^*) v, v \rangle = 0$ for all $v$. The operator $T^*T - T T^*$ is self-adjoint (it is a self-adjoint difference). By Lemma 1, $T^*T - T T^* = 0$, i.e., $TT^* = T^*T$. So (1) ⇔ (2).
>
> **(2) ⇒ (3):** By Lemma 2, $T - \lambda I$ is normal whenever $T$ is. Apply (2) to $T - \lambda I$: $\|(T - \lambda I) v\| = \|(T - \lambda I)^* v\| = \|(T^* - \overline{\lambda} I) v\|$. So $(T - \lambda I) v = 0$ iff $(T^* - \overline{\lambda} I) v = 0$, giving $\operatorname{null}(T - \lambda I) = \operatorname{null}(T^* - \overline{\lambda} I)$.
>
> **(3) ⇒ (4):** Lemma 3.
>
> **(4) ⇒ (5)** (over $\mathbb{C}$): This is the complex spectral theorem; see [[Thm - Complex Spectral Theorem]] for the proof. The key inputs are Lemma 3 (or equivalently characterisation (4)) and the fundamental theorem of algebra. (4) by itself does *not* trivially imply (5) — one also needs that the eigenspaces span $V$, which is the inductive content of the spectral theorem.
>
> **(5) ⇒ (1)** (over $\mathbb{C}$): Suppose $V$ has an orthonormal eigenbasis $e_1, \ldots, e_n$ of $T$ with eigenvalues $\lambda_j$. In this basis, the matrix of $T$ is $D = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$ and the matrix of $T^*$ is $D^* = \operatorname{diag}(\overline{\lambda_1}, \ldots, \overline{\lambda_n})$. Diagonal matrices commute: $DD^* = D^*D = \operatorname{diag}(|\lambda_1|^2, \ldots, |\lambda_n|^2)$. So $TT^* = T^*T$, i.e., $T$ is normal.
>
> Over $\mathbb{R}$, the equivalence (1) ⇔ (5) fails (a rotation by $90^\circ$ is normal but has no real eigenvectors). The remaining equivalences (1) ⇔ (2) ⇔ (3) ⇔ (4) hold over $\mathbb{R}$ exactly as proved. $\blacksquare$

---

# Cross-Field Exercise Suggestions

1. **Quantum mechanics — commuting observables and joint eigenstates.** Two self-adjoint operators $\hat A$ and $\hat B$ commute if and only if they share an orthonormal eigenbasis. By this theorem, both are normal, and commutation lets one diagonalise them simultaneously. Physically, commuting observables can be jointly measured with arbitrary precision; non-commuting observables face Heisenberg uncertainty. The orthogonality of eigenvectors for distinct eigenvalues is exactly the orthogonality of measurement outcomes in standard quantum measurement.

2. **Markov chain mixing — symmetric transition matrices.** A symmetric stochastic matrix (a reversible Markov chain with uniform stationary distribution) is normal, and its spectral decomposition gives the **mixing time** in terms of the second-largest eigenvalue. The orthogonality of eigenvectors for distinct eigenvalues — characterisation (4) — gives the natural "frequency decomposition" of fluctuations from the stationary distribution.

3. **Signal processing — circulant matrices and the DFT.** A circulant matrix is generated by cyclic shifts of a row; it is normal (it commutes with the cyclic shift, hence with its conjugate transpose). By characterisation (5), it is orthonormally diagonalised by the discrete Fourier transform. This is the algebraic root of "[[Def - Convolution|convolution]] in the spatial domain = multiplication in the frequency domain", and is what makes Fourier-based filtering efficient.

4. **Number theory — Hecke operators.** In the theory of modular forms, the Hecke operators $T_p$ acting on spaces of cusp forms are all normal (they are self-adjoint with respect to the Petersson inner product). By the spectral theorem, the space of cusp forms decomposes orthogonally into joint eigenspaces of all the $T_p$ — the **Hecke eigenforms**, which are the canonical basis of the theory. The orthogonality of eigenforms for distinct Hecke eigenvalues is characterisation (4) in action.

---

# Bridges

- **[[Thm - Complex Spectral Theorem]]** — This theorem and the complex spectral theorem are tightly linked: the equivalences (3) ⇔ (4) ⇔ (5) are the algebraic content of the spectral theorem. Knowing this theorem gives the spectral theorem; knowing the spectral theorem gives this theorem. They are two sides of the same fact.

- **[[Def - Self-Adjoint Operator|Self-adjoint operators]] and [[Def - Unitary Operator|unitary operators]]** — Both classes are subclasses of normal operators. For a self-adjoint $T$, the conjugation pairing $T^* w = \overline{\mu} w$ becomes $Tw = \overline{\mu} w$, forcing $\mu = \overline{\mu}$, i.e., real eigenvalues. For unitary $T$, the relation $T^* T = I$ on an eigenvector gives $\overline{\lambda} \lambda = 1$, i.e., $|\lambda| = 1$. The eigenvalue location is the distinguishing feature between subclasses of normal operators.

- **Polar decomposition** — For a normal operator $T$, the polar decomposition $T = U |T|$ has $U$ unitary (not merely a partial isometry), and the factors $U$ and $|T|$ commute. This is special to normal operators: for general operators, the polar factors do not commute. The reason: for normal $T$, $T$ commutes with $T^*$, hence with $T^*T$, hence with $\sqrt{T^*T} = |T|$, hence with $U = T |T|^{-1}$ (when $T$ is invertible).

- **Functional calculus** — For a normal operator, the functional calculus $f(T) = \sum f(\lambda_j) P_j$ produces operators that are themselves normal (they have the same orthonormal eigenbasis). This is what makes the operator-valued exponentials $e^{tT}$, $\sin(T)$, etc., well-defined and well-behaved for normal $T$. The whole edifice of operator-theoretic functional calculus rests on the existence of an orthonormal eigenbasis, which is characterisation (5) of normality.

---

# Unlocked by This

> [!tip] Polar Decomposition of Normal Operators *(from Functional Analysis)*
> For a normal operator $T$ on a finite-dimensional inner product space, the polar decomposition $T = U |T|$ has the special property that the unitary $U$ and the positive operator $|T|$ commute. (For general operators they do not commute.) This is because $T$ commutes with $T^*$, hence with $T^*T$, hence with the spectral functional calculus $\sqrt{T^*T} = |T|$, hence with $U = T |T|^{+}$ where $|T|^+$ is the pseudoinverse. The polar decomposition of a normal operator therefore gives a *commuting* factorisation into "phase" and "magnitude", in close analogy with $z = e^{i\theta} \cdot |z|$ for complex numbers (where multiplication is commutative). For non-normal $T$, the factors of the polar decomposition do not commute, and the analogy with complex numbers breaks down on this point.

> [!tip] Putnam's Inequality and Normal Operator Theory *(from Operator Theory)*
> A theorem of Putnam: for a hyponormal operator $T$ (a generalisation of normal: $T^*T \geq T T^*$), the self-commutator $[T^*, T] = T^*T - TT^*$ has trace bounded by the area enclosed by the spectrum of $T$. For a normal operator, the self-commutator is zero and this trace is trivially zero. For non-normal operators, the self-commutator measures *how far* the operator is from being normal. The whole theory of hyponormal, quasinormal, subnormal, and related operator classes is built around quantitative versions of "almost normal", with this theorem as a foundational measurement of non-normality.

> [!tip] Berezin Symbol and Bohr-Sommerfeld Quantization *(from Mathematical Physics)*
> For a normal operator on $L^2$, the **Berezin symbol** $\widetilde T (z) = \langle T k_z, k_z \rangle$ on coherent states $k_z$ is a smooth function on the parameter space. The condition that $T$ be normal is exactly the condition that $\widetilde T$ behaves "classically" — that the operator can be approximated by multiplication by its symbol in a quantitative sense. Non-normality manifests as commutator corrections in the Berezin–Toeplitz calculus, and the leading-order classical-quantum correspondence holds precisely for normal operators. This is the deformation-quantisation perspective on the equivalence between normal operators and their function-theoretic shadows.
