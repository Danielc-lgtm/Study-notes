---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - The Maurer-Cartan Form"
  - "Thm - Maurer-Cartan Equation"
  - "Def - The Lie Algebra of a Lie Group"
tags: [geometry, gauge-theory, lie-groups, differential-forms]
---

# Problem Statement

Compute the Maurer-Cartan form $\theta_{SU(2)} \in \Omega^1(SU(2); \mathfrak{su}(2))$ on the Lie group $SU(2)$ in a concrete parametrisation, and verify the Maurer-Cartan equation.

**(a)** Parametrise $SU(2) = \{g = a\,1 + i b^a\sigma_a : a, b^a \in \mathbb{R}, a^2 + b^a b_a = 1\}$ where $\sigma_a$ ($a = 1, 2, 3$) are the Pauli matrices and $1$ is the $2 \times 2$ identity. Show this gives a diffeomorphism $SU(2) \cong S^3 \subset \mathbb{R}^4$.

**(b)** Choose a basis of $\mathfrak{su}(2) = \{i\sigma_a/2 : a = 1, 2, 3\}$ (anti-Hermitian traceless $2 \times 2$ matrices). Compute the Maurer-Cartan form $\theta_{SU(2)} = g^{-1}dg$ in the parametrisation of (a), and express it as
$$
\theta_{SU(2)} = \frac{i\sigma_a}{2} \otimes \tilde\sigma^a
$$
for three left-invariant 1-forms $\tilde\sigma^a$ on $SU(2) \cong S^3$.

**(c)** Verify the Maurer-Cartan equation in basis form: $d\tilde\sigma^a + \tfrac{1}{2}\varepsilon^a{}_{bc}\tilde\sigma^b \wedge \tilde\sigma^c = 0$. (This uses the structure constants of $\mathfrak{su}(2)$: $[i\sigma_a/2, i\sigma_b/2] = -\varepsilon_{abc}\,i\sigma_c/2$, so $C^a{}_{bc} = -\varepsilon^a{}_{bc}$... sign conventions vary; verify either $\pm$.)

**Recall:**

