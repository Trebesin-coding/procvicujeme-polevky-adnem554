from bs4 import BeautifulSoup
import requests
import json


def main():
    url = "https://www.kurzy.cz/kalendar/svatky/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    datum = soup.find(string=lambda text: "Dnes je" in text)

    if not datum:
        print("Nenasel jsem dnesni datum!")
    else:
        dnesni_datum = datum.strip()
     print(dnesni_datum)


    svatek = soup.find(string=lambda text: "Dnes má svátek" in text)

    if not svatek:
        print("Nenasel jsem kdo ma dneska svatek!")
    else:
        jmena = [a.text for a in svatek.parent.find_all("a")]

     print(jmena)
    print("Dnes ma svatek:", jmena)
    print("Dnesni datum:", dnesni_datum)
    data = {
        "dnesni_datum": dnesni_datum,
        "dnesni_svatek": jmena
    }
    with open("dnesni_svatek.json", "w", encoding="utf-8") as soubor:
        json.dump(data, soubor, ensure_ascii=False)

if __name__ == "__main__":
    main()