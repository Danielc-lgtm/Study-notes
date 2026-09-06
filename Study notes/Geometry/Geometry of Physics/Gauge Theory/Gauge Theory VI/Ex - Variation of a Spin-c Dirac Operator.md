---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs: ["Def - Spinor Bundle, Chirality, and Twisted Dirac Operator"]
tags: [gauge-theory, spin-c, dirac-operator]
---

# Problem Statement

If determinant-line connections differ by $a\in\Omega^1(M;i\mathbb R)$, prove
$$D_{A+a}\psi=D_A\psi+\frac12c(a)\psi.$$

# Solution

> [!solution]- Solution
> Locally regard the spin-c bundle as $S_{Spin}\otimes L_0$, where the determinant line is $L_0^2$. A connection $B$ on $L_0$ induces $A=2B$ on $L_0^2$. Therefore replacing $A$ by $A+a$ replaces $B$ by $B+a/2$. The product spinor connection changes by scalar multiplication by $a/2$; composing with Clifford multiplication gives $D_{A+a}-D_A=c(a/2)=\frac12c(a)$. Although $L_0$ may not exist globally, both sides transform identically, so the local calculation descends.

