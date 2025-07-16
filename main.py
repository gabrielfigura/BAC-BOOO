import asyncio
import logging
from scraper import get_latest_results
from strategy import analyze_patterns, format_signal
from telegram import Bot
import traceback

# Configurações
TOKEN = "8163319902:AAHE9LZ984JCIc-Lezl4WXR2FsGHPEFTxRQ"
CHAT_ID = "-1002597090660"
INTERVALO = 30  # segundos

bot = Bot(token=TOKEN)

# Configuração de log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("BacBoBot")

# Histórico dos últimos resultados
ultimos_resultados = []

async def enviar_erro_para_telegram(erro):
    msg = f"⚠️ <b>ERRO NO BOT:</b>\n<code>{erro}</code>"
    await bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="HTML")

async def monitorar():
    global ultimos_resultados
    await bot.send_message(chat_id=CHAT_ID, text="🤖 Bot Bac Bo iniciado com sucesso!")

    while True:
        try:
            resultados = get_latest_results()

            if not resultados:
                logger.warning("Nenhum resultado capturado.")
                await asyncio.sleep(INTERVALO)
                continue

            # Se for a primeira vez, apenas armazena
            if ultimos_resultados != resultados:
                novo_resultado = resultados[0]
                if novo_resultado not in ultimos_resultados:
                    ultimos_resultados = resultados
                    logger.info(f"Novo resultado: {novo_resultado}")
                    
                    # Aplica as estratégias
                    sinal, estrategia = analyze_patterns(resultados)

                    if sinal:
                        mensagem = format_signal(sinal, estrategia)
                        await bot.send_message(chat_id=CHAT_ID, text=mensagem, parse_mode="HTML")

            await asyncio.sleep(INTERVALO)

        except Exception as e:
            erro = traceback.format_exc()
            logger.error(erro)
            await enviar_erro_para_telegram(erro)
            await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(monitorar())
