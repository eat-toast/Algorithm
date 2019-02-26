import pandas as pd
from selenium import webdriver
import time
pd.set_option('display.max_columns', 999)

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.naver.com/")  # 네이버 페이지로 이동

# 로그인 버튼
login_button = driver.find_element_by_class_name('ico_local_login')
login_button.click()

# 아이디 비번 입력

# 카페 이동
driver.get("https://m.cafe.naver.com")

# 자유게시판 주소
# EH, free_board = 'https://m.cafe.naver.com/ArticleList.nhn?search.clubid=29458417&search.menuid=1&search.boardtype=L'
free_board  = 'https://m.cafe.naver.com/ArticleList.nhn?search.clubid=29525506&search.menuid=1&search.boardtype=L' # SZ

# 자유게시판까지 간 다음, 모든 게시물 정보 가져오기

def naver_cafe(free_board)
    # 자유 게시판으로 이동
    driver.get(free_board)

    # 더 보기 버튼으로 맨 아래까지 내려가기.
    stop = 0
    while(stop == 1):
        try:
            button = driver.find_element_by_class_name('u_cbox_btn_more')
            button.click()
        except:
            stop = 1


    # 모든 게시글이 나왔을 때, href 값을 가져온다.
    x = driver.find_elements_by_class_name('board_box')
    # 링크 저장 장소
    link = []

    for i in range(len(x)):
        link.append(x[i].find_element_by_css_selector('a').get_attribute('href'))

    # URL 저장
    URL_link = pd.DataFrame(link, columns=['url'])
    URL_link['article'] = ''
    URL_link['title'] = ''

    # 게시글로 들어가 내용 가져오기.
    for i in range(len(link)):
        time.sleep(1)
        driver.get(URL_link['url'].iloc[i])
        URL_link['article'].iloc[i] = driver.find_element_by_id('postContent').text
        time.sleep(1)
        driver.back()


    return URL_link

cafe = naver_cafe(free_board)
cafe.to_csv('result/SZ_공카.csv', encoding='euc-kr', index = False )
