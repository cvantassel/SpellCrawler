create schema spellcrawler;
use spellcrawler;

create table Website (id INT unsigned NOT NULL AUTO_INCREMENT primary key, link VARCHAR(300));
alter table Website ADD UNIQUE KEY (id, link);

drop table Website;
create table Suggestions(word VARCHAR(20), suggestion VARCHAR(20), relatedSite INT);

create user 'spellcrawl' identified by 'pass';
GRANT ALL privileges ON spellcrawler TO 'spellcrawl'@localhost IDENTIFIED BY 'pass';
-- mysql> GRANT USAGE ON *.* TO 'myuser'@'%' IDENTIFIED BY 'mypassword';
SHOW GRANTS FOR 'spellcrawl'@localhost; 
 FLUSH PRIVILEGES;
 
 insert into Website Values (2, 'google.com');
 alter table Website add constraint linkId primary key (id, link);
 ALTER TABLE Website DROP PRIMARY KEY;
 insert into Suggestions values ("booga", "booger", 1), ("yannie", "yanny", 1);
 
 insert into Website Values (2, 'facebook.com');
 insert into Suggestions values ("makr", "mark", 2), ("tes", "test", 2);
 
 select * from Suggestions;
 select * from Website;
 
 
SELECT Website.link, Suggestions.word, Suggestions.suggestion from Suggestions 
inner join Website on Website.id = Suggestions.relatedSite;