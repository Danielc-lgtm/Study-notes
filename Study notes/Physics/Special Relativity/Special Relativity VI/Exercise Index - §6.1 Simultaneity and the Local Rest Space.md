---
type: exercise-index
subject: special-relativity
section: "6.1"
tags: [physics, special-relativity]
---

## §6.1 Simultaneity and the Local Rest Space — Exercises

The exercises of §6.1 drill the foundational move of the chapter: an observer's notion of "now" is metric orthogonality to the four-velocity, and the rest space is the orthogonal complement $U_0^\perp$. The radar synchronisation exercise extracts the simultaneity criterion $U_0\cdot\overrightarrow{AB} = 0$ (and the scalar square that feeds Synge's distance) from the null conditions on a photon round trip; the projector exercise verifies, by direct computation, that $\Pi(X) = X - (X\cdot U_0)U_0$ is the orthogonal projector (idempotent and self-adjoint) and exposes the signature-sign trap; and the two-observers exercise turns the abstract nonexistence of absolute time into named events that two observers in relative motion date differently, with the tilt of the simultaneity lines measured by the rapidity. The unifying technique: replace every statement about "at the same time" by an orthogonality equation, then compute.

- [[Ex - Einstein synchronisation and the radar date]] (⭐⭐) — set up the two null conditions on the radar photon legs, solve the $2\times 2$ linear system for $U_0\cdot\overrightarrow{AB}$ and $\overrightarrow{AB}\cdot\overrightarrow{AB}$, and recover the simultaneity criterion $U_0\cdot\overrightarrow{AB} = 0\Leftrightarrow t = \tfrac12(t_1+t_2)$ together with the spacelike scalar square ([[Def - Einstein-Poincaré Simultaneity]], [[Def - Observer and Local Rest Space]], [[Def - Four-Velocity and Four-Acceleration]], [[Def - The Null Cone and the Time Arrow]], [[Def - Synge World Function and Spatial Distance]]).

- [[Ex - The orthogonal projector is idempotent and symmetric]] (⭐) — verify directly from $\Pi(X) = X - (X\cdot U_0)U_0$ that $\Pi(U_0) = 0$, that $\Pi$ fixes the rest space, that $\Pi^2 = \Pi$, and that $\Pi$ is self-adjoint, then show the sign-flipped map (Gourgoulhon's mostly-plus sign mis-imported) is not even a projector ([[Def - The Orthogonal Projector onto the Local Rest Space]], [[Def - Observer and Local Rest Space]], [[Def - Four-Velocity and Four-Acceleration]]).

- [[Ex - Two observers disagree on simultaneity]] (⭐⭐) — compute the two rest spaces $U_0^\perp = \{X^0 = 0\}$ and $U_0'^\perp = \{X^0 = vX^1\}$ for a boosted observer, exhibit two events simultaneous for one but not the other with date gap $\gamma vL$, and relate the tilt of the simultaneity line to the rapidity $\tan\theta = v = \tanh\varphi$ ([[Thm - Nonexistence of Absolute Time]], [[Def - Observer and Local Rest Space]], [[Def - Einstein-Poincaré Simultaneity]], [[Def - Rapidity]]).
