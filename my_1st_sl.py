import streamlit as st
from streamlit_option_menu import option_menu

# 페이지 설정
st.set_page_config(page_title="홍익대학교 프로젝트", layout="wide")

# 사이드바 메뉴
with st.sidebar:
    selected = option_menu("Menu", ["첫페이지", "두번째 페이지", "세번째 페이지", "네번째 페이지", "다섯번째 페이지"],
                           icons=['house', 'camera', 'book', 'pencil', 'link'], menu_icon="cast", default_index=0)

# 첫 번째 페이지: 과목명, 소속, 학번, 이름, 프로젝트 명
if selected == "첫페이지":
    st.image("image_page1.png")
    st.title("파이썬 프로그래밍 프로젝트")
    st.subheader("개인 프로젝트")
    st.markdown("""
    소속: 홍익대학교 기계시스템디자인공학과  
    학번: C017161  
    이름: 박세광
    """)

# 두 번째 페이지: 창업하고 싶은 아이템 사진과 제품명
elif selected == "두번째 페이지":
    st.title("창업하고 싶은 아이템")
    st.subheader("열전 물질을 이용한 무선 디퓨저")
    st.markdown("""
    열을 동력으로 사용하는 반도체를 이용하여 사용자가 원하는 향을 가진 향초를 기기에 넣고 향초를 점화하면 열이 발생한다. 
    해당 열을 통해서 프로펠러가 돌아가서 디퓨저가 있는 공간에 해당 향이 확산되는 인테리어 소품
    """)
    st.image(["image_page2_1.png", 
              "image_page2_2.png", 
              "image_page2_3.png", 
              "image_page2_4.png", 
              "https://raw.githubusercontent.com/<username>/<repository>/main/path_to_image6.png", 
              "image_page2_5.png"])

# 세 번째 페이지: 아이템 사진 두 개, 기존 제품의 방식, 단점
elif selected == "세번째 페이지":
    st.title("기존 제품의 방식과 단점")
    st.image("image_page3_2.png")
    st.image("image_page3_3.png")
    st.subheader("기존 제품의 방식")
    st.image("image_page3_1.png")
    st.markdown("""
    기존 제품 방식 : 향초를 넣어서 열로 모터를 돌리는 방식
    """)
    st.subheader("단점")
    st.markdown("""
    기존 제품 단점 : 향초의 향이 아닌 아로마 오일을 따로 주입하는 단점이 존재함, 30만원이라는 매우 비싼 가격
    """)

# 네 번째 페이지: 보완하려는 점 등
elif selected == "네번째 페이지":
    st.title("보완하려는 점")
    st.markdown("""
    기존 시장에 나와있는 제품이지만 해당 제품의 단점을 보완하면 좋을 것 같다라고 판단됨. 
    평소에 디자인에 관심이 있어서 인테리어 소품을 많이 보면서 영감을 얻는데 기존 제품은 가격이 너무 비싸게 책정되어 있다고 생각됨. 
    또한 해당 제품은 향을 확산시키기 위해서는 오일을 프로펠러 중앙에 주입하는 방식인데 해당 과정을 단순화해서 오일을 넣지 않고 
    원하는 향을 가진 향초를 직접 확산 시킬 수 있게끔 만들어 볼 생각입니다. 
    또한 기계공학과에서 배웠던 역학적인 지식들과 반도체 관련 지식들을 접목시켜 보다 더 안정적이고 신뢰도 있는 제품을 만들 생각입니다.
    """)

# 다섯 번째 페이지: 참고 문헌
elif selected == "다섯번째 페이지":
    st.title("참고 문헌")
    st.markdown("""
    - lei 디퓨저 - [https://shop.lei-aroma.com/ko-kr](https://shop.lei-aroma.com/ko-kr)  
    - 열전소자 - [https://gamma0burst.tistory.com/594](https://gamma0burst.tistory.com/594)
    """)
