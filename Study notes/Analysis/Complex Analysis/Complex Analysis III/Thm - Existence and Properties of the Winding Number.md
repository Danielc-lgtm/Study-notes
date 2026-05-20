---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Winding Number"
  - "Def - Curve and C1 Curve"
tags: [analysis, complex-analysis, topology]
---

# Notation

$\gamma : [a, b] \to \mathbb{C}$ is a closed continuous curve; $w \in \mathbb{C}$ is a point not on $\gamma^*$. $I(\gamma; w)$ is the winding number. We sometimes write $\tilde\gamma$ for a continuous lift of $\gamma - w$ under the exponential. Full registry on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Motivation

The winding number was *defined* topologically (continuous lift of the angle) and computationally (integral formula). Two key questions remain: does the topological definition actually make sense (does a continuous lift always exist), and do the two definitions agree? Beyond these foundational questions, the theorem gathers the basic properties that make the winding number a useful invariant — integer-valued, locally constant in $w$, zero in the unbounded component, additive under concatenation, sign-reversed under reversal, and homotopy-invariant.

These properties are the operational substance of the winding number. Without them, the definition would be useless. With them, the winding number becomes the topological backbone of complex contour integration: every theorem about contour integrals near singularities will track how the contour winds around the singularities, and how those winding numbers respond to deformation, concatenation, and parameter changes.

---

# Sources and Targets

**Sources (Input Broadening)**

The "input type" of the existence theorem is just continuity of $\gamma$ on a closed interval. The sources we want to broaden are situations where we want to apply winding-number arguments.

The first disguised source is **any closed curve with a parametrization, however ugly.** Property $B$: $\gamma$ is any closed continuous curve. The bridge: continuity is the only hypothesis; the topology of $\mathbb{C} \setminus \{w\}$ is rich enough that continuous lifts always exist. Example: in arguments showing a continuous map from a disc to the plane has a fixed point, the boundary curve might have a wild parametrization, but the winding-number argument still applies.

The second disguised source is **a homotopy through closed curves.** Property $B$: a one-parameter family $\gamma_t$ of closed curves, all avoiding $w$. The bridge: the winding number is locally constant in $t$, by continuity of the integral formula or by joint continuity of the lift. So the winding number is *homotopy-invariant*, and one can compute it for one curve in the family and deduce it for all. Example: in Rouché's theorem, the homotopy $\gamma_t = (1-t)f + tg$ has constant winding number around $0$ provided $\gamma_t$ never reaches $0$.

The third disguised source is **a curve viewed as a sum of simpler curves.** Property $B$: $\gamma$ is a concatenation $\gamma_1 \cdot \gamma_2 \cdots \gamma_n$ of simpler loops. The bridge: by additivity, $I(\gamma; w) = \sum I(\gamma_i; w)$. So a complicated curve's winding number reduces to a sum of winding numbers of simpler pieces.

**Targets (Output Amplification)**

The conclusion is "the winding number is well-defined and has these properties". The targets are everything one can do with the winding number.

Combine integer-valuedness with **continuity of $I(\gamma; \cdot)$ on $\mathbb{C} \setminus \gamma^*$.** Property $D$: $I(\gamma; w)$ varies continuously with $w$ off $\gamma$. Amplified result $E$: $I(\gamma; w)$ is *locally constant* — constant on each connected component of $\mathbb{C} \setminus \gamma^*$. This is what licenses the "winding number is determined by which connected component $w$ is in" intuition.

Combine zero-on-unbounded-component with **integer-valuedness.** Property $D$: in the unbounded component, $I(\gamma; w)$ is an integer and tends to $0$ as $|w| \to \infty$. Amplified result $E$: the winding number is identically zero on the unbounded component. So in particular, every closed curve has at most finitely many components on which the winding number is nonzero, and they are all bounded.

Combine homotopy invariance with **the structure of $\pi_1(\mathbb{C}^\times) = \mathbb{Z}$.** Property $D$: the fundamental group of the punctured plane is $\mathbb{Z}$. Amplified result $E$: the winding number is a *complete* invariant of closed curves in $\mathbb{C}^\times$ up to homotopy — two closed curves are homotopic in $\mathbb{C}^\times$ iff they have the same winding number. So the winding number realizes the isomorphism $\pi_1(\mathbb{C}^\times) \cong \mathbb{Z}$.

---

# Why Is It True

The existence of a continuous lift is a purely local-to-global argument. Locally, on any open set where $\gamma - w$ stays in a half-plane (the half-plane through the origin perpendicular to its "midpoint" direction), the principal branch of the argument is continuous and provides a continuous lift on that piece. By uniform continuity of $\gamma$, the interval $[a, b]$ can be partitioned into finitely many pieces, each of which maps into such a half-plane. Local lifts on each piece exist, and the lifts can be glued by adjusting integer multiples of $2\pi$ so that they agree at endpoints. The result is a continuous lift on the whole interval.

