---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Homogeneous Bundle"
  - "Def - Orthonormal Frame Bundle"
tags: [gauge-theory, associated-bundle, sphere]
---

# Problem Statement

Identify $SO(3)\to S^2$, $R\mapsto Re_3$, as the oriented orthonormal frame bundle of $S^2$ and prove
$$TS^2\cong SO(3)\times_{SO(2)}\mathbb R^2.$$

# Solution

> [!proof]- Solution
> For $R\in SO(3)$, the ordered pair $(Re_1,Re_2)$ is an oriented orthonormal basis of $(Re_3)^\perp=T_{Re_3}S^2$. Conversely, an oriented orthonormal tangent frame $(v_1,v_2)$ at $x$ determines the unique matrix $R$ with columns $(v_1,v_2,x)$; it lies in $SO(3)$. These assignments are smooth inverses.
>
> The stabilizer of $e_3$ consists of block rotations $\operatorname{diag}(A,1)$ with $A\in SO(2)$, and right multiplication changes $(Re_1,Re_2)$ by that basis matrix. Hence $SO(3)\to S^2$ is the oriented frame bundle.
>
> Define
> $$[R,a]\longmapsto R(a_1e_1+a_2e_2).$$
> With the associated-bundle relation $[RA,a]=[R,Aa]$, the map is well defined. It is linear and bijective on every fibre and smooth in local frames, hence is a vector-bundle isomorphism.

# Key Takeaways

The principal frame bundle stores bases; the defining representation reconstructs tangent vectors. Other $SO(2)$ representations construct other homogeneous bundles over $S^2$.
