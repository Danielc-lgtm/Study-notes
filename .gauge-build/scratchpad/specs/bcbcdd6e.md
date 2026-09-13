# PAGE SPEC

- **Filename:** `Def - Yang-Mills Lagrangian and Action Functional.md`
- **Type:** definition
- **Chapter:** Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory  (folder `Gauge Theory VII/`)
- **Section:** §7.4 Yang–Mills Fields and Instantons

## Spec (from the manifest)

type: definition (anchor); source items: B-D3.3.5, B-D3.3.6; prereqs: [Def - The Yang-Mills Field Strength, Def - Wedge Product and Metric Pairing of Bundle-Valued Forms, Def - Hodge Star in Arbitrary Signature, Thm - The Space of Connections is an Affine Space]; spec: $L_{YM}:\mathcal C(P)\to\Omega^4(M;\mathbb R)$, $L_{YM}(\omega) := \tfrac12\lambda(\bar\Omega\wedge\star\bar\Omega)$; the Yang–Mills action $\mathcal{YM}(\omega) := \int_ML_{YM}(\omega)$ (over $\bar U$ for the variational definition on non-compact $M$); $\omega$ is a *Yang–Mills connection* if it is critical: $\frac{d}{dt}\big|_0\int_{\bar U}L_{YM}(\omega+t\eta) = 0$ for all $\eta\in\Omega^1_{\operatorname{Ad}}(P;\mathfrak g)$ horizontal with $\bar\eta$ compactly supported in $U$ (the affine-space anchor identifies such $\eta$ with $\Omega^1_c(M;\operatorname{ad}P)$); Convention callout: conventions.md's $\mathcal{YM}(A) = \tfrac12\int|F_A|^2\mathrm{vol}$ with $|F|^2$ from $-\operatorname{tr}$ coincides with Bär's by the next Thm page; Haydys's Chern–Simons/flat-connection pages (VI, V) use the same $\lambda$; Axiom Motivation: the non-abelian copy of `Def - Electromagnetic Lagrangian and Action` with $\lambda$ replacing the scalar product, why $\operatorname{Ad}$-invariance is forced by gauge invariance; examples: $G = U(1)$ recovers $\tfrac12F\wedge\star F$; flat connections have $\mathcal{YM} = 0$.
