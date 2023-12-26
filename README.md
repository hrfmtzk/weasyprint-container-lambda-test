# AWS Lambda Container Runtime with WeasyPrint

Dockerfile は [Cloud Print Utils](https://github.com/kotify/cloud-print-utils) で提供されているものをベースにしています。

以下のような変更を加えています。

- Lambda 関数にバンドルするパッケージを `requirements.txt` からインストールする
- 日本語フォントのインストール
