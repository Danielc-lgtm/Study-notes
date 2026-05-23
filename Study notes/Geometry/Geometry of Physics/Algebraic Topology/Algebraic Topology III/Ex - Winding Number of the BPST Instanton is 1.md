---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Second Chern Class"
  - "Thm - Chern-Weil Theorem (Statement)"
  - "Thm - Chern Forms are Closed and Their Cohomology Class is Independent of Connection"
tags: [geometry, algebraic-topology, characteristic-classes, gauge-theory, yang-mills]
---

# Problem Statement

The **BPST instanton** is the $SU(2)$ Yang–Mills connection on $\mathbb{R}^4$ given (after choosing scale $\rho$ centred at the origin) by

$$A_\mu(x) = -i\frac{\sigma_{\mu\nu} x^\nu}{|x|^2 + \rho^2},$$

where $\sigma_{\mu\nu}$ are anti-Hermitian $\mathfrak{su}(2)$-matrices encoded by 't Hooft symbols (we will use the simpler gauge transformation description below). Equivalently, the BPST instanton is *pure gauge at infinity*: there is a gauge transformation $g : S^3_\infty \to SU(2) = S^3$ such that $A \to g^{-1}\,dg$ as $|x| \to \infty$.

Compute the **instanton number**:
$$k = \int_{\mathbb{R}^4} c_2(F) = -\frac{1}{8\pi^2}\int_{\mathbb{R}^4} \mathrm{Tr}(F \wedge F),$$
and show that for the standard BPST instanton with $g(x) = (x^4 \mathbf{1} + i\vec{x}\cdot\vec\sigma)/|x|$ at infinity, $k = 1$.

Use **Frankel's identity (22.5)**: for an $SU(n)$ connection with curvature vanishing outside a region bounded by $S^3$,
$$\int_{R^4} \mathrm{Tr}(F \wedge F) = \frac{1}{3}\int_{S^3} \mathrm{Tr}(g^{-1}dg \wedge g^{-1}dg \wedge g^{-1}dg),$$
so $\int c_2 = \frac{1}{24\pi^2}\int_{S^3} \mathrm{Tr}(g^{-1}dg)^{\wedge 3}$ = (winding number of $g : S^3 \to SU(2)$).

**Recall:**

