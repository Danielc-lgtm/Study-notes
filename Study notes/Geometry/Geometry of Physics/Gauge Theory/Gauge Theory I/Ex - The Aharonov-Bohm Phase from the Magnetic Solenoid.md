---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Wilson Line and Holonomy of a Connection"
  - "Def - U(1) Gauge Field and Electromagnetic Connection"
tags: [gauge-theory, aharonov-bohm, holonomy, electromagnetism]
---

# Prerequisite Concepts

- [[Def - Wilson Line and Holonomy of a Connection]]
- [[Def - U(1) Gauge Field and Electromagnetic Connection]]

# Problem Statement

Let $M=\mathbb R^2\setminus\{0\}$ and let
$$A=\frac{\Phi}{2\pi},d\varphi
=\frac{\Phi}{2\pi}\frac{-y,dx+x,dy}{x^2+y^2}.$$
Show that $F=dA=0$ on $M$, compute the holonomy of $\nabla=d+iqA$ around a positively oriented circle winding $n$ times about the origin, and determine when the connection is gauge-equivalent to the trivial connection by a single-valued $U(1)$ gauge transformation.

# Convergent Strategy

Local exactness proves flatness. The global integral of $d\varphi$ records winding number. A gauge transformation removing $A$ must itself be single-valued after $\varphi\mapsto\varphi+2\pi$.

# Solution

> [!proof]- Solution
> On every simply connected angular chart, $d\varphi$ is the differential of a smooth branch of $\varphi$, so $d(d\varphi)=0$. Hence $F=dA=0$ globally on $M$.
>
> For a loop $\gamma_n$ of winding number $n$,
> $$\int_{\gamma_n}A=\frac{\Phi}{2\pi}\int_{\gamma_n}d\varphi=n\Phi.$$
> With the convention $\nabla=d+iqA$, parallel transport therefore is
> $$
> \operatorname{Hol}_{\gamma_n}(\nabla)
> =\exp(-iqn\Phi).
> $$
>
> Locally the active transformation $u=e^{iq(\Phi/2\pi)\varphi}$ sends $A$ to zero (choose the inverse if using the passive convention). It is single-valued precisely when
> $$
> e^{iq\Phi}=1,
> \qquad\text{equivalently}\qquad q\Phi\in2\pi\mathbb Z.
> $$
> This is also exactly the condition that the holonomy of the generating loop be trivial. Thus flatness alone does not imply global gauge-triviality; the remaining obstruction is monodromy.

# Key Takeaways

The phase is not evidence that a particular local potential is observable. The gauge-invariant object is the holonomy of the connection. Curvature detects infinitesimal transport, while holonomy can retain global information invisible to curvature on a nonsimply-connected base.
