from requests_html import HTMLSession

session = HTMLSession()
r = session.get("https://www.imdb.com/chart/top/")
r.html.render(timeout=20)  # simulates a browser

print(r.status_code)
print(r.html.text[:500])
