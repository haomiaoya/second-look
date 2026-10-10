"""Structural checks only; these do not validate model behavior."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")


class StructureTest(unittest.TestCase):
    def test_frontmatter_identity(self):
        self.assertTrue(SKILL.startswith("---\n"))
        parts = SKILL.split("---\n", 2)
        self.assertEqual(len(parts), 3)
        name = re.search(r"^name:\s*(\S+)\s*$", parts[1], re.M)
        self.assertIsNotNone(name)
        self.assertEqual(name.group(1), ROOT.name)
        self.assertRegex(name.group(1), r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

    def test_metadata_and_size(self):
        header = SKILL.split("---\n", 2)[1]
        self.assertIn("description:", header)
        self.assertLess(len(header), 1300)
        self.assertLess(len(SKILL.splitlines()), 500)

    def test_references_exist(self):
        refs = set(re.findall(r"(?:references|scripts)/[\w-]+\.(?:md|py)", SKILL))
        self.assertGreaterEqual(len(refs), 6)
        for ref in refs:
            with self.subTest(reference=ref):
                self.assertTrue((ROOT / ref).is_file())

    def test_single_entry_and_install_identity(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("$second-look", readme)
        self.assertIn("name: second-look", SKILL)
        self.assertIn("不要求附加", SKILL)
        self.assertNotIn("$critical-inquiry", SKILL)
        self.assertNotIn("$critical-inquiry", readme)

    def test_output_template_shape(self):
        for head in ("### 一、原始需求", "### 二、审查结论", "### 三、核心依据",
                     "### 四、改进与闭环（PDCA）", "### 五、本次评分"):
            self.assertIn(head, SKILL)
        for label in ("**要解决的问题：**", "**预期目标：**", "**结果：**",
                      "**1. 需求完成情况**", "**2. 实际效果验证**", "**3. 遗留问题与潜在风险**",
                      "**下一步：**", "**综合评分：[X.X]/10**", "**评价：**", "**得分依据：**", "**最终意见：**"):
            self.assertIn(label, SKILL)
        self.assertIn("| 优先级 | 存在的问题 | 改进措施 | 验收标准 |", SKILL)
        self.assertIn("**只有第四段用表格**", SKILL)

    def test_evidence_grade_vocabulary_consistent(self):
        grade = "[有依据未实测]"
        stale = "[有依据但未实测]"
        for rel in ("SKILL.md", "README.md", "references/examples.md",
                    "references/scoring-rubric.md"):
            with self.subTest(file=rel):
                text = (ROOT / rel).read_text(encoding="utf-8")
                self.assertNotIn(stale, text)
        self.assertIn(grade, SKILL)

    def test_three_mandatory_rules(self):
        for rule in ("原始需求是评审基准", "不是固定凑三点", "评分永远放最后"):
            self.assertIn(rule, SKILL)
        self.assertIn("PDCA", SKILL)

    def test_examples_follow_template(self):
        ex = (ROOT / "references" / "examples.md").read_text(encoding="utf-8")
        for head in ("### 一、原始需求", "### 二、审查结论", "### 三、核心依据",
                     "### 四、改进与闭环（PDCA）", "### 五、本次评分"):
            self.assertIn(head, ex)
        for label in ("**要解决的问题：**", "**结果：**", "**综合评分：**", "**最终意见：**"):
            self.assertIn(label, ex)
        self.assertIn("| 优先级 | 存在的问题 | 改进措施 | 验收标准 |", ex)
        self.assertIn("有依据未实测", ex)
        self.assertNotIn("决定性反问", ex)
        self.assertNotIn("关键反问", ex)

    def test_section_names_consistent(self):
        sec = "遗留问题与潜在风险"
        for rel in ("SKILL.md", "README.md", "references/examples.md",
                    "tests/scenarios.md"):
            with self.subTest(file=rel):
                self.assertIn(sec, (ROOT / rel).read_text(encoding="utf-8"))
        for rel in ("SKILL.md", "references/examples.md", "tests/scenarios.md"):
            with self.subTest(stale=rel):
                self.assertNotIn("遗留问题与风险**", (ROOT / rel).read_text(encoding="utf-8"))
        stale2 = "未发现遗留问题"
        for rel in ("SKILL.md", "tests/scenarios.md"):
            with self.subTest(stale2=rel):
                self.assertNotIn(stale2, (ROOT / rel).read_text(encoding="utf-8"))

    def test_no_overlap_between_risks_and_actions(self):
        self.assertIn("三-3 与四不得重复同一条问题", SKILL)
        self.assertIn("本次不处理", SKILL)
        ex = (ROOT / "references" / "examples.md").read_text(encoding="utf-8")
        self.assertIn("本节只写看到了但本次不处理的问题", ex)
        # 示例 A 的三-3 段落不得出现 P0
        seg = ex.split("**3. 遗留问题与潜在风险**")[1].split("### 四、")[0]
        self.assertNotIn("[P0]", seg)

    def test_scoring_rubric_and_runner_present(self):
        rubric = (ROOT / "references" / "scoring-rubric.md").read_text(encoding="utf-8")
        self.assertIn("25", rubric)
        self.assertIn("20", rubric)
        self.assertIn("15", rubric)
        self.assertTrue((ROOT / "scripts" / "score.py").is_file())


if __name__ == "__main__":
    unittest.main()
