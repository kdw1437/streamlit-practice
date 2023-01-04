import streamlit as st

st.title('project')

item_list = ['item0','item1']

item_labels = {'item0':'intro', 'item1':'세미 프로젝트'}

FIL = lambda x: item_labels[x]
# 밑의 item이 어떻게 돌아가야 하는지 매뉴얼에 설명되어 있어야 한다.

item = st.sidebar.selectbox('항목을 골라요.', item_list, format_func = FIL)

if item == 'item1':
    # pandas

    import streamlit as st
    import pandas as pd

    url  = 'https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv'

    st.title('제주도 통계 데이터')

    df = pd.read_csv(url, encoding = 'euc-kr')

    st.dataframe(df)

    st.dataframe(df.head())

    st.dataframe(df.tail())
    

    
    # folium
    st.title('서울 지역 대학교 위치 데이터')
    import folium
    from streamlit_folium import folium_static


    seoul_map1 = folium.Map(location=[37.55, 126.98], tiles = 'Stamen Terrain', zoom_start = 12)
    seoul_map2 = folium.Map(location=[37.55, 126.98], tiles = 'Stamen Toner', zoom_start = 15)

    df2 = pd.read_excel('./서울지역 대학교 위치.xlsx', engine = 'openpyxl')

    for name, lat, lng in zip(df2.index, df2.위도, df2.경도):
        folium.Marker([lat,lng], popup = name).add_to(seoul_map1)

    folium_static(seoul_map1)

    for name, lat, lng in zip(df2.index, df2.위도, df2.경도):
        folium.CircleMarker([lat, lng],
                        radius = 10,
                        color = 'brown',
                        fill = True,
                        fill_color='coral',
                        fill_opacity=0.7,
                        popup=name
        ).add_to(seoul_map1)

    folium_static(seoul_map1)

    #    matplotlib
    import pandas as pd
    import matplotlib.pyplot as plt
    

elif item == 'item0':
    st.write("\n","streamlit 연습 프로젝트 입니다.")
