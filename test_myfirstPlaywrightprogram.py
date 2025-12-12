from playwright.sync_api import sync_playwright

# Event handler for dialog (alert/confirm/prompt)
def handle_dialog(dialog):
    print(f"Dialog message: {dialog.message}")
    print(f"Dialog type: {dialog.type}")
    if dialog.type == "prompt":
        dialog.accept("Harsh Gujral")  # 👈 Type text into the prompt
    else:
        dialog.accept()
        
def test_dialog_handling():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        brsrcontext = browser.new_context()
        brsrcontext.clear_cookies()
        page = brsrcontext.new_page()
        #page.context.set_default_timeout(4000)
        page.context.clear_cookies()
        page.goto("https://demo.automationtesting.in/Register.html")
        page.get_by_role("link", name="SwitchTo").click()
        page.get_by_role("link", name="Alerts").click()
        page.get_by_role("link", name="Alert with Textbox").click()
        #page.wait_for_timeout(1000)
        page.on("dialog", handle_dialog)
        #page.wait_for_timeout(1000)
        page.get_by_role("button", name="click the button to demonstrate the prompt box ").click()
        browser.close()
    
 