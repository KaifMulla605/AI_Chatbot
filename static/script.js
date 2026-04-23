async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();

    if (!message) return;

    addMessage("You", message, "user");
    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();
    addMessage("Bot", data.response, "bot");
}

function addMessage(sender, text, className) {
    const chatBox = document.getElementById("chat-box");
    const msg = document.createElement("div");
    msg.className = className;
    msg.textContent = `${sender}: ${text}`;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}
