---
type: exercise-index
subject: special-relativity
section: "4.2"
tags: [physics, special-relativity]
---

## §4.2 Rapidity and Boosts as Hyperbolic Rotations — Exercises

The exercises of §4.2 build the [[Def - Rapidity|rapidity]] picture and exploit it. The organising fact is that a boost is a [[Def - Boosts as Hyperbolic Rotations|hyperbolic rotation]] — the Euclidean rotation matrix with $\cos, \sin$ replaced by $\cosh, \sinh$ — and rapidity is its additive parameter, the hyperbolic angle. The first exercise composes collinear boosts both the hard way (matrix multiplication in velocity variables) and the easy way (adding rapidities), showing the velocity-addition law is the $\tanh$ addition formula and that the speed of light is an unreachable ceiling because $\tanh$ is bounded. The second diagonalises the boost, finds its null eigenvectors, and works in light-cone coordinates where the boost is $\mathrm{diag}(e^\varphi, e^{-\varphi})$ and everything trivialises. The third drills the rapidity dictionary and the hyperbolic-angle geometry, connecting rapidity to the Doppler factor by $\varphi = \ln k$. The unifying technique: convert velocities to rapidities, work additively (or multiplicatively with Doppler factors), convert back.

- [[Ex - Composing collinear boosts with rapidity]] (⭐⭐) — multiply two boosts in velocity form to recover $w = (v_1 + v_2)/(1 + v_1 v_2)$, redo it in one line by adding rapidities, compute a rocket-and-probe example, and show $N$ identical boosts give $v_N = \tanh(N\Delta\varphi) \to 1^-$ but never reach $c$ ([[Def - Rapidity]], [[Thm - Boosts Compose by Adding Rapidities]], [[Thm - Relativistic Velocity Addition]]).

- [[Ex - A boost is a hyperbolic rotation and its eigenvectors are null]] (⭐⭐) — find the real eigenvalues $e^{\pm\varphi}$ and null eigenvectors $(1, \pm 1)$, contrast with the rotation's complex eigenvalues, diagonalise in light-cone coordinates where $\Delta s^2 = uw$ and the boost is $\mathrm{diag}(e^\varphi, e^{-\varphi})$, re-prove rapidity additivity, and identify the eigenvalue as the Doppler factor ([[Def - Boosts as Hyperbolic Rotations]], [[Def - Rapidity]], [[Def - Classification of Four-Vectors]], [[Thm - Boosts Compose by Adding Rapidities]]).

- [[Ex - Rapidity, the Doppler factor and the velocity ceiling]] (⭐) — derive the three rapidity relations from $\gamma = \cosh\varphi$, invert to $\varphi = \tanh^{-1}v = \tfrac12\ln\frac{1+v}{1-v}$ mapping $(-1,1)$ onto $\mathbb{R}$, show the Doppler factor is $k = e^\varphi = \sqrt{\frac{1+v}{1-v}}$ with $\varphi = \ln k$, and interpret rapidity as the hyperbolic angle whose asymptote is the speed of light ([[Def - Rapidity]], [[Def - Boosts as Hyperbolic Rotations]]).
