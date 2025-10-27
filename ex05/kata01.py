kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

def main():
    for value in kata:
        print(value, "was created by", kata[value])


if __name__=="__main__":
    main()
