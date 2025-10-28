#!/usr/bin/env python3
"""
Deprecated wrapper. Use: python scripts/downloader/main.py
"""
import asyncio
from scripts.downloader.main import run

if __name__ == "__main__":
    print("[DEPRECATED] Use `python scripts/downloader/main.py`. Running new pipeline...")
    asyncio.run(run())

