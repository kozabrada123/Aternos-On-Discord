from discord import Embed
import Functions

def server_info_embed():

    text = f"**Status:** {Functions.get_status()} \n" \
           f"**Number of players:** {len(Functions.get_players())} \n" \
           f"**Players:** {str(Functions.get_players()).replace('[', '').replace(']', '')} \n" \

    embed = Embed()
    embed.add_field(name="Server Info", value=text, inline=False)
    return embed


def help_embed():
    """ Generates embed object for help command"""
    embed = Embed(title="Help")
    embed.add_field(name="--launch",
                    value="Launches the server",
                    inline=False)
    embed.add_field(name="--status",
                    value="Lists some helpful server info")
    embed.add_field(name="--help",
                    value="Displays this message",
                    inline=False)
    return embed
