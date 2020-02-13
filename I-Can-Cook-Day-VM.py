print("I Can Cook Day informational quiz. \nNutritional Facts \nRecipe/instructions \nby VM '23")

print ("Welcome to the NUTRIWORLD")
print ("Type the corresponding number for the following questions.")

def ask1():
    ask = int(input("""What do you want to know about this food:
    1. Nutrition Facts
    2. How to make it
    
    """))
    return ask

a = int(input("""what do you want to cook:
1. Bean Burritos
2. Burgers
3. Vanilla Mug Cake
4. New Orleans Gumbo
5. Pepperoni Pizza
6. Dinner Rolls
7. Hot Cocoa

"""))

if a == 1:
    ask = ask1()
    print(type(ask))
    if ask==1:
        print ("""
Calories: 584
Total Fat:: 17 grams
Saturated Fat:: 6.6 grams
Trans Fat: 0.3: grams
Polyunsaturated Fat:: 6.4 grams
Monounsaturated Fat:: 3.6 grams
Cholesterol: 14 milligrams
Sodium: 1605 milligrams
Potassium: 744 milligrams
Total Carbohydrates: 89 grams
Dietary Fiber: 12 grams
Sugars: 4.9 grams
Protein: 21g""")
    else:
        print ("""
All you need for these crispy bean and cheese burritos recipe is a can of refried beans, some pantry spices, and shredded cheese. First, mix together the refried beans, cumin, salsa, chili powder and garlic powder. Then, add a spoonful of the beans mixture to your tortilla and smooth it into an even layer. After, sprinkle with shredded cheese and roll it up. Add a little bit of oil to a saute pan over medium heat. Add the rolled burritos to the hot pan and toast them, turning them occasionally until golden brown on all sides.""")

elif a == 2:
    ask = ask1()
    print(type(ask))
    if ask == 1:
        print("""
Calorie: 540
Total Fat:: 27 grams
Saturated Fat:: 11 grams
Polyunsaturated Fat:: 2.8 grams
Monounsaturated Fat:: 10 grams
Cholesterol 122: milligrams
Sodium: 791 milligrams
Potassium: 570 milligrams
Total Carbohydrates: 40 grams
Protein: 34g""")
    else:
        print("""
Add 80% lean ground beef to a large bowl.Then, add Worcestershire sauce, seasoning salt, garlic powder, and pepper. Next, Mix with your hands until well combined. Following this, divide the beef into fourths. Then, use your hands to form 4 hamburger patties 3/4 inch thick. Next, use your thumbs to make an indention in the middle of the patties.Then, grill over medium-high heat for about 4 minutes on each side. Next, serve on hamburger buns. Lastly, top with your favorite traditional burger toppings (lettuce, tomato, onion, pickles, ketchup, etc.)""")

elif a == 3:
    ask = ask1()
    print(type(ask))
    if ask == 1:
       print("""
Calories: 293
Total Fat:: 13 grams
Saturated Fat:: 2.2 grams
Polyunsaturated Fat:: 4.8 grams
Monounsaturated Fat:: 5.7 grams
Cholesterol: 56 milligrams
Sodium: 202 milligrams
Potassium: 40 milligrams
Total Carbohydrates: 42 grams
Dietary Fiber: 0.2 grams
Sugars: 31 grams
Protein: 2.2 grams""")
    else:
        print("""Add flour, sugar, baking powder, and salt to a mug and stir together. Stir in milk, melted butter, and vanilla extract until smooth, being sure to scrape the bottom of the mug. Stir in sprinkles. Cook in microwave for 70-90 seconds* (until cake is just set, but still barely shiny on top). Allow to rest in microwave for 1 minute before consuming.""")
elif a==4:
    ask = ask1()
    print(type(ask))
    if ask ==1:
        print("""
Calories 442
Total Fat:: 17 grams
Saturated Fat:: 5.5 grams
Trans Fat:: 0.1 grams
Polyunsaturated Fat:: 2.4 grams
Monounsaturated Fat:: 6.6 grams
Cholesterol: 67 milligrams
Sodium: 771 milligrams
Potassium: 505 milligrams
Total Carbohydrates: 47 grams
Dietary Fiber: 1.1 grams
Sugars: 1.8 grams
Protein: 23 grams""")
    else:
        print("""Make the Roux*: In a large, heavy bottom stock pot combine flour and oil. Cook on medium-low heat, stirring constantly for 30-45 minutes. This part takes patience--when it's finished it should be as dark as chocolate and have a soft, "cookie dough" like consistency. Be careful not to let it burn! Feel free to add a little more flour or oil as needed to reach this consistency. Brown the sausage. In a separate skillet on medium-high heat place the sausage slices in one layer in the pan. Brown them well on one side (2-3 minutes) and then use a fork to flip each over onto the other side to brown. Remove to a plate. Cook the vegetables in broth. Add 1/2 cup of the chicken broth to the hot skillet that had the sausage to deglaze the pan. Pour the broth and drippings into your large soup pot. Add remaining 5 1/2 cups of chicken broth. Add veggies, parsley, and roux to the pot and stir well. Bring to a boil over medium heat and boil for 5-7 minutes, or until the vegetables are slightly tender. (Skim off any foam that may rise to the top of the pot.) Stir in cajun seasoning, to taste. Add meat. Add chicken, sausage, and shrimp. Taste and serve. At this point taste it and add more seasonings to your liking--salt, pepper, chicken bullion paste, garlic, more Joe's stuff or more chicken broth--until you reach the perfect flavor. Serve warm over rice. (Tastes even better the next day!)""")
