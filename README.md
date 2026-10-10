# 二看 Second Look

> **一看，解决问题。二看，审视答案。**

**一句话**：AI 做完或说完后，你只需叫它“二看”：重新对齐原始问题，检验证据，提出能改变判断的反问，并给有依据的评分。适用于代码、文档、方案、文章、观点、重大决定等，不限领域。

**核心理念**：不盲从，不刻意挑错；重新审视，证据说话。

**适用范围**：代码、文档、方案、文章、观点、重大决定等，不限领域。

---

## 如何调用

只记住一个名字，不用参数：

- **Codex**：`$second-look`
- **Claude Code**：`/second-look`（按客户端实际识别的命令为准）

若先前对话已有待审对象，直接调用即可。它会从上下文自动确定：审查对象、适用模式、审查深度、是否适合打分。不需要记住 audit、challenge、deep 等模式名。想指定对象时，直接补一句自然语言，比如“重点审查刚才的需求覆盖”。

---

## 默认输出

**二看｜**

```text
一、原始需求     **要解决的问题：** …   **预期目标：** …
二、审查结论     **结果：** 已解决 / 部分解决 / 未解决 / 无法确认
三、核心依据     1 需求完成情况 · 2 实际效果验证 · 3 遗留问题与潜在风险
四、改进与闭环   PDCA 表格（P0/P1/P2 · 问题 · 措施 · 验收标准）→ **下一步：**
五、本次评分     **综合评分：** …  **评价：** …  **得分依据：** …  **最终意见：** …
```

五段一律用 `**标签：** 正文` 的行式写法，**只有第四段用表格**。

结构对应 PDCA：**需求 → 结论 → 论证 → 改进 → 评分**，评分永远放最后。

「三-2 实际效果验证」必须区分**实测 / 推断 / 尚未验证**，引用代码或文件要带位置（`path:line`）；
审查代码、文件或报告时**必须先用工具真正打开内容再下判断**，凭记忆和摘要不算核验。
确实打不开就写"未找到"并把结论降为 `无法确认`，不编造内容后照常打分。

---

## 安装

```bash
git clone https://github.com/haomiaoya/second-look.git ~/.claude/skills/second-look
```

安装后确保目录名为 `second-look`，与 SKILL.md Frontmatter 的 `name` 一致。

| 客户端 | 用户级安装目录 | 项目安装目录 |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/second-look/` | `<project>/.claude/skills/second-look/` |
| Codex | `~/.agents/skills/second-look/` | `<project>/.agents/skills/second-look/` |

Windows PowerShell 的 `$HOME` 与 WSL2 的 Linux `~` 可能不同，请安装到你实际运行客户端所用的用户目录。若同时装了其他同类审查 Skill，建议删除旧目录以避免重复触发，而不是简单重命名。

---

## 文件结构

```text
second-look/
├── SKILL.md                    # 单入口、模式自动选择、审查流程及评分原则
├── README.md                   # 安装与使用
├── references/
│   ├── scoring-rubric.md       # 详细评分锚点与上限
│   ├── question-bank.md        # 高辨别力反问
│   ├── domain-checks.md        # 跨领域审查
│   ├── examples.md             # 报告示例
│   └── sources.md              # 理论与项目来源
├── scripts/score.py           # 可复算评分（Python 标准库）
└── tests/                     # 静态测试、行为验收场景、历史自审记录
```

---

## 验证

在 Skill 目录内运行：

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

请用 `tests/scenarios.md` 在实际 Claude Code / Codex 会话测试跨领域反问行为和评分校准。单元测试只验证脚本和文件一致性，不能证明真实 AI 反问质量。`tests/self-audit.md` 是早期设计自审记录，不代表本 Skill 已经过独立实测。
