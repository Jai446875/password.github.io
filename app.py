import streamlit as st

# HTML content with embedded CSS
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Streamlit HTML and CSS Example</title>
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #4CAF50;
            text-align: center;
            margin-top: 50px;
        }
        p {
            font-size: 18px;
            color: #333;
            text-align: center;
        }
        .custom-button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
        .custom-button:hover {
            background-color: #45a049;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Streamlit App</h1>
    <p>This is an example of how to use HTML and CSS in a Streamlit app.</p>
    <div class="container">
        <button class="custom-button" id="customButton">Click Me</button>
    </div>
</body>
</html>
"""

# Display the HTML and CSS in Streamlit using markdown
st.markdown(html_content, unsafe_allow_html=True)

# Adding Streamlit interactive button
if st.button("Click Me"):
    st.write("You clicked the Streamlit button!")
