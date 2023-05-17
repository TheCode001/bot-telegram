import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Создаем бота с помощью токена
bot = telegram.Bot(token=6070519491:AAGjPu_Yx_1QkG8hdn1K2rtN53ZLZYOVWcg')
# Создаем объект Updater для получения обновлений
updater = Updater(token='YOUR_TOKEN', use_context=True)
# Получаем диспетчер из updater
dispatcher = updater.dispatcher

# Создаем список запрещенных слов
bad_words = ["sən","sen","sənin","senin","sikim","göt","got","petux","qəhbə","gijdılaq","gicdılaq","götvərən","gotvərən","gotveren"]

# Создаем функцию-обработчик сообщений
def message_handler(update, context):
    # Получаем текст сообщения
    message_text = update.message.text
    # Проверяем, есть ли в тексте запрещенные слова
    if any(word in message_text for word in bad_words):
        # Если есть, то блокируем пользователя в чате
        bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user.id)
        # И отправляем сообщение в общий чат
        bot.send_message(chat_id=update.message.chat_id, text="Gəlin sülh və dostluq içində yaşayaq.")

# Добавляем обработчик сообщений к диспетчеру с фильтром для групповых чатов
dispatcher.add_handler(MessageHandler(Filters.chat_type.groups, message_handler))

# Запускаем бота
updater.start_polling()
updater.idle()