The integer-valuedness comes from the closed-curve condition. Since $\gamma(a) = \gamma(b)$, the lift $\tilde\gamma(a)$ and $\tilde\gamma(b)$ satisfy $e^{i\tilde\gamma(a)} = e^{i\tilde\gamma(b)}$, so their difference is an integer multiple of $2\pi$.

The agreement with the integral formula comes from $\frac{dz}{z - w} = d[\log(z - w)]$, where $\log(z - w) = \log|z - w| + i\arg(z - w)$. As $z$ traces $\gamma$, the real part $\log|z - w|$ returns to its starting value (closed curve), so contributes zero. The imaginary part $\arg(z - w) = \theta(t)$ changes by $\theta(b) - \theta(a) = 2\pi I(\gamma; w)$. Putting these together, $\int_\gamma dz/(z - w) = 2\pi i I(\gamma; w)$, so $I(\gamma; w) = (2\pi i)^{-1}\int_\gamma dz/(z - w)$.

Local constancy in $w$ follows from differentiation under the integral sign: the integral $\int_\gamma dz/(z - w)$ depends holomorphically on $w$ off $\gamma$, hence continuously. A continuous integer-valued function is locally constant.

Vanishing in the unbounded component: for $|w|$ very large, $|z - w| \geq |w| - \max|z|$ on the contour, so $|1/(z - w)| \leq 1/(|w| - \max|z|)$, and the ML estimate gives $|\int_\gamma dz/(z - w)| \leq \text{length}(\gamma)/(|w| - \max|z|) \to 0$ as $|w| \to \infty$. Continuous, integer-valued, vanishing at infinity: zero on the unbounded component.

Concatenation and reversal: immediate from additivity of integration over concatenated paths and sign-flipping under reversal.

Homotopy invariance: if $\gamma_t$ is a homotopy, the integral $\int_{\gamma_t} dz/(z - w)$ depends continuously on $t$ (joint continuity of the integrand and uniform compactness of the parameter domain), and is integer-valued, hence locally constant in $t$. Connectedness of $[0, 1]$ then forces it to be globally constant.

---

# What Makes This Hard

The non-obvious step is the **existence of a continuous lift** — the topological definition seems to assume what it sets out to define. The trick is the *partition-and-glue* argument: split the interval into pieces small enough that $\gamma$ stays in a half-plane on each piece, define the lift locally on each piece using the principal argument, and adjust by integer multiples of $2\pi$ at gluing points to make the lifts continuous. The common error is to try a single global formula for the lift; this fails because the argument $\arg$ has no single-valued continuous branch on all of $\mathbb{C}^\times$. A second frequent slip is to forget that the integral formula gives a *complex* number that needs to be checked to be a real integer; this requires the explicit calculation $\int = 2\pi i \cdot (\text{change in argument})$, separating real and imaginary parts.

---

# Rederivation Scaffold

**High-level strategy:**
Existence of the lift by partition into half-plane pieces and integer-shift gluing. Agreement of integral and topological formulas by recognizing the integrand as the derivative of $\log(z - w)$ on each piece. The remaining properties follow from properties of the integral formula (continuity in $w$, additivity, decay at infinity) combined with integer-valuedness.

**Subgoal decomposition:**

1. **Existence of a continuous lift.** Show that a continuous $\theta : [a, b] \to \mathbb{R}$ with $\gamma(t) - w = |\gamma(t) - w| e^{i\theta(t)}$ exists.
   - *Hint:* Partition $[a, b]$ so $\gamma$ stays in a half-plane on each subinterval; use the principal argument on each half-plane; glue by adding $2\pi k$.
   - *Why needed:* Without this, the topological definition is vacuous.

2. **Integer-valuedness.** Show $\theta(b) - \theta(a) \in 2\pi\mathbb{Z}$.
   - *Hint:* $e^{i\theta(b)} = e^{i\theta(a)}$ because $\gamma(b) = \gamma(a)$.
   - *Why needed:* Without this, the "winding number" would not be a meaningful integer count.

3. **Agreement with the integral formula (for piecewise $C^1$ curves).** Show $\int_\gamma dz/(z - w) = i(\theta(b) - \theta(a)) = 2\pi i \cdot I(\gamma; w)$.
   - *Hint:* Parametrize, compute $\gamma'/(\gamma - w) = (\log r)' + i\theta'$; integrate.
   - *Why needed:* The integral formula is what makes the winding number computable.

4. **Locally constant in $w$.** Show $I(\gamma; w)$ is locally constant on $\mathbb{C} \setminus \gamma^*$.
   - *Hint:* The integral formula gives continuity in $w$; integer-valued + continuous = locally constant.
   - *Why needed:* Justifies "winding number depends only on the connected component of $w$".

