from pyrogram import Client, filters
from pyrogram.enums import ParseMode
import asyncio
import aiohttp
from aiohttp import web
import os

API_ID   = 35773150
API_HASH = "1ae417974a581a8e409f7600097db8b2"

PAEM = """
**╔════════════════════════════╗**
**║        🤖  ZADXPRO БОТ    ║**
**╚════════════════════════════╝**

**🌙  Салом алейкум, {nom}!**

**😔  Ҳозир  z a d x p r o  всети нест.**

**🤖  Ман боти  z a d x p r o  ҳастам**
**ва ба Шумо гап задастам.**

**⏳  Агар ягон чиз даркор бошад**
**лутфан сабр кунед —**
**ба Шумо ҷавоб хоҳад дод!**

**━━━━━━━━━━━━━━━━━━━━━━━━━━━━**
**🙏  Ташаккур!**
**━━━━━━━━━━━━━━━━━━━━━━━━━━━━**
"""

async def fake_server():
    async def handler(request):
        return web.Response(text="Bot is running!")
    server = web.Application()
    server.router.add_get("/", handler)
    runner = web.AppRunner(server)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"✅  Порт {port} оғоз шуд!")

async def keep_alive():
    url = os.environ.get("RENDER_EXTERNAL_URL")
    if not url:
        return
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    print(f"✅  Бедор! Статус: {resp.status}")
        except Exception as e:
            print(f"⚠️  Хато: {e}")
        await asyncio.sleep(30)

async def main():
    loop = asyncio.get_event_loop()
    
    app = Client(
        "zadxpro",
        api_id=API_ID,
        api_hash=API_HASH,
        no_updates=False
    )

    @app.on_message(filters.private & filters.incoming)
    async def auto_javob(client, message):
        nom = message.from_user.first_name
        await message.reply_text(
            PAEM.format(nom=nom),
            parse_mode=ParseMode.MARKDOWN
        )

    await fake_server()
    await app.start()
    print("✅  Бот оғоз шуд...")
    asyncio.create_task(keep_alive())
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
