from ..apis.traq import *


async def message_stamp_updated_response(body: dict):
    print(body)
    if body["messageId"] == "cead5be4-6dc2-465c-90d3-5a985b6e4689":
        print("あけおめ!!")
        if not len(body["stamps"]) == 1:
            pass
        elif body["stamps"][0]["stampId"] == "dbcc7871-efef-4d6d-a2c6-b0f187f7b936" and body["stamps"][0]["count"] == 1:
            print("あけおめ!!")

    # print(get_traq_message("cead5be4-6dc2-465c-90d3-5a985b6e4689"))
    put_traq_message("cead5be4-6dc2-465c-90d3-5a985b6e4689", "[](:omedetou:を押してね)あけおめ!!")
    res = await add_tag_to_me("あけおめ!!")
    print(res)
    return
