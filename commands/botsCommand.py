import discord
from discord import Option
from discord.ext import commands
from typing import List
from utils.userFilters import filterByDate, filterByName


def register(bot: commands.Bot, GUILD_ID: int) -> None:
    @bot.slash_command(
        name="bots",
        description="Find potential bots based on account data",
        guild_ids=[GUILD_ID],
    )
    async def bots(
        ctx: discord.ApplicationContext,
        category: Option(
            str,
            "Choose a category",
            choices=["date", "name"],
        ),
    ):
        await ctx.defer()

        if ctx.guild is None:
            return

        all_members: List[discord.Member] = ctx.guild.members

        if category == "date":
            matches = filterByDate(all_members)

            if not matches:
                await ctx.respond(
                    "No users' account creation date match their join date!"
                )
            else:
                mentions = [m.mention for m in matches]
                await ctx.respond(" ".join(mentions))

        elif category == "name":
            matches = filterByName(all_members)

            if not matches:
                await ctx.respond("No users' username ends in a digit!")
            else:
                mentions = [m.mention for m in matches]
                await ctx.respond(" ".join(mentions))

        else:
            return
