# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

So the game looked normal and that everything seemed to be working as needed. 
It showed the title, the guess box, and the buttons, so at first it seemed like everything was working.
Three bugs I found was that when I submitted the guess it would always say go lower even if the answer was higher than what I wrote. Another issue was that the debug behaved inconsistently, which made it difficult to tell if the guesses I tried in the  were being considered or not. Another bug was that once I won the game the submit button didn't work.
--- 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I used ChatGPT and Claude code as my main AI tools while working on this project.
One suggestion that was correct was when the AI pointed out that the issue might be related to how the secret number was being compared with the guess. After testing the code and checking the logic, I noticed that sometimes the secret number was being converted into a string, which caused the comparisons to behave incorrectly.
One suggestion that was misleading was when the AI initially suggested that the problem might be with the guess parsing function. After testing different inputs and printing values from the code, I realized the parsing was working correctly and the real issue was the type change in the secret number during certain attempts.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
To decide whether a bug was actually fixed, I both played the game manually and ran automated tests. I used the developer debug section while playing to check whether the secret number, guesses, and attempts matched what I expected after each guess. 
I also wrote pytest tests for the check_guess function to verify cases like winning guesses, guesses that were too high, and guesses that were too low. These tests helped confirm that the comparison logic between the guess and the secret number worked correctly. 
AI helped me understand what edge cases to test, such as checking that the hint direction was correct and making sure the game compared numbers as integers instead of strings.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
The secret number kept changing in the original app because Streamlit reruns the entire script every time the user interacts with the page. Each time I pressed the submit button, the code would run from the top again and sometimes reset values that were not properly stored. Because of that, the game logic did not always behave consistently.
I would explain Streamlit reruns to a friend like this. Every time you click a button or enter input, Streamlit refreshes the script and runs it again from the beginning. If you want something to stay the same between interactions, you have to store it in session state.
The change that gave the game a stable secret number was storing the number in st.session_state and only generating it once. That way the number stayed the same while the player kept guessing instead of changing every time the page reran.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One habit I want to reuse in future projects is writing small tests to check important parts of the code. Creating tests for functions like check_guess helped me quickly verify whether the logic worked correctly without relying only on manually playing the game. It also made it easier to catch mistakes when I changed the code.
One thing I would do differently next time when working with AI is double check its suggestions more carefully and test them right away. In this project, some of the AI suggestions were helpful, but others were not correct and needed verification.
This project changed how I think about AI generated code because I realized that AI can help explain ideas and suggest fixes, but the code still needs to be tested and understood by the developer. I learned that AI is more useful as a helper rather than something that always gives the correct answer.