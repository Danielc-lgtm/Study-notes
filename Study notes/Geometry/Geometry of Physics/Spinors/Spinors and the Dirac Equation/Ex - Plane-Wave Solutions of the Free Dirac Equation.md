---
type: exercise
subject: spinors
difficulty: "⭐⭐"
prereqs:
  - "Def - The Dirac Equation"
  - "Def - Dirac Gamma Matrices"
  - "Thm - Dirac Equation Squares to Klein-Gordon"
tags: [geometry, spinors, quantum-mechanics, relativity, particle-physics]
---

# Problem Statement

Find all plane-wave solutions of the free Dirac equation $\not\partial\psi = m\psi$ on Minkowski space (Frankel signature $\eta = (- + + +)$). Specifically:

1. Look for solutions of the form $\psi(x) = u(p)e^{-ip\cdot x}$ with $p \cdot x = p_\mu x^\mu$ — these are *positive-frequency* plane waves with future-pointing four-momentum $p$.
2. Show that the algebraic equation for the polarization spinor $u(p)$ is $(\not p + im)u(p) = 0$ (in our sign convention).
3. Show that solutions exist iff $p^2 := \eta_{\mu\nu}p^\mu p^\nu = -m^2$ — the on-shell condition (massive particle dispersion).
4. Count the dimension of the solution space: for each on-shell $p$, there are exactly **two** independent positive-energy polarization spinors $u^{(s)}(p)$, indexed by $s = 1, 2$ (spin states).
5. Also find the **negative-frequency** plane waves $\psi(x) = v(p) e^{+ip\cdot x}$ for which $(\not p - im)v = 0$ — these have two independent solutions $v^{(s)}(p)$ corresponding to **antiparticles**.

Work in the Weyl basis and write the explicit solutions in the rest frame $p = (m, \vec 0)$.

**Recall:**

The Dirac equation:

