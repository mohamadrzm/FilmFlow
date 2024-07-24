
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mohamadrzm/FilmFlow">
    <img id='readme-top' src="logo-github.png" alt="Logo" >
  </a>

  <h3 align="center">FilmFlow | فیلم فلو</h3>

  <p align="center">
    با فیلم فلو به راحتی از سایت های مختلف لینک دانلود دریافت کنید.
    <br />
    <br />
    <br />
    <br />
    <br />
    <a href="https://github.com/mohamadrzm/FilmFlow/issues/new?labels=bug">گزارش باگ</a>
    ·
    <a href="https://github.com/mohamadrzm/FilmFlowe/issues/new?labels=enhancement">پیشنهاد قابلیت جدید</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>فهرست مطالب</summary>
  <ol>
    <li>
      <a href="#about-the-project">درباره فیلم فلو</a>
      <ul>
        <li><a href="#built-with"> فیلم فلو با چی ساخته شده ؟</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">شروع کنید</a>
      <ul>
        <li><a href="#prerequisites">پیش نیاز ها</a></li>
        <li><a href="#installation">نصب</a></li>
      </ul>
    </li>
    <li><a href="#usage">استفاده</a></li>
    <li><a href="#roadmap">نقشه راه</a></li>
    <li><a href="#contributing">مشارکت در توسعه</a></li>
    <li><a href="#license">مجوز</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## درباره فیلم فلو

فیلم فلو، یک ابزار ساده، با ایده ساده ست. دسترسی داشتن به کلی سایت فیلم و سریال، در یک سایت و در یک سرویس. فیلم فلو صفحات سایت های مختلف رو میگرده و به نسبت اسم یا آدرس سایت خاصی که بهش میدید میره و لینک های دانلود اون فیلم رو در صورت داشتن آدرس مشخص فیلم براتون میفرسته یا با دادن نام فیلم، لیستی از فیلم هایی که پیدا کرده با آدرس دقیق اون فیلم ها بهتون میده :)

<p align="right">(<a href="#readme-top">برو بالا</a>)</p>



### فیلم فلو با چی ساخته شده ؟

فیلم فلو با پایتون نوشته شده و از کتابخونه BeautifulSoup برای جمع آوری لینک های دانلود و لیست فیلم ها استفاده میکنه

همچنین از کتابخونه های flask و fastapi برای راه اندازی رابط برنامه نویسی استفاده میکنه

**تکنولوژی های فیلم فلو** :

