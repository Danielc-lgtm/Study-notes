---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Eigenvalues and Eigenvectors of a Lorentz Boost"
  - "Def - Boosts as Hyperbolic Rotations"
  - "Def - Rapidity"
tags: [physics, special-relativity]
---

# Problem Statement

Let $\Lambda$ be a boost of rapidity $\psi$ in the $(e_0, e_1)$-plane.

1. Diagonalise $\Lambda$ in the null basis $(\ell_+, \ell_-, e_2, e_3)$, with $\ell_\pm = e_0 \pm e_1$, finding the eigenvalues.
2. Show the two nontrivial eigenvalues are $\lambda_\pm = \sqrt{(1\pm V)/(1\mp V)}$ with $V = \tanh\psi$, and identify them as the relativistic longitudinal Doppler factors for light emitted along $\pm x$.
3. Contrast with a spatial rotation of angle $\theta$: show its eigenvalues are the *complex* unimodular $e^{\pm i\theta}$ on complex eigenvectors $e_2 \mp ie_3$, so a rotation has no real invariant directions in its plane, whereas a boost's eigenvectors are real and null.
4. A photon has frequency $f$ in a source frame and moves along $+x$. Use the eigenvalue $\lambda_-$ to find its observed frequency in a frame receding at speed $V$.

**Recall:**