![[Def - Second Chern Class#The Definition]]

For an $SU(n)$ bundle, $c_2(F) = -\frac{1}{8\pi^2}\mathrm{Tr}(F \wedge F)$.

The **gauge transformation at infinity** is the map $g : S^3_\infty \to SU(n)$ such that the connection $A$ asymptotes to $g^{-1}dg$ (pure gauge). The instanton number is the degree of $g$ as a map between 3-spheres, equivalently the winding number in $\pi_3(SU(n)) = \mathbb{Z}$.

The **Cartan 3-form** on a Lie group $G$ is $\Omega_3 = \mathrm{Tr}(g^{-1}dg \wedge g^{-1}dg \wedge g^{-1}dg)$. For $G = SU(2) = S^3$, $\int_{SU(2)} \Omega_3 = 24\pi^2$ (the bi-invariant volume of $SU(2)$, computed in Frankel (22.2)).

---

# Convergent Strategy

**Problem class.** This is a **compute an instanton number / topological charge** problem — the prototypical application of $c_2$ in gauge theory. The strategy uses Frankel's identity to reduce a bulk integral (over $\mathbb{R}^4$) to a boundary integral (over $S^3_\infty$), and then interprets the boundary integral as the degree of a gauge transformation.

**Assumption pattern.** The hypotheses are: (i) the BPST instanton has finite action, hence the curvature decays at infinity, so the connection asymptotes to pure gauge $g^{-1}dg$; (ii) the gauge transformation $g$ extends from $S^3_\infty$ to a smooth map to $SU(2) = S^3$. The integral $\int c_2$ is well-defined because the curvature has compact support effectively (decays sufficiently fast), and the topological invariant is the degree of $g$.

**Theorem routing.** The route is:
1. Use [[Thm - Chern Forms are Closed and Their Cohomology Class is Independent of Connection|Chern form closedness]] and [[Def - Chern Forms of a U(n) Bundle|the formula $c_2 = -(1/8\pi^2)\mathrm{Tr}(F \wedge F)$]] for $SU(2)$.
2. Apply Frankel (22.4): $\mathrm{Tr}(F \wedge F) = d\,\mathrm{CS}_3$ locally, so Stokes converts the bulk integral to a boundary integral over $S^3_\infty$.
3. On $S^3_\infty$, the connection is pure gauge $A = g^{-1}dg$, so $\mathrm{CS}_3 = \mathrm{Tr}(\tfrac{2}{3}(g^{-1}dg)^3) = \tfrac{2}{3}\Omega_3$ (other terms vanish for pure gauge).
4. The integral $\int_{S^3_\infty}\Omega_3 =$ degree of $g$ times the volume of $SU(2)$, i.e., $24\pi^2 \cdot \deg(g)$.
5. Putting it together: $\int c_2 = \deg(g) = 1$ for the standard BPST $g$.

**Key decision point.** The crucial move is *recognising that the bulk integral reduces to a boundary integral* via Stokes + the Chern–Simons identity. This is the *physical content* of the topological charge: the integer measuring the bundle's twist at infinity, not a property of the bulk field. The same integer would arise for *any* gauge transformation $g : S^3 \to SU(2)$ of the same degree — the BPST instanton is just one (action-minimising) representative of its topological sector.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Algebraic Topology III — Higher Homotopy and Chern Forms#Legal Operations|the topic page's Legal Operations]]:

1. **Compute Chern forms from curvature in a chosen frame** (operation 5). The BPST instanton's curvature is computed asymptotically.

2. **Integrate Chern forms over cycles to get integers** (operation 6). The integration over $\mathbb{R}^4$ (or $S^4$ via compactification) gives the integer.

3. **Recognise a Chern number as a degree** (operation 9). The instanton number is the degree of the gauge transformation at infinity.

4. **Chern–Simons transgression** (operation 11). The reduction from bulk $\mathrm{Tr}(F \wedge F)$ to boundary $\mathrm{CS}_3$ via $d\mathrm{CS}_3 = \mathrm{Tr}(F \wedge F)$.

---

# Hints

> [!note]- Hint 1
> The integral $\int_{\mathbb{R}^4}\mathrm{Tr}(F \wedge F)$ does not look like an integer at first sight. What identity reduces it to a boundary integral?

> [!note]- Hint 2
> Frankel's identity (22.4): $\mathrm{Tr}(F \wedge F) = d\mathrm{CS}_3$ where $\mathrm{CS}_3 = \mathrm{Tr}(A \wedge dA + \tfrac{2}{3}A \wedge A \wedge A)$ is the Chern–Simons 3-form. By Stokes:
> $$\int_{\mathbb{R}^4}\mathrm{Tr}(F \wedge F) = \int_{S^3_\infty}\mathrm{CS}_3.$$

> [!note]- Hint 3
> On $S^3_\infty$, $A = g^{-1}dg$ (pure gauge). For pure gauge, $F = 0$ and $A \wedge A \wedge A = (g^{-1}dg)^3$. The Chern–Simons form simplifies: $\mathrm{CS}_3 = \tfrac{2}{3}\mathrm{Tr}((g^{-1}dg)^3) = \tfrac{2}{3}\Omega_3$.

> [!note]- Hint 4
> So $\int_{\mathbb{R}^4}\mathrm{Tr}(F \wedge F) = \tfrac{2}{3}\int_{S^3_\infty}\Omega_3$, and the integral of the Cartan 3-form over $S^3 = SU(2)$ is $24\pi^2$ times the degree of $g$. Combining gives $\int c_2 = -\frac{1}{8\pi^2}\cdot\tfrac{2}{3}\cdot 24\pi^2\cdot\deg(g) = -2\deg(g)$... wait, let me recompute the prefactors.

