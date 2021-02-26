from app import KHSClassBOT

cogs_list = ["cogs.info", "cogs.SAT", "cogs.school"]

if __name__ == '__main__':
    client = KHSClassBOT()
    client.load_extensions(cogs_list)
    client.run()
