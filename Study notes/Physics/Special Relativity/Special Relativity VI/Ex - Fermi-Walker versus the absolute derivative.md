---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Fermi-Walker Derivative"
  - "Def - The Orthogonal Projector onto the Local Rest Space"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Local Frame and Four-Rotation"
tags: [physics, special-relativity]
---

# Problem Statement

Let $\mathcal{O}$ be an observer with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ ($U_0\cdot U_0 = +1$, $c = 1$), four-acceleration $A_0 = dU_0/d\tau$, and a vector field $V(\tau)$ along the worldline. The [[Def - Fermi-Walker Derivative|Fermi–Walker derivative]] is
$$
D^{\mathrm{FW}}_{U_0}V = \frac{dV}{d\tau} - \big[(U_0\cdot V)A_0 - (A_0\cdot V)U_0\big].
$$

1. Show that the **absolute derivative** $dV/d\tau$ of a vector $V\in U_0^\perp$ (in the rest space) generally has a nonzero component along $U_0$ — so it leaves the rest space.
2. Show that the **Fermi–Walker derivative** of $V\in U_0^\perp$ stays in the rest space, and in fact equals the [[Def - The Orthogonal Projector onto the Local Rest Space|orthogonal projection]] of the absolute derivative, $D^{\mathrm{FW}}_{U_0}V = \Pi(dV/d\tau)$.
3. Show that $D^{\mathrm{FW}}_{U_0}U_0 = 0$ identically — the Fermi–Walker derivative preserves the four-velocity.
4. Conclude in what precise senses the Fermi–Walker derivative is the "non-rotating" derivative, and why the absolute derivative is the wrong law for a gyroscope.

**Recall:**

