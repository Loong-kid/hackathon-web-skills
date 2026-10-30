import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("bundle_install", ROOT / "install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "project with spaces"

    def run_installer(self, *args):
        return subprocess.run([sys.executable, str(ROOT / "install.py"), *map(str, args)],
                              capture_output=True, encoding="utf-8")

    def test_web_profile_installs_complete_skills_and_is_idempotent(self):
        first = self.run_installer("--profile", "web", "--project", self.project)
        self.assertEqual(first.returncode, 0, first.stderr)
        target = self.project / ".agents/skills"
        catalog = installer.load_catalog()
        self.assertEqual({p.name for p in target.iterdir()}, set(catalog["profiles"]["web"]))
        for name in catalog["profiles"]["web"]:
            self.assertEqual(installer.snapshot(target / name), catalog["skills"][name]["sha256"])
        second = self.run_installer("--profile", "web", "--project", self.project)
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertIn("Already installed", second.stdout)

    def test_selection_preserves_references_and_claude_target(self):
        result = self.run_installer("--skills", "hallmark", "--agent", "claude", "--project", self.project)
        self.assertEqual(result.returncode, 0, result.stderr)
        target = self.project / ".claude/skills"
        self.assertEqual([p.name for p in target.iterdir()], ["hallmark"])
        self.assertTrue((target / "hallmark/references/slop-test.md").is_file())

    def test_conflict_preflight_preserves_existing_and_avoids_partial_install(self):
        existing = self.project / ".agents/skills/frontend-design"
        existing.mkdir(parents=True)
        (existing / "SKILL.md").write_text("Existing user's work", encoding="utf-8")
        result = self.run_installer("--profile", "web", "--project", self.project)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((existing / "SKILL.md").read_text(), "Existing user's work")
        self.assertFalse((existing.parent / "web-build").exists())

    def test_dry_run_writes_nothing(self):
        result = self.run_installer("--profile", "all", "--project", self.project, "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.project.exists())

    def test_custom_target(self):
        target = Path(self.temp.name) / "custom skills"
        result = self.run_installer("--skills", "web-check", "--target", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((target / "web-check/SKILL.md").is_file())

    def test_unknown_and_traversal_names_write_nothing(self):
        for name in ("not-a-skill", "../escape"):
            result = self.run_installer("--skills", name, "--project", self.project)
            self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.project.exists())

    def test_corrupt_bundle_fails_before_any_copy(self):
        bundle = Path(self.temp.name) / "corrupt bundle"
        shutil.copytree(ROOT / "skills", bundle / "skills")
        shutil.copy2(ROOT / "catalog.json", bundle / "catalog.json")
        shutil.copy2(ROOT / "install.py", bundle / "install.py")
        (bundle / "skills/frontend-design/SKILL.md").write_text("tampered", encoding="utf-8")
        result = subprocess.run([sys.executable, str(bundle / "install.py"), "--profile", "web",
                                 "--project", str(self.project)], capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.project.exists())


if __name__ == "__main__":
    unittest.main()
