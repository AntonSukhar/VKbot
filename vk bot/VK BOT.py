import datetime

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


class VKBot:
    def __init__(self, bot_name, api_token):
        self.session = vk_api.VkApi(token=api_token)
        self.longpoll = VkLongPoll(self.session)
        self.vk = self.session.get_api()
        self.bot_name = bot_name


    def send_message(self, id , message ):
        self.vk.messages.send(user_id = id, message = message , random_id = datetime.datetime.now().microsecond)

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if str(event.text).split(" ")[0] == self.bot_name:
                    self.send_message(message="Это я!" , id=event.user_id)


bot = VKBot("Анонимные_Программисты" , "vk1.a.ab0U3Jq4JOrcDF5opRjLJslatzUCvm9xnvsj7UbawgAbOBMbWbgyycorcXcfrcYLGAZpgjFD8vI6Ipg7nkxzdlvs6U322110bpjHiQTM0N-cP2fTeZCYO0dkePeX6OQQYMLV11dKcGhonKepsThmoBMW7eFbg8av4pjEjf2dETT1cW6IBJqXBbqH8cELRZT1SxPe5q4YZj3kS58M-R5fSQ")
bot.start()