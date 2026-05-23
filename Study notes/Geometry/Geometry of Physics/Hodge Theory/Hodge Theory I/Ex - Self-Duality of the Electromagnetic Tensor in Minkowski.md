---
type: exercise
subject: hodge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Hodge Star Operator"
  - "Def - Self-Dual and Anti-Self-Dual Forms"
  - "Def - Minkowski Space and the Metric"
tags: [geometry, hodge-theory, electromagnetism, gauge-theory]
---

# Problem Statement

Let $M = \mathbb{R}^{3,1}$ be Minkowski space with metric $g = -dt^2 + dx^2 + dy^2 + dz^2$ and orientation $dt\wedge dx\wedge dy\wedge dz$.

(a) Compute $\star\star\omega$ for a general $2$-form $\omega$ on Minkowski space. Show that $\star\star = -\mathrm{id}$ on $\Omega^2(M)$.

(b) Show that the eigenvalues of $\star : \Omega^2(M) \to \Omega^2(M)$ over $\mathbb{R}$ are not real — there are no nontrivial real self-dual or anti-self-dual $2$-forms in Lorentzian $4$D. Show that over $\mathbb{C}$, the eigenvalues are $\pm i$.

(c) Given the electromagnetic $2$-form $F = E_i dx^i\wedge dt + B_{ij}dx^i\wedge dx^j$ (with the standard cyclic ordering of $B_{ij}$), compute the **complex self-dual combination** $F + i\star F$. Show that this is a complex self-dual $2$-form: $\star(F + i\star F) = -i(F + i\star F)$.

(d) Interpret the complex self-dual combination physically: in classical electromagnetism, the field $\vec E + i\vec B$ is the **complex Maxwell tensor**, and the Maxwell equations $dF = 0$, $d\star F = 0$ are equivalent to a single complex equation $d(F + i\star F) = 0$ when augmented with a "duality rotation" $F \to e^{i\theta}(F + i\star F)$.

(e) Contrast with the **Riemannian** $4$D case: on Euclidean $\mathbb{R}^4$, $\star\star = +1$ on $\Omega^2$, so the eigenvalues of $\star$ are real ($\pm 1$), and the self-dual / anti-self-dual decomposition $\Omega^2(\mathbb{R}^4) = \Omega^2_+\oplus\Omega^2_-$ is over $\mathbb{R}$. This is the algebraic shell for the **instanton equations** in Yang–Mills theory. Discuss why the Riemannian case is the "natural" setting for self-dual gauge fields.

**Recall:**

The Hodge star on a (pseudo-)Riemannian $n$-manifold has $\star\star = (-1)^{k(n-k) + s}\mathrm{id}$ on $k$-forms, where $s$ is the number of negative eigenvalues of the metric. For Lorentzian $4$D ($n = 4$, $s = 1$) and $k = 2$: $\star\star = (-1)^{2\cdot 2 + 1} = -1$.

For Riemannian $4$D ($n = 4$, $s = 0$) and $k = 2$: $\star\star = (-1)^{2\cdot 2} = +1$, so $\star$ is an involution on $\Omega^2(\mathbb{R}^4)$ and splits it into $\pm 1$ eigenspaces $\Omega^2_+$ and $\Omega^2_-$ (self-dual and anti-self-dual).

