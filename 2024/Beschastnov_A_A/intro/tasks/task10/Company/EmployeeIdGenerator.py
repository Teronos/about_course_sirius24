class EmployeeIdGenerator:
    __current_id: int = 0

    def generate_id_for_user(self) -> int:
        self.__current_id += 1

        return self.__current_id