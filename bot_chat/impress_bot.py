import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'bot_chat.settings'
django.setup()


from telegram.ext import *
import re
from user.models import *
from datetime import datetime
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,ReplyMarkup,CallbackQuery,ChatAction

API_KEY = '1942198458:AAGuzZFjj61BLOvt3YVqrg1MD_oHN9HNInU'

def handle_message(update , context):
    try:
        # showing typing
        context.bot.send_chat_action(chat_id=get_chat_id(update, context), action=ChatAction.TYPING, timeout=1)
        if not update.callback_query:
            # Sending Options
            context.bot.send_message(chat_id=get_chat_id(update , context), text='What would you like to receive?', reply_markup=reply_markup)

        # setting name of user from username if username exist else full_name
        if update['message']['chat']['username']:
            str_name = update['message']['chat']['username']
        else:
            str_name = update['message']['chat']['full_name']

        if update.callback_query:
            # Option selected
            choice = update.callback_query.data
            if choice == '1':
                # Choice 1: Stupid
                str_button = 'Stupid'
                update.callback_query.message.edit_text('You have chosen Stupid')
                update.message.reply_text(f"Artificial intelligence is no match for natural stupidity.")
            elif choice == '2':
                # Choice 2: fat
                str_button = 'Fat'
                update.callback_query.message.edit_text('You have chosen Fat')
                update.message.reply_text(f"Every time someone calls me fat I get so depress I cut myself... a piece of cake..")
            elif choice == '3':
                # Choice 3: Dump
                str_button = 'Dump'
                update.callback_query.message.edit_text('You have chosen Dump')
                update.message.reply_text(f"Light travels faster than sound. This is why some people appear bright until they open their mouths.")

             # update count if already exist else add button
            ins_data = ButtonCall.objects.filter(vchr_button_name__iexact = str_button).values('pk_bint_id','int_count').first()
            if ins_data:
                ButtonCall.objects.filter(pk_bint_id = ins_data['pk_bint_id']).update(int_count = ins_data['int_count'] + 1)
            else:
                ButtonCall.objects.create(vchr_button_name = str_button,dat_created = datetime.now(),int_count = 1)

            # update count user wise if already exist else add user
            ins_user = UserDetails.objects.filter(vchr_user_name__iexact = str_name).values('user_ptr_id','int_count')
            if ins_user:
                UserDetails.objects.filter(user_ptr_id = ins_data['user_ptr_id']).update(int_count = ins_data['int_count'] + 1)
            else:
                UserDetails.objects.create(vchr_user_name = str_name,dat_joined = datetime.now(),int_count = 1)

    except Exception as e:
        print(e)

    return False

def get_chat_id(update, context):
    chat_id = -1
    if update['message'] is not None:
        # text message
        chat_id = update['message']['chat']['id']
    elif update['callback_query'] is not None:
        # callback message
        chat_id = update['callback_query']['message']['chat']['id']
    elif update['poll'] is not None:
        # answer in Poll
        chat_id = context.bot_data[update['poll']['id']]

    return chat_id

if __name__ == '__main__':
    updater = Updater(API_KEY , use_context=True)
    options = []
    options.append(InlineKeyboardButton(text='Stupid', callback_data='1'))
    options.append(InlineKeyboardButton(text='Fat', callback_data='2'))
    options.append(InlineKeyboardButton(text='Dump', callback_data='3'))
    reply_markup = InlineKeyboardMarkup([options])
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text , handle_message))

    updater.start_polling(1.0)
    updater.idle()