![[Def - Self-Dual and Anti-Self-Dual Forms#The Definition]]

The electromagnetic $2$-form $F$ on Minkowski space encodes $\vec E$ and $\vec B$ via $F_{0i} = E_i$ and $F_{ij} = \epsilon_{ijk}B_k$.

---

# Convergent Strategy

**Problem class:** Algebraic analysis of the Hodge star's eigenvalue structure on a specific manifold (middle-degree forms in Lorentzian $4$D), with the goal of understanding why Riemannian instantons exist but Lorentzian "instantons" require complex coefficients. The chapter's problem-solving strategy on the self-dual decomposition (operation 2 from the topic page) is the relevant tool.

**Assumption pattern:** Minkowski signature $(- + + +)$, [[Def - Dimension|dimension]] $4$, middle degree $k = 2$. The signature parameter $s = 1$ flips the sign of $\star\star$ from $+1$ (Riemannian) to $-1$ (Lorentzian). The dimension parameter $k(n-k) = 4$ stays the same. The combined effect is $\star\star = -1$, the key difference from Riemannian $4$D.

**Theorem routing:** Use [[Thm - Properties of the Hodge Star]] property 2 (double-star formula) with $s = 1$. For the eigenvalue analysis, observe that an operator with $\star^2 = -\mathrm{id}$ has eigenvalues solving $\lambda^2 = -1$, hence $\lambda = \pm i$ over $\mathbb{C}$ but no real eigenvalues. For the complex self-duality computation, apply $\star$ to $F + i\star F$ and use $\star\star = -1$ to verify.

**Key decision point:** Recognize the *structural significance* of the sign $\star^2 = -1$ in Lorentzian $4$D: it forces real self-duality to be trivial ($F = 0$ only) and complex self-duality to give a complex structure (eigenvalues $\pm i$ from $\sqrt{-1}$). This is in sharp contrast to Riemannian $4$D ($\star^2 = +1$), where real self-duality gives a meaningful eigenspace decomposition. The "miracle of $4$D" — self-duality and instantons — is fundamentally a Riemannian-signature phenomenon, made possible by the dimension matching $k = n/2 = 2$ and the sign matching $\star\star = +1$.

---

# Legal Operations Used

1. **Apply the double-star formula** (operation 2 from the topic page) with the appropriate signature. For Lorentzian $4$D on $2$-forms: $\star\star = -\mathrm{id}$. For Riemannian $4$D: $\star\star = +\mathrm{id}$.

2. **Eigenvalue analysis on an involution / anti-involution**: an operator $A$ with $A^2 = \pm\mathrm{id}$ has eigenvalues $\pm 1$ (over $\mathbb{R}$, if $A^2 = +\mathrm{id}$) or $\pm i$ (over $\mathbb{C}$, if $A^2 = -\mathrm{id}$). Verify by direct computation: $A^2 v = \lambda^2 v$ implies $\lambda^2 = \pm 1$.

3. **Combine $F$ and $\star F$ into the complex form $F + i\star F$**: apply $\star$ to this combination and use $\star^2 = -1$ to simplify. The result $\star(F + i\star F) = -i(F + i\star F)$ shows it is a complex self-dual $2$-form (eigenvalue $+i$... wait, or $-i$? let me check the sign).

4. **Physically interpret** the complex Maxwell tensor as $\vec E + i\vec B$, and explain the duality rotation as a symmetry of source-free Maxwell theory.

---

# Hints

> [!note]- Hint 1
> For part (a), use the formula $\star\star = (-1)^{k(n-k) + s}\mathrm{id}$. Plug in $n = 4$, $k = 2$, $s = 1$ (the one timelike direction). Compute the exponent: $k(n-k) + s = 4 + 1 = 5$, odd, so $\star\star = -\mathrm{id}$ on $2$-forms.

> [!note]- Hint 2
> For part (b), an operator $A$ with $A^2 = -\mathrm{id}$ satisfies $A^2 v = -v$ for all $v$. If $Av = \lambda v$, then $\lambda^2 v = -v$, so $\lambda^2 = -1$. The only complex solutions are $\lambda = \pm i$; no real $\lambda$. Hence $\star$ has no real eigenvalues on $\Omega^2(M^{3,1})$, no nontrivial real self-dual or anti-self-dual $2$-forms.

> [!note]- Hint 3
> For part (c), apply $\star$ to $F + i\star F$. Distributing: $\star(F + i\star F) = \star F + i\star\star F = \star F + i(-F) = \star F - iF = -i(iF + \star F)$… hmm let me recompute. $-i(iF + \star F) = -i\cdot i F - i\star F = F - i\star F \neq -i(F + i\star F)$. Try: $-i(F + i\star F) = -iF - i^2\star F = -iF + \star F$. So $\star(F + i\star F) = \star F - iF = -i(F + i\star F)$? Check: $-i(F + i\star F) = -iF + \star F$. So $\star F - iF = -i F + \star F$ if and only if $-iF = -iF$, which is true. So yes, $\star(F + i\star F) = -i(F + i\star F)$. The form $F + i\star F$ has $\star$-eigenvalue $-i$. (One can also work with $F - i\star F$, the conjugate, with eigenvalue $+i$.)

---

# Solution

The exercise has five parts. Parts (a) and (b) establish the basic algebraic structure: $\star^2 = -1$ on $2$-forms in Lorentzian $4$D, eigenvalues $\pm i$ over $\mathbb{C}$. Part (c) constructs the complex self-dual combination. Part (d) interprets physically. Part (e) contrasts with the Riemannian case.

**Step 1: Double-star on $2$-forms in Lorentzian $4$D (part (a)).**

> [!note]- Derivation
> Apply $\star\star = (-1)^{k(n-k) + s}\mathrm{id}$ on $k$-forms with $n = 4$ (dimension), $k = 2$, $s = 1$ (Lorentzian signature, one timelike direction):
> $$\star\star = (-1)^{2\cdot 2 + 1}\mathrm{id} = (-1)^5\mathrm{id} = -\mathrm{id}.$$
> So on $\Omega^2(M^{3,1})$, $\star\star = -\mathrm{id}$. ✓
>
> Direct verification on a basis $2$-form: $\star(dx\wedge dt)$. Using the orthonormal-coframe formula (with $\epsilon_t = -1, \epsilon_x = +1$, orientation $dt\wedge dx\wedge dy\wedge dz$): from [[Ex - Maxwell's Equations Use the Codifferential]] Step 2, $\star(dx\wedge dt) = dy\wedge dz$. Apply $\star$ again: $\star(dy\wedge dz) = -dx\wedge dt$ (with signature signs). So $\star\star(dx\wedge dt) = -dx\wedge dt$. ✓

**Step 2: Eigenvalue analysis (part (b)).**

> [!note]- Derivation
> Suppose $\omega \in \Omega^2(M^{3,1})$ is a real $2$-form with $\star\omega = \lambda\omega$ for some real $\lambda$. Apply $\star$ again: $\star\star\omega = \lambda\star\omega = \lambda^2\omega$. By Step 1, $\star\star\omega = -\omega$. So $\lambda^2\omega = -\omega$, hence $\lambda^2 = -1$.
>
> Over $\mathbb{R}$, the equation $\lambda^2 = -1$ has no solution. So there are no real eigenvalues of $\star$ on $\Omega^2(M^{3,1})$ — no nonzero real $\omega$ satisfies $\star\omega = \pm\omega$ (these would be "self-dual" and "anti-self-dual" in the Riemannian sense, but neither is achievable in Lorentzian).
>
> Over $\mathbb{C}$, the equation $\lambda^2 = -1$ has solutions $\lambda = \pm i$. Complexifying $\Omega^2$ to $\Omega^2(M; \mathbb{C}) = \Omega^2(M)\otimes\mathbb{C}$, the operator $\star$ extends $\mathbb{C}$-linearly and has eigenvalues $\pm i$ with eigenspaces $\Omega^2_+(M; \mathbb{C})$ and $\Omega^2_-(M; \mathbb{C})$ (each rank-$3$ over $\mathbb{C}$, at each point).
>
> So the natural self-dual decomposition in Lorentzian $4$D is *complex*: $\Omega^2(M; \mathbb{C}) = \Omega^2_+\oplus\Omega^2_-$ with $\star = \pm i$ on each summand. This contrasts with Riemannian $4$D, where the decomposition is real. ✓

**Step 3: Complex self-dual combination (part (c)).**

> [!note]- Derivation
> Compute $\star(F + i\star F)$:
> $$\star(F + i\star F) = \star F + i\star\star F = \star F + i(-F) = \star F - iF = -i(iF + \star F\cdot i \cdot (-i))$$
> Let me redo this more carefully:
> $$\star(F + i\star F) = \star F + i(\star\star F) = \star F + i(-F) = -iF + \star F.$$
> Compare to $-i(F + i\star F) = -iF + (-i)(i\star F) = -iF + \star F$. So $\star(F + i\star F) = -i(F + i\star F)$. ✓
>
> Hence $F + i\star F$ has $\star$-eigenvalue $-i$, making it an anti-self-dual complex $2$-form in our complex sign convention. Equivalently, $F - i\star F$ has eigenvalue $+i$ (self-dual). These are complex conjugates of each other.

**Step 4: Physical interpretation (part (d)).**

The complex Maxwell tensor $F + i\star F$ encodes the combined complex field $\vec E + i\vec B$ (with appropriate sign conventions). The source-free Maxwell equations $dF = 0, d\star F = 0$ become equivalent to the single complex equation $d(F + i\star F) = 0$:
$$d(F + i\star F) = dF + i\,d\star F = 0 + i\cdot 0 = 0.$$
This is one complex equation rather than two real ones, expressing the duality $F\to\star F$ (equivalently $\vec E\to\vec B, \vec B\to -\vec E$) of source-free Maxwell theory.

The duality is more apparent: the source-free Maxwell theory is invariant under the **duality rotation** $F + i\star F \to e^{i\theta}(F + i\star F)$ for any real $\theta$ — a $\mathrm{U}(1)$ symmetry. Physically, this rotates electric into magnetic and back. Maxwell's theory is *symmetric* under this rotation in vacuum; charges break the symmetry. The complex self-dual combination $F + i\star F$ is the natural object exhibiting this symmetry.

**Step 5: Contrast with Riemannian $4$D (part (e)).**

On Euclidean $\mathbb{R}^4$ with signature $(+++ +)$ (so $s = 0$), $\star\star = (-1)^{2\cdot 2 + 0}\mathrm{id} = +\mathrm{id}$ on $\Omega^2$. The eigenvalues of $\star$ over $\mathbb{R}$ are $\pm 1$, and the eigenspace decomposition is $\Omega^2(\mathbb{R}^4) = \Omega^2_+\oplus\Omega^2_-$ over $\mathbb{R}$.

This is the algebraic shell of the **self-dual / anti-self-dual Yang–Mills equations**: on a Riemannian $4$-manifold, a connection's curvature $F_A$ is a $2$-form-valued in the adjoint bundle, and the decomposition $F_A = F_+ + F_-$ has the **self-duality equation** $F_- = 0$ (curvature is self-dual) as the equation for an **instanton**. [[Def - Instanton|Instantons]] are absolute minimizers of the Yang–Mills energy in their topological charge class.

The Lorentzian case has no real self-dual instantons (by part (b)). Riemannian instantons are obtained by **Wick rotation** $t \to it$, converting Lorentzian Minkowski into Euclidean $\mathbb{R}^4$. The Yang–Mills instantons of [[Gauge Theory IV — Yang–Mills Fields and Instantons]] live in the Wick-rotated (Riemannian) setting.

The structural reason: instanton equations require an involution structure on $\Omega^2$ (real eigenspace decomposition), which exists in Riemannian $4$D but not in Lorentzian. The "miracle of $4$D" is genuinely a Riemannian phenomenon.

> [!note]- Complete formal solution
> **Part (a):** $\star\star = (-1)^{k(n-k)+s}\mathrm{id}$ at $n = 4, k = 2, s = 1$: $\star\star = (-1)^5\mathrm{id} = -\mathrm{id}$ on $\Omega^2(M^{3,1})$.
>
> **Part (b):** Real eigenvalues $\lambda$ of $\star$ satisfy $\lambda^2 = -1$, impossible over $\mathbb{R}$. Over $\mathbb{C}$, $\lambda = \pm i$, giving complex self-dual / anti-self-dual decomposition $\Omega^2(M; \mathbb{C}) = \Omega^2_+\oplus\Omega^2_-$ with each summand rank $3$ over $\mathbb{C}$.
>
> **Part (c):** $\star(F + i\star F) = \star F + i\star\star F = \star F - iF = -i(F + i\star F)$. So $F + i\star F$ has $\star$-eigenvalue $-i$.
>
> **Part (d):** Maxwell's source-free equations $dF = 0$, $d\star F = 0$ combine into $d(F + i\star F) = 0$. The $\mathrm{U}(1)$ duality rotation $F + i\star F \to e^{i\theta}(F + i\star F)$ is a symmetry of source-free Maxwell theory.
>
> **Part (e):** On Riemannian $\mathbb{R}^4$, $\star\star = +\mathrm{id}$ on $\Omega^2$, giving real eigenvalues $\pm 1$ and the real self-dual/anti-self-dual decomposition $\Omega^2 = \Omega^2_+\oplus\Omega^2_-$. This is the setting for Yang–Mills instantons (self-dual connections). The Lorentzian case has no real self-dual structure; instantons require Wick rotation to Riemannian signature. $\qquad\blacksquare$

> [!warning] Illegal but tempting: assuming Lorentzian self-duality is just the Riemannian story
> The natural temptation is to compute self-dual electromagnetic fields on Minkowski space the same way as instantons on Euclidean $\mathbb{R}^4$. This fails because $\star^2 = -1$ in Lorentzian (not $+1$): the only real self-dual $2$-form is the zero form. The standard resolution is **Wick rotation** $t\to i\tau$, which converts Lorentzian to Euclidean signature and recovers the Riemannian self-duality story. In some references the Lorentzian "complex self-dual" combination $F + i\star F$ is used as a substitute, but it lives in $\Omega^2(M; \mathbb{C})$ — not $\Omega^2(M; \mathbb{R})$ — and represents a complex (not real) gauge field configuration.

---

# Key Takeaways

**The sign of $\star^2$ in middle dimension is the structural fact for self-duality.** On $\Omega^2$ in dimension $4$: $\star^2 = +1$ in Riemannian, $\star^2 = -1$ in Lorentzian (more generally, $(-1)^s$ where $s$ is the number of timelike directions). The sign determines whether self-duality is a real decomposition (Riemannian) or only a complex one (Lorentzian). This is the algebraic reason that Yang–Mills instantons live naturally in *Euclidean* (Wick-rotated) gauge theory, not Lorentzian quantum field theory directly. The trigger: see "$4$D self-duality" → "check signature": Riemannian gives real instantons, Lorentzian requires complex Wick rotation.

**Complex self-duality in Lorentzian $4$D = the complex Maxwell tensor.** The complex form $F + i\star F$ in Lorentzian $4$D is a complex self-dual $2$-form (eigenvalue $-i$ of $\star$), and it encodes the combined complex electromagnetic field $\vec E + i\vec B$ familiar from classical physics. The duality rotation $\vec E + i\vec B \to e^{i\theta}(\vec E + i\vec B)$ is the symmetry of source-free Maxwell theory, equivalent to rotating $F$ by the Hodge star. This is the simplest example of a **duality symmetry** in physics — the precursor to **electric-magnetic duality** in gauge theory, **S-duality** in string theory, and **Seiberg duality** in supersymmetric gauge theories.

**Wick rotation links Lorentzian and Riemannian.** The standard prescription "Wick rotation $t\to i\tau$" converts a Lorentzian metric $-dt^2 + dx^2 + \dots$ into a Riemannian metric $d\tau^2 + dx^2 + \dots$. This flips the sign of $\star^2$ on $2$-forms from $-1$ to $+1$, enabling real self-duality and instantons. Physical observables in some quantum field theories are computed via Wick rotation to Euclidean, then analytically continued back to Lorentzian — the entire infrastructure of **Euclidean quantum field theory** is built on this passage. The Hodge-theoretic interpretation: signature affects double-star, which affects self-duality, which affects gauge-theoretic structure. This is preview material for [[Gauge Theory IV — Yang–Mills Fields and Instantons]], where the Riemannian instanton story is developed.

This exercise complements [[Ex - Maxwell's Equations Use the Codifferential]] (Lorentzian form of Maxwell's equations) and previews **Yang–Mills self-duality** in Gauge Theory IV. The Riemannian case in [[Def - Self-Dual and Anti-Self-Dual Forms]] is the algebraic shell, instantiated as gauge-theoretic instanton equations.
