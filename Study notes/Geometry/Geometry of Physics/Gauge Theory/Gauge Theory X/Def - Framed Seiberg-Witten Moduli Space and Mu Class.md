---
type: definition
subject: gauge-theory
prereqs: ["Def - Gauge Action and Seiberg-Witten Moduli Space", "Def - Principal G-Bundle"]
tags: [gauge-theory, seiberg-witten, characteristic-class]
---

# Prerequisite Concepts

- [[Def - Gauge Action and Seiberg-Witten Moduli Space]]
- [[Def - Principal G-Bundle]]

# Motivation

A positive-dimensional moduli space cannot be counted point by point. The missing datum is a canonical degree-two cohomology class. It comes from remembering a frame at one base point before quotienting by gauge.

# The Definition

Fix $x_0\in X$ and let
$$\mathcal G_0=\{g\in\mathcal G:g(x_0)=1\}.$$
Evaluation gives an exact sequence
$$1\longrightarrow\mathcal G_0\longrightarrow\mathcal G\xrightarrow{\operatorname{ev}_{x_0}}U(1)\longrightarrow1.$$
On the irreducible solution set define the **framed moduli space**
$$\widehat{\mathcal M}_\eta=\operatorname{SW}_\eta^{-1}(0)/\mathcal G_0.$$
The residual group $\mathcal G/\mathcal G_0\cong U(1)$ acts freely, and
$$\widehat{\mathcal M}_\eta\longrightarrow\mathcal M_\eta$$
is a principal $U(1)$-bundle. Its first Chern class
$$\mu=c_1(\widehat{\mathcal M}_\eta)\in H^2(\mathcal M_\eta;\mathbb Z)$$
is the **point class** or **mu class**.

# Why the residual action is free

If a residual constant $z\in U(1)$ fixes the based-gauge orbit of $(\psi,A)$, then some based $g$ makes $zg$ stabilize $(\psi,A)$. Irreducibility makes this stabilizer trivial, so $zg=1$. Evaluating at $x_0$ gives $z=1$ because $g(x_0)=1$.

# Independence of the base point

A path joining two base points transports the evaluation construction and yields isomorphic residual circle bundles up to homotopy. Consequently the resulting Chern class is independent of the chosen point on connected $X$.
