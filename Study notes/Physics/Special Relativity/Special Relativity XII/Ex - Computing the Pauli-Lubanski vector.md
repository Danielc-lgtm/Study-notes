---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Casimir Invariants of the Poincaré Group"
  - "Def - Angular Momentum Four-Tensor"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Problem Statement

The Pauli–Lubanski four-vector is $W^\mu = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma$, where $J^{\mu\nu}$ is the [[Def - Angular Momentum Four-Tensor|angular-momentum tensor]] and $P^\mu$ the four-momentum. Working with $c = 1$, $\eta = \mathrm{diag}(1,-1,-1,-1)$, and $\varepsilon^{0123} = +1$:

1. Show that $W \cdot P = W^\mu P_\mu = 0$ identically, for any $J^{\mu\nu}$ and any $P^\mu$.
2. Evaluate $W^\mu$ in the rest frame of a massive particle, where $P = (m, 0, 0, 0)$. Show $W^0 = 0$ and $W^i = m\,J^i$, where $J^i = \tfrac{1}{2}\epsilon^{ijk}J_{jk}$ is the spin three-vector.
3. Hence compute the spin Casimir $W^2 = W_\mu W^\mu$ in the rest frame and show $W^2 = -m^2\,\boldsymbol{J}^2$, which on a spin-$s$ representation is $-m^2 s(s+1)$.
4. Verify that $W^2$ is a Lorentz scalar (so its rest-frame value holds in all frames), and conclude that $(P^2, W^2) = (m^2, -m^2 s(s+1))$ are the two Casimir labels.

**Recall:**

