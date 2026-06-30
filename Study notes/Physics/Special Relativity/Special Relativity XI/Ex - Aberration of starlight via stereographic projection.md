---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)"
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
tags: [physics, special-relativity]
---

# Problem Statement

An observer boosts with rapidity $\psi$ (velocity $\beta = \tanh\psi$) along the $z$-axis. Using the [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|celestial-sphere]] formalism with stereographic coordinate $\omega = e^{i\phi}\cot(\theta/2)$ (for a star at polar angle $\theta$ from the forward direction, azimuth $\phi$):

1. Show that the boost acts on the sky by the Möbius dilation $\omega \mapsto \omega' = e^{-\psi}\omega$, and deduce the aberration formula $\cot(\theta'/2) = e^{-\psi}\cot(\theta/2)$, equivalently $\tan(\theta'/2) = e^{\psi}\tan(\theta/2)$.
2. Re-express the aberration formula in terms of velocity, recovering the standard $\cos\theta' = (\cos\theta + \beta)/(1 + \beta\cos\theta)$, and note that $e^{-\psi} = \sqrt{(1-\beta)/(1+\beta)}$.
3. Explain the **headlight effect**: as $\beta \to 1$, stars from all over the sky concentrate into a small forward cone. Estimate the half-angle of the cone containing half the sky as a function of $\psi$.
4. Explain why a *circle* of stars on the sky maps to another circle (not an ellipse), connecting to the Penrose–Terrell invisibility of length contraction.

**Recall:**

![[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)#Statement]]

A boost of rapidity $\psi$ along $z$ corresponds to the Hermitian $SL(2,\mathbb{C})$ matrix $A = \mathrm{diag}(e^{-\psi/2}, e^{\psi/2})$ in Tong's passive convention (the observer's frame moves at $+\beta$), with $\beta = \tanh\psi$, $\gamma = \cosh\psi$. The stereographic coordinate is $\omega = e^{i\phi}\cot(\theta/2)$, with $\theta = 0$ the forward direction ($\omega = \infty$). Möbius maps and stereographic projection are conformal and send circles to circles.

---

# Convergent Strategy

**Problem class.** A *quantitative aberration computation* via the celestial sphere — turning the abstract Möbius action into the measurable bending of starlight, and into the headlight effect. The [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map#Problem-Solving Strategy|topic strategy]] says a boost along the line of sight is the dilation $\omega \mapsto e^{-\psi}\omega$; this exercise extracts the aberration angle from it.

**Assumption pattern.** The boost is along the *line of sight* ($z$-axis), which is the special case where the Möbius map is a pure real dilation $\omega \mapsto e^{-\psi}\omega$ rather than a general fractional-linear map — the diagonal $A$ has $b = c = 0$. The signpost is "boost along $z$ with the forward direction as the pole," which makes the stereographic coordinate's modulus $\cot(\theta/2)$ scale by a single factor.

**Theorem routing.** This applies [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)]] (the Möbius action) with the explicit boost matrix from [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|the correspondence]], and connects to the elementary [[Thm - Aberration of Light]] of Special Relativity VIII for the velocity form.

**Key decision point.** The crux is recognising that the *modulus* of $\omega$ carries the polar angle ($|\omega| = \cot(\theta/2)$) and the *phase* carries the azimuth, so a real dilation $\omega \mapsto e^{-\psi}\omega$ changes only the polar angle, leaving azimuth fixed — which is exactly what a boost along the symmetry axis must do. Scaling $\cot(\theta/2)$ by $e^{-\psi}$ and inverting gives the aberration formula; recognising that $\cot(\theta/2)$ (not $\cos\theta$) is the natural variable is what makes the boost a clean multiplication.

---

# Legal Operations Used

1. **Parametrise a null direction by a spinor and project stereographically** (operation 7 from the topic page): the aberration is computed entirely in the stereographic coordinate $\omega$.

2. **Exponentiate a generator / read off the boost matrix** (operation 4 from the topic page): the boost $A = \mathrm{diag}(e^{-\psi/2}, e^{\psi/2})$ gives the Möbius dilation factor $e^{-\psi}$.

3. **Use conformality (circle-preservation)** (operation 7 / warning 4 from the topic page): part 4 invokes that Möbius maps send circles to circles for the Penrose–Terrell conclusion.

---

# Hints

