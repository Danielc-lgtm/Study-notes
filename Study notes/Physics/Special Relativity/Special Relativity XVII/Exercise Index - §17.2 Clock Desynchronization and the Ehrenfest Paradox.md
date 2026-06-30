---
type: exercise-index
subject: special-relativity
section: "17.2"
tags: [physics, special-relativity]
---

## §17.2 Clock Desynchronization and the Ehrenfest Paradox — Exercises

The exercises of §17.2 drill the two faces of the rotating congruence's vorticity: the impossibility of globally synchronizing clocks (a failure to integrate a *time* one-form around a loop) and the Ehrenfest non-Euclidean geometry (a failure to integrate a *length* one-form). The unifying technique is the loop integral: a quantity that vanishes locally but is wanted globally is tested by its circulation around a closed curve, and the nonzero result — equal by Stokes' theorem to a flux of the vorticity $2\vec\omega$ through the enclosed area — is the measurable obstruction. The line-element exercise extracts the rotating-frame spatial metric directly, exhibiting the tangential enhancement $\Gamma r\,d\varphi$ and the unchanged radial $dr$; the synchronization exercise integrates the local gap to the nonzero desynchronization $\pm 2\pi\Gamma r^2\omega/c^2$; and the Ehrenfest exercise resolves the paradox by rejecting Born rigidity for spin-up. Throughout, the surviving $c^2$ marks these as genuinely relativistic effects, not Newtonian limits, and the non-Euclidean disk geometry stands as the historical seed of curved spacetime.

- [[Ex - The line element on the rotating disk]] (⭐⭐) — transform the flat metric to rotating coordinates, read off the corotating proper time $\Gamma^{-1}dt$ and the cross term $g_{0\varphi} = -r^2\omega$, project out the spatial metric $d\ell'^2 = dr^2 + \Gamma^2 r^2 d\varphi^2$, and integrate to recover the non-Euclidean circumference $L' = \Gamma\,2\pi R$ with unchanged radius $R' = R$ ([[Def - The Ehrenfest Paradox]], [[Def - Uniformly Rotating Observer]], [[Def - Minkowski Space and the Metric]], [[Def - Einstein-Poincaré Simultaneity]]).

- [[Ex - The impossibility of global synchronization and the time gap around a loop]] (⭐⭐⭐) — derive the local synchronization condition $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$ from the orthogonality of the corotating four-velocity to the separation, integrate around the rim to the nonzero desynchronization $\pm 2\pi\Gamma r^2\omega/c^2$, recast it via Stokes and $\mathrm{curl}\,\vec V = 2\vec\omega$ as the vorticity flux $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$, and explain why the surviving $c^2$ marks it as relativistic rather than Newtonian ([[Thm - Impossibility of Global Clock Synchronization on a Rotating Disk]], [[Def - Uniformly Rotating Observer]], [[Def - Einstein-Poincaré Simultaneity]]).

- [[Ex - The Ehrenfest paradox and its resolution]] (⭐⭐) — compute the corotating circumference $\Gamma\,2\pi R_0$ (tangentially enhanced) and radius $R_0$ (unchanged), state the contradiction with Born-rigid spin-up, resolve it by the Herglotz–Noether theorem (no rigid motion connects rest to rotation), and describe the tangential stretching and hoop stress ([[Def - The Ehrenfest Paradox]], [[Def - Born Rigidity Criterion]], [[Thm - Length Contraction (General)]]).
