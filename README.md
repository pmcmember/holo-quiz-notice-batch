# holo-quiz-notice-batch
ホロライブクイズアプリの Slack通知を行うスクリプトバッチです<br>
AWS関連の処理は未作成

## 処理内容
Croud Watch Events を使用して　AWS Lambdaの定期実行を行い　定期的に以下の処理を行います。

1. MicroCMSから追加・更新リクエスト状態のクイズの件数を取得
1. 件数を[Slackのアラート部屋]へ通知
    1. リクエスト件数が0件の場合は通知は行いません

## ローカルでの実行方法
### インストール
事前に以下をインストールしてください
- Python(3系)
- pipenv
- PyCharmやVSCodeなどのPythonを実行出来るIDE(任意)

### 実行
ローカルでの起動用のスクリプトファイルとして main.pyを用意しています。<br>
main.pyをIDE上で指定して実行するか 以下のコマンドで実行してください
````
python main.py
````

## 参考
- [PythonでWeb APIを叩く]
- [Python3でslackに投稿する]
- [2020 年の Python パッケージ管理ベストプラクティス]

<!-- links -->
[Slackのアラート部屋]: https://app.slack.com/client/T02GQ6JF5D2/C03K9QU8XK4
[Python3でslackに投稿する]: https://qiita.com/shtnkgm/items/4f0e4dcbb9eb52fdf316
[PythonでWeb APIを叩く]: https://qiita.com/hisshi00/items/9806eceeee2237624222
[2020 年の Python パッケージ管理ベストプラクティス]: https://qiita.com/sk217/items/43c994640f4843a18dbe
[Pipenvを使ったPython開発まとめ]: https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a
