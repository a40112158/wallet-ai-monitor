"""入口：python run_once.py [--optimize]"""
from __future__ import annotations

import sys

from wallet_ai_monitor.pipeline import run

if __name__ == "__main__":
    force_opt = "--optimize" in sys.argv
    run(force_param_optimizer=force_opt)
