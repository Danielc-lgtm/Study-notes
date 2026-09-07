---
type: exercise
subject: gauge-theory
prereqs: ["Thm - Classification of Simply Connected Topological Four-Manifolds", "Thm - Donaldson Diagonalization Theorem"]
tags: [four-manifolds, exercise]
---
# Exercise
Explain why there is a closed simply connected topological four-manifold with intersection form $E_8$, why it cannot be smooth, and why the two obstructions supplied by Rochlin and Donaldson are logically independent checks here.

> [!solution]- Solution
> $E_8$ is an even unimodular symmetric integral form, so Freedman's realization theorem supplies a closed simply connected topological four-manifold with this form. Its signature is $8$. If smooth, evenness would make it spin, and Rochlin would require its signature to be divisible by $16$, contradiction. Independently, $E_8$ is positive definite but not integrally diagonal, contradicting Donaldson diagonalization. Rochlin uses spin parity and the Dirac index; Donaldson uses instanton moduli spaces. Either excludes smoothability, but by different mechanisms.
