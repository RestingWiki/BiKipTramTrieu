from typing import Optional, Dict


class LoadData:

    __POKE_DATA_SET: Optional[Dict[int, str]] = None

    def __new__(cls) -> Optional[Dict[int, str]]:
        """
        Overrides the __new__ method to ensure that only one instance of load_data2 is created.
        If the data set is not already loaded, it calls the __get_data method to load the data.

        :return: The instance of load_data2.
        """
        ...

    @classmethod
    def __get_data(cls) -> None:
        """
        Loads data from a CSV file and stores it in the __POKE_DATA_SET class variable.
        The CSV file is expected to be in the same directory as this script.

        :return: None
        """
        ...
