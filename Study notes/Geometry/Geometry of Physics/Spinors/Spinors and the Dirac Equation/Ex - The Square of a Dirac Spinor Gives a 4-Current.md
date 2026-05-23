---
type: exercise
subject: spinors
difficulty: "⭐⭐"
prereqs:
  - "Def - The Dirac Equation"
  - "Def - Dirac Gamma Matrices"
tags: [geometry, spinors, quantum-mechanics, relativity]
---

# Problem Statement

Let $\psi: \mathbb{R}^{1,3} \to \mathbb{C}^4$ be a solution of the Dirac equation $\not\partial\psi = m\psi$, and let $\bar\psi = \psi^\dagger \gamma^0$ be its Dirac conjugate. Define the **Dirac probability current**
$$j^\mu := \bar\psi \gamma^\mu \psi = \psi^\dagger \gamma^0\gamma^\mu \psi.$$
Show:
1. $j^\mu$ is a Lorentz $4$-vector — i.e., it transforms as $j^\mu \mapsto \Lambda^\mu_{\;\nu} j^\nu$ under a Lorentz transformation $\Lambda$.
2. $j^\mu$ is conserved: $\partial_\mu j^\mu = 0$, using the Dirac equation.
3. The component $j^0 = \psi^\dagger\psi$ is non-negative, so $j^0$ is a positive-definite probability density.

**Recall:**

The Dirac equation:

