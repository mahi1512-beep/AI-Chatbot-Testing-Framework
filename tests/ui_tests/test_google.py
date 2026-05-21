from playwright.sync_api import sync_playwright


def test_google_title():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        page = browser.new_page()

        page.goto("https://www.google.com")

        print(page.title())

        assert "Google" in page.title()

        page.wait_for_timeout(3000)

        browser.close()