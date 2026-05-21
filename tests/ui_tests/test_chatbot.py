import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from playwright.sync_api import sync_playwright

from utils.logger import setup_logger


logger = setup_logger()


def test_chatbot_response():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=300
        )

        page = browser.new_page()

        try:

            logger.info("Opening chatbot app")

            page.goto("http://127.0.0.1:5000")

            page.wait_for_timeout(2000)

            logger.info("Entering prompt")

            page.locator(
                'input[name="prompt"]'
            ).fill("What is AI?")

            logger.info("Clicking send button")

            page.locator("button").click()

            page.wait_for_timeout(2000)

            content = page.content()

            logger.info("Validating AI response")

            assert "AI Response" in content

            logger.info("Test Passed Successfully")

        except Exception as e:

            logger.error(f"Test Failed: {e}")

            page.screenshot(
                path="screenshots/failure.png"
            )

            raise

        finally:

            browser.close()