> [!note]- Hint 5
> Actually the formula in Frankel (22.5) is $\int_{R^4}\mathrm{Tr}(F\wedge F) = -\frac{1}{3}\int_{S^3}\mathrm{Tr}((g^{-1}dg)^3)$ (with the boundary $S^3$ oriented as outward boundary, hence the minus sign). Then $\int c_2 = -\frac{1}{8\pi^2}\cdot(-\frac{1}{3})\int_{S^3}\Omega_3 = \frac{1}{24\pi^2}\int_{S^3}\Omega_3 = \deg(g)$. For BPST with $g$ the identity $S^3 \to S^3$, $\deg = 1$.

---

# Solution

The proof has four steps: identify the integrand, apply Stokes via Chern–Simons, evaluate the boundary integral as a degree, and verify $\deg(g) = 1$ for the BPST gauge transformation.

**Plan paragraph:** the proof breaks into (1) write $c_2 = -(1/8\pi^2)\mathrm{Tr}(F\wedge F)$ for the $SU(2)$ bundle; (2) use Frankel's identity to reduce the bulk integral to a boundary $S^3_\infty$ via Stokes; (3) simplify the Chern–Simons form on pure gauge and integrate over $S^3$; (4) recognise the result as the degree of the gauge transformation $g : S^3 \to SU(2)$. The non-obvious move is in step 4: $g(x) = (x^4 + i\vec x \cdot \vec\sigma)/|x|$ on $S^3_\infty$ is precisely the identity map under the standard identification $SU(2) = S^3$, hence has degree 1.

**Step 1: $c_2 = -(1/8\pi^2)\mathrm{Tr}(F\wedge F)$ for $SU(2)$.**

For an $SU(n)$ bundle, $\mathrm{Tr}(F) = 0$ (since $\mathfrak{su}(n)$ is traceless), so the [[Def - Second Chern Class|second Chern form]] simplifies to
$$c_2(F) = -\frac{1}{8\pi^2}\mathrm{Tr}(F \wedge F).$$
For our $SU(2)$ bundle, this is the integrand of interest.

**Step 2: Reduce to boundary via Chern–Simons.**

By Frankel's (22.4) — equivalently, [[Thm - Chern Forms are Closed and Their Cohomology Class is Independent of Connection|the Chern–Simons transgression]] — the form $\mathrm{Tr}(F \wedge F)$ is locally exact:
$$\mathrm{Tr}(F \wedge F) = d\,\mathrm{CS}_3, \qquad \mathrm{CS}_3 = \mathrm{Tr}\!\left(A \wedge dA + \tfrac{2}{3}A \wedge A \wedge A\right).$$

