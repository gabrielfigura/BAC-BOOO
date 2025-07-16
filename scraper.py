import requests
from bs4 import BeautifulSoup

def get_latest_results():
    try:
        url = "https://casinoscores.com/es/bac-bo/"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        results = []
        # Supondo que os resultados estão em spans com class "result"
        for span in soup.select("div.gameResults span"):
            text = span.get_text(strip=True).upper()
            if text in ["PLAYER", "BANKER", "TIE"]:
                if text == "PLAYER":
                    results.append("P")
                elif text == "BANKER":
                    results.append("B")
                elif text == "TIE":
                    results.append("T")
        
        return results[:20]  # Pega os 20 últimos

    except Exception as e:
        return []
