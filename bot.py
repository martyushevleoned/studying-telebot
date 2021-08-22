import telebot
import config
from homework import Info

bot = telebot.TeleBot(config.TOKEN)
Info.download_schedule()
Info.download_hw()


@bot.message_handler(content_types=['text'])
def send_text(m):

    if m.chat.id == config.GROUP_ID:

        # Schedule

        if '/set_schedule\n' in m.text:
            Info.set_schedule(m.text.replace('/set_schedule\n', ''))
            bot.send_document(chat_id=m.chat.id, data=open('schedule.txt', 'r'))

        if m.text == '/get_schedule':
            bot.send_document(chat_id=m.chat.id, data=open('schedule.txt', 'r'))

        if m.text == '/download_schedule':
            Info.upload_hw()
            Info.download_schedule()
            Info.download_hw()
            bot.send_document(chat_id=m.chat.id, data=open('schedule.txt', 'r'))

        if m.text == '/upload_schedule':
            Info.upload_schedule()
            bot.send_document(chat_id=m.chat.id, data=open('schedule.txt', 'r'))

        # Homework

        if Info.set_hw(m.text) is True:
            Info.upload_hw()
            bot.send_document(chat_id=m.chat.id, data=open('hw.txt', 'r'))
            bot.send_message(m.chat.id, 'дз успешно изменено')

        if m.text == '/get_hw':
            bot.send_document(chat_id=m.chat.id, data=open('hw.txt', 'r'))

    else:
        bot.send_message(m.chat.id, 'меню', reply_markup=config.Keyboard.main_key, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def handler_call(call):
    for i in range(1, 8):
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
