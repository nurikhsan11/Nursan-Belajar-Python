# Program konsonan

def delVowel(inp):
    vocal = ['a','i','u','e','o', ' ']
    outp = ""

    for ini in inp:
        if ini.lower() not in vocal:
            outp += ini
    return outp
print(delVowel("Nurul Fikri"))