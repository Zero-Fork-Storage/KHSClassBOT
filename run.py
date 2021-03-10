from app import KHSClassBOT

cogs_list = ["cogs.info", "cogs.SAT", "cogs.school"]

client = KHSClassBOT()

if __name__ == '__main__':
    client.load_extensions(cogs_list)
    client.run()
