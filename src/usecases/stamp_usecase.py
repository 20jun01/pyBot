from ..apis.traq import *


async def message_stamp_updated_response(body: dict):
    print(body)
    if body["messageId"] == "cead5be4-6dc2-465c-90d3-5a985b6e4689":
        print("あけおめ!!")
        if not len(body["stamps"]) == 1:
            pass
        elif body["stamps"][0]["stampId"] == "dbcc7871-efef-4d6d-a2c6-b0f187f7b936" and body["stamps"][0]["count"] == 1:
            print("あけおめ!!")
            stamp_user = get_user_info(body["stamps"][0]["userId"])
            post_to_traq("あけおめ!! @" + stamp_user["name"] + " https://q.trap.jp/files/bf2104f2-b528-41c0-a7e2-0ca898991227", "0b725923-2e45-4816-b1f5-8eac5dc74fec")
            res = await add_tag_to("b8c43ab5-21c8-4dee-ba7c-d515584039da", "あけおめ!! " + stamp_user["name"] + " 2024")
            print(res)
            lock_tag_to("b8c43ab5-21c8-4dee-ba7c-d515584039da", res["tagId"])

    # print(get_traq_message("cead5be4-6dc2-465c-90d3-5a985b6e4689"))
    # put_traq_message("cead5be4-6dc2-465c-90d3-5a985b6e4689", "[](:omedetou:を押してね)あけおめ!!")
    return
