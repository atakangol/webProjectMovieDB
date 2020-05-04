CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0));
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "last_name" varchar(150) NOT NULL);
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE "main_genre" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "genreID" integer NOT NULL, "genreName" varchar(20) NOT NULL);
CREATE TABLE "main_person" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "PersonId" integer NOT NULL UNIQUE, "Pname" varchar(50) NOT NULL, "Pbirth" datetime NOT NULL);
CREATE TABLE "main_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "genreID_id" integer NOT NULL REFERENCES "main_genre" ("id") DEFERRABLE INITIALLY DEFERRED, "movieID_id" integer NOT NULL REFERENCES "main_movie" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "main_category_genreID_id_e464d2f5" ON "main_category" ("genreID_id");
CREATE INDEX "main_category_movieID_id_d57465b5" ON "main_category" ("movieID_id");
CREATE TABLE "main_casting" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "order" integer NOT NULL UNIQUE, "movieID_id" integer NOT NULL REFERENCES "main_movie" ("id") DEFERRABLE INITIALLY DEFERRED, "personID_id" integer NOT NULL REFERENCES "main_person" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "main_casting_movieID_id_8f1719db" ON "main_casting" ("movieID_id");
CREATE INDEX "main_casting_personID_id_94247931" ON "main_casting" ("personID_id");
CREATE TABLE "main_movie" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "movieID" integer NOT NULL UNIQUE, "movieName" varchar(30) NOT NULL, "movieYear" integer NOT NULL, "directorID_id" integer NOT NULL REFERENCES "main_person" ("id") DEFERRABLE INITIALLY DEFERRED)
CREATE INDEX "main_movie_directorID_id_c856920f" ON "main_movie" ("directorID_id");
CREATE TABLE "main_list_content" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Order" integer NOT NULL, "ListID_id" integer NOT NULL REFERENCES "main_list" ("id") DEFERRABLE INITIALLY DEFERRED, "MovieID_id" integer NOT NULL REFERENCES "main_movie" ("id") DEFERRABLE INITIALLY DEFERRED)
CREATE INDEX "main_list_content_ListID_id_0d7c8e5e" ON "main_list_content" ("ListID_id");
CREATE INDEX "main_list_content_MovieID_id_51b82c5f" ON "main_list_content" ("MovieID_id");
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE TABLE "main_favorite_actor" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "PersonID_id" integer NOT NULL REFERENCES "main_person" ("id") DEFERRABLE INITIALLY DEFERRED, "UserName_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "main_favorite_actor_PersonID_id_33388ae6" ON "main_favorite_actor" ("PersonID_id");
CREATE INDEX "main_favorite_actor_UserName_id_6859adce" ON "main_favorite_actor" ("UserName_id");
CREATE TABLE "main_favorite_movie" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "movieID_id" integer NOT NULL REFERENCES "main_movie" ("id") DEFERRABLE INITIALLY DEFERRED, "UserName_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "main_favorite_movie_movieID_id_1002bed3" ON "main_favorite_movie" ("movieID_id");
CREATE INDEX "main_favorite_movie_UserName_id_a97ea66b" ON "main_favorite_movie" ("UserName_id");
CREATE TABLE "main_list" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "ListID" integer NOT NULL UNIQUE, "Date" datetime NOT NULL, "Rating" integer NOT NULL, "Public" bool NOT NULL, "ListOwner_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "main_list_ListOwner_id_0d789c54" ON "main_list" ("ListOwner_id")

