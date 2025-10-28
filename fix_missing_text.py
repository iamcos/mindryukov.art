#!/usr/bin/env python3
"""
Deprecated wrapper. Use: python scripts/repair/missing_text.py
"""
import asyncio
from scripts.repair.missing_text import main

if __name__ == "__main__":
    print("[DEPRECATED] Use `python scripts/repair/missing_text.py`. Running new repair...")
    asyncio.run(main())
