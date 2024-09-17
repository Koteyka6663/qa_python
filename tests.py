import pytest

class TestBooksCollector:

    def test_add_new_book_add_one_book(self, collector):

        collector.add_new_book('Снафф')
        assert len(collector.books_genre) == 1

    def test_add_new_book_genre_is_empty(self, collector):

        collector.add_new_book('Снафф')
        assert collector.books_genre.get('Снафф') == ''

    def test_set_book_genre_set_genre(self, collector):

        collector.add_new_book('Хребты безумия')
        collector.set_book_genre('Хребты безумия', 'Ужасы')
        assert collector.books_genre.get('Хребты безумия') is not None


    def test_get_book_genre_get_genre(self, collector):

        collector.add_new_book('Хребты безумия')
        collector.set_book_genre('Хребты безумия', 'Ужасы')
        assert collector.get_book_genre('Хребты безумия') == 'Ужасы'

    def test_get_books_with_specific_genre_get_book(self, collector):

        collector.add_new_book("Дюк, Виски и Малой")
        collector.set_book_genre("Дюк, Виски и Малой", "Комедии")
        book_list = collector.get_books_with_specific_genre("Комедии")
        assert "Дюк, Виски и Малой" in book_list

    def test_get_books_for_children_add_book_in_list(self, collector):

        collector.add_new_book("Дюк, Виски и Малой")
        collector.set_book_genre("Дюк, Виски и Малой", "Комедии")
        book_not_for_children = collector.get_books_for_children()
        assert len(book_not_for_children) == 1

    @pytest.mark.parametrize("name,genre",
                             [
                                 ("Дюк, Виски и Малой", "Комедии"),
                                 ("Хребты безумия", "Ужасы")
                             ]
                             )
    def test_get_books_for_children_book_horror_do_not_add_in_list(self, collector, name, genre):

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        book_for_children = collector.get_books_for_children()
        assert "Хребты безумия" not in book_for_children

    def test_add_book_in_favorites_add_one_book(self, collector):

        collector.add_new_book("Дюк, Виски и Малой")
        collector.add_book_in_favorites("Дюк, Виски и Малой")
        assert"Дюк, Виски и Малой" in collector.favorites

    def test_delete_book_from_favorites(self, collector):

        collector.add_new_book("Дюк, Виски и Малой")
        collector.add_book_in_favorites("Дюк, Виски и Малой")
        collector.delete_book_from_favorites("Дюк, Виски и Малой")
        assert "Дюк, Виски и Малой" not in collector.favorites


    def test_get_list_of_favorites_books_is_list(self, collector):

        fav_books = collector.get_list_of_favorites_books()
        assert isinstance(fav_books, list)