![[Def - The Dirac Equation#The Definition]]

The Dirac conjugate is $\bar\psi = \psi^\dagger\gamma^0$. Under a Lorentz transformation $\Lambda$ with lift $A \in \mathrm{SL}(2, \mathbb{C})$ via the cover $\mathrm{SL}(2, \mathbb{C}) \to L_0$, $\psi$ transforms as $\psi \to \rho(A)\psi$ where $\rho(A) = \mathrm{diag}(A, (A^\dagger)^{-1})$ (in the Weyl basis); the gamma matrices satisfy the intertwining $\rho(A)^{-1}\gamma^\mu\rho(A) = \Lambda^\mu_{\;\nu}\gamma^\nu$.

Hermiticity properties of the gamma matrices: $(\gamma^0)^\dagger = -\gamma^0$ (anti-Hermitian in Frankel signature, since $(\gamma^0)^2 = -I$), and $(\gamma^k)^\dagger = \gamma^k$ for $k = 1, 2, 3$ (Hermitian, since $(\gamma^k)^2 = +I$). Equivalently, $(\gamma^\mu)^\dagger = \gamma^0\gamma^\mu(\gamma^0)^{-1} = -\gamma^0\gamma^\mu\gamma^0$.

---

# Convergent Strategy

**Problem class:** *Verification that a tensor object built from Dirac spinors transforms correctly and is conserved.* This is the standard "verify Noether current" exercise applied to the global $U(1)$ symmetry $\psi \to e^{i\alpha}\psi$ of the Dirac Lagrangian; the resulting Noether current is $j^\mu = \bar\psi\gamma^\mu\psi$.

**Assumption pattern:** We are given a solution $\psi$ of the Dirac equation; we want to use this *plus* the Hermiticity properties of the gamma matrices to verify covariance and conservation. The hermiticity rules $(\gamma^\mu)^\dagger = \gamma^0\gamma^\mu\gamma^0/(-1)$ are essential for the calculations.

**Theorem routing:** For Lorentz covariance, use the intertwining $\rho(A)^{-1}\gamma^\mu\rho(A) = \Lambda^\mu_{\;\nu}\gamma^\nu$ from [[Def - Dirac Gamma Matrices]]; the conjugate transforms as $\bar\psi \to \bar\psi\rho(A)^{-1}$, which combines with $\rho(A)$ on $\psi$ and the gamma intertwining to give the desired covariance. For conservation, use $\partial_\mu(\bar\psi\gamma^\mu\psi) = (\partial_\mu\bar\psi)\gamma^\mu\psi + \bar\psi\gamma^\mu\partial_\mu\psi$, with both terms reducing via the Dirac equation and its conjugate.

**Key decision point:** The non-obvious step is verifying that $\bar\psi$ transforms as $\bar\psi \to \bar\psi\rho(A)^{-1}$ (not $\bar\psi\rho(A)^\dagger$), which requires using $\rho(A)^\dagger\gamma^0 = \gamma^0\rho(A)^{-1}$ — an identity that follows from the spin representation's structure. Without this, the "$\bar\psi$ as transformed dual" of $\psi$ would be wrong.

---

# Legal Operations Used

1. **Operation 10 from the topic page (compute the spinor Lagrangian via $\bar\psi = \psi^\dagger\gamma^0$):** The Dirac conjugate $\bar\psi = \psi^\dagger\gamma^0$ is the "natural" conjugate of a Dirac spinor that makes Lorentz-invariant bilinears work. Its transformation rule under Lorentz, $\bar\psi \to \bar\psi\rho(A)^{-1}$, is what makes $\bar\psi\gamma^\mu\psi$ transform as a vector. In this exercise, $\bar\psi$ does the *combinatorial* work of pairing $\psi^\dagger$ with $\gamma^0$ to produce a Lorentz-covariant quantity.

2. **Operation 6 from the topic page (insert a Lorentz transformation via $\rho(A)$):** To verify Lorentz covariance, replace $\psi \to \rho(A)\psi$ and $\bar\psi \to \bar\psi\rho(A)^{-1}$, then check the transformation of $j^\mu = \bar\psi\gamma^\mu\psi$ using the gamma intertwining $\rho(A)^{-1}\gamma^\mu\rho(A) = \Lambda^\mu_{\;\nu}\gamma^\nu$. This is the standard verification of representation-covariance.

---

# Hints

> [!note]- Hint 1
> For the Lorentz covariance, you need to know how $\bar\psi$ transforms. Starting from $\psi \to \rho(A)\psi$, compute $\bar\psi = \psi^\dagger\gamma^0 \to (\rho(A)\psi)^\dagger\gamma^0 = \psi^\dagger\rho(A)^\dagger\gamma^0$. Use the identity $\rho(A)^\dagger\gamma^0 = \gamma^0\rho(A)^{-1}$ (which follows from the spin representation's structure — verify it for $A = \exp(\theta\sigma_k/2)$ and $A = \exp(i\xi\sigma_k/2)$) to convert this to $\bar\psi\rho(A)^{-1}$.

> [!note]- Hint 2
> For conservation: differentiate $j^\mu = \bar\psi\gamma^\mu\psi$ using the product rule. The term $\bar\psi\gamma^\mu\partial_\mu\psi = m\bar\psi\psi$ from the Dirac equation. The term $(\partial_\mu\bar\psi)\gamma^\mu\psi$ requires the conjugate Dirac equation $\partial_\mu\bar\psi\gamma^\mu = -m\bar\psi$, derived from $\not\partial\psi = m\psi$ by taking the Dirac conjugate.

> [!note]- Hint 3
> For $j^0 = \psi^\dagger\psi \geq 0$: compute $j^0 = \bar\psi\gamma^0\psi = \psi^\dagger\gamma^0\gamma^0\psi$. Using $(\gamma^0)^2 = -I$ in Frankel signature, $j^0 = -\psi^\dagger\psi$ — wait, this has the wrong sign! The fix: the Frankel signature has $(\gamma^0)^2 = -I$, but the *physically meaningful* probability density convention introduces a relative sign. Conventionally, $j^\mu = \bar\psi\gamma^\mu\psi$ with $j^0$ as the *upper-component* density: in the $(+ - - -)$ convention this works out cleanly, in the Frankel convention there is a sign correction. See the solution for the resolution.

---

# Solution

The proof has three steps. Step 1 derives the conjugate Dirac equation, which is the analytical input for conservation. Step 2 verifies conservation via $\partial_\mu j^\mu = 0$ using both Dirac equations. Step 3 verifies Lorentz covariance using the gamma intertwining and the transformation of $\bar\psi$, and clarifies the positivity of $j^0$ in the appropriate convention.

**Step 1: The conjugate Dirac equation.**

The conjugate Dirac equation is $\partial_\mu\bar\psi\gamma^\mu = -m\bar\psi$ — i.e., $\bar\psi$ satisfies a "left-acting" Dirac equation with the *opposite* sign of mass.

> [!note]- Derivation
> Start with the Dirac equation $\gamma^\mu\partial_\mu\psi = m\psi$. Take the Hermitian conjugate (componentwise): $(\partial_\mu\psi)^\dagger (\gamma^\mu)^\dagger = m\psi^\dagger$, i.e., $\partial_\mu\psi^\dagger \cdot (\gamma^\mu)^\dagger = m\psi^\dagger$. Now multiply both sides on the right by $\gamma^0$ (a constant matrix, so it commutes with $\partial_\mu$): $\partial_\mu\psi^\dagger \cdot (\gamma^\mu)^\dagger \gamma^0 = m\psi^\dagger\gamma^0 = m\bar\psi$.
>
> Use the hermiticity relation $(\gamma^\mu)^\dagger\gamma^0 = -\gamma^0\gamma^\mu$ (this is the consequence of $(\gamma^0)^\dagger = -\gamma^0$ and $(\gamma^k)^\dagger = +\gamma^k$ in the Frankel sign convention, combined with $\{\gamma^0, \gamma^k\} = 0$). Substituting: $-\partial_\mu\psi^\dagger\gamma^0\gamma^\mu = m\bar\psi$, i.e., $-\partial_\mu\bar\psi \cdot \gamma^\mu = m\bar\psi$, which rearranges to
> $$\partial_\mu\bar\psi \cdot \gamma^\mu = -m\bar\psi.$$
> This is the conjugate Dirac equation.

**Step 2: Conservation $\partial_\mu j^\mu = 0$.**

Differentiate and use both Dirac equations to get cancellation.

> [!note]- Derivation
> $$\partial_\mu j^\mu = \partial_\mu(\bar\psi\gamma^\mu\psi) = (\partial_\mu\bar\psi)\gamma^\mu\psi + \bar\psi\gamma^\mu(\partial_\mu\psi).$$
> First term: using the conjugate Dirac equation $\partial_\mu\bar\psi\gamma^\mu = -m\bar\psi$, $(\partial_\mu\bar\psi)\gamma^\mu\psi = -m\bar\psi\psi$.
>
> Second term: using the Dirac equation $\gamma^\mu\partial_\mu\psi = m\psi$, $\bar\psi\gamma^\mu\partial_\mu\psi = m\bar\psi\psi$.
>
> Sum: $-m\bar\psi\psi + m\bar\psi\psi = 0$. ∎

**Step 3: Lorentz covariance and positivity of $j^0$.**

Under a Lorentz transformation $\Lambda \in L_0$ with lift $A \in \mathrm{SL}(2, \mathbb{C})$, $j^\mu \to \Lambda^\mu_{\;\nu}j^\nu$. The component $j^0 = -\psi^\dagger\psi$ in Frankel signature (with $(\gamma^0)^2 = -I$), or equivalently $|j^0| = \psi^\dagger\psi \geq 0$ — the *magnitude* is the probability density. (Most physics texts use the opposite sign convention $\eta = (+ - - -)$, where the relations work out so that $j^0 = +\psi^\dagger\psi$ directly.)

> [!note]- Derivation
> *Lorentz covariance:* Under $\psi \to \rho(A)\psi$, $\bar\psi \to \psi^\dagger\rho(A)^\dagger\gamma^0$. Using the identity $\rho(A)^\dagger\gamma^0 = \gamma^0\rho(A)^{-1}$ (verify on generators of $\mathrm{SL}(2, \mathbb{C})$):
> $$\bar\psi \to \psi^\dagger\gamma^0\rho(A)^{-1} = \bar\psi\rho(A)^{-1}.$$
> Now compute the transformed current:
> $$j'^\mu = \bar\psi' \gamma^\mu \psi' = \bar\psi\rho(A)^{-1}\gamma^\mu\rho(A)\psi.$$
> Using the intertwining $\rho(A)^{-1}\gamma^\mu\rho(A) = \Lambda^\mu_{\;\nu}\gamma^\nu$:
> $$j'^\mu = \bar\psi(\Lambda^\mu_{\;\nu}\gamma^\nu)\psi = \Lambda^\mu_{\;\nu}\bar\psi\gamma^\nu\psi = \Lambda^\mu_{\;\nu}j^\nu.$$
> So $j^\mu$ transforms as a $4$-vector under Lorentz transformations.
>
> *Positivity of $j^0$:* $j^0 = \bar\psi\gamma^0\psi = \psi^\dagger\gamma^0\gamma^0\psi = -\psi^\dagger\psi$ in Frankel signature. So $j^0 \leq 0$, with $|j^0| = \psi^\dagger\psi \geq 0$. The physical probability density is $|j^0|$, which is positive-definite.
>
> In the alternative physics convention $\eta = (+ - - -)$, $(\gamma^0)^2 = +I$, so $j^0 = +\psi^\dagger\psi \geq 0$ directly — no sign issue. This is the more common convention in QFT textbooks, where the formula reads cleanly. The sign discrepancy is the same translation we encountered for the Dirac equation itself.

> [!note]- Complete formal solution
> Let $\psi$ satisfy $\gamma^\mu\partial_\mu\psi = m\psi$. Let $\bar\psi = \psi^\dagger\gamma^0$ and $j^\mu = \bar\psi\gamma^\mu\psi$.
>
> *Conjugate Dirac equation.* Take the Hermitian conjugate of the Dirac equation: $\partial_\mu\psi^\dagger \cdot (\gamma^\mu)^\dagger = m\psi^\dagger$. Multiply on the right by $\gamma^0$; use $(\gamma^\mu)^\dagger\gamma^0 = -\gamma^0\gamma^\mu$ (combining $(\gamma^0)^\dagger = -\gamma^0$, $(\gamma^k)^\dagger = +\gamma^k$, $\{\gamma^0, \gamma^k\} = 0$): $-\partial_\mu\psi^\dagger\gamma^0\gamma^\mu = m\psi^\dagger\gamma^0$, i.e., $\partial_\mu\bar\psi \cdot \gamma^\mu = -m\bar\psi$.
>
> *Conservation.* $\partial_\mu j^\mu = (\partial_\mu\bar\psi)\gamma^\mu\psi + \bar\psi\gamma^\mu(\partial_\mu\psi) = -m\bar\psi\psi + m\bar\psi\psi = 0$.
>
> *Lorentz covariance.* Under $\psi \to \rho(A)\psi$: $\bar\psi \to \bar\psi\rho(A)^{-1}$ (using $\rho(A)^\dagger\gamma^0 = \gamma^0\rho(A)^{-1}$), so $j'^\mu = \bar\psi\rho(A)^{-1}\gamma^\mu\rho(A)\psi = \Lambda^\mu_{\;\nu}\bar\psi\gamma^\nu\psi = \Lambda^\mu_{\;\nu}j^\nu$ (using the intertwining $\rho(A)^{-1}\gamma^\mu\rho(A) = \Lambda^\mu_{\;\nu}\gamma^\nu$). So $j^\mu$ is a Lorentz $4$-vector.
>
> *Positivity of $j^0$.* $j^0 = \bar\psi\gamma^0\psi = \psi^\dagger\gamma^0\gamma^0\psi = -\psi^\dagger\psi$ in Frankel signature; the probability density is $|j^0| = \psi^\dagger\psi \geq 0$.

---

# Key Takeaways

**The Dirac conjugate $\bar\psi = \psi^\dagger\gamma^0$ is the natural Lorentz-covariant dual.** The reason for the $\gamma^0$ insertion is that the spin representation $\rho(A) = \mathrm{diag}(A, (A^\dagger)^{-1})$ on Dirac spinors is *not unitary* in general — the boost generators $A = \exp(\xi\sigma_k/2)$ are Hermitian, not anti-Hermitian, so $\rho(A)^\dagger \neq \rho(A)^{-1}$. The $\gamma^0$ insertion fixes this: the identity $\gamma^0\rho(A)^\dagger\gamma^0 = \rho(A)^{-1}$ (verifiable on $\mathrm{SL}(2, \mathbb{C})$ generators) makes $\bar\psi$ transform "correctly". Whenever you build a Lorentz-invariant bilinear from a spinor, you need $\bar\psi$, not $\psi^\dagger$.

**The conserved current $j^\mu = \bar\psi\gamma^\mu\psi$ is the Noether current of the global $U(1)$ symmetry of the Dirac Lagrangian.** The Dirac Lagrangian $\mathcal{L}_D = \bar\psi(\gamma^\mu\partial_\mu - m)\psi$ is invariant under $\psi \to e^{i\alpha}\psi, \bar\psi \to e^{-i\alpha}\bar\psi$. Noether's theorem then gives a conserved current; computing it produces exactly $j^\mu = \bar\psi\gamma^\mu\psi$. This is the conserved charge that becomes **electric charge** when the symmetry is gauged (by introducing an electromagnetic potential $A_\mu$ in the covariant derivative $D_\mu = \partial_\mu - ieA_\mu$). Every massive fermion in the Standard Model has a conserved current of this form for each gauge symmetry it transforms under.

**The positivity of $j^0$ is what makes the Dirac equation a "proper" probabilistic wave equation.** The Klein–Gordon equation has the conserved current $j^\mu = i(\phi^*\partial^\mu\phi - \phi\partial^\mu\phi^*)$, and its $j^0$ is *not* positive-definite — it can be negative depending on the wave function — making the probabilistic interpretation problematic. The Dirac equation's $j^0 = |\psi|^2$ (in appropriate sign convention) is always non-negative, giving a proper probability density. This is one of the original motivations for the first-order Dirac equation over the second-order Klein-Gordon equation, and is the analytical face of the spin-statistics theorem (fermion wave functions are positive-definite, boson wave functions need careful interpretation).
