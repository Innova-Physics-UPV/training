"""Checks for the scripts in the repository root: one per team member."""

import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = sorted(ROOT.glob("*.py"))
EXPECTED_OUTPUT = "Hello World!\n"
UPV_USER = re.compile(r"[a-z][a-z0-9]*")


def test_scripts_found():
    assert SCRIPTS, f"no .py files found in {ROOT}"


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda p: p.name)
def test_filename_is_upv_user(script):
    assert UPV_USER.fullmatch(script.stem), (
        f"{script.name}: name it after your UPV user, in lowercase (e.g. msanlli.py)"
    )


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda p: p.name)
def test_prints_hello_world(script):
    result = subprocess.run(
        [sys.executable, script],
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, (
        f"{script.name} exited with code {result.returncode}:\n{result.stderr}"
    )
    assert result.stdout == EXPECTED_OUTPUT