![[Def - The Dirac Equation#The Definition]]

The gamma matrices satisfy $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$, with the consequence $\not p^2 = p^2 I$ (from [[Thm - Dirac Equation Squares to Klein-Gordon]]). The Feynman slash is $\not p = \gamma^\mu p_\mu = \gamma_\mu p^\mu$.

In the Weyl representation: $\gamma^0 = \begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix}$ and $\gamma^k = \begin{pmatrix} 0 & \sigma_k \\ \sigma_k & 0\end{pmatrix}$ (Frankel convention).

---

# Convergent Strategy

**Problem class:** *Constructing the elementary solutions of a linear PDE by ansatz.* The Dirac equation is linear with constant coefficients, so a Fourier-mode ansatz $\psi \propto e^{-ip\cdot x}$ converts the PDE into an algebraic equation for the amplitude $u(p)$. Counting independent solutions then gives the dimension of the solution space.

**Assumption pattern:** Given a constant-coefficient linear PDE, the natural ansatz is the plane wave $\psi \propto e^{-ip\cdot x}$. Substituting into the Dirac equation converts $\partial_\mu \to -ip_\mu$, so $\not\partial\psi \to -i\not p \psi$, and the equation becomes the *algebraic* eigenvalue-like problem $(\not p + im)u = 0$. The condition for non-zero solutions is that the matrix $\not p + im$ has non-trivial kernel — equivalently, $\det(\not p + im) = 0$, which gives the dispersion relation.

**Theorem routing:** Use $\not p^2 = p^2 I$ from [[Thm - Dirac Equation Squares to Klein-Gordon]] to factor $(\not p + im)(\not p - im) = \not p^2 + m^2 I = (p^2 + m^2)I$, giving the on-shell condition $p^2 = -m^2$. Then explicitly compute the kernel of $\not p + im$ on-shell using the Weyl rep, getting $2$ independent solutions per spin state.

**Key decision point:** The trickiest part is the *counting* of solutions. The matrix $\not p + im$ is $4 \times 4$; naively one expects up to $4$-dimensional kernel, but the on-shell factorisation $\not p^2 + m^2 = 0$ forces rank $\leq 2$ (the rank of $\not p - im$ as projector onto the orthogonal kernel of $\not p + im$). So the kernel has dimension exactly $2$, giving two independent polarization spinors per on-shell momentum — the "spin up" and "spin down" states for a massive particle.

---

# Legal Operations Used

1. **Operation 5 from the topic page (square the Dirac operator using the Clifford relation):** The factorisation $\not p^2 = p^2 I$ is essential: it converts the matrix equation $(\not p + im)u = 0$ into a *scalar* condition on $p$ via $(\not p + im)(\not p - im) = (p^2 + m^2)I$.

2. **Operation 9 from the topic page (use the projection $P_{L,R}$ to split a Dirac spinor):** In the Weyl basis, the Dirac spinor decomposes as $u = (u_L, u_R)^T$, and the Dirac equation decouples (for $m = 0$) into two Weyl equations. For $m \neq 0$, the chirality-coupled form makes the rest-frame solutions particularly transparent.

---

# Hints

> [!note]- Hint 1
> Substitute the ansatz into the Dirac equation: $\not\partial \psi = \gamma^\mu \partial_\mu (u(p) e^{-ip\cdot x}) = u(p) \gamma^\mu (-ip_\mu) e^{-ip\cdot x} = -i\not p \,u(p) e^{-ip\cdot x}$. Setting this equal to $m\psi = mu(p)e^{-ip\cdot x}$ gives $-i\not p u = mu$, i.e., $(\not p + im)u = 0$ (rearranging).

> [!note]- Hint 2
> Multiply the equation $(\not p + im)u = 0$ on the left by $(\not p - im)$: $(\not p - im)(\not p + im)u = (\not p^2 + m^2)u = (p^2 + m^2)u = 0$. For non-zero $u$, this forces $p^2 = -m^2$ — the on-shell condition (using Frankel signature, where the "mass shell" is $p_0^2 - \vec p^2 = m^2$, equivalently $-p^2 = m^2$, i.e., $p^2 = -m^2$).

> [!note]- Hint 3
> In the rest frame $p = (E, \vec 0) = (m, \vec 0)$: $\not p = \gamma^\mu p_\mu = \gamma^0 p_0 = -m\gamma^0$ (since $p_0 = \eta_{00}p^0 = -m$). Then $(\not p + im)u = (-m\gamma^0 + im)u = im(I - i\gamma^0/(-i))u = $... let me redo. With $p^0 = m$ (future-pointing) and $p_0 = \eta_{00}p^0 = -m$: $\not p = \gamma^\mu p_\mu = \gamma^0 p_0 + 0 = -m\gamma^0$. So the equation becomes $(-m\gamma^0 + im)u = 0$, i.e., $\gamma^0 u = i u$. In the Weyl rep, $\gamma^0 = \begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix}$, so $\gamma^0 \begin{pmatrix} u_L \\ u_R\end{pmatrix} = \begin{pmatrix} -u_R \\ u_L\end{pmatrix} = i\begin{pmatrix} u_L \\ u_R\end{pmatrix}$, giving $u_R = -iu_L$ and $u_L = iu_R$, consistent (both reduce to $u_L = iu_R$, i.e., $u_R = -iu_L$). So the rest-frame solutions are $u(p) = \begin{pmatrix} \chi \\ -i\chi\end{pmatrix}$ for any $\chi \in \mathbb{C}^2$, giving 2 solutions for the 2 spin states.

---

# Solution

The plan: substitute the plane-wave ansatz into the Dirac equation to get the algebraic condition $(\not p + im)u = 0$. Use $\not p^2 = p^2 I$ to derive the on-shell condition. Count the dimension of the solution space using the rank-nullity theorem for $\not p + im$. Explicitly write the rest-frame solutions in the Weyl basis.

**Step 1: The algebraic equation for the polarization spinor.**

