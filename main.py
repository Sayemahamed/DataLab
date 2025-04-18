import asyncio
from playwright.async_api import async_playwright, Browser, Page

async def main():
    async with async_playwright() as p:
        browser: Browser =await p.chromium.connect_over_cdp(
            endpoint_url="http://localhost:9222/", timeout=5000
        )
        page: Page = browser.contexts[0].pages[1]
        await page.goto(url="https://www.glassdoor.com/Reviews/index.htm")
        await page.wait_for_timeout(timeout=5000)
        search_box = page.locator('[aria-label="Search for a company"]')
        await search_box.click()  
        await search_box.fill("Microsoft")  
        await search_box.press("Enter")
        await page.wait_for_timeout(timeout=5000)
        box =page.locator('[data-test="company-card"]').first
        await box.click()
        await page.wait_for_timeout(timeout=5000)
        await page.locator('#reviews').click()
        await page.wait_for_timeout(timeout=5000)
        loop:bool =True
        while loop:
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            await page.wait_for_timeout(timeout=5000)
            buttons = page.locator('.expand-button_ExpandButton__Wevvg')
            containers = page.locator('[data-test="review-details-container"]')
            for i in range(await buttons.count()):
                try:
                    button = buttons.nth(i)
                    await button.click(timeout=5000)
                    await page.locator('[data-test="review-subratings-caret-tooltip"]').click()
                    await page.wait_for_timeout(timeout=5000)
                    print(await containers.nth(i).inner_text())
                except Exception:
                    pass
            next_button = page.locator('[data-test="next-page"]')
            if await next_button.count() > 0:
                loop = True
                await next_button.click()
                await page.wait_for_timeout(timeout=5000)
            else:
                loop = False
            


if __name__ == "__main__":
    asyncio.run(main())