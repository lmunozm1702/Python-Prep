class Operaciones:
    def __init__(self, lista):
        self.lista = lista

    def factorial(self):
        for i in self.lista:
            if type(i) != int:
                print('sólo se deben ingresar numeros enteros')
                break
            return self.__factorial(i)
        
    def __factorial(self, number):
        if number < 0 or type(number) != int:
            return 'Invalid number must be an integer greater than 0'
        if number == 0:
            return 1
        return number * self.__factorial(number-1)
    
    def convert_temperatures(self):
        for i in self.lista:
            if type(i[0]) != int or type(i[1]) != str or type(i[2]) != str:
                print('el primer valor debe ser un numero entero, los siguientes dos valores deben ser strings')
                break
            return self.__convert_temperatures(i[0], i[1], i[2])
    
    def __convert_temperatures(self, temperature, unit_from, unit_to):
        if unit_from == 'C':
            if unit_to == 'F':
                return temperature * 9/5 + 32
            elif unit_to == 'K':
                return temperature + 273.15
            else:
                return temperature
        elif unit_from == 'F':
            if unit_to == 'C':
                return (temperature - 32) * 5/9
            elif unit_to == 'K':
                return (temperature - 32) * 5/9 + 273.15
            else:
                return temperature
        elif unit_from == 'K':
            if unit_to == 'C':
                return temperature - 273.15
            elif unit_to == 'F':
                return (temperature - 273.15) * 9/5 + 32
            else:
                return temperature
        else:
            return temperature
        
    def is_prime_number(self):
        result_list = []
        for i in self.lista:
            if type(i) != int:
                print('sólo se deben ingresar numeros enteros')
                break
            result_list.append(self.__is_prime_number(i))
        return result_list

    def __is_prime_number(self, number):
        if number == 1:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    
    def get_most_common_number(self):
        for i in self.lista:
            return self.__get_most_common_number(i)

    def __get_most_common_number(self, numbers):
        number_dict = {}
        for number in numbers:
            if number in number_dict:
                number_dict[number] += 1
            else:
                number_dict[number] = 1
        return max(number_dict, key=number_dict.get)
    