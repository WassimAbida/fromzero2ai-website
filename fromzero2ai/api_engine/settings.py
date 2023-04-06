"""FastApi app config module"""

import os
from typing import Dict, Optional, Union

from pydantic import BaseSettings, validator


class ApiSettings(BaseSettings):
    """Pydantic model for project variables.

    Use the env variables to define the non default ones.
    """
    class Config:
        env_file = ".env"


    API_NAME: str
    RESPONSE_TIMEOUT: int
    API_ROOT_URL: Union[str, None]
    API_SWAGGER_TITLE: Union[str, None]
    PYTHON_ENV: Union[str, None]

    @validator("API_ROOT_URL", pre=True)
    def assemble_root_url(cls, value: Optional[str], values: Dict[str, Union[str, int]]) -> str:
        """Build the root url of the api.

        :param value: _description_
        :param values: _description_
        :return: _description_
        """
        if isinstance(value, str):
            return value
        print("xxxxxx", values)
        api_root_url = os.path.join("/", values.get("API_NAME"))  # type: ignore

        print(api_root_url)
        return api_root_url

    @validator("API_SWAGGER_TITLE", pre=True)
    def assemble_api_swagger_title(cls, value: Optional[str], values: Dict[str, int]) -> str:
        """Build the default title of the swagger documentation

        :param value: _description_
        :param values: _description_
        :return: _description_
        """
        if isinstance(value, str):
            return value
        return f"{values.get('SERVICE_NAME')} Service"


settings = ApiSettings()
