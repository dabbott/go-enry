import yaml
import sys


def filter_yaml_languages(file_path, languages):
    # Read the YAML content from the file
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)

    # Filter the dictionary based on the provided languages
    filtered_data = {key: data[key] for key in languages if key in data}

    # Write the filtered dictionary back to the same file
    with open(file_path, "w") as file:
        yaml.dump(filtered_data, file, sort_keys=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python filter_languages.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    languages = [
        "Text",
        "Batchfile",
        "C#",
        "C++",
        "Clojure",
        "CoffeeScript",
        "CSP",
        "CSS",
        "Dockerfile",
        "F#",
        "Go",
        "Handlebars",
        "HTML",
        "INI",
        "Java",
        "JavaScript",
        "Less",
        "Lua",
        "Markdown",
        "Objective-C",
        "Perl",
        "PHP",
        "PowerShell",
        "Pug",
        "Python",
        "R",
        "Redis",
        "Redshift",
        "Ruby",
        "Rust",
        "Scheme",
        "SCSS",
        "Shell",
        "Solidity",
        "SQL",
        "Swift",
        "TypeScript",
        "XML",
        "YAML",
    ]

    filter_yaml_languages(file_path, languages)
    print(f"Filtered YAML file written to {file_path}")
