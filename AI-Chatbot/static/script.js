const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");

// Send message when Enter is pressed
input.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

async function sendMessage() {

    const message = input.value.trim();

    if (message === "") return;

    // Add user message
    addMessage(message, "user");

    input.value = "";

    // Typing indicator
    const typing = document.createElement("div");
    typing.className = "bot-message";
    typing.id = "typing";
    typing.innerHTML = "Typing...";
    chatBox.appendChild(typing);

    scrollToBottom();

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        typing.remove();

        addMessage(data.response, "bot");

    } catch (error) {

        typing.remove();

        addMessage("Something went wrong. Please try again.", "bot");

        console.error(error);

    }

}

function addMessage(message, sender) {

    const div = document.createElement("div");

    div.className = sender === "user"
        ? "user-message"
        : "bot-message";

    div.innerHTML = message;

    chatBox.appendChild(div);

    scrollToBottom();

}

function scrollToBottom() {

    chatBox.scrollTop = chatBox.scrollHeight;

}