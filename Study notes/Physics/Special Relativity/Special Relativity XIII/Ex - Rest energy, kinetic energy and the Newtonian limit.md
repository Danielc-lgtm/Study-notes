---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Thm - Mass-Energy Equivalence"
tags: [physics, special-relativity]
---

# Problem Statement

For a particle of rest mass $m$ moving at speed $u$ with Lorentz factor $\gamma = (1-u^2/c^2)^{-1/2}$:

1. Derive the energy–momentum relation $E^2 = \mathbf{p}^2 c^2 + m^2 c^4$ by squaring the four-momentum in the rest frame.
2. Expand the total energy $E = \gamma mc^2$ in powers of $u/c$ and identify the rest energy and the kinetic energy; verify the kinetic energy reduces to $\tfrac12 mu^2$ for $u\ll c$.
3. An LHC proton has total energy $E = 7$ TeV; the proton rest energy is $mc^2 = 0.938$ GeV. Find its Lorentz factor $\gamma$ and its speed relative to $c$.
4. An ultra-high-energy cosmic-ray proton has $E = 10^{20}$ eV. Find its Lorentz factor and how close its speed is to $c$.

**Recall:**

![[Thm - Mass-Energy Equivalence#Statement]]

The [[Def - Four-Momentum and Rest Mass|four-momentum]] is $P^\mu = (E, \mathbf{p}) = (\gamma mc^2, \gamma mc\,\mathbf{u}/c\cdots)$; in natural units $P = (\gamma m, \gamma m\mathbf{u})$ with $P\cdot P = m^2$. The total energy is $E = \gamma mc^2$, the rest energy $mc^2$, the kinetic energy $E_{\text{kin}} = (\gamma-1)mc^2$. The Minkowski square $P\cdot P$ is a Lorentz invariant.

---

# Convergent Strategy

**Problem class.** A *derive-and-estimate* problem combining the [[Special Relativity XIII — Energy and Momentum#Problem-Solving Strategy|invariant-square technique]] (part 1) with the Newtonian-limit expansion (part 2) and order-of-magnitude evaluation (parts 3–4). The recurring tool is $E = \gamma mc^2$ together with the mass-shell.

**Assumption pattern.** A single particle with known mass and either speed or energy. The signpost for part 1 is "energy–momentum relation", which is always the squared mass-shell; for parts 3–4 the data are energies and the unknown is $\gamma$, so $\gamma = E/mc^2$ directly.

**Theorem routing.** Part 1 evaluates the invariant $P\cdot P$ in two frames ([[Thm - Mass-Energy Equivalence]] Lemma 2). Part 2 is the Taylor expansion of $\gamma$ ([[Thm - Mass-Energy Equivalence]] Lemma 1). Parts 3–4 use $\gamma = E/mc^2$ from $E = \gamma mc^2$, then $u/c = \sqrt{1 - \gamma^{-2}}$.

**Key decision point.** For the cosmic-ray and LHC speeds, the crux is that $\gamma$ is enormous, so $u$ is *extraordinarily* close to $c$ and the naive $u = c\sqrt{1-\gamma^{-2}}$ underflows; one must expand $1 - u/c \approx 1/(2\gamma^2)$ to see how close. The non-obvious move is to compute the *deficit* $1 - u/c$ rather than $u$ itself.

---

# Legal Operations Used

1. **Square a four-momentum to extract an invariant mass** (operation 2 from the topic page). Part 1 evaluates $P\cdot P$ in the rest frame ($=m^2c^2$) and a general frame ($= E^2/c^2 - \mathbf{p}^2$).

2. **Use the mass-shell to trade energy for momentum** (operation 8). The energy–momentum relation is the mass-shell; given $E$ and $m$ it gives $|\mathbf{p}|$, and given $\gamma$ it gives $u$.

3. **Use a Lorentz invariant to switch frames** (operation 6). The rest-frame value $m^2c^2$ of the invariant transports to the moving frame, yielding the relation.

---

# Hints

> [!note]- Hint 1
> The Minkowski square $P\cdot P$ is the same in every frame. In the rest frame $P = (mc, \mathbf{0})$ so $P\cdot P = m^2c^2$. In a general frame $P = (E/c, \mathbf{p})$ so $P\cdot P = E^2/c^2 - \mathbf{p}^2$. Equate.

> [!note]- Hint 2
> Expand $\gamma = (1-u^2/c^2)^{-1/2} = 1 + \tfrac12 u^2/c^2 + \tfrac38 u^4/c^4 + \cdots$, multiply by $mc^2$. The constant term is the rest energy $mc^2$; the next is $\tfrac12 mu^2$, the Newtonian kinetic energy.

> [!note]- Hint 3
> From $E = \gamma mc^2$, $\gamma = E/(mc^2)$. With $E = 7$ TeV $= 7000$ GeV and $mc^2 = 0.938$ GeV, $\gamma \approx 7500$. Then $u/c = \sqrt{1 - \gamma^{-2}}$, but since $\gamma$ is huge, compute the deficit $1 - u/c \approx 1/(2\gamma^2)$.

> [!note]- Hint 4
> $\gamma = E/(mc^2) = 10^{20}/(0.938\times 10^9) \approx 10^{11}$. The deficit from $c$ is $1 - u/c \approx 1/(2\gamma^2) \approx 5\times10^{-23}$. This is the fastest known massive particle relative to a terrestrial observer.

---

# Solution

A particle's energy is $E = \gamma mc^2 = mc^2 + E_{\text{kin}}$, with rest energy $mc^2$ and kinetic energy $(\gamma-1)mc^2$; the mass-shell gives $E^2 = \mathbf{p}^2c^2 + m^2c^4$. Part 1 derives the mass-shell by an invariant-square argument; Part 2 expands $\gamma$ to recover Newton; Parts 3–4 evaluate $\gamma$ and the speed deficit for high-energy protons. The non-obvious step in 3–4 is computing how close $u$ is to $c$ via the deficit $1 - u/c \approx 1/2\gamma^2$.

**Step 1: The energy–momentum relation.**

> [!note]- Derivation
> The Minkowski square $P\cdot P$ is a Lorentz invariant. In the particle's rest frame, $P = (mc, 0, 0, 0)$, so $P\cdot P = (mc)^2 = m^2c^2$. In any other frame, $P = (E/c, \mathbf{p})$, so $P\cdot P = (E/c)^2 - \mathbf{p}^2 = E^2/c^2 - \mathbf{p}^2$. Equating the two values of the same invariant:
> $$\frac{E^2}{c^2} - \mathbf{p}^2 = m^2 c^2 \;\Longrightarrow\; \boxed{\ E^2 = \mathbf{p}^2 c^2 + m^2 c^4\ }.$$
> For a photon ($m=0$) this degenerates to $E = |\mathbf{p}|c$. In natural units ($c=1$), $E^2 = \mathbf{p}^2 + m^2$.

**Step 2: Newtonian limit of the energy.**

> [!note]- Derivation
> Expand the Lorentz factor for small $u/c$:
> $$\gamma = \Big(1 - \frac{u^2}{c^2}\Big)^{-1/2} = 1 + \frac12\frac{u^2}{c^2} + \frac38\frac{u^4}{c^4} + \cdots.$$
> Multiply by $mc^2$:
> $$E = \gamma mc^2 = mc^2 + \frac12 mu^2 + \frac38 m\frac{u^4}{c^2} + \cdots.$$
> The first term, $mc^2$, is the **rest energy** — present even at $u = 0$. The kinetic energy is the rest, $E_{\text{kin}} = E - mc^2 = \tfrac12 mu^2 + O(u^4/c^2)$, whose leading term is exactly the **Newtonian kinetic energy** $\tfrac12 mu^2$. So $E = mc^2 + \tfrac12 mu^2 + \cdots$: rest energy plus Newtonian kinetic energy plus relativistic corrections. As $u/c\to 0$, the corrections vanish and only $mc^2 + \tfrac12 mu^2$ survives.

**Step 3: The LHC proton.**

> [!note]- Derivation
> From $E = \gamma mc^2$, the Lorentz factor is
> $$\gamma = \frac{E}{mc^2} = \frac{7\ \text{TeV}}{0.938\ \text{GeV}} = \frac{7000\ \text{GeV}}{0.938\ \text{GeV}} \approx 7460 \approx 7.5\times10^3.$$
> The speed follows from $\gamma = (1-u^2/c^2)^{-1/2}$, so $u/c = \sqrt{1 - \gamma^{-2}}$. Since $\gamma$ is large, $\gamma^{-2} = (7.5\times10^3)^{-2} \approx 1.8\times10^{-8}$, and the *deficit* from $c$ is
> $$1 - \frac{u}{c} \approx \frac{1}{2\gamma^2} \approx \frac{1}{2(7.5\times10^3)^2} \approx 9\times10^{-9}.$$
> The proton moves at $c$ to within about one part in $10^8$ — about $3$ m/s slower than light.

**Step 4: The ultra-high-energy cosmic ray.**

> [!note]- Derivation
> $$\gamma = \frac{E}{mc^2} = \frac{10^{20}\ \text{eV}}{0.938\times10^9\ \text{eV}} \approx 1.07\times10^{11} \approx 10^{11}.$$
> The deficit from $c$ is
> $$1 - \frac{u}{c} \approx \frac{1}{2\gamma^2} \approx \frac{1}{2\times10^{22}} \approx 5\times10^{-23}.$$
> This proton is the fastest known massive particle relative to a terrestrial observer: its speed differs from $c$ by about $5$ parts in $10^{23}$. Its kinetic energy, $E_{\text{kin}} \approx E = 10^{20}$ eV $= 16$ J, equals that of a tennis ball served at $\sim 150$ km/h — concentrated in a single proton. (Such protons are at the GZK cutoff, where they lose energy to the cosmic microwave background; see [[Ex - Inverse Compton scattering and the GZK cutoff]].)

> [!note]- Complete formal solution
> **(1)** The invariant $P\cdot P = m^2c^2$ (rest frame) $= E^2/c^2 - \mathbf{p}^2$ (general frame) gives $E^2 = \mathbf{p}^2c^2 + m^2c^4$. **(2)** Expanding $\gamma = 1 + \tfrac12 u^2/c^2 + \cdots$, $E = \gamma mc^2 = mc^2 + \tfrac12 mu^2 + O(u^4/c^2)$: rest energy plus Newtonian kinetic energy. **(3)** For the LHC proton, $\gamma = E/mc^2 = 7000/0.938 \approx 7.5\times10^3$, and $1 - u/c \approx 1/2\gamma^2 \approx 9\times10^{-9}$. **(4)** For the cosmic ray, $\gamma = 10^{20}/(0.938\times10^9) \approx 10^{11}$, and $1 - u/c \approx 1/2\gamma^2 \approx 5\times10^{-23}$. $\blacksquare$

---

# Key Takeaways

**The energy–momentum relation is the squared mass-shell, derived in one line by frame-invariance.** The relation $E^2 = \mathbf{p}^2c^2 + m^2c^4$ is not memorised but *derived*: evaluate the invariant $P\cdot P$ in the rest frame (where it is $m^2c^2$, all energy) and in the moving frame (where it is $E^2/c^2 - \mathbf{p}^2$), and equate. This is the cleanest instance of the invariant-square technique, and the same move — compute an invariant where it is simple, equate to where the data are — recurs in every collision and threshold problem. The relation is the bridge between energy and momentum: given one, it yields the other, and at $m = 0$ it degenerates to the photon's $E = |\mathbf{p}|c$. The trigger is any problem mixing energy and momentum: write the mass-shell.

**The rest energy is the constant Newton discarded.** Expanding $E = \gamma mc^2 = mc^2 + \tfrac12 mu^2 + \cdots$ shows the relativistic energy contains a term $mc^2$ that is present even at rest — the rest energy — and a term $\tfrac12 mu^2$ that is the familiar Newtonian kinetic energy. Newtonian physics set the zero of energy at "particle at rest", discarding $mc^2$ as an irrelevant constant; relativity cannot, because the four-momentum is an absolute object whose time component at rest is $mc^2$. The reusable diagnostic: the *total* energy is $\gamma mc^2$ (use this in conservation laws), the *kinetic* energy is $(\gamma-1)mc^2$ (this reduces to Newton), and confusing $E = mc^2$ (at rest) with $E = \gamma mc^2$ (in motion) is the single most common error in the subject. The Newtonian kinetic energy $\tfrac12 mu^2$ is only the leading term and fails badly as $u\to c$.

**At large $\gamma$, compute the speed deficit, not the speed.** When $\gamma$ is enormous — $7500$ at the LHC, $10^{11}$ for a top cosmic ray — the speed $u$ is so close to $c$ that $u/c = \sqrt{1-\gamma^{-2}}$ rounds to $1$ on any calculator. The informative quantity is the *deficit* $1 - u/c \approx 1/(2\gamma^2)$, obtained by expanding the square root. This tells you the proton lags light by $\sim 3$ m/s at the LHC and by $\sim 5$ parts in $10^{23}$ for the cosmic ray. The trigger is any "how close to $c$?" question with large $\gamma$: do not compute $u$, compute $1 - u/c \approx 1/2\gamma^2$. This also makes vivid that energy, not speed, is the right variable at high $\gamma$ — the speed saturates at $c$ while the energy grows without bound, which is exactly why accelerators are rated by energy and why the speed limit is enforced by the divergence of $\gamma$ rather than any abrupt barrier.
