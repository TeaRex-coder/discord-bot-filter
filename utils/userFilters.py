import discord
from typing import List


def filterByDate(members: List[discord.Member]) -> List[discord.Member]:
    results: List[discord.Member] = []
    for member in members:
        if member.joined_at is None or member.created_at is None:
            continue

        if member.created_at.date() == member.joined_at.date():
            results.append(member)

    return results


def filterByName(members: List[discord.Member]) -> List[discord.Member]:
    results: List[discord.Member] = []
    for member in members:
        if member.name and member.name[-1].isdigit():
            results.append(member)

    return results
