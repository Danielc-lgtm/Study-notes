---
type: definition
subject: gauge-theory
prereqs: []
tags: [algebraic-topology, homotopy]
---
# Motivation
Homotopy forgets rigid coordinates while retaining the obstruction to continuously deforming one map into another. Gauge theory uses this twice: to classify bundles and gauge transformations, and to read topology from fibrations.

# The Definition
Maps $f_0,f_1:X\to Y$ are **homotopic** if a continuous $H:X\times[0,1]\to Y$ satisfies $H(-,i)=f_i$. Spaces $X,Y$ are **homotopy equivalent** if maps $f:X\to Y$ and $g:Y\to X$ have $gf\simeq\operatorname{id}_X$ and $fg\simeq\operatorname{id}_Y$. A space homotopy equivalent to a point is **contractible**.

For a based space $(X,x_0)$,
$$\pi_n(X,x_0)=[(S^n,*),(X,x_0)]_*.$$
Concatenation gives a group for $n\ge1$; the two independent concatenation directions and the Eckmann–Hilton argument make it abelian for $n\ge2$. A based map induces $f_*:\pi_n(X)\to\pi_n(Y)$, and based-homotopic maps induce the same homomorphism. Hence homotopy equivalences induce isomorphisms on all homotopy groups.

# Calibration
$\mathbb R^n$ is contractible; $\mathbb R^{n+1}\setminus\{0\}$ deformation retracts onto $S^n$; $\pi_1(S^1)\cong\mathbb Z$ by winding number, while $\pi_k(S^1)=0$ for $k>1$ by lifting to $\mathbb R$.