![[Def - Casimir Invariants of the Poincaré Group#The Definition]]

The [[Def - Angular Momentum Four-Tensor|angular-momentum tensor]] $J^{\mu\nu} = -J^{\nu\mu}$ generates Lorentz transformations; its spatial part $J^{jk}$ encodes the rotation generators, with the spin three-vector $J^i = \tfrac{1}{2}\epsilon^{ijk}J_{jk}$ (so $J^{12} = J^3$, etc.), and its mixed part $J^{0i}$ the boost generators. The four-momentum $P^\mu = (E, \boldsymbol{P})$ has $P^2 = m^2$ on the mass shell; see [[Def - Four-Momentum and Rest Mass]]. The symbol $\varepsilon^{\mu\nu\rho\sigma}$ is totally antisymmetric with $\varepsilon^{0123} = +1$.

---

# Convergent Strategy

**Problem class.** A *compute-an-invariant* problem: evaluate a tensor expression in a convenient frame and use Lorentz invariance to extend. The [[Special Relativity XII — Inertial Observers and the Poincaré Group#Problem-Solving Strategy|topic strategy]] for representation problems says to fix a standard momentum (here the rest frame) and reduce.

**Assumption pattern.** The decisive simplification is the rest frame $P = (m, \mathbf{0})$, which kills three of the four components of $P_\sigma$, collapsing the sum over $\sigma$ to $\sigma = 0$. The signpost is "compute $W^\mu$ or $W^2$": go to the rest frame, where only $P_0 = m$ survives, and the Levi-Civita symbol then picks out the spatial rotation generators.

**Theorem routing.** The route: (i) $W\cdot P = 0$ from antisymmetry of $\varepsilon$ against $P_\sigma P_\mu$; (ii) in the rest frame, $W^\mu = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho 0}J_{\nu\rho}\,m$, which vanishes for $\mu = 0$ and gives $W^i = m J^i$ for $\mu = i$; (iii) $W^2 = -m^2\boldsymbol{J}^2 = -m^2 s(s+1)$ using $\boldsymbol{J}^2 = s(s+1)$; (iv) $W^2$ is a scalar built from the four-vector $W^\mu$, so its value is frame-independent.

**Key decision point.** The crux is recognising that the rest-frame momentum forces $\sigma = 0$, so the surviving Levi-Civita symbol is $\varepsilon^{\mu\nu\rho 0}$, which is nonzero only for spatial $\mu, \nu, \rho$ — projecting out exactly the *rotation* part $J_{jk}$ of the angular momentum, not the boost part $J_{0i}$. This is *why* the Pauli–Lubanski vector measures spin (rest-frame rotation) and discards orbital/boost information. Choosing the rest frame is what makes the spin visible.

---

# Legal Operations Used

1. **Identify a Casimir by checking it commutes with all generators** (operation 8 from the topic page), here realised concretely: $W\cdot P = 0$ and the four-vector nature of $W^\mu$ make $W^2$ a Lorentz scalar.

2. **Classify a representation via its little group** (operation 9 from the topic page): evaluating in the rest frame is choosing the standard massive momentum, whose little group $\mathrm{SO}(3)$ supplies $\boldsymbol{J}^2 = s(s+1)$.

3. **Compute an invariant in the most convenient frame** (the master invariance technique from earlier chapters): $W^2$ is evaluated in the rest frame and the result holds everywhere by Lorentz invariance.

---

# Hints

> [!note]- Hint 1
> For $W\cdot P$: write $W^\mu P_\mu = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma P_\mu$. The factor $P_\sigma P_\mu$ is symmetric in $(\sigma, \mu)$, but $\varepsilon^{\mu\nu\rho\sigma}$ is antisymmetric in $(\mu, \sigma)$. A symmetric tensor contracted with an antisymmetric one vanishes.

> [!note]- Hint 2
> In the rest frame $P_\sigma = (m, 0, 0, 0)$ (lowering: $P_0 = m$, $P_i = 0$). So $W^\mu = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho 0}J_{\nu\rho}\,m$. The symbol $\varepsilon^{\mu\nu\rho 0}$ is nonzero only when $\mu, \nu, \rho$ are spatial, so $W^0 = 0$ (it would need a spatial index in the last slot too) and $W^i = -\tfrac{m}{2}\varepsilon^{i j k 0}J_{jk}$.

> [!note]- Hint 3
> Use $\varepsilon^{ijk0} = -\varepsilon^{ijk}$ (moving the $0$ from last to... actually $\varepsilon^{ijk0} = -\varepsilon^{0ijk}$ by three transpositions, and $\varepsilon^{0ijk} = \epsilon^{ijk}$ the 3D symbol). Carefully: $\varepsilon^{ijk0}$ equals $\epsilon^{ijk}$ up to sign; track it to get $W^i = m\cdot\tfrac{1}{2}\epsilon^{ijk}J_{jk} = m J^i$.

> [!note]- Hint 4
> $W^2 = \eta_{\mu\nu}W^\mu W^\nu$. In the rest frame $W = (0, m\boldsymbol{J})$, so $W^2 = -m^2(J^1{}^2 + J^2{}^2 + J^3{}^2) = -m^2\boldsymbol{J}^2$. On a spin-$s$ irreducible, the $\mathrm{SO}(3)$ Casimir is $\boldsymbol{J}^2 = s(s+1)$, giving $W^2 = -m^2 s(s+1)$.

---

# Solution

The computation goes to the rest frame, where the momentum picks out the rotation part of the angular momentum. Step 1 proves $W\cdot P = 0$ from symmetry. Step 2 evaluates $W^\mu$ in the rest frame as $(0, m\boldsymbol{J})$. Step 3 squares it to $-m^2 s(s+1)$. Step 4 confirms $W^2$ is a Lorentz scalar, so the value is universal.

**Step 1: $W \cdot P = 0$ identically.**

> [!note]- Derivation
> Contract $W^\mu$ with $P_\mu$:
> $$W^\mu P_\mu = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma P_\mu.$$
> Consider the factor $P_\sigma P_\mu$: it is **symmetric** under exchange of $\sigma$ and $\mu$ (multiplication of numbers commutes). But $\varepsilon^{\mu\nu\rho\sigma}$ is **antisymmetric** under exchange of $\mu$ and $\sigma$ (it is totally antisymmetric). A sum over a symmetric pair of indices contracted with an antisymmetric pair vanishes: for any symmetric $S^{\mu\sigma} = S^{\sigma\mu}$ and antisymmetric $A_{\mu\sigma} = -A_{\sigma\mu}$, $A_{\mu\sigma}S^{\mu\sigma} = -A_{\sigma\mu}S^{\mu\sigma} = -A_{\sigma\mu}S^{\sigma\mu} = -A_{\mu\sigma}S^{\mu\sigma}$ (relabel), so $A_{\mu\sigma}S^{\mu\sigma} = 0$. Here $A = \varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}$ (antisymmetric in $\mu\sigma$ for each fixed $\nu\rho$) and $S = P_\mu P_\sigma$, giving
> $$W^\mu P_\mu = 0.$$
> This holds for *any* $J^{\mu\nu}$ and *any* $P^\mu$ — the orthogonality is an identity, not a special-frame fact. It is what makes $W$ measure only the intrinsic spin (orthogonal to the momentum), discarding the longitudinal/orbital part.

**Step 2: Rest-frame evaluation $W = (0, m\boldsymbol{J})$.**

> [!note]- Derivation
> In the rest frame of a massive particle, $P^\mu = (m, 0, 0, 0)$, so lowering with $\eta$, $P_\sigma = (m, 0, 0, 0)$ as well ($P_0 = m$, $P_i = 0$). The Pauli–Lubanski vector becomes
> $$W^\mu = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho 0}J_{\nu\rho}\,m,$$
> only $\sigma = 0$ surviving. The symbol $\varepsilon^{\mu\nu\rho 0}$ is nonzero only when $\{\mu, \nu, \rho\}$ are the three spatial indices $\{1, 2, 3\}$ (the fourth slot being $0$).
>
> *Time component.* For $\mu = 0$: $\varepsilon^{0\nu\rho 0} = 0$ (two indices equal to $0$), so $W^0 = 0$. The Pauli–Lubanski vector has no time component in the rest frame — consistent with $W\cdot P = 0$, which in the rest frame reads $W^0 m = 0$.
>
> *Spatial components.* For $\mu = i$ (spatial): $W^i = -\tfrac{m}{2}\varepsilon^{ijk0}J_{jk}$, summing over spatial $j, k$. Now $\varepsilon^{ijk0} = -\varepsilon^{ijk0}$... evaluate the sign: moving the index $0$ from the fourth slot to the first costs three transpositions, $\varepsilon^{ijk0} = (-1)^3\varepsilon^{0ijk} = -\varepsilon^{0ijk}$, and $\varepsilon^{0ijk} = \epsilon^{ijk}$ (the three-dimensional Levi-Civita symbol, since the time index is fixed). Hence $\varepsilon^{ijk0} = -\epsilon^{ijk}$, and
> $$W^i = -\tfrac{m}{2}(-\epsilon^{ijk})J_{jk} = \tfrac{m}{2}\epsilon^{ijk}J_{jk} = m\,J^i,$$
> where $J^i = \tfrac{1}{2}\epsilon^{ijk}J_{jk}$ is the **spin three-vector** (the dual of the spatial rotation generators). So in the rest frame
> $$W = (0,\; m\boldsymbol{J}), \qquad \boldsymbol{J} = (J^1, J^2, J^3).$$
> The Pauli–Lubanski vector is $m$ times the rest-frame spin. Crucially, it picked out the *rotation* part $J_{jk}$ of the angular momentum and discarded the boost part $J_{0i}$ — because the momentum's only nonzero component $P_0$ forced $\sigma = 0$, leaving the purely spatial $\varepsilon^{ijk0}$.

