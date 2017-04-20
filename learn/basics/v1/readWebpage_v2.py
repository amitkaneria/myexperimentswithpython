from urllib.request import urlopen

if __name__ == "__main__":
    def words():
        with urlopen('https://americanliterature.com/author/charles-dickens/short-story/the-childs-story') as story:
            story1 = []
            for line in story:
                story1.append(line.decode('utf-8'))
                # print(line.decode('utf-8'))

        print(story1)

    print("##################")
    print(__name__)

    if __name__ == '__main__':
        words()