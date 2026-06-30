---
type: exercise-index
subject: special-relativity
section: "12.3"
tags: [physics, special-relativity]
---

## §12.3 Casimirs, Mass and Spin — Exercises

The exercises of §12.3 drill the two Casimir invariants of the Poincaré group and the Wigner classification they support. The two Casimirs are $P^2 = m^2$ (the mass) and $W^2 = -m^2 s(s+1)$ (the spin), the latter built from the Pauli–Lubanski vector $W^\mu = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma$. The first exercise evaluates this vector — proving the identity $W\cdot P = 0$ from antisymmetry, reducing it in the rest frame to $m$ times the spin three-vector, and squaring to $-m^2 s(s+1)$; the recurring move is to evaluate an invariant in the convenient frame and let the momentum project the angular momentum onto its rotation part. The second exercise verifies, by the covariant commutation relations and the Leibniz rule, that both $P^2$ and $W^2$ commute with all ten generators — with the key lesson that $W^\mu$, not $J^{\mu\nu}J_{\mu\nu}$, is the spin Casimir because the contraction with $P$ buys the translation-invariance that angular momentum alone lacks. The third exercise carries out the little-group classification: the massive little group is the compact $\mathrm{SO}(3)$ giving $2s+1$ polarisations, the massless little group the non-compact $\mathrm{ISO}(2)$ giving exactly two helicity states $\pm s$, with the photon's two polarisations versus the $W$ boson's three as the observable payoff. The unifying theme: mass and spin are not properties a particle has but the two Casimir labels that *name* the irreducible representation — which is what an elementary particle is.

- [[Ex - Computing the Pauli-Lubanski vector]] (⭐⭐) — prove $W\cdot P = 0$ from the antisymmetry of $\varepsilon$ against $P_\mu P_\sigma$, evaluate $W^\mu$ in the rest frame as $(0, m\boldsymbol{J})$, square to the spin Casimir $W^2 = -m^2 s(s+1)$, and confirm it is a Lorentz scalar holding in all frames ([[Def - Casimir Invariants of the Poincaré Group]], [[Def - Angular Momentum Four-Tensor]], [[Def - Four-Momentum and Rest Mass]], [[Def - Spin Four-Vector]]).

- [[Ex - The two Casimir invariants commute with the Poincaré generators]] (⭐⭐⭐) — verify $[P^2, P^\rho] = [P^2, J^{\rho\sigma}] = 0$, show $[W^\mu, P^\nu] = 0$ and that $W^\mu$ transforms as a four-vector, conclude $W^2$ is a Casimir, and learn why $W^\mu$ rather than $J^{\mu\nu}J_{\mu\nu}$ is the spin invariant ([[Def - Casimir Invariants of the Poincaré Group]], [[Thm - The Poincaré Group as a Lie Group]], [[Def - Angular Momentum Four-Tensor]], [[Def - Spin Four-Vector]]).

- [[Ex - Classifying massive versus massless representations]] (⭐⭐) — identify the massive little group as the compact $\mathrm{SO}(3)$ (spin-$s$ multiplets, $2s+1$ states) and the massless little group as the non-compact $\mathrm{ISO}(2)$, show $W = hP$ collapses the massless label to helicity $\pm s$, and contrast the photon's two polarisations with the massive vector boson's three ([[Def - Casimir Invariants of the Poincaré Group]], [[Def - The Lorentz Group]], [[Def - Four-Momentum and Rest Mass]]).
