import csv
import os

class HelpCommand:
    def __init__(self) -> None:
        self.__help_informations = {}
        if(os.path.exists("help.csv")):
            with open("help.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    self.__help_informations[row[0]] = row[1]
        else:
            with open("help.csv", "w") as f:
                writer = csv.writer(f)
                writer.writerow(["Commande", "Description"])

    def add_command(self, name, description):
        self.__help_informations[name] = description
        with open("help.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Commande", "Description"])
            for name, description in self.__help_informations.items():
                writer.writerow([name, description])

    def remove_command(self, name):
        del self.__help_informations[name]
        with open("help.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Commande", "Description"])
            for name, description in self.__help_informations.items():
                writer.writerow([name, description])

    def get_help_informations(self):
        return "```\n" + "\n".join([f"{name} : {description}" for name, description in self.__help_informations.items()]) + "\n```"

    def __str__(self) -> str:
        return f"HelpCommand({self.__help_informations})"
    
    def __repr__(self) -> str:
        return f"HelpCommand({self.__help_informations})"

if __name__ == "__main__":
    help_command = HelpCommand()
    print(help_command.get_help_informations())
    print(help_command)