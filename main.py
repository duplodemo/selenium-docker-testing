from webdriver_util import init


def query_google(keywords):
    print("Loading Firefox driver...")
    driver, waiter, selector, download_path = init()

    print("Fetching google front page...")
    driver.get("https://www.google.com")

    print("Taking a screenshot...")
    waiter.shoot("frontpage")

    print("Typing query string...")
    selector.get_and_clear("input[type=text]").send_keys(keywords)

    print("Hitting Enter...")
    # selector.get("button").click()
    ids = driver.find_elements_by_xpath("//input[@type='submit']")
    for ii in ids:
        ii.click()
        break

    print("Waiting for results to come back...")
    waiter.until_display("#ires")

    print
    print("The top search result is:")
    print
    print('    "{}"'.format(selector.get("#ires a").text))
    print


if __name__ == '__main__':
    query_google('test')
