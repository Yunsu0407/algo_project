# app.py

import os
import sys
import streamlit as st
import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT)

from case1.case1 import excute_case1
from case2.case2 import excute_case2
from algorithm.dijkstra import dijkstra
from algorithm.bellman_ford import bellman_ford
from algorithm.floyd_warshall import floyd_warshall_shortest
from util.visualize import visualize_graph
from data.list import building_list


# 실행 명령어
# streamlit run code/streamlit/app.py

# 제목
st.markdown("## 강의실 간 학생 이동 경로 최소화 시스템")

# 경로 선택
st.markdown("### ➡️ 경로 선택", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    start = st.selectbox("출발지", building_list)
with col2:
    available_ends = [b for b in building_list if b != start]
    end = st.selectbox("도착지", available_ends)


if st.button("경로 계산하기"):
    st.markdown("---")  # 시각적 구분선
    st.markdown("### 📌 알고리즘 실행 결과 비교")
    nodes_case1 = excute_case1()
    nodes_case2 = excute_case2()

    # Case1 계산
    d1_time, d1_cost, d1_path = dijkstra(nodes_case1, start, end)
    b1_time, b1_cost, b1_path = bellman_ford(nodes_case1, start, end)
    f1_time, f1_cost, f1_path = floyd_warshall_shortest(nodes_case1, start, end)
    df_case1 = pd.DataFrame(
        {
            "Algorithm": ["Dijkstra", "Bellman-Ford", "Floyd-Warshall"],
            "Execution Time (µs)": [
                round(d1_time * 1000, 2),
                round(b1_time * 1000, 2),
                round(f1_time * 1000, 2),
            ],
            "Shortest Cost": [d1_cost, b1_cost, f1_cost],
            "Path": [
                " → ".join(d1_path),
                " → ".join(b1_path),
                " → ".join(f1_path),
            ],
        }
    )

    # Case2 계산
    d2_time, d2_cost, d2_path = dijkstra(nodes_case2, start, end)
    b2_time, b2_cost, b2_path = bellman_ford(nodes_case2, start, end)
    f2_time, f2_cost, f2_path = floyd_warshall_shortest(nodes_case2, start, end)
    df_case2 = pd.DataFrame(
        {
            "Algorithm": ["Dijkstra", "Bellman-Ford", "Floyd-Warshall"],
            "Execution Time (µs)": [
                round(d2_time * 1000, 2),
                round(b2_time * 1000, 2),
                round(f2_time * 1000, 2),
            ],
            "Shortest Cost": [d2_cost, b2_cost, f2_cost],
            "Path": [
                " → ".join(d2_path),
                " → ".join(b2_path),
                " → ".join(f2_path),
            ],
        }
    )

    st.markdown("#### 🎯 Case 1 결과")
    st.dataframe(df_case1, use_container_width=True)

    st.markdown("#### 🎯 Case 2 결과")
    st.dataframe(df_case2, use_container_width=True)

    st.markdown("---")
    st.markdown("### 📊 그래프 복잡도")

    # col1, col2 = st.columns(2)

    # with col1:
    st.markdown("#### 📍 Case 1 복잡도")
    st.image("data/case1_graph.png", caption="Case 1 Graph")

    # with col2:
    st.markdown("#### 📍 Case 2 복잡도")
    st.image("data/case2_graph.png", caption="Case 2 Graph")
