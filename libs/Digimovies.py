from bs4 import BeautifulSoup
from requests import get
class DigiMovies() :
    def __init__(self) -> None:
        pass
        
    def get_detail_from_name(self, search_term : str ) -> dict:
        """
        Retrieves details of movies based on a search term from the Digimoviez website.

        Args:
            search_term (str): The search term to find movies.

        Returns:
            dict: A dictionary containing the status code and data.
                - If successful, the status code is '2' and the data is a dictionary with movie details.
                - If there is a network error, the status code is '1' and the data is 'Network Error'.
                - If the service fails to run properly, the status code is '1' and the data is 'Failed to run the proper service.'.

        Raises:
            None

        Example:
            >>> digimovies = DigiMovies()
            >>> result = digimovies.get_detail_from_name('The Matrix')
            >>> result
            {'status code': '2', 'data': {
                '1': {'title': 'TheMatrix', 'src': 'https://digimoviez.com/the-matrix', 'img': 'https://digimoviez.com/the-matrix-poster.jpg'},
                '2': {'title': 'TheMatrixReloded', 'src': 'https://digimoviez.com/the-matrix-reloaded', 'img': 'https://digimoviez.com/the-matrix-reloaded-poster.jpg'},
                '3': {'title': 'TheMatrixRevolutions', 'src': 'https://digimoviez.com/the-matrix-revolutions', 'img': 'https://digimoviez.com/the-matrix-revolutions-poster.jpg'}
            }}
        """
        links , counter , page = {} , 1 , 1
        try :
            while True :
                url = f"https://digimoviez.com/page/{page}/?s={search_term.replace(' ' , '+')}"
                try :
                    response = get(url )
                except :
                    return {'status code': '1', 'data': 'Network Error'}
                soup = BeautifulSoup(response.content, 'html.parser')

                if 'Security'  in  soup.title.text:
                    return {'status code': '1', 'data': 'Failed to connect site.'}
                    
                if soup.title.text == 'صفحه پیدا نشد - دیجی موویز' :
                    break

                for link in soup.find_all('h2', class_='lato_font'):
                    imgs = soup.find_all('img', class_='attachment-poster_thumbnail')
                    link_soup = BeautifulSoup(str(link), 'html.parser')
                    img_soup = BeautifulSoup(str(imgs), 'html.parser')
                    href_link = link_soup.find('a').get('href')
                    img_link = img_soup.find('img').get('src')
                    title_link = link_soup.text
                    print('ok5')
                    links[str(counter)] = {
                        'title' : title_link.replace('دانلود فیلم', '').replace('دانلود سریال' , '').replace('دانلود انیمیشن' , '').replace('دانلود مستند' , '').replace(' ',''),
                        'src' : href_link,
                        'img' : img_link }

                    counter = counter + 1
                page = page + 1
        except :
            return {'status code': '1', 'data': 'Failed to run the proper service.'}
        
        return {'status code': '2', 'data': links , 'copyright' : 'digimoviez.com'}

    def get_detail_from_url(self, url : str) -> None :
        """
        This function retrieves details such as title, source links, and image from the provided URL.
        
        Parameters:
            url (str): The URL to extract details from.
        
        Returns:
            dict: A dictionary containing the title, source links, and image.
                  Format: {'title': str, 'src': {'2160': str, '1080': str, '720': str, '480': str}, 'img': str}
                  or
                  {'status code': '1', 'data': 'Failed to run the proper service.'}
        """
        try :
            try :
                response = get(url)
            except :
                return {'status code': '1', 'data': 'Network Error'}
            soup = BeautifulSoup(response.content, 'html.parser')
            img = soup.select(".attachment-post-thumbnail , .size-post-thumbnail , .wp-post-image")[0].get("src")
            links = {}   
            for link in soup.find_all('a', class_='btn_dl'):
                    if '2160' in str(link):
                        links['2160'] = link.get('href')
                    elif '1080' in str(link):
                        links['1080'] = link.get('href')
                    elif '720' in str(link):
                        links['720'] = link.get('href')
                    elif '480' in str(link):
                        links['480'] = link.get('href')  
            title = soup.select("h1")[0].text
            return {'title': title, 'src': links, 'img': img , 'copyright' : 'digimoviez.com'}
        except :
            return {'status code': '1', 'data': 'Failed to run the proper service.'}
        



