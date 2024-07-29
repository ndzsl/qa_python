from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:
    def test_add_new_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': ''}

    def test_add_new_book_invalid_name(self, collector):
        collector.add_new_book('B' * 41)  # Книга с именем длиной более 40 символов
        assert collector.get_books_genre() == {}

    def test_set_book_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Новый Жанр')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби']

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_new_book('Сказка о потерянном времени')
        collector.set_book_genre('Сказка о потерянном времени', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби', 'Сказка о потерянном времени']

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_duplicate(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_non_existing_book_from_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Не существует книги')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    @pytest.mark.parametrize(
        "book_name, genre, expected_result",
        [
            ('Гордость и предубеждение и зомби', 'Фантастика', 'Фантастика'),
            ('Что делать, если ваш кот хочет вас убить', 'Ужасы', 'Ужасы'),
            ('Сказка о потерянном времени', 'Мультфильмы', 'Мультфильмы')
        ]
    )
    def test_set_and_get_book_genre(self, collector, book_name, genre, expected_result):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_result
