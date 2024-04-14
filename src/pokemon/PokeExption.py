class NoPokeId(Exception):
    """Exception raised when a Pokémon ID is not found."""

    def __init__(self, _id: int):
        self.message = f'pokemon id {_id} not found'
        super().__init__(self.message)
