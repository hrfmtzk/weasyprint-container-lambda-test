# AWS Lambda Container Runtime with WeasyPrint

AWS から提供されている Lambda 用コンテナをベースに以下のような変更を加えています。

- Lambda 関数にバンドルするパッケージを `requirements.txt` からインストールする
- 日本語フォントのインストール
- フォントキャッシュのディレクトリを変更
