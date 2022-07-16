「動かして学ぶ！Pythonサーバレスアプリ開発入門」 サンプルコード
====

「[動かして学ぶ！Pythonサーバレスアプリ開発入門](https://www.shoeisha.co.jp/book/detail/9784798169729)」のサンプルコードです。

<p align="center">
  <img src="https://m.media-amazon.com/images/I/51QnCB0lrdL.jpg" alt="動かして学ぶ！Pythonサーバレスアプリ開発入門"/>
</p>

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [概要](#%E6%A6%82%E8%A6%81)
- [誤字](#%E8%AA%A4%E5%AD%97)
  - [環境変数 （誤）AWS_ACEESS_KEY_ID -> （正）AWS_ACCESS_KEY_ID](#%E7%92%B0%E5%A2%83%E5%A4%89%E6%95%B0-%E8%AA%A4aws_aceess_key_id---%E6%AD%A3aws_access_key_id)
- [QA](#qa)
  - [1.Flask-Scriptがインストールできない](#1flask-script%E3%81%8C%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84)
    - [原因](#%E5%8E%9F%E5%9B%A0)
    - [対応方法](#%E5%AF%BE%E5%BF%9C%E6%96%B9%E6%B3%95)
  - [2.zappaのインストール時にコンフリクトが発生する](#2zappa%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%99%82%E3%81%AB%E3%82%B3%E3%83%B3%E3%83%95%E3%83%AA%E3%82%AF%E3%83%88%E3%81%8C%E7%99%BA%E7%94%9F%E3%81%99%E3%82%8B)
    - [原因](#%E5%8E%9F%E5%9B%A0-1)
    - [対応方法](#%E5%AF%BE%E5%BF%9C%E6%96%B9%E6%B3%95-1)
  - [3.zappa deploy実行時にエラーが発生する](#3zappa-deploy%E5%AE%9F%E8%A1%8C%E6%99%82%E3%81%AB%E3%82%A8%E3%83%A9%E3%83%BC%E3%81%8C%E7%99%BA%E7%94%9F%E3%81%99%E3%82%8B)
    - [原因](#%E5%8E%9F%E5%9B%A0-2)
    - [対応方法](#%E5%AF%BE%E5%BF%9C%E6%96%B9%E6%B3%95-2)
  - [4. P177の python manage.py init_db で 「Unable to locate credentials」エラーが発生する](#4-p177%E3%81%AE-python-managepy-init_db-%E3%81%A7-unable-to-locate-credentials%E3%82%A8%E3%83%A9%E3%83%BC%E3%81%8C%E7%99%BA%E7%94%9F%E3%81%99%E3%82%8B)
    - [原因](#%E5%8E%9F%E5%9B%A0-3)
    - [対応方法](#%E5%AF%BE%E5%BF%9C%E6%96%B9%E6%B3%95-3)
  - [5. 10章にてzappa deploy時に`Error: Warning! Status check on the deployed lambda failed. A GET request to '/' yielded a 502 response code.` が発生するが動作に問題ないか](#5-10%E7%AB%A0%E3%81%AB%E3%81%A6zappa-deploy%E6%99%82%E3%81%ABerror-warning-status-check-on-the-deployed-lambda-failed-a-get-request-to--yielded-a-502-response-code-%E3%81%8C%E7%99%BA%E7%94%9F%E3%81%99%E3%82%8B%E3%81%8C%E5%8B%95%E4%BD%9C%E3%81%AB%E5%95%8F%E9%A1%8C%E3%81%AA%E3%81%84%E3%81%8B)
  - [6. P146で「これまでセッション情報はローカルに保存していましたが」とあるものの、これまでセッションのコードは出てきていないためどの箇所で利用しているのか](#6-p146%E3%81%A7%E3%81%93%E3%82%8C%E3%81%BE%E3%81%A7%E3%82%BB%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%E6%83%85%E5%A0%B1%E3%81%AF%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%AB%E3%81%AB%E4%BF%9D%E5%AD%98%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%81%97%E3%81%9F%E3%81%8C%E3%81%A8%E3%81%82%E3%82%8B%E3%82%82%E3%81%AE%E3%81%AE%E3%81%93%E3%82%8C%E3%81%BE%E3%81%A7%E3%82%BB%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AF%E5%87%BA%E3%81%A6%E3%81%8D%E3%81%A6%E3%81%84%E3%81%AA%E3%81%84%E3%81%9F%E3%82%81%E3%81%A9%E3%81%AE%E7%AE%87%E6%89%80%E3%81%A7%E5%88%A9%E7%94%A8%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%81%AE%E3%81%8B)
  - [7. P157の`.bashrc`の環境変数はP.175で`zappa_settings.json`で設定しているので不要ではないか](#7-p157%E3%81%AEbashrc%E3%81%AE%E7%92%B0%E5%A2%83%E5%A4%89%E6%95%B0%E3%81%AFp175%E3%81%A7zappa_settingsjson%E3%81%A7%E8%A8%AD%E5%AE%9A%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%81%AE%E3%81%A7%E4%B8%8D%E8%A6%81%E3%81%A7%E3%81%AF%E3%81%AA%E3%81%84%E3%81%8B)
  - [8. Mac M1を使っている場合にどのPythonバージョンをインストールすればよいか](#8-mac-m1%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%84%E3%82%8B%E5%A0%B4%E5%90%88%E3%81%AB%E3%81%A9%E3%81%AEpython%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8C%E3%81%B0%E3%82%88%E3%81%84%E3%81%8B)
  - [9. P177でpython manage.py init_dbを実行すると 「AccessDeniedException」エラーが発生するがzappa-exec-userの権限が不足しているか](#9-p177%E3%81%A7python-managepy-init_db%E3%82%92%E5%AE%9F%E8%A1%8C%E3%81%99%E3%82%8B%E3%81%A8-accessdeniedexception%E3%82%A8%E3%83%A9%E3%83%BC%E3%81%8C%E7%99%BA%E7%94%9F%E3%81%99%E3%82%8B%E3%81%8Czappa-exec-user%E3%81%AE%E6%A8%A9%E9%99%90%E3%81%8C%E4%B8%8D%E8%B6%B3%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%81%8B)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

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

## QA

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

以下のコマンドで、下記のライブラリをバージョン指定でインストールしてください。

```
pipenv install "Flask==1.1.2"
pipenv install "Jinja2==3.0.3"
pipenv install "itsdangerous==2.0.1"
pipenv install "Werkzeug==0.15.6"
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

その後、すでに`zappa deploy`を実施していた場合は一度`undeploy`してから再度`deploy`してください。

```
zappa undeploy dev
zappa deploy dev
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

### 7. P157の`.bashrc`の環境変数はP.175で`zappa_settings.json`で設定しているので不要ではないか

`.bashrc`の環境変数ですが2つの理由で作成しております。

1つめは、ローカルで本番用データベースの作成コマンドを実行するためです。


2つめは、それぞれの環境で動作確認および切り分けしながらステップごとに進められるよう用意しました。

- ローカル環境でDyanmoDB localで動作確認
- ローカル環境で本番DynamoDBでの動作確認
- サーバレス環境で本番DynamoDBでの動作確認

問題があったときにどの環境まで正しく動作しているか切り分けたり、
コードをアップデートしたときに順に動作確認することで急に大きな問題が発生することを防いだり、
また本書の構成としてステップごとに学んでいただけるようにというコンセプトも理由としてございます。

### 8. Mac M1を使っている場合にどのPythonバージョンをインストールすればよいか

[Support macOS 11 and Apple Silicon Macs](https://bugs.python.org/issue41100)にあるとおり、Python3.8以降ではM1もサポートされています。

Python3.9以降を新規で使いたい場合は[リリースニュース](https://www.python.org/downloads/release/python-391/)である通り
Apple Siliconに対応したuniversal版のインストーラーをお使いください。

### 9. P177でpython manage.py init_dbを実行すると 「AccessDeniedException」エラーが発生するがzappa-exec-userの権限が不足しているか

本書では、2つのIAMユーザを作成しております。
- `flask-blog-dynamodb`: DynamoDBを操作するためのIAMユーザ
- `zappa-exec-user`: Zappaを使ってサーバレスにデプロイするためのIAMユーザ

そのため、本書の通り`flask-blog-dynamodb`をお使いください。

権限を追加することで、1つのIAMユーザのみですべての操作を行うことも可能です。
本書では締切の関係上掲載できなかったため、興味がありましたら元となっております[Pythonで作るはじめてのサーバレスアプリケーション](https://www.amazon.co.jp/dp/B07JD6NDS7)も合わせてご参考ください。

