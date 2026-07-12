from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://localhost:8000/index.html')

    # Wait for the download button to be visible
    page.wait_for_selector('#download-btn')

    # Ensure it's not disabled initially
    assert not page.is_disabled('#download-btn')

    # Focus it to test focus styles (though we can't easily assert the visual style, we can trigger it)
    page.focus('#download-btn')

    # Click the button
    page.click('#download-btn')

    # Ensure the button becomes disabled and shows the spinner SVG and correct text
    page.wait_for_selector('#download-btn[disabled]')
    text_content = page.text_content('#download-btn')
    assert "PDF wird erstellt..." in text_content

    # Check for the svg indicating loading
    assert page.query_selector('#download-btn svg.animate-spin') is not None

    print("Tests passed!")

    browser.close()
