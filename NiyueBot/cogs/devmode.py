import disnake
from disnake.ext import commands
from disnake.ui import Modal, TextInput


DEV_PASSWORD = "mySecretDevPass"

class DevModeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Включить режим разработчика (по паролю)")
    async def dev(self, inter: disnake.ApplicationCommandInteraction):
        
        password_input = TextInput(
            label="Пароль", 
            placeholder="Введите пароль",
            style=disnake.TextInputStyle.short,
            required=True,
            custom_id="password_input"  
        )
        
       
        modal = Modal(
            title="Введите пароль",
            custom_id="dev_password_modal"
        )
        modal.add_item(password_input)

        
        await inter.response.send_message("Введите пароль для активации режима разработки:", ephemeral=True)
        await inter.send_modal(modal)

    @commands.Cog.listener()
    async def on_modal_submit(self, inter: disnake.ModalInteraction):
        
        password = inter.text_values.get("password_input")  

        if password == DEV_PASSWORD:
            embed = disnake.Embed(
                title="🛠 Режим разработки активирован",
                description=f"{inter.author.mention} успешно включил режим разработчика.",
                color=disnake.Color.red()
            )
            await inter.response.send_message(embed=embed)
        else:
            await inter.response.send_message("❌ Неверный пароль.", ephemeral=True)

def setup(bot):
    bot.add_cog(DevModeCog(bot))
    print(f"Extension {__name__} is ready")