The plane-wave ansatz $\psi(x) = u(p)e^{-ip\cdot x}$ converts $\not\partial\psi = m\psi$ into $(\not p + im)u(p) = 0$ for the amplitude $u$.

> [!note]- Derivation
> Substitute: $\partial_\mu(u(p) e^{-ip\cdot x}) = u(p) \cdot (-ip_\mu) e^{-ip\cdot x}$, so $\not\partial\psi = \gamma^\mu\partial_\mu\psi = -i\gamma^\mu p_\mu u(p) e^{-ip\cdot x} = -i\not p \,u(p) e^{-ip\cdot x}$.
>
> The Dirac equation $\not\partial\psi = m\psi$ becomes $-i\not p \,u(p) = m\,u(p)$, i.e., $\not p\,u(p) = im\,u(p)$, or $(\not p - im)u(p) = 0$. (Sign correction: I had $+im$ earlier; the correct sign in our Frankel convention is $\not p\,u = im\,u$, equivalently $(\not p - im)u = 0$.) The two conventions differ by where the $i$ sits; we proceed with $(\not p - im)u = 0$.

**Step 2: On-shell condition $p^2 = -m^2$.**

The equation $(\not p - im)u = 0$ has non-zero solutions iff $p^2 = -m^2$.

> [!note]- Derivation
> Multiply on the left by $(\not p + im)$: $(\not p + im)(\not p - im)u = (\not p^2 - (im)^2)u = (\not p^2 + m^2)u = 0$.
>
> Using $\not p^2 = p^2 I$ from [[Thm - Dirac Equation Squares to Klein-Gordon]] (more precisely: $\not p^2 = \tfrac{1}{2}\{\gamma^\mu, \gamma^\nu\}p_\mu p_\nu = \eta^{\mu\nu}p_\mu p_\nu I = p^2 I$, where $p^2 = \eta^{\mu\nu}p_\mu p_\nu = p_\mu p^\mu$):
> $$(p^2 + m^2)u = 0.$$
> For $u \neq 0$, this forces $p^2 = -m^2$. With our convention $p^2 = \eta_{\mu\nu}p^\mu p^\nu = -(p^0)^2 + \vec p^2$, the on-shell condition $p^2 = -m^2$ is $(p^0)^2 = \vec p^2 + m^2$, equivalently $E^2 = \vec p^2 + m^2$ — the relativistic dispersion relation.

**Step 3: Count solutions.**

For each on-shell $p$, the kernel of $(\not p - im)$ has dimension $2$, giving two independent polarization spinors.

> [!note]- Derivation
> On the mass shell $p^2 = -m^2$, $(\not p)^2 = -m^2 I$, so the operator $\not p$ has eigenvalues $\pm im$. The eigenspaces are $2$-dimensional each (since the total dimension is $4$ and the two eigenvalues account for all eigenvectors). The kernel of $(\not p - im)$ is the eigenspace with eigenvalue $+im$, which is $2$-dimensional.
>
> Alternatively: in the rest frame $p = (m, \vec 0)$, $\not p = -m\gamma^0$, so $\not p - im = -m\gamma^0 - im = -m(\gamma^0 + iI)$. In the Weyl rep, $\gamma^0 + iI = \begin{pmatrix} iI_2 & -I_2 \\ I_2 & iI_2\end{pmatrix}$, which has rank $2$ (the kernel is 2-dimensional). So the rest-frame solutions form a 2-dimensional space.

**Step 4: Explicit rest-frame solutions.**

In the rest frame $p = (m, \vec 0)$, the solutions are $u^{(s)}(p) = \sqrt{2m}\begin{pmatrix} \xi^{(s)} \\ -i\xi^{(s)}\end{pmatrix}$ for $s = 1, 2$, with $\xi^{(s)}$ a basis of $\mathbb{C}^2$. (The factor of $\sqrt{2m}$ is a normalisation convention.)

