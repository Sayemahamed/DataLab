import asyncio
from playwright.async_api import async_playwright, Browser, Page

async def main():
    async with async_playwright() as p:
        browser: Browser =await p.chromium.connect_over_cdp(
            endpoint_url="http://localhost:9222/", timeout=5000
        )
        page: Page = browser.contexts[0].pages[0]
        await page.goto(url="https://www.facebook.com/shopnillstore")
        await page.wait_for_timeout(timeout=5000)
        # await page.keyboard.press(key="PageDown")
        # await page.keyboard.press(key="PageDown")

if __name__ == "__main__":
    asyncio.run(main())