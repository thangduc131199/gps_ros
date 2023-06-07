import requests
import openai
OPENAI_API_KEY = "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"
# openai.api_key(OPENAI_API_KEY)



class ChatGPT:
    def __init__(self, api_key: str) -> None:
        """
        Constructer

        Parameters
        ----------
        api_key : str
            API key for OpenAI
        """
        openai.api_key = api_key

    def set_past_content(self, u_content: str, a_content: str) -> None:
        """
        Set the assistant content of message for the ChatGPT API.
        Parameters
        ----------
        u_content : str
            The prompt of the message to set for the past prompt.
        a_content : str
            The content of the message to set for the assistant.
        """
        assistant: dict = {"role": "assistant", "content": a_content}
        prompt: dict = {"role": "user", "content": u_content}
        self.past_content_list.append(prompt)
        self.past_content_list.append(assistant)
        diff_num: int = len(self.past_content_list) / 2 - self.num_hold_pass_res
        if diff_num > 0:
            for _ in range(diff_num):
                self.past_content_list.pop(0)
        self.set_past = True

    def set_system_content(self, content):
        """
        Set the system content of message for the ChatGPT API.

        Parameters
        ----------
        content : str
            The content of the message to set for the system.
        """
        self.role_system["content"] = content
        self.set_system = True

    def generate_text(self, prompt: str ):
        """
        Generates text response from ChatGPT API given a prompt.

        Parameters
        ----------
        prompt : str
            The prompt message to initiate the conversation with ChatGPT API.

        length : int, optional
            The maximum number of tokens to generate in the response message.
            Default is 50.

        Returns
        -------
        str
            The generated response text from ChatGPT API.

        Raises
        ------
        requests.exceptions.HTTPError
            If the request to ChatGPT API returns an error status code.
        """
        # Create the message structure for the GPT-3 model
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]

        # Try to send the request to the GPT-3 model and handle any exceptions
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
        except openai.error.InvalidRequestError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
        
        # Extract the GPT-3 model response from the returned JSON
        chatgpt_response = response.choices[0].message['content'].strip()
        #print(chatgpt_response)
        # Find the start and end indices of the JSON string in the response
        start_index = chatgpt_response.find('{')
        end_index = chatgpt_response.rfind('}') + 1
        # Extract the JSON string from the response
        json_response_dict = chatgpt_response[start_index:end_index]
        return chatgpt_response
