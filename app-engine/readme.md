Made changes from the main file available at https://github.com/GoogleCloudPlatform/python-docs-samples

# Commands used in my App Engine tutorial:

1. gcloud sql connect [instance_name] --user=mastergk

2. use [database_name]

3. create table demo_tbl(
   demo_id INT NOT NULL AUTO_INCREMENT,
   demo_txt VARCHAR(500) NOT NULL,
   PRIMARY KEY ( demo_id )
);

4. insert into demo_tbl(demo_id,demo_txt) values(1,"hello guys, thanks for watching my video :)");

5. select demo_txt from demo_tbl;
