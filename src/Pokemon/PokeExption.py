class NoPokeId(Exception):
    """Exception raised when a Pokémon ID is not found."""

    def __init__(self, message="Pokemon ID not found."):
        self.message = message
        super().__init__(self.message)
