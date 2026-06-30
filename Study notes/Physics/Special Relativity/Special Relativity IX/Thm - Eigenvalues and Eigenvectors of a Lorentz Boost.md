---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Boosts as Hyperbolic Rotations"
  - "Def - Classification of Restricted Lorentz Transformations"
  - "Def - Rapidity"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. A [[Def - Boosts as Hyperbolic Rotations|Lorentz boost]] of plane $\Pi_0 = \mathrm{Span}(e_0,e_1)$ and rapidity $\psi$ acts as $\mathrm{diag}\big(\begin{smallmatrix}\cosh\psi & \sinh\psi\\ \sinh\psi & \cosh\psi\end{smallmatrix}, 1, 1\big)$ in the orthonormal basis. The null vectors of the boost plane are $\ell_\pm = e_0 \pm e_1$ ($\ell_\pm\cdot\ell_\pm = 0$). The [[Def - Rapidity|rapidity]] $\psi$ relates to the velocity parameter by $V = \tanh\psi$, $\cosh\psi = \Gamma = (1-V^2)^{-1/2}$. Full registry on [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

---

# Statement

> **Theorem (Eigenstructure of a Lorentz boost).** A Lorentz boost $\Lambda$ of plane $\Pi_0 = \mathrm{Span}(e_0,e_1)$ and rapidity $\psi$ is diagonalisable over $\mathbb{R}$, with eigenvalues and eigenvectors
> $$\lambda_+ = e^{\psi},\quad \ell_+ = e_0 + e_1; \qquad \lambda_- = e^{-\psi},\quad \ell_- = e_0 - e_1; \qquad \lambda_0 = 1,\quad e_2,\ e_3.$$
> The eigenvectors $\ell_\pm$ are **null**; the eigenvalue $1$ has multiplicity two, with eigenspace the entire spacelike plane $\mathrm{Span}(e_2,e_3)$, fixed pointwise. In terms of the velocity parameter $V = \tanh\psi$,
> $$\lambda_\pm = \sqrt{\frac{1\pm V}{1\mp V}},$$
> the relativistic longitudinal Doppler factors. Equivalently, $\cosh\psi = \tfrac12\mathrm{tr}\,\Lambda - 1$.

---

# Motivation

A boost is a hyperbolic rotation, and just as an ordinary rotation is most transparent in the basis where it is diagonal (its complex eigenvectors), a boost is most transparent in the basis where *it* is diagonal. This theorem finds that basis, and the answer is illuminating: the diagonalising directions are not the timelike and spacelike axes but the two *null* directions of the boost plane — the two light rays in the plane. A boost stretches one light ray and shrinks the other, leaving the perpendicular spacelike plane untouched.

The physical payoff is that the eigenvalues turn out to be the Doppler factors. The rapidity $\psi$, an abstract additive parameter, acquires a direct operational meaning: $e^{\pm\psi}$ are exactly the factors by which the frequency of light is redshifted and blueshifted along the boost direction. So the eigenvalues of a boost are not abstract numbers; they are measured every time a moving source's light is observed. This connects the group-theoretic structure of §9.2 to the observable kinematics of [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group|Special Relativity IV]].

The theorem also draws the sharpest possible line between the three types of the classification. A boost has *real* eigenvalues on *null* eigenvectors. A spatial rotation has *complex* (unimodular) eigenvalues $e^{\pm i\theta}$. A null rotation has a *single* eigenvalue $1$ with a defective Jordan block. The eigenstructure is a fingerprint: compute the eigenvalues, and the type is determined.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\Lambda$ is a boost." The disguised sources are the ways one recognises a boost whose eigenstructure is wanted.

The first disguised source is **"a symmetric restricted matrix in a semi-adapted basis."** A boost is exactly a restricted transformation whose matrix in a basis with $e_0$ in the boost plane is symmetric, $\Lambda^\alpha{}_\beta = \Lambda^\beta{}_\alpha$. So whenever a symmetric restricted matrix appears, it is a boost and this theorem applies. The bridge is the symmetry criterion for boosts. *Example problem:* given a symmetric $\Lambda \in SO^+(1,3)$, find its eigenvalues and confirm they are real and positive.

The second disguised source is **"a transformation with two real positive eigenvalues $\ne 1$."** If a restricted transformation has a real eigenvalue $\lambda > 0$, $\lambda \ne 1$, on a null eigenvector, it has a boost component, and a four-screw with $\theta = 0$ is a pure boost. The bridge is that real eigenvalues on null directions are the spectral signature of a boost. *Example problem:* decide whether a given transformation is a boost by checking that its only non-unit eigenvalues are a reciprocal pair $e^{\pm\psi}$.

The third disguised source is **"the relative motion of two observers."** The transformation carrying one inertial observer's 4-velocity to another's is the boost between them, and its eigenvalues are the Doppler factors for light exchanged along the line of relative motion. The bridge is the kinematic interpretation of the boost. *Example problem:* compute the redshift of a signal between two observers in relative motion as the boost eigenvalue $e^{-\psi}$.

**Targets (Output Amplification)**

The conclusion is "$\lambda_\pm = e^{\pm\psi}$ on null $\ell_\pm$, $\lambda_0 = 1$ on the spacelike plane."

Combine the conclusion with **the Doppler interpretation**. Since $\lambda_\pm = \sqrt{(1\pm V)/(1\mp V)}$, the boost eigenvalues *are* the longitudinal Doppler factors, so the rapidity is the logarithm of the Doppler shift, $\psi = \ln(\lambda_+) = -\ln(\lambda_-)$. The further result is an operational reading of rapidity: it is directly measured as $\tfrac12\ln(f_{\text{blue}}/f_{\text{red}})$ for light observed along the motion. The combination links the abstract spectral data to a frequency measurement.

Combine the conclusion with **the type-discrimination of the classification**. Real eigenvalues on null directions $\Rightarrow$ boost; complex unimodular eigenvalues $\Rightarrow$ rotation; a single eigenvalue $1$ with a Jordan block $\Rightarrow$ null rotation. The further result is a complete eigenvalue test for the type of any restricted transformation. The combination is useful because it reduces classification to a spectral computation.

Combine the conclusion with **the determinant and trace**. The eigenvalues multiply to $\det\Lambda = e^{\psi}\cdot e^{-\psi}\cdot 1\cdot 1 = 1$ (confirming properness) and sum to $\mathrm{tr}\,\Lambda = e^\psi + e^{-\psi} + 2 = 2\cosh\psi + 2$ (giving the trace formula $\cosh\psi = \tfrac12\mathrm{tr}\,\Lambda - 1$). The further result is the basis-free extraction of the rapidity from the trace. The combination is the fast route to $\psi$ without diagonalising.

---

# Why Is It True

A boost is a hyperbolic rotation of the timelike plane $\Pi_0$, and the question is what directions it scales. In an ordinary rotation of a Euclidean plane, the scaling directions are complex — the eigenvectors $e_1 \mp ie_2$ with eigenvalues $e^{\pm i\theta}$ — because a rotation has no real invariant lines (it moves every direction). A hyperbolic rotation is different: it *does* have real invariant lines, namely the asymptotes of the hyperbolas it slides points along. Those asymptotes are exactly the two light rays $\ell_\pm = e_0 \pm e_1$ of the plane.

Here is the computation that makes it transparent. In the basis $(\ell_+, \ell_-)$ the boost is diagonal: $\Lambda(\ell_+) = \Lambda(e_0+e_1) = (\cosh\psi\, e_0 + \sinh\psi\, e_1) + (\sinh\psi\, e_0 + \cosh\psi\, e_1) = (\cosh\psi+\sinh\psi)(e_0+e_1) = e^\psi\ell_+$, using $\cosh\psi + \sinh\psi = e^\psi$. Symmetrically $\Lambda(\ell_-) = e^{-\psi}\ell_-$. So the boost stretches the future light ray $\ell_+$ by $e^\psi > 1$ and shrinks the future light ray $\ell_-$ by $e^{-\psi} < 1$. **The mechanism is that the asymptotes of a hyperbola are its invariant directions, and the asymptotes of the boost's hyperbolas are the light rays.**

That the eigenvalues are Doppler factors is then immediate from $e^{\pm\psi} = \cosh\psi \pm \sinh\psi = \Gamma(1\pm V) = \Gamma\pm\Gamma V$, and $\Gamma(1+V) = \sqrt{(1+V)/(1-V)}$ since $\Gamma = (1-V^2)^{-1/2} = 1/\sqrt{(1-V)(1+V)}$. A photon moving along $+x$ has its frequency multiplied by exactly $\sqrt{(1-V)/(1+V)} = e^{-\psi}$ when viewed from a frame receding at $V$ — the relativistic redshift — and by $e^{+\psi}$ when approaching. The light ray $\ell_-$ is shrunk because its frequency is redshifted; $\ell_+$ is stretched because blueshifted.

That the spacelike plane is fixed pointwise is because a boost touches only its own plane: $\Lambda(e_2) = e_2$, $\Lambda(e_3) = e_3$. So $\lambda = 1$ has the whole of $\mathrm{Span}(e_2,e_3)$ as eigenspace.

The contrast with the rotation case is the deep point: a rotation's eigenvectors are complex because $\cos\theta, \sin\theta$ are bounded, so there is no real direction it merely scales — it genuinely rotates. A boost's eigenvectors are real and null because $\cosh\psi, \sinh\psi$ are unbounded, so the hyperbola has real asymptotes the boost slides along. The minus sign in the metric is what turns the circle into a hyperbola and the complex eigenvectors into real null ones.

---

# What Makes This Hard

The non-obvious step is realising that the diagonalising directions are *null*, not the timelike/spacelike axes — the boost has no timelike or spacelike eigenvectors at all (it moves $e_0$ and $e_1$), only the two null asymptotes. The common error is to attempt diagonalisation in the orthonormal basis and produce eigenvectors that are not normalised null vectors, missing that the natural eigenbasis is the *null* basis $(\ell_+, \ell_-, e_2, e_3)$. A second subtlety is the identification of $e^{\pm\psi}$ with the Doppler factors $\sqrt{(1\pm V)/(1\mp V)}$, which requires the algebra $\Gamma(1\pm V) = \sqrt{(1\pm V)/(1\mp V)}$ and is easy to get backwards (redshift versus blueshift).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Change to the null basis $(\ell_+, \ell_-, e_2, e_3)$ with $\ell_\pm = e_0 \pm e_1$; the boost is diagonal there with entries $e^{\pm\psi}$ and $1, 1$, using $\cosh\psi\pm\sinh\psi = e^{\pm\psi}$. Then rewrite $e^{\pm\psi}$ in velocity variables to recognise the Doppler factors.

**Subgoal decomposition:**

1. **Apply the boost to $\ell_\pm$.** Show $\Lambda(\ell_\pm) = e^{\pm\psi}\ell_\pm$.
   - *Hint:* $\Lambda(e_0+e_1) = (\cosh\psi+\sinh\psi)(e_0+e_1)$ since the boost mixes $e_0, e_1$.
   - *Why needed:* It exhibits the null eigenvectors and their eigenvalues.

2. **Apply the boost to $e_2, e_3$.** Show $\Lambda(e_2) = e_2$, $\Lambda(e_3) = e_3$.
   - *Hint:* The boost is the identity on the transverse plane.
   - *Why needed:* It gives the eigenvalue $1$ with eigenspace $\mathrm{Span}(e_2,e_3)$.

3. **Confirm diagonalisability.** Note $(\ell_+, \ell_-, e_2, e_3)$ is a basis (the null pair plus the spacelike pair), so $\Lambda$ is diagonal in it.
   - *Hint:* $\ell_+, \ell_-$ are linearly independent (their sum is $2e_0$, difference $2e_1$).
   - *Why needed:* It establishes real diagonalisability, distinguishing the boost from a rotation.

4. **Rewrite in velocity variables.** Show $e^{\pm\psi} = \Gamma(1\pm V) = \sqrt{(1\pm V)/(1\mp V)}$.
   - *Hint:* $e^{\pm\psi} = \cosh\psi\pm\sinh\psi$, $\cosh\psi = \Gamma$, $\sinh\psi = \Gamma V$, $\Gamma = (1-V^2)^{-1/2}$.
   - *Why needed:* It identifies the eigenvalues with the Doppler factors.

---

# Lemma Decomposition

> [!note]- Lemma 1: The null vectors of the boost plane are eigenvectors
> **Statement:** For a boost of rapidity $\psi$ in $\mathrm{Span}(e_0,e_1)$, $\Lambda(e_0\pm e_1) = e^{\pm\psi}(e_0\pm e_1)$.
>
> **Hint:** Use $\cosh\psi\pm\sinh\psi = e^{\pm\psi}$.
>
> **Why needed:** It is the core eigenvalue computation.
>
> > [!note]- Full proof
> > The boost acts by $\Lambda(e_0) = \cosh\psi\, e_0 + \sinh\psi\, e_1$ and $\Lambda(e_1) = \sinh\psi\, e_0 + \cosh\psi\, e_1$. Hence
> > $$\Lambda(e_0 + e_1) = (\cosh\psi + \sinh\psi)e_0 + (\sinh\psi + \cosh\psi)e_1 = (\cosh\psi+\sinh\psi)(e_0+e_1) = e^{\psi}(e_0+e_1),$$
> > and similarly
> > $$\Lambda(e_0 - e_1) = (\cosh\psi-\sinh\psi)(e_0-e_1) = e^{-\psi}(e_0-e_1),$$
> > using $\cosh\psi\pm\sinh\psi = e^{\pm\psi}$. The eigenvectors $\ell_\pm = e_0\pm e_1$ satisfy $\ell_\pm\cdot\ell_\pm = 1 - 1 = 0$, so they are null. $\blacksquare$

> [!note]- Lemma 2: The transverse plane is fixed pointwise
> **Statement:** $\Lambda(e_2) = e_2$ and $\Lambda(e_3) = e_3$, so $\lambda = 1$ has eigenspace $\mathrm{Span}(e_2,e_3)$.
>
> **Hint:** The boost matrix is the identity on the lower-right $2\times 2$ block.
>
> **Why needed:** It accounts for the eigenvalue $1$ of multiplicity two.
>
> > [!note]- Full proof
> > A boost of plane $\mathrm{Span}(e_0,e_1)$ has matrix $\mathrm{diag}\big(\begin{smallmatrix}\cosh\psi & \sinh\psi\\ \sinh\psi & \cosh\psi\end{smallmatrix}, 1, 1\big)$, so $\Lambda(e_2) = e_2$ and $\Lambda(e_3) = e_3$ directly. Hence every vector in $\mathrm{Span}(e_2,e_3)$ is fixed, and $\lambda = 1$ has geometric multiplicity (at least) two. Since the four eigenvalues $e^\psi, e^{-\psi}, 1, 1$ exhaust the spectrum, the eigenspace of $1$ is exactly $\mathrm{Span}(e_2,e_3)$. $\blacksquare$

> [!note]- Lemma 3: The eigenvalues are the Doppler factors
> **Statement:** $e^{\pm\psi} = \sqrt{(1\pm V)/(1\mp V)}$, with $V = \tanh\psi$.
>
> **Hint:** $e^{\pm\psi} = \Gamma(1\pm V)$ and $\Gamma = 1/\sqrt{(1-V)(1+V)}$.
>
> **Why needed:** It supplies the physical meaning of the eigenvalues.
>
> > [!note]- Full proof
> > Write $e^{\pm\psi} = \cosh\psi \pm \sinh\psi$. With $\cosh\psi = \Gamma$, $\sinh\psi = \Gamma V$, and $\Gamma = (1-V^2)^{-1/2}$,
> > $$e^{\pm\psi} = \Gamma(1 \pm V) = \frac{1\pm V}{\sqrt{(1-V)(1+V)}} = \sqrt{\frac{(1\pm V)^2}{(1-V)(1+V)}} = \sqrt{\frac{1\pm V}{1\mp V}}.$$
> > This is the relativistic longitudinal Doppler factor: a photon emitted with frequency $f$ along $+x$ is observed at frequency $f\,e^{-\psi} = f\sqrt{(1-V)/(1+V)}$ by a frame receding at $V$ (redshift), and $f\,e^{+\psi}$ by a frame approaching (blueshift). $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\Lambda$ be a boost of plane $\mathrm{Span}(e_0,e_1)$ and rapidity $\psi$, matrix $\mathrm{diag}\big(\begin{smallmatrix}\cosh\psi & \sinh\psi\\ \sinh\psi & \cosh\psi\end{smallmatrix}, 1, 1\big)$ in the orthonormal basis.
>
> By Lemma 1, the null vectors $\ell_\pm = e_0\pm e_1$ are eigenvectors with eigenvalues $e^{\pm\psi}$.
>
> By Lemma 2, $e_2$ and $e_3$ are eigenvectors with eigenvalue $1$, spanning the eigenspace of $1$.
>
> The four vectors $(\ell_+, \ell_-, e_2, e_3)$ form a basis ($\ell_+ + \ell_- = 2e_0$, $\ell_+ - \ell_- = 2e_1$ recover $e_0, e_1$), so $\Lambda$ is diagonalisable over $\mathbb{R}$ with spectrum $\{e^\psi, e^{-\psi}, 1, 1\}$. The eigenvectors $\ell_\pm$ are null.
>
> By Lemma 3, $e^{\pm\psi} = \sqrt{(1\pm V)/(1\mp V)}$ with $V = \tanh\psi$, the Doppler factors.
>
> Finally, summing the eigenvalues, $\mathrm{tr}\,\Lambda = e^\psi + e^{-\psi} + 1 + 1 = 2\cosh\psi + 2$, so $\cosh\psi = \tfrac12\mathrm{tr}\,\Lambda - 1$. (And $\det\Lambda = e^\psi e^{-\psi}\cdot 1\cdot 1 = 1$.) $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Squeeze operators in quantum optics.** A Lorentz boost in the $(\ell_+, \ell_-)$ basis is a *squeeze*: it stretches one quadrature by $e^\psi$ and shrinks the conjugate by $e^{-\psi}$, preserving their product (area). This is exactly the squeeze operator $S(\psi)$ of quantum optics, which reduces the noise in one quadrature of light at the expense of the other. The application is to recognise the boost eigenstructure as the classical skeleton of squeezed light, with rapidity the squeeze parameter; it is out-of-distribution because optical squeezing and Lorentz boosts are rarely connected.

**Hyperbolic dynamics and Anosov maps.** A linear map of the plane with real eigenvalues $\lambda, \lambda^{-1}$ ($\lambda > 1$) on transverse directions is the prototype of a *hyperbolic* (Anosov) dynamical system — it has a stretching (unstable) direction and a shrinking (stable) direction, the two null directions of the boost. The cat map of dynamics is such a transformation. The application battle-tests the "real reciprocal eigenvalues = stable/unstable directions" pattern, which underlies chaos theory and the stable-manifold theorem.

**The Lorentz transformation as a Bogoliubov transformation.** In quantum field theory, a Bogoliubov transformation mixes creation and annihilation operators by $\cosh\psi, \sinh\psi$ coefficients, exactly the boost matrix, and its eigenvalues $e^{\pm\psi}$ govern particle creation by accelerated observers (the Unruh effect) and by expanding spacetimes. The application connects the boost eigenstructure to the thermal radiation seen by an accelerated detector, where the rapidity sets the temperature; it is surprising that the eigenvalues of a $2\times 2$ boost matrix control quantum particle production.

---

# Bridges

- **[[Def - Classification of Restricted Lorentz Transformations]]** — this theorem supplies the spectral fingerprint that distinguishes the types: a boost has real eigenvalues on null eigenvectors, a rotation complex unimodular ones, a null rotation a single defective eigenvalue $1$. The eigenvalue computation is the fast route to deciding which type a given restricted transformation is, complementing the geometric (invariant-plane) classification.

- **[[Def - Rapidity|Rapidity and the Doppler factor]]** — the eigenvalues $e^{\pm\psi}$ are literally the relativistic Doppler factors, so this theorem is the bridge between the abstract additive parameter (rapidity) and the observable frequency shift. The rapidity is the logarithm of the Doppler factor, which is why rapidities add for collinear boosts exactly as Doppler factors multiply.

- **The asymptotes of a hyperbola** — the null eigenvectors $\ell_\pm$ are the asymptotes of the hyperbolas $t^2 - x^2 = \text{const}$ along which a boost slides points, and a boost fixes these asymptote directions while sliding along them, the way a Euclidean rotation fixes the centre of its circles while sliding along them. The whole theorem is the statement that a hyperbolic rotation scales its asymptotes by reciprocal factors, the relativistic counterpart of a Euclidean rotation having no real invariant directions at all.

---

# Unlocked by This

> [!tip] The Unruh Effect and Bogoliubov Transformations *(from quantum field theory in curved spacetime)*
> The boost eigenvalues $e^{\pm\psi}$ reappear as the **Bogoliubov coefficients** relating the particle modes of an inertial observer to those of a uniformly accelerated (Rindler) observer. Because a boost stretches one null direction and shrinks the other, the vacuum of one observer is a thermal state of particles for the other — the **Unruh effect** — with temperature $T = a/2\pi$ set by the acceleration, equivalently by the rate of change of rapidity. The same squeeze structure governs particle creation in an expanding universe and Hawking radiation from a black hole horizon. The humble observation that a boost has eigenvalues $e^{\pm\psi}$ on null directions is the linear-algebra seed of the deepest results connecting relativity, quantum theory, and thermodynamics.
