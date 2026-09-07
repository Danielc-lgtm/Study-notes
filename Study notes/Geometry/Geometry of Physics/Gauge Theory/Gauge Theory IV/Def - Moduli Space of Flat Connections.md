---
type: definition
subject: gauge-theory
prereqs: ["Def - Chern-Simons Functional", "Thm - Flat Connections and Monodromy Representations"]
tags: [gauge-theory, flat-connection, moduli-space]
---

# Prerequisite Concepts

- [[Def - Chern-Simons Functional]]
- [[Thm - Flat Connections and Monodromy Representations]]

# The Definition

> [!definition] Flat moduli space
> For a principal $G$-bundle $P\to M$,
> $$\mathcal M_{\mathrm{flat}}(P)=\{A\in\mathcal A(P):F_A=0\}/\mathcal G(P).$$

With a base framing and when bundle topology is allowed to vary, monodromy identifies flat objects with $\operatorname{Hom}(\pi_1(M),G)$; forgetting the framing quotients by conjugation. Stabilizers make the quotient generally singular: reducible representations are precisely the points with larger centralizer.

# Infinitesimal Model

Linearizing curvature at a flat $A$ gives $a\mapsto d_Aa$, while infinitesimal gauge transformations give $\phi\mapsto d_A\phi$. Hence the deformation complex begins
$$\Omega^0(M;\operatorname{Ad}P)\xrightarrow{d_A}\Omega^1(M;\operatorname{Ad}P)\xrightarrow{d_A}\Omega^2(M;\operatorname{Ad}P),$$
where $d_A^2=[F_A,\cdot]=0$. Its first cohomology is the formal tangent space and its zeroth cohomology is the infinitesimal stabilizer.

**True name:** the flat moduli space is the character variety together with its bundle-topology component and singular stabilizer structure.
