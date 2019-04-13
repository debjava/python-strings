def showStringBasics(strParam):
    val1 = len(strParam)
    print("Total length/characters : ", val1)  # 9
    b = "Hello, World!"
    print(b[2:5])  # llo, from position 2 to position 5 (not included).
    print("In upper case ", b.upper())
    print("In lower case ", b.lower())

    sentence = 'Python programming is fun.'
    result = sentence.index('is fun')
    print("Substring 'is fun':", result)


if __name__ == "__main__":
    showStringBasics("ABCD-pqrs")