![[Def - The Maurer-Cartan Form#The Definition]]

![[Thm - Maurer-Cartan Equation#Statement]]

The Lie algebra $\mathfrak{su}(2)$ consists of anti-Hermitian traceless $2 \times 2$ matrices, and a standard basis is $\{i\sigma_a/2\}$ where $\sigma_1 = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$, $\sigma_2 = \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}$, $\sigma_3 = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$. The bracket is $[\sigma_a, \sigma_b] = 2i\varepsilon_{abc}\sigma_c$, so $[i\sigma_a/2, i\sigma_b/2] = -\varepsilon_{abc}(i\sigma_c/2)$.

---

# Convergent Strategy

**Problem class:** This is a *concrete-computation-of-an-invariant-1-form* problem. The general pattern is: given a Lie group $G$ in some explicit parametrisation, compute its Maurer-Cartan form $g^{-1}dg$ and verify the Maurer-Cartan equation. The problem-solving routine reduces to matrix algebra (compute $g^{-1}$ and $dg$, then multiply) plus exterior calculus (compute $d\tilde\sigma^a$ and verify the structural identity).

**Assumption pattern:** $SU(2)$ is a *matrix Lie group* (the matrix-group notation $g^{-1}dg$ is well-defined). The parametrisation in (a) is explicit ($g = a + ib^a\sigma_a$ with $a^2 + b^a b_a = 1$). The Lie algebra basis $\{i\sigma_a/2\}$ is fixed and Pauli matrices' algebra is standard. These three pieces together let us write everything down in components.

**Theorem routing:** [[Def - The Maurer-Cartan Form|Definition of the Maurer-Cartan form]] gives the formula $\theta_G = g^{-1}dg$ in matrix notation. [[Thm - Maurer-Cartan Equation|Maurer-Cartan equation]] gives the structural identity $d\theta + \tfrac{1}{2}[\theta, \theta] = 0$, equivalent in basis form to $d\tilde\sigma^a + \tfrac{1}{2}C^a{}_{bc}\tilde\sigma^b \wedge \tilde\sigma^c = 0$ with $C^a{}_{bc}$ the structure constants. The verification is direct: compute $d\tilde\sigma^a$ from the formula for $\tilde\sigma^a$ in coordinates, then check the algebra matches.

**Key decision point:** The non-obvious choice is how to parametrise $SU(2)$. The "Euler-angle" parametrisation $g = e^{i\alpha\sigma_3/2}e^{i\beta\sigma_2/2}e^{i\gamma\sigma_3/2}$ leads to messy formulas; the "axis-angle" parametrisation $g = \cos(\theta/2) + i\sin(\theta/2)(n^a\sigma_a)$ (with $\hat n$ a unit vector) is cleaner; the "linear" parametrisation $g = a + ib^a\sigma_a$ with $a^2 + b^a b_a = 1$ is the cleanest for the structural-equation verification. We use the third.

---

# Legal Operations Used

1. **Operation 1 (pull back / compute $g^{-1}dg$ explicitly).** From the topic page's legal operations, this is the routine "compute the Maurer-Cartan form by matrix algebra". *Application:* expand $g = a + ib^a\sigma_a$, compute $g^{-1} = g^\dagger$ (since $g$ is unitary), then $g^{-1}dg = (a - ib^a\sigma_a)(da + i\,db^b\sigma_b)$. Expand using $\sigma_a\sigma_b = \delta_{ab}1 + i\varepsilon_{abc}\sigma_c$.

3. **Operation 3 (structural equation).** Verify the curvature of the canonical flat connection $\theta_G$ is zero by computing $d\theta_G + \tfrac{1}{2}[\theta_G, \theta_G] = 0$.

10. **Operation 10 (abelian sanity check).** The abelian case is $G = U(1)$; for $SU(2)$ the bracket is non-trivial ($[\sigma_a, \sigma_b] = 2i\varepsilon_{abc}\sigma_c$), so the $[\theta, \theta]$ term is non-zero and contributes to the calculation. Sanity check that this is consistent with the $\mathfrak{su}(2)$ structure constants.

---

# Hints

> [!note]- Hint 1
> For part (a), the constraint $\det g = 1$ for $g = a + ib^a\sigma_a$ gives $a^2 + b^a b_a = 1$, which is exactly the equation of $S^3 \subset \mathbb{R}^4$. So $(a, b^1, b^2, b^3) \in S^3$ parametrises $SU(2)$.

> [!note]- Hint 2
> For part (b), use $g^{-1} = g^\dagger = a - ib^a\sigma_a$. Then $g^{-1}dg = (a - ib^a\sigma_a)(da + idb^b\sigma_b)$. Expanding: $g^{-1}dg = a\,da + ia\,db^b\sigma_b - ib^a\sigma_a\,da + b^a b^b\sigma_a\sigma_b$. Use $\sigma_a\sigma_b = \delta_{ab}1 + i\varepsilon_{abc}\sigma_c$ and the constraint $a\,da + b^a\,db_a = 0$ (from differentiating $a^2 + b^a b_a = 1$).

> [!note]- Hint 3
> After simplification, the $\sigma_0 = 1$ (identity) coefficient must vanish (it should not appear in $\mathfrak{su}(2)$). The coefficients of $\sigma_a$ give the three left-invariant 1-forms:
> $$
> \tilde\sigma^a = 2(a\,db^a - b^a\,da + \varepsilon^a{}_{bc}b^b\,db^c)
> $$
> (or equivalent up to sign conventions). Verify the prefactor "2" from the convention $\theta_{SU(2)} = (i\sigma_a/2)\tilde\sigma^a$.

> [!note]- Hint 4
> For part (c), compute $d\tilde\sigma^a$ directly. The non-trivial part is $d(a\,db^a - b^a\,da) = 2\,da \wedge db^a$ (since $d(b^a\,da) = db^a \wedge da = -da \wedge db^a$). And $d(\varepsilon^a{}_{bc}b^b\,db^c) = \varepsilon^a{}_{bc}\,db^b \wedge db^c$. The two pieces combine, and using $a^2 + b^a b_a = 1 \Rightarrow a\,da = -b^a\,db_a$, one verifies the Maurer-Cartan equation.

> [!note]- Hint 5
> The cleanest verification uses the matrix form directly: $d(g^{-1}dg) = d(g^{-1})\wedge dg = -g^{-1}(dg)g^{-1}\wedge dg = -(g^{-1}dg)\wedge(g^{-1}dg)$. So $d\theta_G + \theta_G \wedge \theta_G = 0$ as a matrix identity. Then use $\tfrac{1}{2}[\theta_G, \theta_G] = \theta_G\wedge\theta_G$ for matrix-group 1-forms to get the Maurer-Cartan equation.

---

# Solution

**Plan:** The proof breaks into three steps. Step 1 establishes the diffeomorphism $SU(2) \cong S^3$ by verifying the constraint $a^2 + b^a b_a = 1$. Step 2 computes the Maurer-Cartan form $g^{-1}dg$ in components, identifying the three left-invariant 1-forms $\tilde\sigma^a$. Step 3 verifies the Maurer-Cartan equation either via the matrix identity $d(g^{-1}dg) + (g^{-1}dg)\wedge(g^{-1}dg) = 0$ or by direct computation of $d\tilde\sigma^a$ in components.

**Step 1: $SU(2) \cong S^3$.**

Any $g \in SU(2)$ satisfies $g g^\dagger = 1$ and $\det g = 1$. Write $g = a + ib^a\sigma_a$ with $a \in \mathbb{R}$ and $b^a \in \mathbb{R}$ (so $g$ is a complex linear combination of $1$ and $i\sigma_a$, with real coefficients on each).

> [!note]- Derivation
> Any $2 \times 2$ complex matrix can be uniquely written as $g = c_0 \cdot 1 + c^a\sigma_a$ with $c_0, c^a \in \mathbb{C}$, since $\{1, \sigma_1, \sigma_2, \sigma_3\}$ is a basis of $M_2(\mathbb{C})$ over $\mathbb{C}$. For $g$ unitary ($gg^\dagger = 1$):
> $$
> g g^\dagger = (c_0 + c^a\sigma_a)(\bar c_0 + \bar c^b\sigma_b) = |c_0|^2 + |\vec c|^2 + 2\mathrm{Re}(c_0\bar c^a)\sigma_a + \text{cross terms}.
> $$
> Setting equal to $1$ and requiring the constraint, after some calculation we get: $c_0 = a$ real, $c^a = ib^a$ with $b^a$ real, and $a^2 + b^a b_a = 1$. Then $\det g = a^2 + (b^1)^2 + (b^2)^2 + (b^3)^2 = 1$ automatically — the unit-determinant condition is equivalent to the unit-norm condition on $(a, b^1, b^2, b^3)$.
> 
> So $SU(2)$ is parametrised by $(a, b^1, b^2, b^3) \in S^3 \subset \mathbb{R}^4$ — a diffeomorphism, since the parametrisation is smooth in both directions.

**Step 2: Compute $\theta_{SU(2)} = g^{-1}dg$ and identify $\tilde\sigma^a$.**

For $g = a + ib^a\sigma_a$ with $a^2 + b^a b_a = 1$, $g^{-1} = g^\dagger = a - ib^a\sigma_a$. Compute:
$$
\theta_{SU(2)} = g^{-1}dg = (a - ib^c\sigma_c)(da + i\,db^d\sigma_d).
$$

> [!note]- Derivation
> Expand the product:
> $$
> \theta = a\,da + ia\,db^d\sigma_d - ib^c\sigma_c\,da + b^c b^d\sigma_c\sigma_d.
> $$
> Use $\sigma_c\sigma_d = \delta_{cd}\,1 + i\varepsilon_{cde}\sigma_e$:
> $$
> b^c b^d\sigma_c\sigma_d = b^c b^c\,1 + i\,b^c b^d\varepsilon_{cde}\sigma_e = b^c b^c\,1 + 0
> $$
> (the second term vanishes by antisymmetry of $\varepsilon$ against $b^c b^d$ symmetric).
> 
> Also, the cross terms give:
> - $ia\,db^d\sigma_d - ib^c\sigma_c\,da = i(a\,db^d - b^d\,da)\sigma_d$ (relabeling indices).
> 
> Combining:
> $$
> \theta = a\,da + b^c b^c \cdot 1 + i(a\,db^d - b^d\,da)\sigma_d.
> $$
> Wait — but we need to be careful: in $b^c b^d \sigma_c \sigma_d$, the $\sigma_c \sigma_d$ is being differentiated, not the $b$. Let me redo. The form $\theta = g^{-1}dg$ involves $dg = da + i\,db^d\sigma_d$ (the differential is *only* on the $a, b^d$, the $\sigma$'s are constant). The product:
> $$
> \theta = (a - ib^c\sigma_c)(da + i\,db^d\sigma_d) = a\,da + i a\,db^d\sigma_d - ib^c\sigma_c\,da - i^2 b^c\sigma_c\,db^d\sigma_d.
> $$
> $-i^2 = 1$, so the last term is $b^c\,db^d\sigma_c\sigma_d = b^c\,db^d(\delta_{cd}\,1 + i\varepsilon_{cde}\sigma_e)$.
> 
> Combining:
> $$
> \theta = a\,da + b^c\,db^c \cdot 1 + i(a\,db^d - b^d\,da)\sigma_d + ib^c\,db^d\varepsilon_{cde}\sigma_e.
> $$
> Now the constraint $a^2 + b^c b^c = 1 \Rightarrow a\,da + b^c\,db^c = 0$. So the coefficient of $1$ vanishes — as expected, since $\theta$ should be $\mathfrak{su}(2)$-valued (anti-Hermitian traceless).
> 
> Relabeling indices for clarity (let $e = a$ in the $\varepsilon$-term, and combine into the $\sigma_a$-coefficient):
> $$
> \theta = i\sigma_a \cdot \big[ (a\,db^a - b^a\,da) + \varepsilon^a{}_{bc}b^b\,db^c \big].
> $$
> 
> In the convention $\theta_{SU(2)} = (i\sigma_a/2)\tilde\sigma^a$, we have
> $$
> \tilde\sigma^a = 2\big[(a\,db^a - b^a\,da) + \varepsilon^a{}_{bc}b^b\,db^c\big].
> $$
> These are the three left-invariant 1-forms on $SU(2) \cong S^3$.

**Step 3: Verify the Maurer-Cartan equation.**

**Method 1 (matrix identity).** Compute $d\theta + \theta \wedge \theta = 0$ as a matrix identity, then convert to basis form via $\tfrac{1}{2}[\theta, \theta] = \theta \wedge \theta$.

> [!note]- Derivation
> By the matrix-group identity (Frankel Ch 17):
> $$
> d(g^{-1}dg) = -g^{-1}(dg)g^{-1}\wedge dg = -(g^{-1}dg)\wedge(g^{-1}dg).
> $$
> So $d\theta + \theta \wedge \theta = 0$. For matrix Lie algebras, $\tfrac{1}{2}[\theta, \theta] = \theta \wedge \theta$ (where the wedge is the matrix wedge of 1-forms), so $d\theta + \tfrac{1}{2}[\theta, \theta] = 0$ — the Maurer-Cartan equation. ∎

**Method 2 (basis form).** Compute $d\tilde\sigma^a$ in coordinates and verify the structural identity $d\tilde\sigma^a + \tfrac{1}{2}C^a{}_{bc}\tilde\sigma^b \wedge \tilde\sigma^c = 0$ with the appropriate structure constants.

> [!note]- Derivation
> Structure constants: $[i\sigma_a/2, i\sigma_b/2] = -\varepsilon_{abc}(i\sigma_c/2)$, so $C^c{}_{ab} = -\varepsilon^c{}_{ab}$ (Frankel's convention). The Maurer-Cartan equation in basis form reads
> $$
> d\tilde\sigma^c + \tfrac{1}{2}(-\varepsilon^c{}_{ab})\tilde\sigma^a \wedge \tilde\sigma^b = 0, \quad \text{i.e.,} \quad d\tilde\sigma^c = \tfrac{1}{2}\varepsilon^c{}_{ab}\tilde\sigma^a \wedge \tilde\sigma^b.
> $$
> (Some references absorb factors of 2 differently; verify the prefactor against the chosen normalisation.)
> 
> Compute $d\tilde\sigma^c$ from the explicit formula (above): $\tilde\sigma^c = 2(a\,db^c - b^c\,da + \varepsilon^c{}_{de}b^d\,db^e)$.
> $$
> d\tilde\sigma^c = 2(da \wedge db^c - db^c \wedge da + \varepsilon^c{}_{de}\,db^d \wedge db^e) = 2(2\,da \wedge db^c + \varepsilon^c{}_{de}\,db^d \wedge db^e).
> $$
> Wait, $d(a\,db^c) = da \wedge db^c + 0$ (since $d(db^c) = 0$); $d(b^c\,da) = db^c \wedge da = -da \wedge db^c$. So $d(a\,db^c - b^c\,da) = da \wedge db^c - (-da \wedge db^c) = 2\,da \wedge db^c$. ✓
> 
> And $d(\varepsilon^c{}_{de}b^d\,db^e) = \varepsilon^c{}_{de}\,db^d \wedge db^e$. ✓
> 
> So $d\tilde\sigma^c = 4\,da \wedge db^c + 2\varepsilon^c{}_{de}\,db^d \wedge db^e$.
> 
> Now compute $\tilde\sigma^a \wedge \tilde\sigma^b$ and form $\varepsilon^c{}_{ab}\tilde\sigma^a \wedge \tilde\sigma^b$. This is a computation involving $a, b^a$ and their differentials. After using $a^2 + b^a b_a = 1 \Rightarrow a\,da = -b^a\,db_a$, the answer must equal $d\tilde\sigma^c$ as derived above. The verification is direct but tedious; the result is the Maurer-Cartan equation $d\tilde\sigma^c = \tfrac{1}{2}\varepsilon^c{}_{ab}\tilde\sigma^a \wedge \tilde\sigma^b$ (or with an opposite sign, depending on the convention).

> [!note]- Complete formal solution
> **Step 1:** Parametrise $SU(2) = \{g = a + ib^a\sigma_a : (a, b^a) \in \mathbb{R}^4, a^2 + b^a b_a = 1\}$ — the unit sphere $S^3 \subset \mathbb{R}^4$. The diffeomorphism is smooth in both directions: $g \mapsto (a, b^a)$ extracts the coefficients in the Pauli-matrix basis, and the inverse $(a, b^a) \mapsto g$ assembles the matrix.
> 
> **Step 2:** Compute $\theta_{SU(2)} = g^{-1}dg$ for $g = a + ib^a\sigma_a, g^{-1} = a - ib^a\sigma_a$:
> $$
> \theta = (a - ib^c\sigma_c)(da + i\,db^d\sigma_d).
> $$
> Expand using $\sigma_c\sigma_d = \delta_{cd}1 + i\varepsilon_{cde}\sigma_e$:
> $$
> \theta = (a\,da + b^c\,db_c)\cdot 1 + i\sigma_a\big[(a\,db^a - b^a\,da) + \varepsilon^a{}_{bc}b^b\,db^c\big].
> $$
> The coefficient of $1$ vanishes by the constraint $a^2 + b^a b_a = 1 \Rightarrow a\,da + b^c\,db_c = 0$. So $\theta = i\sigma_a \cdot [(a\,db^a - b^a\,da) + \varepsilon^a{}_{bc}b^b\,db^c]$.
> 
> Identifying $\theta = (i\sigma_a/2)\tilde\sigma^a$:
> $$
> \tilde\sigma^a = 2\big[(a\,db^a - b^a\,da) + \varepsilon^a{}_{bc}b^b\,db^c\big].
> $$
> These are the three left-invariant 1-forms on $SU(2) \cong S^3$.
> 
> **Step 3:** Verify the Maurer-Cartan equation via the matrix identity. Compute $d(g^{-1}dg)$:
> $$
> d(g^{-1}dg) = d(g^{-1})\wedge dg = -g^{-1}(dg)g^{-1}\wedge dg = -(g^{-1}dg)\wedge(g^{-1}dg) = -\theta\wedge\theta.
> $$
> So $d\theta + \theta\wedge\theta = 0$. For matrix Lie algebras, $\theta\wedge\theta = \tfrac{1}{2}[\theta, \theta]$ (the matrix wedge of a 1-form with itself is half its self-bracket), so
> $$
> d\theta_{SU(2)} + \tfrac{1}{2}[\theta_{SU(2)}, \theta_{SU(2)}] = 0
> $$
> — the Maurer-Cartan equation for $SU(2)$. In basis form:
> $$
> d\tilde\sigma^c = \tfrac{1}{2}\varepsilon^c{}_{ab}\tilde\sigma^a \wedge \tilde\sigma^b
> $$
> (or with opposite sign depending on convention).
> 
> This completes the verification. ∎

> [!warning] Illegal but tempting alternative route
> One might be tempted to "verify" the Maurer-Cartan equation by *defining* $\tilde\sigma^a$ via the equation $d\tilde\sigma^c = \tfrac{1}{2}\varepsilon^c{}_{ab}\tilde\sigma^a \wedge \tilde\sigma^b$ from the structure constants alone — i.e., by writing down the equation and *assuming* solutions exist. This is backwards: the Maurer-Cartan equation is a *theorem*, not a definition. The 1-forms $\tilde\sigma^a$ are *defined* as the components of $g^{-1}dg$ in the chosen Pauli-matrix basis, and the equation must be *verified* from this definition. The alternative route would only work if you knew, a priori, that the equation has a unique solution up to gauge — which is true (it's the Maurer-Cartan equation on $SU(2)$, and the solution is unique up to left translation), but requires its own argument. Best practice: compute $\tilde\sigma^a$ explicitly first, then verify.

---

# Key Takeaways

**The Maurer-Cartan form on a matrix group is mechanical to compute — just matrix algebra plus Pauli-matrix identities.** Whenever you face a "compute $\theta_G$" problem for a matrix group, the routine is: choose a parametrisation, write $g$ and $g^{-1}$ in matrix form, multiply $g^{-1} \cdot dg$ using the Pauli (or Gell-Mann, or other) algebra. The result is a matrix of 1-forms, and you extract the Lie-algebra components by reading off the basis coefficients. For $SU(2)$, the basis is $\{i\sigma_a/2\}$; for $SU(3)$, it would be $\{iT_A/2\}$ with the Gell-Mann matrices; for $SO(n)$, the basis of antisymmetric matrices. The mechanical routine is the same.

**The Maurer-Cartan equation is a tautology in matrix-group form, then specialised to a basis.** The matrix identity $d(g^{-1}dg) + (g^{-1}dg)\wedge(g^{-1}dg) = 0$ is *automatic* from $d(g^{-1}) = -g^{-1}(dg)g^{-1}$ — a one-line computation. This is the cleanest derivation of the Maurer-Cartan equation, and it works for any matrix Lie group. The specialisation to basis form (with explicit structure constants) is then just extracting the components. This pattern — "do everything in matrix form, then extract components" — is the universal recipe in gauge theory.

**The 1-forms $\tilde\sigma^a$ are a left-invariant parallelisation of $S^3$.** A key feature of $SU(2) \cong S^3$ is that it is **parallelisable**: it admits a global frame of nowhere-vanishing vector fields (the left-invariant ones), equivalently a global frame of left-invariant 1-forms (the $\tilde\sigma^a$). This is rare among manifolds — only $S^1, S^3$, and $S^7$ among spheres are parallelisable. The Maurer-Cartan computation gives an explicit parallelisation, and the Maurer-Cartan equation is the integrability condition that this parallelisation defines a flat connection. (Compare with $S^2$, which is *not* parallelisable: the hairy-ball theorem says any vector field has a zero. The Hopf fibration $S^3 \to S^2$ is the principal $U(1)$-bundle structure that relates $S^3$ (parallelisable) to $S^2$ (not parallelisable) via the $U(1)$-fibre direction.)

**Trigger-reaction pattern: "structural equation for a Lie group" → "Maurer-Cartan + structure constants".** Whenever you encounter a connection structural equation, the first check is "is this just the Maurer-Cartan equation in disguise?" — for a flat connection on a Lie group, yes; for a general connection, the deformation $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$ is the *general* form, with the Maurer-Cartan equation being the *flat* special case. This perspective unifies the structural equation across all connections.
