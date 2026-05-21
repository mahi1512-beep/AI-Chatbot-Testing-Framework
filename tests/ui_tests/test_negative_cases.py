import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from playwright.sync_api import sync_playwright


def test_empty_prompt():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=300
        )

        page = browser.new_page()

        page.goto("http://127.0.0.1:5000")

        page.wait_for_timeout(2000)

        # Empty input
        page.locator(
            'input[name="prompt"]'
        ).fill("")

        page.locator("button").click()

        page.wait_for_timeout(2000)

        content = page.content()

        print(content)

        browser.close()


def test_special_characters():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=300
        )

        page = browser.new_page()

        page.goto("http://127.0.0.1:5000")

        page.wait_for_timeout(2000)

        # Special character input
        page.locator(
            'input[name="prompt"]'
        ).fill("@#$%^&*()")

        page.locator("button").click()

        page.wait_for_timeout(2000)

        content = page.content()

        assert "AI Response" in content

        browser.close()


def test_long_prompt():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=300
        )

        page = browser.new_page()

        page.goto("http://127.0.0.1:5000")

        page.wait_for_timeout(2000)

        long_text = "AI " * 500

        page.locator(
            'input[name="prompt"]'
        ).fill(long_text)

        page.locator("button").click()

        page.wait_for_timeout(2000)

        content = page.content()

        assert "AI Response" in content

        browser.close()