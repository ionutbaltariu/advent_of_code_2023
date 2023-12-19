import re

part_rating_rgx = re.compile(r"(\w{1})=(\d+)")
rule_parser_rgx = re.compile(r"(\w{1})([<>])(\d+):(\w+)")

if __name__ == "__main__":
    file_handler = open("19.in", "r")
    workflows, part_ratings = file_handler.read().split("\n\n")

    part_ratings_parsed = []

    for line in part_ratings.split("\n"):
        part_ratings_parsed.append({
            k: int(v) for k, v in part_rating_rgx.findall(line)
        })

    workflows_parsed = {}

    for line in workflows.split("\n"):
        accolade_idx = line.find("{")
        workflow_naming = line[:accolade_idx]

        rules = line[accolade_idx + 1:-1].split(",")
        default_case = rules[-1]
        rules = rules[:-1]
        rules_commands = []
        for rule in rules:
            parameter, op, value, result = rule_parser_rgx.findall(rule)[0]

            rules_commands.append((
                parameter,
                op,
                int(value),
                result
            ))

        workflows_parsed[workflow_naming] = {
            "commands": rules_commands,
            "default": default_case
        }

    result = None
    node = "in"
    s = 0

    for part in part_ratings_parsed:
        print("#######\n", "part", part)
        while True:
            if node == "A":
                print(part, "is accepted")
                s += part.get("x") + part.get("m") + part.get("a") + part.get("s")
                node = "in"
                break
            elif node == "R":
                print(part, "is rejected")
                node = "in"
                break

            commands = workflows_parsed[node].get("commands")
            default = workflows_parsed[node].get("default")

            for command in commands:
                parameter, op, value, next_node = command
                print(parameter, op, value, next_node)
                if op == "<":
                    if part.get(parameter) < value:
                        node = next_node
                        break
                else:
                    if part.get(parameter) > value:
                        node = next_node
                        break
            else:
                node = default

    print(s)
