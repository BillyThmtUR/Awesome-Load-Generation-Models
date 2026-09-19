# Awesome Load Generation Models

## Navigation

- [All studies, newest → oldest](#all-studies-newest--oldest)
- [WGAN-GP vs cWGAN-GP: verified prior art](#wgan-gp-vs-cwgan-gp-verified-prior-art)
- [Browse by model family](#browse-by-model-family)
- [State-of-the-art and reviews](#state-of-the-art-and-reviews)
- [Reproducible OpenAlex replication of survey Figure 1](docs/OPENALEX_FIGURE1_REPLICATION.md)
- [Quality control and GATE-LOCO](#quality-control-and-gate-loco)
- [Metrics, published numerical results and equation notation](docs/METRICS_RESULTS_NOTATION.md)
- [Datasets and contributions](#datasets-and-contributions)

## All studies, newest → oldest

**Direct**: generates electricity load/net load or benchmarks its synthesis. **Adjacent**: probabilistic forecast residuals, mixed source-load scenarios, appliance-level sequences, or related but different tasks. **À vérifier**: not established by accessible bibliographic evidence. CSV has precise condition groups, metrics, dates and evidence tags.

| Date | Model / paper | Family | Benchmark / dataset | Resolution; horizon | Article / code |
|---|---|---|---|---|---|
| September 2026 | **LoaDiff** — LoaDiff: Conditional Generation of Electricity Consumption Time Series for Energy Analytics<br><sub>Direct; arXiv Sep 2026</sub> | Diffusion conditionnelle | 3 jeux résidentiels | infra-horaire; annuel | [Paper](https://arxiv.org/abs/2609.11639) |
| August 2026 | **Seasonal weekly WGAN-GP** — Synthetic Seasonal Weekly Load Profile Generation Based on Advanced Wasserstein-Distance Generative Adversarial Networks<br><sub>Direct; Energies Aug 2026</sub> | WGAN-GP | Irish residential | à vérifier; semaine saisonnière | [Paper](https://doi.org/10.3390/en19153651) |
| July 2026 | **Temporally-Conditioned DiT** — Temporally-Conditioned Diffusion Transformer for Appliance-Level Load Synthesis in Non-Intrusive Load Monitoring<br><sub>Adjacent appareil/NILM; SSRN Jul 2026</sub> | Diffusion Transformer | Appliances; à vérifier | à vérifier; séquences appareils | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7124192) |
| June 2026 | **AC-WTGAN+** — AC-WTGAN+: A conditional Wasserstein temporal generator for high-quality residential load synthesis<br><sub>Direct; Electric Power Systems Research Jun 2026</sub> | cWGAN-GP | Irish CER | 30 min; 336 pas / semaine | [Paper](https://doi.org/10.1016/j.epsr.2026.113338) |
| June 2026 | **LV conditional diffusion** — Coherent load profile synthesis with conditional diffusion for LV distribution network scenario generation<br><sub>Direct; Sustainable Energy Grids and Networks Jun 2026</sub> | Diffusion conditionnelle | Réseau LV | à vérifier; journée | [Paper](https://doi.org/10.1016/j.segan.2026.102264) · [Code/data](https://github.com/strath-ai/lv-synthesis-diffusion) |
| January 2026 | **Annual convolutional WGAN** — From Data Scarcity to Scalability: Generating Realistic Building Energy Profiles with GANs<br><sub>Direct; SSRN Jan 2026; version 2025 remplacée</sub> | WGAN (GP à vérifier) | 1300 foyers; PV; PAC; EV | 1 h; annuel 24 × 368 | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6135520) · [Code/data](https://github.com/MODERATE-Project/Synthetic-Load-Profiles) |
| January 2026 | **DGAN** — Residential electrical demand data synthesis using the DGAN model: performance evaluation for diverse dwellings<br><sub>Direct; Energy and Buildings Jan 2026</sub> | GAN | Habitations diverses | à vérifier; à vérifier | [Paper](https://doi.org/10.1016/j.enbuild.2025.116722) |
| January 2026 | **Interpretable diffusion + Transformer** — Long-term scenario generation for distribution network loads based on interpretable diffusion models<br><sub>Direct/scénarios; IJEPES Jan 2026</sub> | Diffusion + Transformer | Réseau distribution | multi-échelle; long terme / annuel | [Paper](https://doi.org/10.1016/j.ijepes.2025.111491) |
| July 2025 | **Conv1D-WGAN-GP** — A Data-Driven Approach for Generating Synthetic Load Profiles with GANs<br><sub>Direct; Applied Sciences Jul 2025</sub> | WGAN-GP | 4 datasets industriels; agricoles; résidentiels | à vérifier; 24 h | [Paper](https://doi.org/10.3390/app15147835) |
| June 2025 | **EnergyDiff** — EnergyDiff: Universal Time-Series Energy Data Generation Using Diffusion Models<br><sub>Direct; IEEE TSG Jun 2025; arXiv 2024</sub> | Diffusion DDPM | Électricité; PAC; PV; consommateur et transformateur | 1; 15; 30; 60 min; à vérifier | [Paper](https://doi.org/10.1109/TSG.2025.3581472) |
| May 2025 | **RLP-GAN** — Learning and Generating Diverse Residential Load Patterns Using GAN with Weakly-Supervised Training and Weight Selection<br><sub>Direct; IEEE TCE May 2025</sub> | GAN | 417 foyers | à vérifier; patterns résidentiels | [Paper](https://doi.org/10.1109/TCE.2025.3563272) |
| 2025 (month unverified) | **Activity-based GAN** — Residential Load Modeling With Generative Adversarial Networks<br><sub>Direct/hybride activités vers charge; 2025</sub> | cGAN hybride | Emploi du temps Italie | appareils; journée | [Paper](https://doi.org/10.1109/TSUSC.2025.3605668) |
| 2025 (month unverified) | **Physics-informed diffusion** — Generating Synthetic Net Load Data for Residential Customers With Physics-Informed Diffusion Models<br><sub>Direct/net-load; online 2025; volume 2026</sub> | Diffusion conditionnelle | Pecan Street | à vérifier; à vérifier | [Paper](https://doi.org/10.1109/TSG.2025.3625925) |
| March 2025 | **PV/EV building cGAN** — Conditional generative adversarial network (cGAN) for generating building load profiles with photovoltaics and electric vehicles<br><sub>Direct; Energy and Buildings 2025; March 2025 bibliographic listing; full paper source</sub> | cGAN | 110 households with PV and EV, southwest USA | 1 h; à vérifier | [Paper](https://doi.org/10.1016/j.enbuild.2025.115584) |
| 2025 (month unverified) | **SocioDiff** — SocioDiff: A Socio-Aware Diffusion Model for Residential Electricity Consumption Data Generation<br><sub>Direct; IEEE TSG 2025</sub> | Diffusion conditionnelle | Irish CER | 30 min; 336 pas / semaine | [Paper](https://doi.org/10.1109/TSG.2025.3575819) · [Code/data](https://github.com/Intelligame/SocialDiff) |
| November 2024 | **Source-load cWGAN-GP** — Source-load scenario generation method based on conditional Wasserstein generative adversarial network with gradient penalty<br><sub>Adjacent mixed source+load; EI2 2024 November; direct load-only evaluation not established</sub> | cWGAN-GP (source-load) | Mixed electricity source and load; setup not verified | à vérifier; scénarios | [Paper](https://doi.org/10.1109/EI264398.2024.10991846) |
| October 2024 | **ERGAN** — Synthetic Data Generation for Residential Load Patterns via Recurrent GAN and Ensemble Method<br><sub>Direct; IEEE TIM Oct 2024; données synthétiques</sub> | GAN récurrent | Pecan Street 417 foyers | 1 h; journée | [Paper](https://doi.org/10.1109/TIM.2024.3480225) · [Code/data](https://github.com/AdamLiang42/ERGAN-Dataset) |
| June 2024 | **Building metadata diffusion** — Creating synthetic energy meter data using conditional diffusion and building metadata<br><sub>Direct; Energy and Buildings Jun 2024</sub> | Diffusion conditionnelle | 1828 compteurs multi-pays | à vérifier; annuel | [Paper](https://doi.org/10.1016/j.enbuild.2024.114216) |
| June 2024 | **GAN/WGAN/WGAN-GP benchmark** — Comparative assessment of generative models for transformer- and consumer-level load profiles generation<br><sub>Direct benchmark; SEGAN Jun 2024</sub> | Benchmark | Client et transformateur | 15; 30; 60 min; à vérifier | [Paper](https://doi.org/10.1016/j.segan.2024.101338) |
| April 2024 | **DGAN + wavelets** — Capturing multiscale temporal dynamics in synthetic residential load profiles through Generative Adversarial Networks (GANs)<br><sub>Direct; Applied Energy Apr 2024</sub> | GAN | Résidentiel (confidentiel) | haute fréquence; annuel puis intrajournalier | [Paper](https://doi.org/10.1016/j.apenergy.2024.122831) |
| February 2024 | **Customized load diffusion** — Customized Load Profiles Synthesis for Electricity Customers Based on Conditional Diffusion Models<br><sub>Direct; IEEE TSG Feb 2024; arXiv 2023</sub> | Diffusion conditionnelle | Dataset public à vérifier | à vérifier; à vérifier | [Paper](https://doi.org/10.1109/TSG.2024.3366212) |
| August 2023 | **MultiLoad-GAN** — MultiLoad-GAN: A GAN-Based Synthetic Load Group Generation Method Considering Spatial-Temporal Correlations<br><sub>Direct; IEEE TSG 2023; données réelles restreintes; Online Aug 2023; journal issue Mar 2024</sub> | GAN | Groupe de charges / transformateur | à vérifier; à vérifier | [Paper](https://doi.org/10.1109/TSG.2023.3302192) · [Code/data](https://github.com/hughwln/MultiLoad-GAN_public) |
| October 2022 | **WDCGAN (GP in loss)** — Energy data generation with Wasserstein Deep Convolutional Generative Adversarial Networks<br><sub>Direct; Energy Oct 2022</sub> | WGAN-GP | Irish residential | 30 min; 7 × 48 pas / semaine | [Paper](https://doi.org/10.1016/j.energy.2022.124694) |
| August 2022 | **Grid stress-testing GAN** — Stress testing electrical grids: Generative Adversarial Networks for load scenario generation<br><sub>Adjacent / scope mix electric inland generation et consumption; Energy and AI Aug 2022</sub> | GAN | Pays européens / variable mixte | 1 h; scénarios multivariés | [Paper](https://doi.org/10.1016/j.egyai.2022.100177) · [Code/data](https://github.com/Advestis/els_paper) |
| August 2022 | **RCGAN / TimeGAN / CWGAN / RCWGAN** — Synthetic demand data generation for individual electricity consumers: Generative Adversarial Networks (GANs)<br><sub>Direct benchmark; Energy and AI Aug 2022</sub> | GAN / cWGAN | Clients individuels | à vérifier; à vérifier | [Paper](https://doi.org/10.1016/j.egyai.2022.100161) |
| July 2022 | **ProfileSR-GAN** — ProfileSR-GAN: A GAN Based Super-Resolution Method for Generating High-Resolution Load Profiles<br><sub>Direct super-résolution; IEEE TSG 2022; IEEE TSG issue July 2022; earlier online month not checked</sub> | GAN / super-résolution | Smart-meter LR/HR | haute fréquence; à vérifier | [Paper](https://doi.org/10.1109/TSG.2022.3158235) |
| January 2022 | **Time-Variant GAN** — Synthetic Energy Data Generation Using Time Variant Generative Adversarial Network<br><sub>Direct; Electronics Jan 2022</sub> | GAN | Consommation énergétique | à vérifier; à vérifier | [Paper](https://doi.org/10.3390/electronics11030355) |
| 2022 (month unverified) | **DPWGAN** — DPWGAN: High-Quality Load Profiles Synthesis With Differential Privacy Guarantees<br><sub>Direct; online 2022 / journal 2023</sub> | WGAN + DP | Smart meters | à vérifier; à vérifier | [Paper](https://doi.org/10.1109/TSG.2022.3230671) |
| September 2021 | **Baasch conditional temporal GAN** — A Conditional Generative adversarial Network for energy use in multiple buildings using scarce data<br><sub>Direct; Energy and AI September 2021; 22 experiments</sub> | cGAN / temporal GAN | Residential + commercial buildings; 396 and 156 sequences | à vérifier; sequences | [Paper](https://doi.org/10.1016/j.egyai.2021.100087) |
| July 2021 | **Transmission cGAN** — Synthetic Time-Series Load Data via Conditional Generative Adversarial Networks<br><sub>Direct; arXiv 2021</sub> | cGAN | Réseau de transport | 1 h; 1 semaine | [Paper](https://arxiv.org/abs/2107.03545) |
| December 2020 | **CWGAN-GP residual scenario** — Modeling load forecast uncertainty using generative adversarial networks<br><sub>Adjacent probabilistic load forecast residual scenario generation; Electric Power Systems Research December 2020</sub> | cWGAN-GP (forecast residuals) | Eight US areas open load datasets | à vérifier; day-ahead / trajectory scenarios | [Paper](https://doi.org/10.1016/j.epsr.2020.106732) |
| October 2020 | **Clustered GAN** — Generating realistic building electrical load profiles through the Generative Adversarial Network (GAN)<br><sub>Direct; Energy and Buildings Oct 2020</sub> | GAN | Building Data Genome | 1 h; 24 h | [Paper](https://doi.org/10.1016/j.enbuild.2020.110299) |
| December 2019 | **R-GAN / WGAN / MH-GAN** — Generating Energy Data for Machine Learning with Recurrent Generative Adversarial Networks<br><sub>Direct; online Dec 2019; Energies vol. 2020</sub> | GAN / WGAN | Consommation énergétique | à vérifier; à vérifier | [Paper](https://doi.org/10.3390/en13010130) |
| February 2019 | **ACGAN / Conv GAN** — GAN-based Model for Residential Load Generation Considering Typical Consumption Patterns<br><sub>Direct; ISGT 2019; ISGT conference 18–21 Feb 2019; preprint circulated Dec 2018</sub> | cGAN | Irish smart meters | à vérifier; hebdomadaire | [Paper](https://doi.org/10.1109/ISGT.2019.8791575) |
| October 2018 | **Demand-side cGAN** — Demand Side Data Generating Based on Conditional Generative Adversarial Networks<br><sub>Direct; Energy Procedia Oct 2018</sub> | cGAN | Compteurs + enquêtes | à vérifier; à vérifier | [Paper](https://doi.org/10.1016/j.egypro.2018.09.157) |

**Machine-readable catalogue:** [papers.csv](catalogue/papers.csv) — year, month, date precision, model, family, target, dataset, native resolution, horizon, conditioning, metrics, DOI, code, task scope and GP evidence. [Reviews.csv](catalogue/reviews.csv) holds surveys separately.

## WGAN-GP vs cWGAN-GP: verified prior art

| Date | Study | Exact implication |
|---|---|---|
| June 2026 | [AC-WTGAN+](https://doi.org/10.1016/j.epsr.2026.113338) | **Direct residential cWGAN-GP**: conditions on household attributes; Wasserstein objective, **gradient penalty** and auxiliary classification; Irish CER 336-step weekly loads. |
| August 2026 | [Seasonal weekly WGAN-GP](https://doi.org/10.3390/en19153651) | WGAN-GP trained per seasonal consumption-pattern cluster; **cluster-specific unconditional generators** should not automatically be relabelled as one cWGAN-GP. |
| July 2025 | [Conv1D-WGAN-GP](https://doi.org/10.3390/app15147835) | Direct daily electricity-load WGAN-GP, contrasted with vanilla GAN/WGAN-GP/Conv1D-GAN. |
| November 2024 | [Sun et al., source-load cWGAN-GP](https://doi.org/10.1109/EI264398.2024.10991846) | Explicit **conditional WGAN-GP** but mixed source-load scenarios; direct load-only evaluation not verified. |
| June 2024 | [Xia et al. benchmark](https://doi.org/10.1016/j.segan.2024.101338) | Compare GAN, WGAN and WGAN-GP at 15/30/60 minutes; a benchmark is not an additional new architecture. |
| October 2022 | [WDCGAN](https://doi.org/10.1016/j.energy.2022.124694) | Wasserstein Deep Convolutional GAN with gradient penalty; verify whether and where demographics enter the generator/critic before assigning conditional taxonomy. |
| December 2020 | [Wang et al., CWGAN-GP](https://doi.org/10.1016/j.epsr.2020.106732) | **Conditional WGAN-GP**, but samples *forecast-error/residual scenarios*, rather than independent historical load distributions; 8 US areas. |
| September 2025 | [FCPFlow](https://doi.org/10.1016/j.egyai.2025.100586) | Flow-based model, **not a GAN**; nevertheless explicitly evaluates a **cWGAN-GP comparator under continuous meteorological conditions**. |

**Conclusion for scientific positioning:** cWGAN-GP for load-related generation is **not new in itself**. A plausible specific research question concerns group-wise feature selection with a strict leakage audit, geographic transfer, season representation and multi-resolution QA. It becomes a contribution only if validated by controlled experiments. No equivalent `cWGAN-GP+EMA` novelty claim is established from this list alone.

## Browse by model family

### WGAN-GP and conditional WGAN-GP

- **August 2026 · Seasonal weekly WGAN-GP** — [Synthetic Seasonal Weekly Load Profile Generation Based on Advanced Wasserstein-Distance Generative Adversarial Networks](https://doi.org/10.3390/en19153651).
- **June 2026 · AC-WTGAN+** — [AC-WTGAN+: A conditional Wasserstein temporal generator for high-quality residential load synthesis](https://doi.org/10.1016/j.epsr.2026.113338).
- **July 2025 · Conv1D-WGAN-GP** — [A Data-Driven Approach for Generating Synthetic Load Profiles with GANs](https://doi.org/10.3390/app15147835).
- **November 2024 · Source-load cWGAN-GP** — [Source-load scenario generation method based on conditional Wasserstein generative adversarial network with gradient penalty](https://doi.org/10.1109/EI264398.2024.10991846) *(adjacent task)*.
- **October 2022 · WDCGAN (GP in loss)** — [Energy data generation with Wasserstein Deep Convolutional Generative Adversarial Networks](https://doi.org/10.1016/j.energy.2022.124694).
- **December 2020 · CWGAN-GP residual scenario** — [Modeling load forecast uncertainty using generative adversarial networks](https://doi.org/10.1016/j.epsr.2020.106732) *(adjacent task)*.

### GAN / other WGAN

- **January 2026 · Annual convolutional WGAN** — [From Data Scarcity to Scalability: Generating Realistic Building Energy Profiles with GANs](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6135520).
- **January 2026 · DGAN** — [Residential electrical demand data synthesis using the DGAN model: performance evaluation for diverse dwellings](https://doi.org/10.1016/j.enbuild.2025.116722).
- **May 2025 · RLP-GAN** — [Learning and Generating Diverse Residential Load Patterns Using GAN with Weakly-Supervised Training and Weight Selection](https://doi.org/10.1109/TCE.2025.3563272).
- **2025 (month unverified) · Activity-based GAN** — [Residential Load Modeling With Generative Adversarial Networks](https://doi.org/10.1109/TSUSC.2025.3605668).
- **2025 (month unverified) · PV/EV building cGAN** — [Conditional generative adversarial network (cGAN) for generating building load profiles with photovoltaics and electric vehicles](https://doi.org/10.1016/j.enbuild.2025.115584).
- **October 2024 · ERGAN** — [Synthetic Data Generation for Residential Load Patterns via Recurrent GAN and Ensemble Method](https://doi.org/10.1109/TIM.2024.3480225).
- **April 2024 · DGAN + wavelets** — [Capturing multiscale temporal dynamics in synthetic residential load profiles through Generative Adversarial Networks (GANs)](https://doi.org/10.1016/j.apenergy.2024.122831).
- **August 2023 · MultiLoad-GAN** — [MultiLoad-GAN: A GAN-Based Synthetic Load Group Generation Method Considering Spatial-Temporal Correlations](https://doi.org/10.1109/TSG.2023.3302192).
- **August 2022 · Grid stress-testing GAN** — [Stress testing electrical grids: Generative Adversarial Networks for load scenario generation](https://doi.org/10.1016/j.egyai.2022.100177) *(adjacent task)*.
- **August 2022 · RCGAN / TimeGAN / CWGAN / RCWGAN** — [Synthetic demand data generation for individual electricity consumers: Generative Adversarial Networks (GANs)](https://doi.org/10.1016/j.egyai.2022.100161).
- **July 2022 · ProfileSR-GAN** — [ProfileSR-GAN: A GAN Based Super-Resolution Method for Generating High-Resolution Load Profiles](https://doi.org/10.1109/TSG.2022.3158235).
- **January 2022 · Time-Variant GAN** — [Synthetic Energy Data Generation Using Time Variant Generative Adversarial Network](https://doi.org/10.3390/electronics11030355).
- **2022 (month unverified) · DPWGAN** — [DPWGAN: High-Quality Load Profiles Synthesis With Differential Privacy Guarantees](https://doi.org/10.1109/TSG.2022.3230671).
- **September 2021 · Baasch conditional temporal GAN** — [A Conditional Generative adversarial Network for energy use in multiple buildings using scarce data](https://doi.org/10.1016/j.egyai.2021.100087).
- **July 2021 · Transmission cGAN** — [Synthetic Time-Series Load Data via Conditional Generative Adversarial Networks](https://arxiv.org/abs/2107.03545).
- **October 2020 · Clustered GAN** — [Generating realistic building electrical load profiles through the Generative Adversarial Network (GAN)](https://doi.org/10.1016/j.enbuild.2020.110299).
- **December 2019 · R-GAN / WGAN / MH-GAN** — [Generating Energy Data for Machine Learning with Recurrent Generative Adversarial Networks](https://doi.org/10.3390/en13010130).
- **February 2019 · ACGAN / Conv GAN** — [GAN-based Model for Residential Load Generation Considering Typical Consumption Patterns](https://doi.org/10.1109/ISGT.2019.8791575).
- **October 2018 · Demand-side cGAN** — [Demand Side Data Generating Based on Conditional Generative Adversarial Networks](https://doi.org/10.1016/j.egypro.2018.09.157).

### Diffusion and diffusion Transformer

- **September 2026 · LoaDiff** — [LoaDiff: Conditional Generation of Electricity Consumption Time Series for Energy Analytics](https://arxiv.org/abs/2609.11639).
- **July 2026 · Temporally-Conditioned DiT** — [Temporally-Conditioned Diffusion Transformer for Appliance-Level Load Synthesis in Non-Intrusive Load Monitoring](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7124192) *(adjacent task)*.
- **June 2026 · LV conditional diffusion** — [Coherent load profile synthesis with conditional diffusion for LV distribution network scenario generation](https://doi.org/10.1016/j.segan.2026.102264).
- **January 2026 · Interpretable diffusion + Transformer** — [Long-term scenario generation for distribution network loads based on interpretable diffusion models](https://doi.org/10.1016/j.ijepes.2025.111491).
- **June 2025 · EnergyDiff** — [EnergyDiff: Universal Time-Series Energy Data Generation Using Diffusion Models](https://doi.org/10.1109/TSG.2025.3581472).
- **2025 (month unverified) · Physics-informed diffusion** — [Generating Synthetic Net Load Data for Residential Customers With Physics-Informed Diffusion Models](https://doi.org/10.1109/TSG.2025.3625925).
- **2025 (month unverified) · SocioDiff** — [SocioDiff: A Socio-Aware Diffusion Model for Residential Electricity Consumption Data Generation](https://doi.org/10.1109/TSG.2025.3575819).
- **June 2024 · Building metadata diffusion** — [Creating synthetic energy meter data using conditional diffusion and building metadata](https://doi.org/10.1016/j.enbuild.2024.114216).
- **February 2024 · Customized load diffusion** — [Customized Load Profiles Synthesis for Electricity Customers Based on Conditional Diffusion Models](https://doi.org/10.1109/TSG.2024.3366212).

### Comparative benchmarks

- **June 2024 · GAN/WGAN/WGAN-GP benchmark** — [Comparative assessment of generative models for transformer- and consumer-level load profiles generation](https://doi.org/10.1016/j.segan.2024.101338).

## State-of-the-art and reviews

Surveys are not counted as original generator implementations. [Full review table with dates and findings](docs/REVIEWS.md) · [Reviews CSV](catalogue/reviews.csv). In particular:

- **Turowski et al., August 2024 online / December issue** — [Generating synthetic energy time series: A review](https://doi.org/10.1016/j.rser.2024.114842), 169 reviewed studies and gaps in standardized evaluation.
- **Zhang et al., February 2025** — [Deep generative models in energy system applications](https://doi.org/10.1016/j.apenergy.2024.125059), 228 studies across energy applications.
- **Stenger et al., May 2024** — [Evaluation is key](https://doi.org/10.1186/s40537-024-00924-7), 83 synthetic-time-series evaluation measures.
- **Yilmaz and Korn, September 2024** — [GAN guide for individual electricity demand](https://doi.org/10.1016/j.eswa.2024.123851), includes average coverage error (ACE).
- **Yang et al., April 2024 preprint** — [Survey on diffusion for time-series and spatio-temporal data](https://arxiv.org/abs/2404.18886); later ACM journal version is the *same* study.

## Quality control and GATE-LOCO

There **is** published load generation quality control (e.g., Baasch 2021, Xia 2024, Conv1D-WGAN-GP 2025, AC-WTGAN+ 2026). The defensible issue is **standardized, comparable, multi-dimensional QA**, not “no prior metrics”. Some 2025 published Wasserstein thresholds are expressly heuristic and **must not be directly applied** to unnormalized RTE results.

- [Literature-backed QA comparison and proposed controls](docs/QUALITY_CONTROL_LITERATURE.md).
- [Reusable proposed evaluation protocol](docs/EVALUATION_PROTOCOL.md): distribution, DTW/ACF/peaks, TSTR/TRTR, privacy, cross-resolution consistency, multiple seeds.
- [GATE-LOCO conditioning-variable selection](docs/GATE_LOCO.md): panel of 217 localities, scientific seasons, data availability, group ablations, geo-holdout and failure/leakage controls. **Project notes and provisional results are clearly separated from published literature**.

## Datasets and contributions

| Benchmark or artifact | Resource |
|---|---|
| Irish CER smart meter | [ISSDA](https://www.ucd.ie/issda/data/commissionforenergyregulationcer/) |
| Pecan Street residential | [Pecan Street](https://www.pecanstreet.org/) |
| Building Data Genome | [BDG2](https://github.com/buds-lab/building-data-genome-project-2) |
| ERGAN synthetic profiles | [ERGAN Dataset](https://github.com/AdamLiang42/ERGAN-Dataset) |
| MODERATE annual household generator | [Source](https://github.com/MODERATE-Project/Synthetic-Load-Profiles) |
| Conditional diffusion for LV substations | [Source](https://github.com/strath-ai/lv-synthesis-diffusion) |

Contributions welcome in all source languages: preserve the original title and add English translation if relevant. See [CONTRIBUTING.md](CONTRIBUTING.md) and [methodology](docs/METHODOLOGY.md). Forecast-only papers without genuine synthetic sampling and exclusively renewable-output papers are excluded from the primary list. See [adjacent methodologies](docs/ADJACENT_METHODS.md). Publication months require source confirmation; no guessed months, cross-paper raw score rankings or pirated PDFs.

Inspired by [Awesome-TimeSeries-SpatioTemporal-Diffusion-Model](https://github.com/yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model); independent electricity-load-specific curation.
