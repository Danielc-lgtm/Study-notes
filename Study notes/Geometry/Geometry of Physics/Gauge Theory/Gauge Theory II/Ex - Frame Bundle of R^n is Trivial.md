---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Frame Bundle of a Vector Bundle"
tags: [gauge-theory, frame-bundle, triviality]
---

# Problem Statement

Construct an explicit principal-bundle isomorphism
$$\operatorname{Fr}(T\mathbb R^n)\cong\mathbb R^n\times\mathrm{GL}_n(\mathbb R)$$
and identify the global section which produces it.

# Solution

> [!proof]- Solution
> The coordinate vectors $e_i(x)=\partial_{x^i}|_x$ form a smooth global frame. Let $u_x:\mathbb R^n\to T_x\mathbb R^n$ send the standard basis to $(e_i(x))$. Every frame $v$ at $x$ is uniquely $u_x\circ A$ for $A\in\mathrm{GL}_n$. Therefore
> $$
> \Phi:\mathbb R^n\times\mathrm{GL}_n\to\operatorname{Fr}(T\mathbb R^n),
> \qquad(x,A)\mapsto u_xA
> $$
> is bijective. In standard tangent coordinates, both $\Phi$ and its inverse, which reads off the matrix columns of $v$, are smooth. Moreover $\Phi(x,A B)=\Phi(x,A)B$, so it is a principal-bundle isomorphism. The generating section is $x\mapsto u_x$.

# Key Takeaways

A vector bundle is trivial exactly when its frame bundle has a global section. The choice of section is the choice of trivializing frame, not part of the bare bundle.
