from pyrogram import Client, filters
from pyrogram.enums import ParseMode

API_ID   = 35773150
API_HASH = "1ae417974a581a8e409f7600097db8b2"

PAEM = """
**╔════════════════════════════╗**
**║         🤖  ZADXPRO БОТ         ║**
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

app = Client("zadxpro", api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.private & filters.incoming)
async def auto_javob(client, message):
    nom = message.from_user.first_name
    await message.reply_text(
        PAEM.format(nom=nom),
        parse_mode=ParseMode.MARKDOWN
    )

print("✅  Бот оғоз шуд...")
app.run()