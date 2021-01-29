DROP TABLE IF EXISTS `Categories`;
DROP TABLE IF EXISTS `Tags`;
DROP TABLE IF EXISTS `Reactions`;
DROP TABLE IF EXISTS `PostReactions`;
DROP TABLE IF EXISTS `Posts`;
DROP TABLE IF EXISTS `PostTags`;
DROP TABLE IF EXISTS `Comments`;
DROP TABLE IF EXISTS `Subscriptions`;
DROP TABLE IF EXISTS `DemotionQueue`;
DROP TABLE IF EXISTS `Users`;

CREATE TABLE "AccountTypes" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "password" varchar,
  "bio" varchar,
  "username" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit,
  "account_type_id" INTEGER,
  FOREIGN KEY(`account_type_id`) REFERENCES `AccountTypes`(`id`)
);
CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);
CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit
);
<<<<<<< HEAD
=======
CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  "created_on" DATETIME,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
>>>>>>> main
CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);
CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);
CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);
CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  "created_on" DATETIME,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

INSERT INTO `Posts` VALUES (null, 1, 2, "Title 1", 01282021, "fake url", "fake news", TRUE);
INSERT INTO `Posts` VALUES (null, 1, 2, "Title 2", 01282021, "fake url", "fake news", TRUE);


INSERT INTO `Comments` VALUES (null, 1, 2, "Comment 1", 01282021);
INSERT INTO `Comments` VALUES (null, 2, 1, "Comment 2", 01292021);
INSERT INTO `Comments` VALUES (null, 1, 2, "Comment 3", 01302021);
INSERT INTO `Comments` VALUES (null, 2, 1, "Comment 4", 01302021);


INSERT INTO `Users` VALUES(null, "Silas", "Lowe", "silas@lowe.gmal", "Ahhhh", "I are me", "Slowe", "www.silaslowe.net", "10/10/10", "True", 2)

INSERT INTO `Users` VALUES(null, "Frank", "Frankerson", "frank@lowe.gmal", "Yaaaaaaa", "I are not me", "Flowe", "www.frankerson.net", "11/11/11", "True", 1)
INSERT INTO `Tags` VALUES (null, "Food");
INSERT INTO `Tags` VALUES (null, "Mouth-breathing");
INSERT INTO `Tags` VALUES (null, "Sports");

INSERT INTO `Users` VALUES(null, "Silas", "Lowe", "silas@lowe.gmal", "Ahhhh", "I are me", "Slowe", "www.silaslowe.net", "10/10/10", "True", 2);
INSERT INTO `Users` VALUES(null, "Frank", "Frankerson", "frank@lowe.gmal", "Yaaaaaaa", "I are not me", "Flowe", "www.frankerson.net", "11/11/11", "True", 1);

SELECT * FROM Comments;

DROP TABLE IF EXISTS `Comments`;

SELECT
           *
        FROM Comments c;
INSERT INTO `Posts` VALUES (null, 1, 2, "Title 1", 01282021, "fake url", "fake news", TRUE);
INSERT INTO `Posts` VALUES (null, 1, 2, "Title 2", 01282021, "fake url", "fake news", TRUE);

INSERT INTO `Users` VALUES(null, "Silas", "Lowe", "silas@lowe.gmal", "Ahhhh", "I are me", "Slowe", "www.silaslowe.net", "10/10/10", "True", 2);
INSERT INTO `Users` VALUES(null, "Frank", "Frankerson", "frank@lowe.gmal", "Yaaaaaaa", "I are not me", "Flowe", "www.frankerson.net", "11/11/11", "True", 1);
INSERT INTO `Tags` VALUES (null, "Food");
INSERT INTO `Tags` VALUES (null, "Mouth-breathing");
INSERT INTO `Tags` VALUES (null, "Sports");

SELECT
 *
FROM Comments;



<<<<<<< HEAD
=======
INSERT INTO `Categories` VALUES ( null, "Category 1");
INSERT INTO `Categories` VALUES ( null, "Category 2");

>>>>>>> main
