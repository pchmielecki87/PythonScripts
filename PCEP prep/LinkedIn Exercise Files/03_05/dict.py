language = {"name": "Python", "version": 3}
language["website"] = "https://python.org"
# language["extension"] = ".py"

language["website"] = "https://python.dev"
language["version"] = 4

if "extension" not in language:
    print("No extension provided")
 
file_extension = language.get("extension", 
                             "No extension")

print(language["name"], language["version"],
      language["website"], file_extension)