> [!note]- Derivation
> The identity is verified directly:
> $$d\,\mathrm{CS}_3 = d\,\mathrm{Tr}(A \wedge dA) + \tfrac{2}{3}\,d\,\mathrm{Tr}(A^{\wedge 3}).$$
>
> Compute: $d(A \wedge dA) = dA \wedge dA = (F - A\wedge A)\wedge(F - A\wedge A) = F\wedge F - F\wedge A\wedge A - A\wedge A\wedge F + (A\wedge A)^{\wedge 2}$.
>
> Taking trace: $\mathrm{Tr}(A\wedge A\wedge A\wedge A) = 0$ (Frankel (21.3) — trace of a $\wedge^4$ vanishes for Lie-algebra-valued 1-forms). So $\mathrm{Tr}(d(A\wedge dA)) = \mathrm{Tr}(F\wedge F) - 2\mathrm{Tr}(F\wedge A\wedge A)$.
>
> Compute: $d(A^{\wedge 3}) = dA\wedge A\wedge A - A\wedge dA\wedge A + A\wedge A\wedge dA = (F-A\wedge A)\wedge A\wedge A - A\wedge(F-A\wedge A)\wedge A + A\wedge A\wedge(F-A\wedge A)$.
>
> Taking trace (using cyclicity and the vanishing of $\mathrm{Tr}((A\wedge A)^2)$): $\mathrm{Tr}(d(A^{\wedge 3})) = 3\mathrm{Tr}(F\wedge A\wedge A)$.
>
> Putting together: $d\mathrm{CS}_3 = \mathrm{Tr}(F\wedge F) - 2\mathrm{Tr}(F\wedge A\wedge A) + \tfrac{2}{3}\cdot 3\mathrm{Tr}(F\wedge A\wedge A) = \mathrm{Tr}(F\wedge F)$.
>
> So $\mathrm{Tr}(F\wedge F) = d\mathrm{CS}_3$ locally. The Chern–Simons form $\mathrm{CS}_3$ is not globally defined when the bundle is non-trivial, but the difference $\int_{\partial\Omega} \mathrm{CS}_3$ is independent of the trivialisation modulo $24\pi^2 \mathbb{Z}$.
>
> By Stokes:
> $$\int_{\mathbb{R}^4} \mathrm{Tr}(F\wedge F) = \int_{S^3_\infty} \mathrm{CS}_3.$$

**Step 3: Pure gauge at infinity simplifies $\mathrm{CS}_3$ to the Cartan 3-form.**

On $S^3_\infty$, $A = g^{-1}dg$ for some $g : S^3_\infty \to SU(2)$. For pure gauge, $F = dA + A\wedge A = 0$. Substituting:

$$\mathrm{CS}_3\big|_{S^3_\infty} = \mathrm{Tr}\!\left(g^{-1}dg \wedge d(g^{-1}dg) + \tfrac{2}{3}(g^{-1}dg)^{\wedge 3}\right).$$

> [!note]- Derivation
> Compute $d(g^{-1}dg) = d(g^{-1})\wedge dg = -g^{-1}dg\, g^{-1}\wedge dg = -(g^{-1}dg)\wedge(g^{-1}dg)$, using $d(g^{-1}) = -g^{-1}\,dg\,g^{-1}$.
>
> So $\mathrm{Tr}(g^{-1}dg\wedge d(g^{-1}dg)) = -\mathrm{Tr}((g^{-1}dg)^{\wedge 3}) = -\Omega_3$, where $\Omega_3 = \mathrm{Tr}((g^{-1}dg)^{\wedge 3})$ is the Cartan 3-form.
>
> Therefore $\mathrm{CS}_3\big|_{S^3_\infty} = -\Omega_3 + \tfrac{2}{3}\Omega_3 = -\tfrac{1}{3}\Omega_3$.
>
> Hence
> $$\int_{S^3_\infty}\mathrm{CS}_3 = -\tfrac{1}{3}\int_{S^3_\infty}\Omega_3.$$
>
> Combining with Step 2:
> $$\int_{\mathbb{R}^4}\mathrm{Tr}(F\wedge F) = -\tfrac{1}{3}\int_{S^3_\infty}\Omega_3.$$

**Step 4: Integral of $\Omega_3$ is $24\pi^2\,\deg(g)$.**

For $g : S^3_\infty \to SU(2) = S^3$, the pullback $g^*\Omega_3$ has the same form on $S^3_\infty$. By Frankel (22.2), $\int_{SU(2)}\Omega_3 = 24\pi^2$ (the bi-invariant volume). So $\int_{S^3_\infty}\Omega_3 = 24\pi^2\,\deg(g)$, where $\deg(g)$ is the Brouwer degree.

