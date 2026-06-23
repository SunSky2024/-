# Statistical Learning Notes Changelog

## 2026-06-22 Final quality check

### 图片目录

本页当前使用的图片目录如下：

- `assets/textbook/lecture_01/`
- `assets/textbook/lecture_02/`
- `assets/textbook/lecture_03/`
- `assets/textbook/lecture_04/`
- `assets/textbook/lecture_05/`
- `assets/textbook/lecture_06/`
- `assets/textbook/lecture_07/`
- `assets/textbook/lecture_08/`
- `assets/textbook/lecture_09/`
- `assets/slides/lecture_10/`
- `assets/slides/lecture_11/`
- `assets/slides/lecture_12/`

### 每讲插图数量

| 讲次 | 主题 | 插图数 |
| --- | --- | ---: |
| 第 1 讲 | K 近邻与偏差-方差权衡 | 8 |
| 第 2 讲 | 回归的线性模型 | 6 |
| 第 3 讲 | 惩罚线性回归（一） | 5 |
| 第 4 讲 | 惩罚线性回归（二） | 5 |
| 第 5 讲 | 逻辑回归与判别分析 | 5 |
| 第 6 讲 | RKHS 与核岭回归 | 1 |
| 第 7 讲 | 支持向量机 | 5 |
| 第 8 讲 | 核密度估计与核回归估计 | 6 |
| 第 9 讲 | 树模型与随机森林 | 6 |
| 第 10 讲 | 因果推断导论 | 7 |
| 第 11 讲 | 纵向因果模型 | 6 |
| 第 12 讲 | 工具变量 | 6 |

合计：66 张图。

### 第 10 讲自绘 DAG 图

第 10 讲已将原课件截图替换为更适合讲义阅读的自绘 SVG DAG，并新增随机化与观测研究混杂两张基础图：

- `assets/slides/lecture_10/dag_randomized_trial.svg`
- `assets/slides/lecture_10/dag_observational_confounding.svg`
- `assets/slides/lecture_10/dag_asthma_example.svg`
- `assets/slides/lecture_10/dag_backdoor_paths.svg`
- `assets/slides/lecture_10/dag_collider_bias.svg`
- `assets/slides/lecture_10/dag_d_separation_rules.svg`
- `assets/slides/lecture_10/dag_adjustment_examples.svg`

### 来自课件截图的图片

以下图片来自课件 PDF 截图，并在图注中标明了来源 PDF 与页码：

- 第 11 讲：`assets/slides/lecture_11/p05_longitudinal_dag.png`、`p15_mean_msm_weights.png`、`p18_iptw_procedure.png`、`p30_time_varying_setup.png`、`p34_two_stage_snm.png`、`p42_msm_snm_comparison.png`
- 第 12 讲：`assets/slides/lecture_12/p12_iv_dag.png`、`p21_wald_estimand.png`、`p25_compliance_types.png`、`p29_complier_causal_effect.png`、`p45_two_stage_least_squares.png`、`p54_iv_inequality_test.png`

### 质量检查记录

- `index.html` 中 66 个 `<img>` 的相对路径均存在，无 broken image。
- 所有图片均包含 `alt`、`loading="lazy"`、`decoding="async"`。
- 66 个 `<figure>` 均包含 `figcaption`。
- 未发现连续 3 张以上图片直接堆叠。
- 目录中的内部锚点均能在页面中找到对应 `id`。
- MathJax、公式块、ESL 链接和 PPT/PDF 链接均保留。
- 桌面 1280px 与手机 390px 宽度下页面根级横向溢出为 0；长公式、表格和代码块保留内部横向滚动能力。

### 后续可继续补图的位置

- 第 6 讲目前只有 1 张图，后续可以补充 RKHS 几何直觉、表示定理和核岭回归解的结构图。
- 第 10 讲当前使用自绘 DAG、后门路径、碰撞点、d-separation 和 DAG 练习图；后续若补图，应优先补“混杂调整流程”“IPTW 伪总体机制”这类重绘示意图，而不是公式截图。
- 第 11 至 12 讲已经使用课件截图，后续若追求更统一的视觉风格，可以把部分 DAG、IPTW、2SLS 流程重绘成教材风格示意图。
- 第 3 至 4 讲可继续补充不同惩罚路径随 `lambda` 变化的动态图或多图对照。
- 第 5 讲可补充混淆矩阵、阈值变化与 ROC 曲线之间的对应图。
