# https://github.com/psf/requests
# requests를 이용해서 URL을 get하고 text로 HTML을 표시함
import requests

indeed_URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=%EA%B0%9C%EB%B0%9C%EC%9E%90&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch"

indeed_result = requests.get(indeed_URL)

print(indeed_result.text)

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/