> [!note]- Derivation
> Solve $\gamma^0 u = i u$ (from $\not p u = im u$ with $\not p = -m\gamma^0$, divide both sides by $-m$: $\gamma^0 u = -i u$... let me redo carefully). Actually with $\not p = -m\gamma^0$ and the equation $\not p u = imu$: $-m\gamma^0 u = imu$, so $\gamma^0 u = -iu$.
>
> In the Weyl rep with $u = (u_L, u_R)^T$: $\gamma^0 u = \begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix}\begin{pmatrix} u_L \\ u_R\end{pmatrix} = \begin{pmatrix} -u_R \\ u_L\end{pmatrix} = -i\begin{pmatrix} u_L \\ u_R\end{pmatrix} = \begin{pmatrix} -iu_L \\ -iu_R\end{pmatrix}$.
>
> So $u_R = iu_L$ and $u_L = -iu_R$. The two equations are consistent (verify: $u_R = iu_L = i(-iu_R) = u_R$ ✓). So the general solution is $u(p) = \begin{pmatrix} \chi \\ i\chi\end{pmatrix}$ for any $\chi \in \mathbb{C}^2$ — a 2-dimensional space.
>
> Choosing a basis $\xi^{(1)} = \begin{pmatrix}1 \\ 0\end{pmatrix}$ and $\xi^{(2)} = \begin{pmatrix}0 \\ 1\end{pmatrix}$ of $\mathbb{C}^2$, the rest-frame spin states are $u^{(1)}(p_{\mathrm{rest}}) = \sqrt{2m}\begin{pmatrix}1 \\ 0 \\ i \\ 0\end{pmatrix}$ and $u^{(2)}(p_{\mathrm{rest}}) = \sqrt{2m}\begin{pmatrix}0 \\ 1 \\ 0 \\ i\end{pmatrix}$, where the normalisation $\sqrt{2m}$ ensures $\bar u^{(s)}u^{(s')} = 2m\delta_{ss'}$ (the standard convention).
>
> For a general (non-rest) momentum, the solutions can be obtained by Lorentz-boosting the rest-frame solutions using the spinor representation $\rho(A) = \mathrm{diag}(A, (A^\dagger)^{-1})$ corresponding to the boost.

**Step 5: Negative-frequency solutions.**

The ansatz $\psi(x) = v(p)e^{+ip\cdot x}$ gives the equation $(\not p + im)v(p) = 0$, with two independent solutions $v^{(s)}(p)$ for each on-shell $p$ — the antiparticle modes.

> [!note]- Derivation
> Substitute: $\not\partial\psi = +i\not p v(p)e^{+ip\cdot x}$, so the Dirac equation becomes $+i\not p v = mv$, i.e., $\not p v = -imv$, equivalently $(\not p + im)v = 0$.
>
> The same factorisation argument gives $p^2 = -m^2$ on shell. The kernel of $(\not p + im)$ is the eigenspace of $\not p$ with eigenvalue $-im$, which is 2-dimensional (the complementary eigenspace to the $u(p)$ kernel).
>
> In the rest frame: $\gamma^0 v = +iv$. In the Weyl rep, this gives $v_R = -iv_L$, opposite sign from the $u(p)$ case. So $v^{(s)}(p_{\mathrm{rest}}) = \sqrt{2m}\begin{pmatrix}\eta^{(s)} \\ -i\eta^{(s)}\end{pmatrix}$ for a basis $\eta^{(s)}$ of $\mathbb{C}^2$. These are the **antiparticle spinors**; in the second-quantised theory they create antiparticles when contracted with creation operators.

> [!note]- Complete formal solution
> *Plane-wave ansatz.* Substituting $\psi(x) = u(p)e^{-ip\cdot x}$ into $\not\partial\psi = m\psi$ gives $-i\not p\,u(p) = m\,u(p)$, i.e., $\not p \,u = im\,u$, or $(\not p - im)u = 0$.
>
> *On-shell condition.* Multiplying by $(\not p + im)$: $(\not p^2 + m^2)u = (p^2 + m^2)u = 0$. For $u \neq 0$: $p^2 = -m^2$, the relativistic dispersion relation $E^2 = \vec p^2 + m^2$.
>
> *Solution counting.* On shell, $\not p$ has eigenvalues $\pm im$, each with $2$-dimensional eigenspace. The "particle" solutions $u(p)$ have eigenvalue $+im$; there are 2 independent such $u$ for each on-shell $p$, labeled by spin.
>
> *Rest-frame solutions.* In the rest frame $p = (m, \vec 0)$, $\not p = -m\gamma^0$. The equation $\gamma^0 u = -iu$ in the Weyl rep $u = (u_L, u_R)^T$ gives $u_R = iu_L$. Taking $\xi^{(s)}$ a basis of $\mathbb{C}^2$ (e.g., $\xi^{(1)} = (1, 0)^T$, $\xi^{(2)} = (0, 1)^T$), the rest-frame solutions are $u^{(s)}(p_{\mathrm{rest}}) = \sqrt{2m}(\xi^{(s)}, i\xi^{(s)})^T$.
>
> *Antiparticle solutions.* The ansatz $v(p)e^{+ip\cdot x}$ gives $(\not p + im)v = 0$, equivalent to $\gamma^0 v = +iv$ in the rest frame, yielding $v^{(s)}(p_{\mathrm{rest}}) = \sqrt{2m}(\eta^{(s)}, -i\eta^{(s)})^T$ for a basis $\eta^{(s)}$ — the antiparticle modes.
>
> For general momenta, both $u^{(s)}(p)$ and $v^{(s)}(p)$ are obtained by Lorentz-boosting the rest-frame solutions using the spin representation.

---

# Key Takeaways

**The "$4$-dimensional Dirac spinor = $2$ spin states $\times$ ($1$ particle + $1$ antiparticle)" decomposition.** The total Dirac spinor space $\mathbb{C}^4$ accommodates $4$ degrees of freedom: $2$ from spin (up/down) and $2$ from particle/antiparticle. The plane-wave count makes this explicit: for each on-shell momentum $p$, there are $2$ particle modes $u^{(1)}(p), u^{(2)}(p)$ and $2$ antiparticle modes $v^{(1)}(p), v^{(2)}(p)$. In the quantized theory, $u$ becomes a particle annihilation amplitude and $v$ a antiparticle creation amplitude, giving the Dirac field expansion $\hat\psi = \sum_{s, p}[\hat b_s(p)u^{(s)}(p)e^{-ip\cdot x} + \hat d_s^\dagger(p)v^{(s)}(p)e^{+ip\cdot x}]$. This decomposition is what gives the Dirac field its rich structure — and is why the prediction of antimatter is mathematically inevitable.

**The on-shell condition $p^2 = -m^2$ emerges algebraically from the squaring of the Dirac operator.** No "physical" input is needed beyond the Clifford algebra and the plane-wave ansatz: the algebraic factorisation $(\not p + im)(\not p - im) = p^2 + m^2$ forces $p^2 = -m^2$ for non-zero solutions. The Dirac equation thus *automatically* gives the relativistic dispersion relation, just as desired. This is the cleanest justification of why the Dirac equation is "the right" relativistic wave equation for spin-$\tfrac{1}{2}$ particles.

**The rest-frame analysis is the natural starting point for explicit Dirac solutions.** Every Dirac spinor's structure on a general momentum $p$ can be obtained by *boosting* the rest-frame solution via the spinor Lorentz transformation $\rho(A)$. The rest frame $p = (m, \vec 0)$ trivialises the equation to an eigenvalue problem on $\gamma^0$, which is straightforward to solve. The boost from rest frame to general momentum is the **Wigner construction**: pick any reference momentum on the mass shell (the rest frame), find the stabilizer (rotations $SU(2)$ for massive particles), build the spin representations there, and induce up to the full Lorentz group. This is the modern foundation of relativistic quantum mechanics.
