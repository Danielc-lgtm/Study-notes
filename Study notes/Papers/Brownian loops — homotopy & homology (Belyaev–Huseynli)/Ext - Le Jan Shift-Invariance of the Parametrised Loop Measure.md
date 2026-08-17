---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, probability, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $(\mathcal{E},\mathcal{F})$ | a [[Def - Regular Symmetric Dirichlet Form\|regular symmetric Dirichlet form]] on $L^2(E,m)$ with transition density $p^{\mathcal{E}}$ |
| $W^{t,\mathcal{E}}_{x\to x}$ | the [[Def - Unnormalised Bridge Measure by Disintegration\|unnormalised diagonal bridge]]; $\lvert W^{t,\mathcal{E}}_{x\to x}\rvert=p^{\mathcal{E}}(t,x,x)$ |
| $\mu^{*,\mathcal{E}}$ | $\displaystyle\int_0^\infty\frac{\mathrm{d}t}{t}\int_E W^{t,\mathcal{E}}_{x\to x}\,m(\mathrm{d}x)$ — a measure on $\mathcal{C}^*_E$ |
| $\mathrm{shift}_{s_0}$ | the circular time-shift on $\mathcal{C}^*_E$ |
| $q$ | $\mathcal{C}^*_E\to\mathcal{C}_E$, the quotient by $\sim$ |

---

# Statement

> **(LJ) Shift-invariance of the parametrised loop measure.** *Precondition:*
> **(P1)** $(\mathcal{E},\mathcal{F})$ regular symmetric Dirichlet form on $L^2(E,m)$;
> **(P2)** $e^{-tA}$ admits a jointly measurable symmetric transition density $p^{\mathcal{E}}$ against $m$.
>
> *Conclusion:* $\mu^{*,\mathcal{E}}$ is invariant under every circular time-shift:
> $$(\mathrm{shift}_{s_0})_*\,\mu^{*,\mathcal{E}}=\mu^{*,\mathcal{E}}\qquad\text{for all }s_0 .$$
> It is also invariant under increasing continuous reparametrisation. Consequently $\mu^{*,\mathcal{E}}$ descends: $q_*\mu^{*,\mathcal{E}}$ is a well-defined $\sigma$-finite measure on $\mathcal{C}_E$.

---

# Type card

> [!abstract] Type card — (LJ)
> **Given.** (P1),(P2).
>
> **Produces.** Invariance of $\mu^{*,\mathcal{E}}$ under the group generating $\sim$; hence a well-defined pushforward $q_*\mu^{*,\mathcal{E}}$ on $\mathcal{C}_E$, $\sigma$-finite, of total mass $\int_0^\infty\frac1t\int_Ep^{\mathcal{E}}(t,x,x)\,m(\mathrm{d}x)\,\mathrm{d}t$.
>
> **Lets you.** Define *the loop measure* — an object on geometric loops — rather than only a measure on rooted parametrised ones. Without it, $\mu_X$, $\mu^{\mathcal{E}}_X$, $\mu^\phi_X$ do not exist as stated.

---

# Status

- **Proved here:** no.
- **Source:** Le Jan, *Markov paths, loops and fields* (Saint-Flour XXXVIII-2008, Springer LNM 2026, 2011), Chapter 2.
- **DAG node that would close this:** *GFF Isomorphism Theorems / Loop Soups* (🔵), whose key reference is exactly Le Jan.
- **What is safe to assume:** shift-invariance and hence well-definedness of the pushforward. The paper uses nothing else from Le Jan's chapter, and no proof in §3–§7 unfolds the pushforward.

---

# Used at

- [[Constr - The Brownian Loop Measure]] — $\mu_X:=q_*\mu^*_X$
- [[Constr - The Dirichlet-Form Loop Measure]] — $\mu^{\mathcal{E}}_X:=q_*\mu^{*,\mathcal{E}}_X$
- [[Constr - The Subordinate Brownian Loop Measure]] — $\mu^\phi_X:=q_*\mu^{*,\phi}_X$

---

# Commentary

> [!note]- Commentary (skippable)
> The invariance is where symmetry of the form is spent. Heuristically, $\mu^{*,\mathcal{E}}$ is built from the diagonal $p^{\mathcal{E}}(t,x,x)$, and rotating the root of a loop of duration $t$ by $s_0$ decomposes the diagonal via Chapman–Kolmogorov as $\int p^{\mathcal{E}}(s_0,x,y)p^{\mathcal{E}}(t-s_0,y,x)\,m(\mathrm{d}y)$, which is symmetric in the two factors exactly when $p^{\mathcal{E}}(t,x,y)=p^{\mathcal{E}}(t,y,x)$. The weight $\mathrm{d}t/t$ does not enter — the invariance holds fibrewise in $t$.
>
> This is also where the $\mathrm{d}t/t$ weight earns a second justification. Shift-invariance holds for any weight; but the further invariance under *reparametrisation*, which is what makes $\mathcal{C}_E$ rather than $\bigsqcup_t\{\text{loops of duration }t\}$ the right quotient, is what forces the scale-invariant $\mathrm{d}t/t$.
