class Movies:
    def __init__(self, title, release, rating):
        self.title = title
        self.release = release
        self.rating = rating


    def get_info_movies(self,):
        return self.title + "was released in" + self.release + "and currently has a score of" + self.rating

inception = Movies("inception", "2010", "8.8")
the_martian = Movies("the martian", "2015","8.0")
joker = Movies("joker", "2019", "8.4")

print(f"{inception.title} was released in {inception.release} and currently has a score of {inception.rating}")
print(f"{the_martian.title} was released in {the_martian.release} and currently has a score of {the_martian.rating}")
print(f"{joker.title} was released in {joker.release} and currently has a score of {joker.rating}")

print()

print(f"{inception.get_info_movies()}")
print(f"{the_martian.get_info_movies()}")
print(f"{joker.get_info_movies()}")