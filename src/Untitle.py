{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8dbab14f-919a-4740-b522-b355c2753a93",
   "metadata": {},
   "outputs": [],
   "source": [
    "import telebot\n",
    "import os\n",
    "from loguru import logger"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db642513-fa21-499f-98f2-512da6fb3a63",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "743ca730-3b86-4e62-99c9-91ffe6b6e1c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Bot:\n",
    "    def __init__(self):\n",
    "        self.bot = telebot.TeleBot(os.environ['NASHENAS_BOT_TOKEN'])\n",
    "        self.echo_all = self.bot.message_handler( func=lambda message: True)(self.echo_all) \n",
    "\n",
    "    def run(self):\n",
    "        logger.info('Bot is running...')\n",
    "        self.bot.infinity_polling()\n",
    "        \n",
    "    def echo_all(self, message):\n",
    "        self.bot.reply_to(message, message.txt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b33da109-a6b6-4ce8-adfa-11d1b81d7c0d",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__=='__main__':\n",
    "    logger.info('bot starts...')\n",
    "    bot = Bot()\n",
    "    bot.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
