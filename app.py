import streamlit as st

# ========== ステップ1: クイズのデータ ==========
# TODO: ここにクイズデータを書く
# 例：
quizzes = [
    {
         "question": "泣いても涙がでないや",
         "options": ["ちいかわ", "米津"],
         "correct": 0
    },
    {
         "question":"お前になんかやるもんか",
         "options": ["ちいかわ", "米津"],
         "correct": 1
    },
    {
         "question": "守りたいんだ みんなが戻ってくるまで",
         "options": ["ちいかわ", "米津"],
         "correct": 0
    },
    {
         "question": "この像に誓ったんだ 強くなると",
         "options": ["ちいかわ", "米津"],
         "correct": 0
    },
    {
         "question":"お前になんかやるもんか",
         "options": ["ちいかわ", "米津"],
         "correct": 1
    },
    {
         "question":"難解なパズルみたい",
         "options": ["ちいかわ", "米津"],
         "correct": 0
    },
    {
         "question":"そこから見ていてね 大丈夫ありがとう",
         "options": ["ちいかわ", "米津"],
         "correct": 1
    },
    {
         "question": "ヤンパパン ラララルルラ",
         "options": ["ちいかわ", "米津"],
         "correct": 0
    },
    {
         "question":"ヒッピヒッピシェイク ダンディダンディドン",
         "options": ["ちいかわ", "米津"],
         "correct": 1
    },
    {
         "question":"るるらったったったった",
         "options": ["ちいかわ", "米津"],
         "correct": 1
    }
 ]

# ========== タイトル表示 ==========
st.title("🎯ちいかわか米津玄師か当てるクイズ")


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
