# PAGE SPEC

- **Filename:** `Def - The Adjoint Bundle with its Trace Metric and Induced Connection.md`
- **Type:** definition
- **Chapter:** Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory  (folder `Gauge Theory VII/`)
- **Section:** §7.4 Yang–Mills Fields and Instantons

## Spec (from the manifest)

type: definition (compound: trace inner product on $\mathfrak{su}(N)$; the metric on $\operatorname{ad}P = P\times_{\operatorname{Ad}}\mathfrak g$; the induced covariant derivative $\nabla^\omega$ and $d^\omega$); source items: B-D3.3.3, B-D3.3.4; prereqs: [Def - Associated Bundle, Def - Adjoint Representation, Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles, Def - Local Connection Form and Gauge Potential]; spec: $\lambda(A,B) := -\operatorname{tr}(AB)$ on $\mathfrak{su}(N)$; $\lambda([p,A],[p,B]) := \lambda(A,B)$ on $\operatorname{ad}P$ (well-defined by $\operatorname{Ad}$-invariance, proved on the next page); $\nabla^\omega_X[s,A] := [s,\partial_XA + \operatorname{ad}(s^*\omega(X))A]$ for a local section $s$ of $P$ and $A:U\to\mathfrak g$ (source typos: Bär p. 99 prints "$\partial_Xs$" for $\partial_XA$ and "$s^*\omega(Y)$" for $s^*\omega(X)$); this is the specialisation of the anchor `Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles` to $\rho = \operatorname{Ad}$ (record the dictionary $\nabla^\omega = d + [A_s\wedge\cdot]$ with $A_s = s^*\omega$, Haydys's $d^{\nabla_a}$ on $\operatorname{ad}P$); $d^\omega := d^{\nabla^\omega}$; the identification of Bär's $\bar\Omega$ (an $\operatorname{ad}P$-valued 2-form) with Haydys's $F_a\in\Omega^2(M;\operatorname{ad}P)$ (`[NEEDED FROM I–VI: ad P and the equivariant-horizontal-forms identification]`); examples: $N = 2$, $\lambda(X,Y) = \tfrac12\operatorname{tr}(XY^*)$-type check on the basis $i\sigma_k$; $U(1)$ ($\operatorname{ad}P$ trivial, $\nabla^\omega = d$); non-example: $\operatorname{tr}(AB)$ without the sign is negative definite.
