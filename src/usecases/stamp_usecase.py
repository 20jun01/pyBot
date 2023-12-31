from ..apis.traq import *


async def message_stamp_updated_response(body: dict):
    print(body)
    # print(get_traq_message("cead5be4-6dc2-465c-90d3-5a985b6e4689"))
    put_traq_message("cead5be4-6dc2-465c-90d3-5a985b6e4689", "あけおめ!!")
    res = add_tag_to_me("あけおめ!!")
    lock_tag(res["tagId"])
    return
