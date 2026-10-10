# 思想来源与取舍

本 Skill 是原创整合流程，不复制任何单一项目的整篇文档。以下资料用于确定设计原则，部分开源项目只借鉴思想，不引入其依赖、角色设定或许可证代码。

| 来源 | 保留的长处 | 有意舍弃/修正 |
| --- | --- | --- |
| Barbara Minto, *The Pyramid Principle*（金字塔原理） | 结论先行→分组依据→证据细节 | 不要求创作原文本身变成报告体 |
| Richard Paul / Linda Elder, *Universal Intellectual Standards* | 清晰、准确、相关、逻辑、公平等思维检查 | 不在每次回答中填满所有维度 |
| Dhuliawala et al., *Chain-of-Verification* (ACL 2024) | 先起草核验问题，再从原始资料独立回答，更新结论 | 不把自问自答当成真实外部验证 |
| Gary Klein, *Performing a Project Premortem* (HBR, 2007) | 假设失败，逆推原因及早期信号 | 不凭空编造灾难 |
| obra/superpowers, *verification-before-completion* | 没有新鲜证据，不声称已完成/已解决 | 非代码任务的验证方法不局限于命令 |
| obra/superpowers, *subagent-driven-development* | 需求符合性审查与质量审查分开 | 不要求所有任务都启动子代理或复杂流水线 |
| alirezarezvani/claude-skills, *adversarial-reviewer* | 换视角挑战既有结论 | **明确取消“每个视角必须找出问题”**，避免虚构瑕疵 |
| OpenAI / Anthropic Skill Creator & Agent Skills Spec | YAML 元信息、触发描述、按需加载 references、测试样例 | 主文件保持轻量，不捆绑脚本依赖 |

原始链接：
- https://www.criticalthinking.org/pages/universal.intellectual-standard/527
- https://aclanthology.org/2024.findings-acl.212/
- https://hbr.org/2007/09/performing-a-project-premortem
- https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
- https://github.com/alirezarezvani/claude-skills/blob/main/engineering-team/skills/adversarial-reviewer/SKILL.md
- https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md
- https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- https://agentskills.io/specification
- https://code.claude.com/docs/en/skills
- https://learn.chatgpt.com/docs/build-skills

设计依据的关键区别：批判性思考 ≠ 唱反调；完成动作 ≠ 实现目标；自我解释 ≠ 证据；金字塔 ≠ 文字套模板。

## v2.0 评分体系新增参考

- [OpenAI Codex Skill Creator](https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md)：只保留能改变模型决策的具体规则；区分结构验证与真实行为评测；修改前后验证。
- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)：评估需要明确任务、测量规则、轨迹/可观察证据，不能只看文字自评。
- [OpenAI Evals / Graders](https://developers.openai.com/api/docs/guides/graders)：可采用明确的分项、部分得分、基准用例，并通过样本迭代量表；此处是借鉴可复核评测思路，不依赖其 API。
- [Agent Skills Specification](https://agentskills.io/specification)：目录、YAML frontmatter、references 渐进式披露与验证边界。

**本 Skill 的五维权重与评分锚点属于面向通用个人使用的工程设计选择，不声称是上述文献规定或经过大规模实证校准的客观标准。**
