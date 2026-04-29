# YT-circle-quizapp
YTサークルのクイズアプリ開発を実施

# Pythonクイズアプリ開発 - ミニアプリ開発会 🎯

Python + Streamlitで作る、初心者向けクイズアプリ開発テンプレートです。

## 🎓 このテンプレートについて

ミニアプリ開発会で使用する、Pythonクイズアプリの開発テンプレートです。
Streamlitを使ってWebアプリとして作ります。

## 🚀 デモ

完成イメージ：[Streamlit Cloud でデモを見る](https://あなたのアプリURL.streamlit.app/)

## 📋 準備（3つの方法）

### 方法1：Replit（推奨・環境構築不要）⭐⭐⭐⭐⭐

1. https://replit.com にアクセス
2. このリポジトリURLをインポート
3. 「Run」ボタンで即起動
4. `app.py` を編集して開発

### 方法2：GitHub Codespaces⭐⭐⭐⭐

1. 右上の「Code」→「Codespaces」
2. 「Create codespace on main」
3. ターミナルで `streamlit run app.py`
4. 開発スタート

### 方法3：ローカル環境⭐⭐⭐

**事前準備（必須）：**
```bash
# Python 3.8+ がインストールされているか確認
python --version

# Gitがインストールされているか確認
git --version
```

**セットアップ：**
```bash
# 1. リポジトリをクローン
git clone https://github.com/yourname/quiz-app-python-template.git
cd quiz-app-python-template

# 2. 仮想環境を作成（推奨）
python -m venv venv

# 3. 仮想環境を有効化
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. 必要なパッケージをインストール
pip install -r requirements.txt

# 5. アプリを起動
streamlit run app.py
```

ブラウザが自動で開き、アプリが表示されます。

## 📝 開発の流れ

### ステップ1: クイズのデータを作る（10分）

`app.py` の「ステップ1」にクイズのデータを書きます。

```python
quizzes = [
    {
        "question": "日本の首都はどこ？",
        "options": ["大阪", "東京", "京都"],
        "correct": 1  # 0から数える（東京は1番目）
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
```

### ステップ2: セッション状態の初期化（5分）

Streamlitでは、ページが再読み込みされるたびに変数がリセットされます。
`st.session_state` を使って状態を保持します。

```python
if 'current' not in st.session_state:
    st.session_state.current = 0  # 現在の問題番号
    st.session_state.score = 0    # 得点
```

### ステップ3: クイズを表示（30分）

```python
if st.session_state.current < len(quizzes):
    current_quiz = quizzes[st.session_state.current]
    
    st.write(f"### 問題{st.session_state.current + 1}: {current_quiz['question']}")
    
    answer = st.radio(
        "答えを選んでください：",
        current_quiz['options'],
        key=f"q{st.session_state.current}"
    )
```

### ステップ4: 答えをチェック（30分）

```python
if st.button("回答する"):
    selected_index = current_quiz['options'].index(answer)
    
    if selected_index == current_quiz['correct']:
        st.success("🎉 正解！")
        st.session_state.score += 1
    else:
        st.error("😢 不正解...")
    
    st.session_state.current += 1
    st.rerun()
```

### ステップ5: 結果を表示（20分）

```python
else:
    st.write("## 結果発表！")
    st.write(f"### {st.session_state.score} / {len(quizzes)} 問正解")
    
    if st.button("もう一度"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.rerun()
```

## 🎨 Streamlitの便利な機能

### ウィジェット

```python
st.button("ボタン")           # ボタン
st.radio("質問", ["A", "B"])  # ラジオボタン
st.checkbox("チェック")        # チェックボックス
st.slider("スライダー", 0, 100) # スライダー
st.selectbox("選択", ["A", "B"]) # セレクトボックス
```

### 表示

```python
st.write("テキスト")          # テキスト表示
st.title("タイトル")          # タイトル
st.header("ヘッダー")         # ヘッダー
st.success("成功メッセージ")  # 成功（緑）
st.error("エラーメッセージ")  # エラー（赤）
st.warning("警告")            # 警告（黄）
st.info("情報")              # 情報（青）
st.balloons()                # 風船アニメーション
```

### レイアウト

```python
col1, col2 = st.columns(2)   # 2カラムレイアウト
with col1:
    st.write("左")
with col2:
    st.write("右")
```

## 🚀 デプロイ（Streamlit Cloudで公開）

### 1. Streamlit Cloudにアクセス

https://share.streamlit.io/

### 2. GitHubアカウントでログイン

### 3. 「New app」をクリック

### 4. 設定

- Repository: このリポジトリを選択
- Branch: main
- Main file path: app.py

### 5. 「Deploy!」をクリック

数分で公開完了！URLが発行されます。

## 🎨 カスタマイズ例

### 問題を増やす

`quizzes` リストに問題を追加

### タイマー機能

```python
import time

start_time = time.time()
# ... クイズ処理 ...
elapsed_time = time.time() - start_time
st.write(f"かかった時間: {elapsed_time:.1f}秒")
```

### 画像を追加

```python
st.image("https://example.com/image.jpg", width=300)
```

### グラフ表示

```python
import pandas as pd

df = pd.DataFrame({
    '問題': [f'問題{i+1}' for i in range(len(quizzes))],
    '正解': [1 if i < st.session_state.score else 0 for i in range(len(quizzes))]
})
st.bar_chart(df.set_index('問題'))
```

## 📚 学習リソース

- [Streamlit公式ドキュメント](https://docs.streamlit.io/)
- [Python入門](https://www.python.jp/train/index.html)
- [Python チュートリアル](https://docs.python.org/ja/3/tutorial/)

## 🤝 サポート

わからないことがあったら、サポート役に声をかけてください！

## 📄 ファイル構成
