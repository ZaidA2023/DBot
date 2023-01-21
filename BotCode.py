
import discord
import random
import wikipedia

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        print(message)
        result = wikipedia.search(message.content)
        end=[]
        for index, value in enumerate(result, 0):
            end.append("{}. {}".format(index, value))

        await message.channel.send('{header}{lst}'.format(header="Choose one (Number):"+"\n", lst=end))
        rponse =  await client.wait_for('message')
        print(rponse.content)
        print(message.content)
        print(result[int(rponse.content)])
        try:
            ans = wikipedia.summary(result[int(rponse.content)], sentences = 5)
            await message.channel.send(ans)
        except wikipedia.DisambiguationError as e:
            await message.channel.send(wikipedia.summary(random.choice(e.options)))

client.run(<Bot_Token>)