**Step 3: The spin Casimir $W^2 = -m^2 s(s+1)$.**

> [!note]- Derivation
> Compute $W^2 = \eta_{\mu\nu}W^\mu W^\nu$ in the rest frame, where $W = (0, m\boldsymbol{J})$:
> $$W^2 = \eta_{00}(W^0)^2 + \eta_{ij}W^i W^j = (1)(0)^2 + (-\delta_{ij})(mJ^i)(mJ^j) = -m^2\sum_{i}(J^i)^2 = -m^2\,\boldsymbol{J}^2.$$
> On an irreducible spin-$s$ representation, the spatial rotation generators $J^i$ furnish the spin-$s$ representation of $\mathrm{SU}(2)$ (the rest-frame little group), whose Casimir is $\boldsymbol{J}^2 = J^1{}^2 + J^2{}^2 + J^3{}^2 = s(s+1)\,\mathbb{1}$. Hence
> $$W^2 = -m^2\,s(s+1).$$
> This is the spin Casimir, carrying the spin label $s \in \{0, \tfrac{1}{2}, 1, \ldots\}$. (The minus sign is the mostly-minus signature: $W$ is spacelike for a massive particle, having only spatial components in the rest frame, so $W^2 < 0$.)

**Step 4: $W^2$ is a Lorentz scalar.**

> [!note]- Derivation
> The Pauli–Lubanski vector $W^\mu$ transforms as a genuine four-vector under Lorentz transformations: $[J_{\mu\nu}, W_\rho] = i(\eta_{\nu\rho}W_\mu - \eta_{\mu\rho}W_\nu)$, the standard vector transformation rule (it is built by contracting tensors $\varepsilon, J, P$ with all-contracted indices except the free $\mu$). Therefore its square $W^2 = W_\mu W^\mu$ is a **Lorentz scalar** — invariant under all Lorentz transformations. Since the rest-frame value is $-m^2 s(s+1)$, *this is the value in every frame*. (One cannot reach the rest frame for a massless particle, $m = 0$; that case is handled separately, with $W^2 = 0$ and the helicity label — see [[Ex - Classifying massive versus massless representations]].)
>
> Moreover $W^\mu$ commutes with the translations, $[W^\mu, P^\nu] = 0$ (it is built from $P$ and the translation-covariant combination of $J$), so $W^2$ commutes with both translations and Lorentz generators: it is a **Casimir**. Together with $P^2 = m^2$, the pair $(P^2, W^2) = (m^2, -m^2 s(s+1))$ are the two Casimir invariants labelling the irreducible representation — the mass and the spin.

