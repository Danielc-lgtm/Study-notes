---
type: definition
subject: gauge-theory
prereqs: ["Def - Self-Dual and Anti-Self-Dual Connection", "Def - Moduli Space of Flat Connections"]
tags: [gauge-theory, donaldson, moduli-space]
---

# Prerequisite Concepts

- [[Def - Self-Dual and Anti-Self-Dual Connection]]
- [[Def - Moduli Space of Flat Connections]]

# The Definition
For a principal $SU(2)$-bundle $P\to X$, the anti-self-dual moduli space is
$$\mathcal M_k(X)=\{A:F_A^+=0,\ c_2(P)=k\}/\mathcal G(P).$$
At an irreducible solution its deformation complex is
$$0\to\Omega^0(\operatorname{ad}P)\xrightarrow{d_A}\Omega^1(\operatorname{ad}P)\xrightarrow{d_A^+}\Omega^2_+(\operatorname{ad}P)\to0.$$
Gauge fixing replaces it by the elliptic operator $d_A^*\oplus d_A^+$.

# Compactness mechanism
Curvature can concentrate at finitely many points while preserving total energy in quantized packets. Uhlenbeck compactification records a limiting ASD connection of charge $k-\ell$ together with an unordered $\ell$-tuple of bubbling points:
$$\overline{\mathcal M}_k\subseteq\coprod_{\ell=0}^k\mathcal M_{k-\ell}\times\operatorname{Sym}^{\ell}(X).$$
This is not ordinary compactness of connections; it is compactness after gauge and after admitting ideal instantons.

# Contrast with Seiberg–Witten theory
The abelian Seiberg–Witten curvature equation and spinor estimate prevent bubbling, giving an actually compact moduli space. Donaldson theory is nonabelian and must incorporate bubbling and gluing explicitly.
