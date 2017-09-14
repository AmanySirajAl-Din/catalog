#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# *import the tables from the new DB*
from database_setup_withusers import MainCategory, Base, SubCategory, User

#engine = create_engine('sqlite:///foodCatalogWithUsers.db')
engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# *Create dummy user*
User1 = User(name="Amany Siraj Al-Din", email="amanysirajaldin@gmail.com",
             picture='https://avatars1.githubusercontent.com/u/24775341?v=4&s=400')
session.add(User1)
session.commit()



# Healthy food category
foodCategory1 = MainCategory(user_id=1, name="Healthy", description="A healthy diet is one that helps to maintain or improve overall health.")

session.add(foodCategory1)
session.commit()

# *Add user_id=1 to all sub category item*

foodItem1 = SubCategory(user_id=1, name="Diabetic", description="Diabetic-friendly cakes, cookies, and more low-sugar desserts, plus dinner ideas.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Gluten-Free", description="Recipes that strictly excludes gluten, a mixture of proteins found in wheat and related grains, including barley, rye, oat, and all their species and hybrids.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Low-Sodium", description="According to the Mayo Clinic, a low-sodium recipe is one with no more than 140 milligrams of sodium per serving.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Low-fat", description="Recipes that restricts fat and often saturated fat and cholesterol as well. Low-fat diets are intended to reduce diseases such as heart disease and obesity.", category=foodCategory1)

session.add(foodItem1)
session.commit()


# World Cuisine food category
foodCategory1 = MainCategory(user_id=1, name="World Cuisine", description="Boldly go where your taste buds haven't gone before with recipes from countries far and near. Your kitchen is the flight deck.")

session.add(foodCategory1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="African", description="These tasty recipes are bursting with spice and flavor. Get the recipes from Morocco, Algeria, Egypt, and more.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Middle Eastern", description="Find your favorite Middle Eastern recipes for hummus, falafel, tabbouleh, kebabs, phyllo pastries, and more.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Japanese", description="Bring the bento box home with more than 220 trusted Japanese recipes for chicken teriyaki, sushi, miso soup, and yakisoba.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Italian", description=" is food typical from Italy. It has developed through centuries of social and economic changes. Italian-style pasta, chicken dishes, soup, and more. Traditional recipes with photos and videos to make them just like in the old country.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="U.S.", description="Recipes from across the United States! There are recipes for every region and state, including mouthwatering Southern favorites, classic fare from New England, and spicy Southwest dishes.", category=foodCategory1)

session.add(foodItem1)
session.commit()


# Dessert food category
foodCategory1 = MainCategory(user_id=1, name="Dessert", description="Dessert is a confectionery course that concludes a main meal. The course usually consists of sweet foods and beverages, such as dessert wine or liqueurs, but may include coffee, cheeses, nuts, or other savory items. In some parts of the world, such as much of central and western Africa, and most parts of China, there is no tradition of a dessert course to conclude a meal. Whether you crave sweet, savory, decadent or healthy, dessert recipes have hundreds of recipes to satisfy your taste buds.")

session.add(foodCategory1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Cookie", description="A cookie is a baked or cooked good that is small, flat and sweet. It usually contains flour, sugar and some type of oil or fat. It may include other ingredients such as raisins, oats, chocolate chips, nuts, etc.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Cake", description="Cake is a form of sweet dessert that is typically baked. In its oldest forms, cakes were modifications of breads, but cakes now cover a wide range of preparations that can be simple or elaborate, and that share features with other desserts such as pastries, meringues, custards, and pies.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Chocolate Dessert", description="Chocolate is a typically sweet, usually brown food preparation of Theobroma cacao seeds, roasted and ground. It is made in the form of a liquid, paste, or in a block, or used as a flavoring ingredient in other foods. Chocolate recipes such as decadent cakes, cookies, fudge, and cheesecakes. When your sweet tooth screams for chocolate, chocolate will help you answer the call.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Pie Dessert", description="A pie is a baked dish which is usually made of a pastry dough casing that covers or completely contains a filling of various sweet or savoury ingredients. Pies are defined by their crusts. A filled pie (also single-crust or bottom-crust), has pastry lining the baking dish, and the filling is placed on top of the pastry but left open. A top-crust pie has the filling in the bottom of the dish and is covered with a pastry or other covering before baking. A two-crust pie has the filling completely enclosed in the pastry shell. Shortcrust pastry is a typical kind of pastry used for pie crusts, but many things can be used, including baking powder biscuits, mashed potatoes, and crumbs. Pies can be a variety of sizes, ranging from bite-size to ones designed for multiple servings.", category=foodCategory1)

session.add(foodItem1)
session.commit()


# Main Dish food category
foodCategory1 = MainCategory(user_id=1, name="Main Dish", description='The main dish is usually the heaviest, heartiest, and most complex or substantial dish on a menu. The main ingredient is usually meat, fish or another protein source. It is most often preceded by an appetizer, soup or salad, and followed by a dessert. For those reasons the main course is sometimes referred to as the "meat course". The main course is the featured or primary dish in a meal consisting of several courses. It usually follows the entree ("entry") course. In the United States and parts of Canada, it may be called "entree".')

session.add(foodCategory1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Chicken Main Dish", description=" Chicken is the most common type of poultry in the world,[1] and was one of the first domesticated animals. Chicken is a major worldwide source of meat and eggs for human consumption. It is prepared as food in a wide variety of ways, varying by region and culture. The prevalence of chickens is due to almost the entire chicken being edible, and the ease of raising them.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Pasta Main Dish", description="Pasta is a staple food of traditional Italian cuisine. It is also commonly used to refer to the variety of pasta dishes. Pasta is, typically a noodle made from an unleavened dough of a durum wheat flour mixed with water and formed into sheets or various shapes, then cooked and served in any number of dishes. It can be made with flour from other cereals or grains, and eggs may be used instead of water.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Beef Main Dish", description="Beef is the culinary name for meat from bovines, especially cattle. Beef can be harvested from cows, bulls, heifers or steers. Acceptability as a food source varies in different parts of the world. Beef is the third most widely consumed meat in the world, accounting for about 25% of meat production worldwide, after pork and poultry at 38% and 30% respectively. In absolute numbers, the United States, Brazil, and the People's Republic of China are the world's three largest consumers of beef. On a per capita basis in 2009, Argentines consumed the most beef at 64.6 kg per person; people in the U.S. ate 40.2 kg, while those in the E.U. ate 16.9 kg.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Seafood Main Dish", description="Seafood dishes are distinct food dishes[1] which use seafood (fish, shellfish or seaweed) as primary ingredients, and are ready to be served or eaten with any needed preparation or cooking completed. Many fish or seafood dishes have a specific names (cioppino), while others are simply described (fried fish) or named for particular places (Cullen skink). Bisques are prepared with a variety of seafoods.", category=foodCategory1)

session.add(foodItem1)
session.commit()

foodItem1 = SubCategory(user_id=1, name="Vegetable Main Dish", description="Dishes in which the main ingredient or one of the essential ingredients is a vegetable or vegetables. In culinary terms, a vegetable is an edible plant or its part, intended for cooking or eating raw. Many vegetable-based dishes exist throughout the world.", category=foodCategory1)

session.add(foodItem1)
session.commit()


print "added food categories!"