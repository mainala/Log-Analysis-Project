#Code for analyzing data of a news database
#
#Author: Ayush Mainali

import psycopg2

DBNAME = "news"

print('')

"""This function prints out the name and number of views for the three most popular articles in the news database"""
def popular_articles():
    db = psycopg2.connect(database=DBNAME)
    c=db.cursor()
    c. execute("select title, num from articles, (select substring(path from 10) as "
               "slugfound,  count(*) as num from log where path like '/article/%' "
               "group by path order by num desc limit 3) as slugfinder where slug = "
               "slugfound order by num desc;")
    print("Most popular three articles:")
    rows = c.fetchall()
    
    for row in rows:
        print("{:<35s}:{:>10d}".format(str(row[0]), row[1])+" views")
    print('')
    db.close()

"""This function prints out the name and number of views for the three most popular authors in the nws database"""
def popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c=db.cursor()
    c. execute("select name, count(*) from (select name, slug from authors join articles "
               "on authors.id = articles.author order by name) as slugfind join log on "
               "log.path like '%'||slugfind.slug||'%' where name != 'Anonymous Contributor'"
               "group by name order by count(*) desc;")
    print("Most popular three authors:")
    rows = c.fetchall()
    
    for row in rows:
            print("{:<35s}:{:>10d}".format(str(row[0]), row[1])+" views")
    print('')
    db.close()

"""This function prints out the days with more than 1% errors"""
def error_days():
    db = psycopg2.connect(database=DBNAME)
    c=db.cursor()
    c. execute("select date,  (errors * 100.00/accesses) as percent from access join error "
               "on access.date=error.errordate where (errors * 100.00/accesses) > 1.00;")
    print("Days with more than 1% errors:")
    rows =c.fetchall()
    
    for row in rows:
        print("{:<35s}:{:>10.2f}".format(str(row[0]), row[1])+"%")
    print('')
    db.close()

def main():        
    popular_articles()
    popular_authors()
    error_days()

if __name__ == "__main__":
    main()

