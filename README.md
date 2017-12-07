Log Analysis Project
====================
This is an internal reporting tool that will use the information from the news database to discover what kind of articles the site's readers like. 

Introduction:
-------------
This python module builds an informative summary from logs using complex quefies. There are three tables in the news database: authors, articles, and log.

* The **authors** table has information about the authors that write the articles.
* The **articles** table has information about the articles on the website.
* The **log** table records information everytime an article is accessed by news readers.

This project provides the following information:

*The three most popular articles on the website.
```python
def popular_articles()
```
*The three most popular authors on the website.
```python 
def popular_authors()'
```
*The days with more than 1% errors while accessing websites.
```python
def error_days()
```

Views:
------

To acheive results for the third question, the following views were made:

*accesses
```
create view access as select date(time) as date, count(*) as accesses
from log group by date order by accesses desc;
```

*errors
```
create view error as select date(time) as errordate, count(*) as errors
from log where status like '%404%' group by errordate order by errors desc;
```

Instructions:
-------------
* Download [Vagrant](https://www.vagrantup.com/) and virtualbox[Virtialbox](https://www.virtualbox.org/wiki/Downloads), and install them.

* Clone [this](https://github.com/udacity/fullstack-nanodegree-vm) repository:

* from your shell, go to the ditectory that contains the .vagrant file and run there commands to set up the linux VM:
```vagrant up```
and then
```vagrant ssh```

* Download this [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip it. Copy the file inside it(newsdata.sql) into the vagrant directory.

* Now load the database into the VM using this command:
```psql -d news -f newsdata.sql;```

* Now, create the views described above by copying the code given above.

* Run Module
```python
analyzer.py
```
* The output is:
![result]("https://raw.githubusercontent.com/mainala/Log-Analysis-Project/master/result.PNG")




