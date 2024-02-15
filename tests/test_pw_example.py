from playwright.sync_api import expect


def test_todo(page):
    page.goto("https://www.yahoo.com/", wait_until='domcontentloaded')
    search_bar = page.get_by_placeholder("Search the web")
    expect(search_bar).to_be_editable()
    search_bar.click()
