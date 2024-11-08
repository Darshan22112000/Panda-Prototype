import asyncio
from playwright.async_api import async_playwright

async def login_to_website():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Navigate to login URL
        await page.goto("https://www.panda.ie/d2d/")

        # Accept cookies if necessary (use selector for cookies consent button)
        await page.locator('//*[@id="wt-cli-accept-all-btn"]').click()

        # Fill in password and submit
        await page.fill('input[name="post_password"]', "PANDAD2DREP")
        await page.click('input[name="Submit"]')

        # Wait for the next page to load
        await page.wait_for_load_state('networkidle')

        # Get the current URL and cookies
        logged_in_url = page.url
        cookies = await page.context.cookies()

        print(f"Logged in URL: {logged_in_url}")
        print(f"Cookies: {cookies}")

        await browser.close()

# Run the Playwright automation
asyncio.run(login_to_website())
