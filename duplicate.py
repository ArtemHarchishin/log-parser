log = []


def has_in(line):
    return "duplicate" in line or "Duplicate" in line


def parse(line):
    if not has_in(line):
        return False

    log.append(line)

    return True


def get_output():
    output = "=" * 80
    output += "\n\tDUPLICATE\n"
    output += "=" * 80 + "\n"
    if len(log) > 0:
        output += "\t" + "\t".join(log)
        output += "\n"
    return output
