languages = {
    'python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

list = list(languages.keys())
for i in list:
    print(i, "was created by", languages[i])
