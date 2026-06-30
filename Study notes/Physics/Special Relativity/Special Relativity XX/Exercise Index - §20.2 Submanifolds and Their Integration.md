---
type: exercise-index
subject: special-relativity
section: "20.2"
tags: [physics, special-relativity]
---

## §20.2 Submanifolds and Their Integration — Exercises

The exercises of §20.2 drill the volume, area, and length elements of submanifolds and the flux of a vector field through a hypersurface. The unifying technique is the Hodge-star recipe: the volume element of a $p$-submanifold is the Hodge dual of the wedge of its unit normals — $\star\underline{n}$ for a hypersurface, $\star(\underline{n}\wedge\underline{s})$ for a 2-surface, $\pm\underline{u}$ for a curve — and a flux is the integral of the Hodge dual $\star\underline{v}$ of the field's 1-form. The recurring move is to find the unit normal(s), dualise and Hodge-star to build the measure, then integrate. A second thread is that recasting a flux as $\int\star\underline{v}$ (rather than $\pm\int\vec{v}\cdot\vec{n}\,\mathrm{d}V$) costs nothing and makes the flux Stokes-ready, which is the bridge to the conservation laws of §20.3. The flux through a constant-time slice reduces to the integral of the time component — the "density" crossing the instant — which for the four-current is the total charge.

- [[Ex - The flux of a vector field through a hypersurface]] (⭐⭐) — compute the flux $\int_\Sigma\star\underline{v}$ through a constant-time slice both elementarily and via the Hodge dual, show it reduces to $\int_\Sigma v^0\,\mathrm{d}^3x$, verify a tangent field has zero flux, and identify the flux of the four-current with the total charge ([[Def - Volume, Area, Length Elements and Flux Integrals]], [[Def - The Hodge Star]], [[Def - Metric Duality and Index Manipulation]]).
- [[Ex - The volume element of a hypersurface is the Hodge dual of its normal]] (⭐⭐) — prove $\epsilon_{\mathscr{V}}=\star\underline{n}$ by comparing $(\epsilon_{\mathscr{V}})_{\alpha\beta\gamma}=n^\mu\epsilon_{\mu\alpha\beta\gamma}$ with the Hodge-star component formula, derive $\mathrm{d}V=n^0\sqrt{|g|}\,\mathrm{d}^3x$, recover the ball volume, and verify "volume of a slice = flux of its normal" ([[Def - Volume, Area, Length Elements and Flux Integrals]], [[Def - The Hodge Star]], [[Def - The Levi-Civita Tensor]]).
- [[Ex - Length, area, and volume elements in spherical coordinates]] (⭐) — from the single metric factor $\sqrt{|g|}=r^2\sin\theta$, read off the length element of a radial curve, the area element of a sphere, and the volume element of a ball, recovering radial length $R$, sphere area $4\pi R^2$, and ball volume $\frac{4}{3}\pi R^3$ ([[Def - Volume, Area, Length Elements and Flux Integrals]], [[Def - Integration of Forms and the Volume Element]]).
