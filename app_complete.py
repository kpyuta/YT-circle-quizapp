import streamlit as st

# ========== ステップ1: クイズのデータ ==========
quizzes = [
    {
        "question": "日本の首都はどこ？",
        "options": ["大阪", "東京", "京都"],
        "correct": 1
    },
    {
        "question": "1 + 1 = ?",
        "options": ["1", "2", "3"],
        "correct": 1
    },
    {
        "question": "猫は英語で？",
        "options": ["Dog", "Cat", "Bird"],
        "correct": 1
    }
]

# ========== タイトル表示 ==========
st.title("🎯 クイズアプリ")

# ========== ステップ2: セッション状態の初期化 ==========
if 'current' not in st.session_state:
    st.session_state.current = 0
    st.session_state.score = 0

# ========== ステップ3: クイズ表示 ==========
if st.session_state.current < len(quizzes):
    # 現在の問題を取得
    current_quiz = quizzes[st.session_state.current]
    
    # 問題文を表示
    st.write(f"### 問題{st.session_state.current + 1}: {current_quiz['question']}")
    
    # 選択肢を表示（ラジオボタン）
    answer = st.radio(
        "答えを選んでください：",
        current_quiz['options'],
        key=f"q{st.session_state.current}"
    )
    
    # ========== ステップ4: 答えをチェック ==========
    if st.button("回答する", type="primary"):
        # 選択した答えのインデックスを取得
        selected_index = current_quiz['options'].index(answer)
        
        # 正解判定
        if selected_index == current_quiz['correct']:
            st.success("🎉 正解！")
            st.session_state.score += 1
        else:
            st.error(f"😢 不正解... 正解は「{current_quiz['options'][current_quiz['correct']]}」でした")
        
        # 次の問題へ
        st.session_state.current += 1
        
        # 画面を再読み込み
        st.rerun()

else:
    # ========== ステップ5: 結果表示 ==========
    st.write("## 🎊 結果発表！")
    
    # スコア表示
    score_percentage = (st.session_state.score / len(quizzes)) * 100
    st.write(f"### あなたの得点: {st.session_state.score} / {len(quizzes)} 問正解")
    st.progress(score_percentage / 100)
    
    # メッセージ表示
    if st.session_state.score == len(quizzes):
        st.balloons()
        st.success("🎉 完璧です！全問正解！")
    elif st.session_state.score >= len(quizzes) / 2:
        st.info("😊 いい感じ！半分以上正解！")
    else:
        st.warning("💪 次は頑張りましょう！")
    
    # もう一度ボタン
    if st.button("もう一度挑戦する", type="primary"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.rerun()