[![techs](https://skillicons.dev/icons?i=python,fastapi,flask&theme=dark)](https://www.linkedin.com/in/mohamadreza-mirjani-7841542b8/)


<p align="right">(<a href="#readme-top">برو بالا</a>)</p>



<!-- GETTING STARTED -->
## چجوری از فیلم فلو استفاده کنم ؟

استفاده از فیلم فلو خیلی ساده ست فقط کافیه چنتا مرحله کوچیک رو طی کنید :)

### دانلود پروژه به سیستم خودتون
با دستور زیر فیلم فلو رو  دانلود کنید تو سیستم خودتون :
   ```sh
   git clone hhttps://github.com/mohamadrzm/FilmFlow
   ```
و سپس به پوشه فیلم فلو برید :
   ```sh
   cd FilmFlow
   ```
### پیش نیاز ها

ابتدا با دستور زیر پکیج هایی که فیلم فلو بهشون نیاز داره رو نصب کنید :

  ```sh
  pip install -r requirements.txt
  ```

### اجرای رابط برنامه نویسی
فیلم فلو هم از فلسک هم از فست ای پی آی استفاده میکنه برای تبادل اطلاعات بین برنامه شما و خودش 

اگه از فلسک خوشتون میاد با دستور زیر سرور فلسک رو اجرا کنید :
Clone the repo
   ```sh
   cd Apis  && flask --app flask_app run
   ```
و اگه از فست ای پی آی خوشتون میاد میتونید با دستور زیر سرورش رو اجرا کنید :
   ```sh
   cd Apis  && fastapi dev fastapi_app.py
   ```


اجرا میشه `http://127.0.0.1:5000` سرور فلسک روی 
اجرا میشه `http://127.0.0.1:8000`و سرور فست ای پی آی روی 


<p align="right">(<a href="#readme-top">برو بالا</a>)</p>



<!-- USAGE EXAMPLES -->
## چطوری از فیلم فلو استفاده کنم ؟

رابط های برنامه نویسی فیلم فلو در کل به دو شکل کلی زیر هستن :

برای جستجوی فیلم با نام فیلم :
`/v1/{sourcesite}/search/{search_term}`

و برای دریافت لینک های دانلود فیلم با آدرس اون فیلم :

`/v1/{sourcesite}/get_movie/`

یک مثال خوب :
 من از فیلم 12 مرد خشمگین خیلی خوشم میاد و میخوام لینک دانلودش رو داشته باشم :

: برای همین یک درخواست میزنم به این آدرس  :

 `http://127.0.0.1:8000/v1/digimoviez/get_movie/`
و این ادرس متد POST میگیره

و اطلاعات زیر رو براش به صورت json میفرستم :

``` json
{
    
  "url" : "https://digimoviez.com/12-angry-men-1957/"

}
```

دقت کنید آدرس من برای سایت دیجی موویز هستش و sourcesite هم دیجی موویز گذاشتم
و همچین دیتایی دریافت میکنید :

``` json
{
  "data": {
    "title": "۱۲AngryMen1997",
    "src": {
      "720": "https://dl3.cdnfo.info/Movies6/1997/12.Angry.Men.1997/12.Angry.Men.1997.720p.BrRip.YIFY.ZarFilm.mp4?md5=bb2134ca5ce374baa93dca0f60c6158e&expires=1721816151",
      "1080": "https://dl3.cdnfo.info/Movies6/1997/12.Angry.Men.1997/12.Angry.Men.1997.10bit.1080p.x265.BrRip.RARBG.ZarFilm.mp4?md5=af687778689a8f4fd72f22e13336ec10&expires=1721816151"
    },
    "img": "https://digimovies.com/wp-content/uploads/2024/03/MV5BNDhjMjE4NDItZTkyOC00NjIwLWI0MDQtYTJhZjY2YzlkMDQ0XkEyXkFqcGdeQXVyMTA0MTM5NjI2._V1_SX500-207x310.jpg",
    "copyright": "digimovies.com"
  }
}
```
حالا من میخوام فیلم 12 مرد خشمگین رو سرچ کنم و یه لیست از فیلم های با همین شباهت اسم بگیرم با آدرس دقیقشون تو سایت :
 `http://127.0.0.1:8000/v1/digimoviez/search/12-angry-men`
 این آدرس متد GET میگیره
 و به جای search_term هر اسمی میتونید بذارید

 در پاسخ این درخواست همچین دیتایی دریافت میکنید :

 ``` json
{
  "data": {
    "status code": "0",
    "data": {
      "1": {
        "title": "12AngryMen",
        "src": "https://digimovies.com/12-angry-men-1997/",
        "img": "https://digimovies.com/wp-content/uploads/2024/03/MV5BNDhjMjE4NDItZTkyOC00NjIwLWI0MDQtYTJhZjY2YzlkMDQ0XkEyXkFqcGdeQXVyMTA0MTM5NjI2._V1_SX500-207x310.jpg"
      },
      "2": {
        "title": "12AngryMen",
        "src": "https://digimovies.com/12-angry-men-1957/",
        "img": "https://digimovies.com/wp-content/uploads/2019/11/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SX500-210x310.jpg"
      }
    },
    "copyright": "digimovies.com"
  }
}
```
<p align="right">(<a href="#readme-top">برو بالا</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add zarfilm and digimovies
- [x] Add apis
- [ ] Add Additional sites
- [ ] Add Filmflow to Pypi

<p align="right">(<a href="#readme-top">برو بالا</a>)</p>



<!-- CONTRIBUTING -->
## مشارکت

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. پروژه رو فورک کنید
2. یک برانچ جدید بسازید (`git checkout -b dev/AmazingFeature`)
3. تغییرات خودتون رو کامیت کنید (`git commit -m 'Add some AmazingFeature'`)
4. برانچتوت رو پوش کنید (`git push origin dev/AmazingFeature`)
5. پول ریکوئست بزنید

<p align="right">(<a href="#readme-top">برو بالا</a>)</p>



<!-- LICENSE -->
## مجوز

GPL - 3.0 License. `LICENSE.txt` 





