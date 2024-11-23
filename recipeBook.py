# Recipe book

class RecipeBook:
    def __init__(self,myrecipe):
        self.filename=myrecipe
        self.recipes=[]

    def create_recipe(self, name, ingredients, method):
        recipe = {"name": name, "ingredients": ingredients, "method": method}
        self.recipes.append(recipe)
        self.save_recipe(recipe)

    def add_ingredients(self, name, ingredients):
        for recipe in self.recipes:
            if recipe["name"] == name:
                recipe["ingredients"] += ingredients
                self.save_recipe(recipe) 
                return
        print(f"Recipe {name} not found!")

    def cooking_method(self, name, method):
        for recipe in self.recipes:
            if recipe["name"] == name:
                recipe["method"] = method
                self.save_recipe(recipe) 
                return
        print(f"Recipe {name} not found!")

    def save_recipe(self, recipe):
        with open(self.filename, 'a') as file:
            file.write(f"Recipe Name: {recipe['name']}\n")
            file.write("Ingredients:\n")
            for ingredient in recipe["ingredients"]:
                file.write(f"{ingredient}\n")
            file.write(f"Cooking Method: {recipe['method']}\n\n")

    def load_recipe(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"No recipe file found at {self.filename}")

newRecipe=RecipeBook("myRecipes.txt")
newRecipe.create_recipe("Salad", ["lettuce", "tomatoes", "cucumbers", "carrots"], "Rinse all the vegetables with water.\nPeel and chop them into small peices.")
newRecipe.load_recipe()
newRecipe.add_ingredients("Salad", ["Cheese", "nuts","seeds"])
newRecipe.cooking_method("Salad", "Mix all the vegetables and ingredients.")
newRecipe.load_recipe() 

