import pandas as pd
from selenium import webdriver
import time


driver = webdriver.Chrome('chromedriver')

driver.get("https://www.naver.com/")  # 네이버 페이지로 이동

# 로그인 버튼
login_button = driver.find_element_by_class_name('ico_local_login')
login_button.click()

# 아이디 비번 입력

# 카페 이동
driver.get("https://m.cafe.naver.com")

# EH 자유게시판 주소
free_board = 'https://m.cafe.naver.com/ArticleList.nhn?search.clubid=29458417&search.menuid=1&search.boardtype=L'
driver.get(free_board)

# 첫 게시글을 참조. 더 보기 한계값에 이용
first_row_title = '카페 이용 시 참고해주세요.'

# 더 보기 버튼
button = driver.find_element_by_class_name('u_cbox_btn_more')
button.click()

# 어떻게 해야 될지 감이 안온다.

# 모든 게시글이 나왔을 때, href 값을 가져온다.
x = driver.find_elements_by_class_name('board_box')

#
link = []

for i in range(len(x)):
    link.append(x[i].find_element_by_css_selector('a').get_attribute('href'))

# URL 저장
URL_link = pd.DataFrame(link, columns=['url'])
URL_link['article'] = ''
URL_link['title'] = ''

for i in range(len(link)):
    time.sleep(1)
    driver.get(URL_link['url'].iloc[i])
    URL_link['article'].iloc[i] = driver.find_element_by_id('postContent').text
    time.sleep(1)
    driver.back()


for i in range(len(link)):
    URL_link['title'].iloc[i] = x[i].find_element_by_class_name('tit').text

URL_link.to_csv('result/공카_final.csv', encoding='euc-kr', index = False )
