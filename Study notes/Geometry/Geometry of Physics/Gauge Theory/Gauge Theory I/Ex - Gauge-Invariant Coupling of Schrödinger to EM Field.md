---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - U(1) Gauge Field and Electromagnetic Connection"
  - "Def - Gauge Transformation"
tags: [gauge-theory, electromagnetism, quantum-mechanics, minimal-coupling]
---

# Prerequisite Concepts

- [[Def - U(1) Gauge Field and Electromagnetic Connection]]
- [[Def - Gauge Transformation]]

# Problem Statement

Let $\psi(t,x)$ be a particle of mass $m$ and charge $q$ on $\mathbb R^3$. Define
$$D_t=\partial_t+iq\phi,\qquad D_j=\partial_j+iqA_j$$
(in units $\hbar=1$). Show that
$$
iD_t\psi=-\frac{1}{2m}\sum_{j=1}^3D_jD_j\psi
$$
is invariant under
$$
\psi'=e^{-iq\chi}\psi,\qquad A'=A+d_x\chi,\qquad
\phi'=\phi+\partial_t\chi.
$$
Explain why replacing only the spatial derivatives would fail for time-dependent $\chi$.

# Convergent Strategy

Prove the single intertwining identity $D'_\mu(e^{-iq\chi}\psi)=e^{-iq\chi}D_\mu\psi$. Applying it twice handles the kinetic term; there is no need to expand the whole Hamiltonian.

# Solution

> [!proof]- Solution
> For any spacetime index $\mu$ write $A_0=\phi$. Then
> $$
> \begin{aligned}
> D'_\mu\psi'
> &=(\partial_\mu+iq(A_\mu+\partial_\mu\chi))(e^{-iq\chi}\psi)\\
> &=e^{-iq\chi}\bigl(\partial_\mu\psi-iq(\partial_\mu\chi)\psi
> +iqA_\mu\psi+iq(\partial_\mu\chi)\psi\bigr)\\
> &=e^{-iq\chi}D_\mu\psi.
> \end{aligned}
> $$
> Applying the spatial identity once more gives
> $D'_jD'_j\psi'=e^{-iq\chi}D_jD_j\psi$, while the temporal identity gives
> $D'_t\psi'=e^{-iq\chi}D_t\psi$. Multiplying the original equation by $e^{-iq\chi}$ therefore yields the transformed equation.
>
> If one replaced $\partial_j$ by $D_j$ but left $\partial_t$ ordinary, then
> $$
> \partial_t\psi'=e^{-iq\chi}\bigl(\partial_t\psi-iq(\partial_t\chi)\psi\bigr),
> $$
> and the extra term would have no counterpart on the right-hand side. The scalar potential is the temporal component of the same connection, so it must transform with $\partial_t\chi$.

# Key Takeaways

Minimal coupling is not an optional correction guessed from the Lorentz force. It is the unique first-order replacement of $d$ by a connection that makes local phase changes intertwine with differentiation. Restoring units replaces $qA_\mu$ by $qA_\mu/\hbar$ (and convention-dependent factors of $c$ in spatial Gaussian-unit formulas).
