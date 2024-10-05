


def queryString(inputStr: str) -> dict:

    # Base case of "empty" string catch
    if not((len(inputStr) <= 1) and ("?" in inputStr)):
        output = {}
        # remove the question mark
        if inputStr.startswith("?"):
            inputStr = inputStr[1:]


        #split at &
        strList = inputStr.split("&")

        #for each remaining string split at = and then assing left for key and right for value
        for item in strList:
            finalSplit = item.split("=")
            output.update({finalSplit[0]: finalSplit[1]})

        #return the dict
        return output
    else:
        return {}


tests = ["", "?", "?a=b", "?a=b&c=d"]
for item in tests:
    print(queryString(item))