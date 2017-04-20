from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen('https://americanliterature.com/author/charles-dickens/short-story/the-childs-story') as story:
        story1 = []
        for line in story:
            story1.append(line.decode('utf-8'))
            # print(line.decode('utf-8'))

    print("##################")
    for line1 in story1:
        print(line1)