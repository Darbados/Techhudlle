Please read the below description points before start the project for review.

1. The modules used in that project, were installed in a venv, for the project, but as venv folder contains quite a lot of files, it is obviously not uploaded. But there is a requirements.txt file holding all the modules included in this project, so you can easily install them.
2. For this django project, I am using MySQL for database, and on my side I am using xampp for monitoring it with the phpmyadmin. All the tables were synced with the 'test' database, so you'll find the 'test.sql' dump in the project folder as well, in order to quickly generate the needed tables for the database. It holds some records as well.
3. For the Admin panel, there is a one superuser created with credentials: username: 'admin', password: 'sevastopol'.
4. According to the task description, we should have some components involved in communication process. In my case, I've decided to use a scraper for 'publisher', which collects data from a website: 'www.sofascore.com', for prematch, live and finished football matches.
test_task - scrapers  sofascore - scrape_soccer_live.py , scrape_soccer_prematch.py, scrape_soccer_finished.py AND the main class sofascore.py. So when you want to run any scraper you’ll have to activate your venv and them run the selected file ( any of the scrape_... ).
It will start it’s work and will save a file with the collected data and will also try to send the collected data to a particulas Django view which is written to handle the POST request. If the Django server is not running the scraper will continue it’s work in the ordinary way. So we have independent ‘publisher’.
5. The Django project contains the ordinary modules for each Django project. I.e. models ( which a linked to the mysql ), views handling the data from the scrapers, proving APIviews, and ordinary views for sending some content to templates, and templates to visualize the actual content.
6. Once you open the http://127.0.0.1:8000/football/ page you see the available options to select related to the views that return some content.
