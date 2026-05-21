class ChatbotPage:

    def __init__(self, page):
        self.page = page
        self.text_area = "textarea"

    def open_chatbot(self):

        self.page.goto("https://huggingface.co/chat/")

        self.page.wait_for_timeout(5000)

    def enter_prompt(self, prompt):

        self.page.locator(
            self.text_area
        ).fill(prompt)

    def send_prompt(self):

        self.page.keyboard.press("Enter")

    def take_screenshot(self):

        self.page.screenshot(
            path="screenshots/chatbot_page.png"
        )