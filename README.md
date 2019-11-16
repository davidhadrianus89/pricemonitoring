# pricemonitoring development guidance


- sudo pip install virtualenv virtualenvwrapper
- echo 'export WORKON_HOME=$HOME/.virtualenvs' | tee --append ~/.bashrc
- echo 'source /usr/local/bin/virtualenvwrapper.sh' | tee --append ~/.bashrc
- source ~/.bashrc

- mkvirtualenv --no-site-packages pricemonitoring
- workon pricemonitoring

- cd /home/<ubuntu-user>/Desktop("choose your working directory")
- git clone https://github.com/davidhadrianus89/pricemonitoring.git

- pip install -r requirements

- cd /<pricemonitoring directory>/price_scrapper

- scrapyd

- cd ../

- python manage.py runserver 0.0.0.0:8080

- goto http://localhost:8080/productmonitoring/

- submit url

- see result on http://localhost:8080/productmonitoring/list


