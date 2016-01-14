# Django_Class_based_view_Sample

## セットアップ
```
# 任意のGit用ディレクトリへ移動
>cd path\to\dir

# GitHubからカレントディレクトリへclone
path\to\dir>git clone https://github.com/thinkAmi-sandbox/Django_Class_based_view_Sample.git

# virtualenv環境の作成とactivate
path\to\dir>virtualenv -p c:\python34\python.exe env
path\to\dir>env\Scripts\activate

# requirements.txtよりインストール
(env)path\to\dir>pip install -r requirements.txt

# マイグレーション
(env)path\to\dir>python manage.py migrate

# 開発サーバの起動
(env)path\to\dir>python manage.py runserver

# 開発サーバのURLを既定のブラウザで開く
# (別のコマンドプロンプトを開いて実行)
>start http://localhost:8000/mysite/create
```

　  
## テスト環境

- Windows10
- Python 3.4.3
- Django 1.9.1

　  
## 関係するブログ

- [Djangoで、Class-based generic views + ModelForm を使ってみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/01/15/001903)