![[Def - Fermi-Walker Derivative#The Definition]]

The [[Def - The Orthogonal Projector onto the Local Rest Space|orthogonal projector]] is $\Pi(X) = X - (X\cdot U_0)U_0$. The [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] satisfies $A_0\cdot U_0 = 0$ (from differentiating $U_0\cdot U_0 = +1$). A vector is in the [[Def - Observer and Local Rest Space|rest space]] $U_0^\perp$ iff $V\cdot U_0 = 0$.

---

# Convergent Strategy

**Problem class.** A *compare-two-derivatives* problem: distinguish the absolute and Fermi–Walker derivatives by their action on rest-space vectors and on $U_0$. The [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames#Problem-Solving Strategy|topic strategy]] for transport problems is to compute $dV/d\tau$ and then project / subtract the acceleration tilt.

**Assumption pattern.** The defining formulas for the two derivatives and the orthogonality $A_0\cdot U_0 = 0$ are the inputs. The key fact is that $dV/d\tau$ does not preserve $U_0^\perp$ (a spatial vector tilts out), while the Fermi–Walker derivative is precisely the correction that projects the tilt away. The signpost is "transport a vector along an accelerated worldline" — the gyroscope problem.

**Theorem routing.** Part 1: differentiate $U_0\cdot V = 0$ to get $U_0\cdot(dV/d\tau) = -A_0\cdot V$, nonzero in general. Part 2: substitute $V\in U_0^\perp$ into the Fermi–Walker formula and use $A_0\cdot V = -U_0\cdot(dV/d\tau)$ to recognise $\Pi(dV/d\tau)$. Part 3: substitute $V = U_0$ and use $dU_0/d\tau = A_0$, $A_0\cdot U_0 = 0$. Part 4 interprets.

**Key decision point.** The crux is the identity $A_0\cdot V = -U_0\cdot(dV/d\tau)$ for $V\in U_0^\perp$ (from differentiating $U_0\cdot V = 0$), which converts the Fermi–Walker correction term into exactly the $U_0$-component subtraction that defines the projector. Without this identity the equality $D^{\mathrm{FW}} = \Pi(d/d\tau)$ is opaque.

---

# Legal Operations Used

1. **Differentiate an orthonormality identity** (operation 7 from the topic page). Differentiating $U_0\cdot V = 0$ and $U_0\cdot U_0 = +1$ supplies the relations $A_0\cdot V = -U_0\cdot(dV/d\tau)$ and $A_0\cdot U_0 = 0$ used throughout.

2. **Project the absolute derivative to get the Fermi–Walker derivative** (operation 8 from the topic page). Part 2 is exactly this: $D^{\mathrm{FW}}_{U_0}V = \Pi(dV/d\tau)$ on the rest space.

3. **Project onto the local rest space** (operation 1 from the topic page). The projector $\Pi$ is what extracts the spatial part of the absolute derivative.

---

# Hints

> [!note]- Hint 1
> For $V\in U_0^\perp$, $U_0\cdot V = 0$ is constant along the worldline. Differentiate: $\frac{d}{d\tau}(U_0\cdot V) = A_0\cdot V + U_0\cdot\frac{dV}{d\tau} = 0$, so $U_0\cdot\frac{dV}{d\tau} = -A_0\cdot V$, generally nonzero.

> [!note]- Hint 2
> Substitute $V\in U_0^\perp$ (so $U_0\cdot V = 0$) into the Fermi–Walker formula: $D^{\mathrm{FW}}_{U_0}V = \frac{dV}{d\tau} + (A_0\cdot V)U_0$. Now replace $A_0\cdot V = -U_0\cdot\frac{dV}{d\tau}$ from Hint 1: $D^{\mathrm{FW}}_{U_0}V = \frac{dV}{d\tau} - (U_0\cdot\frac{dV}{d\tau})U_0 = \Pi(\frac{dV}{d\tau})$.

> [!note]- Hint 3
> Substitute $V = U_0$: $D^{\mathrm{FW}}_{U_0}U_0 = \frac{dU_0}{d\tau} - [(U_0\cdot U_0)A_0 - (A_0\cdot U_0)U_0]$. Use $dU_0/d\tau = A_0$, $U_0\cdot U_0 = +1$, $A_0\cdot U_0 = 0$.

> [!note]- Hint 4
> "Non-rotating" means: preserves the rest space (Part 2), preserves $U_0$ as the time axis (Part 3), and equals the minimal correction $\Pi(d/d\tau)$ that keeps spatial vectors spatial. The absolute derivative fails Part 3 ($dU_0/d\tau = A_0\neq 0$) and Part 1 (tilts spatial vectors out of the rest space).

---

# Solution

The exercise contrasts three lines of algebra. Step 1 differentiates the orthogonality $U_0\cdot V = 0$ to expose the tilt of the absolute derivative. Step 2 substitutes into the Fermi–Walker formula and recognises the projector. Step 3 checks $D^{\mathrm{FW}}_{U_0}U_0 = 0$. Step 4 reads off the senses of "non-rotating". The recurring move is differentiating a constant inner product.

**Step 1: The absolute derivative tilts a spatial vector out of the rest space.**

> [!note]- Derivation
> Let $V\in U_0^\perp$, so $U_0\cdot V = 0$ at every proper time. Differentiate this constant:
> $$0 = \frac{d}{d\tau}(U_0\cdot V) = \frac{dU_0}{d\tau}\cdot V + U_0\cdot\frac{dV}{d\tau} = A_0\cdot V + U_0\cdot\frac{dV}{d\tau},$$
> using $dU_0/d\tau = A_0$. Hence
> $$U_0\cdot\frac{dV}{d\tau} = -A_0\cdot V.$$
> This is the **$U_0$-component** of the absolute derivative, and it is generically **nonzero** — it vanishes only when $A_0\cdot V = 0$, i.e. when $V$ is orthogonal to the four-acceleration. So for a spatial vector $V$ with a component along $A_0$, the absolute derivative $dV/d\tau$ has a time component: it **leaves the rest space**. A gyroscope spin governed by $dV/d\tau = 0$ would thus appear to acquire a temporal part — a spurious "tilting out of space" caused by the time axis $U_0$ rotating, not by anything physically rotating the spin.

**Step 2: The Fermi–Walker derivative is the projected absolute derivative.**

> [!note]- Derivation
> For $V\in U_0^\perp$ (so $U_0\cdot V = 0$), the [[Def - Fermi-Walker Derivative|Fermi–Walker derivative]] reduces:
> $$D^{\mathrm{FW}}_{U_0}V = \frac{dV}{d\tau} - \big[(U_0\cdot V)A_0 - (A_0\cdot V)U_0\big] = \frac{dV}{d\tau} - \big[0\cdot A_0 - (A_0\cdot V)U_0\big] = \frac{dV}{d\tau} + (A_0\cdot V)U_0.$$
> Now substitute the identity from Step 1, $A_0\cdot V = -U_0\cdot\frac{dV}{d\tau}$:
> $$D^{\mathrm{FW}}_{U_0}V = \frac{dV}{d\tau} - \Big(U_0\cdot\frac{dV}{d\tau}\Big)U_0 = \Pi\!\left(\frac{dV}{d\tau}\right),$$
> the [[Def - The Orthogonal Projector onto the Local Rest Space|orthogonal projection]] of the absolute derivative onto the rest space. In particular $D^{\mathrm{FW}}_{U_0}V\in U_0^\perp$: the Fermi–Walker derivative of a rest-space vector **stays in the rest space**, exactly cancelling the tilt of Step 1. It is the minimal correction that keeps spatial vectors spatial — it subtracts precisely the offending $U_0$-component and nothing more.

**Step 3: The Fermi–Walker derivative preserves the four-velocity.**

> [!note]- Derivation
> Substitute $V = U_0$:
> $$D^{\mathrm{FW}}_{U_0}U_0 = \frac{dU_0}{d\tau} - \big[(U_0\cdot U_0)A_0 - (A_0\cdot U_0)U_0\big].$$
> Use $dU_0/d\tau = A_0$, $U_0\cdot U_0 = +1$, and $A_0\cdot U_0 = 0$:
> $$D^{\mathrm{FW}}_{U_0}U_0 = A_0 - \big[(+1)A_0 - 0\cdot U_0\big] = A_0 - A_0 = 0.$$
> So $D^{\mathrm{FW}}_{U_0}U_0 = 0$ **identically**: the four-velocity is Fermi–Walker transported into itself. This is exactly the property the absolute derivative *lacks* — $dU_0/d\tau = A_0\neq 0$ — and it is what makes the Fermi–Walker derivative keep $U_0$ as the time axis of a transported frame.

**Step 4: The senses of "non-rotating", and why the absolute derivative is wrong.**

> [!note]- Derivation
> The Fermi–Walker derivative is the **non-rotating** derivative in three precise senses, each a property just proved:
> - it **preserves the rest space** (Part 2): $V\in U_0^\perp\Rightarrow D^{\mathrm{FW}}_{U_0}V\in U_0^\perp$, so a "spatial" vector stays spatial — unlike the absolute derivative, which tilts it (Part 1);
> - it **preserves the four-velocity** (Part 3): $D^{\mathrm{FW}}_{U_0}U_0 = 0$, so the transported frame keeps $U_0$ as its time axis — unlike the absolute derivative, for which $dU_0/d\tau = A_0\neq 0$;
> - on the rest space it equals the **minimal correction** $\Pi(d/d\tau)$, the orthogonal projection of the absolute derivative — it removes exactly the unavoidable acceleration tilt and nothing more.
>
> The absolute derivative is the **wrong** law for a gyroscope precisely because it fails the first two: a torque-free gyroscope must keep its spin in the observer's instantaneous rest space and must not rotate the time axis, but $dV/d\tau = 0$ violates both. The Fermi–Walker derivative subtracts only the kinematically unavoidable tilt (the part forced by $A_0$), leaving any genuine rotation visible; setting it to zero is the correct relativistic statement of "carry this direction along without rotating it". (For an inertial observer, $A_0 = 0$, the tilt vanishes and the two derivatives coincide.)

> [!note]- Complete formal solution
> For $V\in U_0^\perp$, differentiating $U_0\cdot V = 0$ gives $U_0\cdot\frac{dV}{d\tau} = -A_0\cdot V$, generally nonzero, so the absolute derivative leaves the rest space. The Fermi–Walker derivative of such $V$ is $\frac{dV}{d\tau} + (A_0\cdot V)U_0 = \frac{dV}{d\tau} - (U_0\cdot\frac{dV}{d\tau})U_0 = \Pi(\frac{dV}{d\tau})$, which lies in $U_0^\perp$. For $V = U_0$: $D^{\mathrm{FW}}_{U_0}U_0 = A_0 - [(+1)A_0 - 0] = 0$. Hence the Fermi–Walker derivative preserves the rest space and the four-velocity and equals the projected absolute derivative — the three senses of "non-rotating" — while the absolute derivative fails both (it tilts spatial vectors and rotates the time axis), making it the wrong gyroscope law. $\blacksquare$

---

# Key Takeaways

**The absolute derivative tilts spatial vectors out of the rest space because the time axis itself is rotating.** The core computation — differentiate $U_0\cdot V = 0$ to get $U_0\cdot(dV/d\tau) = -A_0\cdot V$ — reveals that a vector lying purely in the observer's space acquires a *time* component under the plain proper-time derivative, whenever it has a component along the four-acceleration. This tilt is not a physical rotation of $V$; it is an artifact of the rest space itself tilting as $U_0$ rotates. The transferable insight: in any accelerated frame, the naive derivative $d/d\tau$ mixes "the quantity changed" with "the frame changed", and the contamination is proportional to the acceleration. This is the relativistic analogue of the classical fact that $d/dt$ in a rotating frame produces fictitious Coriolis and centrifugal terms — the frame's own motion leaks into the derivative, and one must correct for it to extract the physical rate of change.

**The Fermi–Walker derivative is the orthogonal projection of the absolute derivative — the minimal correction that keeps space spatial.** The clean identity $D^{\mathrm{FW}}_{U_0}V = \Pi(dV/d\tau)$ (on the rest space) says the Fermi–Walker derivative subtracts *exactly* the spurious $U_0$-component and nothing more. It is the smallest possible modification of the absolute derivative that maps the rest space to itself, which is why it, and not some other correction, is the canonical non-rotating transport. The diagnostic to carry forward: when you need a derivative along an accelerated worldline that respects the observer's space, project the absolute derivative onto the rest space; the result is automatically the Fermi–Walker derivative, and it is the unique projection-respecting connection. This is also why Fermi–Walker transport preserves lengths and angles (it is metric) and keeps $U_0$ as the time axis — projecting cannot create or destroy norm in the orthogonal directions.

**"Non-rotating" means preserves the rest space and preserves the four-velocity, and only the Fermi–Walker derivative does both.** The three senses established here — stays in the rest space, kills the derivative of $U_0$, equals the projected absolute derivative — together pin down the Fermi–Walker derivative as *the* relativistic non-rotating transport, the law a torque-free gyroscope obeys. The absolute derivative fails decisively: $dV/d\tau = 0$ neither keeps the spin spatial nor keeps $U_0$ fixed, so it describes neither a gyroscope nor a sensible frame. The reusable principle for problem-solving: to transport a direction along a worldline "without rotating it" — a gyroscope axis, a spin vector, a non-rotating frame — never use the absolute derivative; use the Fermi–Walker derivative, set it to zero, and remember that the residual rotation it predicts on a closed accelerated path (which the absolute derivative would miss entirely) is the physically real Thomas precession. The distinction between these derivatives is not pedantry; it is the difference between predicting and missing a measurable rotation.
