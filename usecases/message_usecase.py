from fastapi import Response
from ..apis.traq import *
from .. import domains, api_adapters


# TODO: responseを返すのはここの責務ではないので型を変える
async def message_created_response(body: dict) -> Response:
    if body["message"]["user"]["bot"]:
        print("message from bot")
        return Response(status_code=204)

    message_sent = body["message"]["plainText"]
    channel_id = body["message"]["channelId"]
    user = body["message"]["user"]["name"]
    display_name = body["message"]["user"]["displayName"]

    is_personal, prefix, message_truthy = domains.get_message_prefixes(
        message_sent)
    message_content = ""
    print(is_personal, prefix, message_truthy)

    if domains.is_join_prefix(prefix):
        join_channel(channel_id)

    elif domains.is_leave_prefix(prefix):
        leave_channel(channel_id)

    # .replaceはgenerate側の責務な気もするけど、@を返したくないのはtraqへの投稿の責務なのでここでやる
    elif domains.is_talk_prefix(prefix):
        message_content = api_adapters.generate_talk(
            message_truthy, is_personal, False, user).replace("@", "`@`")

    elif domains.is_talk_cont_prefix(prefix):
        message_content = api_adapters.generate_talk(
            message_truthy, is_personal, True, user).replace("@", "`@`")

    elif domains.is_add_setting_prefix(prefix):
        api_adapters.add_system_settings(message_truthy, is_personal, user)

    elif domains.is_new_setting_prefix(prefix):
        api_adapters.new_system_settings(message_truthy, is_personal, user)

    elif domains.is_del_setting_prefix(prefix):
        api_adapters.new_system_settings("", is_personal, user)

    elif domains.is_show_setting_prefix(prefix):
        message_content = "`" + api_adapters.get_system_settings(is_personal, user) + "`"

    elif domains.is_image_generate_prefix(prefix):
        image_url = await api_adapters.generate_image(message_truthy)
        image_path = domains.save_image_from_url_without_name(image_url)
        # TODO: trapのAPIURLなので適したところから取得する
        message_content = cast_file_id_to_message(
            post_file(image_path, channel_id))

    elif domains.is_image_edit_prefix(prefix):
        image_url, is_succeed = api_adapters.edit_image(
            message_truthy, channel_id)
        if is_succeed:
            image_path = domains.save_image_from_url_without_name(image_url)
            message_content = cast_file_id_to_message(
                post_file(image_path, channel_id))
        else:
            prefix = ""
            message_content = image_url

    # TODO: prefixを受け取った後の処理をする関数は別に作る(つまり、ここではget_message_textはしない)
    message = create_response_message(prefix, message_content)
    post_to_traq(message, channel_id)
    return Response(status_code=204)


def create_response_message(message_type: str, message_content: str) -> str:
    return domains.get_message_text(message_type) + message_content


__all__ = ["message_created_response"]
