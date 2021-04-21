#!/usr/bin/env python

import subprocess
import time
import asyncio

import pyppeteer


async def main():
    browser = await pyppeteer.launch(args=["--no-sandbox"])
    page = await browser.newPage()
    await page.goto("http://localhost:8000")
    await page.screenshot({"path": "/github/home/screenshot.png"})
    await browser.close()


async def start_mkdocs():
    with subprocess.Popen(["mkdocs", "serve"], cwd="/github/workspace") as p:
        time.sleep(3.0)
        asyncio.get_event_loop().run_until_complete(main())
        p.kill()


with subprocess.Popen(
    ["pip", "install", "-r", "requirements.txt"], cwd="/github/workspace"
) as p:
    time.sleep(3.0)
    asyncio.get_event_loop().run_until_complete(start_mkdocs())
    p.kill()
