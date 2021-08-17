import telebot
import config
from homework import Info

bot = telebot.TeleBot(config.TOKEN)
Info.upload_hw_from_file()


@bot.message_handler(content_types=['text'])
def send_text(m):

    if m.chat.id == config.GROUP_ID:

        if Info.set_homework(m.text) is True:
            Info.backup()
            with open('backup.txt', 'r') as f:
                bot.send_document(chat_id=m.chat.id, data=f)

            bot.send_message(m.chat.id, 'дз успешно изменено')

    else:
        bot.send_message(m.chat.id, 'меню', reply_markup=config.Keyboard.main_key)


@bot.callback_query_handler(func=lambda call: True)
def handler_call(call):
    for i in range(7):
        if call.data == str(i):
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=Info.get_homework(i, True),
                reply_markup=config.Keyboard.back_key,
                parse_mode='html')

    if call.data == 'day_key':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='выберите день',
            reply_markup=config.Keyboard.day_key,
            parse_mode='html')

    if call.data == 'get_schedule':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=Info.get_schedule(),
            reply_markup=config.Keyboard.back_key,
            parse_mode='html')

    if call.data == 'back':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='меню',
            reply_markup=config.Keyboard.main_key,
            parse_mode='html')


bot.polling(none_stop=True)
