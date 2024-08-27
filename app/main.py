class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str)\
            -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            print(
                f"Processing car: clean_mark={car.clean_mark}, "
                f" clean_power={self.clean_power}")
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                print(f"Price for car: {price}")
                income += price
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        print(f"Calculating price for car {car.brand}...")
        if car.clean_mark >= self.clean_power:
            print(
                f"Car is already clean enough: clean_mark={car.clean_mark}, "
                f" clean_power={self.clean_power}")
            return 0.0
        cost = (car.comfort_class * (self.clean_power - car.clean_mark)
                * self.average_rating / self.distance_from_city_center)
        print(f"Calculating price: comfort_class={car.comfort_class}, "
              f"clean_power={self.clean_power}, clean_mark={car.clean_mark}, "
              f"average_rating={self.average_rating}, "
              f"distance_from_city_center={self.distance_from_city_center}, "
              f"cost={cost}")
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        # Збільшити кількість оцінок на 1
        self.count_of_ratings += 1

        # Перерахувати новий середній рейтинг
        self.average_rating = round(
            (
                (self.average_rating * (self.count_of_ratings - 1) + rating)
                / self.count_of_ratings
            ), 1
        )


# # Створення автомобілів
# car1 = Car(comfort_class=3, clean_mark=4, brand="Toyota")
# car2 = Car(comfort_class=2, clean_mark=2, brand="Honda")
# car3 = Car(comfort_class=4, clean_mark=5, brand="BMW")
#
# # Створення станції миття
# car_wash = CarWashStation(
#     distance_from_city_center=10.0,
#     clean_power=4,
#     average_rating=4.5,
#     count_of_ratings=100
# )
#
# # Виконання миття автомобілів
# income = car_wash.serve_cars([car1, car2, car3])
#
# # Виведення результатів
# print(f"Income from car wash: {income}")
# print(f"Car1 clean mark after wash: {car1.clean_mark}")
# print(f"Car2 clean mark after wash: {car2.clean_mark}")
# print(f"Car3 clean mark after wash: {car3.clean_mark}")
