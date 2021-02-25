from app import MainSystem

cogs_list = ["cogs.info", "cogs.SAT", "cogs.school"]

if __name__ == '__main__':
    client = MainSystem()
    client.inject_obj()

    client.discord_client.load_extensions(cogs_list)
    client.run()

