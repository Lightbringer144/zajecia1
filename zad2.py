class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Library: {self.city}, {self.street}, {self.zip_code}\n' \
               f'Open hours: {self.open_hours}\nPhone: {self.phone}'


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Employee: {self.first_name} {self.last_name}\n' \
               f'Hire date: {self.hire_date}\nBirth date: {self.birth_date}\n' \
               f'Address: {self.city}, {self.street}, {self.zip_code}\nPhone: {self.phone}'


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Book: {self.author_name} {self.author_surname}\n' \
               f'Published: {self.publication_date}\nPages: {self.number_of_pages}\n' \
               f'Available at: {self.library}'


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = '\n'.join([f'\t{book}' for book in self.books])
        return f'Order Details:\n' \
               f'{self.employee}\n\nStudent: {self.student}\n' \
               f'Order Date: {self.order_date}\nBooks:\n{book_list}'


library1 = Library("Katowice", "Warszawska 1", "00-000", "9:00 - 17:00", "123-456-789")
library2 = Library("Krakow", "Zbigniewa Herberta 1", "00-000", "10:00 - 18:00", "987-654-321")

employee1 = Employee("Maja", "Kowalska", "2022-01-01", "1990-05-15", "Zabrze", "Wiejska", "00-000", "111-222-333")
employee2 = Employee("Jan", "Malczewski", "2020-07-11", "1985-08-20", "Gliwice", "Polna", "00-000", "444-555-666")
employee3 = Employee("Jakub", "Krawiec", "2021-03-07", "1995-03-10", "Ruda Slaska", "W. Pola", "00-000", "777-888-999")

book1 = Book(library1, "2020-01-01", "Ernest", "Hamingway", 200)
book2 = Book(library1, "2021-02-01", "Adam", "Mickiewicz", 250)
book3 = Book(library2, "2019-03-01", "George", "Orwell", 180)
book4 = Book(library2, "2020-04-01", "Wieslawa", "Szymborska", 300)
book5 = Book(library1, "2022-05-01", "Julian", "Slowacki", 150)

order1 = Order(employee1, "Linda Owalska", [book1, book3, book5], "2023-01-15")
order2 = Order(employee2, "Marcin Gumulka", [book2, book4], "2023-02-20")

print("\n====================\n")
print(order1)
print("\n====================\n")
print(order2)
