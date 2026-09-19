# GATE-LOCO — conditioning-variable selection for synthetic electricity load generation

> **Billy Thomont's PhD research project.** This page documents a research direction and reported intermediate notebook observations; it is **not a peer-reviewed contribution, not a completed generator benchmark, and not independently reproduced**. Snapshot: 2026-09-19.

## Research question

Which condition groups available at sampling time improve fidelity, dynamics, controllability, downstream utility and **geographic transfer** of synthetic electricity consumption profiles without leakage, redundancy or unacceptable missingness? Compare a **conditional WGAN-GP (+EMA)** and a **conditional DiT-1D (+EMA)** under matched splits; neither cWGAN-GP nor EMA alone should be claimed as new.

The initial load configuration includes RTE Île-de-France 30-minute measurements and 48-step windows. A global conditioning panel spans **217 countries/territories (2019-01-01 to 2026-07-24)** at 30-minute resolution (~28.8M working-panel records). This does **not** mean all countries have target load and exogenous variables at all timestamps.

## Candidate variable groups

| Group | Examples | Critical check |
|---|---|---|
| Local calendar | hour/weekday; day-of-year sin/cos; weekend | Timezone, daylight saving, availability |
| Scientific seasons | Meteorological, astronomical, hydroclimatic; wet/dry; unimodal/bimodal | Hemisphere/tropics; country-identity leakage |
| Weather & solar | Temperature, humidity, irradiance, rainfall | Coverage, collinearity, lag availability, physical bounds |
| Society & grid | Holidays, school calendars, economic metadata, regional grid IDs | Sparse sources, temporal availability, accidental domain labels |

Scientific seasons are *competing representations*: meteorological DJF/MAM/JJA/SON with hemisphere inversion; astronomical boundaries; hydroclimatic wet/dry seasons derived from 1991–2020 precipitation climatology and Liebmann-style cumulative anomalies; tropical uni-/bimodal regimes. Join to correct **local date and IANA timezone**. Existing data-quality findings included country code NA incorrectly parsed for Namibia, UTC fallback and inappropriate winter/summer labels in the tropics. A seasonal daily reference table contained ~599,354 locality-day rows; joining one reference point per country can itself reveal country identity.

## Proposed operational GATE-LOCO protocol

The name GATE-LOCO denotes the user's project; this document **does not invent an acronym expansion** or assert that all steps are already implemented.

1. Audit target and exogenous data: provenance, units (MW versus MWh), 30-minute continuity, domain/timestamp uniqueness, missingness, timezone, outliers, availability at sampling time.
2. Lock chronological rolling folds and domain holdouts (leave-country-out and climate-family-out are distinct tests). Fit any imputer/scaler/feature selection **only on training data**.
3. Compare a calendar-only baseline with addition and removal of whole scientifically coherent condition groups; assess incremental effect, redundancy, cost and label leakage. A proxy forecast-model importance score is **not equivalent to generative improvement**.
4. Report domain×fold effect distributions, paired uncertainty intervals, failed / zero-sample folds and negative-transfer domains. A provisional SESOI 5%, bootstrap CI >0 and ≥75% positive domain×fold can be preregistered, not taken as universal thresholds.
5. Confirm selected blocks in cWGAN-GP and DiT-1D with identical splits and multiple preassigned seeds: stratified distributional quality, ACF/peaks, normalized DTW, TSTR versus TRTR, conditional calibration and privacy where claimed. EMA on/off ablation.
6. Verify held-out country performance and energy-consistent 30-min → hourly/daily/monthly aggregation. Distinguish post-hoc aggregation from an independently learnt multi-resolution generator.

## Reported snapshots (not interchangeable)

| Experiment snapshot | Reported finding | Status and scientific interpretation |
|---|---|---|
| July 2026 AEMO v2.6 (4 domains, 87,840 hourly observations, 4 rolling folds) | Exploratory calendar +26.2%, solar +18.5%, seasons +8.4%; holiday hours only ~+5.1%. | **Proxy / feature audit**, not cWGAN/DiT generation effect. Recheck outcome metric and logs. |
| July 2026 global EXP-A / early EXP-B | EXP-A completed; EXP-B domain_id failed 0/76 due to minimum-sample eligibility. | Engineering/data failure, **not** a scientific negative result; later work may supersede. |
| September 2026 season ablation after hour, weekday, day-of-year cyclic baseline | Meteorological +0.148%, astronomical +0.008%, hydroclimate ~0 additional proxy gain. | **Marginal effect conditional on existing time features**; does not mean physical seasons have no effect. |
| September 2026 transfer tests | Climate-family holdout ~+23%; country holdout ~−9%; season-only country classification balanced accuracy 1.00. | **Suspected geographic identity leakage** from single reference location per country; investigate and retest before claims. |
| Complete conditioned multi-country generators and multi-resolution tests | No independently verified complete result available to this public bibliography. | Proposed/ongoing, **not** an established contribution or state-of-the-art result. |

The percentages are derived from previously reported working notes and have not been independently checked against notebooks in this repository.

## Relevant published baselines

- [Wang et al. 2020](https://doi.org/10.1016/j.epsr.2020.106732): CWGAN-GP conditional on day type, temperature and history for forecast residuals (different target).
- [Baasch et al. 2021](https://doi.org/10.1016/j.egyai.2021.100087): conditional temporal building-load GAN and monthly mean temperature; temporal QA.
- [Fu et al. 2024](https://doi.org/10.1016/j.enbuild.2024.114216): annual conditional diffusion with location, weather, building and meter metadata.
- [Xia et al. 2025](https://doi.org/10.1016/j.egyai.2025.100586): continuous weather conditions and cWGAN-GP comparator for residential loads.
- [AC-WTGAN+ 2026](https://doi.org/10.1016/j.epsr.2026.113338): explicit residential cWGAN-GP with household attributes and utility/privacy.
- [Seasonal WGAN-GP 2026](https://doi.org/10.3390/en19153651): seasonal weekly load clusters.

**Candidate novelty, not a result:** a reproducible, data-availability-aware, scientific-season-aware and leakage-audited *selection protocol* whose benefits must be confirmed under geographic transfer and conditioned generation, with comparable cross-resolution QA. A negative finding is publishable if reproducible.
