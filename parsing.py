import requests

print("Результат задания №1:")

response = requests.get("https://openlibrary.org/search.json?q=harry+potter")
data = response.json()
if data["docs"]:
    print(f"Первая книга: {data['docs'][0]['title']}")

print("\nРезультат задания №2:")
search_query = "the+witcher"
new_response = requests.get(f"https://openlibrary.org/search.json?q={search_query}")
new_data = new_response.json()


print("\nРезультат задания №3 (информация о новой книге):")
if new_data['docs']:
    book = new_data['docs'][0]
    title = book.get('title', 'Нет названия')
    author = book.get('author_name', ['Автор не указан'])[0]
    year = book.get('first_publish_year', 'Год неизвестен')
    pages = book.get("number_of_pages_median", 'Кол-во страниц не указано')

    print(f"Название: {title}")
    print(f"Автор: {author}")
    print(f"Год первой публикации: {year}")
    print(f"Примерное кол-во страниц: {pages}")
else:
    print("Книга не найдена")
