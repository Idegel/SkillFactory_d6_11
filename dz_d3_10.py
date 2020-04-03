from p_library.models import Author, Book

# books = Book.objects.all()

# max_price = books[0].price
# for book in books:
#     if book.price > max_price:
#         max_price = book.price
# print('Стоимость самой дорогой книги = {}'.format(max_price))

# min_price = books[0].price
# min_price_copy_count = 1
# for book in books:
#     if book.price < min_price:
#         min_price = book.price
#         min_price_copy_count = book.copy_count
# print('Число копий самой дешёвой книги = {}'.format(min_price_copy_count))

price_sorted = sorted(books, key=lambda x: x.price)
print('Число копий самой дешёвой книги = {}'.format(price_sorted[0].copy_count))
print('Стоимость самой дорогой книги = {}'.format(price_sorted[len(price_sorted) - 1].price))

authors = Author.objects.all()
sum_price = 0
for author in authors:
	books = Book.objects.filter(author=author)
	if books.count() > 1:
		for book in books:
			sum_price += book.price * book.copy_count
print('Стоимость всех книг авторов, у которых больше одной книги = {}'.format(sum_price))

authors = Author.objects.all().exclude(country='RU')
sum_price = 0
for author in authors:
	books = Book.objects.filter(author=author)
	for book in books:
		sum_price += book.price * book.copy_count
print('Стоимость книг иностранных писателей = {}'.format(sum_price))

pushkin = Author.objects.get(full_name="Пушкин Александр Сергеевич")
pushkin_books = Book.objects.filter(author=pushkin)
sum_prices = [book.price * book.copy_count for book in pushkin_books]
print('Стоимость всех экземпляров Пушкина в бибилотеке = {}'.format(sum(sum_prices)))

adams = Author.objects.get(full_name="Douglas Adams")
adams_books = Book.objects.filter(author=adams)
sum_prices = [book.price for book in adams_books]
print('Стоимость все книг, автор которых Douglas Adams = {}'.format(sum(sum_prices)))