「動かして学ぶ！Pythonサーバレスアプリ開発入門」 サンプルコード
====

「[動かして学ぶ！Pythonサーバレスアプリ開発入門](https://www.shoeisha.co.jp/book/detail/9784798169729)」のサンプルコードです。

<p align="center">
  <img src="https://m.media-amazon.com/images/I/51QnCB0lrdL.jpg" alt="動かして学ぶ！Pythonサーバレスアプリ開発入門"/>
</p>

## 概要

- `application`: サーバレスBlogアプリケーション
- `serverless-bot`: サーバレスBot
- `snippets`: 本文中のリストのスニペット（例：リスト6.2 -> list.6.2.txt）

`zappa_settings.json`は`zappa_settings.json.sample`としてサンプルを置いております。

## 誤字

### 環境変数 （誤）AWS_ACEESS_KEY_ID -> （正）AWS_ACCESS_KEY_ID

変更後の箇所は以下になります。(詳細は[こちら](https://github.com/chaingng/shoeisha_serverless_python_tutorial/commit/c6080953136b939b6af48d4c8ac1a74a8377f7b5)をご覧ください)


1. `~/.bashrc`
```
AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
```


2. `application/flask_blog/models/entries.py`
```
aws_access_key_id = app.config.get('AWS_ACCESS_KEY_ID')
```

3. `application/flask_blog/models/sessions.py`
```
aws_access_key_id = app.config.get('AWS_ACCESS_KEY_ID')
```

4. `application/flask_blog/config.py`
```
class DevelopmentConfig(Config):
    ....
    AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
    ....
    SESSION_DYNAMODB_KEY_ID = AWS_ACCESS_KEY_ID
    ....

class ProductionConfig(Config):
    ....
    AWS_ACCESS_KEY_ID = os.environ.get('SERVERLESS_AWS_ACCESS_KEY_ID')
    ....
    SESSION_DYNAMODB_KEY_ID = AWS_ACCESS_KEY_ID
```

## Q&A

### 1.Flask-Scriptがインストールできない

#### 原因

現時点(2021/07/20)のFlask-Scriptの最新バージョンにて、Flask2.0との組み合わせでバグ報告が上がっております。

```
$ python manage.py init_db
Traceback (most recent call last):
  File "C:\Users\xxx\workspace\python-serverless\application\manage.py", line 1, in <module>
    from flask_script import Manager
  File "C:\Users\xxx\.virtualenvs\application-rWZzxA8f\lib\site-packages\flask_script\__init__.py", line 15, in <module>
    from flask._compat import text_type
ModuleNotFoundError: No module named 'flask._compat'
```

#### 対応方法

Flaskバージョンを本書記載の1.1.2でインストールしてください。

```
pipenv install "Flask==1.1.2"
```

その後、Flask-Scriptのインストールが可能になります。

### 2.zappaのインストール時にコンフリクトが発生する

#### 原因

現時点(2021/07/20)のzappaの最新バージョン(0.53.0)では、Flaskバージョン1.0系にのみ対応しております。

そのため、Flaskバージョン2.0以上をインストールしている場合にはコンフリクトが発生します。

#### 対応方法

Flaskバージョンを本書記載の1.1.2でインストールしてください。

```
pipenv install "Flask==1.1.2"
```

その後、zappaのインストールが可能になります。


### 3.zappa deploy実行時にエラーが発生する

#### 原因

zappaの関連ライブラリのアップデートにより、zappaにて以下のエラーが発生しております。

```
Traceback (most recent call last):
  File "/Users/hondatakatomo/.local/share/virtualenvs/application-tAyQEiLX/lib/python3.8/site-packages/zappa/cli.py", line 3422, in handle
    sys.exit(cli.handle())
  File "/Users/hondatakatomo/.local/share/virtualenvs/application-tAyQEiLX/lib/python3.8/site-packages/zappa/cli.py", line 588, in handle
    self.dispatch_command(self.command, stage)
  File "/Users/hondatakatomo/.local/share/virtualenvs/application-tAyQEiLX/lib/python3.8/site-packages/zappa/cli.py", line 630, in dispatch_command
    self.deploy(self.vargs["zip"], self.vargs["docker_image_uri"])
  File "/Users/hondatakatomo/.local/share/virtualenvs/application-tAyQEiLX/lib/python3.8/site-packages/zappa/cli.py", line 952, in deploy
    template = self.zappa.create_stack_template(
  File "/Users/hondatakatomo/.local/share/virtualenvs/application-tAyQEiLX/lib/python3.8/site-packages/zappa/core.py", line 2417, in create_stack_template
    self.cf_template.add_description("Automatically generated with Zappa")
AttributeError: 'Template' object has no attribute 'add_description'
```

#### 対応方法

該当のzappa関連ライブラリである`troposphere`を、以下のバージョン指定でインストールしてください。

```
pipenv install "troposphere==2.7.1"
```

2021/08/04時点でのzappa最新バージョン0.53.0では未対応ですが
現在修正対応中のため、今後はzappaの最新バージョンにてエラーが発生しないよう対応される見込みです。
随時こちらでも情報をアップデートさせていただきます。

### 4. P177の python manage.py init_db で 「Unable to locate credentials」エラーが発生する

#### 原因

環境変数が正しく読み込まれていないことが原因になります。

```
...
botocore.exceptions.NoCredentialsError: Unable to locate credentials
...
```

#### 対応方法

以下の５つの環境変数が正しく設定されているか確認してみてください。

「[誤字](https://github.com/chaingng/shoeisha_serverless_python_tutorial/blob/master/README.md#%E8%AA%A4%E5%AD%97)」の項での値が正しく直っているか（`ACEESS` -> `ACCESS`）も再度ご確認ください。

```
SERVERLESS_BLOG_CONFIG
SERVERLESS_USER_PW
SERVERLESS_SECRET_KEY
SERVERLESS_AWS_ACCESS_KEY_ID
SERVERLESS_AWS_SECRET_KEY
```

設定後、windowsを再起動して環境変数が読み込まれているか確認してみてください。

### 5. 10章にてzappa deploy時に`Error: Warning! Status check on the deployed lambda failed. A GET request to '/' yielded a 502 response code.` が発生するが動作に問題ないか

Zappaのデフォルトでは、Webアプリケーションも動くことを想定しているため
エンドポイントが存在しない場合、つまり10章のスクリプトだけの場合には上記のWarningが表示されますが、動作に問題はございません。

もしWarningを消したい場合は、Configにて以下の設定を加えることで表示されなくなります。

```
{
    "dev": {
        "apigateway_enabled": false,
        ....
    }
}
```

本書ではWarning非表示のための設定を追記することでチュートリアルが煩雑になることを防ぐため、あえて注釈での説明のみにとどめておりましたが、こちらで追加説明させていただきます。

### 6. P146で「これまでセッション情報はローカルに保存していましたが」とあるものの、これまでセッションのコードは出てきていないためどの箇所で利用しているのか

前章8章の「ログイン機能を導入する」のところですが、前提としてログイン機能の実現にはセッションが必要となります。

そのため、`Flask-login`が内部的にFlaskのsession機構を利用しております。

ご質問の通り明示的な操作として出てきていなかったため、こちらにて補足させていただきます。
