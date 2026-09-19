# Proposed common synthetic-load evaluation protocol

This is a **proposed** benchmarking framework, NOT metrics reported by all listed papers.

**Reproducibility:** prespecify 10 independent seeds where feasible, report all runs (mean ± SD/CI; failures), data provenance, precise split, preprocessing, hyperparameters, EMA, sampler and training compute. Split by time *and* household / country when assessing transfer. Tune solely on validation, never test.

**Distribution:** Wasserstein with exact 1D/multivariate definition and units; MMD/RBF with bandwidth and pooling scheme; KS and quantiles conditional on region, day and season.

**Dynamics:** normalized DTW with warping window; ACF, periodogram, ramps, peak timing/size, load duration curves and seasonal profiles. Compare per temporal resolution and spatial level.

**Utility:** Train-on-Synthetic-Test-on-Real (TSTR), Train-on-Real-Test-on-Real (TRTR), matched model/feature/split; distinguishability real vs synthetic.

**Privacy:** nearest-neighbour and membership-inference checks if privacy is claimed; high fidelity does not itself guarantee privacy.

**Units / aggregation:** if 30-min inputs are mean power MW, 1-hour mean MW = arithmetic average of the two points, while 1-hour energy MWh = 0.5 × sum of the two MW values. Apply timezone/DST rules; daily and monthly energy are integrals, not mean-power sums. Require consistency between generated and aggregated levels.

Do not rank models using raw DTW, Wasserstein, MMD or TSTR from different datasets and normalizations.
