
from llama_index.llms.ollama import Ollama
llm = Ollama(model="llama2",base_url="http://localhost:11434",request_timeout=300)
response= llm.complete("what is supersonic engine")
print(response)
