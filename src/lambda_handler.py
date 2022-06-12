import slack_notify

"""
AWS Lambdaのハンドラー
"""


def lambda_handler(event, context):
    """
    AWS Lambdaの event handler
    TODO AWS Lambda周りの設定追加

    :param event: lambda event
    :param context: context
    """
    print('called lambda')

    slack_notify.execute()