![[Thm - Eigenvalues and Eigenvectors of a Lorentz Boost#Statement]]

The boost acts by $\Lambda(e_0) = \cosh\psi\,e_0 + \sinh\psi\,e_1$, $\Lambda(e_1) = \sinh\psi\,e_0 + \cosh\psi\,e_1$, and fixes $e_2, e_3$. The [[Def - Rapidity|rapidity]] satisfies $V = \tanh\psi$, $\cosh\psi = \Gamma = (1-V^2)^{-1/2}$, $\sinh\psi = \Gamma V$.

---

# Convergent Strategy

**Problem class.** A *spectral-computation* problem from the [[Special Relativity IX — The Lorentz Group, Structure and Classification#Problem-Solving Strategy|topic strategy]]: diagonalise a boost, identify its eigenvalues physically, and contrast its real null eigenstructure with the complex eigenstructure of a rotation.

**Assumption pattern.** The boost mixes only $e_0, e_1$, so its eigenstructure lives in the $(e_0,e_1)$-plane; the natural eigenbasis is the null basis $(\ell_+, \ell_-)$, the light-cone generators, because a hyperbolic rotation scales its asymptotes. The Doppler identification follows from $e^{\pm\psi} = \Gamma(1\pm V) = \sqrt{(1\pm V)/(1\mp V)}$.

**Theorem routing.** The computation routes through [[Thm - Eigenvalues and Eigenvectors of a Lorentz Boost|the boost-eigenvalue theorem]]: $\Lambda(\ell_\pm) = e^{\pm\psi}\ell_\pm$ on null eigenvectors, $\lambda_\pm = \sqrt{(1\pm V)/(1\mp V)}$ the Doppler factors. The rotation contrast routes through the observation that $\cos\theta, \sin\theta$ are bounded (real eigenvalues forbidden) versus $\cosh\psi, \sinh\psi$ unbounded (real null eigenvalues allowed).

**Key decision point.** The non-obvious choice is to diagonalise in the *null* basis, not the orthonormal basis. The boost has no eigenvectors among the orthonormal basis vectors $e_0, e_1$ (it moves both), but the null combinations $e_0\pm e_1$ are eigenvectors — these are the asymptotes of the boost's hyperbolas. The natural-but-wrong move is to try eigenvectors along the coordinate axes, which fails.

---

# Legal Operations Used

1. **Diagonalise in the null basis** (operation 9 from the topic page): change to $(\ell_+, \ell_-, e_2, e_3)$ where the boost is diagonal.

2. **The eigenvalues of a boost are Doppler factors** (most-reusable property): identify $e^{\pm\psi} = \sqrt{(1\pm V)/(1\mp V)}$ with the redshift/blueshift factors.

---

# Hints

> [!note]- Hint 1
> Apply $\Lambda$ to $\ell_+ = e_0 + e_1$ using the action on $e_0, e_1$, and collect: the result should be a multiple of $\ell_+$.

> [!note]- Hint 2
> $e^{\pm\psi} = \cosh\psi \pm \sinh\psi = \Gamma \pm \Gamma V = \Gamma(1\pm V)$. Then rationalise: $\Gamma(1\pm V) = (1\pm V)/\sqrt{(1-V)(1+V)} = \sqrt{(1\pm V)/(1\mp V)}$.

> [!note]- Hint 3
> For the rotation, solve $R(e_2\mp ie_3) = (\cos\theta \pm i\sin\theta)(e_2 \mp ie_3) = e^{\pm i\theta}(e_2\mp ie_3)$. These complex eigenvectors are not real directions, so a rotation fixes no real line in its plane (for $\theta \ne 0,\pi$).

> [!note]- Hint 4
> A photon emitted along $+x$ corresponds to the null direction $\ell_+$? or $\ell_-$? Light moving in $+x$ has worldline direction $(1,1,0,0) = \ell_+$ — but the *receding* observer sees it redshifted by $\lambda_-$. Track which null direction the photon's wavevector lies along and apply the corresponding eigenvalue.

---

# Solution

We diagonalise the boost (Step 1), make the Doppler identification (Step 2), contrast with the rotation (Step 3), and apply to a photon (Step 4).

**Step 1: Diagonalisation in the null basis.**

> [!note]- Derivation
> Apply the boost to $\ell_+ = e_0 + e_1$:
> $$\Lambda(\ell_+) = \Lambda(e_0) + \Lambda(e_1) = (\cosh\psi\,e_0 + \sinh\psi\,e_1) + (\sinh\psi\,e_0 + \cosh\psi\,e_1) = (\cosh\psi + \sinh\psi)(e_0 + e_1) = e^{\psi}\ell_+,$$
> using $\cosh\psi + \sinh\psi = e^\psi$. Symmetrically $\Lambda(\ell_-) = (\cosh\psi - \sinh\psi)(e_0 - e_1) = e^{-\psi}\ell_-$. And $\Lambda(e_2) = e_2$, $\Lambda(e_3) = e_3$. So in the basis $(\ell_+, \ell_-, e_2, e_3)$ the boost is diagonal: $\Lambda = \mathrm{diag}(e^\psi, e^{-\psi}, 1, 1)$. The eigenvectors $\ell_\pm$ are null: $\ell_\pm\cdot\ell_\pm = (e_0\pm e_1)\cdot(e_0\pm e_1) = 1 - 1 = 0$.

**Step 2: The eigenvalues are the Doppler factors.**

> [!note]- Derivation
> Write the eigenvalues in velocity variables:
> $$\lambda_\pm = e^{\pm\psi} = \cosh\psi \pm \sinh\psi = \Gamma \pm \Gamma V = \Gamma(1 \pm V).$$
> Since $\Gamma = (1-V^2)^{-1/2} = 1/\sqrt{(1-V)(1+V)}$,
> $$\lambda_\pm = \frac{1\pm V}{\sqrt{(1-V)(1+V)}} = \sqrt{\frac{(1\pm V)^2}{(1-V)(1+V)}} = \sqrt{\frac{1\pm V}{1\mp V}}.$$
> These are the relativistic longitudinal Doppler factors: $\lambda_+ = \sqrt{(1+V)/(1-V)} > 1$ is the **blueshift** factor (approaching source), $\lambda_- = \sqrt{(1-V)/(1+V)} < 1$ is the **redshift** factor (receding source). The boost stretches the light ray $\ell_+$ (blueshift) and shrinks $\ell_-$ (redshift). The rapidity is the logarithm of the Doppler factor: $\psi = \ln\lambda_+ = -\ln\lambda_-$.

**Step 3: Contrast with a spatial rotation.**

> [!note]- Derivation
> A rotation $R$ of angle $\theta$ in the $(e_2, e_3)$-plane acts by $R(e_2) = \cos\theta\,e_2 + \sin\theta\,e_3$, $R(e_3) = -\sin\theta\,e_2 + \cos\theta\,e_3$. Try the complex combination $e_2 \mp ie_3$:
> $$R(e_2 \mp ie_3) = (\cos\theta\,e_2 + \sin\theta\,e_3) \mp i(-\sin\theta\,e_2 + \cos\theta\,e_3) = (\cos\theta \pm i\sin\theta)e_2 + (\sin\theta \mp i\cos\theta)e_3.$$
> The second coefficient is $\sin\theta \mp i\cos\theta = \mp i(\cos\theta \pm i\sin\theta)$, so
> $$R(e_2 \mp ie_3) = (\cos\theta \pm i\sin\theta)(e_2 \mp ie_3) = e^{\pm i\theta}(e_2 \mp ie_3).$$
> The eigenvalues are $e^{\pm i\theta}$, *complex* unimodular, on *complex* eigenvectors $e_2 \mp ie_3$. For $\theta \ne 0, \pi$ these are not real, so the rotation fixes no real line in its plane — it genuinely rotates every real direction. The contrast with the boost is exact: the boost has real eigenvalues $e^{\pm\psi}$ on real null eigenvectors (the asymptotes of its hyperbolas), because $\cosh\psi, \sinh\psi$ are unbounded; the rotation has complex eigenvalues $e^{\pm i\theta}$ on complex eigenvectors, because $\cos\theta, \sin\theta$ are bounded and the circle has no real asymptotes. The minus sign in the metric turns the rotation's circle into the boost's hyperbola, and the complex eigenvectors into real null ones.

**Step 4: The photon's observed frequency.**

> [!note]- Derivation
> A photon moving along $+x$ has four-wavevector $K = (\omega, \omega, 0, 0) = \omega\,\ell_+$ in the source frame (with $f = \omega/2\pi$), lying along the null direction $\ell_+$. A frame receding at speed $V$ along $+x$ is reached by the boost $\Lambda$ of rapidity $\psi$ ($V = \tanh\psi$) — but to express the photon in the *receding* frame we apply the *inverse* boost (or equivalently note the frame moves with the photon). The component of $K$ along $\ell_+$ transforms by the eigenvalue: in the receding frame the photon's wavevector is $\Lambda^{-1}(K) = \omega\,\Lambda^{-1}(\ell_+) = \omega\,e^{-\psi}\ell_+ = \omega\sqrt{(1-V)/(1+V)}\,\ell_+$. So the observed angular frequency is
> $$\omega' = \omega\,e^{-\psi} = \omega\sqrt{\frac{1-V}{1+V}}, \qquad f' = f\sqrt{\frac{1-V}{1+V}} = f\,\lambda_-.$$
> The receding observer sees the photon **redshifted** by the factor $\lambda_- = \sqrt{(1-V)/(1+V)} < 1$, exactly the smaller boost eigenvalue. (An approaching observer, reached by the boost of rapidity $-\psi$, would see it blueshifted by $\lambda_+$.)

> [!note]- Complete formal solution
> In the null basis $(\ell_+, \ell_-, e_2, e_3)$ with $\ell_\pm = e_0\pm e_1$, the boost is diagonal: $\Lambda(\ell_\pm) = e^{\pm\psi}\ell_\pm$ (from $\cosh\psi\pm\sinh\psi = e^{\pm\psi}$), $\Lambda(e_2) = e_2$, $\Lambda(e_3) = e_3$. The eigenvectors $\ell_\pm$ are null. The eigenvalues $e^{\pm\psi} = \Gamma(1\pm V) = \sqrt{(1\pm V)/(1\mp V)}$ are the Doppler blueshift/redshift factors. A rotation, by contrast, has $R(e_2\mp ie_3) = e^{\pm i\theta}(e_2\mp ie_3)$, complex eigenvalues on complex eigenvectors, no real invariant line. A photon along $+x$ (wavevector $\omega\ell_+$) seen by a frame receding at $V$ has frequency $f' = f\,e^{-\psi} = f\sqrt{(1-V)/(1+V)}$, redshifted by $\lambda_-$. $\blacksquare$

---

# Key Takeaways

**A boost diagonalises in the null basis because a hyperbolic rotation scales its asymptotes.** The eigenvectors of a boost are the light-cone generators $\ell_\pm = e_0\pm e_1$, not the coordinate axes — because a boost slides points along hyperbolas, and the asymptotes of those hyperbolas are the invariant directions, scaled by reciprocal factors $e^{\pm\psi}$. This is the relativistic counterpart of a Euclidean rotation having *no* real invariant directions (its eigenvectors are complex). The trigger "diagonalise a boost" should immediately fire "use the null basis $\ell_\pm = e_0\pm e_1$," because the boost is diagonal there with the Doppler eigenvalues. The deeper pattern: whenever a transformation slides along a one-parameter family of curves, its eigen-directions are the invariant curves' asymptotes or centres.

**The rapidity is the logarithm of the Doppler shift, which is why rapidities add as Doppler factors multiply.** The eigenvalues $e^{\pm\psi}$ are literally the Doppler factors $\sqrt{(1\pm V)/(1\mp V)}$, so $\psi = \ln\lambda_+$ is the log of the blueshift. This makes the additivity of rapidity for collinear boosts the *multiplicativity* of Doppler factors: composing two boosts multiplies their stretch factors on $\ell_+$, $e^{\psi_1}e^{\psi_2} = e^{\psi_1+\psi_2}$, which is the eigenvalue statement of "rapidities add." The reusable insight: to compose collinear boosts, multiply their Doppler factors (or add their rapidities); to find a single boost's rapidity from data, take the log of the observed Doppler shift. This turns the abstract additive parameter into a directly measurable quantity.

**Real eigenvalues on null vectors versus complex eigenvalues on complex vectors is the spectral fingerprint distinguishing boosts from rotations.** A boost has real positive eigenvalues $e^{\pm\psi}$ on real null eigenvectors; a rotation has complex unimodular eigenvalues $e^{\pm i\theta}$ on complex eigenvectors; and (from the null-rotation analysis) a null rotation has a single eigenvalue $1$ with a defective Jordan block. Computing the spectrum thus classifies the type immediately. The trigger "what type is this restricted transformation" can be answered by "diagonalise and look at the eigenvalues": real and $\ne 1$ on null directions means boost, complex unimodular means rotation, a single $1$ with no full eigenbasis means null rotation. The boundedness of $\cos, \sin$ versus the unboundedness of $\cosh, \sinh$ — ultimately the sign of the metric — is the reason for the real-versus-complex dichotomy.
