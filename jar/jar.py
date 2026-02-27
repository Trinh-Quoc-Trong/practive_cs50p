
class Jar:
    def __init__(self, _capacity = 12):
        self._capacity = _capacity
        self._size = 0
        if _capacity < 0:
            raise ValueError("Số lượng bánh có thể chứa không được âm")

    def __str__(self):
        # return f"{''.join("🍪" for _ in range(self._size))}"
        return "🍪" * self._size
    
    def deposit(self, n: int):
        if n + self._size > self._capacity:
            raise ValueError("Vượt quá sức chứa của hũ bánh!")
        
        self._size += n
    
    def withdraw(self, n: int):
        if self._size < n:
            raise ValueError("Vượt quá số bánh hiện có!")

        self._size -= n
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._size
        