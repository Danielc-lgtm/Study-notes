---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Least Squares Data Fitting"
  - "Def - Validation (Training and Test Error)"
tags: [algebra, linear-algebra, applied, data-fitting, machine-learning]
---

# Notation

A *raw feature vector* is $x \in \mathbb{R}^n$ as observed. *Engineered features* are derived from $x$ via transformations $g_1, g_2, \ldots$ each producing one new scalar feature. The engineered feature vector is $\tilde{x} = (g_1(x), g_2(x), \ldots, g_p(x))$, of dimension $p$ (often $p \gg n$). The model in the engineered representation is $\hat{f}(x) = \theta^T \tilde{x}$, which is *nonlinear in $x$* but *linear in the parameters $\theta$* — the design that makes least squares applicable.

---

# Axiom Motivation

You have raw data — feature vectors $x \in \mathbb{R}^n$ — and you want to fit a model that predicts an outcome $y$. The raw features may not be in the form the model needs. For example: the raw feature "ZIP code" is a 5-digit integer, but the relationship between ZIP code and house price is *not linear* — the difference between ZIP codes 90210 and 95014 is not "meaningful" in any numerical sense. The raw feature "number of bedrooms" *is* numerical, but the price increase from 1 to 2 bedrooms is not the same as from 4 to 5 bedrooms — so a linear-in-this-feature model is mis-specified. The raw feature "house area" is genuinely numerical and roughly linear in price, but the linearity breaks at very large areas (luxury properties price differently from mid-market).

Feature engineering is the (often domain-specific) process of *transforming* the raw features into a form where a linear-in-parameters model can do well. It is the human art that determines whether least squares data fitting will succeed or fail; it is also the deepest source of inductive bias in non-deep-learning ML systems.

The canonical operations are:

*One-hot encoding of categoricals.* A categorical variable with $K$ levels — like ZIP code — is replaced by $K$ Boolean features, each indicating whether the data point falls in that level. The model then learns a *separate* coefficient for each level, with no assumed numerical relationship between them. Often a baseline level is omitted (to avoid linear dependence with the intercept term), giving $K-1$ Boolean features.

*Piecewise-linear (or piecewise-anything) basis.* A continuous feature is augmented with "knot" functions like $\min\{x - a, 0\}$ or $\max\{x - b, 0\}$. These let the model fit a *piecewise-linear* relationship with kinks at $a$ and $b$. This is the simplest way to capture saturation or nonlinear thresholding effects (above $b$ units of area, additional area is worth less).

*Polynomials, sinusoids, and other parametric bases.* When the underlying relationship is suspected to be smooth, polynomial basis functions $1, x, x^2, \ldots, x^d$ capture polynomial relationships; sinusoidal bases capture periodicity (seasonal, diurnal); exponential bases capture saturating growth. Choice of basis is a *prior* on what the relationship is expected to look like.

*Interaction terms.* The features $x_i x_j$ (pairwise products) capture the joint effect of features $i$ and $j$ beyond their individual effects. This is essential when the relationship between $y$ and $x_i$ depends on the value of $x_j$ — for example, "the effect of a medication may depend on patient age." Without interaction terms, a linear model cannot capture this.

*Stratified models.* When a categorical variable strongly modulates the entire relationship between other features and the outcome (e.g., male vs. female patients having entirely different risk profiles), it can be more efficient to fit *separate* models per stratum than to add many interaction terms.

*Custom domain transformations.* In finance, the price-to-earnings ratio (a derived feature from price and earnings) often predicts better than either raw feature alone. In NLP, the TFIDF score for a word (raw count weighted by document frequency) outperforms raw count. These are problem-specific compressions of raw data into informative scalars; they encode domain expertise.

*Random and learned features.* At the limit of "feature engineering": rather than design features by hand, generate random feature transformations (e.g., $(Rx)_+$ for random matrix $R$ and ReLU activation) and stack many of them. With enough random features and sufficient data, this can outperform careful manual engineering — this is the underlying idea of *random feature kitchen-sink* methods and, ultimately, of neural networks.

