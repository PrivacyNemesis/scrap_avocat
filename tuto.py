from bs4 import BeautifulSoup
import requests
import re

# requete = requests.get("https://www.barreaudenice.com/annuaire/avocats/?fwp_paged=1")
# print(requete.status_code)

def requetes():

    page = 1
    
    for i in range(107):
        i = f"https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={page}"
        page += 1

        
def main():
    
    annuaire = []
        
    url = requetes()
    
    for page in url:
    
        requete = requests.get(url)
        soup = BeautifulSoup(requete.content, "html.parser")
    
        avocats = soup.find_all('div', class_='callout secondary annuaire-single')
        # print(len(avocats))
    
        for avocat in avocats:
            nom = avocat.find('h3').text.strip()
            serment = avocat.find('span', class_='date').text.strip()
            adresse = avocat.find('span', class_='adresse').text.strip()
            # nettoyage de l'adresse avec un regex
            adresse_regex = re.sub(r"\s+", " ", adresse)
            telephone = avocat.find('span', class_='telephone').text.strip()
            email = avocat.find('span', class_='email').a.text.strip()
        
        
        
        
    
    
    
main()