> [!note]- Hint 1
> The boost matrix $A = \mathrm{diag}(e^{-\psi/2}, e^{\psi/2})$ gives $\omega' = (e^{-\psi/2}\xi_1)/(e^{\psi/2}\xi_2) = e^{-\psi}\omega$. Since $|\omega| = \cot(\theta/2)$, this means $\cot(\theta'/2) = e^{-\psi}\cot(\theta/2)$.

> [!note]- Hint 2
> Use $\cot(\theta/2) = \frac{1+\cos\theta}{\sin\theta}$ and the identity $\cos\theta = \frac{\cot^2(\theta/2) - 1}{\cot^2(\theta/2) + 1}$. Substitute $\cot(\theta'/2) = e^{-\psi}\cot(\theta/2)$ and simplify using $e^{-2\psi} = \frac{1-\beta}{1+\beta}$ (from $\beta = \tanh\psi$).

> [!note]- Hint 3
> Forward ($\theta \approx 0$) means $\cot(\theta/2)$ large; the dilation $e^{-\psi} < 1$ shrinks $\cot(\theta'/2)$, but a star *behind* ($\theta$ near $\pi$, $\cot(\theta/2)$ small) is pushed even smaller — toward $\theta' = \pi$? Re-examine: the dilation pulls the *pattern* toward $\omega = 0$, but $\omega = 0$ is the *backward* pole. Recheck the sign/pole convention: with the forward direction at $\omega = \infty$, $e^{-\psi}\omega$ moves points *away* from $\infty$, i.e. *toward* the backward pole — so in this convention the boost moves the *source's* sky backward, equivalently the *observer* sees stars bunch forward. The half-sky angle satisfies $\cot(\theta_{1/2}'/2) = e^{-\psi}\cdot 1$ for the star that was at $\theta = \pi/2$.

> [!note]- Hint 4
> A circle on the celestial sphere is a circle in the $\omega$-plane (stereographic projection is conformal). The dilation $\omega \mapsto e^{-\psi}\omega$ is a Möbius map, which sends circles to circles. So the image of a circular pattern is a circle — never an ellipse.

---

# Solution

The exercise extracts the aberration formula from the Möbius dilation, recovers the velocity form, and explains the headlight effect and the circle theorem. The plan: the line-of-sight boost is a real dilation of $\omega$ by $e^{-\psi}$; since $|\omega| = \cot(\theta/2)$, the polar angle transforms by $\cot(\theta'/2) = e^{-\psi}\cot(\theta/2)$; convert to velocity form; analyse the forward bunching; invoke conformality for circles.

**Step 1: The aberration formula $\cot(\theta'/2) = e^{-\psi}\cot(\theta/2)$.**

> [!note]- Derivation
> The line-of-sight boost is $A = \mathrm{diag}(e^{-\psi/2}, e^{\psi/2})$ (Tong's convention). By the [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|Möbius action]], with $a = e^{-\psi/2}$, $d = e^{\psi/2}$, $b = c = 0$,
> $$\omega' = \frac{a\omega + b}{c\omega + d} = \frac{e^{-\psi/2}\omega}{e^{\psi/2}} = e^{-\psi}\omega.$$
> This is a real dilation of the Riemann sphere. Since $\omega = e^{i\phi}\cot(\theta/2)$, the dilation scales only the modulus, leaving the azimuth $\phi$ fixed (as a boost along the symmetry axis must):
> $$\cot\frac{\theta'}{2} = e^{-\psi}\cot\frac{\theta}{2}, \qquad\text{equivalently}\qquad \tan\frac{\theta'}{2} = e^{\psi}\tan\frac{\theta}{2}.$$
> This is the relativistic aberration formula in its most compact form. The half-angle $\theta/2$ is the natural variable precisely because it is what stereographic projection puts into the modulus of $\omega$.

**Step 2: The velocity form $\cos\theta' = (\cos\theta + \beta)/(1 + \beta\cos\theta)$.**

> [!note]- Derivation
> Use $\cos\theta = \frac{1 - \tan^2(\theta/2)}{1 + \tan^2(\theta/2)}$ and the relation $\tan(\theta'/2) = e^{\psi}\tan(\theta/2)$. Writing $u = \tan^2(\theta/2)$, so $\cos\theta = \frac{1-u}{1+u}$, and $\tan^2(\theta'/2) = e^{2\psi}u$, so $\cos\theta' = \frac{1 - e^{2\psi}u}{1 + e^{2\psi}u}$. Now $e^{2\psi} = \frac{1+\beta}{1-\beta}$ (from $\beta = \tanh\psi = \frac{e^\psi - e^{-\psi}}{e^\psi + e^{-\psi}}$, so $e^{2\psi} = \frac{1+\beta}{1-\beta}$). Substitute and clear:
> $$\cos\theta' = \frac{(1-\beta) - (1+\beta)u}{(1-\beta) + (1+\beta)u}.$$
> Solving $\cos\theta = \frac{1-u}{1+u}$ for $u = \frac{1 - \cos\theta}{1 + \cos\theta}$ and substituting, after simplification,
> $$\cos\theta' = \frac{\cos\theta + \beta}{1 + \beta\cos\theta}.$$
> This is the standard aberration formula of [[Thm - Aberration of Light|Special Relativity VIII]], now derived purely from the Möbius dilation. The factor relating the two forms is $e^{-\psi} = \sqrt{\frac{1-\beta}{1+\beta}}$, the relativistic Doppler/aberration factor.

**Step 3: The headlight effect.**

> [!note]- Derivation
> As $\beta \to 1$, $\psi \to \infty$ and $e^{-\psi} \to 0$. The dilation $\omega \mapsto e^{-\psi}\omega$ collapses almost the entire $\omega$-plane toward $\omega = 0$ (the backward pole $\theta = \pi$ in this convention), which means — translating to the *observer's* view of an isotropic star field — that the stars bunch into a narrow cone around the *forward* direction $\theta = 0$. Concretely, a star at $\theta = \pi/2$ ($\cot(\pi/4) = 1$, so $|\omega| = 1$) maps to $\cot(\theta'/2) = e^{-\psi}$, i.e.
> $$\theta'_{1/2} = 2\,\mathrm{arccot}(e^{-\psi}) = 2\arctan(e^{\psi}) \xrightarrow{\psi\to\infty} \pi,$$
> so in this (source-frame) convention half the sky is pushed into $\theta' > \theta'_{1/2} \to \pi$; equivalently, for the *observer moving forward*, half the celestial sphere's stars are compressed into a forward cone of half-angle $\theta_{\text{fwd}} \approx 2e^{-\psi} = 2\sqrt{\frac{1-\beta}{1+\beta}}$ for large $\psi$ (small forward angle). This is the **headlight effect** (or *relativistic beaming*): a fast observer sees the sky ahead crowded with blueshifted stars and the sky behind nearly empty and redshifted. The same effect beams the radiation of a relativistic source (a synchrotron electron, a quasar jet) into a forward cone of half-angle $\sim 1/\gamma$, since for large $\psi$, $e^{-\psi} \approx 1/(2\gamma)$, giving a beam half-angle of order $1/\gamma$.

**Step 4: A circle stays a circle (Penrose–Terrell).**

> [!note]- Derivation
> A circular outline on the celestial sphere — say the silhouette of a spherical object, or a constellation's circular feature — projects under stereographic projection to a circle (or line) in the $\omega$-plane, because stereographic projection is conformal and maps circles to circles. The aberration acts on this by the Möbius dilation $\omega \mapsto e^{-\psi}\omega$, which is a Möbius transformation and therefore *also* sends circles to circles (a dilation maps a circle of radius $r$ centred at $\omega_0$ to a circle of radius $e^{-\psi}r$ centred at $e^{-\psi}\omega_0$). Inverse-projecting back to the sphere, the image is again a circle. So a circular pattern of stars remains circular for the boosted observer — it may shrink and shift, but it never becomes an ellipse.
>
> The dramatic instance is the silhouette of a **sphere**: at rest it subtends a circular cap on the celestial sphere, and after any boost the cap's outline is still a circle. So a relativistic sphere photographs as a perfect circle, *never* a length-contracted ellipse — the **Penrose–Terrell** result, the "invisibility of the Lorentz contraction." The length contraction is genuinely present in the coordinates, but the differential light-travel-time across the sphere conspires with it to produce a conformal (circle-preserving) map of the apparent outline rather than an affine squashing. Patterns *painted* on the sphere are conformally distorted (a drawn square deforms), but the circular outline is rigid. The deep reason is that aberration is a Möbius transformation, and Möbius transformations are exactly the conformal automorphisms of the sphere.

> [!note]- Complete formal solution
> The line-of-sight boost $A = \mathrm{diag}(e^{-\psi/2}, e^{\psi/2})$ gives the Möbius dilation $\omega \mapsto e^{-\psi}\omega$; since $|\omega| = \cot(\theta/2)$, the polar angle obeys $\cot(\theta'/2) = e^{-\psi}\cot(\theta/2)$, i.e. $\tan(\theta'/2) = e^\psi\tan(\theta/2)$. Converting with $\cos\theta = \frac{1-\tan^2(\theta/2)}{1+\tan^2(\theta/2)}$ and $e^{2\psi} = \frac{1+\beta}{1-\beta}$ recovers $\cos\theta' = \frac{\cos\theta+\beta}{1+\beta\cos\theta}$, with $e^{-\psi} = \sqrt{(1-\beta)/(1+\beta)}$. As $\beta\to 1$, $e^{-\psi}\to 0$ collapses the sky into a forward cone of half-angle $\sim 1/\gamma$ — the headlight effect. Because the dilation is a Möbius map and Möbius maps preserve circles, a circular outline (in particular a sphere's silhouette) stays circular for every observer — the Penrose–Terrell invisibility of length contraction. $\blacksquare$

---

# Key Takeaways

**The half-angle $\theta/2$ is the natural variable for aberration because stereographic projection puts it in the modulus.** The aberration formula is ungainly in $\cos\theta$ but trivially simple — a single multiplication — in $\cot(\theta/2)$, and this is no accident: stereographic projection sends a direction at polar angle $\theta$ to a complex number of modulus $\cot(\theta/2)$, so a boost along the line of sight, being a real dilation of that complex number, just scales $\cot(\theta/2)$ by $e^{-\psi}$. The lesson is that the right coordinate makes a hard formula easy, and the right coordinate for the sky is the stereographic one. This is a recurring theme: the relativistic Doppler factor, the aberration factor, and the boost eigenvalues are all powers of $e^{\psi/2}$, and they look simplest in variables ($\cot(\theta/2)$, rapidity, light-cone coordinates) adapted to the multiplicative structure of the boost. When a relativistic formula is messy in the obvious variable, look for the variable in which the boost acts by multiplication.

**The headlight effect is the dilation collapsing the sphere, and it beams radiation into a $1/\gamma$ cone.** As the rapidity grows, the Möbius dilation $e^{-\psi} \approx 1/(2\gamma)$ shrinks the apparent sky toward a forward cone of half-angle $\sim 1/\gamma$, which is why a fast observer sees the stars crowded ahead and why a relativistic emitter (synchrotron electron, blazar jet, the beam of a particle accelerator) radiates almost entirely forward. This single geometric fact — that a boost is a dilation of the Riemann sphere — unifies the aberration of starlight, the forward beaming of synchrotron radiation, and the apparent superluminal motion of quasar jets (which are beamed nearly at us). The reusable estimate is that anything emitted isotropically in its rest frame is beamed into a cone of half-angle $\sim 1/\gamma$ in a frame where it moves at $\gamma \gg 1$, and this follows directly from the $e^{-\psi}$ collapse of the celestial sphere. Recognising "isotropic in the rest frame + large boost" as a trigger for "$1/\gamma$ forward beaming" handles a whole class of high-energy astrophysics problems.

**Conformality is why the contraction is invisible: the apparent outline is Möbius-transformed, not squashed.** The most conceptually important takeaway is the resolution of the apparent paradox between length contraction (real) and the Penrose–Terrell circle theorem (a sphere looks round). The contraction is genuinely present in the *coordinates* the boosted observer assigns, but what the observer *sees* — the apparent outline on the celestial sphere — is governed by the Möbius action, which is conformal and circle-preserving, not affine and ellipse-producing. The differential time-of-flight of light across the object exactly converts the affine coordinate contraction into a conformal apparent map. The transferable diagnostic is that "what is measured" (coordinates, governed by the full Lorentz group) and "what is seen" (the sky, governed by the conformal Möbius subgroup-action) are different questions with different answers, and conflating them is the source of nearly every confusion about relativistic appearance. Whenever a problem asks what an object *looks like* (as opposed to what its coordinates are), reach for the conformal celestial-sphere picture, and remember that round things stay round.