The unifying principle is that *the model class is fixed at "linear in parameters"* — what changes is the feature representation. Two principles guide the choice:

(i) *Simplicity until proven otherwise.* Start with the rawest possible features; add transformations only when [[Def - Validation (Training and Test Error)|validation]] indicates that the simpler model is missing structure. The risk of adding features is overfitting (training error decreases but test error increases) and the only diagnostic is out-of-sample validation.

(ii) *Domain knowledge as inductive bias.* When you know a relationship is periodic, use sinusoidal basis functions. When you know it has a saturation point, use piecewise-linear with a knot. When you know it is monotonic but nonlinear, use logs or splines. The choice of basis functions *embeds* domain knowledge into the model in a way that pure data-fitting cannot recover.

The "feature engineering principle" is sometimes summarized as: with enough features, any predictor can do well on training; the art is choosing features that also help on test. [[Def - Validation (Training and Test Error)|Validation]] is the only way to evaluate this art.

---

# The Definition

> **Definition (Feature Engineering).** Given a raw feature vector $x \in \mathbb{R}^n$, *feature engineering* is the process of constructing transformed features $g_1(x), g_2(x), \ldots, g_p(x)$ — each a scalar function of (possibly) some or all of the raw features — and using the transformed vector $\tilde{x} = (g_1(x), \ldots, g_p(x))$ as input to a linear-in-parameters model
> $$\hat{f}(x) = \theta_1 g_1(x) + \cdots + \theta_p g_p(x).$$
> Common feature-engineering operations include:
> - **One-hot encoding** of categoricals: $g_k(x) = \mathbb{1}\{x = k\}$ for each category $k$.
> - **Piecewise-linear basis**: $g_k(x) = \max\{x_i - a_k, 0\}$ or $\min\{x_i + b_k, 0\}$ for knot points $a_k, b_k$.
> - **Polynomial basis**: $g_k(x) = x_i^k$ (for scalar $x_i$) or monomials in multiple coordinates.
> - **Interaction terms**: $g_k(x) = x_i x_j$ for pairs $(i, j)$.
> - **Custom transformations** (logs, ratios, domain-specific aggregations).
> - **Stratified models** (separate models per category, switched on a categorical).
> - **Random features**: $g_k(x) = \sigma(R_k^T x)$ for random matrix $R$ and nonlinearity $\sigma$.

The fitted model is then obtained by ordinary LS data fitting on the design matrix with engineered features.

---

# Relate to Other Fields / Compression

**True name:** feature engineering is *encoding inductive bias into the design matrix*. The Bayesian / ML reformulation is "choosing a parametric prior on what kind of function the predictor can be." A polynomial basis biases the model toward smooth polynomial relationships; a sinusoidal basis biases toward periodicity; a piecewise-linear basis biases toward functions with kinks at known locations.

This is the same construction as:
- **Kernel Methods** in ML: instead of explicitly engineering features, the kernel trick implicitly defines an inner product $K(x, x') = \langle \phi(x), \phi(x') \rangle$ in some feature space $\phi$ without ever computing $\phi$ explicitly. SVMs, kernel ridge regression, and Gaussian processes are all kernelized least squares with implicit features.
- **Spectral Methods** in PDE numerics: choosing Chebyshev polynomials or Fourier modes as basis functions is feature engineering for function approximation in $L^2$.
- **Neural Networks as Learned Features**: the early layers of a deep neural network can be interpreted as *learned* feature transformations $g_1, g_2, \ldots$ (themselves parametric), with the final layer being a linear-in-features classifier. Deep learning is then "feature engineering at scale, but learned from data."

---

# Examples / Corollaries

