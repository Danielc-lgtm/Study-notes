---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Regularized Least Squares"
  - "Def - Validation (Training and Test Error)"
tags: [algebra, linear-algebra, applied, statistics, machine-learning]
---

# Notation

For Tikhonov regularization $\hat{x}(\lambda) = (A^T A + \lambda I)^{-1} A^T b$, the *bias* (under a data-generating model $b = A x^* + \epsilon$ with $\mathbb{E}[\epsilon] = 0$, $\mathrm{Cov}(\epsilon) = \sigma^2 I$) is $\mathbb{E}[\hat{x}(\lambda)] - x^*$. The *variance* is $\mathbb{E}\|\hat{x}(\lambda) - \mathbb{E}[\hat{x}(\lambda)]\|^2$. The *mean squared error* (MSE) is $\mathbb{E}\|\hat{x}(\lambda) - x^*\|^2 = \|\mathrm{bias}\|^2 + \mathrm{variance}$. The optimal $\lambda^*$ minimizes MSE.

The SVD of $A$ is $A = U \Sigma V^T$ with singular values $\sigma_1 \geq \cdots \geq \sigma_n \geq 0$.

---

# Statement

> **Theorem (Bias-Variance Tradeoff in Regularized LS).** Suppose $b = A x^* + \epsilon$ where $x^* \in \mathbb{R}^n$ is the true parameter, $\epsilon \in \mathbb{R}^m$ is mean-zero noise with covariance $\sigma^2 I$, and $A$ has SVD $A = U \Sigma V^T$. Then the Tikhonov regularized LS solution $\hat{x}(\lambda) = (A^T A + \lambda I)^{-1} A^T b$ satisfies:
> 1. *Bias*:
> $$\mathbb{E}[\hat{x}(\lambda)] - x^* = -\lambda \left(A^T A + \lambda I\right)^{-1} x^* = -V D_\lambda^{\text{bias}} V^T x^*,$$
> where $D_\lambda^{\text{bias}} = \mathrm{diag}\big(\lambda/(\sigma_i^2 + \lambda)\big)$. Bias is zero when $\lambda = 0$ (no regularization) and goes to $-x^*$ (full shrinkage to zero) as $\lambda \to \infty$.
> 2. *Variance*:
> $$\mathrm{Var}(\hat{x}(\lambda)) = \sigma^2 \cdot \mathrm{tr}\!\left((A^T A + \lambda I)^{-2} A^T A\right) = \sigma^2 \sum_i \frac{\sigma_i^2}{(\sigma_i^2 + \lambda)^2}.$$
> Variance decreases monotonically with $\lambda$.
> 3. *Mean squared error*:
> $$\mathrm{MSE}(\lambda) = \mathbb{E}\|\hat{x}(\lambda) - x^*\|^2 = \lambda^2 \sum_i \frac{(v_i^T x^*)^2}{(\sigma_i^2 + \lambda)^2} + \sigma^2 \sum_i \frac{\sigma_i^2}{(\sigma_i^2 + \lambda)^2},$$
> where $v_i$ are the columns of $V$. The MSE has a strict minimum at some $\lambda^* > 0$ (assuming the noise is nonzero), at which the gain from variance reduction balances the cost of bias introduction.
> 4. *Existence of an MSE-optimal $\lambda > 0$*: For $\sigma^2 > 0$, $\frac{d \mathrm{MSE}}{d\lambda} |_{\lambda = 0} < 0$, so $\mathrm{MSE}(\lambda)$ is strictly decreasing at $\lambda = 0$. Hence there exists $\lambda^* > 0$ where $\mathrm{MSE}(\lambda^*) < \mathrm{MSE}(0)$ — *regularization strictly reduces MSE* compared to ordinary LS.

---

# Motivation

The bias-variance tradeoff is the deepest and most operationally useful insight about regularized LS. It says: introducing a small amount of regularization is *always* better than no regularization, in the sense of minimizing expected squared error to the true parameter. The "best $\lambda$" is the one that optimally trades the bias (which grows with $\lambda$) against the variance (which shrinks with $\lambda$).

