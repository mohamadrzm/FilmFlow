from bs4 import BeautifulSoup
from requests import get
class Zarfim() :
    def __init__(self) -> None:
        pass
        
    def get_detail_from_name(self, search_term : str) -> dict:
        """
        Retrieves details of movies based on a search term.

        Args:
            search_term (str): The term to search for.

        Returns:
            dict: A dictionary containing the details of the movies found. The dictionary has the following structure:
                {
                    'status code': str,
                    'data': dict
                }

                - 'status code' (str): The status code indicating the success or failure of the operation. Possible values are '0' for success and '1' for failure.
                - 'data' (dict): A dictionary containing the details of the movies found. The keys of the dictionary are integers starting from 1 and the values are dictionaries with the following structure:
                    {
                        'title': str,
                        'src': str,
                        'img': str
                    }

                    - 'title' (str): The title of the movie.
                    - 'src' (str): The URL of the movie's page.
                    - 'img' (str): The URL of the movie's thumbnail image.

        Raises:
            None

        Notes:
            - The function makes HTTP requests to the 'https://zarfilm.com/' website to retrieve the movie details.
            - The function stops searching for movies when it encounters a page that does not belong to the user.
            - The function returns a dictionary with a 'status code' key indicating the success or failure of the operation. If the operation is successful, the 'data' key contains the details of the movies found. If the operation fails, the 'data' key contains an error message.
        """
        links = {}
        counter , page = 1 , 1
        try :
            while True :
                url = f"https://zarfilm.com/page/{page}/?s={search_term.replace(' ' , '+')}"
                try :
                    response = get(url)
                except :
                    return {'status code': '0', 'data': 'Network Error'}
                soup = BeautifulSoup(response.content, 'html.parser')

                if  'شما' not in soup.title.text :
                    break

                for link in soup.find_all('div', class_='inner_item_body_widget'):
                    link_soup = BeautifulSoup(str(link), 'html.parser')
                    
                    title_link = link_soup.find_all('h3' , class_='movie-title')[0].text
                    href_link = link_soup.find('a').get('href')
                    thumbnail_elements = link.find_all("img", class_ = "attachment-post_cover")
                    
                    for element in thumbnail_elements:
                        hack = element['src']

                    links[str(counter)] = {
                        'title' : title_link.replace('دانلود فیلم', '').replace('دانلود سریال' , '').replace('دانلود انیمیشن' , '').replace('دانلود مستند' , '').replace(' ',''),
                        'src' : href_link,
                        'img' : hack }

                    counter = counter + 1
                page = page + 1
        except :
            return {'status code': '1', 'data': 'Failed to run the proper service.'}
        
        return {'status code': '0', 'data': links , 'copyright' : 'ZarFilm.com'}

    def get_detail_from_url(self, url : str) -> None :
        """
        Retrieves the details of a movie from a given URL.

        Args:
            url (str): The URL of the movie page.

        Returns:
            dict: A dictionary containing the following keys:
                - 'status code' (str): The status code indicating the success or failure of the operation. Possible values are '0' for success and '1' for failure.
                - 'data' (dict): If the operation is successful, this key contains a dictionary with the following keys:
                    - 'title' (str): The title of the movie.
                    - 'src' (dict): A dictionary containing the download links for different resolutions. The keys are the resolutions ('2160', '1080', '720', '480') and the values are the corresponding download links.
                    - 'img' (str): The URL of the movie's thumbnail image.
                - If the operation fails, this key contains an error message.
        """
        try :
            try :
                response = get(url)
            except :
                return {'status code': '1', 'data': 'Network Error'}
            soup = BeautifulSoup(response.content, 'html.parser')
            img = soup.select(".attachment-post_cover")[1].get("src")
            links = {}   
            for link in soup.find_all('a', class_='btndllinks'):
                    if '2160' in str(link):
                        links['2160'] = link.get('href')
                    elif '1080' in str(link):
                        links['1080'] = link.get('href')
                    elif '720' in str(link):
                        links['720'] = link.get('href')
                    elif '480' in str(link):
                        links['480'] = link.get('href')  
            title = str(soup.select("h1")[0].text).replace('دانلود فیلم', '').replace('دانلود سریال' , '').replace('دانلود انیمیشن' , '').replace('دانلود مستند' , '').replace(' ','')
            return {'title': title, 'src': links, 'img': img , 'copyright' : 'ZarFilm.com'}
        except :
            return {'status code': '1', 'data': 'Failed to run the proper service.'}

