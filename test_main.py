"""Local tests for main.py: gate rules from the bounty kit.

The sealed scorer requires /output/entry.txt to be UTF-8 text of
1-200 characters, not only whitespace; the entry must be a single line
in the dog's own voice.
"""

import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.abspath(__file__))


class TestEntry(unittest.TestCase):
    def test_writes_valid_single_line(self):
        with tempfile.TemporaryDirectory() as tmp:
            out_dir = os.path.join(tmp, "output")
            os.makedirs(out_dir)
            # main.py writes to the fixed /output path; run it in a
            # sandbox copy by pointing OUTPUT_DIR via env is not
            # supported, so just run it and check its own output dir.
            result = subprocess.run(
                [sys.executable, os.path.join(REPO, "main.py")],
                capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            with open("/output/entry.txt", "rb") as f:
                raw = f.read()
            text = raw.decode("utf-8")  # must be valid UTF-8
            self.assertTrue(1 <= len(text) <= 200, len(text))
            self.assertTrue(text.strip(), "entry must not be only whitespace")
            self.assertNotIn("\n", text)
            self.assertNotIn("\r", text)
            self.assertIn("show your work", text)
            print(f"entry ({len(text)} chars): {text}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
