# https://github.com/psf/requests
# requests를 이용해서 URL을 get하고 text로 HTML을 표시함
import requests

indeed_URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=JavaScript&radius=25&limit=50"

indeed_result = requests.get(indeed_URL)

print(indeed_result.text)

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/