> [!note]- Complete formal solution
> *Orthogonality:* $W^\mu P_\mu = -\tfrac{1}{2}\varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma P_\mu = 0$, since $\varepsilon$ is antisymmetric in $(\mu, \sigma)$ while $P_\mu P_\sigma$ is symmetric. *Rest frame:* with $P_\sigma = (m, \mathbf{0})$, $W^\mu = -\tfrac{m}{2}\varepsilon^{\mu\nu\rho 0}J_{\nu\rho}$; for $\mu = 0$ this vanishes (repeated $0$), for $\mu = i$ it gives $W^i = -\tfrac{m}{2}(-\epsilon^{ijk})J_{jk} = m\cdot\tfrac{1}{2}\epsilon^{ijk}J_{jk} = mJ^i$, so $W = (0, m\boldsymbol{J})$. *Square:* $W^2 = \eta_{ij}W^iW^j = -m^2\boldsymbol{J}^2 = -m^2 s(s+1)$ on a spin-$s$ representation, using the $\mathrm{SO}(3)$ Casimir $\boldsymbol{J}^2 = s(s+1)$. *Invariance:* $W^\mu$ is a four-vector and commutes with $P^\nu$, so $W^2$ is a Lorentz scalar commuting with all generators — a Casimir — and its rest-frame value $-m^2 s(s+1)$ holds in every frame. With $P^2 = m^2$, the pair $(m^2, -m^2 s(s+1))$ labels the irreducible representation by mass and spin. $\blacksquare$

---

# Key Takeaways

**The rest frame makes the spin visible: the momentum projects the angular momentum onto its rotation part.** The whole computation works because, in the rest frame $P = (m, \mathbf{0})$, the only surviving momentum component $P_0$ forces $\sigma = 0$ in the Levi-Civita contraction, leaving $\varepsilon^{ijk0}$ — which picks out the *spatial* rotation generators $J_{jk}$ and discards the boost generators $J_{0i}$. This is the precise mechanism by which the Pauli–Lubanski vector measures *intrinsic spin* rather than orbital angular momentum or boost: it is the angular momentum contracted against the momentum, and contracting against the rest-frame momentum keeps only the rest-frame rotation. The transferable lesson: when an invariant built from a tensor and a vector is opaque, evaluate it in the frame where the vector is simplest (here the rest frame), and watch which components of the tensor the contraction selects. The selection *is* the physical meaning of the invariant.

**$W \cdot P = 0$ is an identity from antisymmetry, and it is the structural reason $W$ measures spin.** The orthogonality $W^\mu P_\mu = 0$ is not a rest-frame accident but an identity, forced by contracting the antisymmetric $\varepsilon$ against the symmetric $P_\mu P_\sigma$. Its content is that $W$ lives in the three-dimensional space orthogonal to the momentum — exactly the rest-frame spatial directions, where spin lives. This single constraint removes one of $W$'s four components (leaving three for massive, collapsing to one helicity for massless), and forgetting it leads to nonsense (expecting four spin components, or treating $W$ as timelike). The reusable pattern: whenever a four-vector is built by contracting an antisymmetric symbol against a momentum, expect it to be orthogonal to that momentum, and expect that orthogonality to be the key to its physical interpretation. The same structure gives the classical [[Def - Spin Four-Vector|spin four-vector]] $S\cdot U = 0$.

**A scalar built from a four-vector is evaluated in the convenient frame and holds everywhere — this is the master invariance move applied to spin.** The final step, that $W^2$ is a Lorentz scalar so its rest-frame value $-m^2 s(s+1)$ is universal, is the same labour-saving technique that pervades all of relativistic calculation: compute an invariant where it is easiest, transport the answer everywhere. Here the rest frame makes $W = (0, m\boldsymbol{J})$ trivial, and Lorentz invariance promotes $-m^2 s(s+1)$ to the value in every frame. The diagnostic to recognise the technique's applicability: any quantity that is manifestly a Lorentz scalar (a fully-contracted tensor expression) may be evaluated in any single convenient frame. For the spin Casimir the convenient frame is the rest frame; for a particle's invariant mass it is the centre-of-momentum frame; for a system's energy it is wherever the momenta simplify. The recurring move — "it is a scalar, so compute it where it is easy" — is the through-line from the invariant interval of Special Relativity I to the spin Casimir here.
