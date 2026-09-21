import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_skill_metadata(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\n"))
        frontmatter = skill.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name: secure-red-team-hardening$")
        self.assertRegex(frontmatter, r"(?m)^description: .+")
        self.assertIn("authorized", skill.lower())

    def test_readme_local_links_exist(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", readme):
            if target.startswith(("https://", "http://", "#")):
                continue
            with self.subTest(target=target):
                self.assertTrue((ROOT / target).exists(), target)


if __name__ == "__main__":
    unittest.main()
