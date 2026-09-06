---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Associated Bundle"
  - "Def - Principal G-Bundle"
tags: [gauge-theory, associated-bundle, quotient]
---

# Statement

> [!theorem] Associated-bundle construction
> Let $P\to B$ be a smooth principal $G$-bundle and let $G$ act smoothly on a manifold $F$. Then $P\times_GF\to B$ is a smooth fibre bundle with typical fibre $F$. If $F=V$ and the action is linear, it is a vector bundle. For the defining representation,
> $$\operatorname{Fr}(E)\times_{\mathrm{GL}_r}\mathbb K^r\cong E.$$

# Rederivation Scaffold

Use a local section of $P$ to choose a unique representative $[s(x),y]$ of every orbit. This simultaneously proves that the quotient is locally a product and supplies its smooth structure.

# Formal Proof

> [!proof]- Formal Proof
> Let $(U_\alpha,s_\alpha)$ be local sections of $P$. Define
> $$
> \Psi_\alpha:U_\alpha\times F\to(P\times_GF)|_{U_\alpha},
> \qquad (x,y)\mapsto[s_\alpha(x),y].
> $$
> For any $[p,y]$ above $x$, there is a unique $g\in G$ with $p=s_\alpha(x)g$. The quotient relation gives
> $$[p,y]=[s_\alpha(x)g,y]=[s_\alpha(x),gy],$$
> so $\Psi_\alpha$ is surjective. If $[s_\alpha(x),y]=[s_\alpha(x'),y']$, equality of base points gives $x=x'$, and the quotient relation gives a $g$ with $s_\alpha(x)g=s_\alpha(x)$ and $g^{-1}y'=y$. Freeness gives $g=e$, hence $y=y'$. Thus $\Psi_\alpha$ is bijective.
>
> Declare the $\Psi_\alpha$ to be bundle charts. If $s_\beta=s_\alpha g_{\alpha\beta}$, then
> $$
> \Psi_\alpha^{-1}\Psi_\beta(x,y)
> =(x,g_{\alpha\beta}(x)y),
> $$
> which is smooth. These compatible charts give the quotient a unique smooth manifold and fibre-bundle structure. If $F=V$ and the action is linear, the changes of fibre coordinate are linear, so the result is a vector bundle.
>
> For $P=\operatorname{Fr}(E)$ define $\Theta([u,v])=u(v)$. Since
> $$\Theta([ug,v])=ug(v)=u(gv)=\Theta([u,gv]),$$
> it is well defined under the chosen quotient convention. In local frames it is the identity map $U\times\mathbb K^r\to E|_U$, hence a smooth vector-bundle isomorphism.

# Why the Hypotheses Matter

The principal action is free and proper, so the diagonal action on $P\times F$ is free and proper even when the action on $F$ is not. This ensures the orbit-space construction is well behaved; the explicit local charts above prove the stronger bundle statement directly.
