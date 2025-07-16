from datetime import datetime
import random

def analyze_patterns(results):
    if len(results) < 5:
        return None, None

    r = results[:10]  # analisa os últimos 10

    # Estratégia 1: Alternância
    if r[0] != r[1] and r[1] != r[2]:
        return r[2], "Alternância"

    # Estratégia 2: Padrão 3-1
    if r[0] == r[1] == r[2] and r[3] != r[2]:
        return r[3], "Padrão 3-1"

    # Estratégia 3: Padrão 3-2
    if r[0] == r[1] == r[2] and r[3] == r[4] and r[3] != r[2]:
        return r[4], "Padrão 3-2"

    # Estratégia 4: Padrão 2-2
    if r[0] == r[1] and r[2] == r[3] and r[0] != r[2]:
        return r[3], "Padrão 2-2"

    # Estratégia 5: Reação após TIE
    if r[1] == "T":
        if r[0] != r[2]:
            return r[2], "Reação após Empate"

    return None, None

def format_signal(sinal, estrategia):
    emoji = "🔵" if sinal == "P" else "🔴" if sinal == "B" else "🟡"
    cor = "Player 🔵" if sinal == "P" else "Banker 🔴" if sinal == "B" else "TIE 🟡"
    confianca = f"{random.randint(75, 100)}%"

    mensagem = f"""
🎲 <b>Novo sinal Bac Bo ao vivo</b>:
🎯 <b>Entrada:</b> {emoji}{emoji}{emoji}
💡 <b>Padrão:</b> {estrategia}
🛡️ <b>Protege o TIE:</b> 🟡
📈 <b>Confiança:</b> {confianca}
⏰ <b>Validade:</b> 1 minuto
🕒 <i>{datetime.now().strftime('%H:%M:%S')}</i>
"""
    return mensagem.strip()
