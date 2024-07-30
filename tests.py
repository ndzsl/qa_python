from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        assert collector.get_books_genre() == {'Книга1': ''}

    def test_add_new_book_invalid_name(self):
        collector = BooksCollector()
        collector.add_new_book('Книга с очень длинным названием, которое превышает сорок символов')
        assert collector.get_books_genre() == {}

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга2', 'Фантастика')
        assert collector.get_book_genre('Книга2') == 'Фантастика'

    def test_set_book_genre_invalid_book(self):
        collector = BooksCollector()
        collector.set_book_genre('НеСуществующаяКнига', 'Фантастика')
        assert collector.get_book_genre('НеСуществующаяКнига') is None

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга3')
        collector.set_book_genre('Книга3', 'Неизвестный жанр')
        assert collector.get_book_genre('Книга3') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга4')
        collector.set_book_genre('Книга4', 'Ужасы')
        collector.add_new_book('Книга5')
        collector.set_book_genre('Книга5', 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Книга4']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга6')
        collector.set_book_genre('Книга6', 'Мультфильмы')
        collector.add_new_book('Книга7')
        collector.set_book_genre('Книга7', 'Ужасы')
        assert collector.get_books_for_children() == ['Книга6']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга8')
        collector.set_book_genre('Книга8', 'Комедии')
        collector.add_book_in_favorites('Книга8')
        assert collector.get_list_of_favorites_books() == ['Книга8']

    def test_add_book_in_favorites_invalid_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('НеСуществующаяКнига')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга9')
        collector.add_book_in_favorites('Книга9')
        collector.delete_book_from_favorites('Книга9')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_not_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга10')
        collector.delete_book_from_favorites('Книга10')
        assert collector.get_list_of_favorites_books() == []