> [!note]- Derivation
> The map $g : S^3_\infty \to SU(2)$ has Brouwer degree $\deg(g) \in \mathbb{Z}$. The Cartan 3-form $\Omega_3$ on $SU(2)$ is a top-form (since $\dim SU(2) = 3$), so $g^*\Omega_3$ on $S^3_\infty$ is a top-form proportional to the standard volume of $S^3_\infty$. The integral $\int_{S^3_\infty} g^*\Omega_3$ equals $\deg(g)\int_{SU(2)}\Omega_3$ by the definition of degree applied to top forms.
>
> By Frankel (22.2) (a calculation we accept), $\int_{SU(2)}\Omega_3 = 24\pi^2$.
>
> So $\int_{S^3_\infty}\Omega_3 = 24\pi^2 \deg(g)$.

**Step 5: Assemble and verify for BPST.**

$$\int c_2(F) = -\frac{1}{8\pi^2}\int_{\mathbb{R}^4}\mathrm{Tr}(F\wedge F) = -\frac{1}{8\pi^2}\cdot(-\tfrac{1}{3})\cdot 24\pi^2\,\deg(g) = \deg(g).$$

For the BPST instanton, $g(x) = (x^4 \mathbf{1} + i\vec x\cdot\vec\sigma)/|x|$ on $S^3_\infty$. Under the standard identification $SU(2) = S^3 = \{(x^4, \vec x) : (x^4)^2 + |\vec x|^2 = 1\}$ (sending the 4-vector $(x^4, x^1, x^2, x^3)$ to the unit quaternion $x^4 + i x^1\sigma_1 + i x^2\sigma_2 + i x^3 \sigma_3$, normalised), this $g$ is *the identity map* $S^3 \to S^3$. So $\deg(g) = 1$.

> [!note]- Derivation
> The map $S^3_\infty \to SU(2)$ given by $x \mapsto (x^4 \mathbf{1} + i\vec x\cdot\vec\sigma)/|x|$ takes a unit 4-vector $x = (x^4, \vec x)$ on $S^3_\infty$ (with $|x| = 1$ implicitly on the unit sphere, or rescaled by $|x|$ as written for arbitrary radius) and sends it to the corresponding unit quaternion in $SU(2)$. Under the standard identification $SU(2) \cong S^3$ via $a + ib\sigma_1 + ic\sigma_2 + id\sigma_3 \leftrightarrow (a, b, c, d)$, this is the identity map $S^3 \to S^3$.
>
> The identity map has degree 1: $\deg(\mathrm{id}_{S^3}) = 1$ (signed count of preimages of any point — exactly one preimage with positive sign).
>
> Therefore $\int c_2(F_{\mathrm{BPST}}) = \deg(g_{\mathrm{BPST}}) = 1$.

> [!note]- Complete formal solution
> The BPST instanton on $\mathbb{R}^4$ has $SU(2)$ structure group and asymptotes to pure gauge $A = g^{-1}dg$ at infinity, with $g(x) = (x^4 + i\vec x\cdot\vec\sigma)/|x|$ on $S^3_\infty$.
>
> The second Chern number is
> $$\int c_2 = -\frac{1}{8\pi^2}\int_{\mathbb{R}^4}\mathrm{Tr}(F \wedge F).$$
>
> By the Chern–Simons identity $\mathrm{Tr}(F \wedge F) = d\,\mathrm{CS}_3$ (Step 2) and Stokes' theorem, the bulk integral reduces to a boundary integral:
> $$\int_{\mathbb{R}^4}\mathrm{Tr}(F\wedge F) = \int_{S^3_\infty}\mathrm{CS}_3.$$
>
> For pure gauge $A = g^{-1}dg$, the Chern–Simons form simplifies (Step 3):
> $$\mathrm{CS}_3 = -\tfrac{1}{3}\,\Omega_3, \qquad \Omega_3 = \mathrm{Tr}((g^{-1}dg)^{\wedge 3}).$$
>
> The Cartan 3-form $\Omega_3$ on $SU(2) = S^3$ integrates to $24\pi^2$ (Frankel 22.2), and pullback by $g$ scales by degree:
> $$\int_{S^3_\infty}\Omega_3 = 24\pi^2 \deg(g).$$
>
> Combining:
> $$\int c_2 = -\frac{1}{8\pi^2}\cdot(-\tfrac{1}{3})\cdot 24\pi^2 \deg(g) = \deg(g).$$
>
> For the BPST $g$, identified with the identity map $S^3 \to S^3 = SU(2)$, $\deg(g) = 1$. So $\int_{\mathbb{R}^4}c_2 = 1$. $\blacksquare$

