from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
GROUP_USERNAME=env.str("GROUP_USERNAME")
GROUP_USERNAME2=env.str("GROUP_USERNAME2")
GROUP_USERNAME3=env.str("GROUP_USERNAME3")
GROUP_USERNAME4=env.str("GROUP_USERNAME4")

