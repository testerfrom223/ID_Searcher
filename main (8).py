import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await bot.change_presence(activity=discord.Game(name="easy to pg"))

@bot.command(name="generate", help="Generate IDs")
async def generate_ids(ctx: commands.Context):
    # Extract the content from the message
    content = ctx.message.content
    # Extract the number of IDs from the content (you may need to adjust this based on your use case)
    num_ids = int(content.split()[-1])

    custom_id_length = 7
    generated_ids = generate_custom_length_ids(num_ids, custom_id_length)

    file_path = f"generated_ids_length_{custom_id_length}.txt"
    with open(file_path, "w") as file:
        file.write("\n".join(map(str, generated_ids)))

    # Include the first 10 generated IDs in the response
    for i in range(min(10, num_ids)):
        response = f"{generated_ids[i]}\n"

    # Send the response message
    await ctx.send(response)

    # Send the text file containing all generated IDs
    with open(file_path, "rb") as file:
        await ctx.send(file=discord.File(file, filename=file_path))

def generate_custom_length_ids(num_ids, id_length):
    min_value = 10 ** (id_length - 1)
    max_value = (10 ** id_length) - 1
    custom_length_ids = [random.randint(min_value, max_value) for _ in range(num_ids)]
    return custom_length_ids

bot.run("")