5. **Zero on the unbounded component.** Show $I(\gamma; w) = 0$ for $|w|$ sufficiently large.
   - *Hint:* ML estimate on the integral formula.
   - *Why needed:* Establishes that the winding number is supported in the bounded components.

6. **Concatenation and reversal.** Show $I(\gamma_1 \cdot \gamma_2; w) = I(\gamma_1; w) + I(\gamma_2; w)$ and $I(\gamma^{-1}; w) = -I(\gamma; w)$.
   - *Hint:* Additivity of integration over concatenated paths; orientation-reversal flips sign.

---

# Lemma Decomposition

> [!note]- Lemma 1: A curve in a half-plane through the origin has a continuous argument
> **Statement:** If $\gamma : [a, b] \to \mathbb{C} \setminus \{0\}$ has image in the open half-plane $\{z : \operatorname{Re}(e^{-i\alpha} z) > 0\}$ for some $\alpha$, then there is a continuous $\theta : [a, b] \to \mathbb{R}$ with $\gamma(t) = |\gamma(t)| e^{i\theta(t)}$, where $\theta(t) - \alpha \in (-\pi/2, \pi/2)$.
>
> **Hint:** The principal argument $\arg z = \operatorname{Im}\log z$ (with the branch cut along the negative real axis after rotation by $e^{-i\alpha}$) is continuous on this half-plane.
>
> **Why needed:** Provides the local lifts to be glued in Lemma 2.
>
> > [!note]- Full proof
> > After rotating coordinates by $e^{-i\alpha}$, the half-plane becomes $\{z : \operatorname{Re} z > 0\}$. On this half-plane, $\arg z = \arctan(\operatorname{Im} z/\operatorname{Re} z) \in (-\pi/2, \pi/2)$ is a continuous function (composition of continuous functions, denominator nonzero). The function $\theta(t) = \alpha + \arg(e^{-i\alpha}\gamma(t))$ is then continuous on $[a, b]$ and satisfies the required equation.

> [!note]- Lemma 2: A continuous lift of a closed curve exists
> **Statement:** Let $\gamma : [a, b] \to \mathbb{C} \setminus \{w\}$ be continuous. Then there is a continuous $\theta : [a, b] \to \mathbb{R}$ with $\gamma(t) = w + |\gamma(t) - w| e^{i\theta(t)}$.
>
> **Hint:** Partition $[a, b]$ finely enough that $\gamma$ stays in a half-plane through $w$ on each piece; define lifts locally; glue by integer shifts.
>
> > [!note]- Full proof
> > After translating so $w = 0$ and replacing $\gamma$ by $\gamma/|\gamma|$, assume $|\gamma(t)| = 1$. By uniform continuity, there exists $\epsilon > 0$ such that $|s - t| < \epsilon$ implies $|\gamma(s) - \gamma(t)| < \sqrt{2}$. Partition $a = a_0 < a_1 < \ldots < a_N = b$ with $a_k - a_{k-1} < \epsilon$. On each $[a_{k-1}, a_k]$, $\gamma$ stays within distance $\sqrt{2}$ of $\gamma(\tfrac{a_{k-1} + a_k}{2})$, hence lies in a (rotated) half-plane through $0$. By Lemma 1, a continuous $\theta_k : [a_{k-1}, a_k] \to \mathbb{R}$ exists. At each gluing point $a_k$, $\theta_{k+1}(a_k) - \theta_k(a_k) \in 2\pi\mathbb{Z}$; adjust $\theta_{k+1}$ by adding $2\pi B_{k+1}$ for the integer $B_{k+1}$ making them agree. The glued function $\theta$ is continuous on $[a, b]$.

> [!note]- Lemma 3: For piecewise $C^1$ $\gamma$, the integral formula agrees with the topological definition
> **Statement:** If $\gamma$ is piecewise $C^1$ and $w \notin \gamma^*$, then $\frac{1}{2\pi i}\int_\gamma \frac{dz}{z - w} = I(\gamma; w)$.
>
> **Hint:** Write $\gamma(t) = w + r(t) e^{i\theta(t)}$ with $r, \theta$ piecewise $C^1$; compute the integrand and integrate.
>
> > [!note]- Full proof
> > Write $\gamma(t) = w + r(t) e^{i\theta(t)}$ with $r, \theta$ piecewise $C^1$ (the lift from Lemma 2 is piecewise $C^1$ because the local principal arguments are). Then
> > $$\frac{\gamma'(t)}{\gamma(t) - w} = \frac{r'(t)e^{i\theta(t)} + r(t)i\theta'(t)e^{i\theta(t)}}{r(t)e^{i\theta(t)}} = \frac{r'(t)}{r(t)} + i\theta'(t).$$
> > Integrating:
> > $$\int_a^b \frac{\gamma'(t)}{\gamma(t) - w}\,dt = \int_a^b \frac{r'(t)}{r(t)}\,dt + i\int_a^b \theta'(t)\,dt = [\log r(t)]_a^b + i[\theta(t)]_a^b.$$
> > The first bracket is zero (closed curve, $r(a) = r(b)$); the second is $i(\theta(b) - \theta(a)) = 2\pi i \cdot I(\gamma; w)$.

