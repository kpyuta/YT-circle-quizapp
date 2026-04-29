import streamlit as st

# ========== ステップ1: クイズのデータ ==========
# TODO: ここにクイズデータを書く
# 例：
 quizzes = [
    {
         "question": "日本の首都はどこ？",
         "options": ["大阪", "東京", "京都"],
         "correct": 1
     },
    {
         "question":"1 + 1 = ?",
         "options": ["1", "2", "3"],
         "correct": 1
    },
    {
         "question": "猫は英語で？",
         "options": ["Dog", "Cat", "Bird"],
         "correct": 1
    }

# ========== タイトル表示 ==========
st.title("🎯 クイズアプリ")


# ========== ステップ2: セッション状態の初期化 ==========  
# TODO: セッション状態を初期化
if 'current' not in st.session_state:
     st.session_state.current = 0  # 現在の問題番号
     st.session_state.score = 0    # 得点


# ========== ステップ3: クイズ表示 ==========
# TODO: クイズを表示する処理を書く
if st.session_state.current < len(quizzes):
    current_quiz = quizzes[st.session_state.current]
    
    st.write(f"### 問題{st.session_state.current + 1}: {current_quiz['question']}")
    
    answer = st.radio(
        "答えを選んでください：",
        current_quiz['options'],
        key=f"q{st.session_state.current}"
    )

# ========== ステップ4: 答えをチェック ==========
# TODO: 回答ボタンと正解判定の処理を書く
if st.button("回答する"):
    selected_index = current_quiz['options'].index(answer)
    
    if selected_index == current_quiz['correct']:
        st.success("🎉 正解！")
        st.session_state.score += 1
    else:
        st.error("😢 不正解...")
    
    st.session_state.current += 1
    st.rerun()


# ========== ステップ5: 結果表示 ==========
# TODO: 結果を表示する処理を書く
else:
    st.write("## 結果発表！")
    st.write(f"### {st.session_state.score} / {len(quizzes)} 問正解")
    
    if st.button("もう一度"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.rerun()
