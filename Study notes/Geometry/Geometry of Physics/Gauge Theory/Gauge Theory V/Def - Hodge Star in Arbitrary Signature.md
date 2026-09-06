---
type: definition
subject: gauge-theory
prereqs: ["Def - The Hodge Star Operator"]
tags: [gauge-theory, hodge-star, pseudo-riemannian]
---

# Motivation

Gauge-field equations use the metric only through the Hodge star. Its square changes between Euclidean and Lorentzian signature, so self-duality and the sign of the action cannot be transported between the two settings without an explicit convention.

# The Definition

> [!definition] Pseudo-Riemannian Hodge star
> Let $(M^n,g)$ be oriented with signature $(p,q)$, where $q$ is the number of negative directions. The Hodge star is the unique map
> $$*: \Omega^k(M)\to\Omega^{n-k}(M)$$
> satisfying
> $$\alpha\wedge *\beta=\langle\alpha,\beta\rangle_g\operatorname{vol}_g$$
> for all $k$-forms $\alpha,eta$.

On $k$-forms,
$$*^2=(-1)^{k(n-k)+q}.$$
To verify the sign, evaluate on an oriented orthonormal coframe: moving the complementary indices back into order contributes $(-1)^{k(n-k)}$, while the product of the metric signs contributes $(-1)^q$.

# Four-Dimensional Consequences

In Euclidean signature $(4,0)$, $*^2=1$ on two-forms and
$\Omega^2=\Omega^2_+\oplus\Omega^2_-$. In Lorentzian signature with one negative direction, $*^2=-1$ on real two-forms; the eigenvalues are $\pm i$ only after complexification. Real instanton equations therefore belong to Euclidean geometry.

# Legal Operations and Calibration

The star commutes with gauge transformations because it acts on the form factor, whereas gauge transformations act on the adjoint factor. It does not commute with arbitrary conformal rescaling, but on middle-degree forms in dimension $n=2k$ it is conformally invariant.

**Calibration check.** In oriented Euclidean $\mathbb R^4$, $*(dx^1\wedge dx^2)=dx^3\wedge dx^4$ and applying $*$ again returns the original form.
