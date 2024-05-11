from kink import inject
from langchain_community.llms import Ollama
from audio import Audio
from config import Config
from data import Data
from log import Logging
from models import Entity
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate


# anthropic_key = os.environ("ANTHROPIC_KEY")
# openai_key = os.environ("OPENAI_KEY")



@inject
class Llm:


    def __init__(self, config: Config, data: Data, logging: Logging, audio: Audio):
        self._config = config
        self._data = data
        self._logging = logging
        self._audio = audio

        if config.OFFLINE:
            self._llm = Ollama(model=config.LOCAL_OLLAMA_LLM)
        else:
            # We will include cloud based LLMs here in the future
            pass

    def processResponse(self, prompt: str) -> str:
        llmResponse = ""
        parser = JsonOutputParser()
        langchainPrompt = PromptTemplate(
            template= self._config.INSTRUCTIONS,
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        
        chain = langchainPrompt | self._llm | parser

        if prompt == "":
            self._logging.logInfo("Received empty input, skipping...")

        try:
            print("")
            for s in chain.invoke({"query": prompt}):
                self._logging.logLlm(s)
                llmResponse += s            

            print("")
        except Exception as e:
            self._logging.logError(f"Error during LLM response: {e}")
            return

        print(llmResponse)

