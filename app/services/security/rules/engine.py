def capitalize(word):

    return word.capitalize()



def append_number(word, number="1"):

    return f"{word}{number}"



def append_year(word, year="2026"):

    return f"{word}{year}"



def apply_rules(
    word,
    rules
):

    results = [word]


    for rule in rules:

        new_results = []


        for item in results:

            if rule == "capitalize":
                new_results.append(
                    capitalize(item)
                )


            elif rule == "append_number":
                new_results.append(
                    append_number(item)
                )


            elif rule == "append_year":
                new_results.append(
                    append_year(item)
                )


        results.extend(new_results)


    return list(set(results))
