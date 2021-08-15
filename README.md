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

環境変数の設定方法は２つあります。

1. windowsのシステム環境設定から設定(macの場合は.bashrc)
1. `.env`にて設定

##### 1.windowsのシステム環境設定から設定する方法(macの場合は.bashrc)

以下の５つの環境変数が正しく設定されているか確認してみてください。

```
SERVERLESS_BLOG_CONFIG=production
SERVERLESS_USER_PW=xxxx
SERVERLESS_SECRET_KEY=xxxx
SERVERLESS_AWS_ACCESS_KEY_ID=[AWSアクセスキーID]
SERVERLESS_AWS_SECRET_KEY=[AWSシークレットキー]
```

設定後、windowsを再起動して環境変数が読み込まれているか確認してみてください。

##### 2. .envにて設定する方法

本文では解説しておりませんが、Pipenvの機能の１つで、`.env`ファイルをPipfileと同じ箇所に設定すると環境変数として読み込まれる機能があります。

環境変数の設定の仕方にお困りの方に、こちらも合わせて解説します。

例として、windowsで問題が発生する方が多かったため、windowsの場合の手順を解説します。

1. windowsのシステム環境設定から、関連する環境変数を削除（SERVERLESS〜で始まる5つの値）
3. windowsを再起動
4. 再度システム環境変数を確認し削除されていることを確認
5. applicationフォルダ直下（Pipfileと同じ場所）に「.env」という名前でファイルを作成し、以下の内容を記載

```
SERVERLESS_BLOG_CONFIG=production
SERVERLESS_USER_PW=xxxx
SERVERLESS_SECRET_KEY=xxxx
SERVERLESS_AWS_ACCESS_KEY_ID=[AWSアクセスキーID]
SERVERLESS_AWS_SECRET_KEY=[AWSシークレットキー]
```

上記が完了しましたら、以下のコマンドを実行してみてください。

```
python mange.py init_db
```

正しく.envファイルが読み込まれていましたら、「Loading .env environment variables...」とうメッセージが表示されます。
読み込まれない場合は、以下が原因になります。

1. `.env`が正しい場所に置かれていない
1. `.env`ファイルが正しく作成されていない

１の場合は、Pipfileと同じ場所に`.env`ファイルが置かれているか確認してみてください。

２の場合は、applicationフォルダ直下で以下のコマンドを打ってファイルの中身が表示されるかも確認してみてください。(windowsの場合のコマンドです)
```
type .env
```

