from logging import getLogger

import slackweb

log = getLogger(__name__)

"""
Slack通知のメイン処理の実行用スクリプト
"""


def execute():
    """
    Slack通知を行う一連処理を実行します
    """

    total = fetch_request_quiz_total()
    log.info("リクエスト中のクイズ件数: %s", total)

    if total > 0:
        slack_notify(total)
    else:
        log.info('リクエスト中のクイズは存在しません')


def fetch_request_quiz_total():
    """
    MicroCMSから request状態のクイズの件数を取得して返します
    :return: MicroCms側でrequestとなっているクイズの件数
    """

    # TODO microCMSへのget処理を追加する　現時点では固定で10を返却
    return 10


def slack_notify(total):
    """
    Slackへ通知を行います
    :param total: リクエスト中のクイズの件数
    """

    # TODO MicroMicroCMSの管理用ページのURLが決まり次第URLを修正する
    _micro_cms_url = 'dummy'

    _slack_url = 'https://hooks.slack.com/services/T02GQ6JF5D2/B03K9Q92CG3/HFEYwSFaKEBN3EW3ieQRPBzc'
    slack_text = 'holo-quiz-notice-batch 処理終了\n' \
                 '\n' \
                 'リクエスト中のクイズが存在します\n' \
                 'リクエスト中のクイズ件数: {}件\n' \
                 '\n' \
                 '管理UIを確認してください\n' \
                 '{}'.format(total, _micro_cms_url)

    slack = slackweb.Slack(url=_slack_url)
    slack.notify(text=slack_text)
