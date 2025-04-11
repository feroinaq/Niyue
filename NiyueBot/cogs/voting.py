import disnake
from disnake.ext import commands
from disnake.ui import View, Button
from collections import defaultdict

class VoteView(View):
    def __init__(self, author_id, options, message_id, topic, description):
        super().__init__(timeout=None)
        self.votes = defaultdict(set)  # option -> set of user_ids
        self.author_id = author_id
        self.message_id = message_id
        self.topic = topic
        self.description = description

        for label in options:
            self.add_item(VoteButton(label, self))

    def get_results_embed(self):
        embed = disnake.Embed(
            title=f"📊 Голосование: {self.topic}",
            description=self.description,
            color=disnake.Color.blue()
        )

        if any(self.votes.values()):
            for option, users in self.votes.items():
                user_mentions = "\n".join(f"> {f'<@{u}>'}" for u in users) or "—"
                embed.add_field(
                    name=f"{option} — {len(users)} голос(ов)",
                    value=user_mentions,
                    inline=False
                )
        else:
            embed.add_field(name="Никто ещё не проголосовал", value="👀", inline=False)

        return embed


class VoteButton(Button):
    def __init__(self, label, view):
        super().__init__(label=label, style=disnake.ButtonStyle.primary)
        self.vote_view = view

    async def callback(self, interaction: disnake.MessageInteraction):
        user_id = interaction.user.id

        # Удалить старый голос
        for voters in self.vote_view.votes.values():
            voters.discard(user_id)

        # Добавить новый голос
        self.vote_view.votes[self.label].add(user_id)

        embed = self.vote_view.get_results_embed()
        embed.set_footer(text=f"Автор: {interaction.message.interaction.user.display_name}",
                         icon_url=interaction.message.interaction.user.display_avatar.url)

        await interaction.response.edit_message(embed=embed, view=self.vote_view)


class VotingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_votes = {}

    @commands.slash_command(description="Создать голосование")
    async def gavo(
        self,
        inter: disnake.ApplicationCommandInteraction,
        тема: str,
        описание: str,
        вариант1: str,
        вариант2: str,
        вариант3: str = None,
        вариант4: str = None,
        вариант5: str = None
    ):
        await inter.response.defer()

        options = [вариант1, вариант2]
        if вариант3: options.append(вариант3)
        if вариант4: options.append(вариант4)
        if вариант5: options.append(вариант5)

        # Изначальный embed (без голосов)
        view = VoteView(author_id=inter.author.id, options=options, message_id=None, topic=тема, description=описание)
        embed = view.get_results_embed()
        embed.set_footer(text=f"Автор: {inter.author.display_name}", icon_url=inter.author.display_avatar.url)

        msg = await inter.followup.send(embed=embed, view=view)
        view.message_id = msg.id

        self.active_votes[msg.id] = view


def setup(bot):
    bot.add_cog(VotingCog(bot))
    print(f"Extension {__name__} is ready")