---

# Formal Proof

> [!note]- Complete formal proof
> Combining Lemmas 1, 2, 3 establishes existence of the lift and agreement of the integral formula with the topological definition.
>
> **Integer-valuedness.** Since $\gamma(b) = \gamma(a)$, $e^{i\theta(b)} = e^{i\theta(a)}$, so $\theta(b) - \theta(a) \in 2\pi\mathbb{Z}$.
>
> **Independence of the lift.** Two continuous lifts $\theta_1, \theta_2$ have $e^{i(\theta_1 - \theta_2)} = 1$, so $\theta_1 - \theta_2$ is continuous integer-valued (times $2\pi$), hence constant. So $\theta_1(b) - \theta_1(a) = \theta_2(b) - \theta_2(a)$.
>
> **Locally constant in $w$.** The integral $w \mapsto \int_\gamma dz/(z - w)$ is holomorphic on $\mathbb{C} \setminus \gamma^*$ (differentiation under the integral sign is legal because the integrand is jointly continuous on a compact set), hence continuous in $w$. The winding number is integer-valued and continuous in $w$, so locally constant.
>
> **Zero on the unbounded component.** For $|w| > \sup_t |\gamma(t)| + 1$, the ML estimate gives
> $$\left|\int_\gamma \frac{dz}{z - w}\right| \leq \frac{\text{length}(\gamma)}{|w| - \sup|\gamma|} \to 0 \quad \text{as } |w| \to \infty.$$
> Continuous + integer-valued + decaying to $0$: the function is zero for $|w|$ large, and locally constant; the unbounded component contains $\{|w|$ large$\}$, so the function is zero throughout it.
>
> **Concatenation.** $\int_{\gamma_1 \cdot \gamma_2} = \int_{\gamma_1} + \int_{\gamma_2}$ by definition of concatenated integrals; divide by $2\pi i$.
>
> **Reversal.** $\int_{\gamma^{-1}} = -\int_\gamma$ by reversing the parametrization; divide.
>
> **Homotopy invariance.** Let $H : [a, b] \times [0, 1] \to \mathbb{C} \setminus \{w\}$ be a continuous homotopy of closed curves $\gamma_s = H(\cdot, s)$. The function $s \mapsto \int_{\gamma_s} dz/(z - w)$ is continuous (joint continuity + compactness), and integer-valued (each $\gamma_s$ is closed), hence constant on the connected interval $[0, 1]$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Brouwer fixed point in 2D.** The continuous map $f : \overline{\mathbb{D}} \to \overline{\mathbb{D}}$ has a fixed point. The proof: if not, the map $g(z) = (z - f(z))/|z - f(z)|$ retracts $\overline{\mathbb{D}}$ onto $S^1$. On the boundary, $g$ has winding number $1$ (by a homotopy from $g|_{S^1}$ to the identity), but on a contracting disc of radius $r \to 0$, the winding number must be $0$ — contradiction. The winding number is the obstruction.

**Argument principle.** The argument principle ($\frac{1}{2\pi i}\oint f'/f\,dz = N - P$) is "the winding number of $f \circ \gamma$ around $0$ counts zeros minus poles enclosed." This is a direct application: $f'/f\,dz = d\log f$, so its integral around $\gamma$ is the change in $\arg f$, which is $2\pi$ times the winding number of $f \circ \gamma$.

**Topological degree in higher dimensions.** The winding number generalizes to the **Brouwer degree** of a map $S^n \to S^n$: an integer counting how many times the image wraps around. Many fixed-point theorems and existence results for nonlinear PDEs use the degree, and the construction generalizes the lift-and-count argument from §3.1.

---

# Bridges

- **[[Def - Winding Number]]** — the definition the theorem makes rigorous.

- **[[Thm - Cauchy's Theorem for Simply Connected Domains]]** — winding number zero around the complement is exactly the simple-connectedness hypothesis.

- **[[Thm - Residue Theorem]]** — the master theorem of contour integration uses winding numbers as the topological weights on residues.

- **[[Thm - Argument Principle]]** — winding number of $f \circ \gamma$ around $0$ counts zeros and poles.

---

# Unlocked by This

> [!tip] Homotopy and the Fundamental Group *(from Topology)*
> The winding number realizes the isomorphism $\pi_1(\mathbb{C}^\times) \cong \mathbb{Z}$. See [[Topology IV — §13–17 Quotients, Homotopy, Topological Groups, Baire|Topology IV]] for the general framework of covering spaces and lifts.
