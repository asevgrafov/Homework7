class OrderStatusInvalidStateException(Exception):

    def __init__(self, message: str = "Невозможно перевести в данный статус") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f'{self.message}'


class OrderStatus:

    def __init__(self, status: str) -> None:
        if status == "new" or status == "in_progress" or status == "done":
            self.status = status
        else:
            raise OrderStatusInvalidStateException

    def change_to_state(self, status: str) -> None:
        if self.status == status:
            return
        if self.status == "new":
            if status == "in_progress":
                self.status = status
            else:
                raise OrderStatusInvalidStateException
        elif self.status == "in_progress":
            if status == "done":
                self.status = status
            else:
                raise OrderStatusInvalidStateException
        else:
            raise OrderStatusInvalidStateException
