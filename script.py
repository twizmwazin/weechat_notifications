import weechat
import time
import telegram

bot = telegram.Bot(token='ADD YOUR TOKEN HERE')

weechat.register("jackPing", "FlashCode", "1.0", "GPL3", "OH NO", "", "")
weechat.prnt("", "Use without jack2 permition is not allowed")
def i_am_author_of_message(buffer, nick):
    """Am I (the current WeeChat user) the author of the message?"""
    return weechat.buffer_get_string(buffer, 'localvar_nick') == nick
def nick_that_sent_message(tags, prefix):
    for tag in tags:
        if tag.startswith('nick_'):
            return tag[5:]

    if prefix.startswith(('~', '&', '@', '%', '+', '-', ' ')):
        return prefix[1:]

    return prefix

#process messages
def message(data, bufferp, tm, tags, display, is_hilight, prefix, msg):
    nick = nick_that_sent_message(tags.split(','), prefix)
    if (is_hilight or weechat.buffer_get_string(bufferp, 'localvar_type') == 'private') and not(i_am_author_of_message(bufferp, nick)):
        mes = '<' + nick_that_sent_message(tags.split(','), prefix) + '>: '  +msg
        if weechat.buffer_get_string(bufferp, 'localvar_type') != 'private':
            mes =  weechat.buffer_get_string(bufferp, 'short_name') + ': ' + mes
        bot.send_message(chat_id=SET CHAT ID, text=mes)
    return weechat.WEECHAT_RC_OK

# catch all messages
weechat.hook_print("", "", "", 1, "message", "")

