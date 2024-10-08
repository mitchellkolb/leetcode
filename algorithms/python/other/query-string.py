
"""
input : "?foo=hello&other=world"

output: {
    foo: "hello",
    other: "world"
}
"""


"""
    Assumptions:
- Query String can be empty but will always have a ? at the start.
- string items are always seperated with &
- string items are always two parts seperated with a =
- chars & and = can't be in the contents of the string only as seperators for key value pairs

    Test:
"?"
"?a=b&c=d"
"?a=b"

"""

"""
This question is from a mock software interview that you can find at this link to view and watch
https://youtu.be/7CWM-jLowpk?si=DO9DsTpmiZxIGFGx

In this interview you can see that I've compelted the question slightly differently but I would say that I did it will some more considerations in mind

"""



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



#Testing the made up function with an adjustable list of strings
tests = ["", "?", "?a=b", "?a=b&c=d"]
for item in tests:
    print(queryString(item))