elif a==5:
    ask = ask1()
    print(type(ask))
    if ask==1:
        print("""
Calories: 313
Total Fat: 13: grams
Saturated Fat: 5.7: grams
Trans Fat: 0.3: grams
Polyunsaturated Fat: 2.3: grams
Monounsaturated Fat: 4.3: grams
Cholesterol 28: milligrams
Sodium 760: milligrams
Potassium 216: milligrams
Total Carbohydrates 35: grams
Dietary Fiber 2.6: grams
Sugars: 3.6 grams
Protein 13 grams""")
    else:
        print("""Preheat your oven to 450 degrees F. Pre-bake your pizza dough for 6 minutes then top your prebaked pizza dough with a thin layer of pizza sauce. Then add a thin layer of mozzarella cheese, a layer of pepperoni, and sprinkle another thin layer of cheese on top of the pepperoni. Bake at 450 F for 10 -15 minutes or until crust is golden brown and cheese is bubbly. """)
elif a==6:
    ask = ask1()
    print(type(ask))
    if ask ==1:
        print("""
Calories: 76
Total Fat: 1.8: grams
Saturated Fat: 0.4: grams
Polyunsaturated Fat: 0.3: grams
Monounsaturated Fat: 0.9: grams
Cholesterol 0: milligrams
Sodium 147: milligrams
Potassium 32: milligrams
Total Carbohydrates 13: grams
Dietary Fiber 1.1: grams
Sugars 0.5: grams
Protein: 2.4 grams""")
    else:
        print("""Combine warm water, yeast, and 1/4 tsp sugar and stir--allow to rest for 5-10 minutes until foamy. Pour yeast mixture into the bowl of an electric stand mixer (or into a large bowl if you plan on kneading by hand). Add remaining 1/3 cup sugar, warm milk, butter, egg and salt. Blend mixture until combine. While mixing on low speed, slowly add the flour, mixing until the dough is smooth and elastic, about 5 - 6 minutes. You may not use all of the flour called for! The dough should be soft, very slightly sticky when touched with a clean finger. It should be pulling away from the sides of the mixer. Grease a large bowl with cooking spray or a tiny bit of oil. Place the dough in the bottom of the bowl and turn it over once to coat all sides in oil (this helps keep it from drying out.) Cover the bowl with plastic wrap. Allow to rise in a warm place until double in size, about 1 hour. Divide dough into two equal portions. Roll each dough ball out on a lightly floured surface into a large rectangle about 1/4’’ thick. Use a pizza cutter or sharp knife to cut the dough, lengthwise, into two pieces. Then slice the dough into six strips across so you end up with 12 small rectangles. Roll each small rectangle up like a snail and place, open edge down, on a lightly greased or lined baking sheet. Repeat with the second portion of dough. Cover rolls loosely with plastic wrap and allow to rise again in a warm place until double in size, about 1 hour. Preheat oven to 375 degrees F. Remove plastic wrap and bake rolls for 10 - 13 minutes until cooked and golden brown. Remove from oven and brush tops with butter. Store rolls in an air-tight container. They also freeze really well.""")
elif a==7:
    ask = ask1()
    print(type(ask))
    if ask ==1:
        print("""
Calories: 151
Total Fat: 1.5 grams
Saturated Fat: 0.9 grams
Trans Fat: 0.3 grams
Polyunsaturated Fat: 0 grams
Monounsaturated Fat: 0.5 grams
Cholesterol: 0 milligrams
Sodium: 200 milligrams
Total Carbohydrates: 32 grams
Dietary Fiber: 1.4 grams
Sugars: 25 grams
Protein: 2.5g""")
    else:
        print("""Combine the cocoa and sugar in a saucepan over medium-low heat. Add a dash of salt and the boiling water. Bring the mixture to a slow boil, stirring continuously. Once boiling, turn down to a simmer and stir continually for 2 minutes. Stir in milk and heat until very hot, but not boiling! Remove from heat and add vanilla. Divide between 4 mugs. Add the half & half to the mugs of cocoa to cool it to drinking temperature. Top with whipped cream if desired!""")
