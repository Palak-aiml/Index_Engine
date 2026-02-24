#!/usr/bin/env python3
"""
run_all_tests.py

Utility script to run all tests for Index Engine.
"""
import subprocess
import sys

result = subprocess.run([sys.executable, '-m', 'unittest', 'discover', 'tests'])
sys.exit(result.returncode)
