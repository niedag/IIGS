from bs4 import BeautifulSoup
import requests

rand_url = "https://www.cancerresearchuk.org/about-cancer/lung-cancer/stages-types-grades/tnm-staging"
who_url = "https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue"
politico_url = "https://www.politico.com/news/2025/02/27/trump-private-forces-immigration-00206560"
nypost_url = "https://nypost.com/2025/02/27/us-news/teen-faces-civil-rights-complaint-after-refusing-to-play-against-trans-basketball-player/"
thehill_url = "https://thehill.com/homenews/administration/5168456-justice-department-releases-first-phase-of-epstein-files/" # Blocked
UNnews_url = "https://news.un.org/en/story/2024/11/1157451"
breitbart_url = "https://www.breitbart.com/europe/2025/02/26/ukraine-agrees-trumps-rare-earth-minerals-deal-zelensky-to-sign-friday/"
axios_url = "https://www.axios.com/2025/02/28/hpv-vaccine-cervical-cancer-prevention-cdc-report" # Blocked
hhsGOV_url = "https://womenshealth.gov/blog/female-athlete-triad-awareness-women-and-girls-sports" # Need to collect <li> and <p> also

test_url = "https://www.npr.org/2022/06/24/1102305878/supreme-court-abortion-roe-v-wade-decision-overturn"
page = requests.get(test_url)
soup_content = BeautifulSoup(page.content, "html.parser")
soup_text = BeautifulSoup(page.text, "html.parser")
print(soup_content)

#^ Grab header (Need different parsing strategy)
print(soup_content.find_all("h1"))

# ^Grab text
for para in soup_content.find_all("p"): 
    print(para.get_text()) 

# with open('output.txt', 'w', encoding='utf-8') as file:
#     file.write(soup_content)