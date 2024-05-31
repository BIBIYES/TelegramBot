from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# 你的机器人 token
TOKEN = '6884757883:AAEmYYE0bPXpYU6qEYU-iCHJRxwSnBUHggU'

# 群聊 ID
BACKUP_CHAT_ID = -1002117896734  # 备份群 ID
MIRROR_CHAT_ID = -1002177779011    # 镜像群 ID

# 定义一个处理所有消息的处理函数
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    user = update.message.from_user.username
    text = update.message.text
    print(f"Message in chat {chat_id} from {user}: {text}")

    # 如果消息来自备份群，则将其转发到镜像群
    if chat_id == BACKUP_CHAT_ID:
        await context.bot.forward_message(chat_id=MIRROR_CHAT_ID, from_chat_id=chat_id, message_id=update.message.message_id)

def main():
    # 创建 Application 并添加消息处理程序
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL, handle_message))

    # 启动机器人
    application.run_polling()

if __name__ == '__main__':
    main()
