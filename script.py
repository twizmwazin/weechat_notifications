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
    """Returns a nick that sent the message based on the given data passed to
    the callback.
    """
    # 'tags' is a comma-separated list of tags that WeeChat passed to the
    # callback. It should contain a tag of the following form: nick_XYZ, where
    # XYZ is the nick that sent the message.
    for tag in tags:
        if tag.startswith('nick_'):
            return tag[5:]

    # There is no nick in the tags, so check the prefix as a fallback.
    # 'prefix' (str) is the prefix of the printed line with the message.
    # Usually (but not always), it is a nick with an optional mode (e.g. on
    # IRC, @ denotes an operator and + denotes a user with voice). We have to
    # remove the mode (if any) before returning the nick.
    # Strip also a space as some protocols (e.g. Matrix) may start prefixes
    # with a space. It probably means that the nick has no mode set.
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

weechat.hook_print("", "", "", 1, "message", "") # catch all messages

