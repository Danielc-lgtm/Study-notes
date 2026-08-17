---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Primitive Hyperbolic Element and Translation Length"
tags: [paper, hyperbolic-geometry]
---

# Signature

| symbol | type |
|---|---|
| $\ell_{\mathrm{sys}}$ | $:=\inf\{\ell_\gamma:\gamma\in\mathcal{P}_X\}\in(0,\infty)$ |
| $\mathcal{P}_X$ | primitive closed geodesics |
| $N_{\mathrm{sys}}$ | $:=\#\{\gamma\in\mathcal{P}_X:\ell_\gamma=\ell_{\mathrm{sys}}\}\in\mathbb{Z}_{\geq2}$ — the multiplicity; **at least $2$**, see (F4) |

---

# Definition

> **Definition (systole).** $\ell_{\mathrm{sys}}:=\displaystyle\inf_{\gamma\in\mathcal{P}_X}\ell_\gamma$: the length of the shortest closed geodesic.

> **(F1) The infimum is attained and positive.** $\ell_{\mathrm{sys}}>0$ and $N_{\mathrm{sys}}<\infty$, because $N_X(R)<\infty$ for every $R$ ([[Ext - Prime Geodesic Theorem|(PGT)(F1)]]): only finitely many geodesics lie below any bound.
>
> **(F2) The uniform bound used in §4.2.** For $L\geq\ell_{\mathrm{sys}}$,
> $$e^L-1\ \geq\ \big(1-e^{-\ell_{\mathrm{sys}}}\big)e^L\qquad\Longrightarrow\qquad \frac{e^{(1-s)L}}{e^L-1}\ \leq\ \frac{e^{-sL}}{1-e^{-\ell_{\mathrm{sys}}}}.$$
> This is the only role the systole plays in §4: it converts the exact mass formula into a clean exponential bound, with a constant depending on $X$ only through $\ell_{\mathrm{sys}}$.
>
> **(F3) It is a minimum over $\mathcal{P}_X$, not over all $L=m\ell_\gamma$.** Every $L$ occurring in §3–§4 satisfies $L=m\ell_\gamma\geq\ell_\gamma\geq\ell_{\mathrm{sys}}$, so (F2) applies to **every** class.
>
> **(F4) $N_{\mathrm{sys}}\geq2$ always.** $\mathcal{P}_X$ consists of **oriented** primitive closed geodesics, and a hyperbolic element of a torsion-free Fuchsian group is never conjugate to its inverse. So $\gamma$ and $\gamma^{-1}$ are distinct elements of $\mathcal{P}_X$ of the same length, and the systolic length is attained at least twice.

---

# Type card

> [!abstract] Type card — $\ell_{\mathrm{sys}}$
> **Given.** **(H1)** $X$ a geometrically finite hyperbolic surface with $\mathcal{P}_X\neq\emptyset$.
>
> **Produces.** A number $\ell_{\mathrm{sys}}\in(0,\infty)$ and a multiplicity $N_{\mathrm{sys}}\in\mathbb{Z}_{\geq2}$.
>
> **Lets you.** (i) bound $1/(e^L-1)$ by $e^{-L}/(1-e^{-\ell_{\mathrm{sys}}})$ uniformly over classes — [[Thm - Finiteness of the Total Mass|Cor 4.7]] Step 1; (ii) name the limit object of [[Thm - Concentration on Systolic Classes|§6.1]], where the probability measure concentrates on the systolic classes as $s\to\infty$.

---

# Depends on

- [[Def - Primitive Hyperbolic Element and Translation Length]] — $\ell_\gamma$ and $\mathcal{P}_X$
- [[Ext - Prime Geodesic Theorem]] — (F1), via local finiteness of the length spectrum
- 🟢 elementary inequalities

---

# Checks

**Instance.** Closed genus-2 surface: $\ell_{\mathrm{sys}}>0$, attained by finitely many geodesics. Generically the shortest geodesic is unique **as an unoriented curve**, giving $N_{\mathrm{sys}}=2$ by (F4); extra symmetry raises it further.

**Non-instance (fails F1 without geometric finiteness).** An infinite-type surface with geodesics of length $\to0$: then $\ell_{\mathrm{sys}}=0$, not attained, and (F2) is vacuous — $1/(1-e^{-\ell_{\mathrm{sys}}})=\infty$. **Consequence:** Corollary 4.7's constant blows up; the finiteness argument as written needs $\ell_{\mathrm{sys}}>0$.

**Non-instance (a peripheral loop).** A loop around a cusp has $\inf$ length $0$, not attained, and no geodesic representative. It is **not** in $\mathcal{P}_X$ and so does not enter $\ell_{\mathrm{sys}}$. See [[Def - Geometrically Finite Surfaces, Cusps and Funnels]].

---

# Used at

- [[Thm - Finiteness of the Total Mass]] — (F2), Step 1 of the proof
- [[Thm - Concentration on Systolic Classes]] — the limit as $s\to\infty$ is supported on $\{\gamma:\ell_\gamma=\ell_{\mathrm{sys}}\}$, $m=1$
- [[§4 Zeta Identities and Finiteness of the Total Mass]] §4.2

---

# Commentary

> [!note]- Commentary (skippable)
> Two entirely different uses, worth keeping apart. In §4.2 the systole is a **technical constant**: it makes one inequality uniform, and any positive lower bound on the lengths would do. In §6.1 it is the **answer**: the probability measure $\mathbb{P}_s$ on free homotopy classes concentrates, as $s\to\infty$, on the classes of the shortest geodesics, each with weight $1/N_{\mathrm{sys}}$.
>
> The second use is the honest content of "loops prefer short geodesics". The mass $\frac1m\frac{e^{(1-s)L}}{e^L-1}$ decays like $e^{-sL}$, so as $s$ grows the smallest $L$ wins, and $L=m\ell_\gamma$ is smallest at $m=1$ and $\ell_\gamma=\ell_{\mathrm{sys}}$. Nothing subtler than that; the multiplicity $N_{\mathrm{sys}}$ appears because ties are not broken.