*Example 1 (one-hot encoding of ZIP code).* In house price prediction, the raw feature ZIP code (5-digit integer) is replaced by, say, four Boolean features encoding four neighborhood clusters. The model then has four parameters $\theta_{\text{ZIP1}}, \ldots, \theta_{\text{ZIP4}}$, each representing the price premium / discount for that cluster. Linear-in-this-encoding-features captures the categorical structure without falsely assuming numerical relationships between ZIP codes.

*Example 2 (piecewise-linear basis for area).* With raw feature $x_1$ = house area (1000 sq ft), augment with $g_3(x) = \max\{x_1 - 1.5, 0\}$. The model $\hat{y} = \theta_1 + \theta_2 x_1 + \theta_3 \max\{x_1 - 1.5, 0\}$ is piecewise linear: slope $\theta_2$ below 1500 sq ft, slope $\theta_2 + \theta_3$ above 1500 sq ft. The kink at 1.5 captures the empirical observation that very large houses have a different price/sqft relationship.

*Example 3 (interaction terms in medical regression).* When predicting disease risk from age and sex, include the interaction term $g(x) = \text{age} \cdot \mathbb{1}\{\text{male}\}$. The model can now learn different age effects for males vs. females, even though the base linearity-in-parameters is preserved. Without this interaction term, the model is forced to assume the same age slope for both sexes.

*Example 4 (NOT feature engineering — feature scaling).* Standardizing features by subtracting the mean and dividing by the standard deviation is *not* feature engineering in the sense of this definition — it does not introduce new features, just rescales existing ones. Scaling matters for numerical conditioning and for the interpretation of regularization (Tikhonov with $\lambda \|\theta\|^2$ implicitly assumes features are on comparable scales), but it does not change the *expressivity* of the model class.

*Example 5 (random features for image classification).* For the MNIST digit classification problem (28×28 = 784 raw pixel features), Boyd reports that adding 5000 random features of the form $g_k(x) = \max\{(R_k^T x), 0\}$ (with $R_k$ random $\pm 1$ entries) reduces the error rate from 1.6% to 0.21% on training and 0.24% on test. This is the *random feature kitchen-sink* method: massively expand the feature space with random nonlinear transformations, then let LS find the best linear combination. It works because high-dimensional random features approximate (in expectation) a particular kernel feature space.

**Calibration check.** Verify: (i) one-hot encoding with $K$ levels requires $K - 1$ basis functions (or $K$ if no intercept is included) to avoid linear dependence with the intercept; (ii) interaction terms $x_i x_j$ are particularly interpretable when the original features are Boolean (then $x_i x_j = 1$ iff both features are present); (iii) adding more features always reduces training RMS error (monotonically), but can either reduce or increase test RMS error.

---

# Unlocked by This

> [!tip] Kernel Methods *(from Machine Learning)*
> Feature engineering by hand can be replaced (or augmented) by the **kernel trick**: instead of computing engineered features explicitly, define a kernel function $K(x, x') = \langle \phi(x), \phi(x') \rangle$ in some implicit feature space $\phi$. The least squares problem then transforms into a kernel ridge regression that only requires evaluating $K$ on the data, not explicitly computing $\phi$. This is the foundation of SVMs, Gaussian processes, and kernel PCA. The conceptual unification: kernel methods are LS data fitting with an *implicit* and *potentially infinite-dimensional* feature space.

> [!tip] Deep Learning as Learned Features *(from Modern ML)*
> A deep neural network can be viewed as the composition of many feature-engineering layers (each consisting of a linear transformation followed by a nonlinearity), with a final linear-in-features prediction layer. The intermediate layers *learn* their feature transformations from data, rather than relying on a human designer. This is the deepest extension of feature engineering: rather than choose a fixed basis (polynomial, sinusoidal, random), the network *adapts* its basis to the data. The connection to LS is direct: training the final layer of a frozen network is exactly an LS data-fitting problem; the deeper magic is the joint training of all layers via backpropagation.