Without this theorem, regularization could look like an arbitrary trick: why penalize the parameter norm at all? With this theorem, regularization is *forced* by the statistical structure: any unbiased estimator with positive variance can be improved (in MSE sense) by introducing a small bias toward zero. The theorem is the precise mathematical statement of this "shrinkage estimators dominate unbiased ones" principle (Stein's paradox).

The deeper conceptual content is twofold.

First, *the optimal $\lambda^*$ depends on $x^*$ and $\sigma^2$ — quantities we don't know.* The theorem gives the form of the MSE as a function of $\lambda$, but minimizing it requires the true parameter $x^*$ and noise variance $\sigma^2$, which are not observable. In practice, $\lambda$ is chosen by cross-validation, which estimates the MSE empirically without needing $x^*$.

Second, *the Bayesian interpretation is exact*. Under Gaussian noise + Gaussian prior on $x$, the MAP estimator is the Tikhonov solution with $\lambda = \sigma^2/\tau^2$ (noise/prior variance ratio). The "optimal $\lambda$" — minimizing MSE under the prior — coincides with the MSE-optimal $\lambda$ when averaged over $x^*$'s drawn from the prior. The bias-variance tradeoff is the *frequentist* face of the Bayesian shrinkage estimator; both perspectives lead to the same recommendation: regularize.

The role of the theorem: it elevates regularization from an empirical trick to a principled optimization, and it provides the diagnostic for the canonical training/test error U-shape.

---

# Sources and Targets

**Sources (input broadening)**

The theorem requires a noise model $b = A x^* + \epsilon$ with $\mathbb{E}[\epsilon] = 0, \mathrm{Cov}(\epsilon) = \sigma^2 I$. Non-obvious bridges:

*Source 1: Heteroscedastic noise.* If the noise covariance is $\mathrm{Cov}(\epsilon) = \Sigma_\epsilon$ (not isotropic), the bias-variance tradeoff still holds, but with $\sigma^2 I$ replaced by $\Sigma_\epsilon$. The optimal regularization is then $\Sigma_\epsilon^{-1}$-weighted: weight the data fidelity by the inverse covariance to whiten the noise. *Example use*: weighted least squares with non-uniform measurement uncertainties; the optimal weight matrix is $\Sigma_\epsilon^{-1}$.

*Source 2: Correlated noise across samples.* If samples have correlated errors (e.g., from a temporal or spatial dependence structure), the simple isotropic assumption fails, but a generalized least squares with the appropriate noise-covariance correction recovers the same bias-variance picture.

*Source 3: Robust regression.* If the noise has heavy tails (large outliers), the squared-loss MSE is dominated by outliers, and the "optimal $\lambda$" becomes very large to shrink the model away from outlier influence. This motivates robust losses (Huber, absolute-value) that give smaller "effective $\lambda$" requirements.

**Targets (output amplification)**

The theorem gives a quantitative trade-off + the existence of an optimal $\lambda$. Non-obvious uses:

*Target 1 (Bayes-rule equivalence).* The MSE-optimal $\lambda^*$ averaged over $x^* \sim \mathcal{N}(0, \tau^2 I)$ is exactly $\sigma^2/\tau^2$ — the Bayesian noise-to-prior precision ratio. This is the celebrated *empirical Bayes* identification: cross-validating for $\lambda$ in regularized LS is empirically estimating the Bayes-rule shrinkage. *Example use*: hyperparameter tuning in Gaussian process regression via empirical Bayes (maximum marginal likelihood), recovering optimal kernel parameters.

*Target 2 (degrees-of-freedom).* The *effective degrees of freedom* of a regularized LS fit is $\mathrm{df}(\lambda) = \mathrm{tr}\!\left(A (A^T A + \lambda I)^{-1} A^T\right) = \sum_i \sigma_i^2/(\sigma_i^2 + \lambda)$. As $\lambda \to 0$, this approaches the rank of $A$ (full-rank model uses all degrees of freedom); as $\lambda \to \infty$, it approaches zero (full shrinkage). The MSE-optimal $\lambda^*$ is at the degrees-of-freedom where additional model complexity stops helping. *Example use*: Mallows' $C_p$ statistic for model selection, which directly uses degrees-of-freedom.

*Target 3 (information-theoretic justification).* The *minimum description length* (MDL) principle prefers shorter models. The MDL-optimal model length in linear regression coincides (approximately) with the Tikhonov-optimal $\lambda^*$. This makes regularization an information-theoretic shadow of the bias-variance tradeoff. *Example use*: model selection in linguistics (Bayesian information criterion, BIC, derives from MDL), in compression-based statistics.

---

# Why Is It True

**The mechanism in one sentence: introducing a small $\lambda$ creates first-order bias proportional to $\lambda$ but reduces variance by order $\lambda$, with the variance reduction dominating for small $\lambda$ — so the second-order MSE decreases.**

The intuitive picture is the SVD-based filtering. The unregularized LS solution is $\hat{x}(0) = V \Sigma^{-1} U^T b$, which divides each singular component by its singular value. Small singular values (corresponding to nearly-collinear directions in feature space) amplify noise: noise component $u_i^T \epsilon$ is amplified by $1/\sigma_i$. For very small $\sigma_i$, this amplification can be huge, blowing up the variance of $\hat{x}$.

The Tikhonov solution replaces $1/\sigma_i$ with $\sigma_i/(\sigma_i^2 + \lambda)$, which is *bounded* (the maximum is $1/(2\sqrt{\lambda})$ at $\sigma_i = \sqrt{\lambda}$) and goes to zero for very small $\sigma_i$. So Tikhonov *filters out* the noise-amplifying small-singular-value components, at the cost of also slightly attenuating the signal in those components. The trade-off: less noise (good) vs. slight signal attenuation (bad). For small $\lambda$, the noise reduction dominates.

Quantitatively: the variance reduction at small $\lambda$ is $O(\lambda)$, while the bias introduction is $O(\lambda)$ in each parameter. Squared bias is $O(\lambda^2)$, smaller than the variance reduction at first order. So the *net* MSE change at $\lambda = 0$ is negative — MSE strictly decreases as we move $\lambda$ away from 0.

The deeper story is the *Stein paradox*: in dimension $\geq 3$, the maximum-likelihood estimator (which is ordinary LS for Gaussian noise) is *inadmissible* — there exists a better estimator with strictly lower MSE everywhere. The James-Stein estimator and Tikhonov are two examples; both are *shrinkage* estimators that trade bias for variance reduction. This is one of the most counterintuitive results in classical statistics, and it is the deeper justification for why regularization is *always* a good idea (in dimension $\geq 3$).

---

# What Makes This Hard

The hard step is the *SVD-based decomposition* of the MSE. Most students are comfortable with the formula $\hat{x}(\lambda) = (A^T A + \lambda I)^{-1} A^T b$ but find it opaque. Expanding via the SVD $A = U \Sigma V^T$ gives:
$$\hat{x}(\lambda) = V \mathrm{diag}\!\left(\frac{\sigma_i}{\sigma_i^2 + \lambda}\right) U^T b,$$
which makes both the bias and variance transparent — each singular component is filtered by the factor $\sigma_i/(\sigma_i^2 + \lambda)$. The MSE is the sum of squared filtered-noise contributions plus squared signal-attenuation contributions, both expressed in singular-value coordinates.

A secondary difficulty: the optimal $\lambda^*$ depends on unknown quantities ($x^*$, $\sigma^2$). The *theorem* says an optimal $\lambda^*$ exists; the *practice* uses cross-validation to estimate it. Many students miss this distinction.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use the SVD $A = U \Sigma V^T$ to diagonalize the problem. Express $\hat{x}(\lambda)$, bias, variance, and MSE in singular-value coordinates. Compute the derivative of MSE with respect to $\lambda$ at $\lambda = 0$ to show that MSE strictly decreases.

**Subgoal decomposition:**

1. **SVD expansion of $\hat{x}(\lambda)$.** Use $A = U \Sigma V^T$ to write $\hat{x}(\lambda) = V D_\lambda U^T b$ for some diagonal $D_\lambda$.
   - *Hint:* $A^T A + \lambda I = V (\Sigma^2 + \lambda I) V^T$, so $(A^T A + \lambda I)^{-1} = V (\Sigma^2 + \lambda I)^{-1} V^T$.
   - *Why needed:* Diagonalizes the regularized solution.

2. **Bias and variance formulas.** Substitute $b = A x^* + \epsilon$ and take expectations.
   - *Hint:* $\mathbb{E}[\hat{x}(\lambda)] = V D_\lambda U^T A x^* = V D_\lambda \Sigma V^T x^*$; subtract $x^*$ and simplify.
   - *Why needed:* Quantifies bias and variance.

3. **MSE decomposition.** Combine bias squared and variance.
   - *Hint:* MSE $= \|$bias$\|^2 + $ variance $= \sum_i \big(\text{singular component of bias}\big)^2 + \sum_i \big(\text{singular component of variance}\big)$.
   - *Why needed:* Combines into a single tractable formula.

4. **Derivative at $\lambda = 0$.** Compute $\frac{d \mathrm{MSE}}{d\lambda} |_{\lambda = 0}$ and show it is negative.
   - *Hint:* Differentiate the MSE formula and evaluate at $\lambda = 0$. The bias term contributes 0 at $\lambda = 0$ (no bias when no regularization); the variance term contributes the dominant negative term.
   - *Why needed:* Establishes existence of an MSE-optimal $\lambda^* > 0$.

---

# Lemma Decomposition

> [!note]- Lemma 1: SVD expansion of the Tikhonov solution.
> **Statement:** Let $A = U \Sigma V^T$ be the SVD of $A$. Then $\hat{x}(\lambda) = V \cdot \mathrm{diag}\!\left(\frac{\sigma_i}{\sigma_i^2 + \lambda}\right) \cdot U^T b$.
>
> **Hint:** Substitute the SVD into the Tikhonov formula and simplify.
>
> **Why needed:** Diagonalizes the problem in singular-value coordinates, making all subsequent computations straightforward.
>
> > [!note]- Full proof
> > $A^T A = V \Sigma^2 V^T$. Hence $A^T A + \lambda I = V (\Sigma^2 + \lambda I) V^T$. The inverse is $V (\Sigma^2 + \lambda I)^{-1} V^T$. The right-hand side $A^T b = V \Sigma U^T b$. Multiplying:
> > $$\hat{x}(\lambda) = V (\Sigma^2 + \lambda I)^{-1} V^T V \Sigma U^T b = V (\Sigma^2 + \lambda I)^{-1} \Sigma U^T b = V \cdot \mathrm{diag}\!\left(\frac{\sigma_i}{\sigma_i^2 + \lambda}\right) \cdot U^T b.$$

> [!note]- Lemma 2: Bias formula.
> **Statement:** $\mathbb{E}[\hat{x}(\lambda)] - x^* = -V \mathrm{diag}\!\left(\frac{\lambda}{\sigma_i^2 + \lambda}\right) V^T x^*$.
>
> **Hint:** Use $b = A x^* + \epsilon$, take expectations, and apply Lemma 1.
>
> **Why needed:** Quantifies the bias as a function of $\lambda$ and the true parameter $x^*$.
>
> > [!note]- Full proof
> > $\mathbb{E}[\hat{x}(\lambda)] = V \mathrm{diag}\!\left(\frac{\sigma_i}{\sigma_i^2 + \lambda}\right) U^T \mathbb{E}[b] = V \mathrm{diag}\!\left(\frac{\sigma_i}{\sigma_i^2 + \lambda}\right) U^T A x^* = V \mathrm{diag}\!\left(\frac{\sigma_i^2}{\sigma_i^2 + \lambda}\right) V^T x^*$, using $U^T A = U^T U \Sigma V^T = \Sigma V^T$.
> > 
> > So $\mathbb{E}[\hat{x}(\lambda)] - x^* = V \mathrm{diag}\!\left(\frac{\sigma_i^2}{\sigma_i^2 + \lambda} - 1\right) V^T x^* = -V \mathrm{diag}\!\left(\frac{\lambda}{\sigma_i^2 + \lambda}\right) V^T x^*$.

> [!note]- Lemma 3: Variance formula.
> **Statement:** $\mathrm{Cov}(\hat{x}(\lambda)) = \sigma^2 V \mathrm{diag}\!\left(\frac{\sigma_i^2}{(\sigma_i^2 + \lambda)^2}\right) V^T$, so $\mathrm{Var}(\hat{x}(\lambda)) = \sigma^2 \sum_i \frac{\sigma_i^2}{(\sigma_i^2 + \lambda)^2}$.
>
> **Hint:** Use $\hat{x}(\lambda) - \mathbb{E}[\hat{x}(\lambda)] = V \mathrm{diag}\!\left(\frac{\sigma_i}{\sigma_i^2 + \lambda}\right) U^T \epsilon$ and apply the covariance computation.
>
> **Why needed:** Quantifies the variance as a function of $\lambda$ and the noise level $\sigma^2$.
>
> > [!note]- Full proof
> > $\hat{x}(\lambda) - \mathbb{E}[\hat{x}(\lambda)] = V \mathrm{diag}\!\left(\frac{\sigma_i}{\sigma_i^2 + \lambda}\right) U^T \epsilon$. The covariance is
> > $\mathrm{Cov}(\hat{x}(\lambda)) = V D U^T \mathrm{Cov}(\epsilon) U D V^T = \sigma^2 V D U^T U D V^T = \sigma^2 V D^2 V^T$,
> > where $D = \mathrm{diag}(\sigma_i/(\sigma_i^2 + \lambda))$. So $\mathrm{Cov}(\hat{x}(\lambda)) = \sigma^2 V \mathrm{diag}(\sigma_i^2/(\sigma_i^2 + \lambda)^2) V^T$, and the total variance (sum of diagonal) is $\sigma^2 \sum_i \sigma_i^2/(\sigma_i^2 + \lambda)^2$.

> [!note]- Lemma 4: Derivative of MSE at $\lambda = 0$ is negative.
> **Statement:** $\frac{d \mathrm{MSE}}{d\lambda}|_{\lambda = 0} = -2 \sigma^2 \sum_i \sigma_i^{-2}$ (assuming $A$ has full column rank, so all $\sigma_i > 0$).
>
> **Hint:** Differentiate the MSE formula term-by-term and evaluate at $\lambda = 0$. The bias term contributes zero (at $\lambda = 0$); the variance term contributes the dominant negative term.
>
> **Why needed:** Strict negativity at $\lambda = 0$ implies $\mathrm{MSE}(\lambda)$ is strictly decreasing near $\lambda = 0$, so there is some $\lambda^* > 0$ with $\mathrm{MSE}(\lambda^*) < \mathrm{MSE}(0)$.
>
> > [!note]- Full proof
> > $\mathrm{MSE}(\lambda) = \lambda^2 \sum_i (v_i^T x^*)^2 / (\sigma_i^2 + \lambda)^2 + \sigma^2 \sum_i \sigma_i^2 / (\sigma_i^2 + \lambda)^2$.
> > 
> > Differentiating each $\sigma_i$ term: $\frac{d}{d\lambda} \frac{\lambda^2}{(\sigma_i^2 + \lambda)^2} = \frac{2 \lambda (\sigma_i^2 + \lambda) - 2 \lambda^2}{(\sigma_i^2 + \lambda)^3} \big|_{\lambda = 0} = 0$. So the bias term has zero derivative at $\lambda = 0$.
> >
> > For the variance term: $\frac{d}{d\lambda} \frac{\sigma_i^2}{(\sigma_i^2 + \lambda)^2} = -2 \sigma_i^2/(\sigma_i^2 + \lambda)^3 \big|_{\lambda = 0} = -2/\sigma_i^4$. So the derivative at $\lambda = 0$ is $-2 \sigma^2 \sum_i 1/\sigma_i^2 < 0$ (provided $\sigma^2 > 0$ and $A$ has full column rank).

---

# Formal Proof

> [!note]- Complete formal proof
> *Step 1: SVD expansion.* By Lemma 1, $\hat{x}(\lambda) = V \mathrm{diag}(\sigma_i/(\sigma_i^2 + \lambda)) U^T b$.
>
> *Step 2: Bias.* By Lemma 2, $\mathbb{E}[\hat{x}(\lambda)] - x^* = -V \mathrm{diag}(\lambda/(\sigma_i^2 + \lambda)) V^T x^*$. The squared bias norm is
> $$\|\mathbb{E}[\hat{x}(\lambda)] - x^*\|^2 = \lambda^2 \sum_i \frac{(v_i^T x^*)^2}{(\sigma_i^2 + \lambda)^2}.$$
>
> *Step 3: Variance.* By Lemma 3, $\mathrm{Var}(\hat{x}(\lambda)) = \sigma^2 \sum_i \sigma_i^2/(\sigma_i^2 + \lambda)^2$.
>
> *Step 4: MSE decomposition.* Adding squared bias and variance:
> $$\mathrm{MSE}(\lambda) = \lambda^2 \sum_i \frac{(v_i^T x^*)^2}{(\sigma_i^2 + \lambda)^2} + \sigma^2 \sum_i \frac{\sigma_i^2}{(\sigma_i^2 + \lambda)^2}.$$
>
> *Step 5: Existence of MSE-optimal $\lambda^* > 0$.* By Lemma 4, $\frac{d \mathrm{MSE}}{d\lambda}|_{\lambda = 0} = -2 \sigma^2 \sum_i 1/\sigma_i^2 < 0$ (assuming $\sigma^2 > 0$ and full column rank of $A$). So $\mathrm{MSE}(\lambda)$ is strictly decreasing at $\lambda = 0$. As $\lambda \to \infty$, $\mathrm{MSE}(\lambda) \to \|x^*\|^2 + 0 = \|x^*\|^2 < \infty$ (the bias term saturates and the variance term goes to zero). So $\mathrm{MSE}$ takes some minimum value strictly less than $\mathrm{MSE}(0)$, attained at some $\lambda^* > 0$.

---

# Cross-Field Exercise Suggestions

*Suggestion 1 (Bayesian Statistics — empirical Bayes):* The MSE-optimal $\lambda^*$ averaged over $x^* \sim \mathcal{N}(0, \tau^2 I)$ is exactly $\sigma^2/\tau^2$ — the Bayes shrinkage. Cross-validation empirically estimates $\lambda^*$ without needing to specify $\tau$, recovering the empirical Bayes hyperparameter. Apply this theorem to derive the equivalence and to interpret cross-validated $\lambda$ values as empirical estimates of the noise-to-prior precision ratio.

*Suggestion 2 (Information Theory — minimum description length):* The MDL principle minimizes a combined cost of "model complexity" (penalty) and "data given model" (fit error). For linear regression, this is mathematically equivalent to regularized LS with a particular $\lambda$. Derive the optimal MDL penalty for linear models and verify that it matches the MSE-optimal Tikhonov $\lambda^*$ asymptotically.

*Suggestion 3 (Random Matrix Theory — effective rank):* The effective degrees of freedom $\mathrm{df}(\lambda) = \sum_i \sigma_i^2/(\sigma_i^2 + \lambda)$ has a connection to *random matrix theory*: for large random matrices with Marchenko-Pastur distribution of singular values, $\mathrm{df}(\lambda^*)$ scales predictably with the noise level and the matrix aspect ratio. Apply this theorem to derive scaling laws for the MSE-optimal regularization in high-dimensional regression.

---

# Bridges

- **Bayesian Linear Regression** — Tikhonov regularization is the MAP estimator under a Gaussian prior, with $\lambda = \sigma^2/\tau^2$. The bias-variance tradeoff is the frequentist face of the Bayesian shrinkage. Both perspectives agree that some positive regularization is always better than none.

- **Stein's Paradox** — In dimension $\geq 3$, the ordinary LS estimator is *inadmissible* — there exists a (shrinkage) estimator that strictly dominates it in MSE everywhere. The James-Stein estimator and Tikhonov are two such shrinkage estimators. This is one of the most counterintuitive results in classical statistics.

- **Cross-Validation** — In practice, $\lambda^*$ is chosen by cross-validation, which estimates the MSE empirically. The CV-optimal $\lambda$ is a consistent estimator of the MSE-optimal $\lambda^*$ as the sample size grows.

- **Mallows' $C_p$ Statistic** — A model-selection criterion that combines training error with a penalty proportional to the effective degrees of freedom. For Tikhonov, $C_p$ recommends the same $\lambda^*$ as MSE minimization, providing a direct (non-CV) computation of the optimal regularization.

---

# Unlocked by This

> [!tip] Bayesian Information Criterion *(from Statistics)*
> The **BIC** is a model-selection criterion derived from Bayesian model comparison, with a penalty $\frac{1}{2} k \log N$ where $k$ is the number of parameters and $N$ is the sample size. For regularized LS, BIC selects models with effective degrees of freedom matching this penalty. The connection to bias-variance: BIC implicitly favors models with low variance (few effective parameters), consistent with the MSE-optimal Tikhonov $\lambda$ for typical sample sizes.

> [!tip] Generalization Error Bounds *(from Statistical Learning Theory)*
> The bias-variance decomposition is one of two main routes (the other being PAC bounds and VC dimension) to *non-asymptotic* generalization-error bounds. The bias-variance route requires distributional assumptions but gives sharp constants; the PAC route is distribution-free but typically loose. Modern learning theory uses both, depending on whether you want tight constants or robust guarantees.

> [!tip] Double Descent in Modern Machine Learning *(from Deep Learning Theory)*
> Classical bias-variance theory predicts a U-shaped test error as a function of model complexity. **Modern deep learning** exhibits a richer phenomenon: as model size grows past the interpolation threshold (where the model can fit the training data exactly), test error first rises (classical overfitting) and then *decreases* again — the *double-descent* curve. This is a fundamental departure from the classical bias-variance picture and is an active research area; it suggests that the simple "bias up, variance down" story does not capture overparameterized models.
