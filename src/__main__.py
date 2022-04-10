import telegram
import typer
from enum import Enum
from nome_canal import NomeCanal
import contextvars
from enum_emoji import EnumEmoji

NOME_ARQUIVO_TOKEN = "telegram.token"
token = contextvars.ContextVar("token", default=None)
app = typer.Typer()


@app.command()
def token(token_value: str):
    with open(NOME_ARQUIVO_TOKEN, "w") as arquivo_token:
        arquivo_token.write(token_value)
        arquivo_token.close()


@app.command()
def enviar(mensagem: str, canal: NomeCanal = NomeCanal.sysadmin,
           emoji: EnumEmoji = EnumEmoji.info):

    if token.get() is None:
        print("Token não definido.")
    else:
        bot = telegram.Bot(token=token)
        bot.send_message(text=f'{get_emoji_utf(emoji)} {mensagem}', chat_id=get_channel_id(canal))


def get_channel_id(canal: NomeCanal) -> int:
    match canal:
        case NomeCanal.ti:
            return -1001559821987
        case NomeCanal.sysadmin:
            return -1001764196310
    return 0


def get_emoji_utf(emoji: EnumEmoji) -> str:
    match emoji:
        case EnumEmoji.falha:
            return "\U000026d4"
        case EnumEmoji.sucesso:
            return "\U0001F3C6"
        case EnumEmoji.alerta:
            return "\U000026a0"
        case EnumEmoji.info:
            return "\U00002139"
        case EnumEmoji.bateria:
            return "\U0001F50B"
        case EnumEmoji.energia:
            return "\U000026A1"
        case EnumEmoji.feito:
            return "\U00002705"
        case EnumEmoji.cancelado:
            return "\U0000274c"
        case EnumEmoji.on:
            return "\U0001F7E2"
        case EnumEmoji.off:
            return "\U0001F534"
    return None


def get_token():
    try:
        with open(NOME_ARQUIVO_TOKEN, "r") as arquivo_token:
            t = arquivo_token.readline()
            token.set(t)
            arquivo_token.close()
    except FileNotFoundError:
        print("Arquivo de token ausente.")


if __name__ == "__main__":
    print(token.get())
    get_token()
    app()