> [!warning] Illegal but tempting: bulk integration without checking decay
> The integral $\int_{\mathbb{R}^4}\mathrm{Tr}(F\wedge F)$ is a 4-dimensional integral over a non-compact space, and it is only finite because $F$ decays sufficiently fast at infinity ($F \sim 1/|x|^3$ for the BPST instanton). Without this decay, the integral diverges and the topological charge is ill-defined. The reduction to a boundary integral via Stokes requires the bulk integrand to decay so that the boundary at infinity captures all the topology. If one tried this for a generic non-decaying connection, the integral would not be an integer and would have no topological interpretation. The operation is legal exactly when the connection has finite Yang–Mills action (the so-called "finite-action" instantons), which is automatic for the BPST family.

---

# Key Takeaways

**The instanton number is the degree of the gauge transformation at infinity — the topological charge of a finite-action gauge field.** Every finite-action $SU(n)$ Yang–Mills field on $\mathbb{R}^4$ asymptotes to a pure-gauge configuration $A = g^{-1}dg$, where $g : S^3_\infty \to SU(n)$. The integer $\int c_2 \in \mathbb{Z}$ is the degree of $g$ as a map between 3-spheres (or, more generally, the homotopy class in $\pi_3(SU(n)) = \mathbb{Z}$). This integer labels distinct topological sectors of the Yang–Mills configuration space: configurations of different $c_2$ cannot be continuously deformed into each other. The lesson is that *bulk topological invariants of gauge fields are determined by their boundary asymptotics*, a recurring theme in physics (bulk-edge correspondence, asymptotic charges in GR).

**Stokes + Chern–Simons reduces bulk topological integrals to boundary winding numbers.** The recipe — bulk integral of $\mathrm{Tr}(F\wedge F)$ becomes boundary integral of the Chern–Simons 3-form on $S^3_\infty$ — generalises to higher-dimensional analogues: $\int_{\mathbb{R}^{4n}} \mathrm{Tr}(F^{\wedge 2n}) =$ boundary integral of a Chern–Simons $(4n-1)$-form, related to maps $S^{4n-1} \to G$ and elements of $\pi_{4n-1}(G)$. This is the foundation of *anomaly inflow* in physics: bulk topological terms in $(D+1)$ dimensions reduce to anomalies in $D$ dimensions via the boundary mechanism. The lesson: *bulk topological terms = boundary winding integers = elements of $\pi_*$ of the gauge group*.

**The BPST instanton is the smallest, most symmetric representative of the $k=1$ sector.** All $SU(2)$ Yang–Mills fields with $\int c_2 = 1$ form a topological sector; the BPST family (parameterised by translations and a scale $\rho$) gives the explicit *action-minimising* representatives. The action of any BPST instanton is $S = 8\pi^2$ (exactly the Bogomolnyi bound $8\pi^2 |c_2|$), saturated because BPST is self-dual ($\star F = F$). Moduli space of charge-1 $SU(2)$ instantons on $\mathbb{R}^4$ has dimension $4 + 1 = 5$ (translations + scale) modulo conformal symmetries; the full moduli space of $SU(2)$ charge-$k$ instantons has dimension $8k - 3$. These moduli are the data of **Donaldson theory** of smooth 4-manifolds. The lesson: *each instanton sector contains a finite-dimensional moduli space*, and these moduli encode geometric invariants beyond the topological charge.
